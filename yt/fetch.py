import sys,json,subprocess
from youtube_transcript_api import YouTubeTranscriptApi
api=YouTubeTranscriptApi()
def get(vid):
    try:
        tl=api.list(vid)
        langs=[t.language_code for t in tl]
        for pref in (['en'],['ja'],['zh-TW','zh-Hant','zh'],['ko']):
            try:
                t=tl.find_transcript(pref).fetch()
                return ' '.join(s.text for s in t)
            except Exception: pass
        t=next(iter(tl)).fetch()
        return ' '.join(s.text for s in t)
    except Exception as e:
        return None
for vid in sys.argv[1:]:
    t=get(vid)
    if t: open(vid+'.txt','w').write(t); print(vid,len(t))
    else: print(vid,'NO TRANSCRIPT')
