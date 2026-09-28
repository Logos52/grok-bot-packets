# Field Grok Bot failure hunt · packet 2026-09-28 (Monday Asia/Taipei cron; box America/New_York)
Cutoff: after Sep 27 KEEP Tibetan95380 173045 and Joe_Levy1 173037 — **do not re-keep**. Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-26` (+ `after:2026-09-27`) + keyword friction (stuck, routines, plugin, Connected, Always allow, Auto-review, local execution, Reset, reconnecting, computer-use, image, failed to respond). Category `c/grok-bot/l/latest.json` / `c/grok-bot/33.json` skipped (prior 404). Public, no login. No Firecrawl. Scratch for packet compiler. Do **not** write field/latest.md from this hunt.

Already kept / standing (skipped / bounce only): Sep 27 KEEP Tibetan95380 173045 (wide-image pixel dims). Sep 27 KEEP Joe_Levy1 173037 (computer-use mid-run ping). Sep 26 KEEP jsolly 173019 (Plugin Connected = first connector only). Fri KEEP TheAviv 172859 (Always-allow = text). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Sep 27 SEEN bounce: Dtive 173022, ExploiTR 173050, Gurkirat_Singh 173062, donkraider 173041, uparrowinc 173069, Rafael3 173086, zeurpo 173084, Ailang-Author 173081, mason-feature-slayer 173073, Ronnie_O 173055. Standing footer: Kaspersky / DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins** / **Plugin Connected = first connector only** / **Wide-image (pixel dims) in chat history kills that chat; Reset/Update won’t fix; new chat same bot** / **Computer-use helper: new message mid-run stops+restarts — wait / don’t ping**. Do not re-alert footer list (+ TheAviv 172859 / jsolly 173019 / Tibetan95380 173045 / Joe_Levy1 173037 / Wes_Anderson 171029).

## KEEP candidates (2) — recommend for packet

### KEEP 1 — Noah1 · 1Password: one Login website URL >~2000 chars kills whole vault connect
- url: https://forum.cursor.com/t/grokbot-1password/173142
- date: OP 2026-09-27 18:54 UTC; Colin 19:55 UTC; Noah1 confirm 20:13–20:22 UTC
- tags: teach-once, plugins, human-gate, killed-claim
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·plugins·killed-claim] score=9 | Noah1 | Official 1Password connector creates bot but never connects — “credential delivery method is unknown” / “delivery outcome is unknown”. **Colin: one Login in the shared vault has an extremely long website address (>~2,000 chars — usually a sign-in/redirect/tracking URL pasted from the address bar); that one item stops the whole connection**, and the UI only shows the generic delivery-unknown message. Workaround: shorten website fields to the normal origin (e.g. `https://example.com`) **or** empty the vault → connect → move items back; **fully quit Grok Bot (Cmd+Q)** before reconnect (closing the window leaves the dialog blocked). Failed attempts leave leftover 1Password service accounts to clean. Distinct from standing **Name>255** (bot display name) and **ENAMETOOLONG** (sand-client filename) and from IDE `spawn 1password-mcp EACCES` (173073). Alert: **no** (teach/footer; no this-week Field Settings change unless Wedge shares a 1Password vault with long redirect URLs into a live bot).
- staff: Colin
- bank: raw/ai/2026-09-27-noah1-colin-grokbot-1password-long-website-url-kills.md
- topic json/md: forum0928/173142.json · 173142.md

### KEEP 2 — Benahordure · iOS login only offers accounts.x.ai — Cursor Apple SSO needs magic link
- url: https://forum.cursor.com/t/grok-bot-ios-login-only-offers-accounts-x-ai-cursor-apple-sso-account-not-found/173116
- date: OP 2026-09-27 10:16 UTC; Colin 18:37 UTC
- tags: teach-once, human-gate, multi-device
- score: **7** (portable 4 / evidence 3)
- packet one-liner: [agentic·teach-once·human-gate·multi-device] score=7 | Benahordure | Desktop Grok Bot signed in with Cursor via Sign in with Apple; iOS has **no “Sign in with Cursor”** — flow goes to **accounts.x.ai** and Apple proposes creating a **new** account/email. Creating would split identity. Portable gate: find the Apple-private relay / Cursor email and use **“Send link to email to log in” (magic link)** — same Bots as desktop. **Colin: working on it; magic link is the correct workaround now.** Distinct from standing iOS unexpected-error / multi-device account-stuck (those are post-login stuck; this is login-UI path missing Cursor Apple SSO). Alert: **no** (routine teach; not a this-week tool/Settings change for Field path).
- staff: Colin
- bank: raw/ai/2026-09-27-benahordure-colin-grok-bot-ios-login-only-offers.md
- topic json/md: forum0928/173116.json · 173116.md

## OVERFLOW / watch (not packet KEEP)

### chrisoh806 173109 — Computer Updating stuck at 43% (Transferring your data)
- deanrie: known; computer safe; stuck update usually gives up ~1h after start → fully close+reopen; **don’t Reset** (wipes); bots keep running on mobile. Standing Update/Reset hung 43% + nhog don’t-Reset reinforce. Alert: no.

### Ahmed_Elkiki 173136 — Can’t reach 7 days + Recover/Reset fail (partial state)
- Windows 0.57.1; Retry/Recover/Reset fail; Send Feedback undeliverable; sign-out/in left name as “?”. No staff yet. Standing Reset-fail/partial ≡ no access reinforce. Alert: no.

### Ted_Glenwright 173151 — Finance/Plaid: can’t link a second institution after first
- Chase linked; no UI to open Plaid again for Schwab; uninstall/reinstall reconnects Chase only. Soft plugin coverage-ceiling watch (~5–6); no staff. Overflow. Alert: no.

### Wes_Anderson 173140 — Gmail Spam searches empty (merged → 170832)
- Colin merged into TheAviv 170832 Spam/search_threads family. Do not re-alert Wes_Anderson / TheAviv Gmail Spam. Bounce. Alert: no.

### astor-zar me-too on 170661 — Bot failed to respond; Reset didn’t work
- Old oscar_mei thread; deanrie Sep 27: computer recovered Sep 8. Fresh me-too only. Standing Reset-fail / failed-to-respond reinforce. Alert: no.

### GrokBotIsCool 173157 — FR: per-oauth enable/disable toggles
- Security feature request, not a named failure/gate. Bounce. Alert: no.

### TheAviv 172600 — still-cover video B-frames → QuickTime silence (deanrie recipe)
- Do not re-alert TheAviv. Soft media teach overflow. Alert: no.

### Meetups 173103–173108 — Villahermosa / Kigali / Managua / Florianópolis / KSU Atlanta / H-FARM Treviso
- Events only. Bounce. Alert: no.

### 172959 Project sub-agent model mismatch / 173087+172012 usage meter / 170359 Plaid FR bump / 173051 Grok-code rant
- Off Field failure path or non-Grok-Bot-primary. Bounce. Alert: no.

### Mayu-doop bump 170358 — routines still don’t fire (0.61.0 Windows, Japan)
- Standing server-routines reinforce; already seen. Alert: no.

### Dtive 173022 — Backup not ready rematerialized
- Already SEEN Sep 27 overflow; Colin prior. Soft screens-in-use / backup watch. Alert: no.

## Standing kills reinforce (footer, not KEEP)
- Update/Reset hung 43% + nhog don’t-Reset (173109 deanrie) · Reset-fail/partial ≡ no access (173136) · server-routines don’t auto-run (170358 Mayu-doop) · Wide-image pixel-dims (173045 Tibetan confirm fixed via new chat) · Plugin Connected = first connector only (jsolly 173019 — do not re-alert) · TheAviv Always-allow / Gmail Spam family (do not re-alert)

## New standing-kill text (add to footer if packet accepts KEEP)
- **1Password: one Login website URL >~2000 chars kills whole vault connect (“delivery unknown”); shorten URLs or empty vault→connect→move back; full quit Cmd+Q** (from 173142)
- **iOS login: Cursor Apple SSO desktop users — no Sign-in-with-Cursor on iOS (accounts.x.ai only); magic-link to same email** (from 173116)

## Method notes
- Fetched tag latest + page=1; search after:2026-09-26 and after:2026-09-27; keyword friction (stuck/routines/plugin/Connected/Always+allow/Auto-review/local+execution/Reset/reconnecting/computer-use/image/failed+to+respond) — some 429 then retry 200.
- Fully read 22 NEW topics into forum0928/{id}.json + .md; appended ids to seen-forum-ids.txt (329→351).
- Banked KEEP 173142 + 173116.
- Skipped re-KEEP Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859.

FAILURE_COUNT=2
alert=no
