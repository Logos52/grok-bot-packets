# Field Grok Bot failure hunt · packet 2026-09-30 (Wednesday Asia/Taipei cron; box America/New_York)
Cutoff: after Sep 29 KEEP Ajay_Rao 173176, WGG 173187, overflow hyper_core 173206 — **do not re-keep**. Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-28` (+ `after:2026-09-29`) + keyword friction (stuck, routines, plugin, Connected, Always allow, Auto-review, local execution, Reset, reconnecting, computer-use, image, failed to respond, billing, invoice, attachment, Recover). Category `c/grok-bot/l/latest.json` / `c/grok-bot/33.json` skipped (prior 404). Public, no login. No Firecrawl. Scratch for packet compiler. Do **not** write field/latest.md from this hunt.

Already kept / standing (skipped / bounce only): Sep 29 KEEP Ajay_Rao 173176 (unpaid invoice silence). Sep 29 KEEP WGG 173187 (attachments need computer). Sep 29 overflow hyper_core 173206 (Ahrefs rate-limit). Sep 28 KEEP Noah1 173142 (1Password long website URL). Sep 28 KEEP Benahordure 173116 (iOS Apple SSO → magic-link). Sep 27 KEEP Tibetan95380 173045 (wide-image pixel dims). Sep 27 KEEP Joe_Levy1 173037 (computer-use mid-run ping). Sep 26 KEEP jsolly 173019 (Plugin Connected = first connector only). Fri KEEP TheAviv 172859 (Always-allow = text). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Standing footer: Kaspersky / DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins** / **Plugin Connected = first connector only** / **Wide-image (pixel dims) in chat history kills that chat; Reset/Update won’t fix; new chat same bot** / **Computer-use helper: new message mid-run stops+restarts — wait / don’t ping** / **1Password: one Login website URL >~2000 chars kills whole vault connect (“delivery unknown”); shorten URLs or empty vault→connect→move back; full quit Cmd+Q** / **iOS login: Cursor Apple SSO desktop users — no Sign-in-with-Cursor on iOS (accounts.x.ai only); magic-link to same email** / **Unpaid invoice / failed card → all bots “Bot failed to respond” (computer fine); check cursor.com/dashboard billing; don’t Reset/rebind** / **Chat attachments upload to Grok Bot computer first; text OK + “Will send after reconnecting” / Backup not ready = computer dead; Recover not Reset; full quit** / **Ahrefs marketplace: Authenticate / load fails under Ahrefs rate-limit (429 / SyntaxError / Failed to load connector); reinstall/retry won’t fix**. Do not re-alert footer list (+ Ajay_Rao 173176 / WGG 173187 / hyper_core 173206 / Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859 / Wes_Anderson 171029).

## KEEP candidates (2) — recommend for packet

### KEEP 1 — Wes_Anderson · Gmail connector wraps every link in google.com/url redirects
- url: https://forum.cursor.com/t/grok-bot-gmail-connector-user-gmail-rewrites-every-link-into-google-com-url-redirects-on-create-draft-and-send-message/173321
- date: OP 2026-09-29 12:41 UTC; Colin 15:22 UTC
- tags: teach-once, human-gate, killed-claim, plugins, gmail
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·human-gate·killed-claim] score=9 | Wes_Anderson | **user-Gmail** `create_draft` / `send_message`: every URL (plain or HTML) is saved/sent as a **google.com/url** redirect — visible text + href both wrong; placeholders break; same mailbox composed in Gmail UI is fine. **Colin: known/tracked — happens in the Gmail connection itself, not how the bot writes.** Workaround: have the bot write text in chat (or draft without links) and **paste/add links yourself in Gmail before send**; avoid bot `send_message` for link-containing mail until fixed. Alert: **no** (teach/footer; only matters if Wedge ships customer/tutor email with links via connector this week).
- staff: Colin
- bank: raw/ai/2026-09-29-wes-anderson-grok-bot-gmail-connector-rewrites-every.md
- topic json/md: forum0930/173321.json · 173321.md

### KEEP 2 — Todd_Cunningham · “no browser control” — screenshot is view-only; force computer-use helper
- url: https://forum.cursor.com/t/loss-of-browser-control/173319
- date: OP 2026-09-29 12:34 UTC; Colin 15:22 UTC
- tags: teach-once, human-gate, killed-claim, computer-use
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·human-gate·killed-claim] score=9 | Todd_Cunningham | Bot can **screenshot** desktop but claims it **can’t click/type/browse**; Update + full restart didn’t restore “browser control.” **Colin: screenshot tool is view-only on purpose; click/type/browse go through a background computer-use helper** — helper still healthy on account, but bot stopped using it (often a saved note saying tools are gone). Fix: send exactly *“Launch a computer-use helper (Task tool, computerUse) to open https://www.google.com … Don’t reply until it finishes.”* Wait — don’t ping mid-run. Then tell bot to always hand browser work to computer-use helper and **remove any saved note** denying browser control. Distinct from standing **mid-run ping kills computer-use** (Joe_Levy1) and computer-view-OK=backend-unreachable. Alert: **no** (teach/footer).
- staff: Colin
- bank: raw/ai/2026-09-29-todd-cunningham-loss-of-browser-control-screenshot-ok.md
- topic json/md: forum0930/173319.json · 173319.md

## OVERFLOW / watch (not packet KEEP)

### Emanuelle 173354 — 1Password optional; takeover for login; service-account rate-limit
- kevinn: skip 1Password — when bot hits login, take over computer (or iPhone app), type password yourself, hand back; session stays signed in. Service-account token step only if you want unattended fill. OP follow-up: fresh token hits **“1password is rate limiting this service account”**. Soft teach beside standing Noah1 URL-length kill; rate-limit on brand-new SA is watch. Alert: no.

### Lashawn_Martin 173365 — Shared 1Password autofill says Filled but password stays empty
- Instagram/Letterboxd: fill card “Filled” / even fill+submit, but only username lands; password empty; Log In disabled. Vault password fine manually. No staff yet. Strong killed-claim shape (false-success autofill). Overflow watch; may upgrade if staff confirms. Alert: no.

### TG_Promo 173363 — GenerateImage aspect_ratio accepted then dropped (always 1280×720 JPEG)
- Sand `createSandGenerateImageService` doesn’t forward aspect_ratio; .png name / JPEG bytes / C2PA “Grok Imagine”. No staff. Soft image-gen watch. Alert: no.

### mr.ukie 173356 — Chief bot not talking to other bots
- One-way: others can message Chief; Chief can’t message out. No staff. Same family as Sep 29 overflow dob93 173238 (self-solved). Soft multi-bot comms watch. Alert: no.

### Hip_Hoy 173314 — stuck >1h, reset doesn’t help
- Topic deleted by author. Bounce. Alert: no.

### benum 173333 — Bot role description missing from info pane (docs say editable)
- Juniya-Sankara: used to work; recent update removed edit field → treat as BUG. No staff. Soft UI-regression watch / FR. Alert: no.

### pdfer 173349 — per-site Route-through-my-computer FR
- kevinn: aware/tracking. FR not failure KEEP. Alert: no.

### znuttyone 173357 — context compaction / clone-replace / per-bot telemetry
- kevinn merged into standing FR 168333. Bounce. Alert: no.

### Paul_Zapata 172862 — deleted bot / first-run after sign-out (Delilah); don’t Reset
- deanrie: bot was deleted Sep 20; computer intact; engineering restore in progress; signing out ≠ delete; deleting in Grok iPhone app does. Account-specific recovery; standing multi-device / don’t-Reset reinforce. Soft watch. Alert: no.

### Meetups 173296–173299 / 173329–173331 — events only. Bounce.

### Older +1 / FR: 171948 Bitwarden native · 170406 Teams→humans · 168333 prune/compact (active FR). Bounce.

### Sep 28 overflow already logged yesterday (do not re-KEEP): jsolly 173208 · Michael_Fischer 173201 · bjohnson1 173273 · Alexander_Hoyos 173229 · Didier_Didier 173218 · sb6666 173268 · Jacob_Martinez 173217 · Capital_EyeMotors 173167 · dob93 173238 · Raymond_Weiss 173242 · Jason_Chollar 173270 · benum 173241 · KevinC1 173205.

## Standing kills reinforce (footer, not KEEP)
- Computer-use mid-run don’t-ping (173319 Colin helper prompt) · 1Password family (173354 takeover + 173365 false-Filled watch; do not re-alert Noah1) · multi-device / don’t-Reset (172862) · Chief↔bots one-way (173356) · unpaid-invoice / attachments / Ahrefs (Sep 29 KEEP — do not re-alert)

## New standing-kill text (add to footer if packet accepts KEEP)
- **Gmail connector (user-Gmail): create_draft/send_message wraps every link in google.com/url redirects; compose/paste links in Gmail UI yourself; don’t bot-send link mail until fixed** (from 173321)
- **“No browser control” while screenshots work: screenshot is view-only; launch computer-use helper (Task/computerUse) and wait; remove saved notes denying browser tools; Update/restart won’t restore** (from 173319)

## Method notes
- Fetched tag latest + page=1; search after:2026-09-28 and after:2026-09-29; keyword friction batch — first pass 429 on invoice/attachment/Recover; retried OK (+ 1Password/Gmail/browser extras). Primary tag+date + keyword files covered Sep29+ surface.
- Fully read 15 NEW/active topics into forum0930/{id}.json + .md; synced missing forum0929 ids into seen-forum-ids.txt.
- Banked KEEP 173321 + 173319.
- Skipped re-KEEP Ajay_Rao 173176 / WGG 173187 / hyper_core 173206 / Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859 / Chexander 172715 / GFP 171703.

FAILURE_COUNT=2
alert=no
