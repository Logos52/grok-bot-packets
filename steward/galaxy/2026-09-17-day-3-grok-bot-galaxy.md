# Day 3 — Grok Bot Galaxy Livestream (EOD)

## Context
- **Day / title:** Day 3 · Building a company in 3 days - launching today! (2026-09-17)
- **URL:** https://x.com/i/broadcasts/1YGNrbXEeazGw
- **Host:** Grok Bot (@bot)
- **Hub / Luma:** https://x.ai/galaxy · https://luma.com/3ifrgttw
- **Access:** X DVR/replay from box browser. Stream **ENDED** (UI “Ended 2 hours ago” at EOD scrub ~18:03 PDT). Player duration **7:58:23**; end scrub **7:58:22/7:58:23**. Views **~183.5K** (landing ~182.7K → end). End card: **“Grok Bot Galaxy — Thanks for joining!”**
- **Coverage:** OPEN pass ~0:00→~61m (MarOps) + EOD scrub ~61m→7:58 (midday build, Post-Sales / Customer Success, Thursday Arena, Marketing, wrap/showcase, credits). Spoken dialogue **not** transcribed; UI/slide text quoted when readable.
- **Method:** Chronological seek on `<video>.currentTime` + screenshots. Replay-seek chat sidebar is **not** time-synced — prefer end-state chat only; mark uncertainty.
- **Schedule (hub + on-stream overlays; times drifted across overlays):** 8:30 livestream start · 9:00–10:30 Marketing Operations (Matthew Silberman, Teresa Hsu) · midday Build A Game Studio · ~12:30–1:30 Post-Sales / Customer Success (Blake Schuller per hub; identity not plated on camera) · more Build · 2:30–3:30/4:00 Marketing (Josh Kim per hub; **Dan Hill** “X engineering” tagged on-stream at ~6:00 player) · 4:30–5:30 wrap/final showcase.
- **EOD complete:** This file is the full Day 3 brief. Finite routine `galaxy-day-3-open-eod` to be deleted after delivery.

## Field notes

### Opening / Build A Game Studio (~0:00 → ~30:00) — from OPEN
- **~0:00** — Seek may land on non-start “Questions?” frame (uncertain). Better cold-open evidence at **~1:00**.
- **~1:00** — Title card **“Grok Bot Galaxy”**; Live agenda; inset Cupcake Eng (**tater**, **bento**, “+ 40 more”). Shot: `assets/day3-open-01m00-agenda.png`.
- **~10:00** — Couch trio; promo **“New users: one month of free Grok Bot.”** Shot: `assets/day3-open-10m00-couch.png`.
- **~15:00** — **Bake** workspace (Founding eng); PRs / Vercel; threads **Play** / **Ping**. Shot: `assets/day3-open-15m00-bake.png`.
- **~20:00** — CUPCAKE leaderboard: **@roshan_s** / **@poteto** both **1831 GOLD**. Shot: `assets/day3-open-20m00-cupcake-leaderboard.png`.
- **~25:00** — Fleet overlay sample **43** Bots · **120** Messages · **2** Working · **9** Active.
- **~30:00–32:00** — **Be right back** card.

### Marketing Operations (~33:00 → ~61:00) — Matthew Silberman, Teresa Hsu (schedule)
- Speakers **not** name-captioned on camera; solo male stage presenter for most demos.
- **~35:00** — **“Why Grok Bot”** tiles: Easy as iMessage · Always-on 24/7 · Uses your tools like you · Finishes the work · Shareable Templates (“Peng shared Kenny with you”). Shot: `assets/day3-open-35m00-why-grok-bot.png`.
- **~38:00** — **Meet the team:** **OP-1** Chief of Staff · **Fisher** EA · **Juno** PM · **Ondes** Engineer. Shot: `assets/day3-open-38m00-meet-the-team.png`.
- **~40:00–42:00** — **Territory Planner** digest: Approve (relay) vs **Hold** (digest only); Acme Logistics conflict. Governed-approval pattern. Shot: `assets/day3-open-42m00-territory-planner.png`.
- **~45:00–50:00** — **Juno** → locked **Lead Deck v1** markdown → **Ondes** / cloud agent; Accept/Skip/Reject(+reason); no CRM status write on Accept. Spec path `/home/box/shared/lead-deck/lead-deck-product-spec.md`. Shots: `assets/day3-open-45m00-juno.png`, `day3-open-50m00-lead-deck-spec.png`.
- **~53:00** — **First Contact** preview; lead card **Sofia Reyes**. Shot: `assets/day3-open-53m00-first-contact.png`.
- **~55:00** — MarOps **“What we learned”**: Staff dream team · Give bots agency + guardrails (“Governed agency beats ask-each-time or YOLO”) · You are a PM; product is revenue. Shot: `assets/day3-open-55m00-what-we-learned.png`.
- **~61:00 OPEN edge / EOD resume** — Stage **Questions?**; MarOps Q&A. Shot: `assets/day3-open-live-edge.png` / EOD `t-61m.png`.

### Midday build / Cupcake (~1:01 → ~3:45 player)
- **~1:01** — Stage Q&A still on **Questions?** (~9:31 PT wall-clock estimate from scrub report).
- **~1:15** — **Be right back.**
- **~1:45–2:15** — Cupcake **card-game UI**: cards **COMPETITOR WATCH** (PIN; by Shimazaki), **CUSTOMER PROOF DESK** (DUMP; by Anoop Baliga), **EXECUTIVE ASS…** (HYPE). Later tip noted “You took round 1.” Chat at seek (not trusted for time) argued “where’s the business / revenue?” Shot: `assets/day3-eod-105m-card-game.png`.
- **~2:30** — Cupcake fleet workspace: **steve** (chief of staff), **bento** (pm), **ping** (slack mentions; DM listen limited), **crumb** (playtester; **P2-1 BLOCKED—403**), **tater** (engineer). Steve proposes pause DDoS mitigations / bypass agent IPs; HITL choice **“hold - leave WAF”** selected; NEW: “holding firewall — no changes.” On-screen mention of **@ Poteto Mode** full autopilot + **/verify-cupcake skill** + **@ swarm_s** — “critical that we do not break the game for everyone.” Shot: `assets/day3-eod-150m-poteto-waf.png`.
- **~3:00** — Funnel snapshot (practice → convert → play): practice started 2,235 · completed 762 · converted to X 206 · SAP from practice 191 · public matches 2,083. Agenda overlay drifted (Customer Success / Marketing / Build blocks). Speaker chip **Vincent (@vincenthu)** visible.
- **~3:45** — Caption **“Standing up marketing operations.”** **Cerebro** doc: Distribution Today · Signal Recipes · Outbound Story (stadium sponsorship / short auto-battles). Fleet strip: steve / bento / tater + “11 more.” Chat asked for Cerebro Bot marketplace link (@matt_silberman). Shot: `assets/day3-eod-225m-cerebro.png`.

### Post-Sales / Customer Success (~4:00 → ~4:45) — Blake Schuller (hub; not plated)
- On-stream agenda sometimes labeled **“Grok Bot for Customer Success”** in this window (hub: Post-Sales).
- **~4:00** — Female stage presenter; same **“Why Grok Bot”** five-tile slide as MarOps. Shot: `assets/day3-eod-240m-why-grok-bot.png`.
- **~4:15** — **Dream Team** sidebar: **Franny Form** (active), **Wally Writer**, **Trudy Truth**, **Frankie Follow Up**, **Scout**. Prompt: “Make me an roi form for northwind.” Franny: **“Building a Northwind Logistics FlyLO ROI form (default SQ). Draft only — I won't send it. Creating it in Google Forms now — I'll send the share link when it's live.”** Computer/screen share of form build. Shot: `assets/day3-eod-255m-franny-form.png`.
- **~4:30** — Stage **Questions?**; chat praise (“One of the best sessions!”). Shot: `assets/day3-eod-270m-questions.png`.

### Thursday Arena / Build (~5:00 → ~5:45)
- **~5:00** — Split: **THURSDAY ARENA** (PLAY / Practice + bot cards) | **Data** dashboard. Public WR ~42% → ~47%; “ghosts were eating new players”; Season 1 sample metrics (1:25pm PT): 3,666 practice · 1,248 X · 8.4% practice→X · WR 46.8% · feedback 253 · queue 0. One-liner for chat quoted on doc. Shot: `assets/day3-eod-300m-thursday-arena.png`.
- Build A Game Studio panels continue between guest blocks (card UI / studio couch).

### Marketing (~6:00 → ~6:30+) — Josh Kim (hub); Dan Hill tagged on-stream
- **~6:00** — Couch trio + Live agenda (Marketing → Build → Wrap 4:30–5:30). Speaker tag **Dan Hill** / “X engineering.” Shot: `assets/day3-eod-360m-marketing-couch.png`.
- **~6:30** — Marketing **“What we learned”** (three blocks, readable):
  1. **Scope Bots properly** — “Grok Bot is extremely powerful but bloated context and responsibilities can slow you down. Scope like a job description!”
  2. **Then, trust your Bots!** — “Treat Grok Bot as your proactive, ambitious teammate. Hand it tools, access, and context and let it run free to do your work.”
  3. **Invest in your Bots and copy others'** — feedback like a teammate; leverage marketplace; **QR** on slide.
  - Male presenter PiP. Shot: `assets/day3-eod-390m-what-we-learned.png`.

### Wrap / final showcase (~6:45 → 7:58)
- **~6:45–7:00** — Four-person panel; account-loading UI (“Loading your account.”).
- **~7:15** — Showcase of X post by **matt palmer (@mattyp)**: daily Grok Bot reads X Bookmarks → spins up a **Cursor Agent** demo → validates with screenshots/video → branch on repo with **@Cloudflare** preview deploys → **@Bot** sends morning link. Today picked **cobe** from @shuding. Closing line: “If you can do it, it can be automated.” Shot: `assets/day3-eod-435m-showcase-bookmarks.png`.
- **~7:30** — **“Grok Bot Credits”** slide: Within next 5 minutes (1) Post in chat **“credits”** (2) Receive Grok Bot credits by end of day **($200 in value)**; **“Valid for livestream viewers only.”** Chat flooded with Credits. Shot: `assets/day3-eod-450m-credits.png`.
- **~7:40–7:55** — Card-game UI / panel close-ups / business-planning board (“WHAT THE BUSINESS” per scrub report — not re-OCR’d here).
- **7:58:23** — End card: black field, bot icons, **“Grok Bot Galaxy”** + **“Thanks for joining!”** · **183.5K** views. End-state chat still dominated by credits thank-yous. Shot: `assets/day3-eod-endcard.png`.

### Speakers / roles (observed + schedule)
- **MarOps:** Matthew Silberman, Teresa Hsu (hub); male stage presenter uncaptioned.
- **Post-Sales / CS:** Blake Schuller (hub); female stage presenter for Franny Form demo; **not** name-plated.
- **Marketing:** Josh Kim (hub); on-stream tag **Dan Hill** (X engineering) at ~6:00; male presenter for “What we learned.”
- **Cupcake / build spine:** steve, bento, ping, crumb, tater (+ Bake/Play/Ping/Crit from morning); Vincent (@vincenthu) chip; poteto / Poteto Mode / swarm_s / verify-cupcake.
- **MarOps demo fleet:** OP-1, Fisher, Juno, Ondes (+ Territory Planner, First Contact).
- **CS Dream Team:** Franny Form, Wally Writer, Trudy Truth, Frankie Follow Up, Scout.
- **Showcase author:** matt palmer (@mattyp) bookmark→agent workflow.

### Product claims / demos (observed)
- Governed agency: Territory Planner Approve/Hold; WAF **hold - leave WAF** (no auto-pause of edge mitigations).
- Spec-as-handoff: Juno locks Lead Deck markdown before Ondes/cloud agent.
- Swipe HITL: First Contact Accept/Skip/Reject(+reason).
- Draft-only external write: Franny Form Google Forms “won't send” until share link ready.
- Named single-duty fleets across GTM / CS / Cupcake.
- Marketing lessons: scope like a JD · then trust · invest + copy marketplace.
- Morning bookmark feeder → Cursor Agent → screenshot/video validate → Cloudflare preview → daily link.
- Credits giveaway ($200 value) via chat keyword for livestream viewers.
- Free month promo for new users (morning overlay).
- Thursday Arena live metrics / practice→X funnel as game-studio product proof.

### Chat (end-state / live-tip only; seek chat discarded)
- Credits rush at close; thank-yous.
- Morning OPEN: Juno template asks; token burn / Dr Eggbot; cloud-agent downtime.
- Midday seek chat (untrusted for clock): revenue-vs-game skepticism; Cerebro marketplace ask; poteto/dark-mode jokes.

## Themes
1. **Governed agency** — Approve/Hold and “hold - leave WAF” over YOLO edge changes.
2. **Scope then trust** — Marketing close: job-description scoping before “run free.”
3. **Named single-duty fleets** — OP-1/Fisher/Juno/Ondes; Franny/Wally/Trudy/Frankie/Scout; steve/bento/ping/crumb/tater.
4. **Spec / draft artifacts before side effects** — Lead Deck locked md; Franny “draft only — won't send.”
5. **Swipe / keyword HITL surfaces** — First Contact cards; chat “credits” giveaway; Territory Planner Approve vs Hold.
6. **Feeder → agent → validate → ship link** — Bookmarks → Cursor Agent → screenshots/video → Cloudflare preview.
7. **Game studio as company proof** — Thursday Arena metrics + Cupcake card economy alongside GTM demos.
8. **Templates / marketplace as distribution** — Juno template demand; Marketing “copy others” + QR; Cerebro ask.

## Improvements for Wedge
Ranked; existing fleet only. Recommendations — do **not** create/edit bots/routines/skills unless Wedge asks in chat.

1. **Governed agency pin (Steward)** — Day 3 showed both CRM-ish Approve/Hold **and** infra Hold (leave WAF). Cheap next step: Steward first-session one-liner — external writes **and** destructive infra toggles default Hold; never invent a bypass.
2. **Scope-like-a-JD before agency (Intake + Galaxy duty)** — Marketing: bloated context slows bots. Cheap next step: Intake rejects multi-duty asks; Galaxy stays notes→improvements only (no new bots from this brief).
3. **Draft-only before send (Brief + Steward)** — Franny Form: build artifact, don't send until explicit. Cheap next step: Brief Accept/Skip/Reject(+reason) for any outbound draft; default Skip/Hold on send.
4. **Spec-handoff path (Intake → Brief)** — Juno locked markdown before eng. Cheap next step: multi-bot builds require a locked `*-product-spec.md` path first (Galaxy dated notes already SsOT for coverage).
5. **Bookmark/research feeder pattern (Watch)** — Showcase: daily bookmarks → agent → validated preview link. Cheap next step: Watch one weekday line when a research feeder has a new “shipped link” candidate — no auto-post.
6. **Template / marketplace demand (Watch)** — Chat asked for Juno + Cerebro templates. Cheap next step: Watch flags high-demand template names from Galaxy notes for intentional share (no auto-post).
7. **poteto-mode + verify skill for build-adjacent** — On-stream Poteto Mode + `/verify-cupcake` before autopilot. Cheap next step: point nontrivial coding helpers at poteto-mode; require a verify/healthcheck skill before swarm-like runs.
8. **Connector / path honesty (Steward + Watch)** — Spec path + OAuth validate; 403/WAF called out honestly. Cheap next step: Steward “if blocked, say blocked”; Watch Mon/Wed/Fri last-success for GitHub/X/Notion feeders.
9. **Credits/promo awareness only (Watch — optional)** — Chat keyword giveaways are event UX, not fleet. Cheap next step: no bot change; Watch may note promo patterns if Wedge tracks audience offers.

## Open questions / gaps
- Blake Schuller / Josh Kim faces **not** name-plated; IDs from hub/schedule (+ Dan Hill on-stream tag).
- Exact spoken Q&A content not captured (Questions? slides only).
- Midday Build blocks between sessions: sampled, not minute-by-minute.
- “WHAT THE BUSINESS” board at ~7:40 — scrub-reported; not re-OCR’d in EOD write-up.
- Juno / Cerebro template share URLs — not observed.
- First Contact Railway URL / Lead Deck repo ownership — glimpsed earlier; not re-verified at end.
- On-stream agenda spelling **Mark** vs hub **Matthew** Silberman — unresolved.
- Whether Spirit≡GF-1 / Grake≡Grover / Opal roles — still OCR-uncertain from OPEN.
- Audio not verified this EOD (visual scrub only).
- Seek chat never treated as timestamped evidence.

## Screenshot refs (box)
- EOD scrub set: `/tmp/.sand-browser/day3-eod-scrub/` (`landing.png`, `t-61m.png` … `t-475m.png`, `day3-eod-final.png`)
- OPEN scrub: `/tmp/.sand-browser/day3-open-scrub/`; live tips `day3-open-live-*.png`
- Notes assets: `assets/day3-open-*.png`, `assets/day3-eod-*.png`
