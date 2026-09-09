#!/bin/bash
set -euo pipefail
CF_TOKEN=$(cat /workspace/secrets/cf-analytics-readonly)
ACCOUNT=0f2bcde2d42bb2202bfa97b494d0a0cf
CUR_START=2026-09-02T00:00:00Z
CUR_END=2026-09-09T00:00:00Z
PREV_START=2026-08-26T00:00:00Z
PREV_END=2026-09-02T00:00:00Z

rum() {
  local tag=$1 start=$2 end=$3
  local q
  q=$(python3 -c "import json; print(json.dumps({'query':'query { viewer { accounts(filter: {accountTag: \"$ACCOUNT\"}) { rumPageloadEventsAdaptiveGroups(filter: {AND: [{siteTag: \"$tag\"}, {datetime_geq: \"$start\"}, {datetime_lt: \"$end\"}]}, limit: 5000, orderBy: [sum_visits_DESC]) { count sum { visits } dimensions { refererHost } } } } }'}))")
  curl -sS --max-time 30 -X POST "https://api.cloudflare.com/client/v4/graphql" \
    -H "Authorization: Bearer $CF_TOKEN" \
    -H "Content-Type: application/json" \
    -d "$q"
}

summarize() {
  python3 -c '
import sys,json
d=json.load(sys.stdin)
if d.get("errors"):
  print(json.dumps({"error": d["errors"]}))
  raise SystemExit(0)
try:
  groups=d["data"]["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
except Exception as e:
  print(json.dumps({"error": str(e), "raw": d}))
  raise SystemExit(0)
total_v=sum((g.get("sum") or {}).get("visits") or 0 for g in groups)
total_pv=sum(g.get("count") or 0 for g in groups)
ext=0
for g in groups:
  rh=((g.get("dimensions") or {}).get("refererHost") or "")
  if rh and rh.lower() not in ("","(direct)","direct","none"):
    ext += (g.get("sum") or {}).get("visits") or 0
print(json.dumps({"visits":total_v,"pv":total_pv,"ext_ref":ext,"groups":len(groups)}))
'
}

echo "ED_CUR=$(rum 89ac6d4ce2614fffb9b1f674232cfce5 "$CUR_START" "$CUR_END" | summarize)"
echo "ED_PREV=$(rum 89ac6d4ce2614fffb9b1f674232cfce5 "$PREV_START" "$PREV_END" | summarize)"
echo "CC_CUR=$(rum 9c65e7983e994d3f865d700dc95dfe41 "$CUR_START" "$CUR_END" | summarize)"
echo "CC_PREV=$(rum 9c65e7983e994d3f865d700dc95dfe41 "$PREV_START" "$PREV_END" | summarize)"
