#!/usr/bin/env python3
"""Rebuild /workspace/arguments/latest.md from packets dated within last 7 days of as_of."""
from pathlib import Path
from datetime import datetime, timedelta
import re, sys

args = Path("/workspace/arguments")
as_of = datetime.strptime(sys.argv[1], "%Y-%m-%d") if len(sys.argv) > 1 else datetime(2026, 9, 21)
cutoff = as_of - timedelta(days=7)
# last 7 days inclusive of as_of → files with date >= as_of-6? 
# "last 7 days" usually means as_of-6 .. as_of (7 calendar days) OR as_of-7 .. as_of.
# Prior file included from 2026-09-14 when built 2026-09-20 → that's 7 days back inclusive of 14.
# 20-7=13, but they used 14. So cutoff = as_of - 6 days → 7 calendar dates.
cutoff = as_of - timedelta(days=6)

skip = {"latest.md"}
packets = []
for p in args.glob("*.md"):
    if p.name in skip or "fable-pack" in p.name:
        continue
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-", p.name)
    if not m:
        continue
    d = datetime.strptime(m.group(1), "%Y-%m-%d")
    if d >= cutoff:
        packets.append((d, p))
packets.sort(key=lambda x: (x[0], x[1].name), reverse=True)

parts = [f"# Arguments · latest (last 7 days as of {as_of.date()})\n"]
parts.append(f"_Rebuilt {as_of.date()} · {len(packets)} packets · cutoff {cutoff.date()}_\n")
for d, p in packets:
    parts.append("\n---\n\n")
    parts.append(p.read_text().rstrip() + "\n")
out = args / "latest.md"
out.write_text("".join(parts))
print(f"Wrote {out} ({out.stat().st_size} bytes) with {len(packets)} packets")
for d,p in packets:
    print(f"  {p.name}")
