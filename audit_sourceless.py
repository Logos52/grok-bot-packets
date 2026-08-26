import os, re, subprocess
from pathlib import Path
from collections import defaultdict

repo = Path("/workspace/logos52.github.io")
os.chdir(repo)

raw = subprocess.check_output(["git", "ls-files", "-z", "--", "wiki/**/*.md"])
wiki_files = [f for f in raw.decode().split("\0") if f]
print(f"total={len(wiki_files)}")

missing = []
singular = []
source_note = []
has_sources = []
redirects = []

for f in wiki_files:
    text = (repo / f).read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    has_h2_sources = any(line.strip() == "## Sources" for line in lines)
    has_h2_source = any(line.strip() == "## Source" for line in lines)
    other_src = [l for l in lines if l.startswith("## ") and "Source" in l and l.strip() not in ("## Sources", "## Source")]

    is_redirect = False
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end]
            if re.search(r"^type:\s*redirect", fm, re.M) or re.search(r"^status:\s*(moved|empty-redirect)", fm, re.M):
                is_redirect = True

    if has_h2_sources:
        has_sources.append(f)
    else:
        missing.append(f)
        if is_redirect:
            redirects.append(f)
        if has_h2_source:
            singular.append(f)
        if other_src:
            source_note.append((f, other_src))

print(f"has_sources={len(has_sources)}")
print(f"missing={len(missing)}")
print(f"singular_Source={len(singular)}")
for s in singular:
    print(f"  SINGULAR {s}")
print(f"other_Source_headings={source_note}")
print(f"redirects_among_missing={redirects}")

clusters = defaultdict(list)
for f in missing:
    parts = f.split("/")
    key = parts[1] if len(parts) > 1 else f
    clusters[key].append(f)

print("\n=== CLUSTERS ===")
for k, vs in sorted(clusters.items(), key=lambda x: -len(x[1])):
    print(f"{k}: {len(vs)}")

print("\n=== FULL MISSING LIST ===")
for f in sorted(missing):
    extra = ""
    if f in redirects:
        extra = " (redirect)"
    if f in singular:
        extra = " (## Source singular)"
    print(f"- {f}{extra}")

p2 = open("/workspace/p2_sourceless.txt").read().strip().splitlines()
p2_set = set(p2)
missing_set = set(missing)
print(f"\n=== P2 sourceless still missing: {len(p2_set & missing_set)} ===")
print(f"P2 sourceless now have Sources or deleted: {len(p2_set - missing_set)}")
print("NO LONGER SOURCELESS (have Sources or gone from wiki):")
for f in sorted(p2_set - missing_set):
    still = f in wiki_files
    print(f"  {f}  tracked={still}")
print("NEW sourceless (not in p2):")
for f in sorted(missing_set - p2_set):
    print(f"  {f}")
print("PERSIST:")
for f in sorted(p2_set & missing_set):
    print(f"  {f}")
