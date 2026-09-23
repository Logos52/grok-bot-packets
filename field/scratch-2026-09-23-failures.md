# Field Grok Bot failure hunt · packet 2026-09-23 (Wednesday)
Cutoff: after ~2026-09-21/22 00:00 UTC (post Tue packet KEEP Michael_Pan 172494 — **do not re-keep**). Forum via public topic JSON + `tag/grok-bot/l/latest.json` + `search.json?q=Grok+Bot+after:2026-09-21` (+ `after:2026-09-22`) + keyword searches. Category `c/grok-bot/l/latest.json` and `c/grok-bot/33.json` → **404 invalid** (skip; use tag+search). Public, no login. No Firecrawl. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Tue KEEP Michael_Pan 172494 (forever-box empty agent-transcripts = server-side runtime / ReadTranscript). Mon KEEP chrisoh806 172401 (43% Transferring). Sun KEEP BigBojangles 172349 (local-exec root). Sat KEEP Volkan_Erdogan 172135; Sat KEEP Anderson_V_Leite 172142. Fri KEEP Dave_Campos 172070; Fri KEEP allninety 171962. Standing footer: Catty Kaspersky / Zscaler / server-routines webhook / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / router DNS / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / local-exec root / Update/Reset hung 43% / forever-box ReadTranscript / nhog don’t-Reset. Do not re-alert footer list.

## KEEP candidates (3) — recommend for packet (edu setups take priority for cap; compiler pick top 1–2 if slot-tight)

### KEEP 1 — dnz · api2 100.x misroute → Pearson TLS cert; don’t Reset; traceroute / 100.0.0.0/8
- url: https://forum.cursor.com/t/grok-bot-keeps-reconnecting-api2-cursor-sh-resolves-to-100-60-17-13-which-presents-a-certificate-for-devapi-english-com/172578
- date: OP 2026-09-22 03:02 UTC; mohitjain staff 2026-09-22 12:13 UTC
- tags: networking, teach-once, killed-claim (misdiagnosed Reset), persistent-computer
- score: **10** (portable 5 / evidence 5)
- packet one-liner: [agentic·networking·teach-once·killed-claim] score=10 | dnz | “Can’t reach your computer” + updater “certificate invalid / server pretending to be api2.cursor.sh”: api2 → api2geo → api2direct; public DNS (1.1.1.1 / 8.8.8.8) returns **100.60.17.13** which presents cert for **devapi.english.com** (Pearson/Sectigo); sibling IP 34.235.15.195 serves correct api2 cert; **mobile hotspot works**. No local proxy/AV HTTPS scan. **mohitjain: computer healthy — don’t Reset or Recover.** 100.60.17.13 is a real api2 address and serves the correct cert from outside; Pearson cert means **office/ISP is delivering that address to the wrong server**. Teach: `traceroute -n 100.60.17.13` vs `34.235.15.195`; ask net team to check firewall/NAT/routing covering **100.0.0.0/8** (often added by mistake near **100.64.0.0/10** CGNAT). Hotspot keeps you connected meanwhile. **Distinct from** Kin_Su router DNS SERVFAIL and Catty Kaspersky TLS MITM. Alert: **no** (durable standing-kill teach; not a this-week Field roster path change).
- staff: mohitjain
- bank: raw/ai/2026-09-23-dnz-grok-bot-keeps-reconnecting-api2-cursor.md

### KEEP 2 — codercurtis · Ubuntu 22.04 missing GLIBCXX_3.4.31 → local-exec helper never starts; chat OK
- url: https://forum.cursor.com/t/grok-bot-local-execution-never-connects-listmachines-connected-false-while-desktop-chat-works/172307
- date: OP 2026-09-18 23:20 UTC; Colin confirm 2026-09-19; Colin fix 2026-09-20 09:01 UTC; auto-closed 2026-09-22
- tags: local-exec, teach-once, killed-claim, linux
- score: **10** (portable 5 / evidence 5)
- packet one-liner: [agentic·local-exec·teach-once·killed-claim] score=10 | codercurtis | Desktop chat “Sent from machine …” works; **ListMachines connected:false**; Shell with machineId fails before approval (“local machine isn’t connected”). Settings fine; Always-allow on. Daemon log: `libstdc++.so.6: version GLIBCXX_3.4.31 not found` (tree-sitter binding) on **Ubuntu 22.04.5**. **Colin: helper needs newer C++ runtime than 22.04 ships; nothing to Reset.** Fix: (1) `ppa:ubuntu-toolchain-r/test` + `apt install --only-upgrade libstdc++6`, quit+reopen, `hostname` on this computer; or (2) upgrade to **Ubuntu 24.04**. **Distinct from** BigBojangles local-exec root/profile-only and ras434 ConnectError flap. Alert: **no**.
- staff: Colin
- bank: raw/ai/2026-09-23-codercurtis-grok-bot-local-execution-never-connects.md

### KEEP 3 — Ryan_Daley · routines “don’t wake” = schedule **queue** (20–45 min late early US), not asleep; DM skips queue
- url: https://forum.cursor.com/t/grok-bot-routines-dont-wake-up-at-the-beginning-of-a-new-day/172545
- date: OP 2026-09-21 18:58 UTC; mohitjain staff 2026-09-22 06:55 UTC
- tags: routines, teach-once, reveal-schedule, killed-claim
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·routines·teach-once·reveal-schedule] score=9 | Ryan_Daley | Morning routines + sub-agents appear asleep until human “wake up”; staggered starts still late; handoff looks “thinking 30 min.” **mohitjain: routines are firing — they’re queued.** Direct message skips the queue. Worst window ~**5–9 AM Pacific** (20–45 min late); other busy times ~20 min. Teach: schedule time-sensitive jobs **before ~4:30 AM PT** (delay usually <10–15 min + ~10 min randomization slack); if prompts say “don’t catch up when late,” have scouts send a one-line **“skipped, ran too late”** instead of silent stand-down. **Elevates** Tue bounce (no staff) → Wed KEEP; cousin of SEEN 170358 non-fire but **new mechanism = queue latency**. Alert: **no** (ops teach; no Field routine file to change this week unless a roster morning job is hard-timed).
- staff: mohitjain
- bank: raw/ai/2026-09-23-ryan-daley-grok-bot-routines-dont-wake-up.md
- note: Tue scratch bounced this as FR/ops pre-staff; staff landed Tue evening / Wed morning window — elevate.

## OVERFLOW / watch (not packet KEEP)

### Timothy_Gresh 172549 — Windows endpoint security kills process under CopyFromBox+Chrome automation (elevate from Tue watch)
- mohitjain: idle Shell OK hours; dies only on CopyFromBox+%TEMP%+Chrome UI → most likely **endpoint security ending Grok Bot.exe** (no tray on Windows → app closes + computer disconnects; no WER). Teach: admin exclusion for `Grok Bot.exe` + Temp path; check Task Manager + Protection history. **Reinforce** Windows partial-state AV HTTPS family (different surface: process-kill during local automation). Score≈8 — overflow reinforce, not second-KEEP. Alert: no.

### nhog 172535 — 43% Transferring; kevinn don’t-Reset (Tue overflow reinforce)
- Same family as Mon KEEP chrisoh806 172401. kevinn: auto Update copy-step stuck; don’t Reset; wait ~1h; mobile works; fix shipped. Do not KEEP. Alert: no (footer standing).

### Coordinacion_Desarro 172519 — “starting up” 48–72h; mohitjain server-side clear; don’t Reset
- Tue watch → Wed staff: blocked Reset/Recover/Update intentionally; computer restored; quit+reopen. Account-stuck cousin closed. Reinforce only. Alert: no.

### Carter-Ventucci 172368 — runtime replica fixed; Phantom plugin leftover
- Main failure fixed (quit+reopen). Residual Phantom “needs setup” leftover from outage — soft watch, not new computer kill. Footer: do not re-alert Carter. Alert: no.

### Wendell_Santos 172344 — all bots/machines stuck; mohitjain server-side restore; don’t Reset
- Account-stuck cousin; restored Wed. Reinforce. Alert: no.

### Raymond_Weiss / Anthony_Santoso / DoubleTop / Kevin_Scott1 172371 — bots silent; mohitjain server stall ~30 min; don’t Reset
- Soft one-bot-silent / fleet-stall reinforce. Multi-OP pile-on; no new durable mechanism. Alert: no.

### Palan 171969 — still ELB/backend after wipe (Tue reinforce)
- Kin_Su→account-stuck standing. No new staff. Reinforce only. Alert: no.

### ras434 172658 — local-exec flap residual #170488; Colin self-heal / timestamped log
- Server stream drop + retry; Mac healthy since 0.57.1; tracked server-side. Soft reinforce local-exec flap — not KEEP. Alert: no.

### Vikas_Dakshi 172696 — Can’t reach; Recover/Reset fail at 50% (wipe-then-fail)
- first-init incomplete / Volkan cousin; **no staff yet**. Watch. Alert: no.

### Chexander 172715 — “Route traffic through this computer” misses split-horizon DEV (Plex)
- Bot DNS → public IP; desktop → 192.168.x; CONNECT 200 then TLS EOF. **No staff yet.** Potential Wed+ elevate if staff teach portable tunnel/DNS rule. Watch. Alert: no.

### Peacerk 172618 — can’t reach + AdGuard disabled still fails
- Thin OP; DNS/AV cousin; no staff. Soft watch. Alert: no.

### yb-kevin 172626 — Reconnecting; self-closed as local Wi-Fi
- Bounce/self-resolved. Alert: no.

### jsolly 172015 — mobile scroll flips Auto-review (Tue soft≈8)
- No new staff this window. Soft overflow if friction slot. Alert: no.

## BOUNCE

### Already-kept / standing reinforce (do not KEEP)
- Michael_Pan 172494 — Tue KEEP skip
- chrisoh806 172401 / nhog 172535 — 43% family
- BigBojangles 172349 — local-exec root
- Carter 172368 / Coordinacion 172519 / Wendell 172344 / Palan 171969 — account-stuck
- Volkan 172135 — Recover/Reset 50%
- SEEN 170358 routines schedule (Ryan elevates with queue teach, not this id)

### Non-failure / UX / FR / Cloud Agents / meetup
- francotgs 172502 — 0x0 window-state; Colin: exit_code=21 Chromium sandbox / Win KB5124008 family (points to Cursor crash thread) — UX/OS, not Field kill
- David.J 172461 — agent label chip removed intentional (prior)
- 168333 / diaoguoliang 172465 — prune/compact / clear-chat FR
- 172705 ~$1500 fleet spend — billing FR
- 172584 Ultra usage too low — billing FR
- 172592 Origin PR merge — product FR
- 172712 Slack account switch — UX
- 172600 multi-GB review video — capability limit
- 172484 image track-geometry — capability FR
- 171540 context window Pro+ — FR
- 171948 Bitwarden connector — FR
- 170888 SuperGrok vs Ultra — pricing
- 169638 Cloud Agent model mismatch — Cloud Agents
- 172713 My Machines controller_disconnected — Cloud Agents / workers (not Grok Bot forever-box)
- Tyler_Miller 172457 — Cloud Agent empty transcript (Colin Archive; Tue soft)
- 171690 Cursor crashes — Chromium sandbox KB (related to 172502)
- 171680 Desktop MCP Meta Ads — MCP auth
- Meetup stubs 172601–172631 etc. — bounce
- 159110 knowledge-worker product FR — bounce

## Fetch notes
- `c/grok-bot/l/latest.json?page=0|1` and `c/grok-bot/33.json` → **404** (invalid category); used `tag/grok-bot/l/latest.json` + search after:2026-09-21 / after:2026-09-22 + keyword sweeps (Reset, forever-box, ConnectError, Auto-review, ReadTranscript, local-exec, Kaspersky, stuck, failed, Update Computer, transcript, routine). Brief 429 mid-keyword; retries succeeded.
- Saved under `/workspace/field/forum0923/`
- Priority topics fully read: 172578, 172715, 172658, 172535, 172519, 172368, 172371, 172344, 172696, 172626, 172618, 172549, 172502, 172713, 172307, 171969, 172545, 172457 (+ tag/search listings)
- Bank INDEX grepped — no prior deposits for 172578 / 172307 / 172545
- Appended newly fully-read topic ids to seen-forum-ids.txt

## Bank deposits
- KEEP: `raw/ai/2026-09-23-dnz-grok-bot-keeps-reconnecting-api2-cursor.md` ← 172578
- KEEP: `raw/ai/2026-09-23-codercurtis-grok-bot-local-execution-never-connects.md` ← 172307
- KEEP: `raw/ai/2026-09-23-ryan-daley-grok-bot-routines-dont-wake-up.md` ← 172545

## Result for compiler
- FAILURES recommend: **3** (dnz 172578 score=10 — 100.0.0.0/8 api2 misroute / Pearson cert / don’t Reset; codercurtis 172307 score=10 — Ubuntu 22.04 GLIBCXX local-exec; Ryan_Daley 172545 score=9 — routines queue not asleep). Edu SETUPS take remaining cap slots if tight — prefer **dnz** then **codercurtis** if only one friction slot.
- Soft overflow: Timothy_Gresh 172549 (endpoint AV process-kill, staff) ≈8; Chexander 172715 split-horizon route-through watch; Vikas 172696 fail-at-50% watch; jsolly 172015 soft≈8
- KILLED mirror: (1) “Can’t reach + bad api2 cert” ≠ broken computer — **office/ISP 100.x misroute**; don’t Reset; traceroute; hotspot. (2) Linux chat-OK / local-exec-dead ≠ Reset — **GLIBCXX too old on Ubuntu 22.04**. (3) Morning routines “asleep” ≠ broken schedules — **server queue**; schedule earlier / announce skip.
- Related reinforce (not KEEP): nhog 172535 / Coordinacion 172519 / Carter 172368 / Wendell 172344 / 172371 stall / ras434 flap / Palan 171969
- Alert: **none**
