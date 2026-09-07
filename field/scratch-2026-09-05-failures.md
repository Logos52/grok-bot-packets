# Field Grok Bot failure hunt · packet 2026-09-05
Cutoff: after ~2026-09-03 00:00 UTC (post packet-21 / packet-22 keeps). Forum via public JSON: `search.json?q=Grok+Bot+order:latest`, `tag/grok-bot/l/latest.json` pages 0–1. `/tags/grok-bot/l/latest.json` → empty. Public, no login. X skipped. No packet file. field-seen.json untouched.

Already kept/seen (skipped): Chip_Randa 170489, aaron_72 170488, 170482, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, MistakeNot76 170512, michael_pulley 170509, iamkingsleyf 170421, Tangerang 170452.

## KEEP candidates (3)

### KEEP 1 — jumpsuitgroup · Grok Bot Cloud Agent launch falsely hits Privacy Mode (Legacy)
- url: https://forum.cursor.com/t/grokbot-failing-to-connect-to-cloud-agent/170486
- date: 2026-09-03 16:19 UTC (23:19 ICT 3 Sep)
- tags: coverage-ceiling, killed-claim
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·coverage-ceiling·killed-claim] score=9 | jumpsuitgroup | macOS. Ask Grok Bot to launch a Cloud Agent → **“Cloud agents are not supported in Privacy Mode (Legacy).”** Cursor Privacy shows current Privacy Mode (Active — no training; code may be stored for Cloud Agent). Same account/repo/moment: **Cursor Desktop Cloud dropdown launches fine**; only the Grok Bot path fails. Sign-out/in and privacy toggles no-ops. Staff deanrie: account settings correct; **recent release made the Grok Bot launch path incorrectly hit the Legacy check** — tracked, no user-side fix. Killed: Grok Bot → Cloud Agent uses the same current Privacy Mode gate as Cursor Desktop (no false Legacy block). Distinct from model-preference Cloud Agent spawn 169746 — here the launch is hard-blocked by a stale privacy gate. Alert: no.
- staff: deanrie 2026-09-03 18:21 UTC — service-side regression; tracking; don’t reset/sign-out.
- bank: raw/ai/2026-09-05-jumpsuitgroup-grokbot-failing-to-connect-to-cloud.md

### KEEP 2 — andyfraussen · session revoke / password change surfaces as “Can’t reach computer”
- url: https://forum.cursor.com/t/cant-access-grok-bot-anymore-probably-after-updating-to-0-39-0/170568
- date: 2026-09-04 09:53 UTC (16:53 ICT 4 Sep)
- tags: killed-claim
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·killed-claim] score=9 | andyfraussen | macOS 0.39.0 + iOS. Sudden can’t-reach on every network; Retry / Update Computer / Reset all no-ops; Privacy Mode tip from other threads didn’t help. Staff Colin: **computer + bots healthy; routines still completed** — apps look “down” because **Active Sessions were revoked ~07:25 UTC**; clients kept dead tokens and mapped auth failure to the generic can’t-reach / firewall screen. Sign out + sign in on each device restored. Sibling _Remi 170438 (2026-09-03): password change ended sessions → same false can’t-reach after 0.36.0 update; deanrie same diagnosis; sign-out/in fixed; OP asked for auto-logout UX. Killed: when the session is dead, force re-auth UI (not “Can’t reach computer” / Reset / Recover). Distinct from digvijaysai DNS (real reachability) and Chip_Randa service-side setup (temp outage) — here **auth death wears a network costume** while the box keeps running. Alert: no.
- staff: Colin 2026-09-04 12:42 UTC (andy — resolved); deanrie 2026-09-03 09:44 UTC (_Remi — resolved).
- sibling: https://forum.cursor.com/t/grokbot-fails-after-update-cant-reach-your-computer/170438
- bank: raw/ai/2026-09-05-andyfraussen-cant-access-grok-bot-anymore-probably.md (+ raw/ai/2026-09-05-remi-grokbot-fails-after-update-cant-reach.md)

### KEEP 3 — George_Burchell · sign-out clears gateway-descriptor; sign-in leaves empty roster until Android sync
- url: https://forum.cursor.com/t/grok-bot-0-39-0-on-windows-existing-computer-not-reattached-after-sign-in-all-bots-missing/170607
- date: 2026-09-04 15:10 UTC (22:10 ICT 4 Sep)
- tags: persistent-computer, killed-claim
- score: 8 (portable 4 / evidence 4)
- packet one-liner: [agentic·persistent-computer·killed-claim] score=8 | George_Burchell | Windows 11 Grok Bot 0.39.0. Can’t-reach / Zscaler / `*.cursorvm.com` → sign-out/in same account → stuck **“Reconnecting… Retrying…”** plus **“No saved Bots yet.”** DNS/TCP/HTTPS to assigned host OK; no proxy. Local forensics: before sign-out, roster + `gateway-descriptor.json` present; **sign-out wiped them; sign-in never reissued the descriptor**; local-exec daemon never started. Did not Recover/Reset (data-preservation ask). Workaround: install **Android** Grok Bot → accept **sync with computer** → Windows desktop immediately reattached with all Bots/messages/routines intact. Staff Colin: restart Grok Box (before OP workaround). Killed: after re-auth, desktop reattaches the existing computer/gateway descriptor without needing a second client’s sync — and must not flash an empty first-run roster while the remote bots still exist. Distinct from im_grok 170373 (Recover restores sidebar, VM still unreachable) and Axel 170265 (macOS empty env while iOS still lists bots) — here **Android sync is the reattach path** after a wiped gateway descriptor. Alert: no.
- staff: Colin 2026-09-04 15:21 UTC — restart ask; OP resolved via Android sync minutes later.
- bank: raw/ai/2026-09-05-george-burchell-grok-bot-0-39-0-on.md

## BOUNCE

### Named / adjacent (not kept this pass)
- Amy_Ostler 170462 Free/unlinked plan shown as can’t-reach; deanrie: confusing entitlement wording; Goten SuperGrok-linked still stuck (sibling thread ask) — coverage-ceiling adjacent but billing/UX, not roster practice https://forum.cursor.com/t/grok-bot-windows-cant-reach-computer/170462
- LLMTester 170523 status beats leak across projects on same bot — Colin: **by design** (one bot = one memory); separate bots for isolation; chat-scoped memory WIP — not a kill https://forum.cursor.com/t/status-beat-leaks-between-bots/170523
- Ken_Feng 170608 local-exec daemon SIGTERM loop + http_502 (aaron_72 170488 flapping sibling) https://forum.cursor.com/t/i-cant-not-access-my-local-computer-file-with-grok-bot/170608
- AaronW 170632 local machine isn’t connected 0.39.0; kevinn backend computer update https://forum.cursor.com/t/grok-bot-not-connecting-to-local-computer-version-0-39-0/170632
- Jaha 170585 / mblabs.io 170536 phone OK, desktop can’t-reach; deanrie: computer healthy, desktop not reaching servers (proxy/firewall path) — digvijaysai-adjacent ops https://forum.cursor.com/t/windows-11-grok-bot-cant-reach-computer-cursorvm-com/170585 · https://forum.cursor.com/t/grok-bot-0-39-0-macos-cant-reach-computer/170536
- shubham_chaturvedi 170430 Reset partial-state first setup — Colin → DNS sibling of xprayag 170320 (im_grok mechanism already kept) https://forum.cursor.com/t/grok-bot-reset-failed-computer-stuck-in-partial-state-cant-connect/170430

### Sep 3–5 ops / can’t-reach / white-dot / setup cluster (group bounce)
- Price_Ambler 170620 Reset hangs loop (+ Liam_Serour “same”)
- Cole_Kramer 170596 0.39.0 Mac reconnecting / bots missing (Colin backend knobs)
- hwaynefair 170483 first-setup can’t-reach → merged into 170482
- ALIN_FARAH 170474 new-install can’t-reach macOS
- Siddharth_Arya 170450 black-dot blank after setup
- otnayugiret 170408 reconnecting + blank Computers pane
- Mihir_Rabade 170637 Linux RPM download Access Denied (install CDN)

### FR / events / off-hunt
- Shopify connector 170605 · iOS wide markdown tables 170581 · bot colors 170525
- Meetups/workshops: Guangzhou 170586, Porto 170547, CDMX/Chihuahua/Bandung/Hangzhou/Beijing/Freiburg/San Salvador 170545–170538
- Web agents dual spend 170507 · Plaid FR 170359 (older)

### Already-kept (window)
- Chip_Randa 170489 · aaron_72 170488 · 170482 · MistakeNot76 170512 · michael_pulley 170509
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373

## Fetch notes
- `https://forum.cursor.com/tags/grok-bot/l/latest.json` → empty body this run; use `https://forum.cursor.com/tag/grok-bot/l/latest.json` (+ `?page=1`)
- `search.json?q=Grok%20Bot%20order%3Alatest` returned 50 topics (missed some tag-only IDs; tag pages caught 170483/474/462/450/438/430/408)
- Topic JSON public; cooked HTML stripped (raw often omitted)
- X / Slack / Gmail not used

## Bank deposits
- KEEP: `raw/ai/2026-09-05-jumpsuitgroup-grokbot-failing-to-connect-to-cloud.md` ← 170486
- KEEP: `raw/ai/2026-09-05-andyfraussen-cant-access-grok-bot-anymore-probably.md` ← 170568
- KEEP: `raw/ai/2026-09-05-george-burchell-grok-bot-0-39-0-on.md` ← 170607
- Sibling: `raw/ai/2026-09-05-remi-grokbot-fails-after-update-cant-reach.md` ← 170438

## Packet recommendation
Keep count: **3** — jumpsuitgroup 170486, andyfraussen 170568 (+ _Remi 170438), George_Burchell 170607. No alert-line. No packet file written. field-seen.json not edited.
