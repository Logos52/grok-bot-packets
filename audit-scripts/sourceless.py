#!/usr/bin/env python3
import os, re, subprocess, json
from pathlib import Path
from collections import defaultdict

REPO = Path("/workspace/logos52.github.io")
os.chdir(REPO)
tracked = [t for t in subprocess.check_output(["git","ls-files","-z"], text=True).split("\0") if t]
wiki = [f for f in tracked if f.startswith("wiki/") and f.endswith(".md")]
print("wiki", len(wiki))

def classify(text):
    has_sources = bool(re.search(r"^## Sources\s*$", text, re.M))
    has_source = bool(re.search(r"^## Source\s*$", text, re.M))
    has_h3 = bool(re.search(r"^### Sources\s*$", text, re.M))
    # variants
    variants = []
    for m in re.finditer(r"^(#{1,6})\s+(Sources?)\s*$", text, re.M):
        variants.append((m.group(1), m.group(2), m.group(0)))
    # also **Sources** or Sources: 
    return has_sources, has_source, has_h3, variants

missing = []
singular = []
has = []
redirects_missing = []
type_redirect = []
for f in wiki:
    text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    hs, h1s, h3, variants = classify(text)
    fm_type = None
    if text.startswith("---"):
        end = text.find("\n---", 3)
        fm = text[:end] if end!=-1 else ""
        tm = re.search(r"^type:\s*(.+)$", fm, re.M)
        if tm:
            fm_type = tm.group(1).strip().strip('"')
    rec = {"path": f, "type": fm_type, "variants": variants}
    if hs:
        has.append(rec)
    else:
        missing.append(rec)
        if h1s:
            singular.append(rec)
        if fm_type in ("redirect",) or "redirect" in (fm_type or ""):
            type_redirect.append(rec)

print("has ## Sources", len(has))
print("missing ## Sources", len(missing))
print("singular ## Source among missing", len(singular))
print("redirect-type among missing", len(type_redirect))
print("\n=== SINGULAR ===")
for r in singular:
    print(r["path"], r["variants"], "type=", r["type"])
print("\n=== MISSING with other Sources variants ===")
for r in missing:
    if r["variants"]:
        print(r["path"], r["variants"], "type=", r["type"])
print("\n=== ALL MISSING ===")
for r in sorted(missing, key=lambda x: x["path"]):
    print(f"{r['path']}\ttype={r['type']}")

Path("/workspace/audit-scripts/sourceless.json").write_text(json.dumps({"total": len(wiki), "missing": missing, "singular": singular, "has": len(has)}, indent=2), encoding="utf-8")
