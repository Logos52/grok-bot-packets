# Corpus wiki audit — packet #7
Date: 2026-09-21 08:25 +0700 (Asia/Saigon)
Repo: Logos52/logos52.github.io
HEAD: b0e32bb9197c41e9b1d8d0dbe7a8bb61be3c7cdd (2026-09-20 17:29:03 +0700)
Prior full-audit HEAD: f143226ce2b5703fa3cc95ec12f6b1b8658877bd
Prior change-scan HEAD: 83ec03b22964eb57c4de7aad6954fd38c9b5e17f
Window: since packet #6 (2026-09-14). HEAD moved twice: change-scan #1 landed `83ec03b` (harden deploy + cut dead weight), then 4 further commits to `b0e32bb`. Full five-check sweep. Range vs packet #6: 9 commits, 756 files, +2857/−69032 (bulk of deletions from the 2026-09-16 prune). Wiki pages: **350** tracked markdown under `wiki/` (`git ls-files`, `core.quotepath=false`). Packet #6: 341. Like-for-like: +9 adds, 0 wiki deletes.

New wiki pages this range:
- `wiki/Argument Validation/Argument Validation.md`
- `wiki/Research/All-In Summit and Moon Packet 2026-09-16.md`
- `wiki/Systems/AI & Agentic Systems/Cursor Cloud Agents.md`
- `wiki/Systems/AI & Agentic Systems/Grok Bot Galaxy.md`
- `wiki/Systems/AI & Agentic Systems/Picking a computer.md`
- `wiki/Systems/AI & Agentic Systems/Using Grok Bot.md`
- `wiki/Systems/AI & Agentic Systems/pstack.md`
- `wiki/Worldviews & the Political Order/East Asian Exams - The Arms Race.md`
- `wiki/Worldviews & the Political Order/South Africa is a Warning to the West.md`

## Counts
- Near-duplicates: 0 (new: 0, persist: 0, resolved: 0)
- Contradictions: 2 (new: 0, persist: 2, resolved: 0)
- Dead wikilinks: 8 (new: 2, persist: 6, resolved: 0)
- Sourceless: 34/350 inclusive (new: 1, persist: 33, resolved: 0)
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## Near-duplicates

Merge candidates only. Redirect stubs, condensed/hub, book/concept, core/practice, challenge-protocol vs dimension-hub, research bank vs live page, dated field-packet series, and `*, Condensed` vs full are **not** flagged.

### New (0)

No merge candidates. Same-H1 collisions: none. Same-stem collisions: only the intentional book/concept Suicidal Empathy pair (exempt).

### Considered, not flagged (new pages)

- `Grok Bot Galaxy.md` vs `Grok Bot Primer.md` / `Using Grok Bot.md` / `Grok Bot, Condensed.md` — livestream findings map vs primer vs desk how-to vs condensed; different jobs, not copies. Condensed/hub pattern exempt.
- `Cursor Cloud Agents.md` / `Picking a computer.md` / `pstack.md` vs stack / Primer — seat map and product how-tos that cite the stack; complementary, not duplicates.
- `East Asian Exams - The Arms Race.md` vs `Exam Execution.md` — political-order thesis vs domain technique page.
- `South Africa is a Warning to the West.md` vs All-In Summit research packet — live page vs dated research bank (bank pattern exempt).
- `Argument Validation.md` — new hub; no sibling overlap into merge.

Packet #1–#6 ND pairs stay resolved.

---

## Contradictions

### Persist from packet #6 (2)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine.
  - Astro (current): `AGENTS.md:399-401` ("## Static Site (Astro)"; "Astro builds from `src/`"); `AGENTS.md:416` ("The site is a normal Astro project"); `README.md:126` ("built with Astro"); `about.md:33` ("published through Astro"); `.gitignore:62` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts remain `astro`/`astro build`.
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:10` frontmatter tag `quartz`; `:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`" context); `:64` ("then runs `npx quartz build` to publish").
  - Extra cites (same contradiction, not a new item): `tools/scripts/setup-site.sh:4-7` / `:25` / `:31-60` still clones Quartz v4 and would overwrite `package.json`; `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site" (`:57` notes denylist replicated from former `quartz.config.ts`).

- **C-4 (persist) Current model roster disagrees.** Stack still puts **Grok 4.6** on the writer seat; `AGENTS.md`'s three-model block was not aligned.
  - `AGENTS.md:69` — "We use three models in the current setup: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." Claude subsection still "Primary model for … wiki work" (`:72`); general rule `:98` "Use **Claude** for file work, briefs, and wiki."; GPT health-check paths `:201` / `:216` still hard-code `01 - Workbench/GPT - …`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md` (`updated: 2026-09-11`): Primary writer = Grok Build (`grok-4.6`); Research on request = Claude Cowork; Vault pipeline = Grok Build; Coding = Grok Build; IDE = Cursor; Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT peer. Claude is not the default writer.** Hermes/Ollama appear only under history (`:89`) — correct and exempt from mold.
  - New agentic pages this range (`Picking a computer`, `Using Grok Bot`, `Cursor Cloud Agents`, `pstack`, `Grok Bot Galaxy`) all cite the stack's writer seat (Grok 4.6 / Grok Build) and reinforce one-writer-per-tree — they widen the gap with `AGENTS.md` rather than resolve it.
  - Both `AGENTS.md` and the stack page are present-tense "current"; the stack cites `journal/2026-09-01-grok-writes` for the writer-seat move.

### New (0)

### Not flagged

- Alias retargets (`Software 3.0` → Context Engineering, `Pacing Skill Development` → Marginal Gains) — display-name aliases to live paths; not contradictions.
- New pages that say they do not add a seat / restaff — consistent with the stack, not a conflict.
- Agent Glossary Codex entries — industry names in a glossary, not "this vault runs Codex" as the operating schema (Codex-as-live-schema remains mold M-3 / README).

---

## Dead wikilinks

Resolved against tracked files (stem + frontmatter `aliases:` for bare names; full path when the link contains `/`). Path-qualified links that miss the exact path are dead even if the stem/alias lives elsewhere (same rule as packet #6). `raw/**` and `private/**` targets skipped (35 wiki hits into `raw/` — not dead). Heading-only `[[#…]]` skipped. `\|` aliases unescaped before resolve. Site HTML routes (`/tsumugu/cast/…`) are not wiki targets — not counted. Design catalog files with em-dashes match; they are not dead.

### Persist from packet #6 (6)

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

### New (2)

Both exposed by the 2026-09-16 deploy prune that deleted tracked `outputs/L3/**` transcripts the bare names previously stem-matched.

- **DL-11 (new)** `wiki/Bibliography.md:17` → `How I use LLMs`
  - No tracked stem or alias. Was `outputs/L3/GPT/How I use LLMs.md` (deleted in `83ec03b` range). Sibling cite on Context Engineering already uses exempt `raw/sources/…` form; Bibliography still uses the bare name.

- **DL-12 (new)** `wiki/Bibliography.md:33` → `Andrej Karpathy From Vibe Coding to Agentic Engineering`
  - No tracked stem or alias. Was `outputs/L3/GPT/Andrej Karpathy From Vibe Coding to Agentic Engineering.md` (deleted same prune). Same repair shape as DL-11 (`raw/sources/…` or drop the local-transcript wikilink).

### Not flagged

- `[[Pacing Skill Development]]` on `Accuracy Before Speed.md` — resolves via `aliases:` on `wiki/Dimensions/Mindset/Marginal Gains.md`.
- Escaped `\|` path links that point at live files after unescape (Dimensions hubs, Language pages, journal cites, Agent Glossary, etc.).

### Resolved (0)

---

## Sourceless

Exact H2 `## Sources` or `## Sources and links` accepted. **34 / 350** inclusive missing it (packet #6: 33 / 341). Nested rate roughly 31 / 347. Near-miss: `wiki/Glossary.md` still has `## Raw Source` / `## Source Note`, not `## Sources`.

### Resolved since packet #6 (0)

None of the prior 33 gained a Sources section; none of the prior sourceless pages were deleted.

### New (1)

- `wiki/Argument Validation/Argument Validation.md` (new hub this range; no `## Sources`)

### Persist (33 = 30 nested + 3 wiki-root)

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

New pages with Sources (8/9): All-In Summit packet, Cursor Cloud Agents, Grok Bot Galaxy, Picking a computer, Using Grok Bot, pstack, East Asian Exams, South Africa is a Warning to the West.

Redirects among the misses: **0**.

---

## Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/`). History sections ("What's Gone", Evolution, changelog, stack history) exempt. `hermes/` still present as a tracked live-tool tree (27 tracked files).

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

No Ollama in instruction/config as live (stack history only). No new mold ID this sweep. **Seven packets, zero mold edits — drop proposal from packet #4 still stands.**

---

## Scorecard (packets 1–7)

| ID | Packet #6 | Packet #7 |
|---|---|---|
| C-1 Quartz vs Astro | persist | **persist** |
| C-4 Current roster AGENTS.md vs stack table | persist | **persist** (new agentic pages cite stack; AGENTS three-model + Claude-primary-wiki still untouched) |
| DL-4 Selfhood → Meiwaku Has No Revenue Line | persist | **persist** |
| DL-6 Workbench Fable bank link | persist | **persist** |
| DL-7..10 path-dead after moves/merges | persist (new in #6) | **persist** |
| DL-11..12 Bibliography bare transcripts | — | **new** (outputs/L3 prune orphaned stem matches) |
| Sourceless | 33/341 | **34/350**; +1 Argument Validation hub; prior 33 untouched |
| Mold GROK/README/tools/hermes | persist (6) | **persist** (drop still recommended) |
| Near-duplicates | 0 | **0** |

### Action scorecard (packets 1–7; reaffirm after #4)

Wedge has acted on: near-duplicates (cleared), most dead wikilinks (historically), sourceless (big early drop; stalled this window), contradictions C-2/C-3 (Hermes wiki pages). **Never acted on mold (M-1..6 identical since packet 1), C-1, C-4, or DL-4.** DL-6 untouched since #5. DL-7..10 untouched since #6. Propose again: **drop the mold check**; keep ND, contradictions (esp C-4), dead (esp DL-4 and path-dead hygiene), sourceless; optionally park C-1 and DL-6 (gitignored Workbench class).

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure and dead-link counts. `raw/**` and `private/**` targets not dead. No Firecrawl. No repo writes. Report-only.*
