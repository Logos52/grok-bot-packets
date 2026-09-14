# Field Grok Bot failure hunt · packet 2026-09-14 (Monday)
Cutoff: after ~2026-09-13 00:00 UTC (post Sunday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–2 + `search.json?q=Grok+Bot+after:2026-09-12` (+ `after:2026-09-13`, keyword variants). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Sun KEEP jamie_burt 171438 (ENAMETOOLONG sand-client — **Colin Sep 13**: eCryptfs NAME_MAX≈143, not plain Linux 255; reinforcement only, do NOT re-KEEP). Overflow watch was enescanguven 171441 (elevated to KEEP below after Colin staff). Standing skip: Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270, Catty Kaspersky family 171308+, thomas2018 171324 (server-routines), Channels_Cintara Update-Computer auth, Surfshark Temp, session-revoke, F-Secure DeepGuard, Auto-review bind, SuperGrok Start routines, Desktop-secrets overwrite, workspace-media OOS. Overflow watch standing: aiaje Authenticode 171265; y123 VPN 171357 (deanrie Sep 13 permanent-rule reinforce — bounce).

## KEEP candidates (2)

### KEEP 1 — Kin_Su · Client/router DNS SERVFAIL on long `*.cursorvm.com` pod hostname (Reconnecting costume)
- url: https://forum.cursor.com/t/grok-bot-0-47-0-windows-agent-computer-dns-servfail-enotfound-please-rebuild-or-reattach-on-backend/171482
- date: 2026-09-13 09:04 UTC (16:04 ICT 13 Sep); Colin reply 10:01 UTC
- tags: killed-claim, coverage-ceiling, persistent-computer
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·coverage-ceiling] score=9 | Kin_Su | Windows 0.47.0: “trouble connecting” / Reconnecting / “No saved Bots yet”; Network Debugger Computer TLS/health/events fail in 2–3ms; `ENOTFOUND` / router DNS **Server failed** (RT-AC1900P) for long pod hostname `…-pod-….us8.cursorvm.com` while `test123.us8.cursorvm.com` resolves + HTTP 404. OP asked backend rebuild — **wrong**. Colin: VM hostname resolves fine externally (same six addrs as test123); **wildcard** under `us8.cursorvm.com` — no per-computer DNS to rebuild; SERVFAIL is between PC and router/ISP. Teach: `nslookup <pod> 8.8.8.8` then vs router; Manual DNS **1.1.1.1 / 8.8.8.8** + `ipconfig /flushdns`; quit tray → relaunch; router malicious-site / DNS filter can break **long** hostnames. Killed: Reconnecting / can’t-reach / empty roster can be **local DNS**, not a dead box — don’t Reset/Recover chasing it. Siblings same day: TURTLE1 171479 (Colin: Reliance Jio DNS timeout → Reconnecting mid-session); Anmol_Ratan 171514 (deanrie same DNS teach; OP confirmed 1.1.1.1/8.8.8.8 fixed after 2 weeks stuck). Alert: **no** (local network DNS; not a this-week Field file/setting change).
- staff: Colin (mechanism + steps)
- siblings: 171479 TURTLE1; 171514 Anmol_Ratan (confirmed fix). Distinct from Kaspersky TLS MITM / session-revoke / Update-Computer auth.
- bank: raw/ai/2026-09-14-kin-su-grok-bot-0-47-0-windows.md

### KEEP 2 — enescanguven · Secure-card token “Saved” but missing in agent-window shell env (session inheritance)
- url: https://forum.cursor.com/t/token-not-available-in-grok-bot-environment/171441
- date: OP 2026-09-12 16:05 UTC; **Colin 2026-09-13 07:57 UTC** (elevated from Sun overflow)
- tags: coverage-ceiling, human-gate
- score: 8 (portable 4 / evidence 4)
- packet one-liner: [agentic·coverage-ceiling·human-gate] score=8 | enescanguven | Token field UI shows Saved; fresh executor process has no token. Colin: secure card writes to **computer main environment**, but agents in their **own window** start shells from a **separate session** that does not pick up values added after that session started — hence Saved ≠ visible in executor. Known issue (staff-tracked). Workarounds: (1) create **brand-new agent** after save (inherits pre-start env); (2) provide token as **file** on computer (visible to every agent — OP’s GSC pattern). Re-saving into existing agent useless. Distinct from Wes_Anderson Desktop-secrets **overwrite**. Alert: **no** (copyable env-session teach; not a Wedge this-week file/routine change required).
- staff: Colin (root cause + two workarounds)
- siblings: not Wes 171029 / Jeffrey_Nead secrets wipe
- bank: raw/ai/2026-09-14-enescanguven-token-not-available-in-grok-bot.md

## OVERFLOW / watch (not packet KEEP)

### Weekly usage-limit costume (silent bots / no reply; desktop & iOS hide the warning)
- Carlos_Lopez1 171464 https://forum.cursor.com/t/grok-bot-isn-t-responding-in-any-bot/171464 — deanrie: weekly included limit; Windows app doesn’t show warning yet → bots silent; Reset useless/dangerous; Settings > Usage; On-Demand at spending dashboard. Routine toggle locked while silent.
- Rick_Soto 171458 https://forum.cursor.com/t/all-grok-bots-silent-on-ios-agent-computer-visible-but-no-replies/171458 — same limit costume on iOS; VM visible (Instagram open) but reply pipeline dead; don’t Recover/Reset; SuperGrok≠Cursor Pro for Bot usage. Score ~7 portable costume; overflow (billing/UX; education slots preferred). Created just before / on cutoff edge.
- score: ~7 — watch; do not KEEP this packet (cap used by DNS + token)

### aiaje_com Authenticode / y123 VPN (standing overflow)
- aiaje 171265 — no new posts past Colin Sep 11; still overflow.
- y123 171357 — **deanrie 2026-09-13**: permanent rule — bots must not install VPN/proxy or change DNS/network on Agent Computer (self-brick, can’t roll back). Reinforce overflow; do not re-KEEP.

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- jamie_burt 171438 — Colin Sep 13: encoded sand-client names ~140–200 chars; **eCryptfs** caps ~143 (matches ENAMETOOLONG); asks getconf NAME_MAX / mount ecryptfs / df -T. Sun KEEP stands; mechanism refined (encrypted home), not new topic.
- thomas2018 171324 — no new staff past Sat/Sun Mac+mobile; skip.

### Ops / dual-copy / recovery (no new portable gate)
- Kiefer_Menard 171481 — deanrie: shared computer stopped generating replies (screen still visible); Reset (not Update); ops brick.
- OliG 171344 — Colin “restart?”; OP still partial-state after Windows update — ops.
- smolen2011 171177 — bump T-F58206 partial-state; kevinn earlier misread as region/ToS — ops/backend recreate.
- Gideon_H_Guna_e 171091 — still unresolved recovery nag — ops.
- zoe_Joestar 171304 — jadles Sep 13 me-too “icon flashes, no request ID” — thin ops cousin; OP already fixed earlier.
- PrimeSites_Digital 171462 — **topic deleted by author** (created then gone).

### Tips / feature / wrong surface
- Events 171543–171548 — launch nights; skip.
- Imogen 171549 — plugin/bots sort FR.
- verna-stack 171545 — read-only project access FR.
- mohsendev 171540 — context/token accumulation Pro+ question.
- anonix98 171539 — quota explanation tip.
- 171420 notification after leave-app — tip (prior).
- Channels_Cintara / oyagen 171115 — Update-Computer auth me-too wave; standing; skip re-KEEP / skip re-alert.

### Standing / skip list (window mentions)
- Catty/Kaspersky — not re-hit as primary new topic.
- Jason_Chu / Surfshark Temp / F-Secure / session-revoke / Auto-review bind / SuperGrok Start / Desktop-secrets / workspace-media OOS — standing.

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–2 → `/workspace/field/forum0914/`
- Search: `Grok+Bot+after:2026-09-12`, `after:2026-09-13`; variants can’t-reach(0) / unreachable(0) / Reset(0) / webhook(0) / ConnectError(1→171308 standing) / routine / ENAMETOOLONG|sand-client(0) / Kaspersky|antivirus(0) / secrets|Backup(0) / failed to respond(0); `order:latest` empty
- `c/grok-bot/33.json` skipped (invalid category)
- Topics created ≥2026-09-13 00:00 UTC (bugs/friction): **171462** (deleted), **171464**, **171479**, **171481**, **171482**, **171514**, plus tips/FR/events 171539–171549; edge **171458** (Sep 12 23:39)
- Priority topic IDs fetched: 171482, 171479, 171514, 171481, 171464, 171458, 171441, 171462, 171438, 171357, 171324, 171344, 171304, 171177, 171091, 171115, 171265, 171545, 171540, 171539, 171549
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 171482 / 171441 deposit
- bank.py deposited KEEP 1–2; field-seen.json not edited; scratch-seen-urls.txt not edited this turn

## Bank deposits
- KEEP: `raw/ai/2026-09-14-kin-su-grok-bot-0-47-0-windows.md` ← 171482
- KEEP: `raw/ai/2026-09-14-enescanguven-token-not-available-in-grok-bot.md` ← 171441

## Packet recommendation
Keep count: **2** (cap ≤2; education takes other slots). Prefer **Kin_Su 171482** (DNS SERVFAIL / local-resolver killed-claim) + **enescanguven 171441** (secure-card token session inheritance — Sun overflow elevated with Colin). Overflow watch: weekly-limit silent-bots costume (171464/171458); aiaje Authenticode; y123 VPN rule. Reinforced but do not re-KEEP: jamie_burt 171438 (eCryptfs NAME_MAX). **Alert: none** (do not re-alert standing list; DNS is local network; token gap is copyable teach not this-week Field path). No packet file written. field-seen.json not edited.
