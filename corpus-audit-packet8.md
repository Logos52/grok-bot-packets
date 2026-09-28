# Corpus wiki audit — packet #8
Date: 2026-09-28 08:15 +0700 (Asia/Saigon)
Repo: Logos52/logos52.github.io
HEAD: d05e7397699f129d3cac2bea5d39adf9934cc3ab (2026-09-22 16:45:13 +0700)
Prior full-audit HEAD: b0e32bb9197c41e9b1d8d0dbe7a8bb61be3c7cdd (2026-09-20 17:29:03 +0700)
Prior change-scan HEAD: d05e7397699f129d3cac2bea5d39adf9934cc3ab (scan #3, 2026-09-24) — same as current HEAD
Window: since packet #7 (2026-09-21). HEAD moved through change-scans #2/#3 to `d05e739`. Full five-check sweep (HEAD changed since last full audit). Range vs packet #7: 11 commits, 94 files, +855/−3726. Wiki pages: **352** tracked markdown under `wiki/` (`git ls-files` + `^wiki/.*\.md$`; `core.quotepath=false`). Packet #7: 350. Like-for-like: +2 adds, 0 wiki deletes. (`git ls-files 'wiki/**/*.md'` alone undercounts at 348 by missing four wiki-root files.)

New wiki pages this range:
- `wiki/Systems/Agentic Workflows/Karpathy LLM-Wiki.md`
- `wiki/Systems/Agentic Workflows/Poteto Paved Path.md`
(plus 17 `poteto-slides/*.jpg` assets under the same folder)

Non-wiki signal in the same range (context, not wiki-page counts): rewrite of Poteto into ordinary-language explainer; home/note-page reading changes; deletion of 27 writing-generator / handoff files under `02 - System/` (`0debd2d`); `CLAUDE.md` drop of the generator and holdings rewrite pass (`d05e739`). Packet #7's nine new pages (Argument Validation, All-In Summit packet, Cursor Cloud Agents, Grok Bot Galaxy, Picking a computer, Using Grok Bot, pstack, East Asian Exams, South Africa) remain present.

## Counts
- Near-duplicates: 0 (new: 0, persist: 0, resolved: 0)
- Contradictions: 2 (new: 0, persist: 2, resolved: 0)
- Dead wikilinks: 9 (new: 1, persist: 8, resolved: 0)
- Sourceless: 34/352 inclusive (new: 0, persist: 34, resolved: 0)
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## Near-duplicates

Merge candidates only. Redirect stubs, condensed/hub, book/concept, core/practice, challenge-protocol vs dimension-hub, research bank vs live page, dated field-packet series, and `*, Condensed` vs full are **not** flagged.

### New (0)

No merge candidates. Same-H1 collisions: none. Same-stem collisions: only the intentional book/concept Suicidal Empathy pair (exempt). Challenge ↔ dimension hub pairs remain the exempt protocol/hub pattern. Research-bank openings that share boilerplate (Blog Craft / Two Egos / Self-Talk) stay bank-pattern, not merges. Dated Grok Bot Field Packet pair stays series-exempt.

### Considered, not flagged (new pages this range)

- `Poteto Paved Path.md` vs `Agentic Engineering.md` / Condensed — talk-derived how-to (repeated correction → file or failing check) vs the agentic-engineering hub; Agentic Engineering now *links* Poteto under Related pages; complementary, not copies.
- `Karpathy LLM-Wiki.md` vs Context Engineering / wiki-system pages — Karpathy's LLM-wiki operating pattern as a workflow note vs the vault's context-engineering concept page; different jobs.
- Poteto vs Karpathy — both live under Agentic Workflows; different source talks and different operating claims; not merge pressure.

Packet #1–#7 ND pairs stay resolved. Packet #7's "considered, not flagged" agentic pages (Grok Bot Galaxy / Primer / Using Grok Bot / Condensed; Cursor Cloud Agents / Picking a computer / pstack; East Asian Exams vs Exam Execution; South Africa vs All-In research bank; Argument Validation hub) unchanged in role.

---

## Contradictions

### Persist from packet #7 (2)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine.
  - Astro (current): `AGENTS.md:399-401` ("## Static Site (Astro)"; "Astro builds from `src/`"); `AGENTS.md:416` ("The site is a normal Astro project"); `README.md:126` ("built with Astro"); `about.md:33` ("published through Astro"); `.gitignore:62` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts remain `astro` / `astro build` (description also notes re-platform from Quartz).
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:10` frontmatter tag `quartz`; `:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`"); `:64` ("then runs `npx quartz build` to publish").
  - Extra cites (same contradiction, not a new item): `tools/scripts/setup-site.sh:4-7` / `:25` / `:31-60` still clones Quartz v4 and would overwrite `package.json`; `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site" (`:57` notes denylist replicated from former `quartz.config.ts`).
  - Generator purge / CLAUDE.md edits this window did not touch these Quartz leftovers.

- **C-4 (persist) Current model roster disagrees.** Stack still puts **Grok 4.6** on the writer seat; `AGENTS.md`'s three-model block was not aligned.
  - `AGENTS.md:69` — "We use three models in the current setup: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." Claude subsection still "Primary model for … wiki work" (`:72`); general rule `:98` "Use **Claude** for file work, briefs, and wiki."; GPT health-check paths `:201` / `:216` still hard-code `01 - Workbench/GPT - …`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md` (`updated: 2026-09-11`): Primary writer = Grok Build (`grok-4.6`); Research on request = Claude Cowork; Vault pipeline = Grok Build; Coding = Grok Build; IDE = Cursor; Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT peer. Claude is not the default writer.** Hermes/Ollama appear only under history — correct and exempt from mold.
  - New workflow pages this range (Poteto, Karpathy) and the Agentic Engineering touch (`updated: 2026-09-22`) cite or sit beside the stack's one-writer-per-tree rule; they do not rewrite `AGENTS.md`. Gap unchanged.
  - Both `AGENTS.md` and the stack page remain present-tense "current"; the stack cites `journal/2026-09-01-grok-writes` for the writer-seat move.

### New (0)

No new cross-page claim conflicts found after the Poteto rewrite / generator purge. CLAUDE.md now states there is no generator file (consistent with the `02 - System/` deletes); that removes a possible stale-instruction path rather than creating a contradiction.

### Not flagged

- Alias retargets (`Software 3.0` → Context Engineering, `Pacing Skill Development` → Marginal Gains) — display-name aliases to live paths; not contradictions.
- Agent Glossary Codex entries — industry names in a glossary, not "this vault runs Codex" as the operating schema (Codex-as-live-schema remains mold M-3 / README).
- `AGENTS.md:23` Codex in the product-name pick-list before Agent Glossary — glossary routing, same as packet #7 (extra cite under M-3, not a new contradiction ID).

---

## Dead wikilinks

Resolved against tracked files (stem + frontmatter `aliases:` for bare names; full path when the link contains `/`). Path-qualified links that miss the exact path are dead even if the stem/alias lives elsewhere. `raw/**` and `private/**` targets skipped (39 wiki hits into `raw/` / `private/` — not dead). Heading-only `[[#…]]` skipped. Escaped `\|` aliases unescaped before resolve. Site HTML routes are not wiki targets — not counted.

### Persist from packet #7 (8)

- **DL-4 (persist)** `wiki/Concepts/Selfhood.md:90` → `wiki/Concepts/Meiwaku Has No Revenue Line`
  - No tracked file by that stem or path. `wiki/Concepts/Meiwaku.md` exists; `Selfhood and the Ledger.md` is the repair page already linked on the same paragraph. Target still missing.

- **DL-6 (persist)** `wiki/Research/Claude Fable 5.1 Bank.md:21` → `01 - Workbench/Fable - Research Bank - Claude and Grok Tools.md`
  - Not tracked; path matches `.gitignore` `01 - Workbench/*`. Formal exemption list is only `raw/**` and `private/**` — Workbench is the same "gitignored by design" class.

- **DL-7 (persist)** wrong folder for LLM Tool Use (page lives under Domains):
  - `wiki/Concepts/A Motorcycle for the Mind.md:68` / `:94` → `wiki/Concepts/LLM Tool Use`
  - `wiki/Concepts/A Return to Code.md:84` → `wiki/Concepts/LLM Tool Use`
  - Live file: `wiki/Domains/AI & Tooling/LLM Tool Use.md`

- **DL-8 (persist)** `wiki/Concepts/Riding the AGI.md:44` / `:120` → `wiki/Systems/AI & Agentic Systems/Software 3.0`
  - Path deleted earlier; content merged into `wiki/Systems/AI & Agentic Systems/Context Engineering.md` (aliases include `Software 3.0`). Path-qualified link does not resolve.

- **DL-9 (persist)** `wiki/Concepts/The Shortcut Problem.md:64` / `:150` → `wiki/Concepts/The Technique Is Only as Good as the Thinking It Produces`
  - Live file: `wiki/Dimensions/Self-Regulation/The Technique Is Only as Good as the Thinking It Produces.md`

- **DL-10 (persist)** `wiki/Learning Craft/AI-Assisted Learning Workflow.md:122` / `:160` → `wiki/Dimensions/Retrieval/Interleaving for Complex Problem Solving`
  - Live file: `wiki/Dimensions/Deep Processing/Interleaving for Complex Problem Solving.md` (not under Retrieval)

- **DL-11 (persist)** `wiki/Bibliography.md:17` → `How I use LLMs`
  - No tracked stem or alias. Was `outputs/L3/GPT/How I use LLMs.md` (deleted in the 2026-09-16 prune). Sibling cite on Context Engineering already uses exempt `raw/sources/…` form; Bibliography still uses the bare name.

- **DL-12 (persist)** `wiki/Bibliography.md:33` → `Andrej Karpathy From Vibe Coding to Agentic Engineering`
  - No tracked stem or alias. Was `outputs/L3/GPT/Andrej Karpathy From Vibe Coding to Agentic Engineering.md` (deleted same prune). Same repair shape as DL-11 (`raw/sources/…` or drop the local-transcript wikilink).

### New (1)

Exposed by the writing-generator purge (`0debd2d`) that deleted tracked `02 - System/Readers.md` while a research bank still path-links it.

- **DL-13 (new)** `wiki/Research/Context Problem Research Bank.md:293` → `02 - System/Readers`
  - File deleted this range (among the 27 `02 - System/` removals). No remaining tracked stem or alias named `Readers` under that path. Same bank also mentions the path in prose/backtick form at `:382` and an absolute local path at `:510` (not counted as additional wikilink IDs). Unlike DL-6, this target was tracked and then removed — not a standing gitignore class.

### Not flagged

- `[[Pacing Skill Development]]` on `Accuracy Before Speed.md:57` / `:92` — resolves via `aliases:` on `wiki/Dimensions/Mindset/Marginal Gains.md`.
- Escaped `\|` path links that point at live files after unescape (Dimensions hubs, Language pages, journal cites, Agent Glossary, stack page, South Africa cite from the All-In bank, etc.).

### Resolved (0)

---

## Sourceless

Exact H2 `## Sources` or `## Sources and links` accepted. **34 / 352** inclusive missing it (packet #7: 34 / 350). Nested rate roughly 31 / 349. Near-miss: `wiki/Glossary.md` still has `## Raw Source` / `## Source Note`, not `## Sources`.

### Resolved since packet #7 (0)

None of the prior 34 gained a Sources section; none of the prior sourceless pages were deleted.

### New (0)

Both new pages this range ship with `## Sources`:
- `wiki/Systems/Agentic Workflows/Karpathy LLM-Wiki.md:73`
- `wiki/Systems/Agentic Workflows/Poteto Paved Path.md:120`

### Persist (34 = 31 nested + 3 wiki-root)

- wiki/Argument Validation/Argument Validation.md
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
- wiki/Research/Everybodyism and the Maturity Crisis Bank.md
- wiki/Research/Four Quadrants Bank.md
- wiki/Research/Immigration and the Woke Left Bank.md
- wiki/Research/Levels of Thinking Bank.md
- wiki/Research/Report Intro Paragraph Bank.md
- wiki/Research/Self-Talk Research Bank.md
- wiki/Research/Self-Talk and the Two Egos Bridge Bank.md
- wiki/Research/The Table Bank.md
- wiki/Research/Thinking About Thinking Bank.md
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

Redirects among the misses: **0**.

---

## Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/`). History sections ("What's Gone", Evolution, changelog, stack history) exempt. `hermes/` still present as a tracked live-tool tree (27 tracked files). `CLAUDE.md` this window dropped generator/holdings language and has **no** Hermes/Ollama/Codex live hits — mold IDs themselves untouched.

### Persist from packet #1 (6)

Line numbers re-checked; unchanged in substance.

- **M-1 (persist)** `GROK.md:11` — "Latest `hermes/skills/l3-to-l2-voice-converter/references/style-feedback.md` (living before/after refinements)" — presents the hermes/ tree as the living voice-standard location.
- **M-2 (persist)** `GROK.md:65` — "When using these standards (in chat, Grok Build, Hermes, or any remote session)" — Hermes listed as a current session type beside Grok Build.
- **M-3 (persist)** `README.md:75` — "e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex" — Codex presented as a live schema consumer. Extra cite (not a new ID): `AGENTS.md:23` still lists Codex in the live pick-list before Agent Glossary.
- **M-4 (persist)** `tools/wiki-cleanup-ritual.md:16` — "**AI-agnostic** — any agent (Claude, Grok, ChatGPT, Hermes, others) can read this prompt and execute the steps."
- **M-5 (persist)** `tools/publish-snapshots.md:15` — same Hermes-in-the-agent-list phrasing, plus Quartz live trigger (`npx quartz build` at `:64`).
- **M-6 (persist)** `hermes/` tree, present tense as a live TUI/runtime. Representative:
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:27` — "Inside Hermes TUI, you can say things like:"
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:74` — "This skill stays pure Hermes/Grok — no external scripts."
  - `hermes/skills/curator/SKILL.md:4,24` — "Lightweight Hermes skill stub" / "Recommended inside Hermes TUI"
  - `hermes/skills/evolution/README.md:50` — "Now Working in Hermes TUI"
  - `hermes/skills/kb-synthesis-orchestrator/setup.md:11` — "Add the `kanban` toolset to your orchestrator profile in `~/.hermes/config.yaml`"

No Ollama in instruction/config as live (stack history only). No new mold ID this sweep. **Eight packets, zero mold edits — drop proposal from packet #4 still stands.**

---

## Scorecard (packets 1–8)

| ID | Packet #7 | Packet #8 |
|---|---|---|
| C-1 Quartz vs Astro | persist | **persist** |
| C-4 Current roster AGENTS.md vs stack table | persist | **persist** (Poteto/Karpathy + Agentic Engineering touch cite stack; AGENTS three-model + Claude-primary-wiki still untouched) |
| DL-4 Selfhood → Meiwaku Has No Revenue Line | persist | **persist** |
| DL-6 Workbench Fable bank link | persist | **persist** |
| DL-7..10 path-dead after moves/merges | persist | **persist** |
| DL-11..12 Bibliography bare transcripts | persist (new in #7) | **persist** |
| DL-13 Context Problem bank → `02 - System/Readers` | — | **new** (generator purge deleted tracked Readers.md) |
| Sourceless | 34/350 | **34/352**; same 34 pages; +2 new pages both have Sources |
| Mold GROK/README/tools/hermes | persist (6) | **persist** (drop still recommended) |
| Near-duplicates | 0 | **0** |

### Action scorecard (packets 1–8; reaffirm after #4)

Wedge has acted on: near-duplicates (cleared), most dead wikilinks (historically), sourceless (big early drop; stalled since ~#6), contradictions C-2/C-3 (Hermes wiki pages). This window he deleted the writing-generator stack and trimmed CLAUDE.md (good hygiene) but that **created** DL-13 by removing `02 - System/Readers` without updating the Context Problem bank cite. New Poteto / Karpathy pages correctly include `## Sources`. **Never acted on mold (M-1..6 identical since packet 1), C-1, C-4, or DL-4.** DL-6 untouched since #5. DL-7..12 untouched since introduced. Propose again: **drop the mold check**; keep ND, contradictions (esp C-4), dead (esp DL-4, path-dead hygiene, and purge-orphan cites like DL-13), sourceless; optionally park C-1 and DL-6 (gitignored Workbench class).

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure and dead-link counts. `raw/**` and `private/**` targets not dead. No Firecrawl. No repo writes. Report-only.*
