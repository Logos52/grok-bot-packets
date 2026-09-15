# grokbot.dev — 2026-09-15 education sweep (twenty-second)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-15-feed.json` (HTTP 200)
- **generated_at**: `2026-09-14T17:04:06.795Z` (00:04 ICT 15 Sep)
- **count**: **810 → 822** (+12 vs prior feed `scratch-2026-09-14-feed.json` generated_at `2026-09-13T12:24:49.272Z` count 810)
- newest_added_at: `2026-09-14T16:14:52.626Z` (23:14 ICT 14 Sep)
- types overall: template 620 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-14 feed**: **+12 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-30 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (929 URLs) — 0 new delta marketplace URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-13T12:24:49.272Z`; TRUE slug-diff = +12 −0 templates. 12 with added_at ≥ cutoff; 0 backfill)

1. `visa-japan-offer-draws` (2026-09-13T12:52Z) — Plays unused Visa Japan offer draws; personal/life-hacks/saving-money — **library bounce** (Japan = visa offers, not language/tutor)
2. `wechat-alipay-bill-import` (2026-09-13T14:19Z) — Files WeChat/Alipay statements into a ledger; personal/finance — **library bounce**
3. `travel-agent-scott` (2026-09-13T15:41Z) — Researches trips and stages bookings; personal/travel — **library bounce**
4. `about-me` (2026-09-13T17:06Z) — Running read on your state for other bots; personal/wellbeing/meta — **library bounce**
5. `unstick-me` (2026-09-13T18:38Z) — One small question until a stalled task starts; personal/productivity — **library bounce**
6. `grocery-bot` (2026-09-13T19:10Z) — Grocery receipts → spending + spoil flags; personal/shopping/food — **library bounce** (off-work grocery pattern; not roster)
7. `family-safety-monitor` (2026-09-13T21:38Z) — Parent posted on child’s apps without reading messages; personal/family — **library bounce**
8. `x-writer` (2026-09-14T03:05Z) — Learns an account’s voice, drafts posts; creator/content/social/growth — **gate-only** (off-lane creator/marketer GTM; “Learns” ≠ language learning; not roster)
9. `glasser` (2026-09-14T05:29Z) — Reaches paid business-data sources without API-key drawer; research/business — **library bounce**
10. `nessie` (2026-09-14T06:00Z) — Sketches a national dividend / who pays; research/finance — **library bounce**
11. `reply-radar` (2026-09-14T11:42Z) — Catches climbing conversations + drafts reply; creator/social/growth — **gate-only** (off-lane creator GTM; not roster)
12. `vetstack` (2026-09-14T16:14Z) — Savings desk for military life; personal/finance — **library bounce**

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal/engineering — **not education lane**; none added since cutoff; all already in prior feed.
- No delta item is a **use-case**. Weak keyword false-positive: `x-writer` summary “Learns how an account writes” — creator voice clone, **not** language/tutor/Anki. Closest other surfaces are personal ops (`about-me`, `unstick-me`, `grocery-bot`, `family-safety-monitor`, `vetstack`) and research (`glasser`, `nessie`) — all **library bounce**. Off-lane creator/social GTM: `x-writer`, `reply-radar` — **gate-only**.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 756384 bytes written.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Feed `generated_at` dated 2026-09-14 (API rebuilt since yesterday’s sweep which still showed Sep-13 `generated_at`).
- Slug-diff backfills: 0 (all 12 in-window vs prior `generated_at`).
- Twenty-second sweep (yesterday twenty-first).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 12 new slugs → **bounce as library** (12 templates; slug-diff matches; 12 in-window + 0 backfill).
- Off-lane gate-only notes (not roster): `x-writer`, `reply-radar` (creator/social GTM).
