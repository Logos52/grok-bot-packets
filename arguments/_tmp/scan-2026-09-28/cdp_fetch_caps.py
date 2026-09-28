import json, urllib.request, time, re
from pathlib import Path
import websocket

raw = Path('/workspace/arguments/_raw')
ids = ['62lPuJ5ZhA8', 'TLJNJDf2XGo', 'f1FGsTGp6K0', 'CMwy7atVcQY']

def fmt_ts(ms):
    total_s = ms // 1000
    h, rem = divmod(total_s, 3600)
    m, s = divmod(rem, 60)
    return f"[{h}:{m:02d}:{s:02d}]" if h else f"[{m:02d}:{s:02d}]"

def json3_to_lines(data):
    lines = []
    for ev in data.get('events') or []:
        segs = ev.get('segs')
        if not segs:
            continue
        t = ev.get('tStartMs', 0)
        text = ''.join(s.get('utf8', '') for s in segs).replace('\n', ' ').strip()
        if text:
            lines.append(f"{fmt_ts(t)} {text}")
    return lines

def cdp_call(ws, method, params=None, id=1):
    msg = {'id': id, 'method': method}
    if params:
        msg['params'] = params
    ws.send(json.dumps(msg))
    while True:
        resp = json.loads(ws.recv())
        if resp.get('id') == id:
            return resp

# Create a dedicated page target
new = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:9222/json/new?about:blank', method='PUT')))
ws_url = new['webSocketDebuggerUrl']
print('page', new.get('id'), ws_url)
ws = websocket.create_connection(ws_url, timeout=90)
cdp_call(ws, 'Page.enable', id=1)
cdp_call(ws, 'Runtime.enable', id=2)

for i, vid in enumerate(ids):
    print('===', vid, flush=True)
    cdp_call(ws, 'Page.navigate', {'url': f'https://www.youtube.com/watch?v={vid}'}, id=10 + i)
    # wait for load
    time.sleep(8)
    expr = '''
    (async () => {
      const html = document.documentElement.innerHTML;
      let m = html.match(/ytInitialPlayerResponse\\s*=\\s*(\\{.+?\\});/);
      if (!m) return {err:'no player', htmlLen: html.length};
      let d; try { d = JSON.parse(m[1]); } catch(e) { return {err:'parse '+String(e)}; }
      const tracks = (((d.captions||{}).playerCaptionsTracklistRenderer||{}).captionTracks)||[];
      let en = tracks.filter(t => (t.languageCode||'').startsWith('en'));
      if (!en.length) return {err:'no en', play: (d.playabilityStatus||{}).status, reason:(d.playabilityStatus||{}).reason, n:tracks.length, title:(d.videoDetails||{}).title};
      let t = en.find(x => x.kind !== 'asr') || en[0];
      let url = t.baseUrl;
      if (!url.includes('fmt=')) url += '&fmt=json3'; else url = url.replace(/fmt=[^&]+/, 'fmt=json3');
      const r = await fetch(url);
      const text = await r.text();
      return {status:r.status, len:text.length, kind:t.kind, lang:t.languageCode, body:text, title:(d.videoDetails||{}).title, upload:(((d.microformat||{}).playerMicroformatRenderer)||{}).uploadDate, lengthSeconds:(d.videoDetails||{}).lengthSeconds};
    })()
    '''
    resp = cdp_call(ws, 'Runtime.evaluate', {'expression': expr, 'awaitPromise': True, 'returnByValue': True}, id=100 + i)
    val = ((resp.get('result') or {}).get('result') or {}).get('value')
    if not val:
        print(' no val', json.dumps(resp)[:400], flush=True)
        continue
    if val.get('err'):
        print(' err', val, flush=True)
        continue
    print(' status', val.get('status'), 'len', val.get('len'), 'title', (val.get('title') or '')[:70], flush=True)
    body = val.get('body') or ''
    if val.get('status') == 200 and len(body) > 1000:
        (raw / f'{vid}.en.json3').write_text(body)
        data = json.loads(body)
        lines = json3_to_lines(data)
        (raw / f'{vid}.en.txt').write_text('\n'.join(lines) + '\n')
        meta = {'id': vid, 'title': val.get('title'), 'uploadDate': val.get('upload'), 'lengthSeconds': val.get('lengthSeconds'), 'kind': val.get('kind'), 'lang': val.get('lang'), 'n': len(lines)}
        (raw / f'{vid}.info.mini.json').write_text(json.dumps(meta, indent=2))
        print(' SAVED', len(lines), 'lines', flush=True)
    else:
        print(' body head', body[:200], flush=True)
    time.sleep(4)

ws.close()
print('done')
for vid in ids:
    p = raw / f'{vid}.en.txt'
    print(vid, 'OK' if p.exists() else 'MISSING', p.stat().st_size if p.exists() else 0)
