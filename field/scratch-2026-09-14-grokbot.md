# grokbot.dev — 2026-09-14 education sweep (twenty-first)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-14-feed.json` (HTTP 200)
- **generated_at**: `2026-09-13T12:24:49.272Z` (19:24 ICT 13 Sep)
- **count**: **789 → 810** (+21 vs prior feed `scratch-2026-09-13-feed.json` generated_at `2026-09-12T17:03:37.875Z` count 789)
- newest_added_at: `2026-09-13T11:37:04.000Z` (18:37 ICT 13 Sep)
- types overall: template 608 · use-case 138 · plugin 46 · collection 16 · news 2
- **delta vs Sep-13 feed**: **+21 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-30 and none new are education/tutor/Anki lane.
- Skip list: `scratch-seen-urls.txt` (885 URLs) — 0 new delta marketplace URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-12T17:03:37.875Z`; TRUE slug-diff = +21 −0 templates. 13 with added_at ≥ cutoff; 8 backfill absent from prior feed)

1. `gb-gf-victoria` (2026-09-12T06:31Z, backfill) — A fictional companion who reaches out around your day; personal/wellbeing — **library bounce**
2. `weekend-edition` (2026-09-12T15:44Z, backfill) — Collects a week of saved reading into a printable paper; personal/content/`learning` — **library bounce** (has `learning` cat but not language/tutor/Anki use-case; not roster)
3. `task-farming` (2026-09-12T15:54Z, backfill) — Turns meeting/chat agreements into tickets; business/ops — **library bounce**
4. `alumni-coffee-chat-finder` (2026-09-12T16:27Z, backfill) — Finds university alumni for coffee chats; personal/`student`/recruiting — **library bounce** (`student` cat = recruiting, not language/tutor/Anki; not roster)
5. `handshake-job-applier` (2026-09-12T16:27Z, backfill) — Handshake board → submitted applications; personal/`student`/recruiting — **library bounce** (`student` recruiting, not education lane; not roster)
6. `swe-job-applier` (2026-09-12T16:27Z, backfill) — Engineering internship chase via Simplify; personal/`student`/recruiting — **library bounce** (`student` recruiting, not education lane; not roster)
7. `yc-startup-job-applier` (2026-09-12T16:27Z, backfill) — Work at a Startup profile + founder messages; personal/`student`/recruiting — **library bounce** (`student` recruiting, not education lane; not roster)
8. `recruiter-email-finder` (2026-09-12T16:27Z, backfill) — Finds hiring contacts at target employers; personal/`student`/recruiting — **library bounce** (`student` recruiting, not education lane; not roster)
9. `maples-stylist` (2026-09-12T17:50Z) — MapleStory outfit builder; personal/gaming/`creator` — **library bounce** (creator cat incidental; not marketer GTM roster)
10. `do-not-pay` (2026-09-12T19:12Z) — Pushes back on unjustified charges + writes the letter; personal/finance — **library bounce**
11. `alibaba-buyer-ops` (2026-09-12T19:56Z) — Day-to-day factory buying on Alibaba; business/ops — **library bounce**
12. `berliner` (2026-09-12T22:07Z) — Weekly Berlin techno playlist with listening notes; personal/`creator`/content — **library bounce** (creator cat incidental; not marketer GTM roster)
13. `paige-turner` (2026-09-12T22:35Z) — Librarian for a bot team — answer from sources; developer/knowledge-base — **library bounce**
14. `root-agent` (2026-09-12T23:52Z) — Sets goal, assembles smallest team, reports back; business/meta-bot — **library bounce**
15. `text-cleanup` (2026-09-13T01:10Z) — Cleans writing into one send-ready version; personal/productivity — **library bounce**
16. `sweeper-credit-saver` (2026-09-13T02:30Z) — Shows bot credit burn and cuts wasteful wake-ups; developer/ops — **library bounce**
17. `nuggetbot` (2026-09-13T05:33Z) — Podcast best-lines → post-ready graphics; creator/marketer/social — **gate-only** (off-lane creator/marketer GTM; not roster)
18. `memory-steward` (2026-09-13T06:54Z) — Mirrors each bot setup/memory into private Git; developer/ops — **library bounce**
19. `grok-bot-directory` (2026-09-13T09:40Z) — Describe a job → points at shared bot that does it; developer/meta-bot — **library bounce**
20. `cto-bot` (2026-09-13T09:47Z) — Audits how engineering org is running; developer/business — **library bounce**
21. `jre-point-campaigns` (2026-09-13T11:37Z) — Registers for open JRE POINT campaigns; personal/life-hacks — **library bounce**

## Plugin delta — bounce as library
- **0** new plugins (catalog still plugin=46).

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog remain Aug GTM/personal/engineering — **not education lane**; none added since cutoff; all already in prior feed.
- No delta item is a **use-case**. Surfaces with `learning`/`student` cats are templates only: `weekend-edition` (`learning` printable reading digest) and the student-recruiting cluster (`alumni-coffee-chat-finder`, `handshake-job-applier`, `swe-job-applier`, `recruiter-email-finder`, `yc-startup-job-applier`) — all **library bounce**, not language/tutor/Anki roster. Closest other surfaces are meta-bot/ops (`paige-turner`, `root-agent`, `grok-bot-directory`, `memory-steward`, `sweeper-credit-saver`, `cto-bot`) and one off-lane creator/marketer GTM (`nuggetbot`) — **library / gate-only bounce**.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged: `grok-bot-templates-explained`, `lennys-newsletter-free-month-grok-bot`). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 745111 bytes written.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Feed `generated_at` dated 2026-09-13 (API rebuilt since yesterday’s sweep which still showed Sep-12 `generated_at`).
- Slug-diff backfills (8): `gb-gf-victoria`, `weekend-edition`, `task-farming`, `alumni-coffee-chat-finder`, `handshake-job-applier`, `swe-job-applier`, `yc-startup-job-applier`, `recruiter-email-finder` (added_at before prior `generated_at`, missing from prior feed, present now).
- Twenty-first sweep (yesterday twentieth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 21 new slugs → **bounce as library** (21 templates; slug-diff matches; 13 in-window + 8 backfill).
- Off-lane gate-only notes (not roster): `nuggetbot` (creator/marketer GTM).
