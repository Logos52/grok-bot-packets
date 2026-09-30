import json,sys,subprocess,re
base=sys.argv[1]; out=[]
for p in range(1,4):
    r=subprocess.run(['curl','-sL','-m','30','-A','Mozilla/5.0',f'{base}/products.json?limit=250&page={p}'],capture_output=True,text=True).stdout
    try: d=json.loads(r)['products']
    except Exception as e: print('fail',p,r[:100]); break
    if not d: break
    out+=d
print(len(out))
res=[]
for x in out:
    v=x['variants'][0]
    res.append(dict(title=x['title'],type=x.get('product_type'),price=v['price'],url=f"{base}/products/{x['handle']}",img=(x['images'][0]['src'] if x['images'] else None),body=re.sub(r'<[^>]+>',' ',x.get('body_html') or '')[:500],tags=x.get('tags')))
json.dump(res,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
for r in res: print(r['price'],r['title'],'|',r['url'])
