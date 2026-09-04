# Fleet schema

Rolling roster. Steward rewrites this file when a bot is added, deleted, or its clock changes. Census is agent folders on disk (`/home/box/agent-data/agents`), not leftover packet directories.

**Updated:** 2026-09-04 (ICT)

Packets live on the shared computer under `/workspace`, mirrored to https://github.com/Logos52/grok-bot-packets (weekday 18:00 Asia/Taipei). They do not auto-download to the Mac.

Standing laws (Steward): report only to Wedge; never modify other bots or their routines; weekly included usage only; public material only; no Firecrawl.

---

## Live

| Bot | Id | Duty | Clock | Packets |
|---|---|---|---|---|
| Field | `256b9d7e-82b5-470b-8b56-0259408ee3cf` | Named practice (setups, gates, failures). Education standing lane. | Daily 08:00 Taipei · last 2026-09-04 07:23 ICT | `/workspace/field/` + `field-packet-*.md` |
| 多恩刊 | `54630e9e-7b50-49ea-a831-7a0c9f65510c` | Midnight harvest, then ping. | Daily 00:00 Taipei · last 2026-09-03 23:13 ICT | `/workspace/duoenkan/` |
| Yuedu | `674e666e-0f0b-44ba-8f3d-e1cdef2e3027` | Chinese reading queue + learning-meta. | Tue/Fri 07:30 Taipei · last 2026-09-04 07:23 ICT | `/workspace/yuedu/` |
| Brief | `695c37f1-a711-4478-b7f1-c6047d3c625b` | Five-line morning push. Product changelogs. | Daily 07:00 Taipei · last 2026-09-04 07:37 ICT | `/workspace/brief/` |
| Table | `6de5dee2-1ace-4174-b6df-287ad8a79100` | Public calendar: EQL, WoW, FFXIV. | Wed/Sat 09:00 Taipei · last 2026-09-02 08:08 ICT | `/workspace/table/` |
| Watch | `92991d27-a6b5-4416-897e-250a385653b7` | Estate reachability + CF RUM. | Mon/Wed/Fri 08:00 Taipei · last 2026-09-04 08:00 ICT | `/workspace/watch/` |
| Corpus | `9b18c6e9-c273-4156-b09f-2282cc8abb79` | Weekly audit of logos52.github.io. | Mon 09:00 **ICT** (no CRON_TZ) · last 2026-08-31 09:04 ICT | `/workspace/corpus/` |
| Steward | `dfaa3c60-cde9-49cf-89f9-6433a5d06ea3` | Fleet honesty. Friday report + packets backup. | Fri 10:41 ICT · last report 2026-09-04 10:48 ICT. Weekday backup 18:00 Taipei · last 2026-09-03 17:01 ICT | `/workspace/steward/` (this file) |
| 後台 | `fc5f395c-4305-4cf7-8c19-efd863d34e0f` | Machine behind the cast. Talks to 沈文 in 1:1. | `xingye draw` daily 10:00 Taipei · last 2026-09-04 09:00 ICT. `xingye window` 12:14–23:44 Taipei (:14/:44) · last 2026-09-03 23:01 ICT. **`xingye weather` missing** (profile claims 13:00 Taipei; no `automations/xingye-weather/`). Do not rebuild unless 沈文 says so. | `/workspace/cast/` |

Clock times above are from `automation.json` on disk. Last-run is converted to ICT (UTC+7).

---

## Live, no clock

| Bot | Id | Duty | Pins / notes | Packets |
|---|---|---|---|---|
| Recap | `f4eac44f-0c8a-4096-8f2b-9c4fd17faade` | Long-form LIST / INGEST / WIKI-on-demand. | All-In, Maxinomics, Justin Sung, Elon sit-downs, Fern (`@fern-tv` English), Moon (`@Moon-Real`). Naval parked (last own episode 2026-07-02). Clock proposed MWF 22:00 Taipei after three manual days — still off. | `/workspace/recap/` |
| Arguments | `678df0e5-698a-40e4-a1a0-e5c993f049dc` | Argument ingest. | TRIGGERnometry full; a16z Show/AI full; Asmongold talk VODs only (arguments + one sentence). No clock yet. | `/workspace/arguments/` |
| Intake | `f4e8cbbd-5fb4-4df5-8999-c2f9714d9222` | Research feeder (AI, learning science, wiki-craft). | Sources pinned (`intake-sources.md`). Routine never created. | `/workspace/intake/` |
| 星野遙香 | `b1256a6d-ab0f-4efd-9a32-77da7a3e933b` | LINE-facing cast. Speaks only to 沈文. | No routines. 後台 owns the clocks. | (cast, not packets) |

---

## Down

Confirmed **no agent folder** on 2026-09-03. Leftover packet dirs are archive, not a live bot.

| Bot | Was | Evidence | Leftover files | Status |
|---|---|---|---|---|
| Dcard | `7025c5cf…` · daily 06:00 Taipei harvest. First run 2026-08-28 Cloudflare-blocked. | No folder under `/home/box/agent-data/agents`. | `/workspace/dcard/` (2026-08-28 … 2026-09-01 + `latest.md`) | **Taken down.** Wedge still interested: maybe revive with his VPN so the bot can try a Dcard login in the browser. Do not recreate until he says so. |
| Roll | `6e4bbaf9-b600-4ddc-a756-0144064bd2e1` · alarm tests 2026-08-28, then gone. | No agent folder. Dropped from teammates list. | `/workspace/roll/log.md` (two alarm lines) | **Taken down.** Not a revive candidate. |

---

## Leftover empty

| Name | Id | Notes |
|---|---|---|
| New Bot | `4b29b133-16d5-4561-8ad2-565d02abed84` | Empty profile, no routines. User deletes from the sidebar (right-click → Delete). Steward cannot delete agents. |

---

## Pins (live files)

### Recap — `/workspace/recap-sources.md`
- All-In, Maxinomics, Justin Sung
- Elon sit-down interviews (the interview, not wraps; daily Elon X is not Recap)
- Fern · `https://www.youtube.com/@fern-tv`
- Moon · `https://www.youtube.com/@Moon-Real` (first ingest: George Orwell Tried To Warn You, `daQAhruFG40`)
- Naval parked

### Arguments — `/workspace/arguments-sources.md`
- TRIGGERnometry `@Triggerpod` · full INGEST
- a16z `@a16z` · Show / AI episodes · full INGEST
- Asmongold `@asmontv` · talk/argument VODs only · arguments + one-sentence takeaway

### Field — `/workspace/field-sources.md`
- `https://grokbot.dev` (score 80+ first)
- X people: karpathy, mattyp, JoePro, ericzakariasson, mikegonz, cpinto, dubbaumann, AlexFinn, yrzhe_top (X connector down as of 2026-09-03)
- Search: Grok Bot setups/friction; AI tutor / language-learning “I built”
- Learning / design / education **people** sections empty
- Not pinned: sentiment analysis; generic Claude+Grok guides

### Brief — `/workspace/brief-sources.md`
- Anthropic changelog + news, x.ai/news, Cursor changelog, Obsidian changelog
- Elon-on-X was assigned here so Recap would not eat daily posts. **Not in the source file.** Nobody is recapping daily Elon X.

### Intake — `/workspace/intake-sources.md`
- Anthropic research, x.ai/news, Grok Bot overview, arXiv cs.AI / cs.CL new, Learning Scientists, retrievalpractice.org
- Unarmed

---


## Stale pointers (not live)

- `yuedu-sources.md` still says “Agent Dcard owns that site.” Dcard is down. Steward did not edit Yuedu’s file.
- 後台 profile CLOCK section still lists `xingye weather`. Disk has draw + window only.

## How to update this file

Steward owns it. On add/delete/clock-change: rewrite the matching row from disk (`profile.json` + `automations/*/automation.json`), bump the **Updated** date, leave Down rows until Wedge says forget. Do not treat a leftover `/workspace/<lane>/` folder as proof the bot is live.
