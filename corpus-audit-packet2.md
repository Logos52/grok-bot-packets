# Knowledge Base Review Packet #2
**Canary:** HEAD `a466845f4479f2d88fe2d89eda79fd2949d8f221` — 2026-08-14 16:15:05 +0700
**Prior HEAD:** `6b23e6baae49ef93e1ee86c5e81fa25c8bf5f598` (unchanged? NO — full sweep)
**Vs packet #1:** 6 named findings resolved (ND-1..4, DL-1, DL-2); sourceless 222/328 → 71/338 (~151 pages gained `## Sources`). 9 named findings persist (C-1..3 + 6 mold). New this sweep: 5 near-dup pairs, 1 roster contradiction, 3 dead wikilinks.

Wiki pages: **338** tracked `wiki/**/*.md` (`git ls-files -z`). Packet #1's 328 plus 11 adds minus 1 delete (`wiki/Decision Making/Good Decisions.md` → `Judging a Decision by Its Process.md`). Large Grok regen in the range; line numbers re-verified.

## Counts
- Near-duplicates: 5 (of which new: 5, persist: 0, resolved: 4)
- Contradictions: 4 (new: 1, persist: 3, resolved: 0)
- Dead wikilinks: 3 (new: 3, persist: 0, resolved: 2)
- Sourceless: 71 / 338 wiki pages (singular `## Source`: 1; persist ~69, new ~2)
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## 1) Near-duplicates

Merge candidates only. Same-stem hub-vs-track, condensed-vs-full, and book-vs-concept splits were read and are **not** flagged.

### New (5)

The 30-Day Challenge hub (`wiki/Dimensions/30-Day Challenges.md:26-30`) points at the `* Challenge.md` pages. Those five were **added since packet #1**. The older `type: practice-track` files (last updated 2026-05-24) keep the **same title** and the same four-week outline. Fold the stubs into the Challenge pages or convert them to redirects.

- **ND-5 (new)** `wiki/Dimensions/30-Day Challenges/Deep Processing.md` ↔ `wiki/Dimensions/30-Day Challenges/Deep Processing Challenge.md` — identical title "30-Day Challenge - Deep Processing"; stub is a four-week outline, Challenge page is the regen'd full plan.
- **ND-6 (new)** `wiki/Dimensions/30-Day Challenges/Mindset.md` ↔ `wiki/Dimensions/30-Day Challenges/Mindset Challenge.md` — identical title; same week names (Breaking Your Fall → Breaking Chains). Hub links the Challenge file.
- **ND-7 (new)** `wiki/Dimensions/30-Day Challenges/Retrieval.md` ↔ `wiki/Dimensions/30-Day Challenges/Retrieval Challenge.md` — identical title; stub weeks match the Challenge page's week headings.
- **ND-8 (new)** `wiki/Dimensions/30-Day Challenges/Self-Management.md` ↔ `wiki/Dimensions/30-Day Challenges/Self-Management Challenge.md` — identical title; same Week 1–4 arc (Problem Mapping → Fading).
- **ND-9 (new)** `wiki/Dimensions/30-Day Challenges/Self-Regulation.md` ↔ `wiki/Dimensions/30-Day Challenges/Self-Regulation Challenge.md` — identical title; stub is a four-week outline beside a full Challenge page.

### Resolved from packet #1 (4)

- **ND-1 (resolved)** `wiki/Systems/Obsidian Dashboard.md` ↔ `wiki/Self Management/Obsidian Dashboard.md` — Systems path is now `type: redirect` / `status: moved` (line 16: "kept only as a redirect"). Stub remains as an alias, not a merge candidate.
- **ND-2 (resolved)** `wiki/Concepts/Grok - How to Remember Everything You Read.md` ↔ `wiki/Learning Craft/Reading & Retention.md` — Concepts path is now `type: redirect` / `status: empty-redirect` (line 16: folded into Reading & Retention).
- **ND-3 (resolved)** `wiki/Books/Suicidal Empathy.md` ↔ `wiki/Concepts/Suicidal Empathy.md` — intentional split: book page (`type: book`, H1 "Suicidal Empathy (Book)") vs concept page (`type: concept`, H1 "Suicidal Empathy"). Concept page line 66 routes institutional cases to the book page. Not a merge.
- **ND-4 (resolved)** `wiki/Dimensions/Mindset/Marginal Gains.md` ↔ `wiki/Dimensions/Mindset/Marginal Gains in Practice.md` — complementary core vs operating layer; both cross-link (Practice line 17: "The core idea and the full tracker live in [[Marginal Gains]]"). Same stacking example still repeats, but the jobs are distinct. Not a merge.

### Considered, not flagged

- Same-stem `wiki/Dimensions/30-Day Challenges/{X}.md` vs `wiki/Dimensions/{X}.md` — challenge protocol vs dimension hub; different H1s and openings.
- `Story Craft` / `Agentic Engineering` / other `*, Condensed` pairs — hub + condensed doctrine, linked as such.
- `wiki/Concepts/Selfhood.md` vs `wiki/Concepts/Selfhood and the Ledger.md` — complementary; Ledger is the speaking/count repair.
- Remaining redirect stubs (ND-1, ND-2, plus `wiki/Concepts/30-Day Challenge – Mindset.md` → Challenges/Mindset) are aliases, not duplicates.

---

## 2) Contradictions

### Persist from packet #1 (3)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine.
  - Astro (current): `AGENTS.md:403-405` ("## Static Site (Astro)"; "Astro builds from `src/`"); `README.md:126` ("built with Astro"); `.gitignore:63` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts are `astro dev` / `astro build`.
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`"); `:19` ("Quartz `ignorePatterns`"); `:64` ("then runs `npx quartz build` to publish").
  - Extra cites this sweep (same contradiction, not a new item): `AGENTS.md:392` still names Quartz's "`RemoveDrafts` filter" inside the Astro section; `tools/scripts/setup-site.sh:4-7` is a live script that clones Quartz v4 and would overwrite `package.json`; `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site".

- **C-2 (persist) Hermes/Ollama current vs retired.**
  - Retired: `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:16` ("the only local models left are audio instruments"); `:35-36` ("What's Gone" — "Hermes 3 via Ollama … retired within weeks"); `:41` Evolution May 2026 retired.
  - Still live/current: `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md:17` ("shifting toward using **Hermes** (the agent) as the primary actor"); `:21` ("treating **Hermes as the agent**"); `:43-47` ("Current Setup (as of May 2026)" — Hermes main interface, `hermes3:8b` via Ollama).
  - Still live/current: `wiki/Systems/AI & Agentic Systems/Hermes Agent.md:17` ("Hermes functions as an autonomous operator for your work"); `:33` ("Use Hermes when the work has history"); `:47-48` (`hermes run` / `hermes skills list` as current commands); `:77-85` "When to Use Hermes".
  - Hybrid and Hermes Agent were **not** part of the Aug 2026 regen (`updated: 2026-05-17` / `2026-05-24`). Current Stack was (`updated: 2026-08-12`).

- **C-3 (persist) Hermes Access Boundaries claimed, absent from AGENTS.md.**
  - Claimed: `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md:58` — "Strict read/write boundaries are now defined in [[AGENTS.md#hermes-access-boundaries-security-model|AGENTS.md → Hermes Access Boundaries]]".
  - Absent: `AGENTS.md` has **zero** occurrences of "Hermes" and no such heading. Closest live model section is `AGENTS.md:65-98` (Claude / Grok / GPT only).

### New (1)

- **C-4 (new) Current model roster disagrees.**
  - `AGENTS.md:67` — "We use three models in the **current setup**: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." GPT section at `:88-93`; rule of thumb `:95-98`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:18-26` table (as of August 2026): Primary = Claude Cowork; Coding = Grok Build; Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT. No "Grok (remote)" as a third peer.** Grok Bot / standing half is not mentioned in `AGENTS.md` at all.
  - These are both present-tense "current" claims, not history sections.

### Not flagged

- `wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md` (five bots incl. Steward) vs `Standing Research Agents.md` (four agents) — Fleet page says "Nothing on this page is ruled" (`:17`). Candidate vs current, not a contradiction.
- `PRDs/**` Ollama mentions are product-plan "later swap, not now" — not wiki/instruction roster.

---

## 3) Dead wikilinks

Resolved against tracked files. `raw/**` and `private/**` targets skipped (6 hits, all `raw/` — not dead). Heading-only `[[#…]]` skipped. Markdown `.md` links: none dead in wiki.

### Resolved from packet #1 (2)

- **DL-1 / DL-2 (resolved)** `wiki/Story Craft/The Rogue's Code.md:106-107` no longer point at `01 - Workbench/…`. Those lines are now open questions; Sources at `:111`. Packet-1 gitignored workbench targets are gone.

### New (3)

- **DL-3 (new)** `wiki/ICS Program Map.md:131` → `Good Decisions`
  - Target file `wiki/Decision Making/Good Decisions.md` **deleted since packet #1**. Replacement is `wiki/Decision Making/Judging a Decision by Its Process.md` (other wiki pages already retarget with alias `|Good Decisions`; this map line was not updated).

- **DL-4 (new)** `wiki/Concepts/Selfhood.md:39` → `wiki/Concepts/Meiwaku Has No Revenue Line`
  - No tracked file by that stem or path. `wiki/Concepts/Meiwaku.md` exists; this looks like a planned sibling page linked from a new Selfhood page (added since packet #1).

- **DL-5 (new)** `wiki/Language Research/Language Research.md:22` → `wiki/Research/Transliteration Into Chinese Bank`
  - No such file. Actual page: `wiki/Language Research/Transliteration Into Chinese.md`. At packet-1 HEAD this hub linked the correct path; the regen introduced the broken `wiki/Research/… Bank` path.

### Out of wiki (not counted)

Tracked `journal/red-team-pruning.md:47,244` and `log.md:185` still link `wiki/Decision Making/Good Decisions`. Left out of the count (wiki-primary).

---

## 4) Sourceless

Exact H2 `## Sources` required. **71 / 338** wiki pages missing it (packet #1: 222 / 328).

Singular H2 `## Source` (not `## Sources`), counted in the 71:

- `wiki/Learning Craft/Reading & Retention.md:268` — `## Source` (one bullet to `raw/sources/How to Remember Everything You Read.md`)

Also: `wiki/Glossary.md` has `## Source Note` (not a Sources section).

Redirects among the 71 (expected empty): 3
- `wiki/Systems/Obsidian Dashboard.md`
- `wiki/Concepts/Grok - How to Remember Everything You Read.md`
- `wiki/Concepts/30-Day Challenge – Mindset.md`

New pages since packet #1 that are sourceless: `wiki/Systems/AI & Agentic Systems/Bot Operating Rules.md`, `wiki/Writing Craft/The Cold Open.md`. The five new `* Challenge.md` pages **have** `## Sources`. The five leftover practice-track stubs do not.

Notable cluster: 21 Story Craft pages (almost the whole wing except a few that have Sources, e.g. The Rogue's Code).

### Full list (71)

- wiki/Concepts/30-Day Challenge – Mindset.md (redirect)
- wiki/Concepts/Grok - How to Remember Everything You Read.md (redirect)
- wiki/Concepts/The Same Model Twice.md
- wiki/Design/Design Expansion — Reading & Resources.md
- wiki/Design/Design, Condensed.md
- wiki/Dimensions/30-Day Challenges/Deep Processing.md
- wiki/Dimensions/30-Day Challenges/Mindset.md
- wiki/Dimensions/30-Day Challenges/Retrieval.md
- wiki/Dimensions/30-Day Challenges/Self-Management.md
- wiki/Dimensions/30-Day Challenges/Self-Regulation.md
- wiki/Dimensions/Deep Processing/Bear Hunter System - Aim.md
- wiki/Dimensions/Deep Processing/Bear Hunter System - Shoot.md
- wiki/Dimensions/Deep Processing/Bear Hunter System - Skin.md
- wiki/Dimensions/Deep Processing/Best-attempt Encoding.md
- wiki/Dimensions/Deep Processing/Note-Taking.md
- wiki/Dimensions/Mindset/Mindset, Condensed.md
- wiki/Domains/Miscellaneous/Exam Technique.md
- wiki/Fashion/The Personal Uniform.md
- wiki/Fitness/Movement as Accretion.md
- wiki/Fitness/The Treadmill Library.md
- wiki/Glossary.md
- wiki/ICS Program Map.md
- wiki/Language Research/How Foreign Words Become Chinese.md
- wiki/Language/Chinese/Chinese Characters, Condensed.md
- wiki/Learning Craft/Clinical Learning System.md
- wiki/Learning Craft/Microlearning System.md
- wiki/Learning Craft/Reading & Retention.md (## Source singular)
- wiki/Learning Craft/Theme-First Text Analysis.md
- wiki/Minimalism/Minimalism, Condensed.md
- wiki/Money/Money, Condensed.md
- wiki/Research/Blog Craft Research Bank.md
- wiki/Research/Self-Talk Research Bank.md
- wiki/Research/Self-Talk and the Two Egos Bridge Bank.md
- wiki/Research/Two Egos Research Bank.md
- wiki/Self Management/Obsidian Dashboard.md
- wiki/Story Craft/Arc Types.md
- wiki/Story Craft/Character Voice.md
- wiki/Story Craft/Companion Arcs and Party Banter.md
- wiki/Story Craft/Diagnosing a Character.md
- wiki/Story Craft/Foils and Pairings.md
- wiki/Story Craft/Interiority Through Action and Object.md
- wiki/Story Craft/Motif and Symbol.md
- wiki/Story Craft/Premise and Controlling Idea.md
- wiki/Story Craft/Round Characters and the Telling Detail.md
- wiki/Story Craft/Seeding and Payoff.md
- wiki/Story Craft/Setting as Character.md
- wiki/Story Craft/Stakes Without Mortality.md
- wiki/Story Craft/Story Craft, Condensed.md
- wiki/Story Craft/Story Craft.md
- wiki/Story Craft/Story Under a Vocabulary Ceiling.md
- wiki/Story Craft/The Change Arc.md
- wiki/Story Craft/The Character Web.md
- wiki/Story Craft/The Iceberg and World as Pressure.md
- wiki/Story Craft/The Low Point and Catharsis.md
- wiki/Story Craft/The Moral Core.md
- wiki/Story Craft/Tonal Modulation.md
- wiki/Syntheses/Learning, Condensed.md
- wiki/Systems/AI & Agentic Systems/Agentic Engineering, Condensed.md
- wiki/Systems/AI & Agentic Systems/Bot Operating Rules.md
- wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md
- wiki/Systems/AI & Agentic Systems/Gbrain and Lossless.md
- wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md
- wiki/Systems/AI & Agentic Systems/Hermes Agent.md
- wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md
- wiki/Systems/AI & Agentic Systems/Least-Cost Interpretation.md
- wiki/Systems/Obsidian Dashboard.md (redirect)
- wiki/Techniques/Techniques - Learning Craft.md
- wiki/Timeline.md
- wiki/Travel/Reading as Local.md
- wiki/Travel/Warm Countries, Cold Countries.md
- wiki/Writing Craft/The Cold Open.md

---

## 5) Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/**`). History sections ("What's Gone", Evolution, changelog) exempt. Wiki C-2 is the roster contradiction, not mold.

### Persist from packet #1 (6)

- **M-1 (persist)** `GROK.md:11` — "Latest `hermes/skills/l3-to-l2-voice-converter/references/style-feedback.md` (living before/after refinements)" — presents the hermes/ tree as the living voice-standard location.
- **M-2 (persist)** `GROK.md:65` — "When using these standards (in chat, Grok Build, Hermes, or any remote session)" — Hermes listed as a current session type beside Grok Build.
- **M-3 (persist)** `README.md:75` — "e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex" — Codex presented as a live schema consumer. (Generic architecture example, not "this vault runs Codex"; same line as packet #1.)
- **M-4 (persist)** `tools/wiki-cleanup-ritual.md:16` — "**AI-agnostic** — any agent (Claude, Grok, ChatGPT, Hermes, others) can read this prompt and execute the steps."
- **M-5 (persist)** `tools/publish-snapshots.md:15` — same Hermes-in-the-agent-list phrasing, plus Quartz live trigger (`npx quartz build`).
- **M-6 (persist)** `hermes/` tree, present tense as a live TUI/runtime. Representative:
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:27` — "Inside Hermes TUI, you can say things like:"
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:74` — "This skill stays pure Hermes/Grok — no external scripts."
  - `hermes/skills/curator/SKILL.md:4,24` — "Lightweight Hermes skill stub" / "Recommended inside Hermes TUI"
  - `hermes/skills/evolution/README.md:50,75,100,127` — "Now Working in Hermes TUI"; "Open Hermes TUI (Grok-4.3 available)"; "ready for experimental use in the Hermes TUI when desired."
  - `hermes/skills/evolution/evaluate-variant/SKILL.md:14,49` — "Recommended inside Hermes TUI"; "Always uses Grok-4.3 via the current Hermes session"
  - `hermes/skills/kb-synthesis-orchestrator/setup.md:11` — "Add the `kanban` toolset to your orchestrator profile in `~/.hermes/config.yaml`"

`CLAUDE.md` and `AGENTS.md` do **not** present Hermes/Ollama/Codex as live (AGENTS.md:410 only lists `hermes/` as a denylist path). No Ollama in instruction/config; Ollama-as-live is wiki-only (C-2).

`02 - System/L3-Brief-Policy-Options.md` mentions `outputs/L3/Hermes/` as a folder name / "legacy" — not counted as live-tool mold.

---

## Packet #1 scorecard

| ID | Packet #1 | Packet #2 |
|---|---|---|
| ND-1 Obsidian Dashboard pair | merge | **resolved** (Systems path is a redirect) |
| ND-2 Grok reading / Retention | merge | **resolved** (empty-redirect) |
| ND-3 Suicidal Empathy book/concept | merge | **resolved** (intentional split, cross-linked) |
| ND-4 Marginal Gains / in Practice | merge | **resolved** (core vs operating layer) |
| C-1 Quartz vs Astro | yes | **persist** (+ setup-site.sh, RemoveDrafts, ledger.mjs) |
| C-2 Hermes live vs retired | yes | **persist** (Hybrid + Hermes Agent still May-tense) |
| C-3 Hermes Access Boundaries missing | yes | **persist** (AGENTS.md still 0× Hermes) |
| DL-1/DL-2 Rogue's Code → Workbench | yes | **resolved** |
| Sourceless | 222/328 | **71/338** (improved; list above) |
| Mold GROK/README/tools/hermes | yes | **persist** (same files; lines re-checked) |

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure. No repo writes.*
