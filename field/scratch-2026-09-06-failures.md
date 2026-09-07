# Field Grok Bot failure hunt · packet 2026-09-06 (Sunday)
Cutoff: after ~2026-09-05 00:00 UTC (post packet-23 / 2026-09-05 keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+order:latest`. Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, + URLs in scratch-2026-09-06-seen-urls.txt (incl. 170235).

## KEEP candidates (5)

### KEEP 1 — Jarri81 · Surfshark AV scans temp ps-script → 11s > 10s wait → false “temporarily unreachable”
- url: https://forum.cursor.com/t/grok-bot-0-43-windows-local-pc-shows-connected-but-commands-fail-with-temporarily-unreachable/170683
- date: 2026-09-05 09:28 UTC (16:28 ICT 5 Sep)
- tags: killed-claim
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·killed-claim] score=9 | Jarri81 | Windows Grok Bot 0.43. Computers list shows connected; Local execution Always allow; every Shell fails “temporarily unreachable” (sometimes then disconnected). Daemon up but loops ownership-lost / DeadlineExceeded. Staff deanrie: PC *is* connected; **response arrives ~11s, agent stops waiting at 10s** — command actually ran. OP A/B: Surfshark VPN alone OK (~1.3s); web protection alone OK (~3s); **Surfshark Antivirus real-time on** → miss timeout. Root: each local-exec writes `ps-script-<uuid>.ps1` under `%TEMP%`; AV inspects create/execute and adds ~11s. Exclude install folder alone insufficient; exclude `%TEMP%` works (broad trade-off). Asks dedicated `%APPDATA%\\Grok Bot\\tmp` or timeout >~11s. Killed: don’t label local-exec “temporarily unreachable” when the PC answered late; write scripts outside scanned Temp (or wait past typical AV). Distinct from digvijaysai DNS (real reachability) and aaron_72 daemon flap — here **connected + Always-allow + false unreachable = AV latency vs hard 10s**. Alert: no.
- staff: deanrie 2026-09-05 09:56 + 16:38 UTC — timeout diagnosis; Surfshark signal useful.
- bank: raw/ai/2026-09-06-jarri81-grok-bot-0-43-windows-local.md

### KEEP 2 — Winvicta · CodexSandboxUsers ACL without AppContainer RX → silent Windows launch crash (int3 / 0x80000003)
- url: https://forum.cursor.com/t/grok-bot-0-28-0-and-0-43-0-windows-instant-launch-crash-int3-in-v8-jit-grok-bot-786cdd6/170691
- date: 2026-09-05 10:37 UTC (17:37 ICT 5 Sep)
- tags: killed-claim, persistent-computer
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=9 | Winvicta | Windows Grok Bot 0.28.0 + 0.43.0 crash ~1s after launch (no UI). WinDbg: int3 in V8 JIT at `Grok_Bot+786cdd6`; GPU helper STATUS_BREAKPOINT. Ruled out GPU flag, Armoury Crate, clean reinstall. Staff deanrie: `--disable-gpu-sandbox` keeps window (blank); icacls shows **package SID + CodexSandboxUsers inherited, missing S-1-15-2-1 / S-1-15-2-2 (ALL APPLICATION / ALL RESTRICTED APPLICATION PACKAGES)** — Electron/Chromium sandbox child crash shape (upstream Electron, not Grok-specific). Accepted fix: icacls grant *S-1-15-2-2:(OI)(CI)(RX) /T (+ S-1-15-2-1) on `%LOCALAPPDATA%\\Programs\\Grok Bot`; OP confirmed clean start + sign-in. Option B: remove CodexSandboxUsers / orphan package SID + reset inheritance. Killed: after Codex/other AppContainer tools leave package SIDs on the Grok Bot install tree, grant AppContainer RX (or clean orphaned sandbox ACLs) before Reset/reinstall thrash. Distinct from Chip_Randa first-setup service outage — here **install ACL, not cloud box**. Alert: no.
- staff: deanrie 2026-09-05 11:46 + 16:01 UTC — accepted ACL diagnosis; OP fixed 16:42.
- bank: raw/ai/2026-09-06-winvicta-grok-bot-0-28-0-and.md

### KEEP 3 — Benjamin_Barber · graphrag embedding RAM OOM bricks VM; Reset “won’t work” was slow + re-click restarts timer
- url: https://forum.cursor.com/t/grokbot-bricked-wont-reset/170689
- date: 2026-09-05 10:17 UTC (17:17 ICT 5 Sep)
- tags: coverage-ceiling, killed-claim
- score: 8 (portable 4 / evidence 5)
- packet one-liner: [agentic·coverage-ceiling·killed-claim] score=8 | Benjamin_Barber | Linux Grok Bot 0.30→0.43. HuggingFace dataset graphrag indexing “bricked” the box; Reset seemed dead. Staff deanrie: **not disk — memory**. Embedding job hits VM RAM limit → job + system services crash → looks bricked; auto-resume on fresh computer re-OOMs in minutes. Reset *did* work but took **~1 hour**; **re-clicking Reset while in-flight restarts the timer**. ~12 GB data restored each time; apt/pip outside workspace needs reinstall. Stabilize: stop auto-resume indexing; `free -h` before heavy; smaller batches / fewer workers / smaller embed model. Killed: heavy embedding stays under RAM; Reset once and wait up to an hour (don’t hammer); no silent auto-resume after OOM. Distinct from digvijaysai (DNS + webhook burn) and im_grok (Reset partial UI) — here **RAM OOM wears a “won’t reset / bricked” costume**. Alert: no (Field education bots unlikely to run graphrag this week).
- staff: deanrie 2026-09-05 11:25 UTC — memory not disk; Reset slow; batch guidance.
- bank: raw/ai/2026-09-06-benjamin-barber-grokbot-bricked-wont-reset.md

### KEEP 4 — StefanZ (+ bearbones24) · secretRequest.target missing → one Bot freezes desktop chat; iPhone OK
- url: https://forum.cursor.com/t/grok-bot-macos-one-agent-larry-failed-to-send-missing-replies-iphone-ok-other-agents-ok-on-mac/170710
- date: 2026-09-05 16:18 UTC (23:18 ICT 5 Sep); bearbones24 23:53 UTC
- tags: mobile-unblock, killed-claim
- score: 8 (portable 4 / evidence 4)
- packet one-liner: [agentic·mobile-unblock·killed-claim] score=8 | StefanZ | macOS (+ Linux Omarchy): bot **Larry** Failed to send / missing replies; **Heinz OK on same desktop**; **iPhone has full Larry thread**. Reinstall/sign-out no-ops. bearbones24 (Linux 0.43.0 Mint): same one-Bot freeze after that Bot posts a **secret-request widget**; copy Bot copies freeze. Log: SandGatewayMalformedReplyError — gateway listAgents reply malformed because secretRequest.target is a required field the gateway omits → conversation never hydrates; mobile parser fine. Cluster same day: Bradley_Street 170721 (main pane empty, left preview+iOS OK; 2 Macs), John_Millard 170723 (Walter could not load conversation; sidebar+mobile OK; Bradley: do not Reset), David_St 170720 (deleted), Bean on 170702 (desktop stale / Failed to send, iOS current). Killed: desktop must parse secretRequest without required target (or gateway always sends it) so one secret-widget Bot does not freeze only that thread; mobile-unblock until then. Distinct from George_Burchell empty roster / jian_ma no gateway-descriptor (whole desktop attach) — here **per-Bot desktop hydrate after secretRequest**. Alert: no (use iPhone for the stuck Bot).
- staff: none yet (strong peer forensics + multi-thread cluster).
- siblings: 170721 · 170723 · 170720 · Bean@170702
- bank: raw/ai/2026-09-06-stefanz-grok-bot-macos-one-agent-larry.md

### KEEP 5 — jsolly · Shell Auto-review bind failure — escalate retry + Allow rule never surface approval card
- url: https://forum.cursor.com/t/grok-bot-shell-auto-review-executable-content-could-not-be-bound-never-shows-approval-card/170727
- date: 2026-09-05 22:36 UTC (05:36 ICT 6 Sep)
- tags: human-gate, killed-claim
- score: 7 (portable 4 / evidence 3)
- packet one-liner: [agentic·human-gate·killed-claim] score=7 | jsolly | iOS 1.6.0 + shared Linux box. Shell Auto-review returns a **bind failure** (could not bind review / run resolved script or give working_directory) on package-manager path commands under GeoRoids (working_directory set). **Escalation retry with the smart-mode approval flag + exact reject string → same reject; no user-visible Auto-review card** (OP has never seen one). iOS New Rule Allow Automatically for package installs under GeoRoids did not prevent or escalate. Plain listing / python / node -v OK; package-manager path blocked. Implication: bind failure happens **before/outside** the human allow decision. Workaround: invoke the package CLI through node rather than the bin shim. Killed: bind rejects must either run, or raise the approval card (and honor Allow rules) — silent bind must not be a dead end. Distinct from prior jsolly Always-allow Linux local-exec (170255 / Chen path) — here **box Shell Auto-review human-gate is unreachable**. Alert: no (workaround exists; no staff yet).
- staff: none yet.
- bank: raw/ai/2026-09-06-jsolly-grok-bot-shell-auto-review-executable.md

## BOUNCE

### Named / adjacent (not kept this pass)
- oscar_mei 170661 Bot failed to respond + Reset partial — deanrie: backend stuck, don't Reset/Update/reinstall/logout; manual recovery — **im_grok 170373 mechanism already kept** https://forum.cursor.com/t/grok-bot-0-43-0-bot-failed-to-respond-reset-agent-computer-stuck-in-partial-state/170661
- Ah_Ah 170731 Android Bot failed to respond + cannot create bot; box desktop still opens; no Recover/Reset on Android 1.5.0 — ops / 170235 cluster duplicate https://forum.cursor.com/t/grok-bot-android-bot-failed-to-respond-cannot-create-bot/170731
- Nimish_Goel 170694 can't-reach all devices + empty roster after re-login; setup fails on phone — **George_Burchell / andyfraussen adjacent**, no staff https://forum.cursor.com/t/paid-user-cant-reach-grok-bots-computer-on-all-devices-bots-missing-after-re-login/170694
- jian_ma 170702 Mac 0.43 can't attach / no gateway descriptor; iOS OK — **George_Burchell reattach**, Bean reply is chat-pane cluster sibling of StefanZ https://forum.cursor.com/t/grok-bot-0430-mac-desktop-session-broken-ios-works/170702
- Bradley_Street 170721 / John_Millard 170723 / David_St 170720 — desktop chat-pane / couldn't-load cluster; kept via StefanZ+bearbones forensics https://forum.cursor.com/t/grok-bot-mac-replies-missing-in-main-chat-pane-visible-in-left-preview-ios/170721 · https://forum.cursor.com/t/windows-grok-bot-desktop-can-t-load-an-existing-walter-conversation-sidebar-and-mobile-still-work/170723
- Martin_Holmes 170722 recurring unreachable after backend repairs (T-F35990) — ops/ticket, no new kill https://forum.cursor.com/t/grok-bot-computer-unreachable-again-recurring-backend-failure-after-multiple-repairs/170722
- Ricard1 170719 desktop+mobile reconnect; one Reset → hibernated; T-F50709 — support/ops https://forum.cursor.com/t/grok-bot-cannot-connect-on-desktop-or-mobile-reset-outcome-unknown-t-f50709/170719
- jsolly 170725 Inkbox iOS connect card Unsupported redirect_uri (desktop OAuth later OK) — connector/OAuth, not killed roster practice https://forum.cursor.com/t/grok-bot-inkbox-connect-card-fails-with-unsupported-redirect-uri/170725
- 170235 Tamas_King Bot failed to respond — already seen; Ah_Ah bumped 2026-09-05 — bounce

### FR / UX / off-hunt
- 170729 iOS About version copy · 170728 iOS sidebar Move Down snap · 170714 export memory · 170664 SuperGrok vs Heavy · 168333 prune context (bump)

### Already-kept (window)
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Priority topic IDs 170727/683/691/689/710/721/723/702/731/661/694 all 200 via forum topic JSON
- Tag latest: tag/grok-bot/l/latest.json (+ page=1); page 0 caught extras 170722/720/719/725/729/728
- search.json Grok Bot order:latest → 50 topics (aligned with tag p0)
- Saved under /workspace/field/forum0906/
- Public cooked HTML stripped (raw often omitted); no login
- X / Firecrawl / Slack not used

## Bank deposits
- KEEP: `raw/ai/2026-09-06-jarri81-grok-bot-0-43-windows-local.md` ← 170683
- KEEP: `raw/ai/2026-09-06-winvicta-grok-bot-0-28-0-and.md` ← 170691
- KEEP: `raw/ai/2026-09-06-benjamin-barber-grokbot-bricked-wont-reset.md` ← 170689
- KEEP: `raw/ai/2026-09-06-stefanz-grok-bot-macos-one-agent-larry.md` ← 170710
- KEEP: `raw/ai/2026-09-06-jsolly-grok-bot-shell-auto-review-executable.md` ← 170727

## Packet recommendation
Keep count: **5** — Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710 (+ cluster), jsolly 170727. **Alert: none** (no this-week roster/setting change for Wedge). No packet file written. field-seen.json not edited.
