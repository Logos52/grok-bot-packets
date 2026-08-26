import os, re, subprocess
from collections import defaultdict
from pathlib import Path

repo = Path("/workspace/logos52.github.io")
os.chdir(repo)

raw = subprocess.check_output(["git", "ls-files", "-z", "--", "wiki/**/*.md"])
wiki_glob = [f for f in raw.decode().split("\0") if f]
# also include wiki-root md
all_tracked = [f for f in subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0") if f]
tracked_set = set(all_tracked)
wiki_root = [f for f in all_tracked if re.match(r"^wiki/[^/]+\.md$", f)]
wiki_files = sorted(set(wiki_glob) | set(wiki_root))
print(f"glob={len(wiki_glob)} root={len(wiki_root)} union={len(wiki_files)}")

stem_to_paths = defaultdict(list)
for f in all_tracked:
    stem_to_paths[Path(f).stem].append(f)

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
MDLINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

dead_wiki = []
dead_md = []
raw_private = []
heading_only = 0
wrong_path_stem_ok = []  # path specified, file exists elsewhere by stem

def is_raw_private(t):
    t = t.replace("\\", "/").lstrip("/")
    parts = t.split("/")
    if parts and parts[0] in ("raw", "private"):
        return True
    return False

def resolve_pathlike(t, source_file):
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
        # wiki/ prefix
        if not v.startswith("wiki/") and ("wiki/" + v) in tracked_set:
            return "wiki/" + v, None
    return None, "dead"

for f in wiki_files:
    text = (repo / f).read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        for m in WIKILINK.finditer(line):
            inner = m.group(1)
            t = inner.strip()
            if t.startswith("#"):
                heading_only += 1
                continue
            if "|" in t:
                t = t.split("|", 1)[0].strip()
            if "#" in t:
                t = t.split("#", 1)[0].strip()
            if not t:
                heading_only += 1
                continue
            t = t.replace("\\", "/")
            if is_raw_private(t):
                raw_private.append((f, i, inner))
                continue
            if "/" in t:
                res, reason = resolve_pathlike(t, f)
                if reason == "dead":
                    stem = Path(t).stem if t.endswith(".md") else Path(t).name
                    if stem in stem_to_paths:
                        wrong_path_stem_ok.append((f, i, inner, stem_to_paths[stem]))
                    else:
                        dead_wiki.append((f, i, inner, line.strip()[:180]))
            else:
                stem = t[:-3] if t.endswith(".md") else t
                if stem in stem_to_paths:
                    continue
                # try adding wiki
                dead_wiki.append((f, i, inner, line.strip()[:180]))

        for m in MDLINK.finditer(line):
            href = m.group(1).strip()
            if href.startswith(("http://", "https://", "mailto:", "#", "obsidian://")):
                continue
            if " " in href:
                href = href.split()[0]
            href = href.split("#")[0]
            if not href:
                continue
            if is_raw_private(href):
                raw_private.append((f, i, href))
                continue
            if not (href.endswith(".md") or ".md" in href):
                continue
            src_dir = str(Path(f).parent)
            rel = os.path.normpath(str(Path(src_dir) / href)) if not href.startswith("/") else href.lstrip("/")
            ok = False
            for c in [href, rel, os.path.normpath(href.lstrip("./"))]:
                if c in tracked_set:
                    ok = True
                    break
            if not ok:
                stem = Path(href).stem
                if stem in stem_to_paths:
                    wrong_path_stem_ok.append((f, i, href, stem_to_paths[stem]))
                else:
                    dead_md.append((f, i, href, line.strip()[:180]))

print(f"heading_only={heading_only}")
print(f"raw_private={len(raw_private)}")
print(f"DEAD_WIKI={len(dead_wiki)}")
print(f"DEAD_MD={len(dead_md)}")
print(f"WRONG_PATH_STEM_OK={len(wrong_path_stem_ok)}")
print("\n=== DEAD WIKILINKS ===")
for item in dead_wiki:
    print(f"{item[0]}:{item[1]} -> {item[2]}")
    print(f"    {item[3]}")
print("\n=== DEAD MD ===")
for item in dead_md:
    print(f"{item[0]}:{item[1]} -> {item[2]}")
print("\n=== WRONG PATH (exists by stem) ===")
for item in wrong_path_stem_ok:
    print(f"{item[0]}:{item[1]} -> {item[2]}")
    print(f"    actual={item[3]}")
