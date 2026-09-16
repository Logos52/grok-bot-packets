# grokbot.dev — 2026-09-16 education sweep (twenty-third)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-16-feed.json` + convenience copy `feed.json` (HTTP 200)
- **generated_at**: `2026-09-15T12:30:01.042Z` (19:30 ICT 15 Sep)
- **count**: **822 → 831** (+9 vs prior feed `scratch-2026-09-15-feed.json` generated_at `2026-09-14T17:04:06.795Z` count 822)
- newest_added_at: `2026-09-15T11:59:20.000Z` (18:59 ICT 15 Sep)
- types overall: template 629 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-15 feed**: **+9 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-30 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (962 URLs) — 0 new delta marketplace URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-14T17:04:06.795Z`; TRUE slug-diff = +9 −0 templates. 7 with added_at ≥ cutoff; 2 backfill)

1. `teslaway` (2026-09-14T13:01Z, **backfill**) — Finds used Teslas near a ZIP and emails a shortlist; personal/shopping/research — **library bounce**
2. `voice-receipt-ledger` (2026-09-14T15:54Z, **backfill**) — Private ledger from typing / receipt photos / voice; personal/finance — **library bounce**
3. `e-mail-organizer` (2026-09-14T18:42Z) — Files one Gmail by vendor, invoices separate; business/email/back-office — **library bounce**
4. `grottle` (2026-09-14T19:26Z) — Clearer fuel gauge for weekly Grok Bot usage; personal/developer/meta-bot — **library bounce**
5. `commitments` (2026-09-14T19:41Z) — Logs work promises and holds them open till done; personal/business/productivity — **library bounce**
6. `tin-el-investigador` (2026-09-14T21:14Z) — Question → ready-to-post Spanish update daily; creator/content/social + cat `learning` — **gate-only** (off-lane creator GTM; Spanish = content language, not language/tutor/Anki; not roster)
7. `lienzo` (2026-09-14T23:49Z) — Design links → questionable reference library; personal/design/knowledge-base — **library bounce**
8. `prospect-drafts` (2026-09-15T11:35Z) — Prospects + first-touch email left in drafts; business/sales/marketer/growth — **gate-only** (off-lane sales/GTM; not roster)
9. `flippy` (2026-09-15T11:59Z) — Daily mint-phase heads-up for wallets; personal/crypto/monitoring — **library bounce**

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal/engineering — **not education lane**; none added since cutoff; all already in prior feed.
- No delta item is a **use-case**. Weak keyword false-positives on templates only: `teslaway` summary substring “esl” inside “Teslas”; `tin-el-investigador` has cat `learning` + Spanish updates — creator voice/content, **not** language/tutor/Anki. Closest other surfaces are personal ops (`voice-receipt-ledger`, `commitments`, `grottle`, `flippy`), design KB (`lienzo`), and email back-office (`e-mail-organizer`) — all **library bounce**. Off-lane creator/sales GTM: `tin-el-investigador`, `prospect-drafts` — **gate-only**.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 764882 bytes written (`scratch-2026-09-16-feed.json`; copied to `feed.json`).
- RSS / browser fallback not needed. No Firecrawl.
- Removed slugs vs prior: 0.
- Feed `generated_at` dated 2026-09-15 (API rebuilt since yesterday’s sweep which still showed Sep-14 `generated_at`).
- Slug-diff backfills: 2 (`teslaway`, `voice-receipt-ledger` added_at before prior `generated_at`); 7 in-window.
- Twenty-third sweep (yesterday twenty-second).
- Scratch only — did **not** write field-seen.json, latest.md, or field-packet-*.md.

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 9 new slugs → **bounce as library** / gate-only (9 templates; slug-diff matches; 7 in-window + 2 backfill).
- Off-lane gate-only notes (not roster): `tin-el-investigador`, `prospect-drafts` (creator/sales GTM).
