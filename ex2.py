import re,sys,html,base64
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
a=sys.argv[1]
h=open(a+'.html',errors='ignore').read()
print('=====',a,'| title:',clean(re.findall(r'id="productTitle"[^>]*>(.*?)</span>',h,re.S)[0])[:170])
m=re.search(r'id="corePrice_feature_div".*?a-offscreen">\s*([^<]+)<',h,re.S) or re.search(r'id="corePrice_desktop".*?a-offscreen">\s*([^<]+)<',h,re.S)
print('price',m.group(1) if m else re.findall(r'a-offscreen">\s*(\$[\d.,]+)',h)[:3],'| list',re.findall(r'List Price:.{0,80}',clean(h))[:1])
print('rating',re.findall(r'acrPopover[^>]*title="([^"]+)"',h)[:1],re.findall(r'acrCustomerReviewText[^>]*>([^<]+)<',h)[:1],'| stock',re.findall(r'Currently unavailable|In Stock|Only \d+ left',h)[:1])
for k in ['Sold by','Ships from']:
    m=re.search(k+r'.{0,700}?offer-display-feature-text-message[^>]*>(.*?)</span>',h,re.S); print(k,clean(m.group(1)) if m else None)
m=re.search(r'id="feature-bullets".*?</ul>',h,re.S); print(clean(m.group(0))[:3800] if m else None)
for k in ['Item Weight','Product Dimensions','Item Dimensions LxWxH','Maximum Weight Recommendation','Warranty Type','Included Components','Color','Style','Model Number','Item Package Dimensions L x W x H','Package Weight','Date First Available']:
    m=re.search(k+r'\s*</th>\s*<td[^>]*>(.*?)</td>',h,re.S); print(' ',k,':',clean(m.group(1))[:110] if m else None)
i=h.find('Customers say'); s=h[i:i+30000]
for b in re.findall(r'k\+b64 ([A-Za-z0-9+/=]+)',s)[:1]:
    d=base64.b64decode(b+'='*(-len(b)%4)).decode(errors='ignore'); print('CS:',re.findall(r'inertText":"(.*?)"',d))
