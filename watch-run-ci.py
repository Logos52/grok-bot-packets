#!/usr/bin/env python3
import json, urllib.request
from datetime import datetime, timezone
from pathlib import Path

GH = Path("/workspace/secrets/github-readonly").read_text().strip()
repos = [
  "Logos52/tsumugu-core-dev",
  "Logos52/tsumugu-core",
  "Logos52/tsumugu",
  "Logos52/tsumugu-ed",
  "Logos52/tsumugu-wiki",
  "Logos52/logos52.github.io",
  "Logos52/grok-bot-packets",
]

def get(url):
  req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {GH}",
    "Accept": "application/vnd.github+json",
    "User-Agent": "Watch/1.0",
  })
  with urllib.request.urlopen(req, timeout=30) as r:
    body = r.read()
    remaining = r.headers.get("X-RateLimit-Remaining")
    return json.loads(body), remaining

results = {}
for repo in repos:
  try:
    meta, rl = get(f"https://api.github.com/repos/{repo}")
    if "message" in meta and "default_branch" not in meta:
      print(f"REPO={repo} ERROR={meta.get('message')} RL={rl}")
      results[repo] = {"error": meta.get("message"), "alert": False}
      continue
    default_branch = meta.get("default_branch") or "main"
    runs, rl = get(f"https://api.github.com/repos/{repo}/actions/runs?per_page=1&branch={default_branch}")
    if "message" in runs and "workflow_runs" not in runs:
      print(f"REPO={repo} ERROR={runs.get('message')} RL={rl}")
      results[repo] = {"error": runs.get("message"), "alert": True, "default_branch": default_branch}
      continue
    wfr = runs.get("workflow_runs") or []
    if not wfr:
      print(f"REPO={repo} BRANCH={default_branch} STATUS=no_runs CONCLUSION= ALERT=0 AGE= URL= NAME= UPDATED= RL={rl}")
      results[repo] = {
        "conclusion": None, "status": "no_runs", "name": None, "html_url": None,
        "updated_at": None, "default_branch": default_branch, "alert": False, "error": None
      }
      continue
    r = wfr[0]
    upd = r.get("updated_at") or r.get("created_at")
    age_h = ""
    if upd:
      t = datetime.fromisoformat(upd.replace("Z", "+00:00"))
      age_h = round((datetime.now(timezone.utc) - t).total_seconds() / 3600, 1)
    conc = r.get("conclusion")
    status = r.get("status")
    alert = 1 if status == "completed" and conc in ("failure", "cancelled", "timed_out") else 0
    print(f"REPO={repo} BRANCH={default_branch} STATUS={status} CONCLUSION={conc} ALERT={alert} AGE={age_h}h URL={r.get('html_url')} NAME={r.get('name')} UPDATED={upd} RL={rl}")
    results[repo] = {
      "conclusion": conc, "status": status, "name": r.get("name"), "html_url": r.get("html_url"),
      "updated_at": upd, "default_branch": default_branch, "alert": bool(alert), "error": None, "age_h": age_h
    }
  except Exception as e:
    print(f"REPO={repo} ERROR={e}")
    results[repo] = {"error": str(e), "alert": True}

Path("/workspace/watch-ci-out.json").write_text(json.dumps(results, indent=2))
try:
  rl, _ = get("https://api.github.com/rate_limit")
  c = rl.get("resources", {}).get("core", {})
  print("RATE", c.get("remaining"), "/", c.get("limit"))
except Exception as e:
  print("RATE_ERR", e)
