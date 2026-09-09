# grokbot.dev — 2026-09-09 education sweep (sixteenth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-09-feed.json` (HTTP 200)
- **generated_at**: `2026-09-08T12:24:51.547Z` (19:24 ICT 8 Sep)
- **count**: **699 → 707** (+8 vs prior feed `scratch-2026-09-08-feed.json` generated_at `2026-09-08T00:24:07.338Z` count 699)
- newest_added_at: `2026-09-08T11:19:37.000Z` (18:19 ICT 8 Sep)
- types overall: template 505 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-8 feed**: **+8 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-28 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (731 URLs) — 0 new delta URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-08T00:24:07.338Z`; 7 templates with added_at ≥ cutoff; +1 pre-cutoff slug appears in slug-diff vs Sep-8 file — listed for completeness)

1. `lg-laundry-specialist` (2026-09-08T00:34Z) — LG washer cycle starter; home/automation
2. `influencer-marketing-deal-desk` (2026-09-08T01:15Z) — creator deal pricing; marketer/social
3. `sean` (2026-09-08T01:25Z) — Dice/career-portal job applications; recruiting
4. `paste-ready` (2026-09-08T03:43Z) — half-formed bot idea → paste-ready name/title/desc; meta-bot
5. `calibre` (2026-09-08T03:59Z) — ebook format conversion in chat; personal/content
6. `wool-radar` (2026-09-08T04:56Z) — deal watcher (薅羊毛); shopping/saving-money — **gate-only** (off-lane shopping; not roster)
7. `producthunter` (2026-09-08T11:19Z) — Product Hunt + HN morning/evening digest; research/monitoring

Pre-cutoff slug present in delta file compare only:
- `proto` (2026-09-08T00:24:02Z) — three working prototypes for one product problem; developer/design — **library bounce** (template; added_at 5s before prior generated_at)

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal (Amazon cart, CFO, content/marketing OS, email harden/triage) — **not education lane**; none added since cutoff; all already in prior feed.
- No delta template carries `learning`/`education`/`tutor`/`anki` category. Closest shopping surface (`wool-radar`) is deal-monitor — **gate-only**, not roster.

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 647009 bytes written.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Sixteenth sweep (yesterday fifteenth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 8 new slugs → **bounce as library** (7 templates since cutoff + 1 pre-cutoff `proto`).
- Off-lane note only: `wool-radar` shopping/deals — gate, do not recommend as roster.
