#!/bin/bash
set -euo pipefail
GC_TOKEN=$(cat /workspace/secrets/goatcounter-readonly)
echo "GC_CUR=$(curl -sS --max-time 20 -H "Authorization: Bearer $GC_TOKEN" "https://logos52.goatcounter.com/api/v0/stats/total?start=2026-09-02&end=2026-09-08")"
echo "GC_PREV=$(curl -sS --max-time 20 -H "Authorization: Bearer $GC_TOKEN" "https://logos52.goatcounter.com/api/v0/stats/total?start=2026-08-26&end=2026-09-01")"
