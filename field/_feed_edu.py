import json
from datetime import datetime
with open("/workspace/field/scratch-2026-09-06-feed.json") as f:
    d = json.load(f)
print("generated_at", d["generated_at"], "count", d["count"])
cutoff = "2026-09-04T12:24:00"
new_tpl = []
for i in d["items"]:
    aa = i.get("added_at") or ""
    if aa.replace(".000Z","Z").replace(".000","") >= cutoff and i["type"]=="template":
        new_tpl.append(i)
print("templates since cutoff", len(new_tpl))
for i in sorted(new_tpl, key=lambda x: x.get("added_at") or ""):
    print(i.get("added_at"), i["slug"])

# education use-cases
kw = ("anki","tutor","language learn","flashcard","srs","graded","comprehensible","vocab","pronunciation","spaced","japanese","mandarin","spanish","french","german","russian","esl","homeschool","wiki","student")
print("\n=== use-cases possibly education ===")
for i in d["items"]:
    if i["type"] != "use-case":
        continue
    cats = " ".join(i.get("categories") or []).lower()
    text = " ".join([i.get("headline") or "", i.get("summary") or "", i.get("slug") or "", cats]).lower()
    score = i.get("awesome_score") or 0
    # strict: edu categories OR strong language/tutor/anki
    strict = any(x in cats for x in ("education","learning","student","language")) or any(x in text for x in ("anki","language tutor","flashcard","spaced repetition","comprehensible input","graded reader","pronunciation","language learning"))
    if not strict:
        continue
    print("score=%s added=%s slug=%s cats=%s" % (score, i.get("added_at"), i["slug"], i.get("categories")))
    print(" ", i.get("headline"))
    print(" ", (i.get("summary") or "")[:180])
    print()

print("\n=== use-cases score>=80 ===")
for i in d["items"]:
    if i["type"]=="use-case" and (i.get("awesome_score") or 0) >= 80:
        print(i.get("awesome_score"), i.get("added_at"), i["slug"], "|", (i.get("headline") or "")[:80])

print("\n=== newest use-cases (by added_at) ===")
ucs = [i for i in d["items"] if i["type"]=="use-case"]
ucs.sort(key=lambda x: x.get("added_at") or "", reverse=True)
for i in ucs[:8]:
    print(i.get("added_at"), "score=", i.get("awesome_score"), i["slug"])
