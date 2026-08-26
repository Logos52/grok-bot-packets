# Knowledge Base Review Packet #3
**Canary:** HEAD `01a7d5c48b468a345b6a171d3b09ed710d55e13f` — 2026-08-24 04:36:46 +0700
**Prior HEAD:** `a466845f4479f2d88fe2d89eda79fd2949d8f221` (unchanged? NO — full sweep)
**Vs packet #2:** 9 named findings resolved (ND-5..9, C-2, C-3, DL-3, DL-5); 9 persist (C-1, C-4, DL-4, M-1..6); 0 new named ND/C/DL/M. Sourceless 71/338 → 29/355 glob (27 pages gained `## Sources`, 16 sourceless pages deleted, 4 new misses). 3 wiki-root notes from packet #2 still lack `## Sources` (this git's `wiki/**/*.md` pathspec does not match `wiki/*.md`).

Wiki pages: **355** tracked `wiki/**/*.md` (`git ls-files -z`). Packet #2's 338 plus the Worldviews & the Political Order promotion and other adds, minus stub/Hermes/dashboard/Bear-Hunter-split deletes. Range: 278 files, +23028/−3502. Four additional tracked notes sit in `wiki/*.md` (Bibliography, Glossary, ICS Program Map, Timeline) and are **not** in that glob here; packet #2 treated them as wiki pages, so they are rechecked below. Inclusive tracked wiki markdown = **359**. Line numbers re-verified; packet-2 cites that moved are noted.

## Counts
- Near-duplicates: 0 (new: 0, persist: 0, resolved: 5)
- Contradictions: 2 (new: 0, persist: 2, resolved: 2)
- Dead wikilinks: 1 (new: 0, persist: 1, resolved: 2)
- Sourceless: 29 / 355 glob wiki pages (singular `## Source`: 0; persist 25, new 4, plus 3 wiki-root from packet #2)
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## 1) Near-duplicates

Merge candidates only. Redirect stubs, condensed/hub, book/concept, core/practice, and challenge-protocol vs dimension-hub splits are **not** flagged.

### Resolved from packet #2 (5)

The leftover `type: practice-track` stubs in `wiki/Dimensions/30-Day Challenges/` were **deleted** this range. The hub still points at the `* Challenge.md` pages. Same-stem `wiki/Dimensions/{X}.md` hubs remain, with different H1s and jobs (dimension vs 30-day protocol) — already "considered, not flagged" in packet #2.

- **ND-5 (resolved)** `wiki/Dimensions/30-Day Challenges/Deep Processing.md` deleted; `Deep Processing Challenge.md` remains.
- **ND-6 (resolved)** `Mindset.md` stub deleted; `Mindset Challenge.md` remains.
- **ND-7 (resolved)** `Retrieval.md` stub deleted; `Retrieval Challenge.md` remains.
- **ND-8 (resolved)** `Self-Management.md` stub deleted; `Self-Management Challenge.md` remains.
- **ND-9 (resolved)** `Self-Regulation.md` stub deleted; `Self-Regulation Challenge.md` remains.

Packet #1 pairs ND-1..4 stay resolved. The ND-1 / ND-2 redirect stubs (`wiki/Systems/Obsidian Dashboard.md`, `wiki/Concepts/Grok - How to Remember Everything You Read.md`) were themselves deleted this range, as was `wiki/Concepts/30-Day Challenge – Mindset.md`. Suicidal Empathy book vs concept still has distinct H1s (`Suicidal Empathy (Book)` vs `Suicidal Empathy`).

### New (0)

No merge candidates. Same-H1 collisions: none. Same-stem collisions: only the intentional book/concept Suicidal Empathy pair.

### Considered, not flagged

- `wiki/Dimensions/30-Day Challenges/{X} Challenge.md` vs `wiki/Dimensions/{X}.md` — challenge protocol vs dimension hub; different H1s and openings (same as packet #2).
- `Opening Doors` / `Opening Moves Catalog` / `The Cold Open` / `The Context Problem` — four layers (paragraph door, first-sentence moves, operational cold-open register, context-gap). Cross-linked; not copies. Research siblings (`Blog Craft Research Bank`, `Context Problem Research Bank`, `ATTEMPT-CATALOG-context-problem.md`) are banks/catalogs, not twin pages.
- `Grok 4.6 and Grok Bot` / `Current Agentic LLM Stack` / `Standing Research Agents` / `Grok Bot Fleet Structures` / the Grok Bot research banks — model-card vs dated roster vs standing half vs unrulled candidates vs evidence banks.
- `Prohibition After Diffusion` (policy/diffusion) vs `The Prohibition Loop` (writing-correction cycle) — same word, different jobs.
- `Exam Technique` vs `Exam Execution` — before-the-day nets vs day-of layer; Technique `:31` routes the rest to Execution.
- `Bear Hunter System.md` vs `Aim.md` / `Shoot.md` / `Skin.md` — hub vs the three passes (the old `Bear Hunter System - Aim/Shoot/Skin.md` files were deleted this range).
- Worldviews hub + 23 children — hub blurbs are one-line conclusions pointing at distinct pages (Racial Fatigue ≠ Who Gets Called Racist ≠ White Guilt ≠ Racial Egalitarianism, etc.).
- `wiki/Books/Suicidal Empathy.md` ↔ `wiki/Concepts/Suicidal Empathy.md` — still the book/concept split.
- `Marginal Gains` / `Marginal Gains in Practice` — still core vs operating layer.
- Research banks sharing the boilerplate sentence "Verified research bank, gathered by parallel research agents…" (Blog Craft, Two Egos, Self-Talk) — identical *template* opening, different topics. Not merges.
- `*, Condensed` vs full pages — hub + condensed doctrine.
- `_archive/` excluded from merge pressure.

---

## 2) Contradictions

### Persist from packet #2 (2)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine. Line numbers re-checked; they did not move.
  - Astro (current): `AGENTS.md:403-405` ("## Static Site (Astro)"; "Astro builds from `src/`"); `AGENTS.md:420` ("The site is a normal Astro project"); `README.md:126` ("built with Astro"); `.gitignore:63` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts are `astro dev` / `astro build`.
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`"); `:19` ("Quartz `ignorePatterns`"); `:64` ("then runs `npx quartz build` to publish"); frontmatter tag `:10` still `quartz`.
  - Extra cites (same contradiction, not a new item): `AGENTS.md:392` still names Quartz's "`RemoveDrafts` filter" inside the Astro publish section; `tools/scripts/setup-site.sh:4-7` is a live script that clones Quartz v4 and would overwrite `package.json` (`:35-56`); `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site" (`:52` notes the denylist was replicated from the former `quartz.config.ts`).

- **C-4 (persist) Current model roster disagrees.**
  - `AGENTS.md:67` — "We use three models in the **current setup**: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." GPT section at `:88-93`; rule of thumb `:95-98`. Health-check/status report paths at `:199` / `:214` still hard-code `01 - Workbench/GPT - …`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:16-26` table (as of August 2026, `updated: 2026-08-12`): Primary = Claude Cowork (Fable 5); Coding = Grok Build (`grok-4.6`); Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT. No "Grok (remote)" as a third peer.** Grok Bot / standing half is not mentioned in `AGENTS.md` at all.
  - New this range, same contradiction (not a new ID): `wiki/Systems/AI & Agentic Systems/Grok 4.6 and Grok Bot.md:29` restates the stack split ("Judgment work on this vault still sits on Fable in Cowork. Execution still sits on Grok Build.") and points at Current Stack as the dated roster. Both stack pages are present-tense "current"; AGENTS.md is too.

### Resolved from packet #2 (2)

- **C-2 (resolved) Hermes/Ollama current vs retired.** The two live/current pages are **deleted**: `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md` and `wiki/Systems/AI & Agentic Systems/Hermes Agent.md`. `Current Agentic LLM Stack.md:34-41` now holds the retirement only under **What's Gone** / **Evolution** (history, exempt as a live-vs-live clash). Wiki Hermes mentions that remain: that history block, and one omission footnote on `wiki/Systems/AI & Agentic Systems/Agentic Engineering, Condensed.md:56` ("agent-specific setups (Hermes Agent)") — a leftover name in an omit-list, not a current-roster claim. Not re-flagged.

- **C-3 (resolved) Hermes Access Boundaries claimed, absent from AGENTS.md.** The claiming sentence lived on Hybrid Model Workflows (packet #2 `:58`). That page is gone. `AGENTS.md` still has no Hermes heading (the only hit is `:410`, denylist path `hermes/`). Nothing now claims the missing section exists.

### Not flagged

- `wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md:17` ("Nothing on this page is ruled") vs `Standing Research Agents.md:17` (four standing agents) — candidate vs current, same as packet #2.
- `Grok 4.6 and Grok Bot.md:25` quotes public API list prices; `Current Agentic LLM Stack.md:32` says the *desk stack* is subscription or local, nothing pay-per-token. The 4.6 page calls the prices "a card, not a stack change" (`:29`). Not a clash.
- `Grok 4.6 and Grok Bot.md:29` notes `Human vs AI Capability Lens` still grades a July 2026 4.3 snapshot and calls that row stale — acknowledged, not silent.
- Exam Technique and Exam Execution both treat sleep as a lever (before-the-day vs day-of); they cross-link rather than disagree.
- `wiki/Research/Immigration and the Woke Left Bank.md:19` ("Evidence for a page that does not exist yet") vs the now-live `wiki/Worldviews & the Political Order/The Woke Retreat - The New Electorate Claim.md`. Stale bank status line, not two conflicting theses.
- `PRDs/**` Ollama mentions remain product-plan "later swap, not now."

---

## 3) Dead wikilinks

Resolved against tracked files (stem for bare names; full path when the link contains `/`). `raw/**` and `private/**` targets skipped (20 hits, all `raw/` — not dead). Heading-only `[[#…]]` skipped. Markdown `.md` links: none dead in wiki. Wrong-folder paths that still resolve by filename stem (e.g. `wiki/Concepts/LLM Tool Use` → `wiki/Domains/AI & Tooling/LLM Tool Use.md`) are **not** flagged — packet #2 only counted a path-style link dead when the stem itself was missing (DL-5).

### Persist from packet #2 (1)

- **DL-4 (persist)** `wiki/Concepts/Selfhood.md:39` → `wiki/Concepts/Meiwaku Has No Revenue Line`
  - No tracked file by that stem or path. `wiki/Concepts/Meiwaku.md` exists; `Selfhood and the Ledger.md` is the repair page already linked on the same line. Still looks like a planned sibling that was never added.

### Resolved from packet #2 (2)

- **DL-3 (resolved)** `wiki/ICS Program Map.md:131` now points at `[[wiki/Decision Making/Judging a Decision by Its Process|judging a decision by its process]]`. `Good Decisions.md` stays deleted. Other wiki pages already used the `|Good Decisions` alias onto the replacement; this map line caught up. Out-of-wiki leftovers from packet #2 (`journal/red-team-pruning.md:47,244` and `log.md:214`) were retargeted the same way — still out of the wiki count, and no longer dead.

- **DL-5 (resolved)** `wiki/Language Research/Language Research.md:22` → `wiki/Research/Transliteration Into Chinese Bank`
  - File **renamed** this range: `wiki/Language Research/Transliteration Into Chinese.md` → `wiki/Research/Transliteration Into Chinese Bank.md` (R100). The hub path now matches a tracked file.

### New (0)

Only DL-4 remains. Prose (not a wikilink) on `wiki/Techniques/Techniques - Learning Craft.md:31` still says "See Bear Hunter System - Aim, Bear Hunter System - Shoot, Bear Hunter System - Skin" after those filenames were folded into `Aim.md` / `Shoot.md` / `Skin.md` — noted, not counted.

---

## 4) Sourceless

Exact H2 `## Sources` required. **29 / 355** glob wiki pages missing it (packet #2: 71 / 338). Singular H2 `## Source`: **0** (packet #2's one case, `wiki/Learning Craft/Reading & Retention.md:268`, is now `## Sources` at `:103`). No `## Source Note` in the glob set.

This git's `wiki/**/*.md` glob does not return the 4 notes in `wiki/*.md`. Packet #2 listed three of them as sourceless; they still are (rechecked by reading the files):

- `wiki/Glossary.md:84` — `## Source Note` (glossary entry for "Source Note", not a Sources section)
- `wiki/ICS Program Map.md` — no Source/Sources H2 (ends at the Coverage notes section, line 147)
- `wiki/Timeline.md` — none (17 lines)
- `wiki/Bibliography.md:14` — **has** `## Sources` (not a miss)

Inclusive miss rate if those root notes are counted as wiki pages: **32 / 359**.

Redirects among the glob 29: **0** (the three packet-2 redirects were deleted).

### Notable clusters (glob 29)

- **8 condensed doctrine pages** still have no Sources: Design, Mindset, Chinese Characters, Minimalism, Money, Story Craft, Learning, Agentic Engineering.
- **7 Research** files (4 persist banks + 3 new): Blog Craft / Self-Talk / Self-Talk and the Two Egos Bridge / Two Egos, plus new `ATTEMPT-CATALOG-context-problem.md`, `Immigration and the Woke Left Bank.md`, `Report Intro Paragraph Bank.md`.
- **4 Systems/AI operating notes** besides the condensed page: Bot Operating Rules, Current Agentic LLM Stack, Grok Bot Fleet Structures, Least-Cost Interpretation.
- **Story Craft wing** was the packet-2 cluster (21 misses). This sweep added `## Sources` to the full pages; only `Story Craft, Condensed.md` remains.
- **Worldviews:** 23 of 24 new pages have `## Sources`; only the hub is missing.
- Fitness (2) and Travel (2) unchanged.

### New (4)

- `wiki/Research/ATTEMPT-CATALOG-context-problem.md` (`type: catalog`)
- `wiki/Research/Immigration and the Woke Left Bank.md` (`type: research`; evidence bank for the Woke Retreat page)
- `wiki/Research/Report Intro Paragraph Bank.md` (`type: bank`)
- `wiki/Worldviews & the Political Order/Worldviews & the Political Order.md` (hub)

### Persist from packet #2 (25 in glob)

See full list. The other 46 packet-2 misses are gone from this set: **27 gained `## Sources`** (Design Expansion, Best-attempt Encoding, Exam Technique, four Learning Craft pages including Reading & Retention, and the Story Craft full pages), **16 deleted** (challenge stubs, Bear Hunter Aim/Shoot/Skin, Note-Taking, both Obsidian Dashboard paths, Gbrain, Hermes Agent, Hybrid, two redirect aliases).

### Full list (29 glob + 3 wiki-root)

Glob (29):

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
- wiki/Research/ATTEMPT-CATALOG-context-problem.md *(new)*
- wiki/Research/Blog Craft Research Bank.md
- wiki/Research/Immigration and the Woke Left Bank.md *(new)*
- wiki/Research/Report Intro Paragraph Bank.md *(new)*
- wiki/Research/Self-Talk Research Bank.md
- wiki/Research/Self-Talk and the Two Egos Bridge Bank.md
- wiki/Research/Two Egos Research Bank.md
- wiki/Story Craft/Story Craft, Condensed.md
- wiki/Syntheses/Learning, Condensed.md
- wiki/Systems/AI & Agentic Systems/Agentic Engineering, Condensed.md
- wiki/Systems/AI & Agentic Systems/Bot Operating Rules.md
- wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md
- wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md
- wiki/Systems/AI & Agentic Systems/Least-Cost Interpretation.md
- wiki/Techniques/Techniques - Learning Craft.md
- wiki/Travel/Reading as Local.md
- wiki/Travel/Warm Countries, Cold Countries.md
- wiki/Worldviews & the Political Order/Worldviews & the Political Order.md *(new)*
- wiki/Writing Craft/The Cold Open.md

Wiki-root, outside `wiki/**/*.md` on this git (3; persist from packet #2):

- wiki/Glossary.md (`## Source Note` at :84, not `## Sources`)
- wiki/ICS Program Map.md
- wiki/Timeline.md

---

## 5) Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/`). History sections ("What's Gone", Evolution, changelog) exempt. Wiki C-2 is the roster contradiction, not mold — and is now resolved.

### Persist from packet #1 / #2 (6)

Line numbers re-checked; they did not move.

- **M-1 (persist)** `GROK.md:11` — "Latest `hermes/skills/l3-to-l2-voice-converter/references/style-feedback.md` (living before/after refinements)" — presents the hermes/ tree as the living voice-standard location.
- **M-2 (persist)** `GROK.md:65` — "When using these standards (in chat, Grok Build, Hermes, or any remote session)" — Hermes listed as a current session type beside Grok Build.
- **M-3 (persist)** `README.md:75` — "e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex" — Codex presented as a live schema consumer. (Generic architecture example, not "this vault runs Codex"; same line as packets #1–#2.)
- **M-4 (persist)** `tools/wiki-cleanup-ritual.md:16` — "**AI-agnostic** — any agent (Claude, Grok, ChatGPT, Hermes, others) can read this prompt and execute the steps."
- **M-5 (persist)** `tools/publish-snapshots.md:15` — same Hermes-in-the-agent-list phrasing, plus Quartz live trigger (`npx quartz build`).
- **M-6 (persist)** `hermes/` tree, present tense as a live TUI/runtime. Representative (lines unchanged):
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:27` — "Inside Hermes TUI, you can say things like:"
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:74` — "This skill stays pure Hermes/Grok — no external scripts."
  - `hermes/skills/curator/SKILL.md:4,24` — "Lightweight Hermes skill stub" / "Recommended inside Hermes TUI"
  - `hermes/skills/evolution/README.md:50,75,100,127` — "Now Working in Hermes TUI"; "Open Hermes TUI (Grok-4.3 available)"; "ready for experimental use in the Hermes TUI when desired."
  - `hermes/skills/evolution/evaluate-variant/SKILL.md:14,49` — "Recommended inside Hermes TUI"; "Always uses Grok-4.3 via the current Hermes session"
  - `hermes/skills/kb-synthesis-orchestrator/setup.md:11` — "Add the `kanban` toolset to your orchestrator profile in `~/.hermes/config.yaml`"

`CLAUDE.md` and `AGENTS.md` do **not** present Hermes/Ollama/Codex as live (`AGENTS.md:410` only lists `hermes/` as a denylist path). No Ollama in instruction/config; Ollama-as-live is gone from wiki current-tense pages (C-2 resolved). No new mold this sweep.

`02 - System/L3-Brief-Policy-Options.md` mentions `outputs/L3/Hermes/` as a folder name / "legacy" — not counted as live-tool mold.

---

## Packet #2 scorecard

| ID | Packet #2 | Packet #3 |
|---|---|---|
| ND-5..9 leftover 30-Day stubs vs Challenge pages | merge (5) | **resolved** (stubs deleted) |
| C-1 Quartz vs Astro | persist | **persist** (same files/lines; RemoveDrafts / setup-site.sh / ledger.mjs / publish-guard.mjs) |
| C-2 Hermes live vs retired | persist | **resolved** (Hybrid + Hermes Agent deleted; retirement is What's Gone) |
| C-3 Hermes Access Boundaries missing | persist | **resolved** (claiming page deleted) |
| C-4 Current roster AGENTS.md vs stack table | new | **persist** (AGENTS.md still Claude/Grok/GPT; stack still Cowork / Grok Build / Grok Bot; 4.6 page agrees with the stack) |
| DL-3 ICS Program Map → Good Decisions | new | **resolved** (retargeted to Judging a Decision by Its Process) |
| DL-4 Selfhood → Meiwaku Has No Revenue Line | new | **persist** (`:39` unchanged; no such file) |
| DL-5 Language Research hub → Transliteration Bank | new | **resolved** (file renamed to that path) |
| Sourceless | 71/338 | **29/355 glob** (27 gained Sources, 16 deleted, 4 new); +3 wiki-root persist |
| Mold GROK/README/tools/hermes | persist (6) | **persist** (same files; lines re-checked) |

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure. `raw/**` and `private/**` targets not dead. No repo writes.*
