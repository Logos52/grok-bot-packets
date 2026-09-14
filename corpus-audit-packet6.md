# Knowledge Base Review Packet #6
**Canary:** HEAD `f143226ce2b5703fa3cc95ec12f6b1b8658877bd` — 2026-09-13 12:57:25 +0700
**Prior HEAD:** `6aa57409ffea69f1fcdb828f24b08ba934ec567a` (packet #5) — changed, full sweep
**Vs packet #5:** Large wiki prune + rewrite week (49 wiki deletes, 14 adds → **341** pages). C-1/C-4/DL-4/DL-6/M-1..6 persist. Six pages gained exact `## Sources` (five that previously shipped `## Sources and links`, plus How Foreign Words). Five new research banks are sourceless. Four new path-dead wikilinks from moves/merges. Mold still untouched through packet 6 — drop proposal from #4 still stands.

Wiki pages: **341** tracked markdown under `wiki/` (`git ls-files`, `core.quotepath=false`). Packet #5: 376. Like-for-like: −49 deletes, +14 adds. Range vs 6aa5740: 33 commits; 579 files, +29888/−15676.

New wiki pages this range:
- `wiki/Concepts/Five Thinking Habits - Conclusion First.md`
- `wiki/Concepts/Levels of Thinking - The Step Back.md`
- `wiki/Dimensions/Deep Processing/Thinking on Paper - Mindmaps and Other Techniques.md`
- `wiki/Fitness/Fitness Mindsets.md`
- `wiki/Research/Everybodyism and the Maturity Crisis Bank.md`
- `wiki/Research/Four Quadrants Bank.md`
- `wiki/Research/Levels of Thinking Bank.md`
- `wiki/Research/The Table Bank.md`
- `wiki/Research/Thinking About Thinking Bank.md`
- `wiki/Worldviews & the Political Order/China - The Temple and the Monks.md`
- `wiki/Worldviews & the Political Order/Europe - The Slow Agony.md`
- `wiki/Worldviews & the Political Order/Genetics and Unequal Societies - The Distance Claim.md`
- `wiki/Worldviews & the Political Order/Late Stage Feminism.md`
- `wiki/Writing Craft/Five Writing Templates.md`

Notable deletes (aliases often retargeted on survivors — those are not dead): Deep Processing / Mindset / Retrieval / Self-Regulation practice leaves; Self Management cluster; several AI operating notes folded into Primer / Context Engineering / Stack; `Software 3.0.md`, `Bot Operating Rules.md`, `Least-Cost Interpretation.md`, etc.

## Counts
- Near-duplicates: 0 (new: 0, persist: 0, resolved: 0)
- Contradictions: 2 (new: 0, persist: 2, resolved: 0)
- Dead wikilinks: 6 (new: 4, persist: 2, resolved: 0)
- Sourceless: 33 / 341 inclusive (30 nested + 3 wiki-root; new: 5, persist: 28, resolved: 6 gained Sources, 1 deleted while sourceless). Nested rate 30 / 338.
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## 1) Near-duplicates

Merge candidates only. Redirect stubs, condensed/hub, book/concept, core/practice, challenge-protocol vs dimension-hub, research bank vs live page, dated field-packet series, and `*, Condensed` vs full are **not** flagged.

### New (0)

No merge candidates. Same-H1 collisions: none. Same-stem collisions: only the intentional book/concept Suicidal Empathy pair.

### Considered, not flagged (new pages)

- `Five Thinking Habits - Conclusion First.md` vs `Five Writing Templates.md` — habits concept vs writing-template shapes from the same five habits; different jobs, not copies.
- `Levels of Thinking - The Step Back.md` vs `Levels of Thinking Bank.md` (+ sibling banks Everybodyism / Four Quadrants / Thinking About Thinking / The Table) — live page vs research banks; bank pattern exempt.
- `Thinking on Paper - Mindmaps and Other Techniques.md` vs deleted `Thinking on Paper.md` — rename/expansion, single survivor.
- Four Worldviews long pages (China / Europe / Genetics / Late Stage Feminism) + `Fitness Mindsets.md` — unique theses; no sibling overlap into merge.

Packet #1–#5 ND pairs stay resolved.

---

## 2) Contradictions

### Persist from packet #5 (2)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine.
  - Astro (current): `AGENTS.md:408-410` ("## Static Site (Astro)"; "Astro builds from `src/`"); `AGENTS.md:425` ("The site is a normal Astro project"); `README.md:126` ("built with Astro"); `.gitignore:62-63` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts remain `astro`/`astro build`.
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:10` frontmatter tag `quartz`; `:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`"); `:19` (Quartz `ignorePatterns` context); `:64` ("then runs `npx quartz build` to publish").
  - Extra cites (same contradiction, not a new item): `tools/scripts/setup-site.sh:4-7` / `:25` / `:31-60` still clones Quartz v4 and would overwrite `package.json`; `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site" (`:57` notes denylist replicated from former `quartz.config.ts`).

- **C-4 (persist) Current model roster disagrees.** Stack still puts **Grok 4.6** on the writer seat; `AGENTS.md`'s three-model block was not aligned.
  - `AGENTS.md:69` — "We use three models in the current setup: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." Claude subsection still "Primary model for … wiki work" (`:72`); general rule `:98` "Use **Claude** for file work, briefs, and wiki."; GPT health-check paths `:201` / `:216` still hard-code `01 - Workbench/GPT - …`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md` (`updated: 2026-09-11`): Primary writer = Grok Build (`grok-4.6`); Research on request = Claude Cowork; Vault pipeline = Grok Build; Coding = Grok Build; IDE = Cursor; Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT peer. Claude is not the default writer.** Hermes/Ollama appear only under history (`:89`) — correct and exempt from mold.
  - Both pages are present-tense "current"; the stack cites `journal/2026-09-01-grok-writes` for the writer-seat move.

### New (0)

### Not flagged

- Alias retargets after deletes (`Deep Processing Practice` → `Higher-Order Learning`, `Bot Operating Rules` / `Standing Research Agents` → `Grok Bot Primer`, `Software 3.0` alias on `Context Engineering`, `First Principles of Learning` → `Are You Learning…`) — display-name aliases to live paths; not contradictions.
- Research banks that say "page that does not exist yet" — bank status lines, same class as prior packets.
- Agent Glossary Codex entries — industry names in a glossary, not "this vault runs Codex" as the operating schema (Codex-as-live-schema remains mold M-3 / README).

---

## 3) Dead wikilinks

Resolved against tracked files (stem for bare names; full path when the link contains `/`). `raw/**` and `private/**` targets skipped (39 wiki hits into `raw/` — not dead). Heading-only `[[#…]]` skipped. `|` aliases unescaped before resolve. Design catalog files with em-dashes match; they are not dead.

### Persist from packet #5 (2)

- **DL-4 (persist)** `wiki/Concepts/Selfhood.md:90` → `wiki/Concepts/Meiwaku Has No Revenue Line`
  - No tracked file by that stem or path. `wiki/Concepts/Meiwaku.md` exists; `Selfhood and the Ledger.md` is the repair page already linked on the same paragraph. Line moved from `:39` (packet #5) after rewrite; target still missing.

- **DL-6 (persist)** `wiki/Research/Claude Fable 5.1 Bank.md:21` → `01 - Workbench/Fable - Research Bank - Claude and Grok Tools.md`
  - Not tracked; path matches `.gitignore` `01 - Workbench/*`. Formal exemption list is only `raw/**` and `private/**` — Workbench is the same "gitignored by design" class. Only Workbench `[[wikilink]]` left in live `wiki/` this sweep (other Workbench refs are backtick paths).

### New (4)

- **DL-7 (new)** wrong folder for LLM Tool Use (page lives under Domains):
  - `wiki/Concepts/A Motorcycle for the Mind.md:68` / `:94` → `wiki/Concepts/LLM Tool Use`
  - `wiki/Concepts/A Return to Code.md:84` → `wiki/Concepts/LLM Tool Use`
  - Live file: `wiki/Domains/AI & Tooling/LLM Tool Use.md`

- **DL-8 (new)** `wiki/Concepts/Riding the AGI.md:44` / `:120` → `wiki/Systems/AI & Agentic Systems/Software 3.0`
  - Path deleted this range; content merged into `wiki/Systems/AI & Agentic Systems/Context Engineering.md` (aliases include `Software 3.0`). Path-qualified link does not resolve.

- **DL-9 (new)** `wiki/Concepts/The Shortcut Problem.md:64` / `:150` → `wiki/Concepts/The Technique Is Only as Good as the Thinking It Produces`
  - Live file: `wiki/Dimensions/Self-Regulation/The Technique Is Only as Good as the Thinking It Produces.md`

- **DL-10 (new)** `wiki/Learning Craft/AI-Assisted Learning Workflow.md:122` / `:160` → `wiki/Dimensions/Retrieval/Interleaving for Complex Problem Solving`
  - Live file: `wiki/Dimensions/Deep Processing/Interleaving for Complex Problem Solving.md` (not under Retrieval)

### Resolved (0)

Alias-only mentions of deleted titles that already point at surviving paths were **not** counted dead.

---

## 4) Sourceless

Exact H2 `## Sources` required. **33 / 341** inclusive missing it (packet #5: 35 / 376). Nested: **30 / 338**. Near-miss heading `## Sources and links`: **0** (the five from #5 now use exact `## Sources`). `wiki/Glossary.md` still has `## Raw Source` / `## Source Note`, not `## Sources`.

### Resolved since packet #5 (6 gained Sources + 1 deleted)

Gained exact `## Sources`:
- `wiki/Concepts/Dating Apps - The Gini Coefficient.md`
- `wiki/Language Research/How Foreign Words Become Chinese.md`
- `wiki/Worldviews & the Political Order/Britain - Poorer Than Mississippi.md`
- `wiki/Worldviews & the Political Order/Single-Sex Spaces - The Asymmetry.md`
- `wiki/Worldviews & the Political Order/Socialism - The Calculation Problem.md`
- `wiki/Worldviews & the Political Order/The Gen Z Gender War - The Split.md`

Deleted while sourceless:
- `wiki/Systems/AI & Agentic Systems/Least-Cost Interpretation.md`

### New (5)

All new research banks without `## Sources`:
- `wiki/Research/Everybodyism and the Maturity Crisis Bank.md`
- `wiki/Research/Four Quadrants Bank.md`
- `wiki/Research/Levels of Thinking Bank.md`
- `wiki/Research/The Table Bank.md`
- `wiki/Research/Thinking About Thinking Bank.md`

### Persist (28 = 25 nested + 3 wiki-root)

- wiki/Concepts/The Same Model Twice.md
- wiki/Design/Design, Condensed.md
- wiki/Dimensions/Mindset/Mindset, Condensed.md
- wiki/Fashion/The Personal Uniform.md
- wiki/Fitness/Movement as Accretion.md
- wiki/Fitness/The Treadmill Library.md
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
- wiki/Techniques/Techniques - Learning Craft.md
- wiki/Travel/Reading as Local.md
- wiki/Travel/Warm Countries, Cold Countries.md
- wiki/Worldviews & the Political Order/Worldviews & the Political Order.md
- wiki/Writing Craft/The Cold Open.md

Wiki-root (3; persist from packet #2):
- wiki/Glossary.md
- wiki/ICS Program Map.md
- wiki/Timeline.md

New pages with exact Sources: Five Thinking Habits, Levels of Thinking - The Step Back, Thinking on Paper - Mindmaps…, Fitness Mindsets, China / Europe / Genetics / Late Stage Feminism, Five Writing Templates.

Redirects among the misses: **0**.

---

## 5) Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/`). History sections ("What's Gone", Evolution, changelog, stack history) exempt. `hermes/` still present as a tracked live-tool tree.

### Persist from packet #1 (6)

Line numbers re-checked; unchanged in substance.

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

No Ollama in instruction/config as live (stack history only). No new mold ID this sweep. **Six packets, zero mold edits — drop proposal from packet #4 still stands.**

---

## Packet #5 → #6 scorecard

| ID | Packet #5 | Packet #6 |
|---|---|---|
| C-1 Quartz vs Astro | persist | **persist** |
| C-4 Current roster AGENTS.md vs stack table | persist | **persist** (AGENTS three-model + Claude-primary-wiki still untouched) |
| DL-4 Selfhood → Meiwaku Has No Revenue Line | persist | **persist** (now `:90`) |
| DL-6 Workbench Fable bank link | persist | **persist** |
| DL-7..10 path-dead after moves/merges | — | **new** (LLM Tool Use folder; Software 3.0 path; Technique folder; Interleaving folder) |
| Sourceless | 35/376 | **33/341**; −6 gained Sources; −1 deleted; +5 new banks |
| Mold GROK/README/tools/hermes | persist (6) | **persist** (drop still recommended) |
| Near-duplicates | 0 | **0** |

### Action scorecard (packets 1–6; reaffirm after #4)

Wedge has acted on: near-duplicates (cleared), most dead wikilinks, sourceless (big drop; still chipping), contradictions C-2/C-3 (Hermes wiki pages). **Never acted on mold (M-1..6 identical since packet 1), C-1, C-4, or DL-4.** DL-6 untouched since #5. Propose again: **drop the mold check**; keep C-4 / DL-4 / path-dead hygiene live; optionally park C-1 and DL-6 (gitignored Workbench class).

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure and dead-link counts. `raw/**` and `private/**` targets not dead. No repo writes.*
