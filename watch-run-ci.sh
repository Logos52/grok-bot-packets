#!/bin/bash
set -euo pipefail
GH=$(cat /workspace/secrets/github-readonly)
repos=(
  Logos52/tsumugu-core-dev
  Logos52/tsumugu-core
  Logos52/tsumugu
  Logos52/tsumugu-ed
  Logos52/tsumugu-wiki
  Logos52/logos52.github.io
  Logos52/grok-bot-packets
)
for repo in "${repos[@]}"; do
  meta=$(curl -sS --max-time 20 -H "Authorization: Bearer $GH" -H "Accept: application/vnd.github+json" "https://api.github.com/repos/$repo")
  default_branch=$(echo "$meta" | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("default_branch") or "")')
  if [[ -z "$default_branch" ]]; then
    echo "REPO=$repo ERROR=$(echo "$meta" | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("message","unknown"))')"
    continue
  fi
  runs=$(curl -sS -D /tmp/gh_hdr --max-time 20 -H "Authorization: Bearer $GH" -H "Accept: application/vnd.github+json" \
    "https://api.github.com/repos/$repo/actions/runs?per_page=1&branch=$default_branch")
  rl=$(grep -i '^x-ratelimit-remaining:' /tmp/gh_hdr | tr -d '\r' | awk '{print $2}')
  echo "$runs" | DEFAULT_BRANCH="$default_branch" REPO="$repo" RL="$rl" python3 -c '
import sys,json,os
from datetime import datetime,timezone
repo=os.environ["REPO"]; default_branch=os.environ["DEFAULT_BRANCH"]; rl=os.environ.get("RL","")
d=json.load(sys.stdin)
if "message" in d and "workflow_runs" not in d:
  print(f"REPO={repo} ERROR={d.get(\"message\")} RL={rl}")
  raise SystemExit(0)
runs=d.get("workflow_runs") or []
if not runs:
  print(f"REPO={repo} BRANCH={default_branch} STATUS=no_runs CONCLUSION= ALERT=0 AGE= URL= NAME= UPDATED= RL={rl}")
  raise SystemExit(0)
r=runs[0]
upd=r.get("updated_at") or r.get("created_at")
age_h=""
if upd:
  t=datetime.fromisoformat(upd.replace("Z","+00:00"))
  age_h=round((datetime.now(timezone.utc)-t).total_seconds()/3600,1)
conc=r.get("conclusion"); status=r.get("status")
alert=1 if status=="completed" and conc in ("failure","cancelled","timed_out") else 0
print(f"REPO={repo} BRANCH={default_branch} STATUS={status} CONCLUSION={conc} ALERT={alert} AGE={age_h}h URL={r.get(\"html_url\")} NAME={r.get(\"name\")} UPDATED={upd} RL={rl}")
'
done
curl -sS --max-time 10 -H "Authorization: Bearer $GH" -H "Accept: application/vnd.github+json" "https://api.github.com/rate_limit" | python3 -c 'import sys,json; d=json.load(sys.stdin); c=d.get("resources",{}).get("core",{}); print("RATE", c.get("remaining"), "/", c.get("limit"))'
