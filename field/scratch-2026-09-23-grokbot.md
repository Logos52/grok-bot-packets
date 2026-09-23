# grokbot.dev — 2026-09-23 education sweep (thirtieth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-23-feed.json` + convenience copy `feed.json` (HTTP 200)
- **generated_at**: `2026-09-22T12:30:28.942Z` (2026-09-22 19:30 ICT feed stamp; fetched 2026-09-23 ICT)
- **count**: **1064 → 1090** (+26 vs prior feed `scratch-2026-09-22-feed.json` generated_at `2026-09-21T12:31:18.943Z` count 1064)
- newest_added_at: `2026-09-22T11:03:40.000Z` (2026-09-22 18:03 ICT)
- types overall: template 884 · use-case 138 · plugin 50 · collection 16 · news 2
- **delta vs Sep-22 feed**: **+26 templates** (plugins 0 · use-cases 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; no new use-case of any score. Learning-adjacent adds (`maxq-a-bot`, `firstlight`, `phare`, `atelier-building-taste`) are templates only → library bounce, not use-case/roster entries.
- Skip list: append new marketplace URLs to scratch-seen-urls on compile.

## New slugs since prior feed — bounce as library / gate-only
(cutoff = prior feed generated_at `2026-09-21T12:31:18.943Z`; TRUE slug-diff = +26: 26 templates)

1. `mediation-bot` (2026-09-21T13:10:40.000Z) — Mediation Bot: Coaches you through a hard conversation, then drafts the calmer reply.; personal/wellbeing/productivity — **library bounce**
2. `reimagination` (2026-09-21T14:02:15.000Z) — Reimagination: Retells any story under dials you set: era, stakes, point of view.; creator/content/video/design — **gate-only** (off-lane content/creator; not roster)
3. `2nd-brain-2` (2026-09-21T15:07:06.000Z) — 2nd Brain: One shared facts file your other bots all read before they start.; developer/productivity/knowledge-base/agent-team/meta-bot — **library bounce**
4. `jev-router` (2026-09-21T15:29:04.000Z) — Jev router: Fast yes-no and scoring calls, so the big model only runs when it earns it.; developer/meta-bot/automation/decision-support/analytics — **library bounce**
5. `pulse-2` (2026-09-21T16:09:57.000Z) — Pulse: Talks you through Windows gaming-laptop faults, riskiest fix last.; personal/support/productivity — **library bounce**
6. `deep-research` (2026-09-21T16:58:20.000Z) — Deep Research: Works a claim until it lands on something you can actually check.; personal/research/analytics/news — **library bounce**
7. `maxq-a-bot` (2026-09-21T18:00:55.000Z) — MaxQ&A Bot: Turns a rocket mission into a grade-banded lesson kit, no prep.; student/learning/video/news — **library bounce** (learning-adjacent template, not a use-case)
8. `movie-magic` (2026-09-21T18:32:25.000Z) — Movie Magic: Film picks, a running watchlist, and a weekly box-office roundup.; personal/video/analytics/content/scheduled — **library bounce**
9. `newsletterbot-by-contentdrips` (2026-09-21T18:58:36.000Z) — NewsletterBot by Contentdrips: Turns a newsletter link into branded social graphics and carousels.; creator/marketer/content/design/social-media — **gate-only** (off-lane GTM/social; not roster)
10. `longform-editor` (2026-09-21T19:01:34.000Z) — Longform Editor: Edits at manuscript scale: structure and pacing first, polish later.; creator/content/productivity — **gate-only** (off-lane content/creator; not roster)
11. `firstlight` (2026-09-21T19:34:30.000Z) — firstlight: Learns Grok Bot by doing small real tasks, not by reading a manual.; personal/learning/productivity/meta-bot — **library bounce** (learning-adjacent template, not a use-case)
12. `dag-helper` (2026-09-21T19:59:34.000Z) — dag-helper: Keeps several coding agents honest about one repo's conventions.; developer/engineering/data/automation — **library bounce**
13. `hackbot9000` (2026-09-21T20:10:56.000Z) — HackBot9000: A pre-ship review gate: stale deps, fake packages, toy login.; developer/engineering/automation/decision-support — **library bounce**
14. `contest-winner` (2026-09-21T21:05:48.000Z) — Contest Winner: Finds free-to-enter contests and keeps a daily entry routine going.; personal/saving-money/productivity/automation/scheduled — **library bounce**
15. `visibility-marketer` (2026-09-21T21:35:28.000Z) — Visibility Marketer: Writes and posts organic promo for your own bot templates.; marketer/social-media/growth/content/automation — **gate-only** (off-lane GTM/social; not roster)
16. `phare` (2026-09-21T21:52:29.000Z) — phare: Teaches generative-AI basics, then quietly keeps your priorities straight.; student/learning/productivity/personal — **library bounce** (learning-adjacent template, not a use-case)
17. `grok-build-2` (2026-09-21T23:39:53.000Z) — Grok Build: Runs the Grok Build CLI at full effort on an agent computer.; developer/engineering/automation/meta-bot — **library bounce**
18. `penny` (2026-09-21T23:49:27.000Z) — Penny: Handles your Amazon reorders, and asks first before anything new.; personal/shopping/saving-money/automation — **library bounce**
19. `chief-of-staff-2` (2026-09-21T23:49:30.000Z) — Chief of Staff: One intake desk for a construction office's mail, calendar and asks.; business/ops/productivity/email/calendar — **library bounce**
20. `invention-engineer` (2026-09-22T00:34:30.000Z) — Invention Engineer: Turns the gear you own into a workable hardware build plan; developer/engineering/research/productivity — **library bounce**
21. `data-broker-opt-out-bot` (2026-09-22T05:51:48.000Z) — Data Broker Opt-Out Bot: Chases down the deletion requests that pull you off contact-data broker lists; personal/support/productivity — **library bounce**
22. `lead-vetting` (2026-09-22T07:30:42.000Z) — Lead Vetting: Reads your inbound enquiries and sends a short verdict to Slack; business/sales/email/monitoring/productivity/automation/scheduled — **gate-only** (off-lane sales; not roster)
23. `longhand` (2026-09-22T10:14:34.564Z) — Longhand: A governance layer that keeps an agent honest with plain-file memory; business/ops/automation/productivity/monitoring/knowledge-base/scheduled/developer — **library bounce**
24. `atelier-building-taste` (2026-09-22T10:16:57.000Z) — Atelier: building taste: One artwork a day: study it closely, remake it, then read why it works; creator/personal/design/learning/content — **library bounce** (learning-adjacent template, not a use-case)
25. `kickbox-hubspot-importer` (2026-09-22T10:31:04.000Z) — Kickbox → HubSpot Importer: Screens a mailing list for dead addresses before it touches your CRM; business/sales/marketer/email/data/automation — **gate-only** (off-lane sales/GTM; not roster)
26. `loaf` (2026-09-22T11:03:40.000Z) — Loaf: A tiny creature that grows happier as your daily step count grows; personal/health/wellbeing/life-hacks — **library bounce**

## Plugin delta — bounce as library
- **+0 plugins**. Plugin tables unchanged (still 50). No plugin delta to roster.

## Education / language gate
- Strict filter (edu categories or Anki/SRS/tutor/language-learning keywords on **new use-case**): **0 new**; use-case slug delta is 0.
- **Explicit: no NEW use-case with awesome_score ≥80 in education/language/tutor/Anki/learning lane.** There are no new use-cases of any score.
- Education-adjacent additions (templates only, not KEEP): `maxq-a-bot` (student/learning grade-banded rocket lesson kit), `firstlight` (learn Grok Bot by doing), `phare` (generative-AI basics for students), `atelier-building-taste` (daily art study/remake — learning-adjacent like prior `scientific-realism`).
- Off-lane GTM gate-only (not roster): `reimagination`, `newsletterbot-by-contentdrips`, `longform-editor`, `visibility-marketer`, `lead-vetting`, `kickbox-hubspot-importer`.

## News / tool announcements
- **0 new news** items (catalog still news=2). No Brief bounce one-liners.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, feed fetched to `scratch-2026-09-23-feed.json` and copied to `feed.json`.
- Research-bank: feed URL already banked prior days — skip duplicate deposit. No Firecrawl.
- RSS / browser fallback not needed.
- Removed slugs vs prior: 0.
- Slug-diff: 26 additions (26 templates); no new use-case, plugin, collection, or news.
- Thirtieth sweep (yesterday twenty-ninth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 26 new slugs → **bounce as library** / gate-only.
- Library bounce count: **20**. Off-lane gate-only subset (not roster): `reimagination` · `newsletterbot-by-contentdrips` · `longform-editor` · `visibility-marketer` · `lead-vetting` · `kickbox-hubspot-importer`.
- Alert: **no**.

## PACKET LINE
grokbot.dev (thirtieth): feed 1064→1090 (+26 templates; use-cases/plugins/collections/news unchanged); no new ≥80 education use-case; KEEP none; library bounce 20; gate-only `reimagination` · `newsletterbot-by-contentdrips` · `longform-editor` · `visibility-marketer` · `lead-vetting` · `kickbox-hubspot-importer`; alert=no.
