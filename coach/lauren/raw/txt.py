import re,html,sys
for f in sys.argv[1:]:
    t=open(f,errors='ignore').read()
    t=re.sub(r'<(script|style|svg|nav|footer)[\s\S]*?</\1>','',t)
    t=re.sub(r'<br\s*/?>','\n',t)
    p=html.unescape(re.sub(r'<[^>]+>','\n',t)); p=re.sub(r'[ \t]+',' ',p); p=re.sub(r'\n\s*\n+','\n',p)
    open(f.rsplit('.',1)[0]+'.txt','w').write(p)
