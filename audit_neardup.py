import os, re, subprocess
from collections import defaultdict
from pathlib import Path
from difflib import SequenceMatcher

repo = Path("/workspace/logos52.github.io")
os.chdir(repo)

raw = subprocess.check_output(["git", "ls-files", "-z", "--", "wiki/**/*.md"])
wiki_files = [f for f in raw.decode().split("\0") if f]
print(f"TRACKED_WIKI={len(wiki_files)}")

all_tracked = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
all_tracked = [f for f in all_tracked if f]
print(f"TRACKED_ALL={len(all_tracked)}")

records = []
for f in wiki_files:
    text = (repo / f).read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    h1 = None
    for line in lines:
        if line.startswith("# ") and not line.startswith("##"):
            h1 = line[2:].strip()
            break
    fm_title = None
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end]
            m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", fm, re.M)
            if m:
                fm_title = m.group(1).strip()
    stem = Path(f).stem
    body = text
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end != -1:
            body = body[end+4:]
    body = re.sub(r"^# .+\n+", "", body.lstrip(), count=1)
    opening = re.sub(r"\s+", " ", body.strip())[:400]
    records.append({"path": f, "stem": stem, "h1": h1, "fm_title": fm_title, "opening": opening})

h1_groups = defaultdict(list)
stem_groups = defaultdict(list)
for r in records:
    if r["h1"]:
        key = re.sub(r"\s+", " ", r["h1"].lower().strip())
        h1_groups[key].append(r)
    stem_groups[r["stem"].lower()].append(r)

print("\n=== SAME H1 (multiple files) ===")
for k, vs in sorted(h1_groups.items()):
    if len(vs) > 1:
        print(f"H1={vs[0]['h1']!r}")
        for v in vs:
            print(f"  {v['path']}")

print("\n=== SAME STEM (multiple files) ===")
for k, vs in sorted(stem_groups.items()):
    if len(vs) > 1:
        print(f"STEM={k}")
        for v in vs:
            print(f"  {v['path']}  H1={v['h1']!r}")

print("\n=== STEM pairs leftover stubs (X vs X Challenge) ===")
challenge = [r for r in records if r["stem"].lower().endswith(" challenge")]
for r in challenge:
    base = r["stem"][:-len(" Challenge")]
    hits = [x for x in records if x["stem"].lower() == base.lower()]
    if hits:
        print("PAIR:", r["path"], "<->", [h["path"] for h in hits])

print("\n=== Similar openings/titles ===")
pairs = []
for i, a in enumerate(records):
    if a["path"].startswith("wiki/_archive") or "/_archive/" in a["path"]:
        continue
    for b in records[i+1:]:
        if b["path"].startswith("wiki/_archive") or "/_archive/" in b["path"]:
            continue
        sa, sb = a["stem"].lower(), b["stem"].lower()
        h1a = (a["h1"] or "").lower()
        h1b = (b["h1"] or "").lower()
        stem_sim = SequenceMatcher(None, sa, sb).ratio()
        h1_sim = SequenceMatcher(None, h1a, h1b).ratio() if h1a and h1b else 0
        if stem_sim < 0.6 and h1_sim < 0.7:
            continue
        op_sim = SequenceMatcher(None, a["opening"][:250], b["opening"][:250]).ratio()
        if op_sim >= 0.55 or h1_sim >= 0.92:
            pairs.append((op_sim, h1_sim, stem_sim, a["path"], b["path"], a["h1"], b["h1"]))

pairs.sort(reverse=True)
for p in pairs[:100]:
    print(f"op={p[0]:.2f} h1={p[1]:.2f} st={p[2]:.2f}")
    print(f"  A: {p[3]} | {p[5]}")
    print(f"  B: {p[4]} | {p[6]}")
