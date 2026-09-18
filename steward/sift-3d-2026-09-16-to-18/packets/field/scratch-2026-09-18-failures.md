# Field Grok Bot failure hunt · packet 2026-09-18 (Friday)
Cutoff: after ~2026-09-17 00:00 UTC (post Thursday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+after:2026-09-16` (+ `after:2026-09-17`). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped / bounce only): Thu KEEP ziemovit 171791 (GitHub issue-assigned never fires github.com); Thu KEEP Mercer_Alex 171840 (one-bot silent after image_gen = per-bot runner). Wed KEEP Kostadin_S 171735; Wed KEEP Nathan_Arizona 171676. Standing skip: huanl 171563, Serene_Thornton 171615 (+171626/171588), Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270, jamie_burt 171438, Kin_Su 171482, enescanguven 171441, Catty Kaspersky family, thomas2018 171324 webhook, Channels_Cintara Update-Computer auth, Surfshark Temp, session-revoke, F-Secure DeepGuard, Auto-review bind, SuperGrok Start routines, Desktop-secrets overwrite, workspace-media OOS. Thu overflow re-checked below — no elevation (no NEW durable staff mechanism beyond ops “back in action”).

## KEEP candidates (2)

### KEEP 1 — Dave_Campos · iOS “unexpected error” = chat-pattern render bug; computer fine — don’t Update/Reset
- url: https://forum.cursor.com/t/grok-bot-hit-an-unexpected-error/172070
- date: OP 2026-09-17 19:19 UTC; kevinn 2026-09-17 20:46 UTC
- tags: killed-claim, quiet-when-nothing, persistent-computer
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=9 | Dave_Campos | iOS Grok Bot 1.10.0 shows “Grok Bot hit an unexpected error / Try again” on COS chat for ~20h; Update Bot computer did nothing; another staff agent can still reach COS. kevinn: **iOS App Store build fails to draw chats with a particular message pattern** — not the Agent Computer (still running/finishing work). Fix in next iOS release (in testing). Workaround: desktop Mac/Windows opens the chat; keep relaying via other agent. Teach: iOS unexpected-error + siblings/desktop OK ≠ Reset / ≠ Update / ≠ recreate computer (contrast Mercer per-bot runner, Kostadin all-bots backend-unreachable, Serene usage-silent). Alert: **no** (copyable don’t-Reset teach; not a this-week Field file/setting change).
- staff: kevinn (iOS render-pattern mechanism + desktop workaround + upcoming App Store fix)
- siblings: Mercer_Alex 171840 (one-bot runner — different surface); Serene / Aerospace 172073 (usage silence — different); Elizabeth_Rotman 171952 (trial-usage frozen-sending costume)
- bank: raw/ai/2026-09-18-dave-campos-grok-bot-hit-an-unexpected-error.md

### KEEP 2 — allninety · Account stuck “Unknown” multi-device since 11 Sep; status Operational ≠ this account — don’t Reset
- url: https://forum.cursor.com/t/t-f86577-cannot-connect-on-windows-macos-and-iphone-since-11-sep/171962
- date: OP 2026-09-17 06:03 UTC; mohitjain 2026-09-17 07:19 UTC
- tags: killed-claim, coverage-ceiling, persistent-computer
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·coverage-ceiling] score=9 | allninety | All Grok Bots unreachable on Windows + macOS + iPhone since 11 Sep (ticket T-F86577); Retry/Reset/Hard Reset fail; Bot Computer page “Unknown.” Support previously said backend-only / escalated. mohitjain: **on our side, not devices/network/sign-in**; Sep 16 fleet incident that resolved is **separate** — statuspage Operational won’t match this account’s stuck state; each Reset/Recover/Update starts another rebuild and **slows cleanup**; bots/files/logins stored separately and safe. Teach: multi-device total silence + Unknown computer + public Operational = account-stuck recovery queue, not DNS (Kin_Su/Liyo_K), not Zscaler TLS (Andrew 171777), not usage-silent (Serene), not per-bot runner (Mercer). Don’t Reset. Alert: **no** (don’t-Reset teach; ops recovery, not Field path change this week).
- staff: mohitjain (account-specific stuck vs fleet incident; hold Reset; recovery handoff)
- siblings: Kostadin_S 171735 (all-bots + preview-OK contrast); Liyo_K 171796 / Palan 171969 (DNS cursorvm — local fix); Nads_D_Etc 171858 (fleet ops hub — separate)
- bank: raw/ai/2026-09-18-allninety-t-f86577-cannot-connect-on-windows.md

## OVERFLOW / watch (not packet KEEP)

### Nads_D_Etc 171858 — fleet unresponsive hub (153 posts) — no NEW durable mechanism
- https://forum.cursor.com/t/some-of-the-bots-became-unresponsive-failed-to-send-on-my-messages-to-them/171858 — Colin Sep 17: investigating → identified → “back in action” (~15:16 UTC). Merges: 172005, 172006, 172007, 172000, 171983, 172014, 172017, 172022, 172023, 172025, 172031, …. Portable teach still carried by Thu Mercer KEEP (per-bot runner / don’t Reset). **Do not elevate** — no new mechanism beyond ops recovery waves.

### Adam_Purslow 172001 — one-bot Failed to send; others OK; stuck turn queues — Mercer reinforce
- https://forum.cursor.com/t/grok-bot-one-bot-tlc-outbounds-failed-to-send-others-ok-please-restart-runner-only/172001 — deanrie: computer fine; one turn stuck ~1:43 PM Dubai; later messages queued; usually clears in a couple hours; don’t Reset. Reinforces Mercer 171840 — bounce only.

### Aerospace 172073 / Elizabeth_Rotman 171952 — weekly/trial usage silent (thinking dots / frozen sending)
- 172073 kevinn: weekly included usage hit; app supposed to show notice and does not (known); don’t logout/Reset/Update. 171952 deanrie: trial usage exhausted; looks stuck sending. Serene quiet-when-nothing reinforce — bounce/overflow.

### Mariusz_Wojcik 172020 — almost all bots disappeared; staff restored Sep 15 snapshot
- https://forum.cursor.com/t/almost-all-of-my-bots-disappeared/172020 — kevinn restored roster from morning-of-Sep-15 copy; quit apps fully; post-snapshot work not in copy. Ops restore / data-cliff; score ~7–8; overflow (not durable gate beyond “wait for staff restore”).

### Sanghoon_Kang 172009 — parent bot quiet while delegated Cloud Agents run (by design)
- Colin: parent only wakes when delegated agent finishes; watch cursor.com/agents or attach agent card. quiet-when-nothing observability tip ~7–8 — overflow FR/behavior, not killed-claim KEEP.

### Wes_Anderson 172032 — Sep 17 service degradation; messages accepted, turn never ran; “Failed to send” misleading
- kevinn: status.cursor.com degradation (resolved); not AwaitShell hang / not recreate wiring. Ops incident — bounce.

### Andrew_van_Niekerk 171777 / doughy 171895 / yuan_fang 171747 / Liyo_K 171796 / Max_Maldonado 171808 — Thu overflow, no new staff
- No elevation. Andrew Zscaler TLS / doughy update_state / yuan trial / Liyo DNS / Max Kaspersky — reinforce standing only.

### Palan 171969 — Reset/Recover failed = DNS cursorvm (Kin_Su cousin)
- mohitjain: computer healthy; set 1.1.1.1/8.8.8.8 + flushdns; phone hotspot confirm. Bounce DNS family.

### Francesco_Beomonte_Z 172074 — all-bots silent; kevinn server-side reset + Landon usage
- Ops + usage cousin — bounce.

### jsolly 172015 — mobile Settings scroll flips toggles (Auto-review)
- kevinn reproduced iOS; tracking. UX/safety tip, not failure KEEP.

### Kamil_Senk 172003 — corporate reconnecting; no staff yet
- Thin; Andrew Zscaler cousin watch.

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- ziemovit 171791 / Mercer_Alex 171840 — Thu KEEP; Adam 172001 + 6tizer 172005 / Kevin4 172031 Mercer siblings merged/reinforce.
- Kostadin_S 171735 / Nathan_Arizona 171676 — Wed KEEP; bounce only.
- Serene 171615 — Aerospace 172073 + Elizabeth 171952 + yuan_fang trial cousins.
- Kin_Su 171482 — Palan 171969 / Liyo_K DNS reinforce.
- Catty Kaspersky / Andrew Zscaler — Max / Kamil corporate cousins.
- thomas2018 171324 webhook — standing; activity bump only.
- Wes_Anderson standing 171029 ≠ today’s 172032 ops post (different topic).

### Ops / merges / dual-copy / recovery
- Mass merge into 171858: 172005, 172006, 172007, 172000, 171983, 172014, 172017, 172022, 172023, 172025, 172031, ….
- 172048 status notice merged into Cloud Agents 172046 (IDE cloud agents — separate surface from Grok Bot KEEP).
- 172074 / 172020 — staff ops reset/restore.

### Tips / feature / wrong surface / meetups
- jsolly 172013 banner dismiss / 171936 usage reset datetime / 171950 UI rename / 171982 Dock badge / 172033 sidebar sections FR / 172071 redact secrets FR / 171974 credits toggle (merged 169679) / 171948 Bitwarden / 172038 TeX1 IDE custom subagent (not Grok Bot) / Meetup events 170762+ skip.

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–1 → `/workspace/field/forum0918/`
- Search: `Grok+Bot+after:2026-09-16` and `after:2026-09-17` succeeded (50 topics each; overlapping); no rate-limit this turn
- `c/grok-bot/33.json` skipped (invalid category)
- In-window created ≥2026-09-17 00:00 UTC (bugs/friction focus): **171936**, **171948**, **171950**, **171952**, **171962**, **171969**, **171974**, **171982**, **171983**, **172000**, **172001**, **172003**, **172005**, **172006**, **172007**, **172009**, **172013**, **172014**, **172015**, **172017**, **172020**, **172022**, **172023**, **172025**, **172031**, **172032**, **172033**, **172038**, **172046**, **172048**, **172070**, **172071**, **172073**, **172074**; plus activity on overflow 171858 (Colin recovery), 171895/171877/171324 bumps
- Priority topic IDs fetched: 172070, 171962, 172020, 172073, 172001, 172005, 172032, 172009, 172074, 171858 (+stream post_ids), 171895, 171777, 171808, 171796, 171747, 171952, 171969, 172003, 172015, 172038, 172023, 172025, 172006, 172007, 172000, 171983, 172014, 172017, 172022, 172048, 172046
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 172070 / 171962 deposit
- bank.py deposited KEEP 1–2; field-seen.json not edited; latest.md / field-packet-*.md not touched
- Appended 46 new topic ids to `/workspace/field/seen-forum-ids.txt` (total 330)

## Bank deposits
- KEEP: `raw/ai/2026-09-18-dave-campos-grok-bot-hit-an-unexpected-error.md` ← 172070
- KEEP: `raw/ai/2026-09-18-allninety-t-f86577-cannot-connect-on-windows.md` ← 171962

## Packet recommendation
Keep count: **2** (cap ≤2). Prefer **Dave_Campos 172070** (iOS chat-pattern “unexpected error” ≠ computer — don’t Update/Reset; desktop/sibling workaround) + **allninety 171962** (account-stuck Unknown multi-device since 11 Sep; status Operational ≠ this account; don’t Reset — distinct from DNS/TLS/usage/runner). Overflow: 171858 fleet hub (no elevate); Adam 172001 Mercer reinforce; Aerospace/Elizabeth usage-silent; Mariusz roster restore; Sanghoon parent-idle-after-delegate; Wes 172032 Sep17 degradation. **Alert: none** (both don’t-Reset teaches; not this-week Field path changes). No packet file written. field-seen.json not edited.

## PACKET READY
- [agentic·killed-claim·persistent-computer] score=9 | Dave_Campos | iOS “unexpected error” = chat-pattern render bug; computer fine; don’t Update/Reset; use desktop / sibling relay
- [agentic·killed-claim·coverage-ceiling] score=9 | allninety | Account stuck Unknown since 11 Sep on all devices; status Operational ≠ account; don’t Reset (T-F86577)
