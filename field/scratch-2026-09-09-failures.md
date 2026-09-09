# Field Grok Bot failure hunt · packet 2026-09-09 (Wednesday)
Cutoff: after ~2026-09-08 00:00 UTC (post Monday/Tuesday packet keeps). Forum via public topic JSON + `tag/grok-bot/l/latest.json` pages 0–1 + `search.json?q=Grok+Bot+order:latest`. Public, no login. No Firecrawl. No X. Scratch only — no packet file. field-seen.json untouched.

Already kept/seen (skipped): Human_111425250 170869 (CallDynamicTool — ALERTED yesterday), Archit 170899, jsolly 170901 (overflow), Jojo1 170809, TheAviv 170816, noname 170736, jsolly 170727, Jarri81 170683, Winvicta 170691, Benjamin_Barber 170689, StefanZ 170710, andyfraussen 170568, _Remi 170438, George_Burchell 170607, jumpsuitgroup 170486, LLMTester 170523, digvijaysai_g 170315, o_Oaii 170358, im_grok 170373, Chip_Randa 170489, Effective_Autism 170819 (+ URLs in scratch-seen-urls.txt).

## KEEP candidates (3)

### KEEP 1 — Wes_Anderson · Desktop reconnect overwrites in-chat secrets store
- url: https://forum.cursor.com/t/grok-bot-box-secrets-wiped-overnight-shopify-client-id-secret/171029
- date: 2026-09-08 11:49 UTC (18:49 ICT 8 Sep)
- tags: persistent-computer, killed-claim, teach-once
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·teach-once·persistent-computer] score=10 | Wes_Anderson | Shopify Client ID/secret stored via **in-chat secure input** wiped twice overnight without Update/Reset. Daily 5am CT routine then could not mint Admin token after secrets empty (token file on disk survived until expiry). Staff Colin: when Grok Bot **desktop reconnects** (PC sleep / connection drop), it **re-syncs the desktop’s own secrets list onto the computer and overwrites** anything saved through in-chat secure input — matches evening wipe timestamps. OP confirmed: close→reopen Desktop wiped credentials that were fine before. Killed: never treat box secrets from chat secure-input as sole durable store if Desktop is in the loop; re-seed after Desktop wake, keep a copy off-box, or prefer first-party connectors. Alert: **yes** — paste teach-once into Field/tutor bots that stash API keys via secure input this week.
- staff: Colin 2026-09-08 12:59 UTC — desktop reconnect secrets overwrite confirmed; tracking.
- siblings: jsolly 170901 (stdio MCP under deleted agent secrets — already kept); Shopify FR 170605.
- bank: raw/ai/2026-09-09-wes-anderson-grok-bot-box-secrets-wiped-overnight.md

### KEEP 2 — ellisfan · Duplicate Agent Computer → history/bots/groups rolled back across all devices
- url: https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008
- date: 2026-09-08 08:19 UTC (15:19 ICT 8 Sep)
- tags: killed-claim, persistent-computer, ownerless-work
- score: 10 (portable 5 / evidence 5)
- packet one-liner: [agentic·killed-claim·persistent-computer] score=10 | ellisfan (+Adam7, jay_desu, Brian_Miller2, notdimax, sleep-merge cluster) | Overnight/morning 8 Sep, conversation history after a cutoff + newly created bots/groups/routines **disappeared and synced the truncated state** to macOS/Windows/iOS. Support auto-replies said unrestorable; several users rebuilt; some later saw bots reappear. Staff Colin (19:12 UTC): some users were **mistakenly provisioned a duplicate computer**; sessions routed to the duplicate; fix removed duplicate and pointed accounts back to the computer with **most history** — may still miss conversations/state from the dual window. Merged siblings: 170980 / 171037 / 171043 (bots gone after Mac sleep). Portable gate: don’t treat Grok Bot chat/bot roster as sole durable ledger — keep external reconstruction (Adam7: Codex computer history). Don’t Reset/Recover during dual-computer incidents. Alert: **no** (incident marked fixed; teach is hygiene, not a this-week Field file change beyond optional external-ledger note).
- staff: Colin 2026-09-08 19:12 UTC — duplicate computer provisioning; reconciled to most-history copy.
- siblings: oubeichen 170989 (same incident, scheduled-task double-fire); Nicolas_Rodrigues 170788 (told “2 computers”); oryou 170986 (stale copy).
- bank: raw/ai/2026-09-09-ellisfan-grok-bot-conversation-history-rolled-back.md

### KEEP 3 — oubeichen · Same bots on two Agent Computers → duplicate scheduled tasks + desynced chats
- url: https://forum.cursor.com/t/same-grok-bot-split-into-different-instances-across-macos-and-android-causing-duplicate-scheduled-tasks-usage/170989
- date: 2026-09-08 05:49 UTC (12:49 ICT 8 Sep)
- tags: ownerless-work, persistent-computer
- score: 9 (portable 4 / evidence 5)
- packet one-liner: [agentic·ownerless-work·persistent-computer] score=9 | oubeichen | Same bot IDs appeared as **two backend instances** (macOS vs Android): scheduled tasks returned **different results**, chats no longer synced, Android desktop looked wiped/onboarding. Staff deanrie: ~7 Sep 17:00 UTC incident created a **second Agent Computer**; **both copies kept running scheduled tasks**; after Mac restart both clients pointed at one copy. Don’t click Reset/Recover/Update (can create another copy). Double usage → email hi@cursor.com. Killed: routines are not single-flight under dual-computer incidents — expect duplicate sends/side effects. Alert: **no** (same Sep-7 dual-computer cluster as 171008; fixed; overflow if compiler needs a third FAILURES slot for routines-specific gate).
- staff: deanrie 2026-09-08 07:08 UTC — second Agent Computer; both ran schedules; hold Reset.
- siblings: 171008 (history rollback after reconcile); 170788; 170986 stale-copy.
- bank: raw/ai/2026-09-09-oubeichen-same-grok-bot-split-into-different-instances.md

## BOUNCE

### Dual-computer / Bot-failed-to-respond ops wave (same Sep 6–8 backend cluster — not new mechanism beyond KEEP 2/3)
- Diazb123 170915 / nitesh_sharma 170954 / Yum_Cheng 171049 / simpleshadow 171059 / Greg_Tritthart 171087 / Alex_Such 170897 / Velaria 170972 / konstantinosgr-png 170920 / Tristen 170902 — **Bot failed to respond** / create-bot fail; deanrie/Colin/kevinn: backend computer unresponsive or rebuilt; don’t Reset. im_grok ops cluster. https://forum.cursor.com/t/chief-agent-grok-bot-failing-to-respond/170915
- PGT 171001 / oryou 170986 / Loni_Riw 171004 (trial ended costume) / B_Melo 171006 / Charles_Roe 171078 / Chirag_Mewada 171071 / Gideon 171091 / Liam_B 170987 / Nicolas_Rodrigues 170788 — can’t-reach / partial-state / stale-copy; staff recover. 170986 mohitjain: app on **stale copy** of computer (sibling of dual-computer).
- Ronald_Naners 170743 black screen — already bounced yesterday.

### Staff-confirmed but thin / vendor / FR / not FAILURES-portable
- idan_lin 170926 — Public template “team must be selected” on personal Ultra; mohitjain: leftover team workspaces; OP + support say no leftover teams — coverage FR, workaround failed https://forum.cursor.com/t/grok-bot-public-template-publish-fails-with-a-team-must-be-selected-to-share-a-team-template-on-personal-ultra/170926
- jsolly 170900 — needsAuth badge cosmetic for non-OAuth MCP (Fastmail/Cloudflare); mohitjain + Parth support — status-only, tools work https://forum.cursor.com/t/grok-bot-mcp-status-stays-needsauth-after-authenticatemcpserver-says-already-connected/170900
- jsolly 170895 — Todoist PKCE first-attempt; Colin: Todoist drops code_challenge in transit; retry OK — vendor/transient
- TheAviv 170832 — Gmail Spam search; deanrie: default excludes Spam; retest empty Spam — bounced yesterday, still thin
- Maaz_Kazi@168548 — cloud computer on older internal build can’t see healthy Mac helper; Colin: **Update Grok Bot’s Computer** — version-skew ops, not new gate
- Joe_LK 171036 — Slack wake FR (Cloud Agent Automations) — not FAILURES
- AYUSH_LIMBAD 171026 — DNS/*.cursorvm.com local network; deanrie: computer healthy

### Thin / no staff / quota / events
- Channels_Cintara 171107 auth loop · prashant_kumar1 171028 can’t reach · 171109 android small bug · 171108 clean your Grok · 171086 multi-user FR · 171043/171037/170980 merged into 171008 · 171010/170990/170771/170835 quota · 171013 meetup · 170985 API FR · 169982 credit pool · 168579 QuickBooks FR

### Already-kept (window)
- Human_111425250 170869 · Archit 170899 · jsolly 170901
- Jojo1 170809 · TheAviv 170816 · noname 170736 · Effective_Autism 170819 · jsolly 170727
- Jarri81 170683 · Winvicta 170691 · Benjamin_Barber 170689 · StefanZ 170710
- andyfraussen 170568 · _Remi 170438 · George_Burchell 170607 · jumpsuitgroup 170486 · LLMTester 170523
- digvijaysai_g 170315 · o_Oaii 170358 · im_grok 170373 · Chip_Randa 170489

## Fetch notes
- Tag latest: `tag/grok-bot/l/latest.json` page 0 + page 1; `search.json?q=Grok+Bot+order:latest`
- NEW/priority topic IDs fetched → `/workspace/field/forum0909/{id}.json` (30): 171008 (+extra posts), 171029, 170989, 171087, 171091, 171059, 171049, 171078, 171001, 171026, 171006, 170986, 171004, 170987, 170954, 171036, 170969, 168548, 170900, 170895, 170832, 171071, 170788, 171028, 170980, 171043, 171037, 170926, 170915, 171107
- 171008 posts_count 28 — fetched missing stream posts via `/t/171008/posts.json?post_ids[]=…` → 171008-extra.json
- IDs derived from feed JSON (`fetch-ids.txt`); public cooked HTML stripped; no login; no Firecrawl; no X
- Bank INDEX grepped before deposit — no prior entries for 171029/171008/170989
- bank.py Auto-review blocked; raw md written under `raw/ai/`; `index.jsonl` / `INDEX.md` **not** updated (approval denied — parent may `python3 scripts/bank.py --index`)

## Bank deposits
- KEEP: `raw/ai/2026-09-09-wes-anderson-grok-bot-box-secrets-wiped-overnight.md` ← 171029
- KEEP: `raw/ai/2026-09-09-ellisfan-grok-bot-conversation-history-rolled-back.md` ← 171008
- KEEP: `raw/ai/2026-09-09-oubeichen-same-grok-bot-split-into-different-instances.md` ← 170989
- Note: INDEX/index.jsonl not refreshed (tooling block).

## Packet recommendation
Keep count: **3** — Wes_Anderson 171029, ellisfan 171008, oubeichen 170989. Cap ~2–3 FAILURES (compiler total cap 5 with education). Prefer **171029 + 171008** if cut to 2 (distinct gates: secrets overwrite vs dual-computer history rollback); 170989 is same Sep-7 dual-computer incident with routines-specific surface. **Alert: yes** (Wes_Anderson only — Desktop reconnect overwrites in-chat secure-input secrets; re-seed / off-box copy / prefer connectors). Do **not** re-alert CallDynamicTool 170869. Clusters: Bot-failed-to-respond / can’t-reach wave = ops under dual-computer; jsolly MCP status cosmetic; public-template team gate still broken for OP. No packet file written. field-seen.json not edited.
