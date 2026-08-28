#!/usr/bin/env python3
"""bank.py — put a source into the research bank.

    python3 bank.py --from <file-or-folder> [--lane L] [--via V] [--status S] [--dry-run]
    python3 bank.py --index
    python3 bank.py --root <dir>      (default /Users/n1/Research; /workspace/bank on the Grok Bot computer)

Built 2026-08-28. --text works (body on stdin). URL fetch, --recard, --event: not yet.
Stdlib only.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys, unicodedata
from datetime import date
from pathlib import Path

ROOT = Path("/Users/n1/Research")
LANES = ["ai", "learning", "politics", "money", "ideas", "culture", "yuedu", "cast", "gaming", "grok-bot", "misc"]
KEYS = ["id", "kind", "title", "source", "author", "published", "captured", "via", "lane", "status", "private"]

AUTHOR_LANE = {
    "basic logic": "politics", "triggernometry": "politics", "implicitly pretentious": "politics",
    "justin sung": "learning", "linking your thinking with nick milo": "learning", "dralanbarnard": "learning",
    "outlier linguistics": "learning", "matt vs japan": "learning", "the soak": "learning",
    "naval": "ideas", "chamath palihapitiya": "ideas", "gurwinder": "ideas", "all-in podcast": "ideas",
    "sequoia capital": "ai", "andrej karpathy": "ai", "tina huang": "ai", "jeff su": "ai",
    "maxinomics": "money", "elon musk fan zone": "money",
    "cinema therapy": "culture", "cinema on trial": "culture", "movie notepad": "culture",
    "from the screen": "culture", "timjongun productions": "culture", "minimalist - sibu": "culture",
    "solly": "culture", "panpan sawanpornpen": "learning",
}
TITLE_GAME = re.compile(r"\beql\b|\bwow\b|everquest|warcraft|shadow priest|necro|cleric|guild wars", re.I)
TITLE_AI = re.compile(r"claude|cowork|hermes|grok|agentic|\bai\b|llm|gpt|codex|cursor|vibe cod|karpathy|mcp|agent", re.I)
TITLE_LEARN = re.compile(r"learn|study|memory|brain|focus|attention|habit|motivat|rest|goal", re.I)

# ---------- frontmatter ----------
def split_fm(text: str):
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    fm, body = {}, text[m.end():]
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+- ", line) and key:
            fm.setdefault(key, [])
            if not isinstance(fm[key], list):
                fm[key] = [fm[key]] if fm[key] else []
            fm[key].append(line.strip()[2:].strip().strip('"'))
        elif ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip().strip('"')
            fm[key] = val
    return fm, body

def scalar(v):
    if isinstance(v, list):
        v = v[0] if v else ""
    v = str(v).strip()
    return re.sub(r"^\[\[|\]\]$", "", v)

def yaml_str(v: str) -> str:
    v = str(v)
    if v == "" or re.search(r'[:#"\[\]{}]|^\s|\s$|^[-?&*!|>%@`]', v) or v.lower() in ("true", "false", "null", "yes", "no"):
        return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return v

def emit_fm(d: dict, extra: list[str] = ()) -> str:
    lines = ["---"]
    for k in KEYS + list(extra):
        if k in d:
            v = d[k]
            lines.append(f"{k}: {str(v).lower()}" if isinstance(v, bool) else f"{k}: {yaml_str(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"

# ---------- id ----------
def slug(s: str, n: int = 6) -> str:
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[’'‘`\"“”]", "", s)
    words = re.findall(r"[a-z0-9]+|[぀-ヿ一-鿿]+", s)
    return "-".join(words[:n]) or "untitled"

def make_id(fm: dict, fallback_date: str) -> str:
    cap = scalar(fm.get("created") or fm.get("captured") or fallback_date)
    cap = re.sub(r"[^0-9-]", "", cap)[:10] or fallback_date
    auth = slug(scalar(fm.get("author", "")), 2) if scalar(fm.get("author", "")) else ""
    parts = [cap, auth, slug(scalar(fm.get("title", "")))]
    return "-".join(x for x in parts if x)

# ---------- kind / lane ----------
def guess_kind(source: str) -> str:
    s = source.lower()
    if "youtube.com" in s or "youtu.be" in s: return "transcript"
    if "x.com" in s or "twitter.com" in s: return "thread"
    if "nav.al" in s or "podcast" in s: return "podcast"
    return "article"

def guess_lane(fm: dict) -> str:
    author = scalar(fm.get("author", "")).lower()
    title = scalar(fm.get("title", ""))
    if TITLE_GAME.search(title): return "gaming"
    if TITLE_AI.search(title) and author not in ("basic logic",): return "ai"
    if author in AUTHOR_LANE: return AUTHOR_LANE[author]
    if "@" in author: return "ai"
    if TITLE_LEARN.search(title) or re.search(r"clinic|notion", title, re.I): return "learning"
    return "misc"

# ---------- strip ----------
PROMO = re.compile(r"^(WATCH NEXT|SUPPORT US|JOIN OUR DISCORD|FOLLOW US|SUBSCRIBE|TIMESTAMPS|CHAPTERS)\b", re.I)
PROMO_LINE = re.compile(r"📌|buymeacoffee|patreon\.com|discord\.gg|#\w+\s+#\w+|^\s*\d{1,2}:\d{2}(:\d{2})?\s*[-–·]\s", re.I)
STAMP = re.compile(r"^\*\*\d{1,2}:\d{2}(?::\d{2})?\*\*\s*[·•-]\s*")

def strip_body(body: str) -> str:
    out, skip = [], False
    for raw in body.splitlines():
        line = raw.rstrip()
        if re.match(r"^!\[\]\(.*\)\s*$", line):            # embed line
            continue
        if PROMO.match(line.strip()):                        # promo block start
            skip = True; continue
        if skip:
            if line.strip() == "" or PROMO_LINE.search(line): continue
            if line.startswith("#"): skip = False
            else: continue
        if PROMO_LINE.search(line) and not line.startswith("#"):
            continue
        line = STAMP.sub("", line)
        line = re.sub(r"\?(utm_[^&\s)]+&?)+", "?", line)     # tracking params
        line = re.sub(r"&t=\d+s?\b", "", line)
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text

# ---------- index ----------
def load_index(root: Path) -> dict:
    p = root / "index.jsonl"
    idx = {}
    if p.exists():
        for line in p.read_text().splitlines():
            if line.strip():
                o = json.loads(line); idx[o["id"]] = o
    return idx

def save_index(root: Path, idx: dict):
    rows = sorted(idx.values(), key=lambda o: (o["id"]))
    (root / "index.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in rows))
    by_lane = {}
    for o in rows: by_lane.setdefault(o["lane"], []).append(o)
    md = ["# INDEX", "", f"Generated by scripts/bank.py --index. {len(rows)} items. Do not edit.", ""]
    for lane in sorted(by_lane):
        md.append(f"## {lane} ({len(by_lane[lane])})"); md.append("")
        md.append("| id | kind | title | status | card | source |"); md.append("|---|---|---|---|---|---|")
        for o in by_lane[lane]:
            priv = " 🔒" if o.get("private") else ""
            card = "yes" if o.get("card") else ""
            md.append(f"| `{o['id']}`{priv} | {o['kind']} | {o['title'][:70]} | {o['status']} | {card} | {o['source'][:60]} |")
        md.append("")
    (root / "INDEX.md").write_text("\n".join(md))

def rebuild_index(root: Path) -> dict:
    idx = {}
    for p in sorted((root / "raw").rglob("*.md")):
        if p.relative_to(root / "raw").parts[0] == "private":
            continue  # raw/private holds course copies with no schema; folder mark only
        fm, body = split_fm(p.read_text(errors="replace"))
        if "id" not in fm: continue
        o = {k: fm.get(k, "") for k in KEYS}
        o["private"] = str(fm.get("private", "false")).lower() == "true" or p.relative_to(root / "raw").parts[0] == "private"
        o["raw"] = str(p.relative_to(root)); o["body_sha"] = hashlib.sha1(body.encode()).hexdigest()[:12]
        card = root / "cards" / p.relative_to(root / "raw")
        o["card"] = str(card.relative_to(root)) if card.exists() else ""
        o["used_by"] = []
        idx[o["id"]] = o
    save_index(root, idx)
    return idx

# ---------- ingest a file ----------
def ingest_file(src: Path, root: Path, lane: str | None, via: str, status: str | None, idx: dict, seen_sources: dict, dry: bool):
    text = src.read_text(errors="replace")
    fm, body = split_fm(text)
    if not fm.get("title"):
        fm["title"] = src.stem
    source = scalar(fm.get("source", ""))
    if source and source in seen_sources:
        return ("dup", seen_sources[source], src.name)
    fallback = date.fromtimestamp(src.stat().st_mtime).isoformat()
    iid = make_id(fm, fallback)
    base, n = iid, 2
    while iid in idx and idx[iid].get("source") != source:
        iid = f"{base}-{n}"; n += 1
    new = {
        "id": iid, "kind": guess_kind(source), "title": scalar(fm.get("title", "")), "source": source,
        "author": scalar(fm.get("author", "")), "published": scalar(fm.get("published", "")),
        "captured": scalar(fm.get("created") or fm.get("captured") or fallback),
        "via": via, "lane": lane or guess_lane(fm), "status": status or "raw", "private": False,
    }
    extra = {}
    if fm.get("description"): extra["description"] = scalar(fm["description"])[:300]
    out = root / "raw" / new["lane"] / f"{iid}.md"
    if not dry:
        out.parent.mkdir(parents=True, exist_ok=True)
        content = emit_fm({**new, **extra}, extra=["description"]) + "\n" + strip_body(body)
        out.write_text(content)
    seen_sources[source] = iid
    idx[iid] = {**new, "raw": str(out.relative_to(root))}
    return ("ok", iid, new["lane"])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--from", dest="src")
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--via", default="bank-cli")
    ap.add_argument("--status")
    ap.add_argument("--index", action="store_true")
    ap.add_argument("--text", action="store_true", help="body on stdin; metadata from the flags below")
    ap.add_argument("--source", default=""); ap.add_argument("--title", default=""); ap.add_argument("--author", default="")
    ap.add_argument("--published", default=""); ap.add_argument("--kind"); ap.add_argument("--private", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    if a.src:
        idx = load_index(root)
        seen = {o["source"]: o["id"] for o in idx.values() if o.get("source")}
        src = Path(a.src)
        files = sorted(src.rglob("*.md")) if src.is_dir() else [src]
        counts, dups = {}, []
        for f in files:
            r = ingest_file(f, root, a.lane, a.via, a.status, idx, seen, a.dry_run)
            if r[0] == "dup": dups.append((f.name, r[1]))
            else: counts[r[2]] = counts.get(r[2], 0) + 1
        for lane, n in sorted(counts.items()): print(f"{n:4d}  {lane}")
        print(f"{len(dups):4d}  duplicates skipped (same source URL)")
        for name, iid in dups: print(f"      {name}  ==  {iid}")
        if not a.dry_run:
            rebuild_index(root)
    if a.text:
        body = sys.stdin.read()
        if not body.strip():
            print("no body on stdin", file=sys.stderr); sys.exit(2)
        idx = load_index(root)
        seen = {o["source"]: o["id"] for o in idx.values() if o.get("source")}
        if a.source and a.source in seen:
            print(f"dup  {seen[a.source]}"); sys.exit(0)
        fm = {"title": a.title or "untitled", "source": a.source, "author": a.author, "published": a.published,
              "created": date.today().isoformat()}
        iid = make_id(fm, date.today().isoformat())
        base, n = iid, 2
        while iid in idx: iid = f"{base}-{n}"; n += 1
        lane = a.lane or guess_lane(fm)
        new = {"id": iid, "kind": a.kind or guess_kind(a.source), "title": fm["title"], "source": a.source,
               "author": a.author, "published": a.published, "captured": fm["created"], "via": a.via,
               "lane": lane, "status": a.status or "raw", "private": bool(a.private)}
        out = root / "raw" / lane / f"{iid}.md"
        if not a.dry_run:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(emit_fm(new) + "\n" + strip_body(body))
            rebuild_index(root)
        print(f"ok   {out.relative_to(root)}")
    if a.index:
        idx = rebuild_index(root); print(f"index: {len(idx)} items")

if __name__ == "__main__":
    main()
