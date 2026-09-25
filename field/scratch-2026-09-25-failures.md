# Field Grok Bot failure hunt · packet 2026-09-25 (Friday)
Cutoff: after ~2026-09-23/24 UTC (post Thu packet KEEP Chexander 172715 + GFP 171703 — **do not re-keep**). Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-24` (+ `after:2026-09-23`) + keyword friction searches (stuck, reconnecting, routines, route traffic; Reset/can't reach/local execution/Update → **429** rate-limit). Category `c/grok-bot/l/latest.json` and `c/grok-bot/33.json` → **404 invalid** (skip; use tag+search). Public, no login. No Firecrawl. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Thu KEEP Chexander 172715 (route-through rejects RFC1918/split-horizon; use desktop Shell/browser); Thu KEEP GFP 171703 (Reset-fail/partial ≡ no Grok Bot access; access first). Wed KEEP dnz 172578; Wed KEEP codercurtis 172307; Wed overflow Ryan_Daley 172545. Tue KEEP Michael_Pan 172494; Mon KEEP chrisoh806 172401; Sun KEEP BigBojangles 172349; Sat KEEP Volkan / Anderson; Fri KEEP Dave / allninety. Standing footer: Catty Kaspersky / Kin_Su DNS / Zscaler / server-routines webhook / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access**. Do not re-alert footer list.

Elevate watches from Thu IF staff landed: Vikas_Dakshi 172696, Timothy_Gresh 172549, aliciar 172725, Orel/nhog 43%, Sonya_Phillips 172774, Chris_Clarke 172797, Peacerk 172618, David.J 172836, Bernie_Ladoucur 172716 — **only if new portable staff teach**; else reinforce/bounce.

## KEEP candidates (1) — recommend for packet (edu setups take priority for cap; compiler pick top 1–2 if slot-tight)

### KEEP 1 — TheAviv · Always allow = text instruction, not per-tool; prefer broader manual Auto-review Rules
- url: https://forum.cursor.com/t/auto-review-still-prompts-after-always-allowed-standing-approval/172859
- date: OP 2026-09-24 05:02 UTC; deanrie staff 2026-09-24 07:38 UTC (+ follow-up 13:51 UTC)
- tags: auto-run, teach-once, auto-review, Always-allow, standing-approval
- score: **10** (portable 5 / evidence 5)
- packet one-liner: [agentic·teach-once·auto-review·Always-allow] score=10 | TheAviv | Auto-review keeps popping approval cards for the same Gmail trash class after standing approval in chat **and** after Always allowed created for that tool; later similar action still “Allowed once” + new card. **deanrie: Always allow saves the rule as a text instruction, not a strict per-tool permission** — Auto-review may treat the next similar action as outside the rule. **Workaround:** Settings → Auto-review → Auto-review Rules → When Grok Bot wants to: broader phrase (e.g. “move emails in my Gmail to trash”) → Allow automatically → Add Rule. **Rules list has a size limit and evicts oldest** — delete narrow Always-allow trash entries so the broader rule isn’t pushed out. If rules conflict, **Ask first takes priority**. Docs: Approvals and Auto Review. Strict per-tool approval: tracked, no ETA. Alert: **yes** (copyable Auto-review Rules mechanism; Wedge would change Settings → Auto-review Rules THIS WEEK — broader rules + prune Always-allow clutter).
- staff: deanrie
- bank-body: /workspace/field/bank-bodies/bank-body-172859.txt (+ forum0925 copy)
- bank: raw/ai/2026-09-24-theaviv-auto-review-still-prompts-after-always.md

## OVERFLOW / watch (not packet KEEP)

### Peacerk 172618 — can’t reach + AdGuard; **staff: Free plan = no Grok Bot access** (elevate→reinforce GFP)
- deanrie 2026-09-24 09:30 UTC: not network; AdGuard not involved; turn protection back on. Forum account on **Free plan** — server never creates a computer; “can’t reach / having trouble connecting” wording is misleading. Nothing to Reset/restore. Needs paid individual / Teams / linked SuperGrok (+ free 1-week trial). Same root as GFP 171703. Score≈9 mechanism but **already Thu KEEP** — reinforce standing kill, do not KEEP. Alert: no.

### Sonya_Phillips 172774 — Android “Waiting for Browser…”; **staff Samsung deep-link teach** (elevate from Thu watch→overflow)
- mohitjain 2026-09-24 06:45 UTC: Samsung — Apps → Grok Bot → Battery **Unrestricted**; Battery care → not under Sleeping/Deep sleeping; sign in again; the moment browser says “All set!”, switch straight back via Recents. If still hangs + Samsung Internet default → set **Chrome** as default for sign-in. Score≈8 portable Android login — overflow (login path; not Field roster). Alert: no.

### Chris_Clarke 172797 — CoS stuck “working”; **mohitjain: model stall, ListAgents red herring**
- mohitjain 2026-09-24 07:05 UTC: Clarkie back ~17:27 UK; model stopped responding; Stop worked but queued messages restarted turns; ListAgents = stale instruction, not cause. Copy Conversation ID + UK time if recurs. Waleed_Khalid pile = separate IDE hang. Soft **one-bot silent / stuck-turn** reinforce ≈7. Alert: no.

### David.J 172836 + conszi 172842 — screen view “disappeared” 0.58.0; **kevinn: moved into Bot name panel**
- kevinn: top-right monitor folded into Bot’s name (top center) → panel → Back to details → live preview; Win Ctrl+Alt+B / Mac Cmd+Shift+I. UX teach bounce/soft. Alert: no.

### Vikas_Dakshi 172696 — Mac DNS; Cynthia_Culver pile-on after DNS still Retry-dead
- No new staff since deanrie Sep 23 DNS teach. Pile reinforces Kin_Su DNS standing. Don’t Reset. Score≈8 reinforce. Alert: no.

### nhog 172535 — 43% Transferring pile continues (Move / Emanuelle); kevinn checking Move’s box
- Reinforce Update/Reset hung 43% + don’t-Reset. Alert: no.

### Paul_Zapata 172862 — empty sidebar / first-run after sign-out; deanrie corrected: bot was **deleted** Sep 20, computer intact
- First reply (sync/display, don’t Reset) then correction (deleted from Grok app; cache opened dead chat). Soft account/delete watch — don’t generalize first teach. Alert: no.

### Hans_E 172844 — Voice call silent hang after tools done; mohitjain: work finished, spoken result lagged (esp. backgrounded iPhone)
- Keep app foreground + screen on; App Store update helps locked/background. Soft voice UX watch ≈7. Alert: no.

### Palan 171969 — Reset/Recover fail; mohitjain Sep 24: rebuilt new address; “could not be routed” = desktop on old address; quit tray+Task Manager
- Soft DNS/rebind reinforce ≈7. Alert: no.

### Bluevisuals 172529 — can’t reach Windows; deanrie: DNS can’t resolve computer address (Kin_Su family)
- Reinforce DNS. Alert: no.

### Colin 170358 — Sep 24 capacity bump: routines starting within a few minutes (was 20–40m US morning)
- Capacity reinforce of Ryan_Daley queue teach already banked. Soft watch. Alert: no.

### Colin 172106 — messages at 100% weekly usage are **not** queued/retried; resend after reset (or one-time routine while headroom)
- FR clarification bounce/soft. Alert: no.

### Cem_Guzel on 169924 — Windows desktop broken after partial Reset while phone OK; deanrie: client/session; quit tray+Task Manager; don’t Reset cloud
- Soft Windows partial-state / session reinforce. Alert: no.

### Timothy_Gresh 172549 / aliciar 172725 / Bernie 172716 — no new staff this window
- Leave as prior overflow / standing reinforce. Alert: no.

## BOUNCE

### Already-kept / standing reinforce (do not KEEP)
- Chexander 172715 / GFP 171703 — Thu KEEP skip
- Peacerk 172618 — GFP access reinforce (staff landed; not new KEEP)
- Vikas 172696 / Bluevisuals 172529 / Palan 171969 — Kin_Su DNS / rebind reinforce
- nhog 172535 — 43% family
- Sonya 172774 — Android login overflow only (staff landed)
- Chris_Clarke 172797 — stuck-turn overflow
- Timothy 172549 / aliciar 172725 / Bernie 172716 — no elevate

### Non-failure / UX / FR / billing / meetup
- Ja_We 172938 — Duplicate Bot missing in 0.58 (docs still list; FR/docs)
- jsolly 172013 — weekly usage banner dismiss per-app (Colin: desktop vs phone separate dismissals)
- Ronnie_O 172897 — leftover Grok Bot usage → Cursor models FR; kevinn: separate allowances
- FloridaJay 172846 — Plaid/Finance not released; bank browser blocked as new device
- 172905 / 172902 / 172882 — voice amplitude / bigger plan / avatar API FR
- 172877 / 172876 — meetup stubs
- 172740 — Grok bot replace Cursor? discussion
- 170832 — Gmail Spam search (SEEN; deanrie Sep 24 clarifies connector lacks includeSpamTrash/labelIds=SPAM — reinforce browser fallback; not new KEEP)
- 172798 / 172822 — printer / reasoning-effort FR (prior bounce)

## Fetch notes
- `c/grok-bot/l/latest.json` and `c/grok-bot/33.json` → **404** (invalid category); used `tag/grok-bot/l/latest.json` + `?page=1` + search after:2026-09-24 / after:2026-09-23 + keyword sweeps.
- Keyword 429s: Reset, can't reach, local execution, Update (stuck/reconnecting/routines/route traffic OK).
- Saved under `/workspace/field/forum0925/`
- Priority topics fully read: 172859, 172618, 172774, 172862, 172844, 171969, 172797, 172836, 172842, 172696, 172535, 172529, 170358 (+tail), 172106, 172013, 169924, 172938, 172897, 172846, 170832
- Bank INDEX grepped — no prior deposit for 172859 (KEEP); 169924/170358 were dup; others deposited fresh
- Appended newly fully-read topic ids to seen-forum-ids.txt (292→303)

## Bank deposits (bodies ready / deposited)
- KEEP: `bank-bodies/bank-body-172859.txt` ← TheAviv 172859 → bank raw/ai/2026-09-24-theaviv-auto-review-still-prompts-after-always.md
- Overflow: 172618 Peacerk, 172774 Sonya, 172862 Paul, 172844 Hans, 171969 Palan, 172797 Chris, 172529 Bluevisuals, 172106 Taylor, 172013 jsolly, 172842 conszi, 172836 David.J, 172938 Ja_We, 172897 Ronnie, 172846 FloridaJay
- Dup skipped: 169924 Russ, 170358 routines

## Result for compiler
- FAILURES recommend: **1** (TheAviv 172859 score=10 — Always allow = text instruction not per-tool; broader Auto-review Rules + prune Always-allow; Ask-first wins; list size limit). Edu SETUPS take remaining cap slots. Prefer this friction slot if only one.
- Soft overflow: Peacerk 172618 GFP/access reinforce; Sonya 172774 Samsung deep-link ≈8; Chris_Clarke 172797 stuck-turn; Vikas/Bluevisuals/Palan DNS; nhog 43%; Colin routines capacity few-minutes; Voice hang 172844
- KILLED mirror: (1) Always allow / standing approval = durable per-tool permission — **false**; Always allow is a text instruction; use broader manual Auto-review Rules and prune narrow Always-allow entries.
- Related reinforce (not KEEP): Peacerk Free-plan access = GFP; Kin_Su DNS pile; 43%; screen-view moved 0.58.0
- Alert: **yes** — 172859 Auto-review Rules mechanism (change Settings → Auto-review Rules this week)
