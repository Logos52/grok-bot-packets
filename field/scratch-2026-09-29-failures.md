# Field Grok Bot failure hunt · packet 2026-09-29 (Tuesday Asia/Taipei cron; box America/New_York)
Cutoff: after Sep 28 KEEP Noah1 173142 and Benahordure 173116 — **do not re-keep**. Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-27` (+ `after:2026-09-28`) + keyword friction (stuck, routines, plugin, Connected, Always allow, Auto-review, local execution, Reset, reconnecting, computer-use, image, failed to respond, 1password, iOS, magic link). Category `c/grok-bot/l/latest.json` / `c/grok-bot/33.json` skipped (prior 404). Public, no login. No Firecrawl. Scratch for packet compiler. Do **not** write field/latest.md from this hunt.

Already kept / standing (skipped / bounce only): Sep 28 KEEP Noah1 173142 (1Password long website URL). Sep 28 KEEP Benahordure 173116 (iOS Apple SSO → magic-link). Sep 27 KEEP Tibetan95380 173045 (wide-image pixel dims). Sep 27 KEEP Joe_Levy1 173037 (computer-use mid-run ping). Sep 26 KEEP jsolly 173019 (Plugin Connected = first connector only). Fri KEEP TheAviv 172859 (Always-allow = text). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Standing footer: Kaspersky / DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins** / **Plugin Connected = first connector only** / **Wide-image (pixel dims) in chat history kills that chat; Reset/Update won’t fix; new chat same bot** / **Computer-use helper: new message mid-run stops+restarts — wait / don’t ping** / **1Password: one Login website URL >~2000 chars kills whole vault connect (“delivery unknown”); shorten URLs or empty vault→connect→move back; full quit Cmd+Q** / **iOS login: Cursor Apple SSO desktop users — no Sign-in-with-Cursor on iOS (accounts.x.ai only); magic-link to same email**. Do not re-alert footer list (+ Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859 / Wes_Anderson 171029).

## KEEP candidates (3) — recommend for packet

### KEEP 1 — Ajay_Rao · unpaid invoice → all bots “Bot failed to respond” (computer fine)
- url: https://forum.cursor.com/t/grok-bot-bot-failed-to-respond-after-update-and-reset-please-rebind-agent-computer/173176
- date: OP 2026-09-28 05:03 UTC; deanrie 05:35 UTC
- tags: teach-once, human-gate, killed-claim, billing
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·human-gate·killed-claim] score=9 | Ajay_Rao | All bots silent with generic **“Bot failed to respond”** after update/reset/new-chat; iOS + Mac. **deanrie: agent computer is fine — when every bot stops at once and Reset/Update/new chat don’t help, check account billing first.** Unpaid invoice / failed card **pauses bot replies** until paid; app does **not** show a payment message. Check cursor.com/dashboard billing (same account); after pay, replies usually return in a couple of minutes; else hi@cursor.com. Do **not** Reset/rebind. Distinct from standing Reset-fail/partial and one-bot silent (this is account-wide + billing-shaped). Alert: **no** (teach/footer; no this-week Field Settings change unless Wedge has an unpaid Cursor invoice).
- staff: deanrie
- bank: raw/ai/2026-09-28-ajay-rao-grok-bot-bot-failed-to-respond.md
- topic json/md: forum0929/173176.json · 173176.md

### KEEP 2 — WGG · chat attachments need computer; text OK + “Will send after reconnecting” = box dead
- url: https://forum.cursor.com/t/grok-bot-chat-image-file-attachments-fail-to-send-3-pcs-since-2026-09-26-text-ok/173187
- date: OP 2026-09-28 06:14 UTC; mohitjain 08:50 UTC
- tags: teach-once, human-gate, killed-claim, media
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·human-gate·killed-claim] score=9 | WGG | Pasted/dragged **images/files fail to send** (“Will send after reconnecting” / network error) while **plain text still works**; path-based local read still OK; 3 PCs; Update didn’t help; sidebar **Backup not ready**. **mohitjain: text goes straight to servers; attachments upload to the Grok Bot computer first** — when the computer dies, attachments stick and Update stalls at Backup not ready. Staff rebuilt from snapshot; full quit (not just close) → reopen → reconnect; post-death computer changes may be lost. If it recurs: **Recover (Settings → Updates), not Reset**. Distinct from standing **Wide-image kills chat** (history pixel dims) and computer-view-OK=backend-unreachable. Alert: **no** (teach/footer).
- staff: mohitjain
- bank: raw/ai/2026-09-28-wgg-mohitjain-grok-bot-chat-image-file-attachments.md
- topic json/md: forum0929/173187.json · 173187.md

### KEEP 3 — hyper_core · Ahrefs Authenticate rate-limited (429 / SyntaxError); can’t fix client-side
- url: https://forum.cursor.com/t/grokbot-ahref-connector-rate-limited/173206
- date: OP 2026-09-28 11:01 UTC; Colin 13:18 UTC
- tags: teach-once, plugins, killed-claim
- score: **7** (portable 4 / evidence 3)
- packet one-liner: [agentic·teach-once·plugins·killed-claim] score=7 | hyper_core | Marketplace **Ahrefs** connector: press Authenticate → immediate fail with **429 rate-limit** text wrapped as **SyntaxError**. **Colin: known/tracked — Ahrefs rate-limits Grok Bot’s pre-sign-in setup requests; not fixable by reinstall/retry/another account.** Same family as older jsolly **170891** “Failed to load connector” (Colin Sep 7: same rate-limit root). Wait for product backoff/retry change. Alert: **no** (plugin footer teach; off Field education lane unless Wedge adds Ahrefs).
- staff: Colin
- bank: raw/ai/2026-09-28-hyper-core-grokbot-ahrefs-connector-authenticate-rate-limited.md
- topic json/md: forum0929/173206.json · 173206.md (related dump: 170891.json · 170891.md)

## OVERFLOW / watch (not packet KEEP)

### jsolly 173208 — Inkbox MCP “connected” + 51 tools but agent “MCP server not found”
- Colin: transient server-side — scheduled/background tasks started without connector access (~Sep 28 early ET); status stayed Connected; RestartMcpServers useless; fix ~6:15 AM ET. Self-healed. Incident, not lasting gate. Soft watch: Connected UI can lie during backend connector-access outages. Alert: no.

### Michael_Fischer 173201 — cache TTL ~5 min burning quota (~12x)
- Usage-export claim: after 2026-09-24 06:03 UTC, gaps >~5 min become cold cache-write of full context. No staff. Strong evidence shape but unverified. Overflow watch. Alert: no.

### bjohnson1 173273 — mcpServers optional field ignored (needs mcp.json name)
- Marketplace plugin with non-`mcp.json` via manifest `mcpServers` fails auth on Grok Bot + cloud agents; local agents OK. Workaround: rename to mcp.json. No staff. Soft plugin-author watch. Alert: no.

### Alexander_Hoyos 173229 — Reset failed / partial state
- Colin recovered box. Standing Reset-fail/partial ≡ no access reinforce. Alert: no.

### Didier_Didier 173218 — one bot stuck “Working”
- Colin: server-side stall; cleared; nothing user did. Standing one-bot silent reinforce. Alert: no.

### sb6666 173268 / chrisoh-family — stuck 43% Transferring
- Standing Update/Reset hung 43% + nhog don’t-Reset reinforce. Alert: no.

### Ajay-adjacent Jacob_Martinez 173217 — Bot failed to respond; Reset didn’t help; later “solved”
- No staff; self-resolved. Possible billing/transient. Bounce beside KEEP 173176. Alert: no.

### Ajay_Rao-pattern Ajay already KEEP; Capital_EyeMotors 173167 — scheduled Computer update missing
- mohitjain: schedule not on account yet; docs ahead of product; Automatic Updates = client only. FR/docs gap, not failure KEEP. Alert: no.

### David_Branca 173258 — microsoftTeams routine never fires
- Topic deleted by author. Standing server-routines reinforce. Alert: no.

### dob93 173238 — Chief of Staff can’t message other bots
- OP self-solved; ticket closable. Soft multi-bot comms watch. Alert: no.

### Raymond_Weiss 173242 — “incompetent today” / window refresh
- Anecdote; no staff; no portable gate. Bounce. Alert: no.

### Jason_Chollar 173270 — FR usage-stats connector / benum 173241 voice↔chat / KevinC1 173205 per-device hide
- Feature requests. Bounce. Alert: no.

### Meetup 173194 Seattle — event only. Bounce.

### Older newly-dumped (not Sep28+ KEEP): 170891 Ahrefs (folded into KEEP 3) · 172953 re-add same MCP name edits in place (Colin teach; soft) · 172524 1Password vault-only FR (do not re-alert Noah1) · 172502 Windows 0x0 window + Chromium KB (Colin) · 172380 iOS Vercel sheet “Added” force-quit · 168180 ExternalShell vs Always-allow (standing Always-allow family) · 171965 model-provider content filter (deanrie; IDE-primary) · 168075 privacy Cursor-account (mohitjain)

## Standing kills reinforce (footer, not KEEP)
- Reset-fail/partial ≡ no access (173229 Colin recover) · Update/Reset hung 43% (173268) · one-bot silent / Working stall server-side (173218 Colin) · server-routines (173258 deleted) · Ahrefs rate-limit family (170891+173206 → KEEP 3) · Backup not ready + attachment path (173187 → KEEP 2) · billing silence (173176 → KEEP 1)

## New standing-kill text (add to footer if packet accepts KEEP)
- **Unpaid invoice / failed card → all bots “Bot failed to respond” (computer fine); check cursor.com/dashboard billing; don’t Reset/rebind** (from 173176)
- **Chat attachments upload to Grok Bot computer first; text bypasses — text OK + “Will send after reconnecting” / Backup not ready = computer dead; Recover not Reset; full quit** (from 173187)
- **Ahrefs marketplace: Authenticate / load fails under Ahrefs rate-limit (429 / SyntaxError / Failed to load connector); reinstall/retry won’t fix** (from 173206 / 170891)

## Method notes
- Fetched tag latest + page=1; search after:2026-09-27 and after:2026-09-28; keyword friction (stuck/routines/plugin/Connected/Always+allow/Auto-review/local+execution/Reset/reconnecting/computer-use/image/failed+to+respond/1password) — iOS + magic-link + several dated extras 429 after burst; primary tag+date + successful keyword files covered Sep28+ surface.
- Fully read 45 NEW topics into forum0929/{id}.json + .md; appended ids to seen-forum-ids.txt (351→396).
- Banked KEEP 173176 + 173187 + 173206.
- Skipped re-KEEP Noah1 173142 / Benahordure 173116 / Tibetan95380 173045 / Joe_Levy1 173037 / jsolly 173019 / TheAviv 172859.

FAILURE_COUNT=3
alert=no
