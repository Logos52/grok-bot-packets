# Field Grok Bot failure hunt · packet 2026-09-15 (Tuesday)
Cutoff: after ~2026-09-14 00:00 UTC (post Monday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–2 + `search.json?q=Grok+Bot+after:2026-09-13` (+ `after:2026-09-14`, keyword variants). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Mon KEEP Kin_Su 171482 (DNS SERVFAIL — bounce only); Mon KEEP enescanguven 171441 (secure-card env session — bounce only); Sun KEEP jamie_burt 171438 (ENAMETOOLONG eCryptfs — bounce only). Siblings noted: TURTLE1 171479, Anmol_Ratan 171514. Standing skip: Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270, Catty Kaspersky family 171308+, thomas2018 171324 (server-routines webhook UI — reinforce only), Channels_Cintara Update-Computer auth, Surfshark Temp, session-revoke, F-Secure DeepGuard, Auto-review bind, SuperGrok Start routines, Desktop-secrets overwrite, workspace-media OOS. Overflow watch standing: Carlos_Lopez1 171464 + Rick_Soto 171458 weekly-limit silent (**elevated below** after major Sep 14 staff wave); aiaje Authenticode 171265; y123 VPN 171357.

## KEEP candidates (2)

### KEEP 1 — huanl · “Reconnecting…” costume masks inactive Grok Bot access (SuperGrok / trial), not a dead box
- url: https://forum.cursor.com/t/grok-bot-is-stuck-on-reconnecting-to-your-computer-and-cannot-connect-to-my-existing-bot-computer-since-september-14/171563
- date: OP 2026-09-14 03:57 UTC; deanrie 06:36 UTC
- tags: killed-claim, coverage-ceiling, persistent-computer
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·coverage-ceiling] score=9 | huanl | Windows 0.20.0 stable: stuck on “Reconnecting to your computer…”; Retry / Restore / Reset / hotspot all fail; grok.com chat works same account. OP asked backend recover — **wrong**. deanrie: Bot computer + saved Bots are fine; Reconnecting is **misleading**. Real banner above input: “Start a Grok Bot trial…” / account lacks active Grok Bot access. Access = paid Cursor plan (or Teams) **or** linked active SuperGrok. Free + inactive SuperGrok → Retry/Reset all send the same dead request. Teach: check grok.com Settings for SuperGrok; re-link same email at Sign in; renew SuperGrok / Cursor Pro / trial (card verify; region may block). Once access returns, app reconnects to **existing** computer automatically. Distinct from Kin_Su DNS SERVFAIL Reconnecting and from weekly-limit silent (computer preview still works there). Killed: don’t Reset/Recover chasing Reconnecting when the account simply has no Bot access. Alert: **no** (account-access teach; not a this-week Field file/setting change).
- staff: deanrie (mechanism + checklist)
- siblings: none same-day for access costume; DNS siblings 171482/171479/171514 already kept/noted
- bank: raw/ai/2026-09-15-huanl-grok-bot-is-stuck-on-reconnecting.md

### KEEP 2 — Serene_Thornton · Weekly Grok Bot usage-limit silent costume (… then blank; computer preview OK) — elevated from Mon overflow
- url: https://forum.cursor.com/t/grok-bot-windows-chat-then-blank-computer-preview-works-please-recover-agent-computer/171615
- date: OP 2026-09-14 13:08 UTC; deanrie 13:25 UTC
- tags: killed-claim, coverage-ceiling, quiet-when-nothing
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·quiet-when-nothing] score=9 | Serene_Thornton | Windows 0.47.0: every msg to LEO/Adam → … then blank; Agent Computer preview works (Chrome/Dropbox); Adam stuck “IN PROGRESS — Credentialing”; OP Reset already + asked backend recover — **wrong**. deanrie: computer fine; don’t Reset again (can cost Dropbox login/files). Desktop back after Reset + chat still silent ⇒ not the box. Root: **weekly included Grok Bot usage limit** — messages declined before reply; app should show limit notice (known missing). Teach: Grok Bot Settings → Usage (Grok Bot pool ≠ cursor.com Cursor plan usage); on-demand at cursor.com/dashboard same account; IN PROGRESS stuck because no turn completes. Multi-bot handoff burns limit faster. Same-day staff siblings: looker_dakidaki 171626 (Colin: same limit; reset removed nothing; Settings → Usage); The_Meganator 171588 (deanrie: icon flash ~3s = limit costume; OP confirmed 100% Usage). Elevates Mon overflow Carlos_Lopez1 171464 / Rick_Soto 171458 after major Sep 14 staff wave. Alert: **no** (copyable usage/UX teach; not a Wedge this-week file/routine change required).
- staff: deanrie (171615 + 171588); Colin (171626)
- siblings: 171626 looker_dakidaki; 171588 The_Meganator (confirmed); prior 171464/171458
- bank: raw/ai/2026-09-15-serene-thornton-grok-bot-windows-chat-blank-weekly.md

## OVERFLOW / watch (not packet KEEP)

### Ricardo_Daud 171555 — Take over shows main desktop; bot launched IBKR on separate Xvfb :1
- https://forum.cursor.com/t/grok-bot-viewer-blank/171555 — deanrie: viewer connected (gray wallpaper); bot’s own Xvfb→x11vnc→noVNC stack ≠ Take over display; ask bot to run IBKR on main display without custom :1. OP confirmed fixed. Score ~8–9 persistent-computer / human-gate; overflow (education slots preferred; not Reset/killed core).

### Nathan_Arizona 171676 — Slack routine trigger never fires (Test Run + Slack write OK)
- https://forum.cursor.com/t/grok-bot-slack-routine-trigger-never-fires-while-test-run-and-slack-return-both-work/171676 — no staff yet; lastRunAt null; watch for delivery/subscription teach. Score thin until staff.

### Webhook URL missing cluster (standing — do not re-KEEP thomas2018 171324)
- Alex0 171606 — Colin: not a Pro+ plan issue; newer server-stored routines → desktop panel read-only, no Webhook URL/key/header; use schedule or Slack; manage pause/delete via chat.
- Grzesiek_Zawlodzki 171664; Shaun_Bowe 171677 — same missing fields / Edit injects chat prompt. Tom5 clipboard Accessibility kludge on 171324. Reinforce overflow/coverage-ceiling; thomas2018 standing skip.

### aiaje Authenticode / y123 VPN (standing overflow)
- No new first-party teach past prior packets; still overflow.

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- Kin_Su 171482 / TURTLE1 171479 / Anmol 171514 — DNS Reconnecting; no new mechanism this window.
- enescanguven 171441 — no new staff past Colin Sep 13.
- jamie_burt 171438 — quiet.

### Kaspersky / TLS (standing Catty family — reinforce only)
- Jean_Pierre_Soto_Ch1 171609 — Network Debugger `SELF_SIGNED_CERT_IN_CHAIN` + ConnectError across Auth/Updates/Origin/*.cursorvm.com while DNS OK; OP self-resolved: Kaspersky HTTPS scanning injects cert. New error signature useful; do **not** re-KEEP (Catty Kaspersky standing).
- OliG 171344 — Colin Network Debugger steps; OP confirms Kaspersky; ops/AV cousin.
- Raul_Martins 171283 — deanrie glad Kaspersky exception worked; standing.

### Ops / dual-copy / recovery (no new portable gate)
- Laercio_Albuquerque 171644 — Recover/Reset fail twice partial state; no staff yet; ops.
- Boulders_Brews 171648 — **topic deleted by author**.
- William1 171271 — deanrie Sep 14: machine recreate transfer stuck; don’t spam Reset; wait/ops.
- Gideon_H_Guna_e 171091 — still unresolved day#6; ops.
- Charles_Roe 171078 — bump “Can’t reach”; standing skip.
- Nicolas_Perez1 171008 — sync rollback T-F70063; ops.
- Channels_Cintara / CREODOT 171115 / Tim_Kochatkov 171164 — Update-Computer / auth me-too; standing.

### Tips / feature / wrong surface
- Julien_Mayeur 171678 — live-meeting FR.
- mwjt42 171654 — disable phone notifs when desktop FR; 171567 — mobile no “+” fresh chat (mohitjain: desktop Duplicate workaround).
- Imogen 171549 — sorting FR (prior).
- mohsendev 171540 / anonix98 171539 — context/quota tips.
- tomcomp 171583 — llm controls / new-chat UX.
- TByte007 171561 — 1GB+ RAM Windows; tip/ops.
- Events 171543–171548 — launch nights; skip.
- Effective_Autism 170727/170819 — Auto-review bind standing; Computer Update progress notes only.
- SuperGrok Start / Desktop-secrets / workspace-media OOS — standing.

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–2 → `/workspace/field/forum0915/`
- Search: `Grok+Bot+after:2026-09-13`, `after:2026-09-14`; variants Reconnecting(8) / ENOTFOUND(1→171482 kept) / silent(4) / token(5) / Reset|webhook|secrets|Kaspersky|ENAMETOOLONG|sand-client|DNS|VPN → 0 topic hits on keyword+after combo (tag+date search carried load)
- `c/grok-bot/33.json` skipped (invalid category)
- Topics created ≥2026-09-14 00:00 UTC (bugs/friction): **171549**, **171555**, **171561**, **171563**, **171567**, **171583**, **171588**, **171606**, **171609**, **171615**, **171626**, **171644**, **171648** (deleted), **171654**, **171664**, **171676**, **171677**, **171678**; plus tips/FR
- Priority topic IDs fetched: 171563, 171615, 171626, 171588, 171555, 171609, 171606, 171664, 171324, 171677, 171676, 171644, 171648, 171271, 171567, 171344, 171283, 171561
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 171563 / 171615 deposit
- bank.py deposited KEEP 1–2; field-seen.json not edited; scratch-seen-urls.txt not edited this turn

## Bank deposits
- KEEP: `raw/ai/2026-09-15-huanl-grok-bot-is-stuck-on-reconnecting.md` ← 171563
- KEEP: `raw/ai/2026-09-15-serene-thornton-grok-bot-windows-chat-blank-weekly.md` ← 171615

## Packet recommendation
Keep count: **2** (cap ≤2; education takes other slots). Prefer **huanl 171563** (Reconnecting = no Grok Bot access / SuperGrok inactive — new killed-claim costume distinct from DNS) + **Serene_Thornton 171615** (weekly-limit silent elevated from Mon overflow after Colin/deanrie Sep 14 wave; siblings 171626/171588). Overflow watch: Ricardo_Daud 171555 dual-display Take over vs Xvfb :1; Nathan_Arizona 171676 Slack trigger; webhook URL missing cluster (thomas2018 standing); aiaje; y123. Bounce reinforce: Kaspersky SELF_SIGNED_CERT 171609 (Catty standing); Kin_Su DNS; enescanguven token. **Alert: none** (do not re-alert standing list; access + usage teaches are copyable, not this-week Field path changes). No packet file written. field-seen.json not edited.
