# grokbot.dev — 2026-09-13 education sweep (twentieth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-13-feed.json` (HTTP 200)
- **generated_at**: `2026-09-12T17:03:37.875Z` (00:03 ICT 13 Sep)
- **count**: **767 → 789** (+22 vs prior feed `scratch-2026-09-12-feed.json` generated_at `2026-09-11T12:25:09.268Z` count 767)
- newest_added_at: `2026-09-12T15:11:24.721Z` (22:11 ICT 12 Sep)
- types overall: template 587 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-12 feed**: **+22 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-30 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (853 URLs) — 0 new delta marketplace URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-11T12:25:09.268Z`; TRUE slug-diff = +22 −0 templates. 21 with added_at ≥ cutoff; 1 backfill `judd-the-bug` added_at 2026-09-10T18:03Z absent from prior feed)

1. `judd-the-bug` (2026-09-10T18:03Z, backfill) — digs Sentry for a sourced answer; developer/engineering — **library bounce**
2. `creador-de-facturas-arca` (2026-09-11T19:03Z) — ARCA e-invoicing + monthly Factura C PDFs; business/back-office — **library bounce**
3. `newspaper` (2026-09-11T19:41Z) — one-page morning broadsheet that explains how one thing works; personal/news/`learning` — **library bounce** (has `learning` cat but not language/tutor/Anki use-case; not roster)
4. `creator-shortlist-crew` (2026-09-11T22:24Z) — shortlist of creators worth partnering with; marketer/creator — **gate-only** (off-lane creator/marketer GTM; not roster)
5. `lookalike-scout` (2026-09-11T22:24Z) — name one company, get lookalikes; sales/marketer — **gate-only** (off-lane sales/GTM; not roster)
6. `serp-watch-team` (2026-09-11T22:24Z) — brand in search + AI answers; seo/marketer — **gate-only** (off-lane SEO/marketer GTM; not roster)
7. `rival-watch-desk` (2026-09-11T22:24Z) — standing competitor watch; marketer — **gate-only** (off-lane marketer GTM; not roster)
8. `icp-map-coach` (2026-09-11T22:24Z) — who could buy / who decides; sales/marketer — **gate-only** (off-lane sales/GTM; not roster)
9. `researcher` (2026-09-11T23:50Z) — research seat that trains other bots; developer/meta-bot — **library bounce**
10. `x-task-dispatcher` (2026-09-12T07:59Z) — routes X tasks to cheaper path; developer/meta-bot — **library bounce**
11. `skroutz` (2026-09-12T08:01Z) — price-hunt on Skroutz.gr; personal/shopping — **library bounce**
12. `store-setup-from-zero` (2026-09-12T10:01Z) — idea → shop page; business — **library bounce**
13. `weekly-p-l-analyst` (2026-09-12T10:01Z) — weekly financial readout; business/finance — **library bounce**
14. `paid-ads-manager` (2026-09-12T10:01Z) — paid acquisition creative→launch→triage; business/marketer — **gate-only** (off-lane ads/GTM; not roster)
15. `churn-retention-manager` (2026-09-12T10:01Z) — cancellations / failed payments; business/ops — **library bounce**
16. `store-from-template` (2026-09-12T10:01Z) — copy a working storefront for a niche; business — **library bounce**
17. `landing-page-generator` (2026-09-12T10:01Z) — sales page + checkout; business/marketer — **gate-only** (off-lane marketer/GTM; not roster)
18. `affiliate-program-operator` (2026-09-12T10:01Z) — creator affiliate programme ops; business/marketer — **gate-only** (off-lane affiliate/GTM; not roster)
19. `partner-referral-outreach` (2026-09-12T10:01Z) — referral network outreach; business/sales — **gate-only** (off-lane sales/GTM; not roster)
20. `ugc-bounty-manager` (2026-09-12T10:01Z) — creator clipping bounties; business/marketer — **gate-only** (off-lane creator/GTM; not roster)
21. `business-ops` (2026-09-12T10:01Z) — shop ops entry point / delegate; business/meta-bot — **library bounce**
22. `receipt-reaper` (2026-09-12T15:11Z) — finds forgotten software subscriptions; personal/finance — **library bounce**

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal/engineering — **not education lane**; none added since cutoff; all already in prior feed.
- No delta item is a **use-case**. One new template carries `learning` cat (`newspaper` — morning “how one thing works” broadsheet) — **library bounce**, not language/tutor/Anki roster. Closest other surfaces are meta-bot/ops (`researcher`, `x-task-dispatcher`, `business-ops`) and off-lane marketer/sales GTM clusters (`creator-shortlist-crew`, `lookalike-scout`, `serp-watch-team`, `rival-watch-desk`, `icp-map-coach`, `paid-ads-manager`, `landing-page-generator`, `affiliate-program-operator`, `partner-referral-outreach`, `ugc-bounty-manager`) — all **library / gate-only bounce**.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 724844 bytes written.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Feed `generated_at` dated 2026-09-12 (API rebuilt since yesterday’s sweep which still showed Sep-11 `generated_at`).
- One slug-diff backfill: `judd-the-bug` (added_at 2026-09-10) missing from prior feed, present now.
- Twentieth sweep (yesterday nineteenth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 22 new slugs → **bounce as library** (22 templates; slug-diff matches; 21 in-window + 1 backfill).
- Off-lane gate-only notes (not roster): `creator-shortlist-crew`, `lookalike-scout`, `serp-watch-team`, `rival-watch-desk`, `icp-map-coach`, `paid-ads-manager`, `landing-page-generator`, `affiliate-program-operator`, `partner-referral-outreach`, `ugc-bounty-manager` (marketer/sales/creator/SEO GTM).
