# Field Grok Bot failure hunt · packet 2026-09-11 (Friday)
Cutoff: after ~2026-09-10 00:00 UTC (post Thursday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+order:latest`. Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Charles_Roe 171078 (125 GB restore OOS — ALERTED), KishoreKV 171173 (SuperGrok+Start routines), Teddy1 171170 (Privacy Mode unsaved overflow), Wes_Anderson 171029, ellisfan 171008, oubeichen 170989. Prior: Human_111425250 170869, Archit 170899, jsolly 170901/170727, Jojo1 170809, TheAviv 170816, noname 170736, Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710, andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, Effective_Autism 170819 (+ URLs in scratch-seen-urls.txt).

## KEEP candidates (3)

### KEEP 1 — ReinerKuestner · First-bot Name >255 misreported as “Can’t reach your computer”
- url: https://forum.cursor.com/t/grok-bot-macos-initial-setup-fails-agent-computer-unreachable/171270
- date: 2026-09-10 17:13 UTC (00:13 ICT 11 Sep); staff 2026-09-10 17:46 UTC (00:46 ICT 11 Sep)
- tags: killed-claim, human-gate
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·killed-claim·human-gate] score=9 | ReinerKuestner | Brand-new macOS setup dies with “Grok Bot couldn’t finish setting up. Can’t reach your computer right now.”; Settings won’t open so Recover/Update unavailable; curl to us8.cursorvm.com returns 404 (host reachable); status-page Cloud Agents blip looked related. Staff **kevinn**: Agent Computer is **healthy and reachable**; status page **unrelated**. Failure is the **last setup step — Create your first Bot** — which **rejects a Bot name longer than 255 characters** and the UI **reports that as a connection problem**. Unblock: Quit → reopen → short Name (e.g. “Assistant”) → put long instructions in the first chat message. Staff: auto-cap name update coming. Killed: “Can’t reach” on first-run setup can be **name-length validation costume**, not a dead computer — don’t burn Recover/Reset. Alert: **no** (onboarding edge; Wedge already past first-bot).
- staff: kevinn 2026-09-10 17:46 UTC — healthy box; >255 name rejected; misreported as unreachable; short-name fix; auto-cap coming.
- siblings: Teddy1 171170 (Privacy Mode unsaved → can’t-reach costume — different gate); smolen2011 171177 / robobobo 171186 dual/partial-state ops (real backend).
- bank: raw/ai/2026-09-11-reinerkuestner-grok-bot-macos-initial-setup-fails.md

### KEEP 2 — Jason_Chu · F-Secure DeepGuard delays Temp one-shot PS past 10s → false “temporarily unreachable”
- url: https://forum.cursor.com/t/grok-bot-local-exec-blocked-by-f-secure-on-windows-folder-exclusions-ineffective/171219
- date: 2026-09-10 04:17 UTC (11:17 ICT 10 Sep); staff A/B 2026-09-10 09:11 UTC; OP confirm 10:50 UTC
- tags: killed-claim, persistent-computer, coverage-ceiling
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·persistent-computer·coverage-ceiling] score=10 | Jason_Chu | Windows local-exec: chat OK, PC may show connected, local commands “unavailable / temporarily unreachable”. Fully disabling F-Secure restores; exclusions of Grok Bot install + `.grokbot` folders **do nothing**. Staff **mohitjain**: F-Secure is **delaying each command past the ~10s agent wait** (~12s on / ~1s off), not blocking the pipe; each command is a **fresh one-off PowerShell under `%LOCALAPPDATA%\Temp`**, outside app-folder exclusions. OP A/B: **DeepGuard/Behavior Detection OFF alone → works**; allowlisting only `Grok Bot.exe` with DeepGuard ON → still fails; excluding whole `Temp` with DeepGuard ON → works; narrower Grok subfolder under Temp → fails. Killed: treat “temp unreachable” on Windows AV as **DeepGuard scanning Temp one-shots past the wait**, not a dead Agent Computer / Reset. Prefer DeepGuard app allow or longer timeout when shipped; whole-Temp exclude is insecure last resort. Alert: **no** (Windows F-Secure; Wedge not on this path — copyable cousin of Jarri81, not a this-week Field file change).
- staff: mohitjain 2026-09-10 09:11 UTC — 10s wait / Temp one-shot PS; DeepGuard A/B plan. OP confirmed DeepGuard-only and Temp-exclude results.
- siblings: Jarri81 170683 (Surfshark AV Temp `ps-script-*.ps1` >10s — same portable gate, different vendor; this adds DeepGuard-specific + exe-allowlist-insufficient teach).
- bank: raw/ai/2026-09-11-jason-chu-grok-bot-local-exec-blocked-by.md

### KEEP 3 — Channels_Cintara · “Authentication error / try logging out” while signedIn — Update Computer, not logout
- url: https://forum.cursor.com/t/authentication-error-try-logging-in/171107
- date: 2026-09-08 23:32 UTC; **NEW staff diagnosis** deanrie 2026-09-10 18:30 UTC (01:30 ICT 11 Sep)
- tags: killed-claim, human-gate
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·killed-claim·human-gate] score=9 | Channels_Cintara | Desktop banner “Authentication error / If you are logged in, try logging out and back in” despite UI signed-in; logout/reinstall useless. Staff **deanrie** (2026-09-10): session is fine; **recent backend change** is preventing some Grok Bot computers from reaching the model; logout/reinstall won’t help. User fix: **Settings → Grok Bot’s Computer → Update** (bots/files stay); if still failing, staff reset. Me-too cluster (oyagen 171115 / Lit_Sky 171164 / Gustavo_Lage / Otavio_Cavalcante) + community confirm Josh2/rodschulz: **Update Grok Bot’s Computer** clears it. Killed: auth-error costume ≠ local logout bug — try **Update Computer** before Reset/reinstall. Alert: **no** (ops costume teach; not quota/routines/what-Bot-may-hold this week).
- staff: deanrie 2026-09-10 18:30 UTC — session OK; backend model-reach change; Update Computer path. Sibling threads: kevinn/Colin per-account resets (171115/171164).
- siblings: andyfraussen 170568 / _Remi 170438 (session-revoke can’t-reach costume — related auth surface, different symptom); Thursday auth-wave bounce now has portable Update-Computer gate.
- bank: raw/ai/2026-09-11-channels-cintara-authentication-error-try-logging-in-staff.md

## BOUNCE

### Secrets wipe sibling (do NOT re-alert Wes_Anderson)
- Jeffrey_Nead 171280 — MIPP API keys via secure in-chat card wiped on desktop reconnect/sleep/quit; OP cites staff confirm from other report (reconnect sync overwrites secrets). Same portable gate as **Wes_Anderson 171029** (already ALERTED). New named production blocker, **no new mechanism** — bounce; do not re-alert. https://forum.cursor.com/t/grok-bot-box-secrets-wiped-on-desktop-reconnect-mipp-api-keys-production-blocker/171280

### Gmail Spam MCP coverage-ceiling (overflow / watch)
- TheAviv 170832 — `list_labels` shows SPAM counts but `search_threads` (incl. staff-documented `in:anywhere label:SPAM`) returns `{}`; deanrie 2026-09-10 conclusive: hosted Gmail server side, connector passes args as-is; raised upstream; browser fallback. Score ~9 coverage-ceiling but MCP/vendor; prefer not to spend FAILURES slot vs 171270/171219/171107. (TheAviv 170816 GTK already kept — different surface.) https://forum.cursor.com/t/grok-bot-gmail-search-threads-returns-empty-for-spam-while-list-labels-shows-threads/170832

### Dual-computer / partial-state / rebuild ops (no new portable gate vs Wed–Thu)
- robobobo 171186 — mohitjain: **two computer copies**, app pointed at unfinished one; stop Reset/Recover (bots safe). Me-too RoamPT/glittle (Android OK / Windows can’t). Same dual-copy cluster as oubeichen cousin.
- Gideon_H_Guna_e 171091 — recovery state, staff looking, still unresolved — ops.
- Steve_Solomon 171240 — kevinn rebuilt — thin.
- Raul_Martins 171283 — looping reconnection, no staff mechanism yet.
- smolen2011 171177 — kevinn geo/ToS reply contested by OP (partial-state ticket) — not FAILURES-portable.
- nitesh_sharma 170954 — deanrie: computer stopped authorizing 6 Sep; tracking — costume wave.
- prashant_kumar1 171028 — deanrie: **Jio DNS** for `*.cursorvm.com` — local DNS, not Reset; ISP-specific bounce.

### Auth-error me-too (mechanism captured in KEEP 3)
- oyagen 171115 / Lit_Sky 171164 / Channels siblings Gustavo_Lage / Otavio_Cavalcante — logout useless; Update Computer or staff knobs. Do not double-keep.

### OAuth / connector — thin or already-covered
- brianrobt 171183 Todoist Authenticate toast (kevinn: known tracking) — Thu bounce.
- BG1 171111 Robinhood OAuth 15-min window — Thu overflow.
- Olivier_GUILLOUX 169991 Zoom `localhost:8787` reject (deanrie: tracking; no workaround) — already in scratch-seen-urls; still open.

### Quota / billing / display (not killed-claim FAILURES)
- olegdater 171221 Ultra weekly burn — mohitjain: cache-read long chats, fresh chat per task, space routines, delegate to Cloud Agents — hygiene tips.
- Sinn 171226 — deanrie: grok-bot-* rows under Cursor Models are **display bug**; weekly pool separate.
- Publicidade_Ja_Marke 170951 — deanrie pool table (weekly vs Cursor) — docs.
- krstoevan 171010 — SuperGrok on-demand; deanrie: don’t buy Pro for Bot quota; on-demand with SuperGrok link.
- Dominik-N 170888 — Ultra vs Heavy same top Bot tier; Heavy no longer free Ultra.

### Install / update packaging / FR / tips
- aiaje_com 171265 — in-app update Authenticode `installer_signature_invalid`; manual Setup.exe Valid — no staff yet; watch.
- Kyles_Cousin 171281 — RPM download links stale filename; kevinn gave direct 0.47.0 + yumrepo — install docs.
- Yaddu 171187 job-search tips · DannyB 170714 memory export how-to (mohitjain zip teach) — not FAILURES.

### Already-kept (window)
- Charles_Roe 171078 · KishoreKV 171173 · Teddy1 171170
- Wes_Anderson 171029 · ellisfan 171008 · oubeichen 170989
- Human_111425250 170869 · Archit 170899 · jsolly 170901/170727
- Jojo1 170809 · TheAviv 170816 · noname 170736 · Effective_Autism 170819
- Jarri81 170683 · Winvicta 170691 · Benjamin_Barber 170689 · StefanZ 170710
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` page 0 + page 1; `search.json?q=Grok+Bot+order:latest` → `/workspace/field/forum0911/`
- Priority topic IDs fetched (26): 171280, 171219, 171265, 171270, 171283, 170832, 171186, 171091, 171115, 171164, 171177, 171221, 171226, 171240, 171281, 171010, 170951, 169991, 170714, 171107, 171028, 170954, 170888, 171183, 171111, 171187
- Full slugs from feed JSON (no empty short-slug misses this run)
- Public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior entries for 171270/171219/171107
- bank.py deposited all 3 KEEP raws + refreshed INDEX

## Bank deposits
- KEEP: `raw/ai/2026-09-11-reinerkuestner-grok-bot-macos-initial-setup-fails.md` ← 171270
- KEEP: `raw/ai/2026-09-11-jason-chu-grok-bot-local-exec-blocked-by.md` ← 171219
- KEEP: `raw/ai/2026-09-11-channels-cintara-authentication-error-try-logging-in-staff.md` ← 171107

## Packet recommendation
Keep count: **3** — ReinerKuestner 171270, Jason_Chu 171219, Channels_Cintara 171107. Cap ~2–3 FAILURES (compiler total cap 5 with education). Prefer **171270 + 171219** if cut to 2 (distinct gates: first-bot name-length human-gate costume vs F-Secure DeepGuard/Temp 10s local-exec coverage-ceiling); 171107 is strong auth Update-Computer teach for the signedIn:true wave (overflow if room). **Alert: none** (do not re-alert Charles_Roe 171078, Wes_Anderson 171029, or CallDynamicTool 170869; Jeffrey_Nead 171280 is Wes sibling only). Overflow watch: TheAviv 170832 Gmail Spam hosted-server `{}`; aiaje_com 171265 Authenticode updater; dual-copy 171186. No packet file written. field-seen.json not edited.
