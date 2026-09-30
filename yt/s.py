import sys,json,subprocess
chs=['Wanhee','Samurai Matcha','大山','ミニマリストしぶ','干場義雅','MKBHD','Marques Brownlee']
q=sys.argv[1]
out=subprocess.run(['yt-dlp','--flat-playlist','--dump-json',f'ytsearch15:{q}'],capture_output=True,text=True).stdout
for l in out.splitlines():
    try:d=json.loads(l)
    except: continue
    c=d.get('channel') or ''
    if any(x in c for x in chs): print('***',end='')
    print(d['title'][:90],'|',c,'|',d['id'])
