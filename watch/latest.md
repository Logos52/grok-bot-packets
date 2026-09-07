**2026-09-07 · slowest TTFB ~0.26s** (tsumugu.cc/) · CF as-of 2026-09-06

**REACH:** All green · 5/5
Actions: success. CF cache MISS / MISS / EXPIRED / EXPIRED (not DYNAMIC).

**AUDIENCE:**
- ed (CF RUM): 10 visits / 10 pv · 7d (was 0/0) · ext-ref 0
- cc (CF RUM): 31 visits / 39 pv · 7d (was 0/0) · ext-ref 21
- gc (cc home): 11 pv · 7d (was 4)

**NEW:** ed visits 0→10 · cc visits 0→31 · cc ext-ref 0→21 · ed ext-ref 1→0

**SEARCH:**
- ed: 0 clicks / 1 impr · 14d (was 0/0)
- cc: 0 clicks / 0 impr · 14d (was 0/7)

**CI:**
- Logos52/tsumugu-core-dev — CI — failure — https://github.com/Logos52/tsumugu-core-dev/actions/runs/33885746332 — ~58h (was success)
- Logos52/tsumugu-core — Deploy Tsumugu Core — failure — https://github.com/Logos52/tsumugu-core/actions/runs/28697465339 — ~65d (stale)
- Logos52/tsumugu-ed — validate corpus — failure — https://github.com/Logos52/tsumugu-ed/actions/runs/33648836647 — ~4d

**DECISIONS:**
1. Investigate new CI failure on tsumugu-core-dev (compaction/2026-07).
2. tsumugu-ed validate corpus still red since Sep 2.
3. tsumugu-core Deploy still red since Jul 4 — ignore or archive?
