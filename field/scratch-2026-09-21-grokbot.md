# grokbot.dev — 2026-09-21 education sweep (twenty-eighth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-21-feed.json` + convenience copy `feed.json` (HTTP 200)
- **generated_at**: `2026-09-20T17:08:41.139Z` (2026-09-21 00:08 ICT for feed stamp; fetched 2026-09-21 ICT)
- **count**: **1000 → 1041** (+41 vs prior feed `scratch-2026-09-20-feed.json` generated_at `2026-09-19T17:04:48.110Z` count 1000)
- newest_added_at: `2026-09-20T12:53:53.531Z` (2026-09-20 19:53 ICT)
- types overall: template 836 · use-case 138 · plugin 49 · collection 16 · news 2
- **delta vs Sep-20 feed**: **+40 templates · +1 plugin** (use-cases 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; no new use-case of any score. Education-adjacent template `learnbot` is a library bounce, not a use-case/roster entry.
- Skip list: append new marketplace URLs to scratch-seen-urls on compile.

## New slugs since prior feed — bounce as library / gate-only
(cutoff = prior feed generated_at `2026-09-19T17:04:48.110Z`; TRUE slug-diff = +41: 40 templates + 1 plugin)

1. `kalshi` (2026-09-19T00:57:42.000Z) — Kalshi: Reads one event contract and lays out thesis, size and risk plainly; investor, research, decision-support, finance, on-demand — **library bounce**
2. `kindling-app` (2026-09-19T04:21:11.000Z) — Kindling App: Turns real app screenshots into punchy vertical video for launch posts; creator, marketer, content, design, video, growth, business — **gate-only** (off-lane GTM/content/social/sales; not roster)
3. `linkedin-lead-outreach` (2026-09-19T05:59:11.000Z) — LinkedIn Lead Outreach: Turns comments on a lead post into logged, qualified LinkedIn contacts; sales, marketer, business, social-media, automation, growth — **gate-only** (off-lane GTM/content/social/sales; not roster)
4. `moving-concierge` (2026-09-19T13:52:16.000Z) — Moving Concierge: Plain-spoken moving advice across DIY, hybrid and full-service; personal, home, travel, saving-money, decision-support, on-demand — **library bounce**
5. `x-agent` (2026-09-19T14:06:35.000Z) — X Agent: Scouts AI threads, drafts replies that sound like you, waits for your OK; personal, creator, social-media, content, productivity, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)
6. `x-hygiene` (2026-09-19T14:26:19.000Z) — X Hygiene: Audits your followers, prices the cleanup, then lists who to cut; personal, social-media, productivity, monitoring, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)
7. `grok-telegram` (2026-09-19T14:29:07.000Z) — Grok Telegram: Puts your bot behind Telegram DMs on a webhook that never calls the model; developer, engineering, support, automation, on-demand — **library bounce**
8. `mike` (2026-09-19T14:41:45.000Z) — Mike: Reads school and personal mail, flags what matters, asks first; personal, family, email, calendar, monitoring, scheduled — **library bounce**
9. `lead-scout` (2026-09-19T15:45:39.000Z) — Lead Scout: Finds nearby small firms whose sites are under-optimised for search; business, sales, marketer, seo, research, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)
10. `site-research` (2026-09-19T15:45:39.000Z) — Site Research: Turns a local-business dossier into a search and maps gap brief; business, marketer, seo, research, content, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)
11. `terminator` (2026-09-19T15:56:32.000Z) — Terminator: Audits your bot roster and argues who to keep, merge or retire; business, ops, meta-bot, knowledge-base, decision-support, on-demand — **library bounce**
12. `top-coder` (2026-09-19T16:04:39.000Z) — Top Coder: Codes to locked criteria, then proves every one with a test; developer, engineering, productivity, on-demand — **library bounce**
13. `token-efficiency-optimizer` (2026-09-19T16:04:59.000Z) — Token Efficiency Optimizer: Spots the runs where more spend cannot change the outcome; developer, business, engineering, monitoring, analytics, on-demand — **library bounce**
14. `game-builder` (2026-09-19T16:05:09.000Z) — Game Builder: Ships small playable games with real win states that work offline; creator, developer, content, engineering, on-demand — **library bounce**
15. `plant-field-os` (2026-09-19T16:30:30.000Z) — Plant Field OS: A field-sales day for industrial reps: plan, installed base, audit; business, sales, productivity, data, analytics, agent-team — **gate-only** (off-lane GTM/content/social/sales; not roster)
16. `chief-of-staff` (2026-09-19T17:12:44.000Z) — Chief of Staff: Opens the weekday with a brief and hands work to your bots; business, personal, productivity, agent-team, email, scheduled — **library bounce**
17. `deal-finder-ops` (2026-09-19T17:12:45.000Z) — Deal Finder Ops: Checks a coupon against a real cart and shows you the receipt; personal, shopping, saving-money, research, decision-support, on-demand — **library bounce**
18. `momentum` (2026-09-19T18:45:04.000Z) — Momentum: Nudges idle specialist bots and lines up the next zero-cost moves; business, sales, growth, agent-team, monitoring, scheduled — **gate-only** (off-lane GTM/content/social/sales; not roster)
19. `learnbot` (2026-09-19T19:31:56.000Z) — 💡 LearnBot: A single engineering word each day, explained for people who never code; personal, student, learning, engineering, scheduled, on-demand — **library bounce**
20. `restaurant-canceled-errors-order-recovery` (2026-09-19T19:43:54.000Z) — Restaurant Canceled/Errors Order Recovery: Finds cancelled or mis-billed delivery orders and files the claims; business, back-office, finance, automation, monitoring, scheduled — **library bounce**
21. `rv-trip-planner` (2026-09-19T21:42:28.000Z) — RV Trip Planner: Holds a multi-day RV route and checks overnight spots in real time; personal, travel, productivity, calendar, on-demand — **library bounce**
22. `dig-org-digest` (2026-09-19T22:12:03.000Z) — Dig | Org Digest: One company signal, five briefing altitudes from daily to annual; business, ops, productivity, knowledge-base, scheduled — **library bounce**
23. `arnie-actions-plans` (2026-09-19T22:15:19.000Z) — Arnie | Actions & Plans: Turns a workshop decision into a staged model change you approve; business, ops, productivity, automation, decision-support, on-demand — **library bounce**
24. `mat-analytics` (2026-09-19T22:19:46.000Z) — Mat | Analytics: Ask questions of your org schema and get reports, charts, no writes; business, ops, data, analytics, decision-support, on-demand — **library bounce**
25. `last-stop` (2026-09-19T22:23:10.000Z) — Last Stop: Keeps a public atlas of Grok bots and files each new find as a skill; developer, meta-bot, knowledge-base, research, monitoring, on-demand — **library bounce**
26. `piper-etl-pipelines` (2026-09-19T22:27:39.000Z) — Piper | ETL & Pipelines: Stands up and feeds the event-log store once your schema is settled; business, ops, data, engineering, automation, scheduled — **library bounce**
27. `jev` (2026-09-19T23:28:34.000Z) — Jev: Adds typed triage — category, severity, yes-or-no — to a Jev pipeline; developer, business, ops, automation, decision-support, on-demand — **library bounce**
28. `indexx` (2026-09-19T23:35:48.000Z) — INDEXX: Rebuilds your Instagram saves into a searchable library on your Mac; personal, creator, knowledge-base, content, data, on-demand — **library bounce**
29. `kampalo` (2026-09-20T00:00:00Z) — Kampalo: Brief synced Google and Meta ads, then pause a weak campaign only after you confirm.; marketing — **library bounce**
30. `the-list` (2026-09-20T00:12:40.268Z) — The List: Three lines in your own chat whenever a new bot lands in the directory; personal, monitoring, news, scheduled — **library bounce**
31. `legend-lead-ops` (2026-09-20T00:38:39.000Z) — Legend Lead Ops: Sorts roofing enquiries and drafts the follow-ups your quote handoff needs.; business, sales, support, email, ops, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)
32. `ryan-app-shop` (2026-09-20T00:42:02.000Z) — Ryan App Shop: Builds beginner-friendly mobile web apps with big tap targets and plain labels.; developer, creator, design, engineering, business, on-demand — **library bounce**
33. `sous` (2026-09-20T02:05:02.000Z) — Sous: Turns a fridge photo or a quick answer into dinner, and tracks the pantry.; personal, food, family, home, on-demand — **library bounce**
34. `grok-bot-troubleshooter` (2026-09-20T02:32:21.000Z) — Grok Bot Troubleshooter: Diagnoses why a bot in your fleet stalled and hands you the next concrete move.; developer, ops, support, monitoring, meta-bot — **library bounce**
35. `lee` (2026-09-20T02:43:16.000Z) — Lee: Fills shopping carts at the big-box stores from your list, then stops there.; personal, shopping, saving-money, productivity, on-demand — **library bounce**
36. `jevify` (2026-09-20T03:15:45.000Z) — Jevify: Turns your scoring and checking bots into batch-sweep siblings for big sets.; developer, automation, meta-bot — **library bounce**
37. `dexter-the-home-lab-boss` (2026-09-20T05:00:26.000Z) — Dexter the home lab boss: Maps your homelab first, then builds helpers for it only after you approve.; developer, engineering, home, meta-bot, automation, agent-team — **library bounce**
38. `x-reply-scout` (2026-09-20T05:22:56.000Z) — X Reply Scout: Finds X accounts worth talking to, then goes quiet - it never posts for you.; personal, creator, social-media, growth, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)
39. `fashion-stylist` (2026-09-20T07:37:12.000Z) — Fashion Stylist: Turns your own clothing photos into a virtual closet with try-on clips.; personal, shopping, design, content, creator, on-demand — **library bounce**
40. `lighting-specialist` (2026-09-20T08:46:03.000Z) — Lighting Specialist: A senior lighting designer for stage and building installs, plots to specs.; creator, design, engineering, content, on-demand — **library bounce**
41. `kampalo-ads-assistant` (2026-09-20T12:53:53.531Z) — Kampalo ads assistant: Briefs synced ad spend and ROAS, then drafts pauses you approve before anything changes.; marketer, business, analytics, monitoring, decision-support, on-demand — **gate-only** (off-lane GTM/content/social/sales; not roster)

## Plugin delta — bounce as library
- **+1 plugin**: `kampalo` (added_at 2026-09-20; surfaced in this feed). Plugin tables are library; no plugin delta to roster.

## Education / language gate
- Strict filter (edu categories or Anki/SRS/tutor/language-learning keywords on **new use-case**): **0 new**; use-case slug delta is 0.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.** Current feed has 28 score≥80 cards, all use-cases, and none is named education/language practice.
- Education-adjacent addition: `learnbot` (engineering word each day) is a template only; it does not qualify for the use-case/score gate.
- Off-lane GTM gate-only (not roster): `kindling-app`, `linkedin-lead-outreach`, `x-agent`, `x-hygiene`, `lead-scout`, `site-research`, `plant-field-os`, `momentum`, `legend-lead-ops`, `x-reply-scout`, `kampalo-ads-assistant`.

## News / tool announcements
- **0 new news** items (catalog still news=2). No Brief bounce one-liners.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, feed fetched to `scratch-2026-09-21-feed.json` and copied to `feed.json`.
- Research-bank: feed URL already banked prior days — skip duplicate deposit. No Firecrawl.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Slug-diff: 41 additions (40 templates + 1 plugin); several early template additions are feed-visibility/backfill entries with added_at before the prior snapshot.
- Twenty-eighth sweep (yesterday twenty-seventh).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 41 new slugs → **bounce as library** / gate-only.
- Library bounce count: **30**. Off-lane gate-only subset (not roster): `kindling-app` · `linkedin-lead-outreach` · `x-agent` · `x-hygiene` · `lead-scout` · `site-research` · `plant-field-os` · `momentum` · `legend-lead-ops` · `x-reply-scout` · `kampalo-ads-assistant`.

## PACKET LINE
grokbot.dev (twenty-eighth): feed 1000→1041 (+40 templates +1 plugin; use-cases/collections/news unchanged); no new ≥80 education use-case; KEEP none; library bounce templates+plugin; gate-only off-lane GTM/content/social/sales additions (not roster); alert=no.
