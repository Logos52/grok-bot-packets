import sys,json,urllib.request,urllib.parse
def s(q,n=6):
    u='https://tiki.vn/api/v2/products?limit=%d&q=%s'%(n,urllib.parse.quote(q))
    r=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
    try:
        d=json.load(urllib.request.urlopen(r,timeout=20))
    except Exception as e:
        print(q,'ERR',e);return
    print('##',q)
    for p in d.get('data',[]):
        print(' %s | %s | %s | %s'%(p['name'][:90],p['price'],p.get('seller_name'),p.get('rating_average')),'| https://tiki.vn/'+p['url_path'][:60])
for q in sys.argv[1:]: s(q)
