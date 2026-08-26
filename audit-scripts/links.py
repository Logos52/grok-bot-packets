#!/usr/bin/env python3
"""Dead wikilink / markdown .md link checker. Tracked files only."""
import os, re, subprocess, json, urllib.parse
from pathlib import Path
from collections import defaultdict

REPO = Path("/workspace/logos52.github.io")
os.chdir(REPO)

tracked = subprocess.check_output(["git", "ls-files", "-z"], text=True).split("\0")
tracked = [t for t in tracked if t]
tracked_set = set(tracked)

stem_to_paths = defaultdict(list)
stem_lc = defaultdict(list)
for f in tracked:
    p = Path(f)
    if f.endswith(".md"):
        stem_to_paths[p.stem].append(f)
        stem_lc[p.stem.lower()].append(f)

wiki_md = [f for f in tracked if f.startswith("wiki/") and f.endswith(".md")]
print("wiki_md", len(wiki_md), flush=True)

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
MDLINK = re.compile(r"(?<!\!)\[([^\]]*)\]\(([^)]+)\)")

def normalize_target(raw: str):
    s = raw.strip()
    if "|" in s:
        s = s.split("|", 1)[0].strip()
    if "#" in s:
        s = s.split("#", 1)[0].strip()
    return s

def is_raw_or_private(target: str) -> bool:
    t = target.replace("\\", "/").lstrip("./")
    if t.startswith("raw/") or t.startswith("private/"):
        return True
    if "/raw/" in t or "/private/" in t:
        # only if path component
        parts = t.split("/")
        return "raw" in parts or "private" in parts
    return False

def resolve_wiki(target, source):
    if not target:
        return "EMPTY", "empty"
    if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
        return "EXT", "external"
    t = target.replace("\\", "/")
    t_nomd = t[:-3] if t.lower().endswith(".md") else t
    src_dir = str(Path(source).parent)
    for cand in (t, t + ".md", t_nomd + ".md"):
        if cand in tracked_set:
            return cand, "exact"
        rel = os.path.normpath(str(Path(src_dir) / cand))
        if rel in tracked_set:
            return rel, "relative"
    stem = Path(t_nomd).name
    if stem in stem_to_paths:
        return stem_to_paths[stem][0], "stem"
    hits = stem_lc.get(stem.lower())
    if hits:
        return hits[0], "stem-ci"
    return None, "unresolved"

dead = []
ok_raw_private = []
stats = defaultdict(int)

for f in wiki_md:
    text = (REPO / f).read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        for m in WIKILINK.finditer(line):
            stats["wiki_links"] += 1
            inner = m.group(1)
            cleaned = normalize_target(inner)
            if inner.strip().startswith("#") or cleaned == "":
                stats["heading_only"] += 1
                continue
            if is_raw_or_private(cleaned) or is_raw_or_private(inner.split("|")[0].strip()):
                stats["raw_private_skipped"] += 1
                ok_raw_private.append((f, i, cleaned))
                continue
            resolved, why = resolve_wiki(cleaned, f)
            if resolved == "EXT":
                stats["external"] += 1
                continue
            if resolved == "EMPTY":
                stats["heading_only"] += 1
                continue
            if resolved is None:
                stats["dead"] += 1
                dead.append({"file": f, "line": i, "kind": "wikilink", "raw": inner, "target": cleaned, "snippet": line.strip()[:180]})
            else:
                stats["resolved"] += 1

        for m in MDLINK.finditer(line):
            href = m.group(2).strip().strip('"').strip("'")
            if " " in href and not href.startswith("http"):
                href = href.split(" ", 1)[0]
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "://" in href:
                continue
            href_path = urllib.parse.unquote(href.split("#", 1)[0])
            if not (href_path.endswith(".md") or href_path.endswith(".MD")):
                continue
            stats["md_links"] += 1
            if is_raw_or_private(href_path):
                stats["raw_private_skipped"] += 1
                ok_raw_private.append((f, i, href_path))
                continue
            resolved, why = resolve_wiki(href_path, f)
            if resolved is None:
                stats["dead"] += 1
                dead.append({"file": f, "line": i, "kind": "md", "raw": href, "target": href_path, "snippet": line.strip()[:180]})
            else:
                stats["resolved"] += 1

print("STATS", json.dumps(dict(stats), indent=2))
print("DEAD COUNT", len(dead))
by_t = defaultdict(list)
for d in dead:
    by_t[d["target"]].append(d)
print("=== DEAD BY TARGET ===")
for t, items in sorted(by_t.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"[{len(items)}] {t}")
    for it in items[:8]:
        print(f"    {it['file']}:{it['line']} ({it['kind']})")
    if len(items) > 8:
        print(f"    ... +{len(items)-8} more")
print("raw/private skipped", len(ok_raw_private))
for x in ok_raw_private[:20]:
    print(" ", x)
Path("/workspace/audit-scripts/dead_links.json").write_text(json.dumps(dead, indent=2), encoding="utf-8")
