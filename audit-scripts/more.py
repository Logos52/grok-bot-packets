#!/usr/bin/env python3
import os, re, subprocess, json
from pathlib import Path
from collections import defaultdict
REPO = Path("/workspace/logos52.github.io")
os.chdir(REPO)
tracked = [t for t in subprocess.check_output(["git","ls-files","-z"], text=True).split("\0") if t]
wiki = [f for f in tracked if f.startswith("wiki/") and f.endswith(".md")]

# Ollama anywhere tracked md
print("=== OLLAMA in tracked md/instruction ===")
for f in tracked:
    if not re.search(r"\.(md|mjs|js|sh|yml|yaml|txt)$", f):
        continue
    if f.startswith("_archive/"):
        continue
    text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        if re.search(r"Ollama|ollama", line):
            print(f"{f}:{i}: {line.strip()[:180]}")

print("\n=== type:redirect wiki pages ===")
for f in wiki:
    text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    if re.search(r"^type:\s*redirect\b", text, re.M):
        print(f)

print("\n=== ## Sources variants (colon, extra) ===")
pat = re.compile(r"^#{1,3}\s+Sources?\b.*$", re.M)
for f in wiki:
    text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    if re.search(r"^## Sources\s*$", text, re.M):
        continue
    hits = pat.findall(text)
    if hits:
        print(f, hits[:5])

print("\n=== Workbench wikilinks in wiki ===")
for f in wiki:
    text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        if "Workbench" in line and "[[" in line:
            print(f"{f}:{i}: {line.strip()[:180]}")

print("\n=== Codex in instruction ===")
for f in tracked:
    if f.startswith("_archive/"):
        continue
    if f not in ("AGENTS.md","CLAUDE.md","GROK.md","README.md") and not f.startswith(("tools/","scripts/","hermes/","02 - System/")):
        continue
    if not f.endswith((".md",".mjs",".sh",".yml")):
        continue
    text = (REPO/f).read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        if re.search(r"Codex", line):
            print(f"{f}:{i}: {line.strip()[:180]}")
