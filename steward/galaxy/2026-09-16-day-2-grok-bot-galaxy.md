# Day 2 — Grok Bot Galaxy Livestream (EOD)

## Context
- **Day / title:** Day 2 · Grok Bot builds a Game Studio LIVE (2026-09-16)
- **URL:** https://x.com/i/broadcasts/1PKqrNyvmYwGb
- **Host:** Grok Bot (@bot)
- **Access:** X DVR/replay from box browser. Stream **ENDED** ~16:53 PDT 2026-09-16. Player duration **8:23:19**; end scrub at **8:23:18/8:23:19**. Views **~378K** (UI). End card: **“Grok Bot Galaxy — Final day starts tomorrow at 8:30am PST.”** X MCP was unavailable earlier (`failed_to_load`); browser used throughout.
- **Coverage of this note:** Full EOD. Dense catch-up **0:00→~57:47** (Sales Engineering). Midday **~1:00→~6:00** sparsely scrubbed (schedule-aligned; Sales / SDR handoffs inferred from x.ai/galaxy + late live tips — not a minute-by-minute VOD pass). Dense live tips **~6:00→end** through Cupcake fleet, Support, sound design, end card.
- **Method:** Chronological seek + live tip appends. UI/chat quoted when readable; spoken dialogue paraphrased / marked uncertain. Replay chat sidebar not always time-synced on seek; prefer live-tip chat.
- **Schedule (x.ai/galaxy, Day 2):** SE Amrita Venkatraman 9:00–10:30 · Sales SpaceXAI Sales Team 12:30–2:00 · SDRs Simon Lackowski 2:30–3:30 · Customer Support David Gan 4:00–5:00 · Livestream ends 6:00 PM PT (actual X end ~4:53 PM PT / player 8:23).

## Field notes

### Catch-up (0:00 → ~57:47) — Sales Engineering / Templates
- **0:00–15:04** — Opening/title-card interlude. “Grok Bot Galaxy” animation with colored bot icons; no speaker or session title. No numeric bot count.
- **20:20** — “Grok Bot Templates!!” slide. Flow: Grok Bot Template → character in a game → head-to-head competition. Attribute diagram (CHA, DEX, INT, etc.). Male presenter inset, not name-captioned. Chat: Don Davis asked whether this covers real business-problem engineering vs travel-agent toys; StokPix: define the problem first; chat limits / parallel coding questions.
- **25:35** — Same templates/attributes demo. Chat: competitive bots; building in parallel.
- **31:07** — Agenda: 1 Welcome · 2 Introducing Grok Bot · 3 Why Grok Bot · 4 Sales Engineer Use Cases · 5 Demo · 6 What we learned · 7 Q&A · 8 Build. Chat: course summary/timeline; agents slow on simple tasks.
- **36:31** — Agenda still up; presenter inset. Chat: how this relates to sales engineering.
- **42:01** — “Introducing Grok Bot”: create bots for different jobs; message like teammates; retain context and improve; connect to tools; set up automations/routines for roles. Transitioned to “Connecting” app state. Chat: apply principles to customers’ businesses; future team members speculation.
- **47:32** — Support/travel workflow demo. On-screen: prevent two customers claiming same cabin/seat via Postgres row locks + 10-minute hold. Bot workspace: customer/support tickets; presenter inset. Chat: Serena as template?; merge all bots into one?
- **52:36–54:07** — Serena Williams / Sherlock support-agent workflow. Testing plan: Southwest and Spirit; search/fare/extras/checkout; AI travel-agent capabilities. Notes on customer requirements, token usage, prompt guardrails vs security boundaries, proprietary-data risk. Chat: tokens; airline booking knowledge; functional bot names; forgetfulness.
- **~57:15** — Sherlock workspace entries: Serena Williams, Sherlock, “Sherlock, Amrita Venkatraman”; presenter lower-right. Chat: Grok Bot slow; compensation for product failures; Fortnite backlog joke.

### Midday (~1:00 → ~6:00) — sparse / schedule-aligned
- **Schedule only (not densely scrubbed this EOD):** Grok Bot for Sales (SpaceXAI Sales Team, 12:30–2:00 PT) sits between SE catch-up and SDR tip. Exact Sales demos / slides not captured in a full VOD pass here — **gap**.
- **~5:59 player sample (pre-SDR tip):** On-stream graphic “You” (purple pause-like icon + word) on dark purple field + QR lower-right; player ~5:59:02; views ~377.8K at that capture. Chat at tip mixed (website / cards jokes) — treat as possibly not time-synced on seek.
- **~14:40 PDT (~6h tip)** — LIVE title “Grok Bot builds a Game Studio LIVE”. Stage on **“SDR use cases”** (four blocks): Prospecting (ICP → titles via web search + enrichment); Sequencing (CSV/XLSX lists through custom sequences); Account Research (fundraising/job postings → messaging); Drafting Copy (sync email → style → personalized drafts). Chat ID’d presenter as **Simon Lackowski** (matches schedule; not name-captioned on-frame). Chat: “Joining from Nigeria”; usage % questions.
- **~15:02 PDT (~6:33 tip)** — Concluding slide **“What we learned”**: Go End to End · Be Intentional · Think Systematically. Chat: “Bot calls the app, retrieves output, adds to dB, reports”; “Great demo!”; “This is my favorite demo so far.”

### Afternoon build / demos (~7:00 → ~8:00 player)
- **~15:32 PDT (~7:01 tip)** — Product demo **Ping**: left messaging/inbox (Glow, Bake, Ping, Shardul, Data, Paul); mention listener (“Mention listener is saved — I'll wake me anywhere Cursor is invited”); right “View of Tasks” kanban (e.g. Release #21 Clerk JWT; Land #19 Clerk auth). Two presenters inset. Chat: house-cat bot / kitty-treats; “we love @poteto”; Remotion Cupcake ads; blender bot; SPROCKETSAI.
- **~15:45 PDT** — Multi-bot **Cupcake / game-studio fleet** workspace. Sidebar: **Chief** (CoS), **dr eggbot**, **Bake**/Bako (Founding Eng), **Crit** (Game Designer), **Ping**, **Glow** (3D prototyping), **Shardul** (Intern), **Data**. Claims (on-screen; long lines approximate): Glow prototyping 3D on `shipbythursday/cupcake` via potato cloud-agent swarms (draft PRs; Bake graduates winners); Crit grounded in Lauren’s critique cards — **Notion page 404** for connector; host: “tell the team that notion is source of truth and every bot should keep it updated”; **PR #30** `feat(web): play back the replay tape (potato)` on `shipbythursday/cupcake`. Chat: “cupcake is just the bot they using”; “SSoT !!!”; “Oh nooo”.
- **~15:58 PDT (~7:30 tip)** — Fleet updates: **Pixel** (Designer) new; Bake “#38 pushed…”; Glow stills round-2; **arena** named in fleet-tell. **dr eggbot** confirms fleet message + shared memory; reports telling 8 bots (pixel, arena, chief, bake, ping, glow, crit, shardul). Host spinning **audio engineer** bot for sound-design (Notion tasks; 8-bit styles). Promo overlay **“Want free Grok Bot?”** — free month ($200 value); duplicate bot with **dr eggbot**; first 1,000; QR. Chat: “qr code blocked”; “I made the bot”; Notion whiteboarding wish; voice/audio asks.
- **~16:13 PDT (~7:45 tip)** — **Support Agent** demo. Doc **“Grokbot Support Agent Rules”**: (1) Read Plain thread; (2) Knowledge — Public Docs for answers; Internal Policies to decide only (never paste); (3) Reply vs Handoff (high/medium/low; low/missing/ambiguous → Handoff); (4) Act if needed (e.g. Stripe refund/cancel per Internal Policies); (5) Write customer reply + note. Inbox UI: Reply/Done; Ticket Generator / Tune / Alert / Build; Auto-review blocked Slack update pending approve; “Replied from Public:Auto:Forgot password (high confidence)”. Chat: QR follow-ups; 720P stall; “what kind of company building”.
- **~16:30 PDT (~8:01 tip)** — On-stage talking-head; capture ID’d **David Gan** (matches Customer Support schedule; no on-frame caption). Partial **SXSW** branding visible. Chat: Plain↔Grok support praise; hands-on thanks; enterprise/Cursor utility; usage jokes; short thank-yous.

### Close — sound design → end card (~8:00 → 8:23)
- **~16:42 PDT** — **Cupcake sound-design**: Notion **“Sound design for the game”** / Cupcake RPG — owner **Tone**; status Foley v0 + Suno refs; Updated 2026-09-16 PT. Foley stubs: `01 draft pick`, `02 lineup lock`, `03 reveal`, `04 slot win`, `05 slot loss`. **Suno** open for battle/boss-style tracks. PiP: three on couch/stage, Grok Bot Galaxy sign. Chat: Hive Dynamics — “Lobby-song review live: audio-engineer bot dumped Strudel tones into Notion — calm/soothing lobby tracks, hit play and listen on-air.”; “GROKBOT BATTLE MUSIC”; JRPG / Fire Red comparisons; “I created new bot using dr eggbot”.
- **Final (~8:23)** — End card: black field, ring of colorful bot icons, **“Grok Bot Galaxy”** + **“Final day starts tomorrow at 8:30am PST.”** Player **8:23:18/8:23:19**; **~378K** views. Chat at end tip included: “THE WEBSITE IS BOSS LOL”; “Love your website Shardul”; card-game jokes (Yu-Gi-Oh / Magic). Shot: `assets/day2-eod-endcard.png`.

### Speakers / roles (observed + schedule)
- **SE block:** Amrita Venkatraman (schedule + Sherlock workspace name); Templates / Sherlock demos.
- **SDR block:** Simon Lackowski (schedule + chat ID; not captioned).
- **Support block:** David Gan (schedule + capture ID; not captioned).
- **Sales (midday):** SpaceXAI Sales Team per schedule — **not densely scrubbed**.
- **Build spine:** Cupcake game studio on `shipbythursday/cupcake`; fleet Chief / Bake / Glow / Crit / Pixel / Ping / Shardul / Data / arena / Tone (audio); host used **dr eggbot** as duplicate seed for free-bot promo.
- **Stage core:** presenters often uncaptioned; poteto affinity in chat + Lauren critique cards referenced for Crit.

### Product claims / demos (observed)
- Role **templates** + attribute “game” framing for SE.
- Hard constraints in travel demo: **Postgres row locks + hold**.
- SDR playbook: prospect → sequence → research → draft copy.
- Wrap slide: End to End / Intentional / Systematic.
- **Ping** mention listeners + task kanban.
- Multi-bot game studio with **Notion as SsOT**; cloud-agent PR swarm; connector 404 failure mode.
- **Support Agent Rules** with Public Docs vs Internal Policies + confidence handoff + Auto-review gate.
- Audio bot → Notion Foley + **Suno** / Strudel on-air listen.
- Promo: free month via **dr eggbot** duplicate (first 1,000).

### Chat themes (live tips; not seek-replay)
- Cost/speed/tokens; functional bot names; SsOT / Notion; poteto love; QR free-bot rush; Plain support praise; music taste (JRPG / battle); website praise for Shardul; “why did this turn into a Cursor Livestream” (later tip memory).

## Themes
1. **Department playbooks** — SE → Sales → SDR → Support as role-shaped bot packs, not one generic agent.
2. **Templates + competition framing** — bots as characters with attributes; head-to-head demos.
3. **Single source of truth (Notion)** — host ordered fleet to keep Notion updated; 404 exposed connector fragility.
4. **Named single-duty fleet** — Chief/Bake/Glow/Crit/Pixel/Ping/Tone/Shardul parallel work on Cupcake.
5. **Support discipline** — Public Docs for answers; Internal Policies never pasted; confidence → handoff; Auto-review before Slack writes.
6. **Creative pipeline bots** — audio engineer → Foley stubs + Suno/Strudel into the same SsOT.
7. **Audience maps to poteto / dr eggbot** — chat + critique-card grounding + free-bot seed via dr eggbot.

## Improvements for Wedge
Ranked, tied to existing fleet only. Do **not** create/edit bots/routines/skills in this pass — recommendations only.

1. **SsOT + connector health (Steward + Watch)** — Day 2’s Notion 404 stalled Crit mid-demo. Cheap next step: Steward first-session pin “if a connector 404s, say blocked — don’t invent the page”; Watch Mon/Wed/Fri one line on any feeder that needs Notion/GitHub/X and last success.
2. **Support-style Reply vs Handoff (Intake + Brief)** — Copy the high/medium/low confidence gate: low/ambiguous → handoff to Wedge, never invent. Cheap next step: add three confidence labels to Intake/Brief decision lines for one week.
3. **Public vs internal knowledge split (Corpus + Steward)** — Support Rules: Public Docs answer; Internal Policies decide only / never paste. Cheap next step: Corpus Monday mold audit adds “did any bot paste internal-only into a public-facing draft?”
4. **Fleet tell / shared memory broadcast (dr eggbot pattern → Steward Friday)** — Host used dr eggbot to tell 8 bots + save shared memory. Cheap next step: Steward Friday pulse includes “one fleet-tell sentence” when a rule changes (no new bot).
5. **Named single-duty clarity (no new bots)** — Cupcake fleet roles were verbs/titles. Cheap next step: kill fuzzy overlap among Intake/Watch/Brief/Steward/Corpus/Galaxy only; Galaxy stays notes→improvements only.
6. **Auto-review before external write (Steward pin)** — Support demo blocked Slack until approve. Cheap next step: Steward pin for any bot that can post outside chat: “external write needs explicit ask / approval path.”
7. **Creative artifact → dated file (Galaxy + Recap pattern)** — Tone wrote Foley into Notion with listen stubs. Cheap next step: keep Galaxy EOD as the dated markdown SsOT for streams (already doing); Recap stays long-form only — don’t merge lanes.
8. **poteto-mode for build-adjacent asks (existing skill)** — Chat “we love @poteto” + Lauren critique cards. Cheap next step: point coding/design helpers at [poteto-mode](sand-workflow:poteto-mode) on nontrivial work; feeders stay terse.
9. **Token/cost opacity (Watch)** — Chat still asked usage %. Cheap next step: Watch weekly “usage opaque / visible” one-liner if any UI is reachable; else leave pin.

## Open questions / gaps
- **Sales session (12:30–2:00 PT)** not densely VOD-scrubbed — schedule-aligned gap.
- Exact SE→Sales→SDR handoff player clocks not fully mapped.
- Speaker names often not captioned; Amrita / Simon / David from schedule + workspace/chat/capture — faces not name-plated every frame.
- Whether **Tone** ≡ audio-engineer bot spun on-stream — likely but not caption-confirmed.
- QR destination for free Grok Bot promo — not decoded.
- Whether Ticket Generator / Tune / Alert / Build are distinct bots vs Support UI chrome — unclear.
- Replay chat on seek may be stale; live-tip quotes preferred.
- **Day 3 X broadcast URL** still not published as a concrete `x.com/i/broadcasts/…` on x.ai/galaxy fetch (hub says watch on X; start 8:30am PT / end card “8:30am PST”). Do not invent. Day 3 schedule: Marketing Ops (Silberman/Hsu) · Post-Sales (Blake Schuller) · Marketing (Josh Kim) · Wrap + Final Showcase 4:30–5:30.
- Actual X end ~16:53 PDT vs schedule “6:00 PM Day 2 Livestream Ends” — early end relative to schedule card.

## Screenshot refs (box)
- End card final: `assets/day2-eod-endcard.png` (also `/tmp/.sand-browser/shot-call_4eLUP25NvLR8LJsPBIDT2xeOfc_090be62b212d5f13.png`)
- Sound design / Tone / Suno: `assets/day2-sound-design.png`
- Additional live-tip captures remain under `/tmp/.sand-browser/shot-call_*` from Day 2 coverage (Ping, Cupcake fleet, Support Rules, David Gan stage, promo QR).
