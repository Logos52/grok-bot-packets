import re,sys,html
h=open(sys.argv[1]+'.html',errors='ignore').read()
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
t=re.search(r'id="productTitle"[^>]*>(.*?)</span>',h,re.S); print('T:',clean(t.group(1))[:140] if t else None)
m=re.search(r'id="corePrice_feature_div".*?a-offscreen">\s*([^<]+)<',h,re.S) or re.search(r'id="corePriceDisplay_desktop_feature_div".*?a-offscreen">\s*([^<]+)<',h,re.S); print('P:',m.group(1) if m else None)
for k in ['acrPopover','acrCustomerReviewText']:
    m=re.search(k+r'[^>]*?(?:title="([^"]+)"|>([^<]+)<)',h); print(k,m.groups() if m else None)
m=re.search(r'id="feature-bullets".*?</ul>',h,re.S); print('B:',clean(m.group(0))[:900] if m else None)
for k in ['Item Weight','Product Dimensions','Maximum Weight Recommendation','Date First Available','Material']:
    m=re.search(k+r'\s*</th>\s*<td[^>]*>(.*?)</td>',h,re.S); print(k,clean(m.group(1))[:100] if m else None)
m=re.search(r'Customers say.{0,1500}',h,re.S); print('CS:',clean(m.group(0))[:900] if m else None)
for k in ['Sold by','Ships from']:
    m=re.search(k+r'.{0,600}?offer-display-feature-text-message[^>]*>(.*?)</span>',h,re.S); print(k,clean(m.group(1)) if m else None)
print('return:',re.findall(r'(\d+-day[^<]{0,50}(?:return|refund)[^<]{0,30})',h,re.I)[:2])
