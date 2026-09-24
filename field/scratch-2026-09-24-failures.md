# Field Grok Bot failure hunt · packet 2026-09-24 (Thursday)
Cutoff: after ~2026-09-22/23 UTC (post Wed packet KEEP dnz 172578 + codercurtis 172307; overflow Ryan_Daley 172545 banked — **do not re-keep**). Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-22` (+ `after:2026-09-23`) + keyword friction searches (stuck, reconnecting, can't reach, Reset, local execution, routines). Category `c/grok-bot/l/latest.json` and `c/grok-bot/33.json` → **404 invalid** (skip; use tag+search). Public, no login. No Firecrawl. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Wed KEEP dnz 172578 (api2→100.x Pearson cert / 100.0.0.0/8 misroute); Wed KEEP codercurtis 172307 (Ubuntu 22.04 GLIBCXX_3.4.31); Wed overflow Ryan_Daley 172545 (routines queue latency). Tue KEEP Michael_Pan 172494 (forever-box ReadTranscript). Mon KEEP chrisoh806 172401 (43% Transferring). Sun KEEP BigBojangles 172349 (local-exec root). Sat KEEP Volkan_Erdogan 172135; Sat KEEP Anderson_V_Leite 172142. Fri KEEP Dave_Campos 172070; Fri KEEP allninety 171962. Standing footer: Catty Kaspersky / Kin_Su DNS / Zscaler / server-routines webhook / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset. Do not re-alert footer list.

Elevate watches from Wed IF staff landed: Timothy_Gresh 172549, Chexander 172715, Vikas_Dakshi 172696, Peacerk 172618 — **only if new portable staff teach**; else reinforce/bounce.

## KEEP candidates (2) — recommend for packet (edu setups take priority for cap; compiler pick top 1–2 if slot-tight)

### KEEP 1 — Chexander · Route-through rejects RFC1918 / split-horizon DEV; use desktop Shell/browser
- url: https://forum.cursor.com/t/grok-bot-route-traffic-through-this-computer-fails-for-split-horizon-internal-dev-hosts/172715
- date: OP 2026-09-22 23:45 UTC; deanrie staff 2026-09-23 04:41 UTC (elevate from Wed watch)
- tags: networking, teach-once, route-through, split-horizon, persistent-computer
- score: **10** (portable 5 / evidence 5)
- packet one-liner: [agentic·networking·teach-once·route-through] score=10 | Chexander | “Route traffic through this computer” ON; UI “routed this session” increments; public hosts OK; **split-horizon DEV fails**: bot DNS → public IP, desktop → 192.168.x; HTTP CONNECT :443 returns 200 then TLS EOF / ERR_CONNECTION_CLOSED. **deanrie: relay only covers public internet addresses.** When desktop resolves hostname to **private** 192.168.x / 10.x / 172.16–31.x, desktop side **rejects**; CONNECT 200 then TLS closes. Public cloud hosts keep working. Bot-side DNS via cloud resolver is expected; routed traffic resolves on desktop. Docs currently imply internal hosts should work — mismatch filed with team. **Workaround (correct now):** with Execution on this computer allowed, have bot run DEV checks via **Shell/browser on the registered desktop**, not on the bot computer. **Distinct from** dnz 172578 (api2 100.x/Pearson cert) and Kin_Su DNS. Alert: **no** (durable teach; no this-week Field roster file change).
- staff: deanrie
- bank-body: /workspace/field/bank-bodies/bank-body-172715.txt (+ forum0924 copy)

### KEEP 2 — GFP · “Reset failed / partial state” ≡ no Grok Bot access; access first, then rebuild
- url: https://forum.cursor.com/t/grokbot-cant-connect/171703
- date: OP 2026-09-15; deanrie diagnose 2026-09-19; **deanrie unify teach 2026-09-23 18:24 UTC** (post–Wed-packet staff land)
- tags: networking, teach-once, killed-claim, access/billing, Reset
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·access·teach-once·killed-claim] score=9 | GFP | “Can’t reach your computer” + Reset/Recover always fail; VPN/AV/reinstall didn’t help. **deanrie (Sep 19): not a Mac network issue — account used up free trial / no Grok Bot access**; server rejects computer requests; UI wording misleading. Needs paid Cursor individual / Teams / linked eligible SuperGrok. **deanrie (Sep 23 elevate):** “Reset failed / partial computer state” and “no access / needs upgrade” are **the same root cause**. Order: **access first, then clean rebuild**. Until access is active, don’t Reset/Recover — they won’t work; teammate inspection hits the same wall. After subscribe: fully quit (menu bar) + reopen + same account. If plan active but still failing → Request ID (Privacy Mode off). Alert: **no** (durable standing-kill; billing/access path, not Field roster).
- staff: deanrie
- bank-body: /workspace/field/bank-bodies/bank-body-171703.txt (+ forum0924 copy)
- note: older topic; **new portable staff unify teach landed Wed evening** after Wed packet — elevate as Thu KEEP.

## OVERFLOW / watch (not packet KEEP)

### Vikas_Dakshi 172696 — Can’t reach; Recover/Reset fail at 50%; **staff: Mac DNS**, don’t Reset (elevate→reinforce Kin_Su)
- deanrie 2026-09-23 04:33 UTC: computer healthy on server; each Recover/Reset created a new computer in ~1 min; **Mac can’t resolve** address app uses (`nslookup test.us12.cursorvm.com` vs `… 1.1.1.1`). Don’t Reset again. Fix: System Settings → DNS add 1.1.1.1 + 8.8.8.8; fully quit+reopen; wait ~2 min. Same-ISP hotspot usually won’t help. Score≈8 — **reinforce Kin_Su DNS standing**, do not KEEP. Alert: no.

### aliciar 172725 — new-account first-init incomplete; staff rebuild; don’t Reset/Update
- deanrie: first startup unfinished; Reset/Update from app can’t complete; known server-side. mohitjain rebuilt; OP confirmed fixed. Bot name/settings Mac↔iOS sync goes through computer. **Reinforce first-init incomplete** standing. Alert: no.

### Orel 172737 / nhog 172535 / Raymond_Bell / Mister_Deed / toneill — 43% Transferring pile-on
- mohitjain (Orel): server-side; bots/files safe; quit+reopen; no Update/Recover/Reset/reinstall. kevinn (nhog thread): auto Update copy-step; don’t Reset; mobile works during dialog. **Reinforce Update/Reset hung 43% + nhog don’t-Reset**. Do not KEEP. Alert: no.

### Timothy_Gresh 172549 — Windows endpoint security process-kill under CopyFromBox+Chrome (Wed overflow)
- No new staff since Wed. **Reinforce** Windows AV / process-kill family ≈8 overflow. Alert: no.

### Peacerk 172618 — can’t reach + AdGuard disabled still fails
- Still thin OP; **no staff**. Bounce/soft watch. Alert: no.

### Sonya_Phillips 172774 — Android login stuck “Waiting for Browser…” (deep-link callback)
- Chromebook OK; Android 1.11.1 Samsung; browser “All set” → app stuck. **No staff yet.** Watch (login/deep-link). Alert: no.

### Chris_Clarke 172797 (+ Waleed_Khalid pile) — CoS stuck turn / dead ListAgents tool; “working” forever
- Turn stuck calling nonexistent ListAgents; workers OK. No staff. Soft **one-bot silent / stuck-turn** watch. Alert: no.

### David.J 172836 — macOS 0.58.0 bot screen-view UI disappeared
- Preview/click-to-open screen gone. OP-only. Soft UX watch. Alert: no.

### Bernie_Ladoucur 172716 — bot failed / no respond; kevinn server reset; still failing after logout
- Account-stuck / backend cousin; no durable new teach. Soft reinforce. Alert: no.

### Raymond_Weiss et al. 172371 — bots silent; mohitjain server stall; don’t Reset
- Soft one-bot-silent reinforce. Alert: no.

## BOUNCE

### Already-kept / standing reinforce (do not KEEP)
- dnz 172578 — Wed KEEP skip (mohitjain follow-up: office DNS / hotspot OK)
- codercurtis 172307 — Wed KEEP skip
- Ryan_Daley 172545 — Wed overflow banked (queue latency)
- Michael_Pan 172494 / chrisoh806 172401 / BigBojangles 172349 / Volkan / Anderson / Dave / allninety
- Vikas 172696 — Kin_Su DNS reinforce (staff landed; not new KEEP)
- aliciar 172725 — first-init reinforce
- nhog 172535 / Orel 172737 — 43% family
- Timothy 172549 — AV process-kill overflow only

### Non-failure / UX / FR / Cloud Agents / meetup / billing
- jsolly 172798 — printer FR; kevinn: cloud agent can’t see home printers; send file to registered Mac
- geminga 172822 — per-agent reasoning effort FR; kevinn: not available yet
- AndrewC 172769 / 172777 — billing / orchestration feedback
- SmokedMeats 172712 — Slack account switch (self-fixed GitHub reconnect)
- ConstantineX on 170358 — routines late pile-on (Ryan queue teach already banked)
- doughy 171895 — update_state brain-docs snapshot; OP says fixed
- TheAviv 172600 — multi-GB review video capability
- Sonya/Raymond edu plan ask 172773 — pricing FR not failure
- Meetup stubs 172743–172748 — bounce
- 172705 / 172584 — fleet spend / Ultra usage FR
- 172713 My Machines controller_disconnected — Cloud Agents (not forever-box)
- 171877 MCP OAuth redirect_uri — MCP auth
- 172524 1Password vault-only — security FR (resolved UX clarity)
- 169904 shared team roster FR
- 172740 Grok bot replace Cursor? — discussion
- Gideon 171091 — OP marked Resolved

## Fetch notes
- `c/grok-bot/l/latest.json` and `c/grok-bot/33.json` → **404** (invalid category); used `tag/grok-bot/l/latest.json` + `?page=1` + search after:2026-09-22 / after:2026-09-23 + keyword sweeps (stuck, reconnecting, can't reach, Reset, local execution, routines).
- Saved under `/workspace/field/forum0924/`
- Priority topics fully read: 172715, 171703, 172696, 172725, 172737, 172716, 172797, 172836, 172774, 172535, 172549, 172618 (+ tag/search listings)
- Bank INDEX grepped — no prior deposits for 172715 / 171703
- Appended newly fully-read topic ids to seen-forum-ids.txt (now 292)

## Bank deposits (bodies ready for bank.py)
- KEEP: `bank-bodies/bank-body-172715.txt` ← Chexander 172715
- KEEP: `bank-bodies/bank-body-171703.txt` ← GFP 171703
- Overflow optional: `bank-body-172696.txt` (Vikas DNS), `bank-body-172725.txt` (aliciar first-init)

## Result for compiler
- FAILURES recommend: **2** (Chexander 172715 score=10 — route-through rejects RFC1918 / split-horizon; use desktop Shell; GFP 171703 score=9 — Reset-fail/partial ≡ no access; access first). Edu SETUPS take remaining cap slots if tight — prefer **Chexander** if only one friction slot.
- Soft overflow: Vikas 172696 DNS reinforce≈8; Timothy 172549 AV≈8; Sonya 172774 Android deep-link watch; Chris_Clarke 172797 stuck-turn watch
- KILLED mirror: (1) Route-through “works” counter ≠ internal DEV reachable — **private IPs rejected**; use desktop execution. (2) Can’t-reach + Reset/partial ≠ broken Mac — often **no Grok Bot plan access**; don’t Reset until subscribed.
- Related reinforce (not KEEP): Orel/nhog 43%; aliciar first-init; 172371 stall; Bernie 172716; Peacerk thin
- Alert: **none**
