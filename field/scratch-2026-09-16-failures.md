# Field Grok Bot failure hunt · packet 2026-09-16 (Wednesday)
Cutoff: after ~2026-09-15 00:00 UTC (post Tuesday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–2 + `search.json?q=Grok+Bot+after:2026-09-14` (+ `after:2026-09-15`, keyword variants). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Tue KEEP huanl 171563 (Reconnecting = inactive SuperGrok/trial access — bounce only); Tue KEEP Serene_Thornton 171615 (weekly-limit silent — bounce only; siblings 171626/171588). Mon KEEP Kin_Su 171482 (DNS SERVFAIL — bounce); Mon KEEP enescanguven 171441 (secure-card — bounce); Sun KEEP jamie_burt 171438 (ENAMETOOLONG — bounce). Standing skip: Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270, Catty Kaspersky family 171308+, thomas2018 171324 (webhook UI — reinforce only), Channels_Cintara Update-Computer auth, Surfshark Temp, session-revoke, F-Secure DeepGuard, Auto-review bind, SuperGrok Start routines, Desktop-secrets overwrite, workspace-media OOS, Ricardo_Daud 171555 overflow, webhook cluster Alex0 171606 / Grzesiek 171664 / Shaun_Bowe 171677. Standing watch elevated below: Nathan_Arizona 171676.

## KEEP candidates (2)

### KEEP 1 — Kostadin_S · Cloud computer lost backend reach; desktop view OK; not usage; Reset/Update rejected server-side
- url: https://forum.cursor.com/t/grok-bot-android-all-bots-fail-to-generate-after-reset-computer-view-works-weekly-usage-72-not-capped/171735
- date: OP 2026-09-15 11:17 UTC; deanrie 11:54 UTC; Colin 11:57 UTC
- tags: killed-claim, persistent-computer, coverage-ceiling
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=9 | Kostadin_S | Android (+ same-account desktop closed): every bot → “Bot failed to respond” / “Message not delivered”; Agent Computer view still works (/workspace, Chrome, terminal); Weekly usage 72% (OP correctly ruled out cap); Reset/Update from phone rejected or timed out. OP asked inspect sendPrompt / don’t wipe again. deanrie: diagnosis spot on — **not** weekly usage, **not** Android app; cloud computer lost ability to reach backend mid Sep 13; desktop stream healthy so preview works while generation dies. Reset/Update did nothing useful (rejected server-side). Teach: don’t Reset/Update/reinstall while staff restores or migrates computer (data + backup intact); after restore fully quit Android + hello Master. Colin: restart and try again. Distinct from Serene weekly-limit silent (computer preview OK **and** usage capped there) and from huanl Reconnecting=no-access. Killed: don’t chase Reset when generation fails but computer view works and Usage isn’t at 100%. Alert: **no** (server-side restore teach; not a this-week Field file/setting change).
- staff: deanrie (mechanism); Colin (restart nudge)
- siblings: stoplion123 171698 (zombie-healthy — Reset **helped**; contrast); Diazb123 170915 / nitesh_sharma 170954 prior “failed to respond” backend class (seen/ops)
- bank: raw/ai/2026-09-16-kostadin-s-grok-bot-android-all-bots-fail.md

### KEEP 2 — Nathan_Arizona · Slack private-channel trigger never fires until Cursor app invited (Test Run ≠ subscription) — elevated from Tue watch
- url: https://forum.cursor.com/t/grok-bot-slack-routine-trigger-never-fires-while-test-run-and-slack-return-both-work/171676
- date: OP 2026-09-14 22:31 UTC; kevinn 2026-09-15 03:36 UTC
- tags: human-gate, quiet-when-nothing, coverage-ceiling
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·human-gate·quiet-when-nothing] score=9 | Nathan_Arizona | Slack-triggered routine Active; canary in #tars-conduit never sets lastRunAt; Test Run OK + Slack plugin write/readback OK → OP asked backend subscription recover. kevinn: **no message from channel ever reached Cursor** — channel is **private** and Slack only delivers when **Cursor Slack app is a member**; it wasn’t. Test Run bypasses Slack entirely; reply path is a different Slack app than the listener. Teach: `/invite @Cursor` in the private channel → wait ~1 min → repost canary → check Run history. Don’t Reset computer or recreate routine chasing “trigger dead” when Test Run works. Elevates Tue overflow watch after staff confirm. Sibling watch: ziemovit 171791 GitHub “issue assigned” never fires (no staff yet; same trigger-silent class). Alert: **no** (copyable Slack membership gate; not a Wedge this-week Field path change).
- staff: kevinn (private-channel membership checklist)
- siblings: ziemovit 171791 (GitHub issue-assigned silent — watch); webhook URL-missing cluster standing (thomas2018)
- bank: raw/ai/2026-09-16-nathan-arizona-grok-bot-slack-routine-trigger-never.md

## OVERFLOW / watch (not packet KEEP)

### yuan_fang 171747 — Trial usage allowance silent (Connecting costume; usage shows 0%)
- https://forum.cursor.com/t/grok-bot-mac-mobile-computer-stuck-connecting-messages-get-no-reply-ticket-t-f81493/171747 — deanrie: computer fine; don’t Reset again; **trial Grok Bot usage allowance used up**; app should notify (missing); usage 0% = empty enabled pool not remaining trial balance; pick plan / SuperGrok + quit menu-bar + reopen. Connecting panel = slow health check / VPN — doesn’t block replies. Score ~8–9 quiet-when-nothing; overflow (Serene weekly sibling with **trial** flavor; education slots preferred).

### bibimbap 171704 — Weekly included usage silent after Reset (Serene sibling — do not re-KEEP)
- https://forum.cursor.com/t/grok-bot-0-47-0-windows-all-bots-no-reply-after-reset/171704 — deanrie: weekly included used ~Tue 13:30 KST; Settings → Usage; on-demand at cursor.com/dashboard/spending; Cursor Pro ≠ Grok Bot pool; dual app copies 0.47/0.51. Reinforce Serene 171615 only.

### stoplion123 171698 — Zombie-healthy computer: reports healthy but all requests fail; Reset helped
- https://forum.cursor.com/t/grokbot-failing-to-respond/171698 — Colin: computer stuck reporting healthy so never auto-replaced; phone “Can’t reach” + bot fail; desktop Reset brought fresh computer with bots/files preserved. Contrast KEEP 1 (don’t Reset) — Reset correct when zombie-healthy. Score ~8 persistent-computer; overflow (ops resolution; Cap).

### Benny_Leng 171740 — Can’t reach / Reset stuck 50% / partial state day#3 (ops)
- https://forum.cursor.com/t/grok-bot-cannot-connect-to-its-agent-computer-t-f77505/171740 — Colin restart nudges; OP still broken evening Sep 15. Watch/ops; no portable gate yet.

### ziemovit 171791 — GitHub “issue assigned” routine never fires (5 attempts)
- https://forum.cursor.com/t/grok-bot-github-issue-assigned-routine-never-fires-5-attempts-recreated-routine-app-has-repo-access/171791 — no staff; chat handle works; trigger silent; notes webhook UI gap. Watch with Nathan class.

### Liyo_K 171796 / GFP 171703 — New-user / OSX can’t reach + Reset/Recover fail
- No staff yet; ops/partial-state watch.

### Andrew_van_Niekerk 171777 — Permanent Reconnecting 0.51.0 (healthy local diagnostics)
- No staff; could be huanl access costume or Kin_Su DNS cousin — thin until staff.

### traeyee 171742 — Does Grok Bot consume Cursor quota? (tip, not failure)
- Colin: separate weekly Grok Bot pool; cloud-agent launch exception; on-demand spill. Tip/library.

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- huanl 171563 / Serene 171615 (+171626/171588) — no new mechanism; yuan_fang/bibimbap are trial/weekly cousins only.
- Kin_Su 171482 / TURTLE1 171479 / Anmol 171514 — quiet/closed.
- enescanguven 171441 / jamie_burt 171438 — quiet.

### Kaspersky / TLS (standing Catty family — reinforce only)
- Laercio_Albuquerque 171644 — Colin: machine healthy; phone works; Windows desktop can’t open secure channel (old 0.29 client). OP resolved: **Kaspersky Premium HTTPS scanning** — trust Grok Bot.exe + “Do not scan encrypted traffic”. New locale (PT-BR) + version note; do **not** re-KEEP.
- OliG 171344 — OP confirms antivirus was the issue (Colin Network Debugger path).

### Webhook URL missing (thomas2018 standing — reinforce only)
- ziemovit on 171324 — macOS 0.51.0 same missing POST URL / crsr_ key. Colin merged 171664 into 171324. Standing skip.

### Ops / dual-copy / recovery (no new portable gate)
- Gideon_H_Guna_e 171091 — kevinn Sep 15 escalate: edge-case box; standard reset tools won’t help; offer alternate account + free usage. Ops day#8.
- Diazb123 170915 — bump “returned Sep 15”; prior backend-restore class (seen).
- nitesh_sharma 170954 — still waiting; SuperGrok unused; prior deanrie don’t-Reset.
- Biniam_N_Mulisa 169940 — Mac attach finally worked after reinstall (self-resolved).
- Charles_Roe 171078 — standing skip.
- Channels_Cintara / CREODOT / Tim auth family — standing.

### Tips / feature / wrong surface / events
- mwjt42 171654 — phone notifs while desktop FR (Colin focus-window nuance).
- Johnsters 171745 — what is Grok Bot? (confused newbie).
- CosVoice 171766 — hosted MCP product pitch.
- Julien_Mayeur 171678 — live-meeting FR (prior).
- Meetup events 171706–171710 — skip.
- Cloud Agents Grok billing 169576 / 171736 — wrong surface (not Grok Bot app killed-claim).

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–2 → `/workspace/field/forum0916/`
- Search: `Grok+Bot+after:2026-09-14`, `after:2026-09-15` saved; keyword+after variants mostly **rate-limited** (`{"failed":"FAILED","message":"You’ve performed this action too many times…"}`) — tag+date search carried load; silent keyword returned thin hits only
- `c/grok-bot/33.json` skipped (invalid category)
- Topics created ≥2026-09-15 00:00 UTC (bugs/friction focus): **171698**, **171703**, **171704**, **171735**, **171740**, **171742**, **171745**, **171747**, **171777**, **171791**, **171796**; plus tips/events; activity on 171676 (staff), 171644 (Kaspersky resolve), 171091, 170915, 170954, 169940, 171324
- Priority topic IDs fetched: 171747, 171740, 171704, 171735, 171698, 171777, 171791, 171796, 171703, 171742, 171745, 171644, 171676, 170915, 171091, 170954, 169940, 171654
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 171735 / 171676 deposit
- bank.py deposited KEEP 1–2; field-seen.json not edited; scratch-seen-urls.txt not edited this turn

## Bank deposits
- KEEP: `raw/ai/2026-09-16-kostadin-s-grok-bot-android-all-bots-fail.md` ← 171735
- KEEP: `raw/ai/2026-09-16-nathan-arizona-grok-bot-slack-routine-trigger-never.md` ← 171676

## Packet recommendation
Keep count: **2** (cap ≤2; education takes other slots). Prefer **Kostadin_S 171735** (desktop OK + generation dead = backend-unreachable computer, not usage — new killed-claim costume distinct from Serene/huanl) + **Nathan_Arizona 171676** (elevated from Tue watch: private Slack channel needs `/invite @Cursor`; Test Run ≠ listener subscription). Overflow: yuan_fang 171747 trial-silent; bibimbap 171704 Serene reinforce; stoplion123 171698 zombie-healthy Reset-helps contrast; Benny_Leng 171740 ops; ziemovit 171791 GitHub trigger watch; Andrew 171777 Reconnecting thin. Bounce reinforce: Laercio Kaspersky 171644 (Catty standing); webhook 171324 ziemovit. **Alert: none** (do not re-alert standing list; both teaches are copyable, not this-week Field path changes). No packet file written. field-seen.json not edited.
