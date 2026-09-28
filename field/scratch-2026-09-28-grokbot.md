# grokbot.dev — 2026-09-28 education sweep (thirty-fifth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-28-feed.json` + convenience copy `feed.json` (HTTP 200)
- **generated_at**: `2026-09-27T17:05:45.696Z`
- **count**: **1254 → 1318** (+64 vs prior feed `scratch-2026-09-27-feed.json` generated_at `2026-09-26T12:39:28.772Z` count 1254)
- newest_added_at: `2026-09-27T13:26:28.576Z`
- types overall: template 1111 · use-case 138 · plugin 51 · collection 16 · news 2
- **delta vs Sep-27 feed**: **+63 templates · +1 plugin** (use-cases 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; no new use-case of any score. All 64 adds are templates (63) + plugin (1) → library bounce / gate-only / learning-adjacent note. KEEP none.
- Skip list: append new marketplace/plugin URLs to scratch-seen-urls on compile.

## New slugs since prior feed — bounce as library / gate-only
(TRUE slug-diff = +64: 63 templates · 1 plugin)

1. `smallbiz-chief-of-staff` (2026-09-18T08:58:51.000Z) — Chief of Staff: A coordinating desk that routes work to your specialist bots, lane by lane; business,ops,productivity,automation,agent-team,meta-bot,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
2. `japan-form-first-outreach` (2026-09-26T04:13:05.000Z) — フォーム優先アウトバウンド: Form-first B2B outreach for Japan: prep daily, send only on your GO; business,sales,automation,scheduled — **gate-only** (off-lane GTM/sales/legal; not roster)
3. `apply-bot` (2026-09-26T08:36:53.000Z) — Apply Bot: Applies to live job listings at scale, tuned to each posting's rubric; personal,productivity,recruiting,automation,on-demand — **library bounce**
4. `x-weekly-ops-advisor` (2026-09-26T14:47:15.000Z) — X運用アドバイザー: Weekly consultant-style reports on your X account, every action human-approved; social-media,marketer,analytics,business,scheduled — **gate-only** (off-lane GTM/sales/legal; not roster)
5. `journal-self-review` (2026-09-26T14:48:02.000Z) — 精神メンタル・アドバイザー: Sorts old journal notes into fact, impression and unverified, then proposes next steps; wellbeing,personal,learning,on-demand — **library bounce** (learning-adjacent journal/wellbeing sorter; template not named language/tutor practice ≥80 use-case)
6. `ssh-to-grok-bot-via-tailscale` (2026-09-26T16:36:46.000Z) — SSH to Grok Bot via Tailscale: Puts the bot's own computer on your tailnet so you can shell straight in; developer,engineering,automation,on-demand — **library bounce**
7. `kids-daily-spark` (2026-09-26T18:47:50.000Z) — Kids Daily Spark: A one-page STEM hook for each kid, every day, with a 30-second try-it; family,learning,student,scheduled — **library bounce** (learning-adjacent STEM kids daily hook; template not named language/tutor practice ≥80 use-case)
8. `first-week-coach` (2026-09-26T19:20:55.000Z) — First-Week Coach: Seven days of ten-minute lessons that turn a new user into a confident one; learning,productivity,meta-bot,scheduled — **library bounce** (learning-adjacent teach-once Grok Bot onboarding lessons; template not ≥80 use-case)
9. `master-chief` (2026-09-26T19:26:58.000Z) — Master Chief: Inbox triage, voice-matched replies and a weekday brief for your morning; email,calendar,business,productivity,scheduled — **library bounce**
10. `github-pr-desk` (2026-09-26T19:29:20.000Z) — GitHub PR Desk: One weekday digest of every PR, issue and comment across your repos; developer,engineering,monitoring,scheduled — **library bounce**
11. `grok-workhorse` (2026-09-26T19:37:12.000Z) — Grok Workhorse: A coding foreman that delegates to sandboxed agents and reviews their work; developer,engineering,agent-team,automation,on-demand — **library bounce**
12. `video-editor` (2026-09-26T20:16:58.000Z) — Video Editor: Turns a talking-head recording into a clean, branded YouTube cut; video,youtube,creator,content,on-demand — **library bounce**
13. `connection-mapper` (2026-09-26T20:29:17.000Z) — Connection Mapper: Charts every direct and one-hop path between any two people or companies; research,data,personal,business,on-demand — **library bounce**
14. `market-sentiment-bot` (2026-09-26T22:27:12.000Z) — Market Sentiment Bot: Grades US risk assets one to ten, with a card for the market and each ticker; finance,investor,analytics,news,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
15. `cosmo` (2026-09-26T22:35:12.000Z) — Cosmo: A phone-first daily desk and scorecard with a firewall on everything outbound; personal,productivity,business,on-demand — **library bounce**
16. `bookmark-miner` (2026-09-26T22:51:08.000Z) — Bookmark Miner: Turns the X posts you saved into a ranked list of things actually worth doing; personal,productivity,research,social-media,on-demand — **library bounce**
17. `tee-timey` (2026-09-26T22:56:19.000Z) — Tee Timey: Your own tee-time sniper: supply the courses, pick the windows, it fires; automation,life-hacks,personal,on-demand — **library bounce**
18. `elon-ecosystem-desk` (2026-09-26T22:59:09.000Z) — Elon Ecosystem Desk: A weekday news desk for Tesla, SpaceX, xAI, Neuralink, Boring and X; news,investor,business,scheduled — **library bounce**
19. `webb-knox` (2026-09-26T23:03:22.000Z) — Webb Knox: Finds scored leads with evidence they need you now, then drafts the opener; sales,growth,business,marketer,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
20. `team-builder` (2026-09-26T23:05:56.000Z) — Team Builder: Interviews you, then hires a whole company of bots to run the floor; business,agent-team,meta-bot,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
21. `ai-security-advisor` (2026-09-26T23:06:27.000Z) — AI Security Advisor: Defensive hardening advice for AI apps: injection, tool abuse, leakage; developer,engineering,business,on-demand — **library bounce**
22. `superfan` (2026-09-26T23:16:10.000Z) — Superfan: A daily check-in for your teams: next fixture, last result, season ledger; personal,news,scheduled — **library bounce**
23. `x-growth-assistant` (2026-09-26T23:17:47.000Z) — X Growth Assistant: Prunes dead follows, clears spam accounts and suggests niche-relevant adds; social-media,growth,marketer,automation,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
24. `the-box-of-names` (2026-09-26T23:19:08.000Z) — The Box of Names: Traces any name across civilizations and eras, marking each link real or legendary; learning,research,knowledge-base,on-demand — **library bounce** (learning-adjacent name/history knowledge walk; template not language/tutor practice)
25. `opus-motion` (2026-09-26T23:19:26.000Z) — Opus Motion: Short motion-graphics drafts for products and brands, delivered as MP4s; creator,video,content,on-demand — **library bounce**
26. `phone-use-bot` (2026-09-26T23:19:34.000Z) — Phone Use Bot: Drives your Android remotely: mirrored screen, taps on your behalf; automation,personal,developer,on-demand — **library bounce**
27. `brew-what-you-got` (2026-09-26T23:21:19.000Z) — Brew What You Got: Cafe-quality drink recipes built from the gear and beans you already own; food,life-hacks,personal,on-demand — **library bounce**
28. `pal` (2026-09-26T23:21:40.000Z) — Pal: Reads today's MLB slate and surfaces the prop spots that stand out; analytics,decision-support,data,on-demand — **library bounce**
29. `handyman` (2026-09-26T23:23:22.000Z) — Handyman: Remembers your filter sizes and chore dates, then books the next round; home,calendar,family,scheduled — **library bounce**
30. `shawn` (2026-09-26T23:26:20.000Z) — Shawn: Paper-first sports wager research: closing-line moves and post-juice value; analytics,decision-support,data,on-demand — **library bounce**
31. `mamboitalianobot` (2026-09-26T23:29:21.000Z) — MamboItalianoBot: End-to-end travel plans with trade-offs, checklists and a plan B; travel,personal,decision-support,on-demand — **library bounce**
32. `subscription-manager` (2026-09-26T23:30:17.000Z) — Subscription Manager: A running ledger of every renewal, with a nudge two days before each; finance,saving-money,personal,monitoring,scheduled — **library bounce**
33. `scriptsprint` (2026-09-26T23:34:35.000Z) — ScriptSprint: Turns meeting and voice transcripts into summary, speakers and action items; meetings,productivity,knowledge-base,automation,on-demand — **library bounce**
34. `quill` (2026-09-26T23:36:07.000Z) — Quill: A revision pass for your notes: voice punch-up, continuity check or depth read; content,knowledge-base,productivity,on-demand — **library bounce**
35. `calendar-liftoff` (2026-09-26T23:43:54.000Z) — Calendar Liftoff: A print-ready 12-by-12 photo wall calendar PDF on any theme you name; design,content,family,on-demand — **library bounce**
36. `seo-content-desk-seodraft` (2026-09-26T23:45:34.586Z) — SEO Content Desk (seodraft): An editorial desk that plans, drafts and audits SEO content for your own blog.; seo,content,marketer,business,growth — **gate-only** (off-lane GTM/sales/legal; not roster)
37. `it-department-lead` (2026-09-26T23:46:45.000Z) — IT Department Lead: Staffs a bench of IT sub-bots across helpdesk, systems, network and security; business,ops,support,agent-team,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
38. `3-day-notice-validator` (2026-09-26T23:56:52.000Z) — 3-Day Notice Validator: Checks California pay-or-quit notices field by field before you serve them; real-estate,business,ops,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
39. `upload-post` (2026-09-27T00:00:00Z) — Upload-Post: Let your agent publish, schedule and analyze posts on 11 social networks.; marketing — **library bounce** (plugin table = library)
40. `the-morning-paper` (2026-09-27T03:58:27.000Z) — The Morning Paper: Your ZIP code's own daily paper: hometown headlines, local weather and jobs nearby; personal,news,scheduled,on-demand — **library bounce**
41. `find-good-stocks` (2026-09-27T04:28:27.000Z) — Find Good Stocks: Puts your stock thesis through the wringer on public reporting, then says what holds up; investor,finance,research,analytics,scheduled,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
42. `media-ledger` (2026-09-27T04:32:27.000Z) — Media Ledger: A running ledger of the books, games, films and albums you own, straight from receipts; personal,shopping,data,back-office,automation,productivity — **library bounce**
43. `vern` (2026-09-27T04:46:39.000Z) — Vern: A small private address book that nudges you before a birthday or when a friendship cools; personal,family,productivity,monitoring,scheduled — **library bounce**
44. `quartermaster` (2026-09-27T04:55:07.000Z) — Quartermaster: A zero-sum household budget kept in Google Sheets, with a daily money report to read; personal,finance,productivity,analytics,scheduled,data — **library bounce**
45. `launch-sky-watch` (2026-09-27T04:56:31.000Z) — Launch & Sky Watch: Rocket schedules, station flyovers and eclipses, timed to your clock and your own sky; personal,news,events,scheduled,monitoring — **library bounce**
46. `chop-bot` (2026-09-27T05:10:18.000Z) — Chop Bot: One morning brief for email, calendar and X replies, with every draft approved by you; personal,business,productivity,email,automation,scheduled,on-demand — **library bounce**
47. `inbox-scout` (2026-09-27T05:49:10.000Z) — Inbox Scout: Each morning your unread mail comes back sorted: needs-you, can-wait and noise; personal,business,email,productivity,automation,scheduled — **library bounce**
48. `coverage-desk` (2026-09-27T05:49:32.000Z) — Coverage Desk: Turns your insurance declarations page into everyday wording, so you know what you carry; personal,business,finance,decision-support,learning,on-demand — **library bounce** (learning-tagged insurance plain-language explainer; off language-tutor lane)
49. `lineage-desk` (2026-09-27T05:53:33.000Z) — Lineage Desk: Family history with analyst's discipline: free sources first, each one graded for trust; personal,research,family,knowledge-base,learning,on-demand — **library bounce** (learning-adjacent family-history research desk; template not language/tutor practice ≥80 use-case)
50. `improve-my-odds` (2026-09-27T06:22:12.000Z) — Improve My Odds: Pick a goal and an everyday choice; get a straight helps, hurts or neutral read on it; personal,decision-support,life-hacks,wellbeing,on-demand — **library bounce**
51. `rugradar-ai` (2026-09-27T06:22:42.000Z) — RugRadar AI: Scans a fresh Solana token's public chain record and lays out the rug-pull warning signs; crypto,research,finance,data,monitoring,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster)
52. `sports-bet-prophet` (2026-09-27T06:23:53.000Z) — Sports bet prophet: A research desk for bettors: two-leg doubles in a set price band, wager left to you; personal,analytics,decision-support,on-demand — **library bounce**
53. `markets-digest` (2026-09-27T06:41:30.000Z) — Markets Digest: Plain-language markets news twice each weekday, with no repeats in the evening edition; investor,personal,news,finance,research,scheduled — **gate-only** (off-lane GTM/sales/legal; not roster)
54. `epigenetics-scout` (2026-09-27T06:42:46.000Z) — Epigenetics Scout: A weekly readable digest of new partial-reprogramming research, findings split from hype; personal,research,health,learning,news,scheduled — **library bounce** (learning-adjacent science digest; off language-tutor lane)
55. `weather-scout` (2026-09-27T06:53:06.000Z) — Weather Scout: A three-day go / marginal / no-go weather outlook for launches at the big US spaceports; personal,research,monitoring,engineering,on-demand — **library bounce**
56. `bot-foundry` (2026-09-27T07:44:02.000Z) — Bot Foundry: Describe an idea or a daily chore and get a full draft bot package, ready to publish; developer,creator,automation,productivity,meta-bot,on-demand — **library bounce**
57. `pounce` (2026-09-27T07:47:00.000Z) — POUNCE: A daily hunt for AI-company contests, grants, credits and hackathons, deadlines verified; personal,developer,saving-money,monitoring,scheduled,on-demand — **library bounce**
58. `mystery-eshopper` (2026-09-27T08:23:34.000Z) — Mystery eShopper: Shops your online store like a customer and hands back a scored journey with bug reports; business,developer,support,design,data,on-demand — **library bounce**
59. `fitboard` (2026-09-27T08:30:40.000Z) — Fitboard: Answer five quick questions and get a furnishing plan with real prices, inside budget; personal,shopping,home,design,saving-money,on-demand — **library bounce**
60. `math-researcher` (2026-09-27T09:25:31.000Z) — Math Researcher: A proof-first math partner that grades every claim by how hard it was actually checked; student,research,learning,decision-support,on-demand — **library bounce** (learning-adjacent student math proof partner; template not named language/tutor practice ≥80 use-case)
61. `claimed` (2026-09-27T09:54:05.000Z) — Claimed: One deep pass over the refunds, settlements and compensation programs you may be owed; personal,saving-money,finance,research,on-demand — **library bounce**
62. `delta-x` (2026-09-27T10:07:21.000Z) — Delta-X: A Friday planner that audits your subscriptions and commits to just three changes; personal,saving-money,email,productivity,wellbeing,scheduled — **library bounce**
63. `chinese-earnings-digest` (2026-09-27T12:00:02.000Z) — 财报锦囊: One US ticker in, a seven-point Chinese skim of the newest earnings out; investor,finance,research,analytics,learning,on-demand — **gate-only** (off-lane GTM/sales/legal; not roster) — also language-adjacent Chinese earnings skim for investors; template not tutor practice ≥80 use-case
64. `bill-watch` (2026-09-27T13:26:28.576Z) — Bill Watch: Surface the subscriptions and charges your inbox quietly forgot about; personal,saving-money,finance,productivity — **library bounce**

## KEEP
- none (no education/language use-case ≥80 with practice)

alert=no
