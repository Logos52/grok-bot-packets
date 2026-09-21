# Field Grok Bot failure hunt · packet 2026-09-21 (Monday)
Cutoff: after ~2026-09-19/20 00:00 UTC (post Sunday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+after:2026-09-19` (+ `after:2026-09-20`). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Sun KEEP BigBojangles 172349 (local-exec root CopyFromBox/Read profile-only; Shell OK). Sat KEEP Volkan_Erdogan 172135; Sat KEEP Anderson_V_Leite 172142. Fri KEEP Dave_Campos 172070; Fri KEEP allninety 171962. Thu KEEP ziemovit 171791; Thu KEEP Mercer_Alex 171840. Wed KEEP Kostadin_S 171735; Wed KEEP Nathan_Arizona 171676. Standing: Catty Kaspersky / Andrew Zscaler / Serene usage-silent / Kin_Su DNS / thomas2018 webhook / Channels_Cintara Update-Computer auth / first-init incomplete / Windows partial-state AV. Overflow re-check: Nads_D_Etc 171858 fleet hub — no elevate; Mercer siblings 172350/353/354; Carter 172368 (deanrie replica teach reinforce — see overflow); warpdev 172343; Emmjayed/Raymond → merged into 172401 KEEP hub.

## KEEP candidates (1) — recommend for packet (edu setups take priority for cap)

### KEEP 1 — chrisoh806 · Update stuck at 43% “Transferring your data” = backend rehydrate fail; wait / Recover after “update failed”; don’t Reset/uninstall
- url: https://forum.cursor.com/t/grokbot-unavailable-hung-on-updating-grok-bots-computer-at-43/172401
- date: OP 2026-09-20 06:34 UTC; Colin 2026-09-20 08:12 UTC; still getting me-toos through 2026-09-20 21:56 UTC
- tags: killed-claim, persistent-computer, teach-once, coverage-ceiling
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·persistent-computer·teach-once] score=9 | chrisoh806 (hub) | Multi-user **Update/Reset hung at 43% Transferring your data** (0.57.1 Win+Mac); chat blocked; Recover button often absent while dialog spins. Colin: **known backend rehydrate-during-recreation failure**; most boxes come up on their own eventually; team investigating. Community path (Joseph_Ridenour / support): known issue → computer flips to **“update failed”** → then **Recover** restores bots/files. Merges: Emmjayed 172377, Raymond_Weiss 172378, Alex_Cao 172382 (self-resolved Recover), Chris_Garbacz 172386, Zomer 172431 cousin. Teach: **43% Transferring ≠ local disk/VPN**; don’t Reset again / don’t uninstall / don’t re-Update while spinning; wait or wait-for-failed-then-Recover; data usually preserved. Alert: **no** (ops incident + durable don’t-Reset teach; not a this-week Field path/setting change).
- staff: Colin (rehydrate fail; wait; investigating)
- siblings: warpdev 172343 Backup-not-ready (related gate, box still healthy); UCC3 172453 unreachable-while-routines-run (attach cousin, no staff yet); Volkan first-init 50% (different); Carter replica (different)
- bank: raw/ai/2026-09-21-chrisoh806-colin-grokbot-unavailable-hung-updating-at-43.md

## OVERFLOW / watch (not packet KEEP)

### UCC3 172453 — unreachable Win+phone since Sep 20 evening KST; routines still run; no Recover/Reset pressed
- No staff yet. Strong attach/rehydrate cousin of 172401 (routines prove cloud partly alive). Watch for staff durable teach → possible elevate Tue.

### jsolly 172015 — mobile Settings scroll activates toggles (can flip Auto-review / “Agent guards”)
- kevinn staff: reproduced iOS; scroll-from-switch flips control; protective control = **Auto-review** (not labeled Agent guards); start scroll on row text. Score≈8 durable human-gate friction — **not packet KEEP** (edu cap; not killed/computer). Soft promote if compiler has a free friction slot. Alert: no.

### warpdev 172343 — “Backup not ready” blocks Update; Reset Transferring endless; box-doctor PASS
- Colin: box healthy again. OP clarify: healthy runtime ≠ update unblocked; Settings still Backup not ready (T-F98010). Watch; no new durable teach beyond 172401 cousin.

### Carter-Ventucci 172368 — deanrie NEW teach (Sep 20): routed to dead runtime replica since Sep 8; Reset rejected server-side; backend cleanup; don’t Reset/Recover/Update
- Elevates Sun overflow with mechanism detail, but **allninety account-stuck family** already kept Fri — reinforce only, do not second-KEEP.

### Sanghoon_Kang 172009 — parent bot quiet while delegated Cloud Agents run (by design)
- Colin: intentional wake-on-finish; watch at cursor.com/agents; ask parent to attach agent card. FR/observability — bounce for failure hunt.

### doughy 171895 — update_state memory “brain docs snapshot was cut short”; file-append workaround; don’t Reset
- deanrie confirmed; pre-cutoff (Sep 16) + never in seen list — bank-worthy but **out of window**; note for compiler backlog, not Mon KEEP.

## BOUNCE
### Already-kept reinforced
- BigBojangles 172349 — Sun KEEP skip
- Volkan 172135 / Anderson 172142 — Sat
- Dave_Campos / allninety — Fri; Carter reinforce
- Mercer siblings 172350/353/354 / Nads 171858 fleet — no elevate
- Emmjayed 172377 / Raymond 172378 / Alex_Cao 172382 / Chris_Garbacz 172386 — merged into 172401 hub

### Standing families / misdiagnosis
- Max_Maldonado 171808 — Kaspersky encrypted-scan = Catty family (fixed)
- GFP 171703 — “Can’t reach” = trial/access exhausted (Serene cousin); misleading copy
- Luke_Adams 171947 — usage exhausted (Serene)
- Kamil_Senk 172003 — corporate network can’t reach servers (Kin_Su/Andrew cousin)
- nitesh_sharma 170954 — ops “Failed to Respond”; don’t Reset (old)

### Non-failure / UX / events
- David_Stredansky 172445 — praise “got faster”
- Johnsters 171745 — product confusion (deanrie Cursor vs Grok Bot explain)
- jsolly 172380 — iOS Vercel plugin sheet stuck “Added” (force-quit; Colin steps)
- jsolly 172381 — FR show real plugin account identity
- jsolly 171950 — mobile UI rename doesn’t stick; agent self-rename works (mohitjain)
- Meetup event stubs 172403–172409 — bounce

## Fetch notes
- Tag latest p0–p1 + search after:2026-09-19 / after:2026-09-20 → `/workspace/field/forum0921/`
- Priority topics fetched: 172453, 172401 (+extra posts), 172431, 172382, 172386, 172380, 172381, 172015, 170242, 171950, 172003, 171947, 172074, 171703, 170954, 172009, 171895, 172343, 172377, 172378, 172368, 171858, 172445, 171745, 171808
- `c/grok-bot/33.json` skipped
- Bank INDEX grepped — no prior 172401
- Appended fully-read new topic ids to seen-forum-ids.txt (this hunt)

## Bank deposits
- KEEP: `raw/ai/2026-09-21-chrisoh806-colin-grokbot-unavailable-hung-updating-at-43.md` ← 172401

## Result for compiler
- FAILURES recommend: **1** (chrisoh806 172401 hub — 43% rehydrate) — edu SETUPS take remaining cap slots
- Soft overflow promote if slot: jsolly 172015 (mobile scroll flips Auto-review) score≈8
- KILLED mirror: Update/Reset 43% Transferring = backend rehydrate; wait / Recover-after-failed; don’t Reset/uninstall
- Alert: **none**
