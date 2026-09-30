import re,json,sys,subprocess,html
def get(u):
    return subprocess.run(['curl','-sL','-m','30','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
u=sys.argv[1]
s=get(u)
print(len(s), re.findall(r'<title>([^<]*)',s)[:1])
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
    try:
        j=json.loads(m.group(1))
        js=j if isinstance(j,list) else [j]
        for j in js:
            if j.get('@type')=='Product':
                print(json.dumps(j,ensure_ascii=False)[:1800])
    except Exception as e: pass
