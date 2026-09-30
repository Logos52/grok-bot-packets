import re,html,glob,json
from html.parser import HTMLParser
files=['p0.html']+[f'page{i}.html' for i in range(1,8)]
out=[]
for f in files:
    t=open(f,errors='ignore').read()
    if f=='p0.html':
        i=t.find('id="item-box"'); t=t[i:] if i>0 else t
    # strip scripts/styles
    t=re.sub(r'<(script|style)[\s\S]*?</\1>','',t)
    # split on per-tweet blocks by status links
    parts=re.split(r'(?=lauren&nbsp;Reposted|(?<=\n)\s*lauren\s*\n\s*@poteto)',t)
    out.append(t)
txt='\n'.join(out)
txt=re.sub(r'<br\s*/?>','\n',txt)
# capture links to status
links=re.findall(r'href="https://twiscan.com/en/x/([A-Za-z0-9_]+)/(\d+)"',txt)
print(len(links),len(set(links)))
plain=re.sub(r'<[^>]+>','\n',txt); plain=html.unescape(plain)
plain=re.sub(r'\n\s*\n+','\n',plain)
open('all.txt','w').write(plain)
print(len(plain))
