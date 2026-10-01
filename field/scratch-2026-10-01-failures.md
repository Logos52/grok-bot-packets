# Field Grok Bot failure hunt · packet 2026-10-01 (Asia/Taipei cron; box America/New_York Wed Sep 30 evening ET)
Cutoff: after Sep 30 KEEP Wes_Anderson 173321, Todd_Cunningham 173319 — **do not re-keep**. Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-29` (+ `after:2026-09-30`) + keyword friction (stuck, routines, plugin, Connected, Always allow, Auto-review, local execution, Reset, reconnecting, computer-use, image, failed to respond, billing, invoice, attachment, Recover, Gmail, 1Password, browser). Category `c/grok-bot/l/latest.json` / `c/grok-bot/33.json` skipped (prior 404). Public, no login. No Firecrawl. Scratch for packet compiler. Do **not** write field/latest.md from this hunt.

Already kept / standing (skipped / bounce only): Sep 30 KEEP Wes_Anderson 173321 (Gmail google.com/url redirects). Sep 30 KEEP Todd_Cunningham 173319 (screenshot view-only → computer-use helper). Sep 29 KEEP Ajay_Rao 173176 (unpaid invoice silence). Sep 29 KEEP WGG 173187 (attachments need computer). Sep 29 overflow hyper_core 173206 (Ahrefs rate-limit). Sep 28 KEEP Noah1 173142 (1Password long website URL). Sep 28 KEEP Benahordure 173116 (iOS Apple SSO → magic-link). Sep 27 KEEP Tibetan95380 173045 (wide-image pixel dims). Sep 27 KEEP Joe_Levy1 173037 (computer-use mid-run ping). Sep 26 KEEP jsolly 173019 (Plugin Connected = first connector only). Fri KEEP TheAviv 172859 (Always-allow = text). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Standing footer: Kaspersky / DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins** / **Plugin Connected = first connector only** / **Wide-image (pixel dims) in chat history kills that chat; Reset/Update won’t fix; new chat same bot** / **Computer-use helper: new message mid-run stops+restarts — wait / don’t ping** / **1Password: one Login website URL >~2000 chars kills whole vault connect (“delivery unknown”); shorten URLs or empty vault→connect→move back; full quit Cmd+Q** / **iOS login: Cursor Apple SSO desktop users — no Sign-in-with-Cursor on iOS (accounts.x.ai only); magic-link to same email** / **Unpaid invoice / failed card → all bots “Bot failed to respond” (computer fine); check cursor.com/dashboard billing; don’t Reset/rebind** / **Chat attachments upload to Grok Bot computer first; text OK + “Will send after reconnecting” / Backup not ready = computer dead; Recover not Reset; full quit** / **Ahrefs marketplace: Authenticate / load fails under Ahrefs rate-limit (429 / SyntaxError / Failed to load connector); reinstall/retry won’t fix** / **Gmail connector (user-Gmail): create_draft/send_message wraps every link in google.com/url redirects; compose/paste links in Gmail UI yourself; don’t bot-send link mail** / **“No browser control” while screenshots work: screenshot is view-only; launch computer-use helper (Task/computerUse) and wait; remove saved notes denying browser tools**. Do not re-alert footer list (+ Wes_Anderson 173321 / Todd_Cunningham 173319 / Ajay_Rao 173176 / WGG 173187 / hyper_core 173206 / Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859).

## KEEP candidates (2) — recommend for packet

### KEEP 1 — Lashawn_Martin · Shared 1Password autofill says Filled but password stays empty
- url: https://forum.cursor.com/t/grok-bot-shared-1password-autofill-says-filled-but-password-stays-empty-instagram/173365
- date: OP 2026-09-29 20:06 UTC; deanrie 2026-09-30 05:06 UTC
- tags: teach-once, human-gate, killed-claim, 1password, plugins
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·human-gate·killed-claim] score=9 | Lashawn_Martin | Shared 1Password Connect autofill can show **Filled** (even fill+submit) while only username lands and **password stays empty** — Instagram / Letterboxd and “every site” for OP. Vault password fine manually. **deanrie: known/tracked — on some login pages the site won’t accept the autofilled password; Grok Bot then clears the password for security; the card still says Filled.** Workarounds: (1) ask bot to use the **secure in-chat login form** (you type password; bot can’t see it); (2) **take over** the bot computer once, log in + 2FA yourself, hand back — session usually sticks. Distinct from standing Noah1 URL-length vault-connect kill and Emanuelle takeover/rate-limit overflow. Alert: **no** (teach/footer 1Password family).
- staff: deanrie
- bank: raw/ai/2026-09-30-lashawn-martin-grok-bot-shared-1password-autofill-says.md
- topic json/md: forum1001/173365.json · 173365.md

### KEEP 2 — Mitra · Galaxy promo credit burns while Weekly Usage stays 0%; bots hidden without access
- url: https://forum.cursor.com/t/grok-bots-missing/173460
- date: OP 2026-09-30 22:57 UTC; kevinn 23:40 UTC
- tags: teach-once, killed-claim, billing, access, multi-device
- score: **8** (portable 5 / evidence 3)
- packet one-liner: [agentic·teach-once·killed-claim] score=8 | Mitra | Created/trained 12 bots on **Grok Bot Galaxy** promo; **Weekly Usage bar stayed 0%** the whole night while grant burned; next morning membership paywall; second-account switch then roster “gone”; Recover failed. **kevinn: bots not deleted — hidden because account has no active Grok Bot access; Galaxy credit is a fixed free grant tracked separately from the Weekly Usage bar (bar can stay 0% while grant burns); 12 bots training overnight exhausted it ~9:50 PM Toronto Sep 23.** Restore access (Start Trial / paid plan / SuperGrok link), fully quit+reopen — don’t Recover, Reset, or recreate same-name bots. Extends standing **Free-plan≡no-access** with portable meter teach. Alert: **no** (teach/footer; only matters if Wedge is on Galaxy/promo grant this week).
- staff: kevinn
- bank: raw/ai/2026-09-30-mitra-grok-bots-missing.md
- topic json/md: forum1001/173460.json · 173460.md

## OVERFLOW / watch (not packet KEEP)

### Shaun_Bowe 173423 — 1Password won’t fill Google OAuth popup password
- deanrie: known/tracked — filler rejects small Google sign-in popup (“doesn’t qualify as full sign-in form”); nothing typed. Workaround: take over at password step, type from 1Password yourself + 2FA, hand back; Google session usually sticks for later Sign-in-with-Google. Soft teach beside KEEP 173365 / Emanuelle takeover; overflow (same 1P human-gate family). Alert: no.

### Daniel_Brin 173388 — bot installed VPN → computer unreachable; Retry/Recover/Reset fail
- Colin: computer stuck running-but-unreachable; in-app Retry/Recover/Reset can’t clear; staff rebuilt; bots/files/logins kept; full quit+reopen. OP blamed free VPN client the bot installed. Soft killed-claim / don’t-let-bot-VPN watch; staff didn’t explicitly confirm VPN as root cause. Alert: no.

### KeilMS 173436 — restore keeps copying ~117GB SharePoint mirror into home/box/Projects
- kevinn: wipe offered (files/logins gone; bots/chats/routines stay). OP: also wipe cloud backup that re-restores the SharePoint mirror. Niche disk/backup loop; account-specific support. Soft watch beside standing Backup-not-ready / Reset family. Alert: no.

### Mike_Winn 173434 — new account first startup incomplete; mobile stuck reconnecting
- kevinn: first startup didn’t finish; staff rebuilt; full quit Mac+iPhone; resolved. Standing **first-init incomplete** reinforce. Bounce. Alert: no.

### TG_Promo 173363 — GenerateImage aspect_ratio dropped (always 1280×720 JPEG)
- deanrie: known — aspect_ratio dropped before send; .png name / JPEG bytes tracked separately; crop workaround only. Soft image-gen watch (yesterday overflow + staff). Alert: no.

### mr.ukie 173356 — Chief bot not talking to other bots
- Colin: new Chief messaging OK now; known issue if it recurs. Soft multi-bot reinforce. Alert: no.

### benum 173333 — Bot role description missing from info pane
- deanrie: docs/UI mismatch after pane layout change; known/tracked; Team Bots still show description in About. Soft UI-regression / FR. Alert: no.

### Kevin_Carroll 173426 — Asana connector redirect_uri invalid_request
- kevinn: Asana stopped accepting saved sign-in; redirect_uri must match Asana app OAuth settings. Config/setup, not portable kill. Soft connector watch (near 171877 MCP redirect_uri family). Alert: no.

### zdfs 173424 — shared canvases don’t scroll (Grok Bot Terms dialog z-index trap)
- kevinn: shared-canvas viewer; Radix “Grok Bot Terms” dialog behind opaque shell blocks input; OP DevTools-accepted terms. Dashboard UI quirk, not Grok Bot agent friction. Bounce. Alert: no.

### Danick 173419 — Cloud Agents by Grok Bot bill Team credits not personal
- Colin: on a team, everything (incl. bot-started cloud agents) bills team seat; promo team cloud credits spend first then seat included. Billing explain, not failure KEEP. Bounce. Alert: no.

### BigFluffyCookie 173450 — tighter OAuth scopes / fixed approval for mutable calls FR. Bounce.

### CSM_Tile / jsolly / Sam_Smith 173412 · 173373 · 173404 — voice remember / iOS webhook URL / Google Chat connector FRs (Colin tracking). Bounce.

### moonj_asmr 173376 — CLI login token + headless “hang” (Colin: stream-json; not Grok Bot agent). Bounce.

### Phone_Macro 173428 — “lied because of ego” confabulation (deanrie). Bounce.

### Paul_Zapata 172862 — Delilah restore still open (no new staff today). Soft don’t-Reset reinforce. Alert: no.

### Joe_Levy1 173037 — computer-use stall follow-up + request id (standing mid-run ping; do not re-KEEP). Bounce.

### warpdev 172343 — Backup not ready; Colin: fresh empty computer only option (huge Sep19 backup). Soft standing Backup/Reset. Alert: no.

### Meetups 173296–173299 / 173329–173331 / 173396–173397 — events only. Bounce.

### Sep 30 KEEP already logged (do not re-KEEP): Wes_Anderson 173321 · Todd_Cunningham 173319.

### Sep 29 overflow already logged (do not re-KEEP as NEW): Emanuelle 173354 · Lashawn was overflow → upgraded KEEP today · TG_Promo 173363 · mr.ukie 173356 · Hip_Hoy 173314 · benum 173333 · pdfer 173349 · znuttyone 173357.

## Standing kills reinforce (footer, not KEEP)
- Free-plan≡no-access / don’t Recover without access (173460 Galaxy meter teach) · 1Password family (173365 false-Filled KEEP; 173423 Google-popup overflow; do not re-alert Noah1) · first-init incomplete (173434) · multi-bot Chief one-way (173356) · computer-use don’t-ping (173037 follow-up) · Backup-not-ready / don’t-Reset (172343 · 172862) · Gmail redirects / screenshot→computer-use (Sep 30 KEEP — do not re-alert)

## New standing-kill text (add to footer if packet accepts KEEP)
- **Shared 1Password autofill can show Filled while password stays empty (Instagram/Letterboxd etc.): page rejects fill → bot clears password for security; card still says Filled; use secure in-chat login form or take over once and hand back** (from 173365)
- **Grok Bot Galaxy / promo credit is a fixed grant tracked separately from the Weekly Usage bar — bar can stay 0% while grant burns; without access bots are hidden not deleted; restore access (trial/plan/SuperGrok), fully quit+reopen; don’t Recover/Reset/recreate** (from 173460)

## Method notes
- Fetched tag latest + page=1; search after:2026-09-29 and after:2026-09-30; keyword friction batch — first pass 429 on invoice/Gmail/attachment/Recover/1Password/browser; retried OK (invoice+Gmail recovered; attachment/Recover/1Password/browser OK).
- Fully read 18+ NEW/active topics into forum1001/{id}.json + .md (incl. bumped Sep29 overflow with new staff).
- Banked KEEP 173365 + 173460.
- Skipped re-KEEP Wes_Anderson 173321 / Todd_Cunningham 173319 / Ajay_Rao 173176 / WGG 173187 / hyper_core 173206 / Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859 / Chexander 172715 / GFP 171703.
- seen-forum-ids.txt: 376 → 398 (Sep29+ surface ids appended, sorted unique).

FAILURE_COUNT=2
alert=no
