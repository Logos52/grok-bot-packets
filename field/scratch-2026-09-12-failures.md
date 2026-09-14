# Field Grok Bot failure hunt · packet 2026-09-12 (Saturday)
Cutoff: after ~2026-09-11 00:00 UTC (post Friday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+order:latest`. Optional fail-keyword search returned 0 (Discourse OR query rejected). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Friday KEEP Jason_Chu 171219 (F-Secure DeepGuard Temp >10s), ReinerKuestner 171270 (Name>255 as unreachable), Channels_Cintara 171107 (Update Computer auth costume — Friday KEEP/overflow; in scratch-seen-urls; skip re-KEEP). Recent: Charles_Roe 171078, KishoreKV 171173, Teddy1 171170, Wes_Anderson 171029, ellisfan 171008, oubeichen 170989, Human_111425250 170869, Archit 170899, jsolly 170901/170727, Jojo1 170809, TheAviv 170816, noname 170736, Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710, andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, Effective_Autism 170819. Jeffrey_Nead 171280 = Wes secrets sibling — bounce only.

## KEEP candidates (3)

### KEEP 1 — Catty · Kaspersky Encrypted-connections MITM → ConnectError.Internal / “re-provision” costume
- url: https://forum.cursor.com/t/grok-bot-0-44-0-windows-can-t-reach-computer-entitlement-read-connecterror-internal-please-re-provision-agent-computer/171308
- date: 2026-09-11 04:49 UTC (11:49 ICT 11 Sep); staff 05:57 UTC; OP confirm 09:20; staff close 09:54 UTC
- tags: killed-claim, persistent-computer, coverage-ceiling
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·persistent-computer·coverage-ceiling] score=10 | Catty | Windows “Can’t reach / Retrying”; logs `ConnectError.Internal` on entitlement-read / privacy-mode / profile-fetch; `base_url_kind=unknown`; HTTPS to Agent hosts returns expected 404; OP asked backend re-provision (did **not** Reset). Staff **deanrie**: account entitled, Agent Computer healthy; **no requests from the app reached servers after Sep 10** — errors mean the secure connection is cut **on the PC before send**. Browser/Cursor trust Windows store; **Grok Bot trusts only public CAs**, so HTTPS MITM AV fails. Cert check: `api2.cursor.sh` Issued by should be **Amazon RSA 2048 M01**. OP: Issued by was **Kaspersky Anti-Virus Personal Root Certificate**; Kaspersky Plus 21.26 **Encrypted connections scanning** ON → set **Do not scan encrypted connections** → issuer Amazon again → quit/relaunch → connected; **no Recover/Reset**. Staff: exception list works if scanning stays on. Killed: ConnectError.Internal + “re-provision me” can be **TLS MITM AV**, not a dead box — check cert issuer before Reset. Alert: **no** (Windows Kaspersky path; Wedge not on this AV — copyable cousin of Jarri81/Jason_Chu local-exec AV family, different surface: **desktop TLS**, not Temp PS wait).
- staff: deanrie 2026-09-11 05:57 + 09:54 UTC — healthy box; MITM cert; Kaspersky encrypted-scanning confirm; exception alternative.
- siblings: Raul_Martins 171283 (same Kaspersky encrypted-scanning; phone OK / desktop dead; exception fix); Pat4 171358 (partial-state Reset failed → staff healthy + local AV → OP “It was Kaspersky”); glittle/RoamPT on robobobo 171186 (Kaspersky pause/allow; Android OK); Jason_Chu 171219 / Jarri81 170683 (AV Temp >10s local-exec — different mechanism).
- bank: raw/ai/2026-09-12-catty-grok-bot-0-44-0-windows.md

### KEEP 2 — thomas2018 · Server-stored webhook routines: desktop shows no POST URL / crsr_ key
- url: https://forum.cursor.com/t/desktop-grok-bot-webhook-routine-shows-no-post-url-crsr-key-windows-0-47-0/171324
- date: 2026-09-11 08:16 UTC (15:16 ICT 11 Sep); staff 09:30 UTC
- tags: coverage-ceiling, human-gate, quiet-when-nothing
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·coverage-ceiling·human-gate] score=9 | thomas2018 | Desktop 0.47.0 webhook routine panel: Enabled + Instructions + “When a webhook fires” + empty history — **no** gray click-to-copy POST URL / Secret `crsr_…` / Authorization header; deep links empty; recreate useless; bot can’t emit credentials. Related iOS thread said credentials are desktop-only, but desktop still blank. Staff **deanrie**: not user error — **new bots store routines on the server** (“This Bot keeps its routines on the server”); desktop **does not fetch/show** webhook URL/key/header for those; bot can’t provide them either; **known tracked issue; no workaround right now**. Killed: blank webhook fields ≠ broken routine toggle — it’s a **server-routines credential UI gap**; don’t Reset Computer chasing missing `crsr_` keys. Alert: **no** (routines UI ceiling; not a this-week Field file/setting change unless Wedge already ships webhook callers — default no).
- staff: deanrie 2026-09-11 09:30 UTC — server-stored routines; desktop doesn’t surface webhook credentials; no workaround; tracking.
- siblings: (iOS “webhook url missing” cited by OP — desktop-only myth broken by this thread). Distinct from KishoreKV SuperGrok+Start routines gate.
- bank: raw/ai/2026-09-12-thomas2018-desktop-grok-bot-webhook-routine-shows.md

### KEEP 3 — aiaje_com · In-app updater Authenticode probe fails → stays on old build (manual Setup.exe OK)
- url: https://forum.cursor.com/t/grok-bot-windows-in-app-update-downloads-then-fails-authenticode-probe-installer-signature-invalid/171265
- date: 2026-09-10 15:16 UTC; **NEW staff** Colin 2026-09-11 09:06 UTC (post-Friday cutoff)
- tags: killed-claim, coverage-ceiling
- score: 8 (portable 4 / evidence 4)
- packet one-liner: [agentic·killed-claim·coverage-ceiling] score=8 | aiaje_com | Windows in-app update downloads then fails verify (“downloaded update could not be verified”); repeats across versions (0.36→0.39, 0.44→0.47); `%LOCALAPPDATA%\sand-updater\installer.exe` stays old; official **Setup.exe** Authenticode Valid (Anysphere) and silent-installs fine. Staff **Colin**: verification step fails post-download (AV holding file or check too long); signing cert itself OK (same machine verified other days); workaround = manual Setup.exe from download page; **Agent Computer needs no Reset/Update** — desktop app only. Killed: `installer_signature_invalid` costume ≠ bad Cursor signer — try **manual Setup.exe**, not Recover. Alert: **no** (Windows updater packaging; not Wedge’s this-week path).
- staff: Colin 2026-09-11 09:06 UTC — post-download verify flake / AV hold; manual Setup.exe; don’t touch Agent Computer.
- siblings: Friday watch on same thread; now staff-closed enough to KEEP. Catty was stuck on 0.44 while 0.47 downloaded — same updater family surface.
- bank: raw/ai/2026-09-12-aiaje-com-grok-bot-windows-in-app-update.md

## BOUNCE

### Kaspersky MITM siblings (mechanism captured in KEEP 1 — do not double-keep)
- Raul_Martins 171283 — looping reconnection; Recover/Update/Reset/reinstall failed; phone works; staff deanrie: Agent Computer fine; Kaspersky encrypted-scanning replaces cert; exception or disable scanning fixed. Same portable gate as Catty. https://forum.cursor.com/t/looping-reconnection/171283
- Pat4 171358 — “partial state” Reset failed; deanrie: computer healthy, don’t Reset; OP “It was Kaspersky.” Thinner than Catty (no cert A/B). https://forum.cursor.com/t/grok-bot-windows-computer-stuck-in-partial-state-reset-failed/171358
- glittle / RoamPT on robobobo 171186 — Kaspersky pause/allow; Android OK / Windows dead; mohitjain separated their AV cases from robobobo dual-copy.

### Dual-copy / recovery ops (no new portable gate vs Wed–Fri)
- robobobo 171186 — mohitjain dual unfinished copy; staff reconnected Sep 11 — Friday bounce, still ops.
- Gideon_H_Guna_e 171091 — kevinn recovery-state; still unresolved Sep 11 nag — ops.
- Martin_Holmes 170722 — mohitjain OOM from parallel panes (Sep 7) + restored Sep 11; prevention = concurrency 1 / no mass-resume — **Benjamin_Barber 170689 OOM sibling**; bounce.
- Bradley_Street 170721 — Mac main-pane missing replies; later dual-copy outage explain (Sep 7) — UI/ops, not FAILURES slot.
- Ronald_Naners 170743 / Parammehta / Raul_Mena_Montes — cloud computer unresponsive; per-account email — ops.
- zoe_Joestar 171304 — clientNonce/no requestId; Colin restored box — thin ops.
- JobJet 171339 / OliG 171344 / Altair_Beterelli_Gon 171393 — stuck/unreachable, no staff mechanism yet.
- Esteban1 171384 — “era el antivirus” / “It’s done.” — thin, no portable teach.

### Agent-Computer VPN self-brick (watch / overflow)
- y123 171357 — bot installed VPN **inside** Agent Computer → all bots unreachable incl. phone; OP self-teaches “VPN on box unsupported”; “problem was fixed” (~1 min later) — no staff quote. Portable instinct (don’t let bots change box routing) but evidence < staff KEEP bar. Score ~7 overflow. https://forum.cursor.com/t/grok-bot-agent-computer-unreachable-after-bot-installed-a-vpn-all-bots-fail-to-reconnect/171357

### Secrets wipe sibling (do NOT re-alert Wes_Anderson)
- Jeffrey_Nead 171280 — still Wes_Anderson 171029 sibling; bounce only.

### Auth Update-Computer (already Friday KEEP)
- Channels_Cintara 171107 — Friday KEEP 3 / packet overflow; in scratch-seen-urls; skip. Me-too oyagen 171115 / Lit_Sky 171164 unchanged.

### Privacy / labeling / OAuth — already covered or thin
- michael_pulley / Liam_B 170509 — Privacy Mode unsaved → reconnecting forever (Teddy1 cousin); deanrie still debugging Liam — bounce.
- jsolly 170898 — GitHub “Needs auth” / Authenticate toast is **labeling**; PAT under Setup Values already works (mohitjain) — not killed-claim FAILURES; jsolly already kept elsewhere.

### Quota / events / tips (not FAILURES)
- Ultra/allowance / Models display threads (171221, 170771, 170742, 170990, 170835, 170951, 171226) — hygiene/docs.
- Miami/Goiânia/Atlanta meetup posts — events.
- Yaddu job-search / DannyB memory export — tips.

### Already-kept (window)
- Jason_Chu 171219 · ReinerKuestner 171270 · Channels_Cintara 171107
- Charles_Roe 171078 · KishoreKV 171173 · Teddy1 171170
- Wes_Anderson 171029 · ellisfan 171008 · oubeichen 170989
- Human_111425250 170869 · Archit 170899 · jsolly 170901/170727
- Jojo1 170809 · TheAviv 170816 · noname 170736 · Effective_Autism 170819
- Jarri81 170683 · Winvicta 170691 · Benjamin_Barber 170689 · StefanZ 170710
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` page 0 + page 1; `search.json?q=Grok+Bot+order:latest` → `/workspace/field/forum0912/`
- Optional `search.json?q=Grok+Bot+(unreachable OR …)` → 0 topics (query rejected / empty)
- Priority topic IDs fetched (18): 171384, 171393, 171358, 171357, 171344, 171339, 171308, 171324, 171304, 171283, 171091, 171265, 170722, 171186, 170509, 170721, 170743, 170898
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior entries for 171308/171324/171265
- bank.py deposited all 3 KEEP raws + refreshed INDEX
- Channels_Cintara 171107 skipped (Friday KEEP + scratch-seen); Jeffrey_Nead 171280 bounce-only

## Bank deposits
- KEEP: `raw/ai/2026-09-12-catty-grok-bot-0-44-0-windows.md` ← 171308
- KEEP: `raw/ai/2026-09-12-thomas2018-desktop-grok-bot-webhook-routine-shows.md` ← 171324
- KEEP: `raw/ai/2026-09-12-aiaje-com-grok-bot-windows-in-app-update.md` ← 171265

## Packet recommendation
Keep count: **3** — Catty 171308, thomas2018 171324, aiaje_com 171265. Cap ~2–3 FAILURES (compiler total cap 5 with education). Prefer **171308 + 171324** if cut to 2 (distinct gates: Kaspersky TLS MITM / ConnectError.Internal re-provision costume vs server-routines webhook credential UI ceiling); 171265 is strong updater kill for the Authenticode wave (overflow if room). **Alert: none** (do not re-alert Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, or Jason_Chu 171219; Jeffrey_Nead 171280 Wes sibling only; Kaspersky/Authenticode are Windows AV paths Wedge doesn’t run). Overflow watch: y123 171357 Agent-Computer VPN self-brick; Raul/Pat4 as Catty siblings only. No packet file written. field-seen.json not edited.
