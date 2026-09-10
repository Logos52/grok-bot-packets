# Field Grok Bot failure hunt · packet 2026-09-10 (Thursday)
Cutoff: after ~2026-09-09 00:00 UTC (post Wednesday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+order:latest`. Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Wes_Anderson 171029 (Desktop reconnect secrets — ALERTED yesterday), ellisfan 171008, oubeichen 170989 (overflow). Prior: Human_111425250 170869, Archit 170899, jsolly 170901/170727, Jojo1 170809, TheAviv 170816, noname 170736, Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710, andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, Effective_Autism 170819 (+ URLs in scratch-seen-urls.txt).

## KEEP candidates (3)

### KEEP 1 — Charles_Roe · 125 GB workspace bricks restore → Connecting forever
- url: https://forum.cursor.com/t/can-t-use-grok-bot-ios-app/171078
- date: 2026-09-08 17:57 UTC (00:57 ICT 9 Sep); **NEW staff diagnosis** Colin 2026-09-09 15:33 UTC (22:33 ICT 9 Sep) — was thin can’t-reach bounce in yesterday’s scratch before this post
- tags: coverage-ceiling, persistent-computer, killed-claim
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·coverage-ceiling·persistent-computer] score=10 | Charles_Roe | iOS Grok Bot stuck “Connecting to your computer…” → “Something went wrong”. Reinstall/Recover/Reset don’t help. Staff deanrie: not phone/network. Staff **Colin**: Agent Computer holds **~125 GB** (large videos in workspace); **restore runs out of space** before last files finish → app never past Connecting. Staff **cannot surgically delete** individual files; short-term only option is **hard reset** (loses existing bots). OP wants bots kept, waiting for eng space free. Killed: don’t stash huge media/downloads on the shared Agent Computer — workspace bloat can brick every client (iOS/desktop) until hard reset. Alert: **yes** — first-party “what Bot may hold” gate; paste teach-once into Field/tutor bots that download video/audio corpora this week (cap workspace media; off-box archive).
- staff: deanrie 2026-09-08 18:29 UTC (tracking; asked about large files); Colin 2026-09-09 15:33 UTC — 125 GB restore OOS; no surgical delete; hard reset = lose bots.
- siblings: Benjamin_Barber 170689 (graphrag RAM OOM bricks VM — coverage-ceiling cousin); dual-computer can’t-reach wave (costume only — this is distinct disk/restore mechanism).
- bank: raw/ai/2026-09-10-charles-roe-cant-use-grok-bot-ios-app.md

### KEEP 2 — KishoreKV · Routines refuse to fire on SuperGrok path (Cursor Start)
- url: https://forum.cursor.com/t/bot-routines-refuse-to-fire/171173
- date: 2026-09-07 11:47 UTC (18:47 ICT 7 Sep); staff clarification 2026-09-09 14:56 UTC (21:56 ICT 9 Sep)
- tags: quiet-when-nothing, human-gate, killed-claim
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·quiet-when-nothing·human-gate] score=10 | KishoreKV | Routines never fire across Windows/macOS/iOS despite resets/replacements on 0.44.0. Staff **Colin** (split from other thread): Grok Bot access via **linked SuperGrok** while Cursor plan is **Start** — **routines are the one Grok Bot feature that checks the Cursor plan**; Start does not include them, so server refuses to schedule no matter how often you reset bot/computer. Fix: move Cursor to **Pro+**; other Grok Bot features keep working. OP: subscribed X Premium+ because both listed Grok Bot; docs didn’t say routines need Cursor Pro. Killed: don’t treat “routines won’t fire” as a computer bug when plan path is SuperGrok+Cursor Start — it’s entitlement, not Reset. Alert: **no** (Wedge on Cursor Ultra path; copyable plan-gate for docs/hygiene, not a this-week Field file/setting change).
- staff: Colin 2026-09-09 14:56 UTC — routines check Cursor plan; Start excluded; Pro+ unblocks.
- siblings: o_Oaii 170358 (routines don’t auto-run — already kept, different surface); oubeichen 170989 (dual-computer duplicate schedules — different).
- bank: raw/ai/2026-09-10-kishorekv-bot-routines-refuse-to-fire-supergrok.md

### KEEP 3 — Teddy1 · New account: Privacy Mode unsaved → Can’t reach / Reset partial-state costume
- url: https://forum.cursor.com/t/grok-bot-macos-persistent-cant-reach-your-computer/171170
- date: 2026-09-09 14:41 UTC (21:41 ICT 9 Sep)
- tags: human-gate, killed-claim
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·killed-claim·human-gate] score=9 | Teddy1 | Brand-new account: Grok Bot macOS+iOS stuck Connecting; Retry useless; Recover/Reset → “partial state”. Not VPN/browser/firewall. Staff **deanrie**: on a **new account the Privacy Mode choice hasn’t been explicitly saved**; Grok Bot needs that saved choice to connect — until set, every attempt rejected and Retry/Recover/Reset can’t advance. Unblock: cursor.com/dashboard → Settings → Privacy → select **Privacy Mode** (not Legacy), data sharing off, confirm → Cmd+Q quit → reopen (OP: step 6 worked). Killed: “Can’t reach / partial state” on a fresh account can be **Privacy Mode not persisted**, not a broken computer. Alert: **no** (onboarding-only; Wedge already configured).
- staff: deanrie 2026-09-09 15:13 UTC — Privacy Mode must be saved; known tracking; step list.
- siblings: jumpsuitgroup 170486 (false Legacy privacy gate on Cloud Agent — related privacy surface, different product path); Loni_Riw 171004 trial-ended costume.
- bank: raw/ai/2026-09-10-teddy1-grok-bot-macos-persistent-cant-reach.md

## BOUNCE

### Auth-error wave (signedIn:true costume — server session; logout/reinstall often useless)
- oyagen 171115 / Lit_Sky 171164 / Channels_Cintara 171107 cluster — “Authentication error / try logging out” while UI shows signed in; kevinn/Colin: backend machine reset or knobs; many me-too on Win/mac 0.44–0.47. Strengthens andyfraussen/_Remi session-costume path; **not a new portable gate** beyond “auth error ≠ local logout fix”. https://forum.cursor.com/t/grok-bot-windows-0-44-0-authentication-error-persists-after-update-logout-login-and-cache-clear/171115

### Can’t-reach / Bot-failed-to-respond / partial-state ops (no new mechanism vs Wed dual-computer + rebuild cluster)
- robobobo 171186 · smolen2011 171177 (kevinn: regional ToS/availability — not FAILURES-portable) · ethan-pacifica 171126 (deanrie: wrong account / expired sub) · Gideon 171091 · Greg_Tritthart 171087 · Philippe_Wong 171058 (kevinn rebuilt) · bit0rbit 170912 · Ricard1 170719 (mohitjain: hold Reset) · David_Stredansky 170957 (self-healed) · Charles_Roe pre-diagnosis thin bounce superseded by KEEP 1

### OAuth / connector — thin or vendor / already-covered siblings
- BG1 171111 Robinhood MCP — deanrie: grokbot:// callback retired Sep 7 (https://www.cursor.com/agents/…); auth arrived **17 min late** vs ~15 min window; retry Allow quickly or connect once from desktop. Portable OAuth-timeout teach is real but **vendor-specific + FR/workaround**; score ~8 overflow only — prefer not to spend FAILURES slot vs 171078/171173/171170. https://forum.cursor.com/t/grok-bot-robinhood-agentic-trading-mcp-oauth-fails-after-allow-grokbot-callback-oauth-error/171111
- brianrobt 171183 Todoist Authenticate never opens browser (toast + AuthenticateMcpServer “unreachable”) — kevinn: **known tracking**, uninstall won’t help; distinct from jsolly 170895 iOS PKCE first-attempt. Mechanism thin (no root cause yet); bounce / watch. https://forum.cursor.com/t/grok-bot-desktop-todoist-authenticate-never-opens-browser-unreachable-toast-only-t-f50688/171183
- jsolly 170898 GitHub Authenticate “no sign-in link” — mohitjain: labeling/PAT Setup Values, not browser OAuth (bounced Wed)

### Version-skew / local-exec (already covered)
- Maaz_Kazi 171169 / 168548 — cloud computer on older internal build; Update greyed → Colin backend knobs; local-exec restored. Same version-skew ops as Wed bounce of 168548.

### Thin / FR / quota / events
- Yaddu 171187 job-search tips · Jos_Osei 171154 release-notes FR · 171109 android small bug · 171108 Clean your Grok · 170875/170835 quota · 170971 Alt+Tab bots vanished (no new staff)

### Already-kept (window)
- Wes_Anderson 171029 · ellisfan 171008 · oubeichen 170989
- Human_111425250 170869 · Archit 170899 · jsolly 170901/170727
- Jojo1 170809 · TheAviv 170816 · noname 170736 · Effective_Autism 170819
- Jarri81 170683 · Winvicta 170691 · Benjamin_Barber 170689 · StefanZ 170710
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` page 0 + page 1; `search.json?q=Grok+Bot+order:latest` → `/workspace/field/forum0910/`
- Priority topic IDs fetched (24): 171183, 171115, 171111, 171177, 171078, 170957, 171164, 171173, 171169, 171170, 171126, 171186, 171091, 171087, 170912, 171187, 171154, 171058, 170898, 170719, 168548, 170875, 171107, 171109
- Slug truncations: first curl for 171183/171115/171111/171177 returned empty (short slug); refetched with full slug from feed JSON
- Public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior entries for 171078/171173/171170
- bank.py deposited all 3 KEEP raws + refreshed INDEX (187 items)

## Bank deposits
- KEEP: `raw/ai/2026-09-10-charles-roe-cant-use-grok-bot-ios-app.md` ← 171078
- KEEP: `raw/ai/2026-09-10-kishorekv-bot-routines-refuse-to-fire-supergrok.md` ← 171173
- KEEP: `raw/ai/2026-09-10-teddy1-grok-bot-macos-persistent-cant-reach.md` ← 171170

## Packet recommendation
Keep count: **3** — Charles_Roe 171078, KishoreKV 171173, Teddy1 171170. Cap ~2–3 FAILURES (compiler total cap 5 with education). Prefer **171078 + 171173** if cut to 2 (distinct gates: workspace coverage-ceiling vs SuperGrok/Cursor routines entitlement); 171170 is strong human-gate for new-account Privacy Mode (overflow if room). **Alert: yes** (Charles_Roe only — don’t let Field/tutor bots fill Agent Computer with large media; restore cannot surgically delete; hard reset loses bots). Do **not** re-alert Wes_Anderson 171029 secrets or CallDynamicTool 170869. Overflow watch: BG1 171111 OAuth 15-min window; brianrobt 171183 Todoist Authenticate toast (known, thin). Auth-error 171115/171164 = session costume ops. No packet file written. field-seen.json not edited.
