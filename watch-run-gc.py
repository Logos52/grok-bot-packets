#!/usr/bin/env python3
import json, urllib.request
from pathlib import Path
from datetime import date, timedelta

token = Path("/workspace/secrets/goatcounter-readonly").read_text().strip()
# yesterday-ended 7d windows
# today 2026-09-09 → cur 2026-09-02..2026-09-08, prev 2026-08-26..2026-09-01

def fetch(start, end):
  url = f"https://logos52.goatcounter.com/api/v0/stats/total?start={start}&end={end}"
  req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {token}",
    "User-Agent": "Watch/1.0",
  })
  try:
    with urllib.request.urlopen(req, timeout=30) as r:
      body = r.read().decode()
      return json.loads(body)
  except urllib.error.HTTPError as e:
    body = e.read().decode(errors="replace")
    return {"error": e.code, "body": body[:500], "url": url}

for label, start, end in [
  ("CUR", "2026-09-02", "2026-09-08"),
  ("CUR2", "2026-09-02", "2026-09-09"),
  ("CUR3", "2026-08-31", "2026-09-06"),  # previous known-good window for sanity
  ("PREV", "2026-08-26", "2026-09-01"),
]:
  d = fetch(start, end)
  if "error" in d and "total" not in d:
    print(label, "ERR", d.get("error"), d.get("url"), (d.get("body") or "")[:120].replace("\n"," "))
  else:
    # sum daily if present
    daily = sum((s.get("daily") or 0) for s in d.get("stats") or [])
    print(label, "total=", d.get("total"), "daily_sum=", daily, "days=", len(d.get("stats") or []))
