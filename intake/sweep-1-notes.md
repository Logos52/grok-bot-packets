# Sweep 1 notes — manual 1/3
window: 2026-08-19T00:00:00+08:00 — 2026-08-26T17:45:10+08:00 (Asia/Taipei)
fetched_at_utc: 2026-08-26T09:45:10Z

## Per-source fetch

| source | method | status | notes |
|---|---|---|---|
| anthropic.com/research | WebFetch + curl for slugs | ok | listing + publications table |
| x.ai/news | WebFetch timeout; curl HTML ok | ok | Next.js listing; dates from visible cards |
| docs.x.ai/grok-bot/overview | WebFetch ok | not a find | already in seen (Field bounce). Product/docs landing. Exact URL not re-queued. |
| arxiv.org/list/cs.AI/new | WebFetch IDs only; curl HTML ok | ok | new listings Wed 26 Aug 2026; 117 new / 111 cross / 124 repl |
| arxiv.org/list/cs.CL/new | WebFetch IDs only; curl HTML ok | ok | 53 new / 36 cross / 74 repl |
| learningscientists.org/blog | WebFetch + curl | ok | dated posts extracted |
| retrievalpractice.org | WebFetch + curl | ok | landing/catalog; no dated new post in window |

failed sources: none (x.ai/news recovered via curl)

## Counts

- pinned sources attempted: 7
- sources with usable listing: 7
- failed: 0
- packet items (≥6): 18
- below threshold (considered): 48
- new URLs added to seen index: 66
- Field-bounce entries kept: 34
- grok-bot overview: already seen; not added again

## Truncation

Arxiv new-submission titles+listing abstracts only. Replacements skipped. Cross-lists not scored unless they also appeared as new in cs.AI/cs.CL.
cs.AI: keyword-filtered 41 of 117 new titles (agent/workflow/tool/eval/memory/tutor/wiki/skill/harness/handoff).
cs.CL: scored 12 unique keyword hits (2 packeted, 10 below); did not walk the other 41 new titles.
Did not fetch individual arxiv abs pages.

## Below-threshold (short)

Anthropic: protein design (Aug 18, science app), worker retraining (Aug 12), Riemann/math (Aug 10).
x.ai: Grok 4.6 on Gemini Enterprise Agent Platform (Aug 21), Amazon Bedrock (Aug 19), Grok Build on web/mobile (Aug 19), Grok 4.6 in GitHub Copilot (Aug 14) — distribution/surface, not new workflow research.
Learning Scientists Aug 14: KISS call-for-practice + 2020 spaced-practice repost.
retrievalpractice.org: no dated new item; old strategy pages (2018–2022) and book landing not treated as finds.
Arxiv below: domain agent apps (medical, tax, trading, radiology, GUI, voice), serving/KV memory, incremental RAG/RL/search-agent papers. See intake-seen.json.

## Wiki

No in-window first-party item on how people maintain public knowledge systems.
