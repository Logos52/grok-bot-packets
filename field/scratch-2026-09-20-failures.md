# Field Grok Bot failure hunt · packet 2026-09-20 (Sunday)
Cutoff: after ~2026-09-18/19 00:00 UTC (post Saturday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+after:2026-09-18` (+ `after:2026-09-19`). Category `c/grok-bot/33.json` → invalid (skip). Public, no login. No Firecrawl. No X. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Sat KEEP Volkan_Erdogan 172135 (first-init incomplete Recover/Reset fail-at-50% chat-OK); Sat KEEP Anderson_V_Leite 172142 (Windows “partial state” = Kaspersky encrypted-scan; Reset never hit servers). Fri KEEP Dave_Campos 172070; Fri KEEP allninety 171962. Thu KEEP ziemovit 171791; Thu KEEP Mercer_Alex 171840. Wed KEEP Kostadin_S 171735; Wed KEEP Nathan_Arizona 171676. Standing: Catty Kaspersky / Andrew Zscaler / Serene usage-silent / Kin_Su DNS / thomas2018 webhook / Channels_Cintara Update-Computer auth. Overflow re-check: Nads_D_Etc 171858 fleet hub — no elevate.

## KEEP candidates (1) — recommend for packet (edu setups take priority for cap)

### KEEP 1 — BigBojangles · CopyFromBox/Read limited to user profile (local-exec root); Shell OK — don’t Reset; use Shell or home-then-move
- url: https://forum.cursor.com/t/copyfrombox-and-read-refuse-paths-outside-user-profile-after-0-57-1-outside-the-allowed-local-exec-root/172349
- date: OP 2026-09-19 14:05 UTC; deanrie 2026-09-19 15:32 UTC
- tags: killed-claim, persistent-computer, gui-as-api, teach-once
- score: 9 (portable 5 / evidence 4)
- packet one-liner: [agentic·killed-claim·persistent-computer·gui-as-api] score=9 | BigBojangles | Windows registered machine: **CopyFromBox / Read / CopyToBox** refuse paths outside `C:\Users\<you>` with “outside the allowed local-exec root” (noticed ~0.53.0, still on 0.57.1); **Shell still reads/writes** D:/G: fine; junctions/symlinks from profile to other drives also rejected (real-path check). deanrie: **current local-machine design, not a broken disk**; workaround = CopyFromBox into home then Shell-move, or read/copy other drives via Shell (`Get-Content` / `Copy-Item`); team exploring file-tools=Shell scope OR bot should prefer Shell when limited. Teach: profile-only file tools + Shell-OK ≠ Reset/Recover/disk failure — **local-exec root ceiling**. Alert: **no** (durable diagnostic; not a this-week Field path/setting change unless you copy outside profile on a registered PC).
- staff: deanrie (local-exec root = by design; workaround; junctions rejected; team handoff)
- siblings: Mercer stuck-runner (different); Anderson/Catty AV HTTPS (different); Volkan first-init (different)
- bank: raw/ai/2026-09-20-bigbojangles-copyfrombox-local-exec-root.md

## OVERFLOW / watch (not packet KEEP)

### warpdev 172343 — Update/Reset stuck “Backup not ready” / endless “Transferring data”
- box-doctor PASS; no staff yet — watch for durable backup-gate teach.

### Emmjayed 172377 / Raymond_Weiss 172378 — stuck updating computer (43% / multi-hour)
- no staff yet — watch (cousin of Update stuck); don’t Reset advice pending.

### Carter-Ventucci 172368 — unusable since Sep 7; computer reachable; all bots fail; T-F65125
- allninety account-stuck cousin — bounce/reinforce; don’t Reset.

### TheAviv 172314 — Message failed to send; deanrie: short Sep 18 service window fixed; StupidYas: network flap (desktop only; Android OK; switch networks fixed)
- ops temporary + local network — bounce; don’t Reset already taught.

### bucheyu 172350 / Matt_Vine 172353 / Justin_Breiner 172354 — one-bot / CoS silent; ask restart runner only
- deanrie/Colin: Mercer stuck-runner reinforce; merged 171858 — bounce; **do not elevate**.

### Raymond_Weiss 172371 — bots not responding again — Mercer/Nads reinforce — bounce.

### Aerospace 172372 — “Grop project / Fable” vent — not a portable teach — bounce.

## BOUNCE
### Already-kept reinforced
- Volkan 172135 / Anderson 172142 — Sat KEEP skip
- Dave_Campos 172070 / allninety 171962 — Fri
- ziemovit / Mercer — Thu; 172350/353/354 Mercer siblings
- Serene / Kin_Su / Catty families — standing

### Ops / merges
- Mass merge into 171858 continues
- 172314 service-window fixed + network diagnosis

## Fetch notes
- Tag latest p0–p1 + search after:2026-09-18 / after:2026-09-19 → `/workspace/field/forum0920/`
- Priority topics fetched: 172349, 172314, 172343, 172350, 172353, 172354, 172368, 172371, 172372, 172377, 172378
- `c/grok-bot/33.json` skipped
- Bank INDEX grepped — no prior 172349
- Appended new topic ids to seen-forum-ids.txt on compile

## Bank deposits
- KEEP: `raw/ai/2026-09-20-bigbojangles-copyfrombox-local-exec-root.md` ← 172349

## Result for compiler
- FAILURES recommend: **1** (BigBojangles 172349) — edu SETUPS take remaining cap slots
- KILLED mirror: local-exec root file-tools vs Shell
- Alert: **none**
