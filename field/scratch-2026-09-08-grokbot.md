# grokbot.dev — 2026-09-08 education sweep (fifteenth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-08-feed.json` (HTTP 200)
- **generated_at**: `2026-09-08T00:24:07.338Z` (07:24 ICT 8 Sep)
- **count**: **668 → 699** (+31 vs prior feed `scratch-2026-09-07-feed.json` generated_at `2026-09-06T17:03:17.823Z` count 668)
- newest_added_at: `2026-09-07T23:37:28.000Z`
- types overall: template 497 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-7 feed**: **+30 templates · +1 plugin** (use-cases 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-28 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (687 URLs) — 0 new delta URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-06T17:03:17.823Z`; 28 templates with added_at ≥ cutoff; +2 pre-cutoff slugs appear in slug-diff vs Sep-7 file — listed for completeness)

1. `firewatch` (2026-09-06T17:30Z)
2. `three-kingdoms-illustrator` (2026-09-06T21:44Z)
3. `coach-g` (2026-09-06T22:26Z)
4. `sweeper` (2026-09-06T22:43Z)
5. `the-king` (2026-09-06T23:03Z)
6. `thrift` (2026-09-06T23:20Z)
7. `stellar-cartography` (2026-09-07T02:54Z)
8. `marketplace-bot` (2026-09-07T03:29Z)
9. `stack-sentinel` (2026-09-07T03:29Z)
10. `architecture-shorts-master` (2026-09-07T04:49Z)
11. `career-scout` (2026-09-07T04:50Z)
12. `recent-bookmarks-search-bot` (2026-09-07T07:44Z)
13. `product-promo-copywriter` (2026-09-07T08:52Z)
14. `social-ops-bot` (2026-09-07T10:56Z)
15. `chief-of-staff-travis-vanlife` (2026-09-07T11:45Z)
16. `ticker-wire` (2026-09-07T11:45Z)
17. `dr-disk-clean` (2026-09-07T13:15Z)
18. `discogs-bot` (2026-09-07T15:03Z)
19. `whatsapp-bot` (2026-09-07T15:05Z)
20. `todo` (2026-09-07T16:12Z)
21. `video-transcriber` (2026-09-07T19:10Z)
22. `unifi` (2026-09-07T19:24Z)
23. `fishing-bot` (2026-09-07T19:38Z)
24. `golf-caddie` (2026-09-07T19:38Z)
25. `realtor-bot` (2026-09-07T19:38Z)
26. `tire-kicker` (2026-09-07T22:04Z)
27. `exec-cos-digest` (2026-09-07T22:30Z)
28. `liveavatar-launchpad` (2026-09-07T23:37Z) — cats include learning; avatar demos one-tap — **library bounce** (template)

Pre-cutoff slugs present in delta file compare only:
- `serenity` (2026-09-05T14:18Z) — ticker alerts; finance/monitoring
- `korean-public-api` (2026-09-06T13:08Z) — KR gov open-API matcher for product ideas; not language-learning

## Plugin delta — bounce as library
- `centricmem` (2026-09-06T23:20Z) — hosted librarian / Markdown cards for agents — **plugin table → library bounce**

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog are all Aug GTM/personal (Amazon cart, CFO, content team, etc.) — **not education lane**; none added since cutoff; all already in prior feed.
- Template with `learning` cat in delta (`liveavatar-launchpad`) remains **marketplace library** — bounce per Field rule. Closest surface (learning cat) but product-demo launcher, not a named education use-case ≥80.

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 639512 bytes written.
- RSS fallback not needed.
- Removed slugs vs prior: 0.
- Fifteenth sweep (yesterday fourteenth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 31 new slugs → **bounce as library** (28 templates since cutoff + 2 pre-cutoff slug-diff + 1 plugin `centricmem`).
