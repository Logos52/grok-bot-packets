# Field Grok Bot failure hunt · packet 2026-09-13 (Sunday)
Cutoff: after ~2026-09-12 00:00 UTC (post Saturday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–2 + `search.json?q=Grok+Bot+after:2026-09-11` (+ keyword variants). Category `c/grok-bot/33.json` → error (no such category id). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Sat KEEP Catty 171308 (Kaspersky TLS MITM ConnectError.Internal) + siblings Raul_Martins 171283 / Pat4 171358 / Mumje me-too; thomas2018 171324 (server-routines webhook credential UI gap — **new Sep 12 staff confirm Mac+mobile same**); aiaje_com 171265 Authenticode (overflow); y123 171357 Agent-Computer VPN self-brick (overflow). Friday+: Jason_Chu 171219, ReinerKuestner 171270 (Bot name>255 as unreachable), Channels_Cintara 171107 (Update Computer auth). Jeffrey_Nead 171280 = Wes secrets sibling — bounce only. Do NOT re-alert: Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270. Standing kills: Auto-review bind, Surfshark Temp 10s, session-revoke, F-Secure DeepGuard, Name>255 (bot-name), workspace-media OOS, SuperGrok/Cursor Start routines, Desktop-secrets overwrite, Update-Computer auth costume.

## KEEP candidates (1)

### KEEP 1 — jamie_burt · Linux ENAMETOOLONG on `sand-client-<huge token>` filename (first-time setup dies locally)
- url: https://forum.cursor.com/t/grok-bot-0-47-0-on-ubuntu-24-04-first-time-setup-fails-with-enametoolong-writing-sand-client-huge-token/171438
- date: 2026-09-12 15:37 UTC (22:37 ICT 12 Sep); OP-only as of hunt (no staff yet)
- tags: killed-claim, coverage-ceiling, persistent-computer
- score: 8 (portable 5 / evidence 3)
- packet one-liner: [agentic·killed-claim·coverage-ceiling] score=8 | jamie_burt | Ubuntu 24.04 grok-bot 0.47.0 amd64 first-time setup after browser Auth: “Grok Bot couldn’t finish setting up” / `edge/handler-failed: ENAMETOOLONG: name too long, open ‘/home/…/.config/Grok Bot/sand-client-<very long token>’`. Last path component > Linux **NAME_MAX 255**; client uses long session/device token as **filename**. Dies on local `open()`, **not** on reaching Agent Computer. Config dir has space (`Grok Bot`); Try again useless; Cursor IDE fine. OP teach: hash id for basename or write token as file contents under `sand-client/<short-id>`. Killed: ENAMETOOLONG / “couldn’t finish setting up” can be **local client token-as-filename**, not a dead box — don’t Reset/Recover Agent Computer chasing first-bot setup. Distinct from ReinerKuestner 171270 (**Bot name** >255 reported as can’t-reach) — same 255-byte family, different surface (filesystem basename vs bot display name). Alert: **no** (Linux desktop client packaging; not a this-week Field file/setting change).
- staff: none yet (watch for deanrie/kevinn).
- siblings: ReinerKuestner 171270 (bot-name>255 → unreachable costume — standing Name>255; do not re-KEEP/re-alert). Not Kaspersky/AV.
- bank: raw/ai/2026-09-13-jamie-burt-grok-bot-0-47-0-on.md

## OVERFLOW / watch (not packet KEEP)

### enescanguven · Token field “saved” but missing in executor env (file workaround)
- url: https://forum.cursor.com/t/token-not-available-in-grok-bot-environment/171441
- date: 2026-09-12 16:05 UTC; OP-only; OS form says iOS vs version darwin — thin
- tags: coverage-ceiling, human-gate
- score: ~6 (portable 3 / evidence 2) — below staff KEEP bar; overflow only
- one-liner: Setup/token UI shows saved; fresh executor process has no token; workaround = provide as file (like GSC). Don’t trust UI “saved” for env injection. Distinct from Wes_Anderson Desktop-secrets **overwrite** (do not re-alert). No staff.
- bank: not deposited (not KEEP)

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- thomas2018 171324 — **deanrie 2026-09-12 18:30 UTC**: not Windows-only; Mac + mobile same; server-stored routines; clients don’t fetch webhook URL/key/header; no ETA; recreating useless. Me-toos: phonebooth (Agent Mail push), Fern (Mac+mobile), Robby_Grossman. OP tip: localhost gateway `:1340` (don’t expose WAN). Sat KEEP stands; new staff quote is reinforcement only.
- Catty/Kaspersky family — Mumje on Pat4 171358 (“god damn kaspersky”); glittle/RoamPT already bounced Sat.
- Channels_Cintara / Update Computer auth — oyagen 171115 still me-too wave (usmxaxn, Pomme Sep 12); Josh2/Paul_Anderson: Settings > Updates > Update Grok Bot’s Computer. Nikita_Chirkin separated by deanrie (sign-in never completes — backend, not Update-Computer). Skip re-KEEP / skip re-alert.

### Ops / dual-copy / recovery (no new portable gate)
- Mario_Murgado_Jr on Diazb123 170915 — Sep 12 “Bot failed to respond” all bots desktop+mobile; Network Debugger green; Settings “Backup not ready”; asks recovery list — dual-copy/backend ops (mohitjain restored earlier cohort Sep 11).
- OliG 171344 — Recover+Reset both fail “partial state” after Windows update; bots visible, computer inaccessible — ops, no staff mechanism yet.
- JobJet 171339 — self-solved: free trial burned in ~45 min; blue bar ambiguous 100% left vs used — quota/UX hygiene, not FAILURES mechanism.
- Altair_Beterelli_Gon 171393 — “resolved… antivirus” thin, no portable teach (Esteban1 cousin).
- robobobo 171186 — bradandhaze Mac me-too emailing 4 days — ops; Kaspersky siblings already under Catty.
- Gideon_H_Guna_e 171091 — still unresolved recovery nag — ops.
- zoe_Joestar 171304 — no new in-window staff.

### Wrong product / tips / standing kills
- Em_Strange 171376 — Cursor IDE 3.20 login / ECONNRESET / Portmaster·HTTP/2 (deanrie) — **not Grok Bot**.
- Kyles_Cousin 171281 — RPM download page stale filenames; kevinn gave direct 0.47.0 links + yumrepo — install docs, not FAILURES.
- 171420 notification after leave-app — tip.
- 171404 “stop the spam” — tip.
- Effective_Autism 170819 — Auto-review bind; deanrie Sep 12 clarifies `../`-leading “relative” python still binds as interpreter; bare relative + abs script path works — **standing Auto-review bind**; skip re-KEEP.
- HeyHeathbar 169592 — X plugin OAuth still broken; Tom_Anderson bump — standing X MCP; skip.
- 170358 routines schedule — Andrew_Simard webhook ping workaround; already seen URL.

### Standing / skip list (window mentions)
- ReinerKuestner 171270 Name>255 bot-name — standing; jamie is **cousin not clone** (kept above as distinct filename gate).
- Jason_Chu / Jarri81 AV Temp — not re-hit as primary.
- Wes_Anderson / Jeffrey_Nead secrets — bounce only; enescanguven overflow not Wes overwrite.

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–2 → `/workspace/field/forum0913/`
- Search: `Grok+Bot+after:2026-09-11`, `order:latest`, `after:2026-09-12`; variants can’t-reach / unreachable / Reset(0) / webhook(0) / ConnectError / routine / partial state / Kaspersky|antivirus / ENAMETOOLONG / sand-client / Backup not ready / failed to respond(0) / secrets(0)
- `c/grok-bot/33.json` → `errors` / invalid category
- Topics created ≥2026-09-12: **171441, 171438, 171420, 171404** only (thin Sunday window)
- Priority topic IDs fetched (~24): 171438, 171441, 171376, 171115(+extra posts), 170915, 171344, 171339, 171393, 169592, 171281, 170819, 171186, 171324, 171384, 171420, 170358, 171304, 171270, 171091, 170509, 171107, 171265, 171358, 171357
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 171438
- bank.py deposited KEEP 1; field-seen.json not edited; scratch-seen-urls.txt not edited this turn

## Bank deposits
- KEEP: `raw/ai/2026-09-13-jamie-burt-grok-bot-0-47-0-on.md` ← 171438

## Packet recommendation
Keep count: **1** (cap ≤2; education takes other slots). Prefer **jamie_burt 171438** only. Overflow watch: enescanguven 171441 token-env gap (thin, no staff). Reinforced but do not re-KEEP: thomas2018 171324 (deanrie Mac+mobile confirm). **Alert: none** (do not re-alert Charles_Roe, Wes_Anderson, CallDynamicTool, Jason_Chu, ReinerKuestner; jamie is Linux client filename, not Wedge this-week path). Sparse Sep 12–13 morning window: only two new grok-bot bug topics; rest me-toos/ops/standing. No packet file written. field-seen.json not edited.
