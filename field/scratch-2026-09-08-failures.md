# Field Grok Bot failure hunt · packet 2026-09-08 (Tuesday)
Cutoff: after ~2026-09-07 00:00 UTC (post packet Monday / 2026-09-07 keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+order:latest`. Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Jojo1 170809, TheAviv 170816, noname 170736, jsolly 170727, Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710, andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, Effective_Autism 170819 (+ URLs in scratch-seen-urls.txt).

## KEEP candidates (3)

### KEEP 1 — Human_111425250 · CallDynamicTool nests namespace/toolName → SendToAgent/Task dead until teach-once
- url: https://forum.cursor.com/t/grok-bot-calldynamictool-fails-missing-namespace-toolname-sendtoagent-task-broken/170869
- date: 2026-09-07 09:18 UTC (16:18 ICT 7 Sep)
- tags: killed-claim, teach-once, human-gate
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·teach-once] score=10 | Human_111425250 | Since ~Sun 6 Sep 21:45 Europe/London, one agent (Maturin) fails every `CallDynamicTool` with **Missing required fields: namespace, toolName** — even when those fields are supplied nested/flattened in args. Breaks SendToAgent, Task/browserUse/computerUse, CreateAgent/UpdateAgent, SearchPlugins/WebSearch via same path. Shell/files/memory/routines OK; GetDynamicTools still lists tools; Reset Computer no-ops (history not on computer). Staff deanrie: calls reached backend **without top-level `namespace`/`toolName` beside `arguments`** (likely nested inside `arguments`); once a few bad shapes land in chat history the bot **repeats the same shape**. Fix step 1 (worked): tell the bot *“When you call CallDynamicTool, namespace and toolName must be top-level keys alongside arguments, never inside arguments. Send a one-line hello to one of your teammates now using that shape.”* Step 2 if needed: Duplicate bot (fresh history). Killed: multi-agent / Task orchestration is dead until the call-shape teach-once sticks. Alert: **yes** — paste teach-once into Field multi-agent / CallDynamicTool instructions this week; prefer Duplicate over Reset if history is poisoned.
- staff: deanrie 2026-09-07 09:42 UTC — top-level shape; teach-once then Duplicate.
- siblings: none exact; adjacent to any SendToAgent / Task / plugin-via-CallDynamicTool friction.
- bank: raw/ai/2026-09-08-human-111425250-grok-bot-calldynamictool-fails-missing-namespace.md

### KEEP 2 — Archit · Synced skills only reach Cloud Agents from Agents Window — not Grok Bot / web
- url: https://forum.cursor.com/t/sync-skills-for-cloud-agents-stuck/170899
- date: 2026-09-07 13:20 UTC (20:20 ICT 7 Sep)
- tags: coverage-ceiling
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·coverage-ceiling] score=9 | Archit | Cursor Agents Window “Sync Skills for Cloud Agents” stuck on **Syncing 58 of 58** (UI hang). Staff deanrie: download already finished; hang is final verification (`reason=missing` / “destination is not serving the migrated skills yet”) — known. Separate **first-party gap** (staff×2): synced skills are picked up **only** by Cloud Agents started from desktop Agents Window / IDE. Agents started from **Grok Bot** and from **cursor.com/agents** do **not** get them yet — not a user-config bug. Workaround: start Cloud Agent from Agents Window (OP confirmed skills/commands work there; web still no). Killed: don’t design Grok Bot → Cloud Agent handoffs that assume local `~/.cursor/skills` travel with the spawn. Alert: **no** (workaround exists; education/tutor lane rarely depends on Cloud Agent skill sync this week).
- staff: deanrie 2026-09-07 17:03 + 18:27 UTC — UI hang known; Grok Bot / web coverage gap flagged.
- siblings: none prior Field keep for this gap.
- bank: raw/ai/2026-09-08-archit-sync-skills-for-cloud-agents-stuck.md

### KEEP 3 — jsolly · stdio MCP command path under deleted agent secrets → ENOENT forever
- url: https://forum.cursor.com/t/grok-bot-stdio-mcp-keeps-spawn-path-into-deleted-agent-secrets/170901
- date: 2026-09-07 13:33 UTC (20:33 ICT 7 Sep)
- tags: ownerless-work, persistent-computer
- score: 7 (portable 4 / evidence 3)
- packet one-liner: [agentic·ownerless-work·persistent-computer] score=7 | jsolly | Stdio MCP connectors store executable paths under `/home/box/agent-data/agents/<agentId>/secrets/...`. After agent delete / empty “New Agent” shell, spawn still points at dead tree → **ENOENT** (e.g. `spawn …/agents/fca450d8-…/secrets/alpaca-mcp.sh`). Symlink into deleted agent `2a4856ef-…`. RestartMcpServers does not recreate missing file. Manual restore of real wrapper + RestartMcpServers recovered alpaca-paper / alpaca-paper-read / alpaca-judge. Killed: never host shared MCP wrappers only under a deletable agent’s secrets; use a shared path outside agent trees, or re-point command after delete. No staff yet (evidence 3). Alert: **no** (hygiene for MCP installers; not a this-week Field file change unless deleting agents that own MCP scripts).
- staff: none
- siblings: jsolly 170900 (needsAuth status stuck after Authenticate says connected — bounce, status-only); jsolly 170898 GitHub no sign-in link; 170895 Todoist PKCE first-attempt; 170891 Ahrefs rate-limit (Colin staff, vendor-specific bounce).
- bank: raw/ai/2026-09-08-jsolly-grok-bot-stdio-mcp-keeps-spawn.md

## BOUNCE

### Staff-confirmed but not new portable keep
- Diazb123 170915 / Eric_Han 170834 / Alex_Such 170897 / bit0rbit 170912 / Tristen 170902 / Velaria 170972 / konstantinosgr-png 170920 — **Bot failed to respond** / create-bot fail while Agent Computer still visible; deanrie/Colin: backend computer unresponsive, don’t Reset/Update/logout; recovery list. **im_grok / oscar_mei cluster** — ops, not new mechanism https://forum.cursor.com/t/chief-agent-grok-bot-failing-to-respond/170915
- Matt_Fuller1 170932 — `Model name is not valid: "grok-4-7-0907"` ~20 min first-party model-config blip Mac/iOS/Android; deanrie confirmed restored — transient ops https://forum.cursor.com/t/model-name-is-not-valid-grok-4-7-0907-grok-bot/170932
- Aleks_E@170775 — after sign-out/in still “No saved Bots yet” + `*.cursorvm.com`; deanrie: **distinct from password-revoke costume** — account↔computer mapping needs hi@cursor.com, no Reset. Strengthens andyfraussen/_Remi ops path; not a copyable Field mechanism this week https://forum.cursor.com/t/grok-bot-lost-connection-with-its-computer-and-cant-update-recover-reset/170775
- Ronald_Naners 170743 black screen white-dot — mohitjain restored computer; OP recovered https://forum.cursor.com/t/stuck-on-black-screen-with-white-dot-after-setting-up-grok-bots-computer/170743
- Bradley_Street 170721 / StefanZ 170710 — main-pane replies missing; resurfaced on all devices 7 Sep — **StefanZ/noname secret-card cluster**, already kept
- jsolly 170891 Ahrefs `failed_to_load` — Colin: Ahrefs rate-limits Grok Bot connect attempts; wait for backoff change — vendor-specific coverage, not Field-portable https://forum.cursor.com/t/grok-bot-ahrefs-plugin-fails-with-failed-to-load-connector/170891
- TheAviv 170832 Gmail Spam `search_threads` empty — deanrie: Gmail search excludes Spam/Trash by default; try `in:anywhere label:SPAM` (OP retest inconclusive when Spam empty) — MCP coverage, bounced yesterday as thin for FAILURES lane https://forum.cursor.com/t/grok-bot-gmail-search-threads-returns-empty-for-spam-while-list-labels-shows-threads/170832

### Thin / no staff / FR / already-kept
- notdimax 170971 bots vanished after Alt+Tab during setup (no staff) · MWT 170963 auth loop · David_Stredansky 170957 Recover hang self-healed · idan_lin 170926 Public template “team must be selected” on personal Ultra (no staff; publish coverage) · jsolly 170900 needsAuth status mismatch · jsolly 170898 GitHub no sign-in link · jsolly 170895 Todoist PKCE first-attempt (retry OK) · jsolly@170727 new repro `node --experimental-strip-types` bind (already-kept Auto-review cluster / Jojo1) · o_Oaii 170358 routines still not auto-running (already kept) · quota FR threads 170951/170875/170742/170771 · QuickBooks FR 168579 · SuperGrok vs Ultra 170888 · memory export 170714

### Already-kept (window)
- Jojo1 170809 · TheAviv 170816 · noname 170736 · Effective_Autism 170819 · jsolly 170727
- Jarri81 170683 · Winvicta 170691 · Benjamin_Barber 170689 · StefanZ 170710
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` page 0 + page 1; `search.json?q=Grok+Bot+order:latest` (50 posts)
- Priority NEW topic IDs fetched 200 → `/workspace/field/forum0908/{id}.json`: 170869, 170899, 170901, 170900, 170898, 170895, 170891, 170915, 170932, 170926, 170920, 170971, 170972, 170963, 170957, 170912, 170902, 170897, 170843, 170834, 170832, 170775, 170721, 170743
- Also saved tag-p1.json; search.json present in folder
- Public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior entries for 170869/170899/170901

## Bank deposits
- KEEP: `raw/ai/2026-09-08-human-111425250-grok-bot-calldynamictool-fails-missing-namespace.md` ← 170869
- KEEP: `raw/ai/2026-09-08-archit-sync-skills-for-cloud-agents-stuck.md` ← 170899
- KEEP: `raw/ai/2026-09-08-jsolly-grok-bot-stdio-mcp-keeps-spawn.md` ← 170901

## Packet recommendation
Keep count: **3** — Human_111425250 170869, Archit 170899, jsolly 170901. Cap ~2–3 FAILURES for packet (compiler total cap 5 with education). Prefer 170869 + 170899 if compiler must cut to 2 (staff×2, clearer gates). **Alert: yes** (Human_111425250 only — CallDynamicTool teach-once: `namespace`/`toolName` top-level beside `arguments`; Duplicate if history poisoned). Clusters noted: Bot-failed-to-respond backend wave (170915/834/897/912/902/972/920) = im_grok ops; jsolly MCP burst (901/900/898/895/891); Auto-review bind siblings already kept. No packet file written. field-seen.json not edited.
