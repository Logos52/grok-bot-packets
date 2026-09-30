import json,subprocess,sys
# usage: dl.py json prefix names...
f,prefix=sys.argv[1],sys.argv[2]
d=json.load(open(f))
seen=set();sel=[]
for x in d:
    if x['name'] in seen: continue
    seen.add(x['name']); sel.append(x)
for i,x in enumerate(sel[:int(sys.argv[3])]):
    for j,u in enumerate(x['images'][:1]):
        if not u: continue
        subprocess.run(['curl','-sL','-m','40','-A','Mozilla/5.0','-o',f"/workspace/machismo-imgs/{prefix}_{i:02d}_{j}.jpg",u])
    print(i,x['name'])
