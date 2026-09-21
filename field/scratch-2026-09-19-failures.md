# Field Grok Bot failure hunt · packet 2026-09-19 (Saturday)
Cutoff: after ~2026-09-18 00:00 UTC (post Friday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+after:2026-09-17` (+ `after:2026-09-18`). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped / bounce only): Fri KEEP Dave_Campos 172070 (iOS chat-pattern unexpected-error ≠ computer — don’t Update/Reset); Fri KEEP allninety 171962 (account-stuck Unknown multi-device since 11 Sep; status Operational ≠ account — don’t Reset). Thu KEEP ziemovit 171791; Thu KEEP Mercer_Alex 171840. Wed KEEP Kostadin_S 171735; Wed KEEP Nathan_Arizona 171676. Standing skip: huanl 171563, Serene_Thornton 171615 (+171626/171588), Charles_Roe 171078, Wes_Anderson 171029, CallDynamicTool 170869, Jason_Chu 171219, ReinerKuestner 171270, jamie_burt 171438, Kin_Su 171482, enescanguven 171441, Catty Kaspersky family, thomas2018 171324 webhook, Channels_Cintara Update-Computer auth, Surfshark Temp, session-revoke, F-Secure DeepGuard, Auto-review bind, SuperGrok Start routines, Desktop-secrets overwrite, workspace-media OOS, Andrew Zscaler 171777, Liyo_K/Palan DNS. Fri overflow re-checked — no elevation (Nads 171858 fleet hub still ops/merge; Adam Mercer reinforce; Aerospace/Elizabeth usage-silent; Mariusz restore; Sanghoon parent-idle; Wes 172032 degradation).

## KEEP candidates (2)

### KEEP 1 — Volkan_Erdogan · First-init never finished → Recover/Reset stuck at 50%; chat OK — don’t Reset again
- url: https://forum.cursor.com/t/cant-reach-your-computer-on-macos-recover-and-reset-both-fail-at-50/172135
- date: OP 2026-09-18 11:11 UTC; deanrie 2026-09-18 11:39 UTC
- tags: killed-claim, persistent-computer, coverage-ceiling
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=9 | Volkan_Erdogan | macOS “Can’t reach your computer”; Recover **and** Reset both fail at identical server step “Starting Grok Bot’s computer” ~50%; OP ruled out DNS (1.1.1.1/8.8.8.8 + flush), hotspot, VPN, privacy Share Data; **chat with the bot still works**. deanrie: computer **never finished the very first initialization**, so app Recover/Reset cannot complete — same stuck server-side step; nothing user can do; **don’t run Reset again** (won’t finish); known issue needing staff-side fix; account + existing chat safe because chat is server-side while VM unavailable; after staff fix: fully Quit menu-bar → reopen. Teach: chat-OK + Recover/Reset fail-at-50% + DNS/hotspot already ruled out ≠ DNS (Kin_Su/Palan/Liyo/soulsoup) ≠ AV HTTPS (Catty/Anderson/August) ≠ account-stuck Unknown (allninety) ≠ usage-silent (Serene) — it’s **first-init incomplete / staff-only**. Alert: **no** (don’t-Reset teach; wait for staff; not a this-week Field file/setting change).
- staff: deanrie (first-init incomplete mechanism; hold Reset; chat-safe; staff handoff)
- siblings: allninety 171962 (account-stuck multi-device — different); Palan/Liyo/soulsoup 172128 DNS (local fix — ruled out here); Anderson 172142 / August 172087 AV HTTPS (Windows phone-OK — different); Kostadin all-bots backend
- bank: raw/ai/2026-09-19-volkan-erdogan-cant-reach-your-computer-on-macos.md

### KEEP 2 — Anderson_V_Leite · “Reset failed / partial state” loop = Windows HTTPS interception; Reset never reached servers — don’t Retry Reset
- url: https://forum.cursor.com/t/grok-bot-stuck-in-reset-failed-partial-state-loop-retry-reset-hangs-at-getting-ready-0/172142
- date: OP 2026-09-18 11:45 UTC; deanrie 2026-09-18 12:30 UTC; OP confirm 2026-09-18 16:42 UTC
- tags: killed-claim, persistent-computer, quiet-when-nothing
- score: 9 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=9 | Anderson_V_Leite | Windows “Can’t reach” → Reset failed / “computer may be in a **partial state**” → Retry Reset hangs “Getting ready” 0%; phone had created healthy computer. deanrie: Agent Computer **fine**; Bot on it; **none of the Windows Reset attempts ever reached servers** — nothing wiped, nothing half-stuck; **“partial state” wording is misleading**; don’t Reset/Recover. Cause: PC HTTPS inspection (Kaspersky encrypted-connections scanning); browsers trust Windows store, Grok Bot trusts public CAs only; **pausing protection is not enough**. Check api2.cursor.sh cert Issued by = Amazon RSA 2048 M01. OP confirmed: Kaspersky → Do not scan encrypted connections → full Quit tray → connected; bots/files/logins intact. Teach: phone-OK + Windows Reset-failed/partial-state = local TLS interception costume, **not** a half-wiped computer — don’t Retry Reset (elevates Catty/Andrew AV family with durable UI-lie + “Reset never hit servers” diagnostic). Alert: **no** (don’t-Reset + local AV toggle; not a this-week Field path change).
- staff: deanrie (partial-state misleading; Reset never reached servers; Kaspersky encrypted-scan steps; pause≠disable)
- siblings: Catty Kaspersky / Andrew Zscaler 171777 / August_Su 172087 (white-blank AV costume) / kk_huang 172120 (Windows ID-not-Gmail + phone OK = same TLS); Max_Maldonado Kaspersky
- bank: raw/ai/2026-09-19-anderson-v-grok-bot-stuck-in-reset-failed.md

## OVERFLOW / watch (not packet KEEP)

### Nads_D_Etc 171858 — fleet unresponsive hub (~180 posts) — no NEW durable mechanism
- https://forum.cursor.com/t/some-of-the-bots-became-unresponsive-failed-to-send-on-my-messages-to-them/171858 — continues merge sink for Sep 18 one-bot / Failed-to-send (172121, 172134, 172138, 172139, …). Portable teach still Mercer 171840 (per-bot runner / don’t Reset). **Do not elevate**.

### August_Su_TW_SR 172087 — white/blank Windows after “Creating computer” = AV/proxy HTTPS scanning
- https://forum.cursor.com/t/grok-bot-briefly-shows-creating-grok-bot-s-computer-then-the-main-window-goes-fully-white-blank/172087 — mohitjain: computer healthy; don’t Update/Reset; white window ≈ AV/proxy HTTPS scan; check api2.cursor.sh Issued by = Amazon. AV-family reinforce of KEEP 2 — bounce/overflow.

### kk_huang 172120 — Windows can’t reach + profile shows user ID not Gmail; iPhone OK
- deanrie: same account; computer fine; don’t Reset/Recover; Windows post-login requests blocked by HTTPS inspection. AV/TLS reinforce — bounce.

### soulsoup 172128 — Android Can’t reach / Recover = mobile-carrier DNS; Private DNS fix confirmed
- Colin: computer + bots fine; Recover taps completed (nothing deleted); carrier DNS can’t resolve computer address; Android Private DNS → `one.one.one.one`; OP “It worked.” Kin_Su/Palan/Liyo DNS cousin (Android Private DNS path) — bounce/overflow.

### Innovaite 172118 / oxi_ixo 172290 — all-bots silent after Reset = usage exhausted (trial / weekly); notice missing
- deanrie: computer fine; trial credit used / weekly limit hit; app should show usage notice (known missing); Settings → Usage % = used not remaining; don’t Reset. Serene quiet-when-nothing reinforce — bounce. (Innovaite follow-up: SuperGrok link confusion — account/billing ops.)

### Dasheng 172121 / Human_111425250 172134 / Wadels 172138 / Raymond_Weiss 172139 — Failed to send / one-bot deaf; merged 171858
- deanrie/Colin: computer fine; service-side queue; don’t Reset/create extras; Maturin temporal-vs-box harness observation only. Mercer reinforce — bounce.

### Sanghoon_Kang 172166 — Cloud Agent ResourceExhausted vttablet = Sep 17 statuspage degradation
- kevinn: Cursor-side Cloud Agents/Automations degradation Sep 17 15:20–20:04 UTC; not Ultra quota / not per-account pool / not Caller-ID workspace; nothing to Reset. Ops/incident — overflow (~7–8); not durable Field gate beyond “ResourceExhausted ≠ plan / wait statuspage.”

### Armorr 172304 — Windows Can’t reach; Android OK = laptop DNS
- kevinn: computer healthy; don’t Reset; set 1.1.1.1/8.8.8.8 + hotspot confirm. DNS family bounce.

### codercurtis 172307 — ListMachines connected=false; desktop chat works; no staff yet
- Thin watch; local-exec / registered-machine surface — overflow until staff mechanism.

### Kumar_Melvani 172292 — iOS 1.11.1 voice/call icon missing = staged rollout
- kevinn: gradual rollout; reinstall won’t help; desktop voice + phone dictation OK. UX/rollout — not failure KEEP.

### RebarRebel 172302 — Grok Bot 0.57.0 Windows download AccessDenied
- kevinn: tracking; interim 0.56.1 link. Ops/download — bounce.

### Prashanth_Kumar 172163 — duplicate local machines / reset fails; template-bot only
- No human staff mechanism yet — watch.

## BOUNCE

### Already-kept reinforced in-window (do not re-KEEP)
- Dave_Campos 172070 / allninety 171962 — Fri KEEP; allninety bumped 18 Sep day-8 status note only (still account-stuck; no new mechanism).
- ziemovit 171791 / Mercer_Alex 171840 — Thu KEEP; 172121/172134/172138 Mercer siblings merged/reinforce.
- Kostadin_S 171735 / Nathan_Arizona 171676 — Wed KEEP; bounce only.
- Serene 171615 — Innovaite 172118 + oxi_ixo 172290 + Aerospace/Elizabeth cousins.
- Kin_Su 171482 / Liyo_K / Palan — soulsoup 172128 Android Private DNS + Armorr 172304 Windows DNS reinforce.
- Catty Kaspersky / Andrew Zscaler — Anderson KEEP-adjacent + August 172087 + kk_huang 172120 TLS reinforce (KEEP 2 carries the new “partial state misleading / Reset never hit servers” teach; plain AV tips bounce).
- thomas2018 171324 webhook — standing; no elevate.
- Wes_Anderson standing 171029 ≠ 172032 ops (already Fri overflow).

### Ops / merges / recovery
- Mass merge into 171858: 172121, 172134, 172138, 172139, ….
- 172166 Cloud Agents statuspage window (resolved).
- 172302 download 0.57.0 AccessDenied interim.

### Tips / feature / wrong surface / promo
- 172106 chat-queue before usage reset FR / 172148 + 166689 multi-account FR / 172292 voice staged rollout / 172310 1Password Mac-only connector / 172305 DeFi Daddy soft-invite promo / 171950 rename bump / 168499 Vercel OAuth bump / meetups skip.

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` pages 0–1 → `/workspace/field/forum0919/`
- Search: `Grok+Bot+after:2026-09-17` (50 topics) and `after:2026-09-18` (38 topics) succeeded; no rate-limit this turn
- `c/grok-bot/33.json` skipped (invalid category)
- In-window created ≥2026-09-18 00:00 UTC (bugs/friction focus): **172087**, **172106**, **172118**, **172120**, **172121**, **172128**, **172134**, **172135**, **172138**, **172139**, **172142**, **172148**, **172163**, **172166**, **172290**, **172292**, **172302**, **172304**, **172305**, **172307**, **172310**; plus activity bumps on 171858 (merges), 171962 (allninety day-8), 172074, 172009, 171950, 171895, 171969
- Priority topic IDs fetched: 172135, 172142, 172087, 172120, 172128, 172118, 172290, 172121, 172134, 172138, 172139, 172166, 172304, 172307, 172292, 172302, 172163, 172106, 172310, 172305, 171962, 171858
- Full slugs from feed JSON; public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior 172135 / 172142 deposit
- bank.py deposited KEEP 1–2; field-seen.json not edited; latest.md / field-packet-*.md not touched
- Appended 55 new topic ids to `/workspace/field/seen-forum-ids.txt` (total 318)

## Bank deposits
- KEEP: `raw/ai/2026-09-19-volkan-erdogan-cant-reach-your-computer-on-macos.md` ← 172135
- KEEP: `raw/ai/2026-09-19-anderson-v-grok-bot-stuck-in-reset-failed.md` ← 172142

## Packet recommendation
Keep count: **2** (cap ≤2). Prefer **Volkan_Erdogan 172135** (first-init never finished → Recover/Reset stuck 50%; chat OK; don’t Reset again; staff-only) + **Anderson_V_Leite 172142** (“partial state” Reset-failed loop = Windows HTTPS/Kaspersky; Reset never reached servers; pause≠disable encrypted scan; don’t Retry Reset — elevates AV family with UI-lie diagnostic). Overflow: 171858 fleet hub (no elevate); August white-blank AV; kk_huang TLS; soulsoup Android Private DNS; Innovaite/oxi usage-silent; Mercer merges; Sanghoon ResourceExhausted statuspage; Armorr DNS; codercurtis ListMachines watch. **Alert: none** (both don’t-Reset teaches; not this-week Field path changes). No packet file written. field-seen.json not edited.

## PACKET READY
- [agentic·killed-claim·persistent-computer] score=9 | Volkan_Erdogan | First-init incomplete → Recover/Reset fail at 50%; chat OK; don’t Reset again (staff-only)
- [agentic·killed-claim·persistent-computer] score=9 | Anderson_V_Leite | “Partial state” Reset loop = Windows HTTPS interception; Reset never hit servers; don’t Retry Reset
