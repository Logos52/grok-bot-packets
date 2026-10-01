import sys,re,json,urllib.request
id=sys.argv[1]
req=urllib.request.Request("https://apps.apple.com/us/app/id"+id,headers={'User-Agent':'Mozilla/5.0'})
h=urllib.request.urlopen(req).read().decode()
m=re.search(r'<script type="application/json" id="serialized-server-data">(.*?)</script>',h,re.S)
s=m.group(1)
d=json.loads(s)
def walk(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in('deviceFamilies','supportedDevices','requiredDeviceCapabilities') : print(k,v)
            walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
iap=re.findall(r'"title":"([^"]+)","text":"([^"]*)"',s)
t=[x for x in re.findall(r'"(?:title|text|textPair)":\s*\[?"[^"]*\$[0-9.]+[^"]*"',s)][:15]
print(t)
print('watchmentions', len(re.findall('Apple Watch',s)))
