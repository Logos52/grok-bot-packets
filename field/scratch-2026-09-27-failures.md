# Field Grok Bot failure hunt · packet 2026-09-27 (Sunday Asia/Taipei cron; box America/New_York)
Cutoff: after Sep 26 KEEP jsolly 173019 — **do not re-keep**. Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-25` (+ `after:2026-09-26`) + keyword friction (stuck, routines, plugin, Connected, Always allow, Auto-review, local execution, Reset, reconnecting→200). Category `c/grok-bot/l/latest.json` / `c/grok-bot/33.json` skipped (prior 404). Public, no login. No Firecrawl. Scratch for packet compiler. Do **not** write field/latest.md from this hunt.

Already kept / standing (skipped / bounce only): Sep 26 KEEP jsolly 173019 (Plugin Connected = first connector only). Fri KEEP TheAviv 172859 (Always-allow = text). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Sep 26 SEEN bounce: DXM888 172957, sd-tenbridge 172951, jsolly 172955, tianmind 172989, doughy 171895, Josiah_Fannon 173021, HorstHauser 172965, chiayu0816 172963, aptlabs 173020, NeoLuca 173014, jesse85 172902. Standing footer: Kaspersky / DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins** / **Plugin Connected = first connector only**. Do not re-alert footer list (+ TheAviv 172859 / jsolly 173019).

## KEEP candidates (2) — recommend for packet

### KEEP 1 — Tibetan95380 · Wide image (pixel dims, not file size) kills that chat; Reset/Update won’t fix
- url: https://forum.cursor.com/t/grok-bot-failed-to-respond-after-update-and-reset-windows-0-59-1/173045
- date: OP 2026-09-26 10:06 UTC; deanrie 10:25 + 13:38 UTC; Colin 14:59 UTC
- tags: teach-once, coverage-ceiling, killed-claim, human-gate
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·coverage-ceiling] score=9 | Tibetan95380 | After Update+Reset, every message in one chat fails (“Bot failed to respond”) including “hello”; other bot on same computer works. **deanrie: computer is fine — one image in that chat’s server-side history exceeds max pixel dimensions** (wide table screenshots often several thousand px across even when they look thin); limit is **pixels not file size**. Update/Reset don’t touch chat history. Workaround: **new chat same bot** (don’t need new bot / don’t delete old). Colin later asked if fixed. Distinct from weekly-limit / computer-dead / Reset-fail. Alert: **no** (teach/footer; no this-week Settings change unless Wedge pastes ultra-wide screenshots into a live tutor chat).
- staff: deanrie, Colin
- bank: raw/ai/2026-09-26-tibetan95380-deanrie-grok-bot-failed-to-respond-after.md
- topic json/md: forum0927/173045.json · 173045.md

### KEEP 2 — Joe_Levy1 · Computer-use helper: new message mid-run stops + restarts → tasks never finish
- url: https://forum.cursor.com/t/grok-bot-computer-use-agents-stall-and-fail-to-complete-simple-tasks/173037
- date: OP 2026-09-26 07:01 UTC; Colin 15:14 UTC
- tags: teach-once, human-gate, computer-use, quiet-when-working
- score: **8** (portable 5 / evidence 3)
- packet one-liner: [agentic·teach-once·human-gate·computer-use] score=8 | Joe_Levy1 | Healthy computer; clicks complete in seconds; long computer-use tasks stall / take hours. **Colin: bot hands computer tasks to a separate computer-use helper that keeps working after the chat reply; a new user message while that helper is still running tends to stop it and start over**, so the job never gets far. Portable gate: **don’t ping / progress-check mid computer-use — wait for the helper to finish** (pairs Field quiet-when-nothing / tutor-loop). Alert: **no** (routine teach, not a Settings/tool capability change this week).
- staff: Colin
- bank: raw/ai/2026-09-26-joe-levy1-grok-bot-computer-use-agents-stall.md
- topic json/md: forum0927/173037.json · 173037.md

## OVERFLOW / watch (not packet KEEP)

### Dtive 173022 — “Backup not ready” + “All screens on the shared computer are in use”
- Colin backend tweak; rematerialized; idle reclaim freed extra agent desktop leases (`:1` shared + `:2` agent). Soft coverage-ceiling watch (~6–7): host screen leases ≠ kill-local-Xvfb. Alert: no.

### ExploiTR 173050 — Linux XDG text/html hijack on launch (GNOME family)
- Colin: registering grokbot:// / sand:// via system tool also sets HTML handler on GNOME/Cinnamon/MATE; known. Workaround: `xdg-mime default brave-browser.desktop text/html` after launch / edit shortcut. Soft Linux desktop teach — overflow (not Field education path). Alert: no.

### Gurkirat_Singh 173062 — Kaspersky HTTPS scanning → ConnectError.Internal + 1000+ leaked conns (0.59.1 Windows)
- Colin confirms: Grok Bot uses **built-in public CA list**, not Windows cert store (browser/curl/Cursor IDE still work). Exclude Grok Bot / disable encrypted-connection scanning. **Standing Kaspersky reinforce** — not new KEEP. Alert: no.

### donkraider 173041 — Can’t reach + misleading *.cursorvm.com / Zscaler (Windows, India); old app can’t auto-update
- deanrie: computer healthy server-side; Retry/Recover don’t leave the machine; error text misleading; clean reinstall + AV HTTPS exclusions + hotspot test. Reinforces Zscaler/can’t-reach / AV-HTTPS family. Alert: no.

### uparrowinc 173069 (+ Mauricio_A_Perez_J) — Agent Computer Reset stuck (iOS/Mac M3)
- deanrie: forum account ≠ Grok Bot login; Reset once + wait ~5 min; screen can look stuck while reset runs in background; Mac app update + kill fixed; data kept. Mauricio: Transferring + “Bot couldn’t respond” with On-Demand remaining — separate watch. Reinforces Reset-stuck / 43% family. Alert: no.

### Rafael3 173086 — stuck 43% Transferring your data (don’t-Reset plea)
- Standing Update/Reset hung 43% reinforce; no staff yet. Alert: no.

### zeurpo 173084 — Reset freezes 50% “partial state”; can’t view screen (Mac/iOS 0.59.1)
- Standing Reset-fail/partial ≡ no access reinforce; system template only. Alert: no.

### Ailang-Author 173081 — GitHub large-file write/push burns token budget (character/byte limits)
- Soft tool-chunking / GitHub integration watch; weak Field portable teach; no staff. Overflow. Alert: no.

### mason-feature-slayer 173073 — 1Password plugin MCP `spawn 1password-mcp EACCES`
- OP marks **Cursor IDE** Marketplace plugin, not Grok Bot computer — off Field path. Bounce. Alert: no.

### Ronnie_O 173055 — “usages help” / what to use Grok Bot for
- Not a failure; community pointer to hubs. Bounce. Alert: no.

## Standing kills reinforce (footer, not KEEP)
- Kaspersky / built-in CA ≠ Windows store (173062 Colin) · Zscaler/can’t-reach misleading *.cursorvm.com + old-app reinstall (173041) · Update/Reset hung 43% (173086) · Reset-fail/partial ≡ no access (173084) · Reset screen can look stuck while background completes (173069) · Plugin Connected = first connector only (jsolly 173019 — do not re-alert)

## New standing-kill text (add to footer if packet accepts KEEP)
- **Wide-image (pixel dims) in chat history kills that chat; Reset/Update won’t fix; new chat same bot** (from 173045)
- **Computer-use helper: new message mid-run stops+restarts — wait / don’t ping** (from 173037)

## Method notes
- Fetched tag latest + page=1; search after:2026-09-25 and after:2026-09-26; keyword friction all 200 (incl. reconnecting).
- Fully read 12 NEW topics into forum0927/{id}.json + .md; appended ids to seen-forum-ids.txt (317→329).
- Banked KEEP 173045 + 173037.

FAILURE_COUNT=2
alert=no
