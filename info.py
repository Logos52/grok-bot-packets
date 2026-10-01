import sys,re,json,urllib.request
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})).read().decode()
for id in sys.argv[1:]:
    us=json.loads(get("https://itunes.apple.com/lookup?id=%s&country=us"%id))['results']
    vn=json.loads(get("https://itunes.apple.com/lookup?id=%s&country=vn"%id))['results']
    r=us[0]
    print("=====",r['trackName'],id,'US %.2f/%d'%(r['averageUserRating'],r['userRatingCount']),r['formattedPrice'],'| VN store:', ('YES '+vn[0]['formattedPrice']) if vn else 'NOT FOUND', '| watchdev', [x for x in r['supportedDevices'] if 'Watch' in x][:2])
    h=get("https://apps.apple.com/us/app/id"+id)
    s=re.search(r'id="serialized-server-data">(.*?)</script>',h,re.S).group(1)
    pairs=re.findall(r'"leadingText":"([^"]+)","trailingText":"([^"]+)"',s)
    seen=[]
    for p in pairs:
        if p not in seen: seen.append(p)
    print(' IAP:',seen[:12])
    desc=r['description']
    for sent in re.split(r'(?<=[.!\n])\s+',desc):
        if re.search(r'watch|premium|pro\b|free|subscri|complicat',sent,re.I): print('  -',sent[:220].replace('\n',' '))
