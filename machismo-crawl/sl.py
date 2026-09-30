import re,json,sys,subprocess,time
def get(u):
    return subprocess.run(['curl','-sL','-m','30','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
def crawl(base,pages=4,maxn=60):
    links=[]
    for p in range(1,pages+1):
        s=get(f"{base}/products?page={p}")
        l=[x for x in dict.fromkeys(re.findall(r'href="(/products/[A-Za-z0-9_%.-]+)"',s)) if 'item' not in x]
        new=[x for x in l if x not in links]
        if not new: break
        links+=new
    out=[]
    for l in links[:maxn]:
        s=get(base+l)
        d=None
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
            try:
                j=json.loads(m.group(1))
                if j.get('@type')=='Product': d=j
            except: pass
        if d:
            off=d['offers']; off=off[0] if isinstance(off,list) else off
            out.append(dict(url=base+l,name=d['name'],price=off.get('price'),cur=off.get('priceCurrency'),desc=re.sub(r'\s+',' ',d.get('description',''))[:700],images=d.get('image',[])[:3] if isinstance(d.get('image'),list) else [d.get('image')]))
        time.sleep(0.5)
    return out
if __name__=='__main__':
    o=crawl(sys.argv[1]); json.dump(o,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
    for x in o: print(x['price'],x['name'],x['url'])
