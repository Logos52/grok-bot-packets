# grokbot.dev — 2026-09-18 education sweep (twenty-fifth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-18-feed.json` + convenience copy `feed.json` (HTTP 200)
- **generated_at**: `2026-09-17T12:33:38.098Z` (19:33 ICT 17 Sep)
- **count**: **872 → 905** (+33 vs prior feed `scratch-2026-09-17-feed.json` generated_at `2026-09-16T12:32:12.643Z` count 872)
- newest_added_at: `2026-09-17T10:08:25.000Z` (17:08 ICT 17 Sep)
- types overall: template 702 · use-case 138 · plugin 47 · collection 16 · news 2
- **delta vs Sep-17 feed**: **+33 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; no new use-case of any score. Education-adjacent templates (`learning-dna`, `homebase`, `jarvis-davesacritic`) are library bounces, not use-cases/roster entries.
- Skip list: `scratch-seen-urls.txt` (995 → 1028 URLs) — appended 33 new marketplace URLs.

## New template slugs since prior feed — bounce as library / gate-only
(cutoff = prior feed generated_at `2026-09-16T12:32:12.643Z`; TRUE slug-diff = +33 templates: 32 in-window + 1 backfill)

1. `skool-community-bot` (2026-09-14T16:31Z) — Skool community members/posts/questions; support/community — **library bounce** (backfill; not language/tutor)
2. `grok-pot` (2026-09-16T20:19Z) — Household food planning and cart — **library bounce**
3. `property-visit` (2026-09-16T21:15Z) — Property-visit land/research pack — **library bounce**
4. `remote-grok-build` (2026-09-16T21:17Z) — Remote Grok Build setup — **library bounce**
5. `wainwright-manager` (2026-09-16T21:27Z) — Hire/onboard bot roles — **library bounce**
6. `fernando-arana` (2026-09-16T21:38Z) — WhatsApp read/draft stand-in — **library bounce**
7. `sniffbot` (2026-09-16T21:45Z) — Preflight-check a bot template — **library bounce** (learning category ≠ language tutor)
8. `blaise` (2026-09-16T21:47Z) — X contest-entry drafting; creator/marketer/growth — **gate-only** (off-lane GTM; not roster)
9. `moonshot` (2026-09-16T21:57Z) — Tech-podcast investor briefs — **library bounce**
10. `historian` (2026-09-16T22:14Z) — Voice-note day reconstruction — **library bounce**
11. `yusician` (2026-09-16T22:24Z) — Local song rendering — **library bounce**
12. `single-stock-options` (2026-09-16T22:46Z) — Option-chain read — **library bounce**
13. `clinic` (2026-09-16T22:54Z) — Bot-fleet health check — **library bounce**
14. `podcast-pipeline` (2026-09-16T22:57Z) — Research-to-published podcast — **library bounce**
15. `bochi-chan` (2026-09-16T23:09Z) — Anime companion — **library bounce**
16. `ownphonebot` (2026-09-16T23:14Z) — Callable phone number for assistant — **library bounce**
17. `house-cat` (2026-09-16T23:16Z) — Novelty fleet companion — **library bounce**
18. `xx-engineeringarteditor-xx` (2026-09-16T23:40Z) — Engineering-drawing editor — **library bounce**
19. `steve` (2026-09-17T00:19Z) — Engineering-spend Scrum voice — **library bounce**
20. `marketing-bot` (2026-09-17T01:16Z) — X launch copy; marketer/growth — **gate-only** (off-lane GTM; not roster)
21. `estack` (2026-09-17T01:16Z) — Coding steward — **library bounce**
22. `punto-tricolor-ops` (2026-09-17T02:55Z) — Business ops to bookings; sales/growth — **gate-only** (off-lane GTM; not roster)
23. `linkedin-bot` (2026-09-17T03:22Z) — LinkedIn history and messages; sales/marketer — **gate-only** (off-lane GTM; not roster)
24. `replay` (2026-09-17T03:25Z) — Marketing brief to social video — **gate-only** (off-lane GTM; not roster)
25. `little-x` (2026-09-17T04:13Z) — X/document tasks by email — **library bounce**
26. `dealer` (2026-09-17T04:40Z) — Repository stack summary card — **library bounce**
27. `home-hunter` (2026-09-17T04:59Z) — Apartment shortlist — **library bounce**
28. `nourishment` (2026-09-17T05:25Z) — Fridge-photo recipes — **library bounce**
29. `learning-dna` (2026-09-17T05:34Z) — Personalized subject-teaching assessment — **library bounce** (template, not new scored use-case)
30. `naver-gmail-morning-brief` (2026-09-17T05:56Z) — Korean email brief — **library bounce**
31. `homebase` (2026-09-17T06:21Z) — Homework/forms/shared calendar — **library bounce** (not language/tutor/Anki)
32. `jarvis-davesacritic` (2026-09-17T07:18Z) — Job, home-admin and study chief of staff — **library bounce** (not language/tutor/Anki)
33. `unicron` (2026-09-17T10:08Z) — Consolidated bot-fleet document — **library bounce**

## Plugin delta — bounce as library
- **0 new plugins**: catalog remains 47. Plugin tables are library; no plugin delta to roster.

## Education / language gate
- Strict filter (edu categories or Anki/SRS/tutor/language-learning keywords on **use-case**): **0 new** in window; use-case slug delta is 0.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**
- `learning-dna` is the only clearly learning-themed addition, but it is a template and does not qualify for the use-case/score gate. `homebase`/`jarvis-davesacritic` mention homework/study but are general household/admin templates.
- Off-lane GTM gate-only (not roster): `blaise`, `marketing-bot`, `punto-tricolor-ops`, `linkedin-bot`, `replay`.

## News / tool announcements
- **0 new news** items (catalog still news=2: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 833838 bytes written (`scratch-2026-09-18-feed.json`; copied to `feed.json`).
- Feed was deposited once in the research bank as `raw/ai/2026-09-18-grokbot-dev-grokbot-dev-feed-2026-09-18.md`.
- RSS / browser fallback not needed. No Firecrawl.
- Removed slugs vs prior: 0.
- Slug-diff backfill: 1 (`skool-community-bot`, added before prior generated_at); 32 additions are in-window.
- Twenty-fifth sweep (yesterday twenty-fourth).
- Scratch only — did **not** write field-seen.json, latest.md, or field-packet-*.md.

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 33 new slugs → **bounce as library** / gate-only (33 templates; 0 plugins; 32 in-window + 1 backfill).
- Off-lane gate-only notes (not roster): `blaise`, `marketing-bot`, `punto-tricolor-ops`, `linkedin-bot`, `replay`.

## PACKET LINE
grokbot.dev (twenty-fifth): feed 872→905 (+33 templates; use-cases/plugins/collections/news 0); no new ≥80 education use-case; KEEP none; library bounce templates; gate-only off-lane GTM `blaise` · `marketing-bot` · `punto-tricolor-ops` · `linkedin-bot` · `replay` (not roster).
