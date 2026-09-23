# Fleet audit PACKET — draft for dr eggbot

**Date:** 2026-09-23 (Asia/Saigon)  
**Owner ask:** Wedge → eggbot fleet audit  
**Sources:** Galaxy Days 1–3 complete + Day2/3 summary + EOD skims; 19 `profile.json` under `/home/box/agent-data/agents/`; journal `2026-08-27-xingye-texts-as-a-person.md` (Lauren Kwok cadence); journal `2026-09-18-grok-bot-galaxy-rules.md`.  
**Scope:** recommendations only — no bots/routines created or edited this pass.  
**Lauren split:** Lauren Tan (@poteto) = critique cards, poteto-mode, Cloud PR authorship (Galaxy live). Lauren Kwok (SpaceXAI) = routine frequency + fresh bot for recurring work (Xingye journal).

---

### A. Fleet map (live bots)

Confirmed **19** profiles on box (matches known fleet; no unnamed orphans). Cadences are Asia/Taipei unless noted.

- **Brief** — five-line morning push (what changes this week). Cadence: daily 07:00. Fence: not Yuedu (Chinese), not Field (setups), never invent Watch lines/forks. Health: **tight**.
- **Watch** — CF estate + audience + Logos52 CI + one FLEET pulse line; USAGE real-or-opaque. Cadence: Mon/Wed/Fri 08:00. Fence: report-only (no deploy/purge/DNS/Actions re-run); not Corpus. Health: **tight** (fleet line already encodes Day-1 overlay ask).
- **dr stewbot** — fleet honesty, no lane; Friday ~10:41 pulse + security pin; weekday 18:00 packets backup; Lock/Iterate/Hold on forks. Fence: not eggbot, not Watch/Corpus/Brief. Health: **tight**.
- **Intake** — AI / learning-science / wiki-craft feeder from `intake-sources.md` only. Cadence: Mon/Wed/Fri noon. Fence: bounce practice→Field, Chinese→Yuedu, shows→Recap; no vault. Health: **tight**; overlap risk if scoring drifts into Field setups.
- **Field** — named-practice hunt from `field-sources.md` only. Cadence: daily 08:00; chat only on high-pri “change this week.” Fence: no fleet design/roster recs; bounce library→Intake; no vault. Health: **tight**.
- **Recap** — long-form pin LIST/INGEST/WIKI-on-demand (All-In, Maxinomics, Justin Sung, Elon sit-downs, Fern/Moon/Frontpage; Naval when live). Cadence: daily noon. Fence: never Arguments pins (TRIGGERnometry/a16z/Asmongold). Health: **tight**.
- **Arguments** — argument ingest for TRIGGERnometry, a16z, Design Theory, Asmongold talk VODs. Fence: never Recap pins. Health: **tight** (Asmongold scope is the fuzzy edge — talk/argument only, not every highlight).
- **Galaxy** — Galaxy livestream notes → ranked fleet improvements. On-assignment. Fence: never CreateAgent / edit fleet; notes-only. Health: **tight**; fence vs eggbot must stay hard.
- **Yuedu** — Chinese reading queue + learning-method news from `yuedu-sources.md`. Cadence: Tue/Fri 07:30. Fence: no dictionary/wiki writes; Chinese stays out of Brief; no Dcard. Health: **tight**.
- **多恩刊** — midnight Taiwan-life harvest → files only (今日無刊 still writes). Cadence: daily 00:00; no chat ping. Fence: no graded rewrite, no Decisions, no Field, no English glosses. Health: **tight**.
- **Corpus** — logos52.github.io honesty (Mon mold audit; Tue/Thu thin change-scan; quiet if empty). Fence: report-only, never edit repo; not Watch. Health: **tight** (Day-1 morning change-scan already landed here).
- **Table** — public calendar for EQL / WoW / FFXIV + pinned dates. Cadence: Wed/Sat 09:00. Fence: official pages only; no APIs/logins. Health: **tight**; low strategic heat.
- **Haggle** — buy-offs / landed-cost tables; never book/pay without explicit OK. On-demand. Fence: not checkout; not Route. Health: **tight**.
- **Route** — travel how-to-go / meet spots / food / caveats. On-demand. Fence: never book; not Haggle; not Brief. Health: **tight**.
- **dr eggbot** — design + CreateAgent; poteto-mode bar for coding bots; CloudAgent coordinator for repo PRs (Wedge merges). On-demand. Fence: never harvest feeder lanes; never become stewbot; never Watch/Corpus-as-merge. Health: **tight** by JD; **overlap risk** if asked to “just verify” (Engineer’s seat).
- **Engineer** — create/maintain project `verify-<app>` skills; prove like a user; CloudAgent for repo writes; quiet when clean. Fence: no CreateAgent; no merge/deploy; no research harvest. Health: **tight** (new seat; prove it stays verify-only).
- **dr bite** — past-24h compression of sibling ingest (Recap/Arguments + Intake/Field/Yuedu). Cadence: daily 13:00 (app TZ); quiet when empty. Fence: never re-watch/scrape; not Recap/Arguments/Intake. Health: **tight** as compressor; **overlap risk** with Brief if bite starts deciding “what changes this week.”
- **星野遙香** — in-character LINE friend (繁體); own draw + hourly send window; friend not tutor. Fence: no commands in her 1:1; no gloss/homework; settings via 後台 only. Health: **tight** character; cadence discipline is the standing risk (see Kwok).
- **後台** — cast machine: weather/holiday alerts, backup, remember/status commands; never speaks as 星野. Routines: 13:00 weather, 09:00 holidays, 03:00 backup (Asia/Tokyo). Fence: no clock-wake of her day; no article dumps; no draws. Health: **tight**.

**Known fences (confirm):** Recap↔Arguments · Intake↔Field↔Yuedu · Watch↔Corpus · Galaxy↔eggbot · 星野↔後台. Also enforce: Haggle↔Route · eggbot↔Engineer · bite↛Brief decision · stewbot↛CreateAgent.

---

### B. Optimizations on EXISTING bots (ranked)

Prefer **Lock / Iterate / Hold**. Cite Galaxy day.

1. **Lock — Watch FLEET pulse as the Day-1 overlay strip (Watch + stewbot).** Day 1: visible fleet health. Watch already owns “last routine fire / silent-vs-ok”; Steward Friday one-line fleet pulse. **Action:** this week’s Mon/Wed/Fri Watch run must include all 19 names (or “silent ok”); Friday stewbot cites that file, no invent. No new bot.

2. **Lock — Brief forks = Lock / Iterate / Hold + owner bot (Brief + stewbot).** Day 1 admin mock; Day 3 Territory Planner. Brief profile already requires it. **Action:** audit last 7 `brief/latest.md` — any real fork missing the triad → Iterate profile/examples until every fork names who builds on Lock.

3. **Lock — governed agency pin on stewbot (already in JD; make it sticky).** Day 3: Approve/Hold + “hold — leave WAF.” **Action:** first-session + Friday line: external sends **and** destructive infra default Hold; shared box ≠ isolation; connector 404 = blocked (Day 2 Notion), never invent SsOT page.

4. **Iterate — bite vs Brief boundary (bite + Brief).** bite compresses ingest; Brief decides week-action. **Action:** bite bullets stay “what siblings said”; never “do X this week” unless quoting Brief. If bite starts agenda-setting → Hold bite expansion, Lock the fence in both profiles.

5. **Iterate — Arguments Asmongold edge (Arguments).** Fuzzy: talk/argument VODs vs every TV highlight. **Action:** add one hard example pair in description (in / out); if still noisy after 2 weeks → Hold new Asmongold until pins re-ruled.

6. **Iterate — Intake/Field bounce discipline (Intake + Field).** Day 3: scope like JD. **Action:** after each Intake packet, count mis-scored “named practice” items; if ≥2/run two weeks running → Lock a bounce checklist in both profiles (not a new bot).

7. **Hold — eggbot CreateAgent wave.** Galaxy↔eggbot fence + Day 3 “prefer existing.” **Action:** no new seats until §C earns one; eggbot designs only on explicit Wedge ask. Galaxy keeps recommending, never creating.

8. **Lock — poteto-mode + verify before unattended coding (eggbot + Engineer).** Day 1–3: @poteto PR authorship, critique cards, Poteto Mode + `/verify-cupcake`. **Action:** nontrivial CloudAgent runs require poteto-mode + an existing `verify-*` skill (Engineer creates/maintains; eggbot does not stretch into verify).

9. **Iterate — Corpus change-scan quiet contract (Corpus).** Day 1 morning scan. Already Tue/Thu thin + quiet if empty. **Action:** confirm two consecutive empty Tue/Thu produced **no** chat filler; if filler appears → Lock “file-only on empty.”

10. **Hold — Table expansion / game APIs.** Low heat, official pages only. Don’t stretch into Watch or Intake.

11. **Iterate — Haggle↔Route handoff clarity.** Travel buy-off vs how-to-go. **Action:** one shared one-liner each can paste: “price/counter → Haggle; logistics/meet/food → Route.”

12. **Lock — 星野 cadence (後台 + 星野 settings).** Lauren Kwok: 15-min ≈ ~100/day is crazy; hourly or few/day enough; recurring work on fresh bot (後台), character chat stays clean. **Action:** keep standing initiated sends at 1–2/day with skip days; never poll 15-min; never put settings English in Xingye 1:1.

---

### C. Gaps / NEW specialized bots worth considering

Only seats that earn a single duty. Prefer stretching existing first.

| Candidate | Job | Why not stretch | Anti-jobs | Delivery path |
|-----------|-----|-----------------|-----------|---------------|
| **Spec** (maybe) | Lock a `*-product-spec.md` before multi-bot / CloudAgent builds (Day 3 Juno Lead Deck). | Intake is feeder not product owner; eggbot designs bots not product specs; Brief is morning push. | No coding, no CreateAgent, no merge, no research harvest. | Chat draft → locked file path → eggbot/Engineer/CloudAgent read-only. |
| **Draft** (maybe, thin) | Outbound Accept/Skip/Reject drafts (Day 3 Franny Form). | Brief can Hold send; stewbot can pin gate. Only earn if Wedge regularly needs non-Brief outbound (email/X) with HITL. | Never send; never become Brief. | Draft artifact + triad; Wedge Accept. |
| **do NOT add — CoS / manager bot** | — | Galaxy rules refuse chief-of-staff in front (holds every login; shared box). stewbot is honesty, not routing. | — | — |
| **do NOT add — merge bot** | — | Done = Wedge merges; no bot merges (Galaxy rules + eggbot/Engineer JDs). | — | — |
| **do NOT add — tutor / gloss bot beside 星野** | — | Xingye journal: teacher-Bot is never-try; friend wins. Yuedu is reading queue not grader. | — | — |
| **do NOT add — 15-min clock / Emily-Lai joke bot** | — | Kwok cadence; Emily 48/day refused. | — | — |
| **do NOT add — second Galaxy-like note bot** | — | Galaxy already notes→improvements; eggbot creates. | — | — |
| **do NOT add — usage/$ invent bot** | — | Watch USAGE: real or “opaque”; never invent (Day 1 chat beg). | — | — |
| **do NOT add — Notion/SsOT writer swarm** | — | Desk SsOT is dated files + git; Day 2 connector 404 is the lesson. | — | — |

**Default this week:** Hold all new seats. Unlock Spec only if a real multi-bot build is queued without a locked md.

---

### D. Operator mindset (Wedge) — drills from Lauren + Galaxy

Not slogans — run these.

1. **JD drill (Day 3 Marketing + rules page).** Before any new bot or duty: write one standing job + anti-jobs + delivery + quiet-when-empty in ≤10 lines. If you need “and also,” split or Hold.
2. **Governed agency drill (Day 3).** Anything that leaves the account or touches protective infra: bot prepares, you Approve/Hold. Default Hold on WAF-class toggles. Say the Hold out loud once so the chat log owns it.
3. **SsOT honesty drill (Day 2).** Name the file that is true. If connector/path 404s, write “blocked” — never invent the page. One owner writes; others read.
4. **Critique-card / poteto bar drill (Lauren Tan).** For coding: one job, unslopped, verified, deliberate subagents. Reject PRs that are mocks without playable proof. poteto-mode before swarm.
5. **Draft-before-send drill (Day 3 Franny).** Artifact first; Accept/Skip/Reject(+reason). Skip/Hold is success, not failure.
6. **Colleagues not tools drill (Day 1).** Message named bots with outcomes; keep long-running context on the bot that owns the lane; don’t paste six jobs into one chat.
7. **Quiet-when-empty drill.** Zero packet is legal (Intake/Field/Corpus/bite/Brief). If you miss the ping, check the file before asking “are you broken?”
8. **Merge ownership drill (rules + eggbot/Engineer).** CloudAgent owns VM/branch/PR; you merge. “Agent finished” ≠ done.
9. **Routine cadence drill (Lauren Kwok).** Prefer few/day or exception-only. Recurring knob-twiddling → fresh bot (後台 pattern), not the character/feeder chat. Never 15-min polls.
10. **Fence drill.** When a bot answers outside its box, reply with the fence name (e.g. “Arguments pin”) and bounce — don’t argue the content.
11. **Duplicate-for-empty-memory drill (rules).** Fat chat → duplicate bot, same JD, empty memory; don’t keep paying long-context tax on routines.
12. **Lock/Iterate/Hold fork drill (Day 1).** Every real fork: three labels + owner bot on Lock. Record yes/no after you choose so Friday stewbot can build on it.

---

### E. Sidebar / org chart suggestion

Six-section map **updated** (Engineer + bite seated; no orphans left outside):

1. **Morning** — Brief · Watch · dr stewbot  
2. **Research** — Intake · Field · Recap · Arguments · Galaxy · **dr bite** (compress layer under research, not morning)  
3. **Language / life** — Yuedu · 多恩刊  
4. **Ops / wiki** — Corpus · Table  
5. **On-demand / build** — Haggle · Route · dr eggbot · **Engineer**  
6. **Cast** — 星野遙香 · 後台  

**Notes for sidebar chrome:** bite sits under Research (sibling of ingest, not Brief). Engineer sits beside eggbot under On-demand/build (verify ≠ design). Table stays Ops even if low heat — don’t orphan into On-demand.

---

### F. Top 7 next moves this week

Ordered, concrete.

1. **Mon Watch** — emit full 19-name FLEET pulse (last fire / silent-vs-ok) into `watch/latest.md`; Brief must read it next morning.  
2. **Brief audit** — review last 7 days of forks; any missing Lock/Iterate/Hold+owner → fix examples in Brief profile (Iterate).  
3. **stewbot Friday** — one fleet pulse citing Watch + security pin (shared box ≠ isolation; Hold on external/infra). No inventory dump.  
4. **Fence pin pass** — eggbot (or Wedge paste) confirm Galaxy↔eggbot, bite↛Brief, eggbot↔Engineer in the three profiles’ anti-jobs (wording only; no new duties).  
5. **Engineer smoke** — pick one live app with or without `verify-*`; either maintain-clean report or create-verification-skill once; prove quiet-when-clean.  
6. **Xingye cadence check (後台 status)** — confirm initiated sends still ~1–2/day with skip/pause legal; no 15-min or hourly spam; settings only in 後台.  
7. **Hold CreateAgent** — no new specialized bots unless a locked product-spec is on disk for a real build; Galaxy recs stay recs.

---

*End of PACKET. Draft path: `/workspace/packets/fleet-audit-2026-09-23-draft.md`*
