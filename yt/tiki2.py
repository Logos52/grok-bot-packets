import sys,json,urllib.request,urllib.parse,time
def s(q,n=5):
    for t in range(3):
        u='https://tiki.vn/api/v2/products?limit=%d&q=%s'%(n,urllib.parse.quote(q))
        r=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Accept':'application/json'})
        try:
            d=json.load(urllib.request.urlopen(r,timeout=20));break
        except Exception as e:
            d=None;time.sleep(4)
    if d is None: print('##',q,'ERR');return
    print('##',q)
    for p in d.get('data',[]):
        print(' %s | %s | %s'%(p['name'][:80],p['price'],p.get('seller_name')))
for q in sys.argv[1:]:
    s(q);time.sleep(2)
