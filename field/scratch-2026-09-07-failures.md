# Field Grok Bot failure hunt · packet 2026-09-07 (Monday)
Cutoff: after ~2026-09-06 00:00 UTC (post packet-24 / 2026-09-06 keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–2 + `search.json?q=Grok+Bot+order:latest`. Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710, jsolly 170727, andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, + URLs in scratch-2026-09-07-seen-urls.txt + yesterday bounce list in scratch-2026-09-06-failures.md.

## KEEP candidates (3)

### KEEP 1 — Jojo1 · Auto-review bind: compiled binary / `-c` read fails → reject before approval card
- url: https://forum.cursor.com/t/grok-bot-auto-review-blocks-local-commands-executable-content-could-not-be-bound-to-this-review/170809
- date: 2026-09-06 15:39 UTC (22:39 ICT 6 Sep)
- tags: human-gate, killed-claim
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·human-gate·killed-claim] score=10 | Jojo1 | ChromeOS Linux/Penguin local-exec: even `/usr/bin/python3 -c "print('exec-ok')"` fails Auto-review with **executable content could not be bound to this review** after Allow once; same command works in a normal terminal. Staff deanrie root cause: before run, Auto-review **reads the program** to show what will happen; that read fails on **compiled binaries** (`/usr/bin/python3`) and when first arg is a flag like **`-c`** → reject **before** the approval card. Allow once / escalate retry useless. Workarounds that work: `echo "print('exec-ok')" | python3` (pipe); staff also listed `python3 exec_ok.py` with bare interpreter name — OP confirmed pipe works end-to-end for a real helper; **`python3 script.py` with explicit working_directory still bound-failed** for that helper. Avoid: full paths (`/usr/bin/python3`, `/bin/echo`), `python3 -c`, `bash -c`, heredoc-to-python, `~/` inside paths passed to interpreters. Sibling cluster: jsolly 170727 (kept yesterday, no staff yet) + Effective_Autism 170819 (0.44.0 macOS, escalate+card never surfaces). Killed: Shell human-gate is unreachable for absolute-binary / `-c` shapes; prefer pipe or bare-name script. Distinct from jsolly package-manager shim path — here **staff-named mechanism**. Alert: **yes** — change Field/agent Shell hygiene this week (pipe / bare interpreter; no `/usr/bin/python3 -c`).
- staff: deanrie 2026-09-06 16:31 UTC — known issue; binary/`-c` read; pipe + bare-name workarounds.
- siblings: jsolly 170727 · Effective_Autism 170819
- bank: raw/ai/2026-09-07-jojo1-deanrie-grok-bot-auto-review-blocks-local.md

### KEEP 2 — TheAviv · computerUse GTK Open sits on dock → click no-ops (human Open also broken)
- url: https://forum.cursor.com/t/grok-bot-computeruse-gtk-file-chooser-open-no-ops-for-local-video-upload/170816
- date: 2026-09-06 17:01 UTC (00:01 ICT 7 Sep)
- tags: coverage-ceiling, killed-claim
- score: 8 (portable 4 / evidence 5)
- packet one-liner: [agentic·coverage-ceiling·killed-claim] score=8 | TheAviv | Box desktop computerUse: attaching local ~136MB MP4 via native GTK “Open Files” — selection works, **Open often no-ops** (dialog stays; page never gets file); drag-drop also failed. Staff deanrie: Bot desktop has **fixed screen + bottom dock**; Open/Cancel land **on the dock**, so click hits dock not button. Same file uploads when dialog happens higher. Workarounds: skip dialog — browser DevTools `DOM.setFileInputFiles` on the page input; or drag/maximize dialog so Open is above dock. OP follow-up: **human takeover also cannot click Open** — dialog geometry broken for humans too, not only computerUse/Auto-review. Killed: never depend on GTK Open for box uploads; set file input via DevTools or reposition dialog. Distinct from prior computerUse friction — here **staff-confirmed dock occlusion + human repro**. Alert: no (workaround exists; education bots rarely need native Open this week).
- staff: deanrie 2026-09-06 17:23 UTC — dock occlusion; DevTools bypass.
- bank: raw/ai/2026-09-07-theaviv-deanrie-grok-bot-computeruse-gtk-file-chooser.md

### KEEP 3 — noname · secretRequest.target missing → malformed listAgents → whole app stuck “Reconnecting”
- url: https://forum.cursor.com/t/grok-bot-stuck-on-reconnecting-to-your-computer-fully-unusable-malformed-listagents-gateway-response/170736
- date: 2026-09-06 00:36 UTC (07:36 ICT 6 Sep)
- tags: killed-claim, mobile-unblock, gateway-descriptor
- score: 8 (portable 4 / evidence 4)
- packet one-liner: [agentic·killed-claim·mobile-unblock] score=8 | noname | Ubuntu 24.04 Grok Bot 0.43.0: after ~30 min normal use, permanently stuck **Reconnecting to your computer** — Retry/sign-out/Recover/delete local `gateway-descriptor.json` no-ops. Daemon starts; logs `SandGatewayMalformedReplyError: gateway listAgents reply is malformed` because **`secretRequest.target` required field missing**. Reproduced on two accounts after upgrade; fresh account OK until upgrade. Network/VPN/proxy ruled out. Same schema hole as StefanZ 170710 (per-Bot desktop freeze after secret widget) but **bricks entire roster hydrate / reconnect**, not one thread. Same-day staff on siblings Casti_Cimpian 170750 / yifan_Hong 170745: secret/credential card → desktop can’t load that chat (iPhone OK); fix rolling out automatically — don’t Reset/Update. Bean@170702: duplicate bot healthy until **SECRET INPUT UI** save → immediate Failed-to-send on macOS only. Killed: leave no hanging secretRequest without target; use iPhone until backend hydrate fix; don’t thrash Reset/gateway-descriptor delete. Distinct from George_Burchell whole-desktop attach wipe — here **malformed listAgents from secretRequest schema**. Alert: no (mobile-unblock; wait for rollout).
- staff: none on this thread; staff on cluster 170750/170745 (deanrie: secret card → desktop load; auto fix ≤24h).
- siblings: StefanZ 170710 · Casti_Cimpian 170750 · yifan_Hong 170745 · Bean@170702 · Bradley_Street 170721 · John_Millard 170723
- bank: raw/ai/2026-09-07-noname-grok-bot-stuck-on-reconnecting-malformed.md

## BOUNCE

### Named / adjacent (not kept this pass)
- Effective_Autism 170819 Auto-review bind on 0.44.0 macOS + escalate never shows card — **Jojo1 170809 mechanism** (staff root cause kept there); also posted on jsolly 170727 https://forum.cursor.com/t/grok-bot-0-44-0-on-macos-shell-executable-binding-rejection-persists-approval-card-never-appears/170819
- Casti_Cimpian 170750 / yifan_Hong 170745 — secret-card desktop “Couldn’t load” / replies missing in main pane; **staff confirms StefanZ cluster**; don’t Reset; auto fix ≤24h https://forum.cursor.com/t/cannot-load-chat-history-for-some-grok-bots/170750 · https://forum.cursor.com/t/grok-bot-windows-one-chat-can-send-but-replies-never-render-in-main-pane-sidebar-preview-ok-mobile-ok/170745
- Bean@170702 MAJOR repro: duplicate Cecil v2 healthy until webhook **SECRET INPUT** save → same desktop freeze — StefanZ forensics strengthen, not new kill https://forum.cursor.com/t/grok-bot-0430-mac-desktop-session-broken-ios-works/170702
- grokpanda 170775 can’t-reach + Update/Recover/Reset fail after password change — **andyfraussen session-revoke costume**; staff: sign out/in https://forum.cursor.com/t/grok-bot-lost-connection-with-its-computer-and-cant-update-recover-reset/170775
- Steve_Grayt 170804 all bots dead / Reset partial — staff: **Privacy Mode choice never saved** on dashboard (not Legacy false-gate); set Privacy Mode then relaunch — jumpsuitgroup-adjacent, one-shot setup https://forum.cursor.com/t/grok-bots-not-responding/170804
- Nicolas_Rodrigues 170788 can’t-reach all devices after relogin 0.43→0.44 — ops, no staff https://forum.cursor.com/t/cant-reach-my-grok-bot-computer-on-any-device-tried-relogin/170788
- oscar_mei 170661 still Bot failed to respond ~38h — **im_grok** backend stuck; don’t Reset https://forum.cursor.com/t/grok-bot-0-43-0-bot-failed-to-respond-reset-agent-computer-stuck-in-partial-state/170661
- Suman1 170829 macOS local-exec generation 0 — **topic deleted by author**
- ras434@170488 residual Mac “temporarily unreachable” 1–2 min self-heal on 0.43 — aaron_72 flap family, no new kill
- Jaha/oleje32 170585 Windows *.cursorvm.com — staff: network path OK; app-side; DNS root A-record red herring

### Thin / ops / FR / off-hunt
- Joel_Whittle 170831 bots non responsive (thin) · Ronald_Naners 170743 black screen white dot · Cyle 170741 can’t log in phone+laptop · TheAviv 170832 Gmail search_threads empty for Spam (MCP coverage, not roster kill) · z_l 170771 / harrisonhou 170742 quota / Teams first-party allowance FR · meetup events 170744/759/761/762/763 · Cloud Agents fast mode 170026 · companion voice FR 168103 · SuperGrok Heavy 168558

### Already-kept (window)
- Jarri81 170683 · Winvicta 170691 · Benjamin_Barber 170689 · StefanZ 170710 · jsolly 170727
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–2; search.json Grok Bot order:latest → 50 topics; 65 unique across tag+search
- Priority NEW topic IDs fetched 200: 170819/809/829/736/816/750/745/775/788/804/831/743/741/742/832/771 + bumps 170488/585/702/727/661/694
- Saved under /workspace/field/forum0907/ (+ bodies/ for KEEP)
- Public cooked HTML stripped; no login
- Hunt itself hit Jojo1 bind reject on `python3 script.py` shapes; pipe-to-python3 worked (confirms KEEP 1)
- X / Firecrawl / Slack not used

## Bank deposits
- KEEP: `raw/ai/2026-09-07-jojo1-deanrie-grok-bot-auto-review-blocks-local.md` ← 170809
- KEEP: `raw/ai/2026-09-07-theaviv-deanrie-grok-bot-computeruse-gtk-file-chooser.md` ← 170816
- KEEP: `raw/ai/2026-09-07-noname-grok-bot-stuck-on-reconnecting-malformed.md` ← 170736

## Packet recommendation
Keep count: **3** — Jojo1 170809, TheAviv 170816, noname 170736. Cap ~2–3 FAILURES for packet (compiler total cap 5 with education). **Alert: yes** (Jojo1 only — Shell hygiene: prefer `echo … | python3` / bare interpreter; avoid absolute binary paths and `-c`). No packet file written. field-seen.json not edited.
