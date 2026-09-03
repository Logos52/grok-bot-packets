import re, json
from datetime import datetime, timezone

# --- WoW ---
html=open('/workspace/table-fetch/wow-news.html',encoding='utf-8',errors='ignore').read()
scripts=re.findall(r'<script[^>]*>(.*?)</script>', html, re.S|re.I)
best=None
for s in scripts:
    if '"blogList"' in s and 'Hotfixes: September 1' in s:
        best=s; break
m=re.search(r'"blogList"\s*:\s*\{\s*"blogs"\s*:\s*(\[)', best)
start=m.start(1)
depth=0; end=None
for j,ch in enumerate(best[start:], start):
    if ch=='[': depth+=1
    elif ch==']':
        depth-=1
        if depth==0:
            end=j+1; break
arr=best[start:end]
objs=[]; depth=0; cur=None
for j,ch in enumerate(arr):
    if ch=='{':
        if depth==0: cur=j
        depth+=1
    elif ch=='}':
        depth-=1
        if depth==0 and cur is not None:
            objs.append(arr[cur:j+1]); cur=None

wow=[]
for obj in objs:
    title_m=re.search(r'"title"\s*:\s*"((?:\\.|[^"\\])*)"', obj)
    url_m=re.search(r'"url"\s*:\s*"((?:\\.|[^"\\])*)"', obj)
    pub_m=re.search(r'"published"\s*:\s*"([^"]+)"', obj)
    if not title_m or not url_m: continue
    title=title_m.group(1)
    try:
        title=bytes(title,'utf-8').decode('unicode_escape')
    except Exception:
        pass
    # fix mojibake from latin1-ish
    title=title.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2122','')
    pub=pub_m.group(1)[:10] if pub_m else None
    # Prefer date in title for hotfixes like "Hotfixes: September 1, 2026"
    tm=re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s*(20\d{2})', title)
    if tm:
        months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
        article_date=f"{tm.group(3)}-{months[tm.group(1)]:02d}-{int(tm.group(2)):02d}"
    else:
        article_date=pub
    url='https://worldofwarcraft.blizzard.com/en-us'+url_m.group(1)
    wow.append({'game':'wow','headline':title.strip(),'date':article_date,'published':pub,'url':url})

print('WOW', len(wow))
for w in wow[:12]:
    print(json.dumps(w, ensure_ascii=False))

# --- FFXIV ---
def parse_ffxiv(path):
    html=open(path,encoding='utf-8',errors='ignore').read()
    pattern=re.compile(r"document\.getElementById\('datetime-([^']+)'\)\.innerHTML = ldst_strftime\((\d+), 'YMD'\);")
    items=[]
    for m in pattern.finditer(html):
        epoch=int(m.group(2))
        dt=datetime.fromtimestamp(epoch, tz=timezone.utc).strftime('%Y-%m-%d')
        start=max(0, m.start()-900)
        prev=html[start:m.start()]
        hrefs=re.findall(r'href="(/lodestone/(?:news|topics)/detail/[a-f0-9]+)"', prev)
        href=hrefs[-1] if hrefs else None
        clean=re.sub(r'<script[^>]*>.*?</script>','', prev, flags=re.S)
        texts=re.findall(r'>([^<]{5,220})<', clean)
        title=None
        skip={'-', 'News', 'Topics', 'Notices', 'Maintenance', 'Updates', 'Status', 'Latest', '[Important]', '[Recovery]', '[Follow-up]', '[Chaos]', '[Materia]', '[Dynamis]', '[Crystal]'}
        for t in reversed(texts):
            t=re.sub(r'\s+',' ',t.strip())
            if not t or t in skip: continue
            if 'getElementById' in t or 'ldst_' in t: continue
            if re.match(r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}$', t): continue
            if t.startswith('Page '): continue
            # rebuild recovery titles if fragments
            title=t
            break
        # Try richer title from nearby HTML including bracket tags
        richer=re.sub(r'<script[^>]*>.*?</script>','', prev, flags=re.S)
        richer=re.sub(r'<br\s*/?>',' ', richer, flags=re.I)
        # pull last anchor text or headline-like block
        anch=re.findall(r'<a[^>]+href="(/lodestone/(?:news|topics)/detail/[a-f0-9]+)"[^>]*>(.*?)</a>', richer, re.S)
        if anch:
            href2, raw = anch[-1]
            href=href2
            raw=re.sub(r'<[^>]+>',' ', raw)
            raw=re.sub(r'\s+',' ', raw).strip()
            if raw: title=raw
        items.append({'date':dt,'headline':title,'path':href,'epoch':epoch})
    # dedupe by path
    seen=set(); out=[]
    for it in items:
        key=it['path'] or (it['headline'], it['date'])
        if key in seen: continue
        seen.add(key); out.append(it)
    return out

news=parse_ffxiv('/workspace/table-fetch/ffxiv-news.html')
topics=parse_ffxiv('/workspace/table-fetch/ffxiv-topics.html')
print('NEWS', len(news))
for n in news[:20]:
    print(json.dumps(n, ensure_ascii=False))
print('TOPICS', len(topics))
for n in topics[:15]:
    print(json.dumps(n, ensure_ascii=False))

open('/workspace/table-fetch/parsed.json','w').write(json.dumps({'wow':wow,'ffxiv_news':news,'ffxiv_topics':topics}, indent=2, ensure_ascii=False))
print('wrote parsed.json')
