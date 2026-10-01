import json,sys,urllib.parse,urllib.request
def get(u):
    return json.load(urllib.request.urlopen(u))
for t in sys.argv[1:]:
    try:
        d=get("https://itunes.apple.com/search?term=%s&entity=software&country=us&limit=3"%urllib.parse.quote(t))
    except Exception as e:
        print(t,'ERR',e);continue
    print("==",t)
    for r in d['results'][:3]:
        w=any('Watch' in x for x in r['supportedDevices'])
        print(' ',r['trackName'][:50],'|',r['trackId'],'|%.2f'%r.get('averageUserRating',0),r.get('userRatingCount'),r['formattedPrice'],'watch=',w,'|',r['sellerName'],'|iOS',r['minimumOsVersion'])
