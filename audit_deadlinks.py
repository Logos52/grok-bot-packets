import os, re, subprocess
from collections import defaultdict
from pathlib import Path

repo = Path("/workspace/logos52.github.io")
os.chdir(repo)

raw = subprocess.check_output(["git", "ls-files", "-z", "--", "wiki/**/*.md"])
wiki_files = [f for f in raw.decode().split("\0") if f]

all_tracked = [f for f in subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0") if f]
tracked_set = set(all_tracked)

stem_to_paths = defaultdict(list)
for f in all_tracked:
    p = Path(f)
    stem_to_paths[p.stem].append(f)

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
MDLINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

dead_wiki = []
dead_md = []
raw_private_skipped = []
heading_only = 0

def resolve_wikilink(target, source_file):
    t = target.strip()
    if t.startswith("#"):
        return None, "heading-only"
    if "|" in t:
        t = t.split("|", 1)[0].strip()
    if "#" in t:
        t = t.split("#", 1)[0].strip()
    if not t:
        return None, "heading-only"
    t = t.replace("\\", "/")
    if t.startswith("^"):
        return None, "block-ref"

    low = t.lower()
    if t.startswith("raw/") or t.startswith("private/") or t.startswith("/raw/") or t.startswith("/private/"):
        return "SKIP", "raw-or-private"
    # path containing raw/ or private/ as first segment
    parts = t.split("/")
    if parts and parts[0] in ("raw", "private"):
        return "SKIP", "raw-or-private"

    src_dir = str(Path(source_file).parent)
    variants = [t]
    if not t.endswith(".md"):
        variants.append(t + ".md")
    for v in variants:
        if v in tracked_set:
            return v, None
        rel = os.path.normpath(str(Path(src_dir) / v))
        if rel in tracked_set:
            return rel, None

    stem = Path(t).stem if t.endswith(".md") else Path(t).name
    if "/" in t:
        for prefix in ["", "wiki/"]:
            for ext in ["", ".md"]:
                cand = (prefix + t + ext).replace("//", "/")
                if cand.endswith(".md.md"):
                    cand = cand[:-3]
                if cand in tracked_set:
                    return cand, None
        if stem in stem_to_paths:
            return stem_to_paths[stem][0], None
        if parts and parts[0] in ("raw", "private"):
            return "SKIP", "raw-or-private"
        return None, "dead"
    else:
        if stem in stem_to_paths:
            return stem_to_paths[stem][0], None
        return None, "dead"

for f in wiki_files:
    text = (repo / f).read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        for m in WIKILINK.finditer(line):
            inner = m.group(1)
            res, reason = resolve_wikilink(inner, f)
            if reason == "heading-only":
                heading_only += 1
            elif reason == "raw-or-private":
                raw_private_skipped.append((f, i, inner))
            elif reason == "dead":
                dead_wiki.append((f, i, inner, line.strip()[:160]))

        for m in MDLINK.finditer(line):
            href = m.group(1).strip()
            if href.startswith(("http://", "https://", "mailto:", "#", "obsidian://")):
                continue
            if " " in href and not href.startswith("/"):
                href = href.split()[0]
            href = href.split("#")[0]
            if not href:
                continue
            if href.startswith("raw/") or href.startswith("/raw/") or href.startswith("private/") or href.startswith("/private/"):
                raw_private_skipped.append((f, i, href))
                continue
            if not (href.endswith(".md") or ".md" in href):
                continue
            src_dir = str(Path(f).parent)
            rel = os.path.normpath(str(Path(src_dir) / href)) if not href.startswith("/") else href.lstrip("/")
            candidates = [href, rel, href.lstrip("./")]
            ok = False
            for c in candidates:
                c = os.path.normpath(c)
                if c in tracked_set:
                    ok = True
                    break
            if not ok:
                stem = Path(href).stem
                if stem in stem_to_paths:
                    ok = True
            if not ok:
                dead_md.append((f, i, href, line.strip()[:160]))

print(f"heading_only={heading_only}")
print(f"raw_private_skipped={len(raw_private_skipped)}")
print(f"DEAD_WIKI={len(dead_wiki)}")
print(f"DEAD_MD={len(dead_md)}")
print("\n=== DEAD WIKILINKS ===")
for item in dead_wiki:
    print(f"{item[0]}:{item[1]} -> {item[2]}")
    print(f"    {item[3]}")

print("\n=== DEAD MD LINKS ===")
for item in dead_md:
    print(f"{item[0]}:{item[1]} -> {item[2]}")
    print(f"    {item[3]}")

print("\n=== RAW/PRIVATE (all) ===")
for item in raw_private_skipped:
    print(f"{item[0]}:{item[1]} -> {item[2][:100]}")
