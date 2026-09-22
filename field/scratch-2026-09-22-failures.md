# Field Grok Bot failure hunt · packet 2026-09-22 (Tuesday)
Cutoff: after ~2026-09-20/21 00:00 UTC (post Monday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+after:2026-09-20` (+ `after:2026-09-21`). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Mon KEEP chrisoh806 172401 (Update/Reset hung 43% Transferring = backend rehydrate; wait / Recover-after-failed). Sun KEEP BigBojangles 172349 (local-exec root). Sat KEEP Volkan_Erdogan 172135; Sat KEEP Anderson_V_Leite 172142. Fri KEEP Dave_Campos 172070; Fri KEEP allninety 171962. Thu KEEP ziemovit 171791; Thu KEEP Mercer_Alex 171840. Wed KEEP Kostadin_S 171735; Wed KEEP Nathan_Arizona 171676. Standing: Catty Kaspersky / Andrew Zscaler / Serene usage-silent / Kin_Su DNS / thomas2018 webhook / Channels_Cintara Update-Computer auth / first-init incomplete / Windows partial-state AV / allninety account-stuck / Carter 172368 reinforce. Overflow re-check: UCC3 172453 (topic deleted by author — close); jsolly 172015 (no elevate); warpdev 172343 (Backup-not-ready still; no new durable teach); doughy 171895 (still out-of-window backlog).

## KEEP candidates (1) — recommend for packet (edu setups take priority for cap)

### KEEP 1 — Michael_Pan · forever-box “missing agent-transcripts” = server-side runtime; use ReadTranscript; local mirror empty is expected
- url: https://forum.cursor.com/t/grok-bot-forever-box-agent-transcripts-mirror-never-created-server-agent-proxy-transcript-tail-connecterror/172494
- date: OP 2026-09-21 11:49 UTC; Colin 2026-09-21 17:12 UTC; OP close-loop 2026-09-21 18:58 UTC
- tags: persistent-computer, teach-once, coverage-ceiling, killed-claim (misdiagnosed)
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·persistent-computer·teach-once·coverage-ceiling] score=10 | Michael_Pan | Forever-box fleet healthcheck expected on-disk `$AGENT_TRANSCRIPTS` / `agent-transcripts/` + `transcript_entries` / search-index — all empty while chats work; host log `server-agent-proxy: server transcript tail dropped … ConnectError`. **Colin: expected, not a broken mirror** — bots run on **server-side runtime**; chat history lives on the server; nothing local writes `agent-transcripts/` / transcript tables / search index anymore. ConnectError lines = read-only feed reconnecting (server closes stream ~20 min by design); high attempt counters were a fixed host bug. Teach: **use ReadTranscript** (own history; `agent_id` for same-account peer; `session_id` / `subagent_id`; pages newest-first with `before`) — **not** local file greps. Known gap: in-app Search still local-only (empty for these bots; tracked separately). OP rewrote harness healthcheck → ReadTranscript; closed. Alert: **no** (durable mechanism teach; Field edu lane has no transcript-healthcheck path to change this week — only alert if a roster harness still assumes on-disk mirrors).
- staff: Colin (server-side runtime; ReadTranscript API shape; Search gap)
- siblings: Sanghoon_Kang 172009 parent-quiet-while-Cloud-Agents (observability cousin); doughy 171895 memory/brain-docs (different); 170727 Auto-review bind (resolved separately)
- bank: raw/ai/2026-09-22-michael-pan-grok-bot-forever-box-agent-transcripts.md

## OVERFLOW / watch (not packet KEEP)

### nhog 172535 — 43% Transferring cousin; kevinn reinforce + fix shipped
- Same family as Mon KEEP chrisoh806 172401. kevinn: auto Update copy-step stuck; existing computer/bots/files untouched; account gave up ~20 min later; **don’t Reset** (wipes); wait ~1h for finish/fail; mobile keeps working during desktop dialog; **team rolled out change for stuck copy**. Bounce/merge reinforce — do not second-KEEP. Alert: no.

### Timothy_Gresh 172549 — Windows 0.57.1 quits under local Shell/CopyFromBox + Chrome UI; idle stays up
- Named pattern: light Shell OK hours; heavier CopyFromBox→%TEMP% + Win32 Chrome focus/automation → ListMachines disconnect + window vanishes (no WER/Sentry). No staff yet. Score≈5 (portable 3 / evidence 2) — **under ≥6**. Watch for staff durable teach → possible elevate Wed. Alert: no.

### Coordinacion_Desarro 172519 — Agent Computer “starting up” ~48–72h; Update/Reset failed all devices
- Account-wide (phone+desktop+laptop); asks server reprovision; won’t Reset again. No staff yet. Strong allninety/Carter attach cousin. Watch for staff elevate. Alert: no.

### Palan 171969 — Sep 21 update: after wipe/reinstall still ELB 404 us9 “could not be routed”
- Pre-cutoff OP; mohitjain initially DNS (Kin_Su family). New evidence: client local OK; `sand.box_reachability` network/ControlPortCallError; us9.cursorvm.com ELB 404 — **backend unroutable**, not local DNS. Elevates standing DNS family toward Carter-style account-stuck — **reinforce only**, do not KEEP. Watch for staff backend rebind. Alert: no.

### Carter-Ventucci 172368 — mohitjain Sep 21: account healthy again; quit+reopen
- Closes Mon reinforce: replica cleanup landed; bots/files intact. Standing allninety family — bounce reinforce. Alert: no.

### jsolly 172015 — mobile Settings scroll flips Auto-review
- No new staff since Mon; OP reiterates footgun. Soft friction overflow (score≈8) — **not packet KEEP** (edu cap; not killed/computer). Soft promote only if compiler has free friction slot. Alert: no.

### warpdev 172343 — Backup-not-ready still blocks Update
- No new staff; healthy runtime ≠ update unblocked (T-F98010). Watch; no new durable teach beyond 172401 cousin. Alert: no.

### UCC3 172453 — topic deleted by author
- Mon overflow closed; no elevate path. Drop from watch.

### jsolly 170727 — Auto-review “executable content could not be bound” **FIXED**
- Colin: fix shipped; jsolly retested after Computer Update — python absolute + npm-in-path bind path pass; closes original. Resolution note for compiler backlog, not failure KEEP. (.mts / strip-types shape still TBD.)

### Tyler_Miller 172457 — Grok-handed Cloud Agent never started → empty transcript
- Colin: Archive blank bc-… entry; re-run. Soft observability; not Grok Bot computer kill. Bounce/soft.

### doughy 171895 — brain-docs snapshot cut short
- Still pre-cutoff / out of window; backlog only.

## BOUNCE

### Already-kept reinforced
- chrisoh806 172401 — Mon KEEP skip; nhog 172535 / Zomer 172431 cousins merge
- BigBojangles 172349 — Sun
- Volkan 172135 / Anderson 172142 — Sat
- Dave_Campos / allninety — Fri; Carter 172368 closed healthy
- Mercer siblings / Nads 171858 — Colin closed fleet hub “stable place” Sep 21 — no elevate

### Standing families / misdiagnosis
- Bluevisuals 172529 — “can’t reach your computer” thin OP (Serene/Kin_Su/first-init cousin)
- Palan 171969 — Kin_Su→account-stuck reinforce (see overflow)
- 168499 Vercel plugin OAuth “redirect URL invalid” — Colin known since ~Sep 16; nothing user can change; gate-only (off-lane GTM)

### Non-failure / UX / FR
- David.J 172461 — agent labels/chips removed on desktop 0.57 **intentional** (Colin); iOS still has them; stored labels kept
- Ryan_Daley 172545 — routines don’t wake / don’t finish on time — FR/ops, no staff
- GrokUser841719 172533 — false play/state claims honesty FR (killed seat) — product trust FR, not setup kill
- jsolly 172561 — Cursor iOS Agents Live Activity “Waiting” while Working — Cloud Agent surface, not Grok Bot failure
- francotgs 172502 — window-state.json 0x0; Colin: file ignored on relaunch; real no-window = exit_code=21 sandbox refuse — soft UX
- stacker21 172524 — 1Password vault-only; Colin: Shared with Grok Bot vault design — not a failure
- TheAviv 172456 — honesty/show-before-send Instructions mitigate — product defaults FR
- diaoguoliang 172465 — Clear chat FR → merged into 168333 prune/compact
- David_Stredansky 172445 — praise “got faster”
- Johnsters 171745 — product confusion
- Meetup stubs / usage quota threads — bounce

## Fetch notes
- Tag latest p0–p1 + search after:2026-09-20 / after:2026-09-21 → `/workspace/field/forum0922/`
- Priority topics fetched: 172494, 172535, 172549, 172519, 172502, 172545, 172561, 171969, 172461, 168499, 172457, 172524, 172456, 172465, 172529, 172533, 170727, 172401, 172453, 172015, 172343, 172368, 171858, 172431, 172371, 172445, 172478, 172354, 170819, 172380, 172135, 171540, 172484
- `c/grok-bot/33.json` skipped
- Bank INDEX grepped — no prior 172494
- Appended fully-read new topic ids to seen-forum-ids.txt (this hunt; 323→340)

## Bank deposits
- KEEP: `raw/ai/2026-09-22-michael-pan-grok-bot-forever-box-agent-transcripts.md` ← 172494

## Result for compiler
- FAILURES recommend: **1** (Michael_Pan 172494 — server-side transcripts / ReadTranscript) — edu SETUPS take remaining cap slots
- Soft overflow promote if slot: jsolly 172015 (mobile scroll flips Auto-review) score≈8; Timothy_Gresh 172549 watch for staff
- KILLED mirror: empty local `agent-transcripts/` on forever box ≠ dead host — **server-side runtime**; healthcheck via **ReadTranscript**, not file mirror; ConnectError transcript-tail = reconnect noise
- Related reinforce (not KEEP): nhog 172535 / 172401 family — don’t Reset on 43%; wait ~1h; copy-step fix shipped
- Alert: **none**
