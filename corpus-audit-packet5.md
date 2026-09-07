# Knowledge Base Review Packet #5
**Canary:** HEAD `6aa57409ffea69f1fcdb828f24b08ba934ec567a` — 2026-09-05 22:11:13 +0700
**Prior HEAD:** `5726e9fdd365c3cb117f7bce350b17ae8e7ce18b` (packet #4) — changed, full sweep
**Vs packet #4:** 9 new wiki pages; C-1/C-4/DL-4/M-1..6 persist; 3 sourceless AI operating notes gained `## Sources`; 5 new pages ship `## Sources and links` (not exact `## Sources`); 1 new dead wikilink into gitignored Workbench. Mold still untouched through packet 5 — reaffirm drop proposal from #4.

Wiki pages: **376** tracked markdown under `wiki/` (`git ls-files -- wiki`, `*.md`). Nested 372 + 4 wiki-root. Packet #4 stated 363; that count missed the same 4 Design em-dash filenames (git `quotepath` quoting), so like-for-like was 367 → 376 (+9 adds, 0 wiki deletes). Range vs 5726e9f: 174 files, +8986/−631.

New wiki pages this range:
- `wiki/Concepts/Dating Apps - The Gini Coefficient.md`
- `wiki/Research/Claude Fable 5.1 Bank.md`
- `wiki/Research/Grok Bot Field Packet 2026-08-31.md`
- `wiki/Research/Probability Distributions Bank.md`
- `wiki/Systems/AI & Agentic Systems/Grok Bot, Condensed.md`
- `wiki/Worldviews & the Political Order/Britain - Poorer Than Mississippi.md`
- `wiki/Worldviews & the Political Order/Single-Sex Spaces - The Asymmetry.md`
- `wiki/Worldviews & the Political Order/Socialism - The Calculation Problem.md`
- `wiki/Worldviews & the Political Order/The Gen Z Gender War - The Split.md`

## Counts
- Near-duplicates: 0 (new: 0, persist: 0, resolved: 0)
- Contradictions: 2 (new: 0, persist: 2, resolved: 0)
- Dead wikilinks: 2 (new: 1, persist: 1, resolved: 0)
- Sourceless: 35 / 376 inclusive (32 nested + 3 wiki-root; new: 5, persist: 30, resolved: 3). Nested rate 32 / 372.
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## 1) Near-duplicates

Merge candidates only. Redirect stubs, condensed/hub, book/concept, core/practice, challenge-protocol vs dimension-hub, research bank vs live page, dated field-packet series, and `*, Condensed` vs full are **not** flagged.

### New (0)

No merge candidates. Same-H1 collisions: none. Same-stem collisions: only the intentional book/concept Suicidal Empathy pair.

### Considered, not flagged (new pages)

- `Grok Bot, Condensed.md` vs `Grok Bot Primer.md` vs `Grok 4.6 and Grok Bot.md` vs `Bot Operating Rules.md` — condensed doctrine vs one-person setup vs product card vs operating rules. Condensed/hub pattern; not a merge.
- `Grok Bot Field Packet 2026-08-31.md` vs `…2026-08-15.md` — dated series, openings differ; not copies.
- `Probability Distributions Bank.md` vs `Concepts/Probability Distributions.md` — bank vs live page (same split prior packets declined).
- `Claude Fable 5.1 Bank.md` — launch/field bank; not a twin of Claude Fable operating notes.
- Four Worldviews long pages (Britain / Single-Sex Spaces / Socialism / Gen Z Gender War) + `Dating Apps - The Gini Coefficient.md` — unique theses; no sibling overlap into merge.
- Dimension hubs vs `* Challenge.md` still different jobs (unchanged).

Packet #1–#4 ND pairs stay resolved.

---

## 2) Contradictions

### Persist from packet #4 (2)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine. Line numbers re-checked; Astro block unchanged from #4; Quartz leftovers same files.
  - Astro (current): `AGENTS.md:407-409` ("## Static Site (Astro)"; "Astro builds from `src/`"); `AGENTS.md:424` ("The site is a normal Astro project"); `README.md:126` ("built with Astro"); `.gitignore:62-63` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts remain `astro`/`astro build`.
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:10` frontmatter tag `quartz`; `:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`"); `:19` ("Quartz `ignorePatterns`" context); `:64` ("then runs `npx quartz build` to publish").
  - Extra cites (same contradiction, not a new item): `AGENTS.md:396` still names Quartz's "`RemoveDrafts` filter" inside the (now Astro) publish section; `tools/scripts/setup-site.sh:4-7` / `:25` / `:31-60` is a live script that clones Quartz v4 and would overwrite `package.json`; `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site" (`:52` notes denylist replicated from former `quartz.config.ts`).

- **C-4 (persist) Current model roster disagrees — wider this week.** Stack page moved the **writer seat to Grok 4.6** (signed 1 September 2026); AGENTS.md's three-model block was not touched and still names Claude as primary for wiki.
  - `AGENTS.md:69` — "We use three models in the current setup: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." Claude subsection still "Primary model for … wiki work" (`:72-80`); GPT section `:90-100`; health-check/status paths `:201` / `:216` still hard-code `01 - Workbench/GPT - …`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md` (`updated: 2026-09-01`): Primary writer = Grok Build (`grok-4.6`); Research on request = Claude Cowork (Fable 5); Vault pipeline = Grok Build; Coding = Grok Build; IDE = Cursor; Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT peer. Claude is not the default writer.** `:35` keeps API-metered seats off the roster. Hermes/Ollama appear only under history (`:62-67`) — correct and exempt from mold.
  - Both pages are present-tense "current"; the stack cites `journal/2026-09-01-grok-writes` for the writer-seat move. AGENTS.md's Working With Different Models section still routes wiki work to Claude.

### New (0)

### Not flagged

- `wiki/Research/Woke Mind Virus Bank.md` stale "page that does not exist yet" vs live Woke Mind Virus page — bank status line, same class as prior packets.
- `Grok Bot Fleet Structures.md` ("Nothing on this page is ruled") vs `Standing Research Agents.md` — candidate vs current.
- Agent Glossary Codex entries — industry names, not "this vault runs Codex."
- Stack history Hermes/Ollama — dated retirement, not live-tool phrasing.

---

## 3) Dead wikilinks

Resolved against tracked files (stem for bare names; full path when the link contains `/`). `raw/**` and `private/**` targets skipped (35 hits, all `raw/` — not dead). Heading-only `[[#…]]` skipped. `\|` aliases unescaped before resolve. Design catalog files with em-dashes in the filename exist and match; they are not dead.

### Persist from packet #4 (1)

- **DL-4 (persist)** `wiki/Concepts/Selfhood.md:39` → `wiki/Concepts/Meiwaku Has No Revenue Line`
  - No tracked file by that stem or path. `wiki/Concepts/Meiwaku.md` exists; `Selfhood and the Ledger.md` is the repair page already linked on the same line. Still looks like a planned sibling that was never added.

### New (1)

- **DL-6 (new)** `wiki/Research/Claude Fable 5.1 Bank.md:21` → `01 - Workbench/Fable - Research Bank - Claude and Grok Tools.md`
  - Not tracked; path matches `.gitignore:67` rule `01 - Workbench/*` (file also absent on disk in this clone). Neighbor links on the same line to Claude Fable / Current Stack / journal resolve. Formal exemption list is only `raw/**` and `private/**` — Workbench is the same "gitignored by design" class, so expand the exemption or retarget the link.

### Resolved (0)

---

## 4) Sourceless

Exact H2 `## Sources` required. **35 / 376** inclusive missing it (packet #4: 33 / 363 stated). Nested: **32 / 372**. Singular H2 `## Source`: **0**. Near-miss heading `## Sources and links`: **5** (all new this range — contentful source sections under the wrong H2). `wiki/Glossary.md` still has `## Raw Source` / `## Source Note`, not `## Sources`.

### Resolved since packet #4 (3)

Gained exact `## Sources`:
- `wiki/Systems/AI & Agentic Systems/Bot Operating Rules.md` (`:60`)
- `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md` (`:87`)
- `wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md` (`:107`)

### New (5)

All ship `## Sources and links` instead of `## Sources`:
- `wiki/Concepts/Dating Apps - The Gini Coefficient.md`
- `wiki/Worldviews & the Political Order/Britain - Poorer Than Mississippi.md`
- `wiki/Worldviews & the Political Order/Single-Sex Spaces - The Asymmetry.md`
- `wiki/Worldviews & the Political Order/Socialism - The Calculation Problem.md`
- `wiki/Worldviews & the Political Order/The Gen Z Gender War - The Split.md`

### Persist (30 = 27 nested + 3 wiki-root)

Prior nested list minus the three AI operating notes that gained Sources; wiki-root three unchanged. Clusters: condensed doctrine pages, research banks, Fitness/Travel, Worldviews hub, The Cold Open, The Same Model Twice, The Personal Uniform, How Foreign Words Become Chinese, Techniques - Learning Craft, Least-Cost Interpretation, Agentic Engineering Condensed.

### Full list (32 nested + 3 wiki-root)

Nested (32):

- wiki/Concepts/Dating Apps - The Gini Coefficient.md *(new; has `## Sources and links`)*
- wiki/Concepts/The Same Model Twice.md
- wiki/Design/Design, Condensed.md
- wiki/Dimensions/Mindset/Mindset, Condensed.md
- wiki/Fashion/The Personal Uniform.md
- wiki/Fitness/Movement as Accretion.md
- wiki/Fitness/The Treadmill Library.md
- wiki/Language Research/How Foreign Words Become Chinese.md
- wiki/Language/Chinese/Chinese Characters, Condensed.md
- wiki/Minimalism/Minimalism, Condensed.md
- wiki/Money/Money, Condensed.md
- wiki/Research/ATTEMPT-CATALOG-context-problem.md
- wiki/Research/Blog Craft Research Bank.md
- wiki/Research/Immigration and the Woke Left Bank.md
- wiki/Research/Report Intro Paragraph Bank.md
- wiki/Research/Self-Talk Research Bank.md
- wiki/Research/Self-Talk and the Two Egos Bridge Bank.md
- wiki/Research/Two Egos Research Bank.md
- wiki/Research/Woke Mind Virus Bank.md
- wiki/Story Craft/Story Craft, Condensed.md
- wiki/Syntheses/Learning, Condensed.md
- wiki/Systems/AI & Agentic Systems/Agentic Engineering, Condensed.md
- wiki/Systems/AI & Agentic Systems/Least-Cost Interpretation.md
- wiki/Techniques/Techniques - Learning Craft.md
- wiki/Travel/Reading as Local.md
- wiki/Travel/Warm Countries, Cold Countries.md
- wiki/Worldviews & the Political Order/Britain - Poorer Than Mississippi.md *(new; has `## Sources and links`)*
- wiki/Worldviews & the Political Order/Single-Sex Spaces - The Asymmetry.md *(new; has `## Sources and links`)*
- wiki/Worldviews & the Political Order/Socialism - The Calculation Problem.md *(new; has `## Sources and links`)*
- wiki/Worldviews & the Political Order/The Gen Z Gender War - The Split.md *(new; has `## Sources and links`)*
- wiki/Worldviews & the Political Order/Worldviews & the Political Order.md
- wiki/Writing Craft/The Cold Open.md

Wiki-root (3; persist from packet #2):

- wiki/Glossary.md (`## Source Note` / `## Raw Source`, not `## Sources`)
- wiki/ICS Program Map.md
- wiki/Timeline.md

`wiki/Bibliography.md` still has `## Sources`. New pages with exact Sources: Claude Fable 5.1 Bank, Grok Bot Field Packet 2026-08-31, Probability Distributions Bank, Grok Bot Condensed.

Redirects among the misses: **0**.

---

## 5) Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/`). History sections ("What's Gone", Evolution, changelog) exempt. Wiki C-2 remains resolved. `hermes/` was not touched this range (still 27 tracked files).

### Persist from packet #1 (6)

Line numbers re-checked; they did not move (GROK.md this range only a tiny unrelated edit elsewhere).

- **M-1 (persist)** `GROK.md:11` — "Latest `hermes/skills/l3-to-l2-voice-converter/references/style-feedback.md` (living before/after refinements)" — presents the hermes/ tree as the living voice-standard location.
- **M-2 (persist)** `GROK.md:65` — "When using these standards (in chat, Grok Build, Hermes, or any remote session)" — Hermes listed as a current session type beside Grok Build.
- **M-3 (persist)** `README.md:75` — "e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex" — Codex presented as a live schema consumer. Extra cite (not a new ID): `AGENTS.md:23` still lists Codex in the live pick-list before Agent Glossary.
- **M-4 (persist)** `tools/wiki-cleanup-ritual.md:16` — "**AI-agnostic** — any agent (Claude, Grok, ChatGPT, Hermes, others) can read this prompt and execute the steps."
- **M-5 (persist)** `tools/publish-snapshots.md:15` — same Hermes-in-the-agent-list phrasing, plus Quartz live trigger (`npx quartz build`).
- **M-6 (persist)** `hermes/` tree, present tense as a live TUI/runtime. Representative:
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:27` — "Inside Hermes TUI, you can say things like:"
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:74` — "This skill stays pure Hermes/Grok — no external scripts."
  - `hermes/skills/curator/SKILL.md:4,24` — "Lightweight Hermes skill stub" / "Recommended inside Hermes TUI"
  - `hermes/skills/evolution/README.md:50` — "Now Working in Hermes TUI"
  - `hermes/skills/kb-synthesis-orchestrator/setup.md:11` — "Add the `kanban` toolset to your orchestrator profile in `~/.hermes/config.yaml`"

`CLAUDE.md` does not present Hermes/Ollama/Codex as live. No Ollama in instruction/config as live (stack history only). No new mold ID this sweep. **Five packets, zero mold edits — drop proposal from packet #4 still stands.**

---

## Packet #4 → #5 scorecard

| ID | Packet #4 | Packet #5 |
|---|---|---|
| C-1 Quartz vs Astro | persist | **persist** (same files/lines) |
| C-4 Current roster AGENTS.md vs stack table | persist | **persist / wider** (writer seat → Grok 4.6 on stack; AGENTS three-model + Claude-primary-wiki untouched) |
| DL-4 Selfhood → Meiwaku Has No Revenue Line | persist | **persist** (`:39` unchanged) |
| DL-6 Workbench Fable bank link | — | **new** (gitignored Workbench target) |
| Sourceless | 33/363 stated | **35/376**; −3 AI notes gained Sources; +5 new pages with `## Sources and links` |
| Mold GROK/README/tools/hermes | persist (6) | **persist** (same files/lines; drop still recommended) |
| Near-duplicates | 0 | **0** |

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure. `raw/**` and `private/**` targets not dead. No repo writes.*
