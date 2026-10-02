# Sweep MWF 12 notes
window: 2026-09-30T12:16:23+08:00 — 2026-10-02T12:12:29+08:00 (Asia/Taipei)
fetched_at_utc: 2026-10-02T04:12:29Z

## Per-source fetch
| source | method | status | notes |
|---|---|---|---|
| anthropic.com/research | curl | ok | new: Claude-shaped science (2026-10-01) packeted+banked; What work can robots do? (2026-09-30) below+banked; GLM-5.3/your-thoughts already seen; other nav stamped scanned |
| x.ai/news | curl | ok | no new posts since Team Bots (2026-09-28, MWF 11); listing/nav stamped scanned if new |
| docs.x.ai/grok-bot/overview | curl | ok | overview fetch ok; content deep-links stamped scanned — not separately packeted (news is canonical) |
| arxiv cs.AI/cs.CL /new + pastweek | curl HTML | ok | Thu 1 + Fri 2 Oct keyword-core; title-strong craft ≥9 packeted (70); Wed 30 already in MWF 11; undated/other replacements stamped below; no Sat/Sun |
| learningscientists.org/blog | curl + RSS | ok | no new posts since 2026/9/25-1 (already MWF 10); RSS/category unseen stamped scanned |
| retrievalpractice.org | curl (+ RSS 404) | ok | RSS endpoint 404 HTML; no dated 2026 posts in window |

failed sources: none
packet items (≥6, effective ≥9 arxiv): 71
below/scanned stamped: 1067 below (arxiv non-packet + demoted + editorial scans)
banked full reads: 2 (Anthropic Claude-shaped science → bank raw/ai/2026-10-02-matthew-schwartz-claude-shaped-science.md; Anthropic What work can robots do? → bank raw/ai/2026-10-02-anthropic-economics-what-work-can-robots-do.md)
truncation: weekly usage — keyword-core + combined≥9 for arxiv; craft filter + domain/vertical demotion; listing titles (+abstract skim on listing HTML) only; no PDF downloads; Sep/Oct-2026 arxiv ids only
calibration: packet_count=12 — no full re-calibration (packet-10 cut proposals for retrievalpractice.org + docs.x.ai/grok-bot/overview still await Wedge yes; intake-sources.md untouched)
