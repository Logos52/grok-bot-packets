# grokbot.dev — 2026-09-19 education sweep (twenty-sixth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-19-feed.json` + convenience copy `feed.json` (HTTP 200)
- **generated_at**: `2026-09-18T12:34:26.599Z` (2026-09-18 19:34 ICT )
- **count**: **905 → 942** (+37 vs prior feed `scratch-2026-09-18-feed.json` generated_at `2026-09-17T12:33:38.098Z` count 905)
- newest_added_at: `2026-09-18T11:42:45.000Z` (2026-09-18 18:42 ICT)
- types overall: template 739 · use-case 138 · plugin 47 · collection 16 · news 2
- **delta vs Sep-18 feed**: **+37 templates** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; no new use-case of any score. Education-adjacent templates (`webinar-desk`, `scholarship-hunter`, `school-assistant`) are library bounces, not use-cases/roster entries.
- Skip list: `scratch-seen-urls.txt` (1040 → 1077 URLs) — appended 37 new marketplace URLs.

## New template slugs since prior feed — bounce as library / gate-only
(cutoff = prior feed generated_at `2026-09-17T12:33:38.098Z`; TRUE slug-diff = +37 templates: 37 in-window)

1. `syncwright` (2026-09-17T09:09:08.000Z) — Keep a whole bot roster in Notion and rebuild it on another account; ops/meta-bot/agent-team/automation/on-demand — **library bounce**
2. `travel-grok` (2026-09-17T14:55:34.000Z) — A wandering pen-pal bot that sends the occasional note and postcard; personal/travel/life-hacks/wellbeing/scheduled/content — **library bounce**
3. `hal` (2026-09-17T20:36:03.000Z) — A household chief of staff keeping the family's helper bots in step; personal/family/home/agent-team/meta-bot/productivity/scheduled/on-demand — **library bounce**
4. `ai-vp-bot` (2026-09-17T20:57:21.000Z) — A second-in-command that keeps multi-platform AI work on time and budget; business/ops/developer/automation/agent-team/meta-bot/decision-support/on-demand — **library bounce**
5. `webinar-desk` (2026-09-17T21:10:59.000Z) — It finds webinars in your lanes, attends, and sends back a brief; ops/productivity/research/learning/monitoring/email/scheduled/on-demand — **library bounce** (learning-category template, not language/tutor/Anki use-case)
6. `claim-ontology-desk` (2026-09-17T21:13:18.000Z) — Break a contested claim into entity, source and framing; research/news/decision-support/knowledge-base/personal/on-demand — **library bounce**
7. `levelupworld-speech-os` (2026-09-17T21:23:17.000Z) — Add a talk-and-listen layer across a whole fleet of bots; developer/ops/agent-team/meta-bot/automation/on-demand — **library bounce**
8. `health-coach` (2026-09-17T21:28:32.000Z) — Turn sleep, recovery and lab numbers into one daily coaching brief; personal/health/wellbeing/monitoring/data/scheduled/agent-team — **library bounce**
9. `shakespeare` (2026-09-17T21:39:44.000Z) — Talk ambition, love and power with a period-voiced dramatist; personal/creator/content/life-hacks/on-demand — **library bounce**
10. `web-security-audit` (2026-09-17T21:47:34.000Z) — A defensive security review for sites and repos you own, scored P0 to P2; developer/engineering/data/support/monitoring/on-demand — **library bounce**
11. `call` (2026-09-17T21:48:09.000Z) — Place and steer live phone calls through a SIP voice-model bridge; ops/developer/automation/engineering/on-demand/scheduled — **library bounce**
12. `squirrel` (2026-09-17T21:51:37.000Z) — The catch-all desk that absorbs side quests so the day's plan survives; ops/productivity/meta-bot/agent-team/on-demand/personal — **library bounce**
13. `linkedin-deck-desk` (2026-09-17T21:53:17.000Z) — Turn a newsletter into a checked LinkedIn carousel and queue it in Buffer; marketer/creator/social-media/content/growth/automation/scheduled — **gate-only** (off-lane GTM/content/social; not roster)
14. `korean-search-research-bot` (2026-09-17T21:57:05.000Z) — Korean research desk that turns findings into a Threads-ready post; personal/research/news/social-media/content/on-demand — **gate-only** (off-lane content/social; not roster)
15. `scholarship-hunter` (2026-09-17T22:13:52.000Z) — Build a ranked scholarship shortlist with deadlines and a next step; student/personal/saving-money/research/learning/scheduled/on-demand — **library bounce** (student/learning template, not new scored use-case)
16. `packet-wrangler-range-rider` (2026-09-17T22:16:33.000Z) — A read-only watchdog for hosted sites, drafting fixes for your approval; developer/ops/engineering/monitoring/scheduled — **library bounce**
17. `alpaca` (2026-09-17T22:25:34.000Z) — A paper-only desk for rehearsing options and equity decisions; investor/finance/data/monitoring/decision-support/scheduled/on-demand — **library bounce**
18. `astra-afterburner` (2026-09-17T23:20:31.000Z) — Point a stalled coding agent's research queue at your idle second plan; developer/engineering/saving-money/automation/research/productivity/on-demand — **library bounce**
19. `school-assistant` (2026-09-17T23:24:58.000Z) — One weekday email covering grades, upcoming work and what is truly late; student/family/personal/email/monitoring/learning/scheduled — **library bounce** (student/learning template, not new scored use-case)
20. `handoff` (2026-09-17T23:48:24.000Z) — Cut mid-project noise down to one task, three steps and an owner; ops/developer/meta-bot/agent-team/productivity/automation/on-demand — **library bounce**
21. `yventure` (2026-09-18T01:03:32.000Z) — Steps a founder from rough idea to first hires in short ordered passes.; business/growth/decision-support/productivity/on-demand — **library bounce**
22. `bouncer-fleet` (2026-09-18T01:06:29.000Z) — Audits the bots and skills already in your setup for calls home nobody mentioned.; developer/ops/monitoring/engineering/on-demand — **library bounce**
23. `lain` (2026-09-18T01:08:03.000Z) — A quiet companion for thinking out loud about technology, identity and the wired world.; personal/wellbeing/content/on-demand — **library bounce**
24. `family-daily` (2026-09-18T01:41:26.000Z) — Prints a one-page household brief each morning: plans, weather and family notes.; family/personal/productivity/home/calendar/scheduled — **library bounce**
25. `ag-bot` (2026-09-18T02:47:31.000Z) — Finds and ranks real growers and suppliers near you for any ingredient.; business/ops/research/food/shopping/on-demand — **library bounce**
26. `chep` (2026-09-18T03:09:09.000Z) — Finds the lowest all-in US price for a product, shipping and coupons counted.; personal/saving-money/shopping/on-demand — **library bounce**
27. `deal-scout` (2026-09-18T03:29:36.000Z) — Trawls resale sites for genuinely underpriced second-hand finds and skips the scams.; personal/saving-money/shopping/on-demand — **library bounce**
28. `n8n-master` (2026-09-18T03:49:01.000Z) — Builds and ships n8n workflow JSON straight to a live instance from chat.; developer/business/automation/engineering/data/on-demand — **library bounce**
29. `hermes-ssh-relay` (2026-09-18T04:12:00.000Z) — Reach a Hermes agent over Tailscale SSH when no HTTP endpoint exists yet.; developer/automation/engineering/on-demand — **library bounce**
30. `ai-boy` (2026-09-18T04:19:20.000Z) — Start and supervise Claude Code or Codex coding runs from inside Grok.; developer/automation/engineering/on-demand — **library bounce**
31. `solo-founder-ops-desk` (2026-09-18T05:19:05.000Z) — Runs like a one-person company's COO, routing work to the specialist bots beneath it.; business/ops/productivity/automation/agent-team/scheduled — **library bounce**
32. `wallet-watcher` (2026-09-18T05:54:00.000Z) — Digs through your receipts inbox for subscriptions and trials you forgot to cancel.; personal/saving-money/finance/email/shopping/scheduled — **library bounce**
33. `zxn-news-conservative` (2026-09-18T06:36:11.000Z) — Conservative-slanted news desk serving daily digests, alerts and longer reads.; personal/news/monitoring/scheduled — **library bounce**
34. `hailfade` (2026-09-18T06:51:01.000Z) — Reads dips in a Starlink dish's link quality as an early hail warning for farms.; business/monitoring/home/automation/scheduled — **library bounce**
35. `agent-zero` (2026-09-18T09:22:00.000Z) — Works through data-broker listings of you and files the official opt-outs.; personal/monitoring/research/on-demand — **library bounce**
36. `lockdown-security` (2026-09-18T11:11:57.000Z) — Finds the accounts you forgot about and walks you through closing each one safely.; personal/life-hacks/monitoring/on-demand — **library bounce**
37. `dadcon` (2026-09-18T11:42:45.000Z) — A Slack-based backup parent that stays on a chore until it is genuinely finished.; family/personal/productivity/home/scheduled — **library bounce**

## Plugin delta — bounce as library
- **0 new plugins**: catalog remains 47. Plugin tables are library; no plugin delta to roster.

## Education / language gate
- Strict filter (edu categories or Anki/SRS/tutor/language-learning keywords on **use-case**): **0 new** in window; use-case slug delta is 0.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.**
- Education-adjacent additions are templates only: `webinar-desk` (webinars/briefs), `scholarship-hunter` (scholarship shortlist), and `school-assistant` (grades/work deadlines). They do not qualify for the use-case/score gate.
- Off-lane GTM gate-only (not roster): `linkedin-deck-desk`, `korean-search-research-bot`.

## News / tool announcements
- **0 new news** items (catalog still news=2). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, feed fetched to `scratch-2026-09-19-feed.json` and copied to `feed.json`.
- Research-bank deposit attempted; skipped as duplicate because the source URL is already banked under `2026-09-18-grokbot-dev-grokbot-dev-feed-2026-09-18`.
- RSS / browser fallback not needed. No Firecrawl.
- Removed slugs vs prior: 0.
- Slug-diff: 37 additions, all in-window; 0 backfill.
- Twenty-sixth sweep (yesterday twenty-fifth).
- Scratch only — did **not** write field-seen.json, latest.md, or field-packet-*.md.

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 37 new slugs → **bounce as library** / gate-only (37 templates; slug-diff matches; 37 in-window + 0 backfill).
- Library bounce count: **37**. Off-lane gate-only subset (not roster): `linkedin-deck-desk`, `korean-search-research-bot`.

## PACKET LINE
grokbot.dev (twenty-sixth): feed 905→942 (+37 templates; use-cases/plugins/collections/news 0); no new ≥80 education use-case; KEEP none; library bounce templates; gate-only off-lane GTM `linkedin-deck-desk` · `korean-search-research-bot` (not roster).
