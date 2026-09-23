# Sweep MWF 8 notes
window: 2026-09-21T12:12:32+08:00 — 2026-09-23T12:10:33+08:00 (Asia/Taipei)
fetched_at_utc: 2026-09-23T04:10:33Z

## Per-source fetch
| source | method | status | notes |
|---|---|---|---|
| anthropic.com/research | curl | ok | all listing research links already in seen |
| x.ai/news | curl | ok | Grok 4.7 (2026-09-21) + grok-bot-customer-support (2026-09-22) packeted; other listing URLs stamped scanned if new |
| docs.x.ai/grok-bot/overview | skipped | already seen | bounced in seen |
| arxiv cs.AI/cs.CL /new + pastweek | curl HTML | ok | Tue 22 + Wed 23 keyword-core; title-strong craft ≥9 packeted; Mon 21 already in MWF 7 |
| learningscientists.org/blog | curl + RSS | ok | newest still 2026/9/17 already packeted |
| retrievalpractice.org | curl + RSS | ok | no dated new item (RSS endpoint returns HTML / no 2026 posts) |

failed sources: none
packet items (≥6, effective ≥9 arxiv): 40
below/scanned stamped: 790 below (arxiv non-packet + demoted); 0 new x.ai scanned ghosts
banked full reads: none (arxiv listing-only; grok-4-7 already in bank INDEX; no re-bank)
truncation: weekly usage — keyword-core + combined≥9 for arxiv; craft filter + domain demotion; no expensive abstract/PDF rescoring beyond Tue/Wed listing titles
calibration: packet 8 of 10 — no threshold/source cuts proposed
