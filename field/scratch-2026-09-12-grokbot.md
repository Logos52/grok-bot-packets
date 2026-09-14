# grokbot.dev — 2026-09-12 education sweep (nineteenth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-12-feed.json` (HTTP 200)
- **generated_at**: `2026-09-11T12:25:09.268Z` (19:25 ICT 11 Sep)
- **count**: **755 → 767** (+12 vs prior feed `scratch-2026-09-11-feed.json` generated_at `2026-09-11T00:25:09.615Z` count 755)
- newest_added_at: `2026-09-11T11:55:24.000Z` (18:55 ICT 11 Sep)
- types overall: template 565 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-11 feed**: **+12 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-30 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (826 URLs) — 0 new delta marketplace URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-11T00:25:09.615Z`; 12 templates with added_at ≥ cutoff; slug-diff = +12 −0, all in-window)

1. `linkedin-watch` (2026-09-11T00:42Z) — scheduled LinkedIn digest (feed/messages/invites/views/jobs); personal/marketer — **gate-only** (off-lane marketer/recruiting GTM; not roster)
2. `announcr-voice` (2026-09-11T00:44Z) — speaks other bots' updates out loud; personal/meta-bot — **library bounce**
3. `clickbait-skipper` (2026-09-11T01:48Z) — skips padding; says what a video/podcast actually says; personal/research/content — **library bounce**
4. `usage-bot` (2026-09-11T03:04Z) — watches Grok Bot quota left, tells other bots; developer/ops/meta-bot — **library bounce**
5. `the-chief` (2026-09-11T03:48Z) — daily roll-call for a roster of specialist bots; ops/agent-team — **library bounce**
6. `chief-of-staff-cursor-relay` (2026-09-11T07:32Z) — delegates to a Cursor cloud agent and relays result (参谋长); developer/meta-bot — **library bounce**
7. `sales-orchestrator` (2026-09-11T10:07Z) — traffic control for a group chat of sales bots; sales/business — **gate-only** (off-lane sales/GTM; not roster)
8. `albert` (2026-09-11T10:36Z) — police union contracts → side-by-side spreadsheets; business/ops/data — **library bounce**
9. `the-morning-newspaper` (2026-09-11T11:26Z) — printed front page of your own day by breakfast; personal/productivity — **library bounce**
10. `billionairebot` (2026-09-11T11:34Z) — finds someone to pay to kill an annoying errand; personal/life-hacks — **library bounce**
11. `optima` (2026-09-11T11:49Z) — clears dead rules other bots still obey; developer/ops/meta-bot — **library bounce**
12. `fed-x-brief` (2026-09-11T11:55Z) — weekday Fed brief + whether to post/quote/wait on X; creator/investor — **gate-only** (off-lane creator/social GTM; not roster)

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal/engineering — **not education lane**; none added since cutoff; all already in prior feed.
- No delta item is a **use-case**. No new template carries `learning`/`education` cat. Closest surfaces are meta-bot/ops (`the-chief`, `usage-bot`, `optima`, `chief-of-staff-cursor-relay`) and off-lane GTM (`linkedin-watch`, `sales-orchestrator`, `fed-x-brief`) — all **library / gate-only bounce**, not language/tutor/Anki roster.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.
- Note only (not news item): template `chief-of-staff-cursor-relay` mentions Cursor cloud agents as a capability — still **library bounce**, not a Brief news announcement.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 703524 bytes written.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Feed `generated_at` still dated 2026-09-11 (API had not rolled a Sep-12 rebuild by sweep time); delta is vs prior Sep-11 morning feed.
- Nineteenth sweep (yesterday eighteenth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 12 new slugs → **bounce as library** (12 templates since cutoff; slug-diff matches window).
- Off-lane gate-only notes (not roster): `linkedin-watch`, `sales-orchestrator`, `fed-x-brief` (marketer/sales/creator GTM).
