# Field Grok Bot failure hunt · packet 2026-09-17 (Thursday)
Cutoff: after ~2026-09-16 00:00 UTC (post Wednesday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+after:2026-09-15` (+ `after:2026-09-16`). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped / bounce only): Wed KEEP Kostadin_S 171735 (generation-dead + preview-OK = backend-unreachable; don’t Reset); Wed KEEP Nathan_Arizona 171676 (Slack private-channel `/invite @Cursor`; Test Run ≠ listener). Tue KEEP huanl 171563 / Serene_Thornton 171615 (+171626/171588). Standing skip: Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270, jamie_burt 171438, Kin_Su 171482, enescanguven 171441, Catty Kaspersky family, thomas2018 171324 webhook, Channels_Cintara Update-Computer auth, Surfshark Temp, session-revoke, F-Secure DeepGuard, Auto-review bind, SuperGrok Start routines, Desktop-secrets overwrite, workspace-media OOS. Wed overflow elevated below where staff confirmed NEW mechanism.

## KEEP candidates (2)

### KEEP 1 — ziemovit · GitHub “issue assigned” trigger never fires for github.com (not user config) — elevated from Wed overflow
- url: https://forum.cursor.com/t/grok-bot-github-issue-assigned-routine-never-fires-5-attempts-recreated-routine-app-has-repo-access/171791
- date: OP 2026-09-15 21:05 UTC; deanrie 2026-09-16 05:59 UTC
- tags: quiet-when-nothing, coverage-ceiling, human-gate
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·quiet-when-nothing·coverage-ceiling] score=9 | ziemovit | Bot-owned Active routine “When an issue is assigned…” never starts despite assignment events on GitHub, Cursor GitHub App All repos + issues RW, and chat handle on the same issue working. 5 recreate attempts; timings table. deanrie: **setup is correct — known product bug**; GitHub issue-assigned trigger currently **does not fire for github.com repos** no matter how assignee is set; filter is assigner not assignee; by design should fire on create-with-assignee (separate `assigned` event). No user-facing received/non-matching event log. Workaround: scheduled routine + chat (webhook blocked by 171324 for OP). Teach: don’t recreate routine / chase app access / Reset computer when chat works but GitHub assign trigger is silent — it’s a coverage-ceiling on the trigger, not membership (contrast Nathan Slack invite). Elevates Wed overflow after staff confirm. Alert: **no** (known-issue teach; not a this-week Field file/setting change).
- staff: deanrie (known-issue + filter semantics + workaround)
- siblings: Nathan_Arizona 171676 (trigger-silent class — Slack membership, different mechanism); thomas2018 171324 webhook URL missing (standing)
- bank: raw/ai/2026-09-17-ziemovit-grok-bot-github-issue-assigned-routine.md

### KEEP 2 — Mercer_Alex · One bot silent after image_gen; other bots + computer OK; runner stuck — do NOT Reset
- url: https://forum.cursor.com/t/grok-bot-one-bot-silent-after-image-gen-restart-this-bots-runner-only-do-not-reset/171840
- date: OP 2026-09-16 09:25 UTC; deanrie 10:39 UTC; Colin merge → 171858 11:21 UTC
- tags: killed-claim, persistent-computer, quiet-when-nothing
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=9 | Mercer_Alex | One bot dead after image_gen/draw tool; other bots on same Agent Computer still reply; takeover desktop operable; usage open; “Stop now” / hello fail. OP asked restart **this bot’s runner only** — don’t Reset/rebuild/delete. Bot self-recovered with history intact. deanrie: reply processing runs **on our side, not the Agent Computer** — computer looked fine because it was; only this bot’s background step stuck and later messages queued. Chat history server-side. Teach: one-bot silent + siblings OK + computer OK ≠ Reset / ≠ usage (contrast Kostadin all-bots + backend-unreachable, Serene weekly-limit silent, huanl Reconnecting=no-access). Fleet sibling hub: Nads_D_Etc 171858 (Colin investigating / recovery waves Wed). Alert: **no** (copyable don’t-Reset teach; not a Wedge this-week Field path change).
- staff: deanrie (per-bot runner / queue mechanism); Colin (merged into incident hub)
- siblings: Nads_D_Etc 171858 fleet unresponsive hub; weiwei929 / Gokul_Daroji 171864 / Raymond_Weiss 171855 / Ultra_James (same-day partial-fleet silent); Kostadin_S 171735 (all-bots contrast)
- bank: raw/ai/2026-09-17-mercer-alex-grok-bot-one-bot-silent-after.md

## OVERFLOW / watch (not packet KEEP)

### Nads_D_Etc 171858 — Wed fleet “bots unresponsive / failed to send” hub (62 posts)
- https://forum.cursor.com/t/some-of-the-bots-became-unresponsive-failed-to-send-on-my-messages-to-them/171858 — Colin: investigating → recovery → relapse → recovery; statuspage. Many merges (171854, 171855, 171836, 171840, 171857, 171886, 171879, 170915, 171464…). Portable teach carried by Mercer KEEP; hub = evidence density / ops incident. Watch if staff publishes a durable mechanism beyond “investigating.”

### Andrew_van_Niekerk 171777 — Reconnecting = Zscaler/SWG TLS to *.cursorvm.com (elevated from Wed thin)
- https://forum.cursor.com/t/grok-bot-0-51-0-stuck-permanently-on-reconnecting-despite-healthy-local-connectivity/171777 — Colin: computer healthy; chat/api2 OK; **corporate Zscaler egress fails TLS handshake to `<computer>.us8.cursorvm.com`** while non-corporate connects; SWG inspecting/blocking *.cursorvm.com while allowing *.cursor.sh. Score ~8–9 dual-endpoint TLS; overflow (TLS/proxy standing family with Catty/Kaspersky — reinforce, do not re-KEEP Catty).

### doughy 171895 — update_state memory writes fail fleet-wide (“brain docs snapshot was cut short”)
- https://forum.cursor.com/t/grok-bot-update-state-memory-writes-fail-fleet-wide-brain-docs-snapshot-was-cut-short-before-completing/171895 — deanrie: known issue; settings update_state + direct file writes work; workaround write memory/*.md; don’t Reset. Score ~7–8 coverage-ceiling / tip; overflow (product bug, not killed-claim costume).

### yuan_fang 171747 — Trial usage allowance silent (Wed overflow — no new mechanism)
- Reinforces Serene quiet-when-nothing trial flavor; no new staff Wed→Thu. Bounce/overflow only.

### Liyo_K 171796 — DNS can’t resolve cursorvm; flushdns + 1.1.1.1 fixed
- deanrie: Recover/Reset completed server-side; Windows DNS to cursorvm.com fails; stop Reset. OP confirmed flushdns worked. Kin_Su DNS cousin — bounce reinforce.

### Max_Maldonado 171808 — Windows-only Reset-failed; Ubuntu+phone OK → Kaspersky HTTPS scanning
- deanrie: computer up; Windows app not sending (MITM). Catty Kaspersky standing — reinforce only.

### Musvik_ASADZADE 171807 — Onboarding provision retry-exhausted (ops)
- deanrie recreating cloud computer; Colin backend fiddle + restart. Ops/provision; no portable gate yet.

### Benny_Leng 171740 — Partial-state Reset stuck 50% (Wed ops — resolved)
- Colin Sep 16: Reset went through; computer connected; bots/files preserved. Bounce resolved.

### stoplion123 171698 / bibimbap 171704 — no new staff; contrast/reinforce only
- stoplion zombie-healthy Reset-helps contrast to Kostadin; bibimbap Serene weekly sibling.

### LiuChunYin 171877 — Custom MCP OAuth redirect_uri / CF Access headers
- Product/MCP auth FR; not killed-claim. Tip/overflow.

### g0uv4 171839 — Ctrl+, Settings vs Traditional Chinese full-width comma IME
- Colin confirmed shortcut/IME collision. UX tip, not failure KEEP.

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- Kostadin_S 171735 / Nathan_Arizona 171676 — Wed KEEP; bounce only.
- huanl 171563 / Serene 171615 (+siblings) — yuan_fang trial cousin only.
- Kin_Su 171482 — Liyo_K 171796 DNS reinforce.
- Catty Kaspersky — Max_Maldonado 171808 + Andrew Zscaler cousin (TLS family).
- thomas2018 171324 webhook — OP notes + Tom5 outbound workaround chatter; standing; ziemovit workaround blocked by it.

### Ops / merges / dual-copy / recovery
- Gokul_Daroji 171864 — deanrie: Wed 15:00–17:00 IST backend queue (same incident as 171858) + DNS advice; not new gate.
- Diazb123 170915 / nitesh_sharma 170954 — merged/bumped into unresponsive hub class.
- Linus_Boss 171802 — topic deleted by author.
- Alan_Lai 171886 / Adam7 171836 / weiwei929 171857 / Julio_Fort 171854 — merged into 171858.

### Tips / feature / wrong surface
- traeyee 171742 quota tip (prior); CosVoice 171766 MCP pitch; Johnsters 171745 newbie; mwjt42 171654 notifs FR; 171540 context-window tip; 169904 shared team FR; Meetup events skip; Cloud Agents IDE unresponsive 171912 (staff: separate from Grok Bot).

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–1 → `/workspace/field/forum0917/`
- Search: `Grok+Bot+after:2026-09-16` and `after:2026-09-15` succeeded (41/50 topics); no rate-limit this turn
- `c/grok-bot/33.json` skipped (invalid category)
- In-window created ≥2026-09-16 00:00 UTC (bugs/friction focus): **171802**, **171807**, **171808**, **171819**, **171836**, **171839**, **171840**, **171854**, **171855**, **171857**, **171858**, **171864**, **171877**, **171879**, **171886**, **171895**; plus activity on overflow 171791 (staff), 171777 (staff), 171796 (staff+resolve), 171740 (resolved), 171747 (quiet), 171324
- Priority topic IDs fetched: 171858 (+ remaining posts via post_ids), 171895, 171877, 171807, 171864, 171808, 171802, 171819, 171855, 171840, 171791, 171777, 171740, 171747, 171796, 171839, 171698, 171704, 171324
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 171791 / 171840 deposit
- bank.py deposited KEEP 1–2; field-seen.json not edited; latest.md / field-packet-*.md not touched

## Bank deposits
- KEEP: `raw/ai/2026-09-17-ziemovit-grok-bot-github-issue-assigned-routine.md` ← 171791
- KEEP: `raw/ai/2026-09-17-mercer-alex-grok-bot-one-bot-silent-after.md` ← 171840

## Packet recommendation
Keep count: **2** (cap ≤2; education takes other slots). Prefer **ziemovit 171791** (elevated Wed watch: GitHub issue-assigned trigger dead for github.com — not config) + **Mercer_Alex 171840** (one-bot runner stuck after tool; computer + siblings OK; don’t Reset — distinct from Kostadin all-bots backend-unreachable). Overflow: Nads_D_Etc 171858 fleet hub; Andrew 171777 Zscaler cursorvm TLS; doughy 171895 memory update_state; yuan_fang 171747 trial-silent; Liyo_K DNS / Max Kaspersky bounce. **Alert: none** (do not re-alert standing list; both teaches are copyable, not this-week Field path changes). No packet file written. field-seen.json not edited.

## PACKET READY
- [agentic·quiet-when-nothing·coverage-ceiling] score=9 | ziemovit | GitHub “issue assigned” routine never fires for github.com — setup correct, known trigger bug; don’t recreate/Reset; scheduled+chat workaround (webhook blocked by 171324)
- [agentic·killed-claim·persistent-computer] score=9 | Mercer_Alex | One bot silent after image_gen; siblings + computer OK; per-bot runner/queue on backend — don’t Reset (fleet hub 171858)
