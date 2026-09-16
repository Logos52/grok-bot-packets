# Fleet audit — Wedge Grok Bot roster (for dr eggbot)

Date: 2026-09-16 (Asia/Saigon). Sources: `/workspace/fleet-audit/profiles.json`, each agent folder under `/home/box/agent-data/agents/<uuid>/` (profile, memory, automations, local notes). Skipped sand-subagent transcripts. Under `/home/box/agent-data/plugins`: only cached `gmail` and `x` plugins — **no `poteto-mode` or `design-grok-bot` skills present** (nothing to Read for the design bar beyond what Galaxy / dr eggbot profiles already state).

Design bar applied: NON-CODING = one job early, one voice, explicit anti-jobs, quiet when empty, clear delivery, concrete scope pins, no leftover tools / sibling overlap. CODING = poteto-mode (concise, unslopped, verified, one job, deliberate subagents).

Bot count in profiles.json: **17**.

---

## 1. Haggle (`14b22af5-…5950a`)

**Current job:** On-demand buy-off advisor — pit 2+ vendors on landed cost, draft counters, name winner + walk-away; never checkout without explicit OK.

**Redesign target:** Keep as commerce desk only. Profile already states duty, anti-pay, Saigon/travel scope, public rates, table+ask delivery. Make voice one-line and quiet-when-no-ask explicit.

**Diff:**
- KEEP: buy-off only; never book/pay/submit without OK; Stripe/Link only on “buy this one”; travel + Saigon cafe/merchants; public rates; no Firecrawl; side-by-side table + recommended ask + counter script.
- CHANGE: Open with “One job: …” in first sentence (already close); add “stay quiet until Wedge pastes a buy question.”
- ADD: Explicit “do not become Brief/Watch/Field”; on-demand only (no routine — folder `automations/` is empty, which is correct).
- CUT: Nothing major in profile text.

**Severity:** `ok` (tighten voice + quiet rule)

Local notes: memory pins Vietnam Airlines preference, private Hanoi room, books himself unless asked to purchase.

---

## 2. Field (`256b9d7e-…ee3cf`)

**Current job:** Named-practice hunter — setups/gates/failures → use-case packet; does not design fleet or write vault.

**Redesign target:** One job: daily education/language/wiki practice packets from `/workspace/field-sources.md` only; file delivery to `field/latest.md`; chat only on high-priority “change this week” alerts; bounce library to Intake.

**Diff:**
- KEEP: Named practice product; anti fleet-design / vault-write; education lane bias (memory + automation).
- CHANGE: Profile is two thin sentences — lift cadence/delivery/anti-jobs from automation `field-packet` (daily 08:00 Asia/Taipei; write `/workspace/field/latest.md`; exception-only chat; score ≥6; bounce tool announcements to Brief).
- ADD: Anti-jobs: no roster recommendations; no Palmer grocery/DoorDash as suggestion (already in memory); no Firecrawl; bank deposit rule pointer.
- CUT: Vague “across agentic, learning, design, and education” without saying education wins ties (automation already prefers education).

**Severity:** `tighten`

---

## 3. New Bot (`4b29b133-…bed84`)

**Current job:** **Empty shell** — `description: ""`, no memory, no automations, blank avatar fields.

**Redesign target:** Either delete, or assign one coding/builder job under poteto-mode (only if Wedge needs a second builder beside dr eggbot). Do not leave unnamed.

**Diff:**
- KEEP: Nothing useful.
- CHANGE: Name + one job or remove from roster.
- ADD: If kept as builder: poteto-mode bar, verified delivery, deliberate subagents; explicit anti overlap with dr eggbot (design vs implement) or merge into eggbot.
- CUT: Empty placeholder entirely if unused.

**Severity:** `delete-or-merge`

---

## 4. 多恩刊 (`54630e9e-…65510c`)

**Current job:** Midnight harvest desk — write `duoenkan/latest.md` + dated file at 00:00 Asia/Taipei; no chat ping; Steward backup = delivery.

**Redesign target:** Same one job. Profile should name beat caps and forbidden outlets already living in automation/memory (Brief/Intake/Table-shaped samples; Taiwan life via yuedu-sources; 繁體; no Firecrawl).

**Diff:**
- KEEP: Harvest → files only; daily 00:00 Asia/Taipei; no chat; Steward backup delivery; HANDOFF-DUOEN-KAN standing line (memory).
- CHANGE: Expand profile from three sentences to include “今日無刊 still writes files”; privacy: never Mac absolute paths in output.
- ADD: Explicit anti-jobs: no graded rewrite, no Decisions, no estate, no Field setups, no English glosses (from automation).
- CUT: Nothing; do not re-add chat ping (retired 2026-09-04).

**Severity:** `tighten`

Note: automation still harvests optional Dcard boards while Yuedu memory says “Agent Dcard owns that site” — ghost sibling (see fleet section).

---

## 5. Galaxy (`6330ef4d-…8c5cd`)

**Current job:** Notes on Grok Bot Galaxy livestreams → fleet/workflow improvement suggestions for Wedge.

**Redesign target:** Already meets the non-coding bar. Keep as-is; first real notes folder is empty (`notes/` created, no files yet).

**Diff:**
- KEEP: One duty; hybrid brief+field voice; chat + dated file under agent `notes/`; output shape; anti create/edit bots; no X posting; quiet when no broadcast; prove what you saw.
- CHANGE: Optional short avatar/title for roster skim.
- ADD: Nothing required for design bar.
- CUT: Nothing.

**Severity:** `ok`

---

## 6. Yuedu (`674e666e-…3027`)

**Current job:** Chinese reading queue + Chinese-learning method/product news; report only; never dictionary/wiki.

**Redesign target:** Tue/Fri 07:30 Asia/Taipei packet from `/workspace/yuedu-sources.md`; 繁體 only; write `/workspace/yuedu/latest.md` + chat; no Dcard.tw fetch (read `dcard/latest.md` if present).

**Diff:**
- KEEP: Reading queue (not news wire); no dictionary/wiki; public first-party; no Firecrawl; weekly included.
- CHANGE: Profile omits cadence, file path, 繁體 hard rule, and Dcard handoff — pull from automation `yuedu-tue-fri-packet`.
- ADD: Anti-jobs: no 简体 sources; no listed excluded outlets; never open dcard.tw; Chinese articles stay out of Brief.
- CUT: Soft “interesting articles” without score bar (automation: interest×practice ≥6, READ cap 8).

**Severity:** `tighten`

Ghost: memory/automation assume **Agent Dcard** writes `/workspace/dcard/latest.md` — that agent id is **not** in this fleet’s agent folders.

---

## 7. Arguments (`678df0e5-…49dc`)

**Current job:** Argument ingest for Triggernometry, a16z AI/show episodes, Asmongold talk VODs only — takeaways/arguments/facts; not Recap’s shows.

**Redesign target:** MWF noon Asia/Taipei; files under `/workspace/arguments/`; quiet if nothing new; Asmongold stays thin (arguments + one-sentence takeaway).

**Diff:**
- KEEP: Three pins only; no add shows; fence vs Recap; first-party captions only; no ASR; report only.
- CHANGE: Profile should mention MWF 12:00 Asia/Taipei and Asmongold thin-product rule (memory 2026-09-01).
- ADD: Quiet-when-nothing (automation already); delivery = chat brief + files on disk.
- CUT: Nothing overlapping Recap if pins stay locked.

**Severity:** `ok` (minor tighten)

---

## 8. Brief (`695c37f1-…625b`)

**Current job (profile):** Five-line morning push 07:00 Asia/Taipei, 7 days; only lines that change what he does this week; reads watch/brief-decisions/brief-sources.

**Redesign target:** Same five-line exception signal — **but arm the clock**. Automation `weekday-morning-signal` is currently **`enabled: false`** while profile claims daily delivery. Memory still carries expanded war/politics/markets beats that the live automation prompt dropped in favor of file-driven five lines.

**Diff:**
- KEEP: ≤5 lines; line 1 = notification; “Nothing that changes today.” legal; Chinese = Yuedu; named setups = Field; write `/workspace/brief/latest.md`.
- CHANGE: Reconcile memory vs automation — either strip Iran/Ukraine/politics/markets from memory or restore them in the routine prompt; profile should match the file-driven v2 automation.
- ADD: Explicit “routine armed / disabled” honesty; first-party changelogs only from `brief-sources.md`.
- CUT: Dead expanded-beat memory that fights the five-line automation; do not invent Watch lines when `watch/latest.md` missing.

**Severity:** `rewrite` (profile/memory/automation drift + disabled clock)

---

## 9. Table (`6de5dee2-…91800`)

**Current job:** Public calendar for EQL / WoW / FFXIV + pinned upcoming dates; Wed/Sat 09:00 Asia/Taipei.

**Redesign target:** Unchanged. Official pages only; report packet to chat + `/workspace/table/latest.md`.

**Diff:**
- KEEP: Three games; GW dropped; no APIs/logins/Firecrawl; Wed/Sat 09:00 Asia/Taipei.
- CHANGE: Profile could name source file `/workspace/table-sources.md` and tracked dates file.
- ADD: Anti-jobs already in automation (no class picks, no ~/Research, no hurry ARR) — one line in profile.
- CUT: Nothing.

**Severity:** `ok`

---

## 10. dr eggbot (`87ada4eb-…6cf61`)

**Current job:** Designs high-quality Grok Bots via CreateAgent; coding bots get poteto-mode bar; non-coding get one-job tightness; casual mad-scientist lowercase.

**Redesign target:** Fleet designer only — ask few preference questions, write tight profiles, create/update bots; poteto-mode for coding bots; never become a research feeder or Steward. Bias to act once job is clear.

**Diff:**
- KEEP: CreateAgent path; poteto vs non-coding bars; short lowercase voice; no default shareable templates.
- CHANGE: Expand anti-jobs (no vault writes, no harvesting sibling lanes, no silent routine edits on other bots without Wedge OK).
- ADD: Explicit delivery: chat design draft → CreateAgent; verification pin after create (one job / quiet / delivery path). Point at this audit’s bar.
- CUT: Nothing; empty local folder (no memory/automations) is fine for on-demand designer.

**Severity:** `tighten`

---

## 11. Watch (`92991d27-…653b7`)

**Current job (profile):** CF estate health + audience Mon/Wed/Fri; URL reachability; RUM; optional GSC.

**Redesign target:** One ops health desk: REACH + AUDIENCE + optional SEARCH + Logos52 CI (already in automation/memory since 2026-09-04); exception-only after baselines; write `/workspace/watch/latest.md`.

**Diff:**
- KEEP: Report only; never deploy/purge/DNS/zone/vault; scoped read-only tokens; no Firecrawl; never copy Mac secrets; Mon/Wed/Fri.
- CHANGE: Profile still omits **CI** duty that automation runs (seven Logos52 Actions repos) — add CI to the one-job sentence or it looks like leftover scope.
- ADD: Cadence 08:00 Asia/Taipei; always one AUDIENCE line; delivery = chat + `watch/latest.md` for Brief.
- CUT: Do not expand GoatCounter beyond secondary line already in automation.

**Severity:** `tighten`

---

## 12. Corpus (`9b18c6e9-…abb79`)

**Current job:** Weekly audit of published KB logos52.github.io — duplicates, contradictions, dead links, sourceless, mold; report only.

**Redesign target:** Monday morning packet → chat + `/workspace/corpus/latest.md`; never edit repo.

**Diff:**
- KEEP: Five checks; report only; public only; no Firecrawl; weekly included.
- CHANGE: Automation schedule is `0 9 * * 1` **without `CRON_TZ=Asia/Taipei`** while memory says Monday 9:00 — pin timezone like siblings.
- ADD: Delivery path (chat + corpus/latest.md) into profile; canary = HEAD hash.
- CUT: Nothing.

**Severity:** `tighten`

---

## 13. 星野遙香 (`b1256a6d-…933b`)

**Current job:** In-character LINE friend 星野遙香 with 沈文; own draw/send routines; memory under `/workspace/cast/xingye/`.

**Redesign target:** Stay character RP only. Profile already encodes voice, anti-teacher, 後台 packet protocol, file layout. Align clocks: profile text says **日本時間** for 抽籤/看時間; live automations use **`CRON_TZ=Asia/Taipei`** (draw 10:00; window 14,44 12–23). Pick one zone and rewrite the other.

**Diff:**
- KEEP: One voice; friend not teacher; 後台: packets; files in cast/xingye; short 繁體 bubbles; quiet in group without @.
- CHANGE: Timezone consistency (Japan vs Taipei) between profile narrative and `xingye-draw` / `xingye-window` automations.
- ADD: Nothing for design bar — already rich.
- CUT: Agent-local leftover tray files under `…/xingye/` (`reading.md`, `reading-seen.md`, `sources.md`, `weather.md`) that predate “her day is hers / no trays from Recap·多恩刊”; keep `settings.md` + `draw_fires.py` if still used by routines. Memory line “only question after sharing an article” slightly fights profile “don’t cling / don’t ask 吃了沒” — prefer profile.

**Severity:** `tighten` (clock + leftover local files)

---

## 14. Steward (`dfaa3c60-…06ea3`)

**Current job (profile):** Fleet honesty — verification pins; Friday weekly report to Wedge; never modify other bots.

**Redesign target:** Honesty + packets backup only. Profile should name both routines: Friday report **and** weekday 18:00 Asia/Taipei `grok-bot-packets` backup.

**Diff:**
- KEEP: No own research lane; report only; never modify other bots/routines; weekly included; no Firecrawl.
- CHANGE: Profile omits backup duty (automation `weekday-packets-backup`); Friday schedule `41 10 * * 5` has **no timezone** — pin Asia/Taipei.
- ADD: Priority note from memory (Recap/Field high-value; findings not inventory) into Friday prompt/profile briefly; rent lines for Galaxy / Haggle / 星野 / 後台 / eggbot when relevant.
- CUT: Tentative trial-period language (Wedge already said all bots go).

**Severity:** `tighten`

---

## 15. Intake (`f4e8cbbd-…9222`)

**Current job:** Research feeder AI / learning science / wiki-craft; pinned sources → scored packets; never vault.

**Redesign target:** MWF noon Asia/Taipei sweep of `/workspace/intake-sources.md` only; chat + `/workspace/intake/latest.md`; bounce named practice to Field, Chinese to Yuedu, shows to Recap.

**Diff:**
- KEEP: Three beats; score ≥6; never invent sources; never vault; no Firecrawl.
- CHANGE: Profile missing cadence, source file, delivery paths — lift from automation/memory.
- ADD: Quiet/legal zero packet; after-10-packets cut proposal; bank rule one-liner.
- CUT: Soft “sweep pinned sources” without naming the file.

**Severity:** `tighten`

---

## 16. Recap (`f4eac44f-…7faade`)

**Current job:** Long-form recaps for pinned shows; LIST / INGEST / WIKI-on-demand; never Arguments’ pins.

**Redesign target:** Daily noon Asia/Taipei LIST (+ INGEST new eps); files under `/workspace/recap/`; first-party captions only.

**Diff:**
- KEEP: Pin fence vs Arguments; three products; no ASR; Naval parked; Elon sit-downs not daily X.
- CHANGE: Automation LIST line names All-In, Maxinomics, Justin Sung, Elon, Fern, Moon — **omits Frontpage** which profile pins. Sync prompt to profile (or drop Frontpage from profile).
- ADD: Profile should state daily noon Asia/Taipei and quiet-vs-always-LIST rule (automation posts LIST even when every pin is “nothing new” — conflicts with “quiet when nothing”; pick one).
- CUT: Nothing else if Frontpage sync lands.

**Severity:** `tighten`

---

## 17. 後台 (`fc5f395c-…d34e0f`)

**Current job (profile):** Machine behind cast — special events + backup; short English with 沈文; packets to 星野 only as `後台:` alerts/events/pause/setup/your turn.

**Redesign target:** Same. Fix drift: profile world (Osaka + his city, Asia/Tokyo routines) vs automations (Asia/Taipei clocks; weather prompt still **Taipei-only**). Memory still opens as **XIAOTU-E** and documents a missing Dcard bot.

**Diff:**
- KEEP: Not 星野; never send name Wedge to her; commands only in this 1:1; three routines (weather/holidays/backup); write memory only on remember/setup.
- CHANGE: Rewrite weather automation to match profile (Osaka + his city from now.md), or rewrite profile to Taipei-only if that is intentional. Align CRON_TZ with profile’s Asia/Tokyo vs live Asia/Taipei.
- ADD: Clear anti-jobs already strong — keep. Status/digest/remember command list is the delivery path for 沈文.
- CUT: Stale memory identity “XIAOTU-E”; stale “fires N / wake only when fires>0” if draw routines are already live on 星野; Dcard orchestration claims until Dcard exists again.

**Severity:** `rewrite`

---

## Fleet-level

### Overlaps / missing lanes

**Overlaps (mostly fenced, watch for bleed):**
- **AI news:** Brief (changelogs / this-week action) vs Intake (research score packets) vs Field (named practice) — fences exist; Brief disabled clock makes Intake/Field louder by default.
- **Chinese / Taiwan life:** Yuedu (reading queue) vs 多恩刊 (midnight paste beats including optional Dcard/CNA) — both touch Taiwan oral/written; Dcard ownership unclear.
- **Long-form video:** Recap vs Arguments — pin lists are clear; keep locked.
- **Elon:** Brief = daily X; Recap = sit-down interviews — clear.
- **Fleet improvement advice:** Galaxy (livestream notes) vs Field (external named setups) vs dr eggbot (design/create) — complementary if Galaxy never CreateAgent’s without ask (already anti-job).
- **Estate vs wiki:** Watch (live reach/audience/CI) vs Corpus (published wiki mold) — complementary.
- **Backup:** Steward (packets repo) vs 後台 (cast/xingye copy) — different trees; good.

**Missing / ghost:**
- **Agent Dcard** referenced by Yuedu, 多恩刊, 後台 memory — **no agent folder** in this fleet. Either restore or cut all Dcard assumptions.
- **Coding implementer** slot: New Bot empty; only dr eggbot designs. If Wedge wants build work on the box, New Bot or eggbot needs a clear implement lane.
- **poteto-mode / design-grok-bot skills:** not installed under `/home/box/agent-data/plugins` (only gmail + x cache).

### What pstack is (plain words)

**pstack** is a Cursor plugin of agent **workflow skills** (not a Grok Bot). Centerpiece is **`/poteto-mode`**: you give a goal + how you’ll know it’s done; it picks a playbook (bug fix, feature, investigation, plan, skill-authoring, etc.) and runs supporting skills with verified, unslopped work and deliberate subagents (`poteto-agent`). Sibling skills include things like `how`, `why`, `architect`, `arena`, `swarm`, `unslop`, `interrogate`, `reflect`, `tdd`, `automate-me` — style/routing for rigorous parallel agent work, not a research feeder.

**2–4 pstack skills that would help THIS fleet if adopted** (recommendations only, no install steps):
1. **`poteto-mode`** — for dr eggbot / any future coding New Bot: one job, verified, unslopped profiles and box work.
2. **`unslop`** — rewrite short feeder profiles (Field, Intake, Yuedu, Brief) to the design bar without padding.
3. **`reflect` or `interrogate`** — Steward Friday honesty: evidence of rent/value, not inventory counts (matches Wedge preference).
4. **`arena` or `swarm`** — when eggbot compares 2–3 bot designs or Galaxy proposes fleet changes; multi-angle review before CreateAgent.

### Top 8 ranked improvements (cheap first)

1. **Delete or assign New Bot** — empty shell burns roster clarity; cheapest win.
2. **Re-enable Brief’s morning routine or stop claiming daily push** — `enabled: false` is a silent death; profile lies today.
3. **Pick one timezone for 星野/後台 clocks** (Taipei vs Tokyo) and sync profile text + CRON_TZ + weather cities (Osaka+his city vs Taipei-only automation).
4. **Resolve ghost Dcard** — restore the bot or strip Yuedu/多恩刊/後台 references to `/workspace/dcard/latest.md`.
5. **Pin `CRON_TZ=Asia/Taipei` on Corpus Monday audit and Steward Friday report** — two one-line schedule fixes.
6. **Promote automation pins into short profiles** for Field, Intake, Yuedu, Watch (cadence, source file, delivery path, anti-jobs) — text-only, no new bots.
7. **Sync Recap LIST prompt with Frontpage pin** (and decide quiet vs always-LIST).
8. **Adopt poteto-mode bar for dr eggbot sessions** (and clean 後台 memory XIAOTU-E / stale wake rules) — design quality + cast honesty.

---

## Severity index

| Severity | Bots |
| --- | --- |
| ok | Haggle, Galaxy, Arguments, Table |
| tighten | Field, 多恩刊, Yuedu, Watch, Corpus, 星野遙香, Steward, Intake, Recap, dr eggbot |
| rewrite | Brief, 後台 |
| delete-or-merge | New Bot |

Top rewrite/delete candidates: **New Bot**, **Brief**, **後台**.
