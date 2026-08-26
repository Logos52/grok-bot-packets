#!/usr/bin/env python3
import os, re, subprocess
from pathlib import Path
REPO = Path("/workspace/logos52.github.io")
os.chdir(REPO)
tracked = [t for t in subprocess.check_output(["git","ls-files","-z"], text=True).split("\0") if t]

# instruction/config scope
def is_instr(f):
    if f in ("AGENTS.md","CLAUDE.md","GROK.md","README.md"):
        return True
    prefixes = ("tools/", "scripts/", "hermes/", ".github/")
    if any(f.startswith(p) for p in prefixes):
        return True
    # similar
    if f.startswith("02 - System/") and f.endswith(".md"):
        return True
    return False

instr = [f for f in tracked if is_instr(f) and not f.endswith((".png",".jpg",".json",".lock"))]
print("instruction files", len(instr))

terms = re.compile(r"Hermes|Ollama|Codex|quartz|Quartz", re.I)
history_heads = re.compile(r"^#{1,3}\s+(What.?s Gone|Evolution|changelog|Change log|History)\b", re.I)

def in_history_section(lines, lineno):
    # walk backward for a history heading
    current = None
    for i, line in enumerate(lines, 1):
        m = history_heads.match(line.strip()) if False else None
    # simpler: find last heading before lineno
    last = None
    for i in range(lineno):
        s = lines[i].strip()
        if s.startswith("#"):
            last = s
    if last and re.search(r"What.?s Gone|Evolution|changelog|History|What changed", last, re.I):
        return last
    return None

print("\n=== MOLD/TERM HITS IN INSTRUCTION ===")
for f in instr:
    if not f.endswith((".md",".mjs",".js",".sh",".yml",".yaml",".ts",".txt",".SKILL.md")) and "SKILL" not in f and not f.endswith(".md"):
        # still scan md, mjs, sh, yml, ts
        if not re.search(r"\.(md|mjs|js|sh|yml|yaml|ts|txt)$", f):
            continue
    try:
        text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if terms.search(line):
            hist = in_history_section(lines, i)
            tag = "HIST" if hist else "LIVE?"
            print(f"{tag} {f}:{i}: {line.strip()[:200]}")

print("\n=== AGENTS.md Hermes / Codex / Ollama / quartz / GPT current ===")
text = (REPO/"AGENTS.md").read_text(encoding="utf-8")
for i, line in enumerate(text.splitlines(), 1):
    if re.search(r"Hermes|Ollama|Codex|quartz|RemoveDrafts|GPT", line, re.I):
        print(f"AGENTS.md:{i}: {line.rstrip()[:200]}")
