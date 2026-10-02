# Field Grok Bot failure hunt · packet 2026-10-02 (Asia/Taipei cron; box America/New_York Thu Oct 1 evening ET)
Cutoff: after Oct 1 KEEP Lashawn_Martin 173365, Mitra 173460 — **do not re-keep**. Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-30` (+ `after:2026-10-01`) + keyword friction (stuck, routines, plugin, Connected, Always allow, Auto-review, local execution, Reset, reconnecting, computer-use, image, failed to respond, billing, invoice, attachment, Recover, Gmail, 1Password, browser, Galaxy, Weekly Usage, VPN, screenshot). Category `c/grok-bot/l/latest.json` / `c/grok-bot/33.json` skipped (prior 404). Public, no login. No Firecrawl. Scratch for packet compiler. Do **not** write field/latest.md from this hunt.

Already kept / standing (skipped / bounce only): Oct 1 KEEP Lashawn_Martin 173365 (1Password Filled≠password). Oct 1 KEEP Mitra 173460 (Galaxy grant≠Weekly bar). Sep 30 KEEP Wes_Anderson 173321 (Gmail google.com/url redirects). Sep 30 KEEP Todd_Cunningham 173319 (screenshot view-only → computer-use helper). Sep 29 KEEP Ajay_Rao 173176 (unpaid invoice silence). Sep 29 KEEP WGG 173187 (attachments need computer). Sep 29 overflow hyper_core 173206 (Ahrefs rate-limit). Sep 28 KEEP Noah1 173142 (1Password long website URL). Sep 28 KEEP Benahordure 173116 (iOS Apple SSO → magic-link). Sep 27 KEEP Tibetan95380 173045 (wide-image pixel dims). Sep 27 KEEP Joe_Levy1 173037 (computer-use mid-run ping). Sep 26 KEEP jsolly 173019 (Plugin Connected = first connector only). Fri KEEP TheAviv 172859 (Always-allow = text). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Standing footer: Kaspersky / DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins** / **Plugin Connected = first connector only** / **Wide-image (pixel dims) in chat history kills that chat; Reset/Update won’t fix; new chat same bot** / **Computer-use helper: new message mid-run stops+restarts — wait / don’t ping** / **1Password: one Login website URL >~2000 chars kills whole vault connect (“delivery unknown”); shorten URLs or empty vault→connect→move back; full quit Cmd+Q** / **Shared 1Password autofill can show Filled while password stays empty — page rejects fill → bot clears password; use in-chat secure login form or take over once** / **iOS login: Cursor Apple SSO desktop users — no Sign-in-with-Cursor on iOS (accounts.x.ai only); magic-link to same email** / **Unpaid invoice / failed card → all bots “Bot failed to respond” (computer fine); check cursor.com/dashboard billing; don’t Reset/rebind** / **Chat attachments upload to Grok Bot computer first; text OK + “Will send after reconnecting” / Backup not ready = computer dead; Recover not Reset; full quit** / **Ahrefs marketplace: Authenticate / load fails under Ahrefs rate-limit (429 / SyntaxError / Failed to load connector); reinstall/retry won’t fix** / **Gmail connector (user-Gmail): create_draft/send_message wraps every link in google.com/url redirects; compose/paste links in Gmail UI yourself; don’t bot-send link mail** / **“No browser control” while screenshots work: screenshot is view-only; launch computer-use helper (Task/computerUse) and wait; remove saved notes denying browser tools** / **Grok Bot Galaxy / promo credit is a fixed grant tracked separately from the Weekly Usage bar — bar can stay 0% while grant burns; without access bots are hidden not deleted; restore access, fully quit+reopen; don’t Recover/Reset/recreate**. Do not re-alert footer list (+ Lashawn_Martin 173365 / Mitra 173460 / Wes_Anderson 173321 / Todd_Cunningham 173319 / Ajay_Rao 173176 / WGG 173187 / hyper_core 173206 / Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859).

## KEEP candidates (2) — recommend for packet

### KEEP 1 — shoplytics.de · All outbound non-HTTPS egress blocked since Oct 1 (SAND HTTPS-only)
- url: https://forum.cursor.com/t/grok-bot-computer-all-outbound-non-https-traffic-blocked-since-oct-1-mysql-ssh-imap-smtp-ftp-time-out/173504
- date: OP 2026-10-01 14:17 UTC; NavyWings 19:08 UTC; Aadam 20:03 UTC
- tags: teach-once, killed-claim, networking, egress, shared-computer
- score: **10** (portable 5 / evidence 5)
- packet one-liner: [agentic·teach-once·killed-claim] score=10 | shoplytics.de | After **Oct 1, 2026** computer restart, Grok Bot cloud computers can only reach the internet over **HTTPS/443** — plain HTTP/80, MySQL 3306, IMAP 993, SMTP 465/587, FTP/FTPS, SSH/22 (incl. github.com), and even non-TLS TCP on 443 all **time out**. Fingerprint: `SAND_EGRESS_TUNNEL_ENABLED=1`, `SAND_HTTP_PROXY_NAME=fastly-prod-xai-1`, local CONNECT proxy `127.0.0.1:8791`. Confirmed on **three accounts** (shoplytics.de Ultra, NavyWings, Aadam) with no Enterprise network policy. Contradicts current docs (port restrictions Enterprise-only; no-policy = allow-all). **“Route traffic through this computer” does not help** (browser-only; showed 0 routed). Stopgap: HTTPS endpoints on your own server. Don’t Reset. Await staff word on intentional vs bug. Alert: **yes** (first-party shared-computer egress capability change Oct 1 — assume non-443 dead after any computer restart until clarified).
- staff: none yet (multi-user confirm)
- bank: raw/ai/2026-10-01-shoplytics-de-grok-bot-computer-all-outbound-non.md
- topic json/md: forum1002/173504.json · 173504.md

### KEEP 2 — captMick · SAND CONNECT: hostname HTTPS TLS EOF; literal public IP works
- url: https://forum.cursor.com/t/on-grok-bot-s-cloud-computer-https-through-the-shared-sand-connect-proxy-127-0-0-1-8791-fastly-prod-xai-1-fails-when-connect-uses-my-public-hostname-but-succeeds-when-connect-uses-that-host-s-literal-public-ip/173542
- date: OP 2026-10-01 20:21 UTC
- tags: teach-once, killed-claim, networking, mcp, sand-proxy
- score: **7** (portable 4 / evidence 3)
- packet one-liner: [agentic·teach-once·killed-claim] score=7 | captMick | On Grok Bot cloud computer via shared SAND CONNECT (`127.0.0.1:8791` / fastly-prod-xai-1), **HTTPS CONNECT by public hostname** returns 200 then **TLS unexpected EOF**; same origin via **literal public VIP** completes TLS + HTTP 401. `--resolve` still CONNECTs the hostname → same EOF. Well-known public sites OK. Distinct from Local Egress RFC1918 reject and from KEEP 173504 (non-443 block) — this is hostname-vs-IP on **443**. Impact: custom MCP attach URL must be a hostname → **fails_to_load** even though origin works over SAND-by-IP. Workaround: host/ACL by IP where connector allows, or wait for SAND hostname CONNECT fix. Alert: **no** (niche MCP host; no staff yet; teach beside 173504).
- staff: none yet
- bank: raw/ai/2026-10-01-captmick-on-grok-bots-cloud-computer-https.md
- topic json/md: forum1002/173542.json · 173542.md

## OVERFLOW / watch (not packet KEEP)

### NavyWings 173540 — Viber QR login fails; bot blames blocked ports
- Bot opens Viber QR sign-in; QR never loads (“no connection”). Bot claims ports 5242/4244/5243/7985 blocked. Same day as KEEP 173504 HTTPS-only egress; NavyWings also +1’d 173504. Soft symptom reinforce of SAND non-443 kill. Alert: no.

### Brian_Miller2 173544 — 1Password won’t match Vercel preview links
- Community ask: Vercel preview URLs not recognized by 1P → Shared vault autofill won’t associate credentials; bot can’t auth preview apps. No staff. Soft 1P family watch beside 173365 / Noah1 (URL match / fill), not a new filled≠password teach. Alert: no.

### Shaun_Bowe 173549 — message pane paint glitch when switching bots
- Windows desktop 0.66.0: switch bots → blank/cutoff message pane; one mouse-wheel scroll fixes. UI paint bug, no kill mechanism. Soft watch. Alert: no.

### Ric_T 173483 — Description field missing on Ubuntu desktop
- deanrie: same docs/UI mismatch as benum 173333 — personal-bot details pane redesigned; Description no longer separate settings page. Soft UI reinforce / bounce. Alert: no.

### Sam_Smith 173538 — how to share custom MCP with team
- kevinn how-to: Publish to team → Add plugins → custom URL (local command files won’t travel). Not a failure. Bounce. Alert: no.

### Oliver_Michalik 173550 — “Hey Grok” wake-word FR. Bounce.

### Meetups 173477–173480 — Halifax / Ambato / Vienna / Kenya. Bounce.

### Juan_Carlos_Elias bump 168476 — shared Chrome sessions across Bots
- +1 on old FR: clinic Calendar Bot signed out when another Bot touches Google on shared cookie store; asks per-Bot isolated session dirs. Soft reinforce “bots are not a security boundary” / shared-computer sessions — FR without new portable kill. Overflow watch. Alert: no.

### HorstHauser 172965 / AndrewC 172777 — three Surfaces / orchestration feedback
- Colin: IDE + Agents window + Grok Bot integration WIP; launch recap. Bounce. Alert: no.

### Johannes_Isabell 169904 — shared team roster FR (bumped). Bounce.

### Hadi_Yazbeck on Mike_Winn 173434 — “connecting to cursor” stuck
- Different user on first-init thread; no new staff teach. Soft first-init / reconnecting reinforce. Alert: no.

### standing bump reinforce (do not re-KEEP): Joe_Levy1 173037 (computer-use stall + request id) · Paul_Zapata 172862 (Delilah restore still open) · KeilMS 173436 (SharePoint 117GB restore loop) · Ahmed_Elkiki 173136 closed (Kaspersky HTTPS intercept confirmed) · zeurpo/clewis 173084 (partial-state Reset ~50%) · warpdev 172343 (Backup not ready).

### Oct 1 KEEP already logged (do not re-KEEP): Lashawn_Martin 173365 · Mitra 173460.

### Oct 1 overflow already logged: Shaun_Bowe 173423 · Daniel_Brin 173388 · KeilMS 173436 · Mike_Winn 173434 · TG_Promo 173363 · etc.

## Standing kills reinforce (footer, not KEEP)
- Free-plan≡no-access / Galaxy grant≠Weekly bar (173460 — do not re-alert) · 1Password family (173365 false-Filled; 173544 Vercel-preview match overflow; do not re-alert Noah1) · first-init incomplete (173434 / Hadi watch) · computer-use don’t-ping (173037) · Backup-not-ready / don’t-Reset / partial-state (172343 · 172862 · 173084 · 173136 Kaspersky) · Description UI mismatch (173333 · 173483) · Gmail redirects / screenshot→computer-use (Sep 30 KEEP — do not re-alert) · bots≠security-boundary / shared Chrome sessions (168476 bump)

## New standing-kill text (add to footer if packet accepts KEEP)
- **Since Oct 1, 2026 computer restarts: Grok Bot shared egress (SAND tunnel / fastly-prod-xai-1 / 127.0.0.1:8791) appears HTTPS/443-only — MySQL, SSH, IMAP/SMTP, FTP, HTTP/80 time out; Route-through won’t fix (browser-only); no Enterprise policy required to hit this; don’t Reset; use HTTPS stopgaps until staff clarifies intentional vs bug** (from 173504)
- **SAND CONNECT: HTTPS by public hostname can CONNECT 200 then TLS EOF while the same public VIP completes TLS — custom MCP hostname attach may fail_to_load; try IP CONNECT / ACL by VIP; distinct from RFC1918 Local Egress reject** (from 173542)

## Method notes
- Fetched tag latest + page=1; search after:2026-09-30 and after:2026-10-01; keyword friction batch (Galaxy/1Password/VPN/screenshot/Gmail/Recover/browser/attachment/Auto-review/Weekly Usage/Always allow returned 0 on first pass — coverage already from tag+date search; retry hung, killed).
- Fully read NEW/active topics into forum1002/{id}.json + .md (173550·173549·173544·173542·173540·173538·173504·173483·meetups·172965·172777·172584·170247·169985·169904·168476·167802 + bumped SEEN 173404·173151·173136·173084·173037·172862·173434·173436·173333).
- Banked KEEP 173504 + 173542.
- Skipped re-KEEP Lashawn_Martin 173365 / Mitra 173460 / Wes_Anderson 173321 / Todd_Cunningham 173319 / Ajay_Rao 173176 / WGG 173187 / hyper_core 173206 / Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859 / Chexander 172715 / GFP 171703.
- seen-forum-ids.txt: 398 → 418 (surface ids appended, sorted unique).

FAILURE_COUNT=2
alert=yes
