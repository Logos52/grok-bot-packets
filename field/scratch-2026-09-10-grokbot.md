# grokbot.dev — 2026-09-10 education sweep (seventeenth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-10-feed.json` (HTTP 200)
- **generated_at**: `2026-09-09T12:23:39.136Z` (19:23 ICT 9 Sep)
- **count**: **707 → 723** (+16 vs prior feed `scratch-2026-09-09-feed.json` generated_at `2026-09-08T12:24:51.547Z` count 707)
- newest_added_at: `2026-09-08T23:11:59.000Z` (06:11 ICT 9 Sep)
- types overall: template 521 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-9 feed**: **+16 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-30 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (750 URLs) — 0 new delta marketplace URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-08T12:24:51.547Z`; 14 templates with added_at ≥ cutoff; +2 pre-cutoff slugs appear in slug-diff vs Sep-9 file — listed for completeness)

1. `canonizer` (2026-09-08T13:00Z) — running status file across sessions; ops/knowledge-base
2. `personal-brand-desk` (2026-09-08T14:23Z) — top posts → five personal-brand drafts; creator/marketer — **gate-only** (off-lane GTM/content; not roster)
3. `blueberry-research-monitor` (2026-09-08T14:58Z) — morning blueberry-research briefing, quiet on empty; research/monitoring
4. `x-daily-posting-playbook` (2026-09-08T15:14Z) — daily X posting system; creator/social — **gate-only** (off-lane GTM; not roster)
5. `flights` (2026-09-08T16:49Z) — return-fare compare + price-drop watch; travel/shopping — **gate-only** (off-lane travel/deals; not roster)
6. `staypick` (2026-09-08T19:18Z) — neighbourhood pick before booking; travel
7. `ai-fitness-coach` (2026-09-08T21:05Z) — training/eating plan from available time/kit; health (has `learning` cat — still template/library, not language/tutor)
8. `telnyx` (2026-09-08T21:56Z) — Telnyx empty→first live test walkthrough; developer (has `learning` cat — product setup, not language/tutor lane)
9. `guide` (2026-09-08T22:02Z) — booked trip → day-by-day plan; travel
10. `adventure-bot` (2026-09-08T22:48Z) — one map-pin outing for time+mood; travel/events
11. `gamer-bro` (2026-09-08T22:48Z) — gaming news/deals + stock alerts; shopping/monitoring — **gate-only** (off-lane shopping; not roster)
12. `benebot` (2026-09-08T23:01Z) — plain-language benefits entitlement explainer; personal/support
13. `rezbot` (2026-09-08T23:01Z) — find open table + book restaurant; food/automation
14. `social-media-by-eclincher` (2026-09-08T23:11Z) — schedule posts + reply to comments/DMs/reviews; marketer — **gate-only** (off-lane GTM/social desk; not roster)

Pre-cutoff slugs present in delta file compare only:
- `omni-grok-bot` (2026-09-04T22:44Z) — ethics-first companion, no file access; personal/wellbeing — **library bounce** (template; added_at before prior generated_at)
- `koe` (2026-09-05T09:06Z) — twelve-month thinking coach (self-fill plan); personal/creator (has `learning` cat — thinking coach, **not** language/tutor/Anki use-case) — **library bounce**

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal (marketing-os, Amazon cart, machine→team, email, content/marketing OS, hedge fund, CRM, CFO, etc.) — **not education lane**; none added since cutoff; all already in prior feed.
- No delta item is a **use-case**. Closest learning surfaces are templates only: `koe` (thinking coach), `ai-fitness-coach` (fitness plan), `telnyx` (API setup walkthrough) — all **library bounce**, not language/tutor/Anki roster.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 661859 bytes written.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Seventeenth sweep (yesterday sixteenth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 16 new slugs → **bounce as library** (14 templates since cutoff + 2 pre-cutoff `omni-grok-bot`, `koe`).
- Off-lane gate-only notes (not roster): `personal-brand-desk`, `x-daily-posting-playbook`, `social-media-by-eclincher` (GTM/content); `flights`, `gamer-bro` (travel/shopping deals).
