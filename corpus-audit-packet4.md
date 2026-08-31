# Knowledge Base Review Packet #4
**Canary:** HEAD `5726e9fdd365c3cb117f7bce350b17ae8e7ce18b` — 2026-08-28 16:36:57 +0700
**Prior HEAD:** `01a7d5c48b468a345b6a171d3b09ed710d55e13f` (packet #3) — changed, full sweep
**Vs packet #3:** 8 new wiki pages; 0 named ND/C/DL/M resolved; persist set unchanged (C-1, C-4, DL-4, M-1..6). Sourceless 29/355 glob + 3 wiki-root → 30 nested misses + 3 wiki-root (33/363 inclusive). One new miss: `Woke Mind Virus Bank.md`. This is packet 4, so the four-packet action scorecard is at the end.

Wiki pages: **363** tracked markdown under `wiki/` (`git ls-files -- wiki`, `*.md`). Nested 359 + 4 wiki-root (Bibliography, Glossary, ICS Program Map, Timeline). Packet #3's 355 glob + 8 new pages. Range vs 01a7d5c: 51 files, +4528/−53. No wiki deletes.

New wiki pages this range:
- `wiki/Concepts/Probability Distributions.md`
- `wiki/Research/Woke Mind Virus Bank.md`
- `wiki/Systems/AI & Agentic Systems/Agent Glossary.md`
- `wiki/Systems/AI & Agentic Systems/Agent Wrong-Door Log.md`
- `wiki/Systems/AI & Agentic Systems/Grok Bot Primer.md`
- `wiki/Systems/AI & Agentic Systems/How to Use the Claude Tools.md`
- `wiki/Systems/AI & Agentic Systems/The Writing Pipeline.md`
- `wiki/Worldviews & the Political Order/The Woke Mind Virus.md`

Line numbers re-verified. C-1 Astro cites moved (~3 lines) because AGENTS.md gained the Agent Glossary pointer and a Writing Pipeline bullet.

## Counts
- Near-duplicates: 0 (new: 0, persist: 0, resolved: 0)
- Contradictions: 2 (new: 0, persist: 2, resolved: 0)
- Dead wikilinks: 1 (new: 0, persist: 1, resolved: 0)
- Sourceless: 33 / 363 inclusive (30 nested + 3 wiki-root; new: 1, persist: 32, resolved: 0). Nested rate 30 / 359.
- Mold: 6 (new: 0, persist: 6, resolved: 0)

---

## 1) Near-duplicates

Merge candidates only. Redirect stubs, condensed/hub, book/concept, core/practice, challenge-protocol vs dimension-hub, research bank vs live page, and `*, Condensed` vs full are **not** flagged.

### New (0)

No merge candidates. Same-H1 collisions: none. Same-stem collisions: only the intentional book/concept Suicidal Empathy pair.

### Considered, not flagged (new pages)

- `Grok Bot Primer.md` vs `Grok 4.6 and Grok Bot.md` vs `Current Agentic LLM Stack.md` vs `Standing Research Agents.md` vs `Grok Bot Fleet Structures.md` vs `Bot Operating Rules.md` — primer is one-person setup (shared computer, one job, report-only); 4.6 page is the product card; stack is the dated roster; standing / fleet / rules are the always-on half at different resolutions. Cross-linked; not copies.
- `Agent Glossary.md` vs `wiki/Glossary.md` — industry product names (as of 28 August 2026) vs vault-term glossary. Different jobs.
- `How to Use the Claude Tools.md` vs `Agent Glossary.md` — which Claude door to walk into vs the name table. Glossary points at the Claude page for that job.
- `The Writing Pipeline.md` (wiki) vs `02 - System/Writing Pipeline.md` — wiki page is the four-stage mechanism; `02 - System/` is the operating spec (outside wiki, not a wiki merge). AGENTS.md and CLAUDE.md now point at the system file.
- `The Woke Mind Virus.md` vs `Woke Mind Virus Bank.md` vs `Immigration and the Woke Left Bank.md` — live stats-heavy page vs evidence bank vs a different bank. Same split packet #3 already declined to merge.
- `Agent Wrong-Door Log.md` — scoreboard of misses; not a twin of the glossary or the stack.
- `Probability Distributions.md` — unique cookbook; no sibling.

Packet #1–#3 ND pairs stay resolved. Dimension hubs vs `* Challenge.md` still different jobs.

---

## 2) Contradictions

### Persist from packet #3 (2)

- **C-1 (persist) Quartz vs Astro.** Live instruction still disagrees on the site engine. Astro cites moved ~3 lines after the AGENTS.md insert; Quartz leftovers did not move.
  - Astro (current): `AGENTS.md:406-408` ("## Static Site (Astro)"; "Astro builds from `src/`"); `AGENTS.md:423` ("The site is a normal Astro project"); `README.md:126` ("built with Astro"); `.gitignore:63` ("Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"); `package.json` scripts are `astro dev` / `astro build`.
  - Quartz (stale live-tool phrasing): `tools/publish-snapshots.md:15` ("for the Quartz site"; "Manually triggered before `npx quartz build`"); `:19` ("Quartz `ignorePatterns`"); `:64` ("then runs `npx quartz build` to publish"); frontmatter tag `:10` still `quartz`.
  - Extra cites (same contradiction, not a new item): `AGENTS.md:395` still names Quartz's "`RemoveDrafts` filter" inside the (now Astro) publish section; `tools/scripts/setup-site.sh:4-7` is a live script that clones Quartz v4 and would overwrite `package.json` (`:35-56`); `tools/ledger.mjs:7` writes `quartz/components/ledgerData.json`; `tools/scripts/publish-guard.mjs:3` header still says "public Quartz site" (`:52` notes the denylist was replicated from the former `quartz.config.ts`).

- **C-4 (persist) Current model roster disagrees.** Wider this week: the stack page grew a Claude Code seat and an explicit no-API ruling; AGENTS.md's three-model block was not touched.
  - `AGENTS.md:69` — "We use three models in the current setup: Claude/Opus (via Cowork), Grok (remote), and GPT (remote)." GPT section `:90-100`; health-check/status paths `:201` / `:216` still hard-code `01 - Workbench/GPT - …`.
  - `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:16-27` table (updated this range, `updated: 2026-08-28`): Primary = Claude Cowork (Fable 5); Vault pipeline = Claude Code (Fable 5); Coding = Grok Build (`grok-4.6`); Standing = Grok Bot; Local = Qwen3-TTS + Whisper. **No GPT. No "Grok (remote)" as a third peer.** Grok Bot / Claude Code / standing half are not in the AGENTS.md three-model block. `:34` rules API-metered seats off the roster ("i don't like anything with API.").
  - `wiki/Systems/AI & Agentic Systems/Grok 4.6 and Grok Bot.md:29` still restates the stack split (Fable in Cowork / Grok Build execution) and points at Current Stack as the dated roster. Both stack pages are present-tense "current"; AGENTS.md is too.
  - New this range, same contradiction (not a new ID): `AGENTS.md:23` now points operators at Agent Glossary / Wrong-Door Log before picking a product name, but the Working With Different Models section (`:67-100`) still lists the old three. Glossary documents Codex/Copilot/Devin as industry products; it is not a second roster.

### New (0)

### Not flagged

- `wiki/Research/Woke Mind Virus Bank.md:18` ("Evidence for a page that does not exist yet") vs live `wiki/Worldviews & the Political Order/The Woke Mind Virus.md`. Stale bank status line, same class as packet #3's Immigration bank vs Woke Retreat — not two conflicting theses.
- `wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md` ("Nothing on this page is ruled") vs `Standing Research Agents.md` — candidate vs current, same as packet #3.
- `Grok 4.6 and Grok Bot.md:25` public API list prices vs `Current Agentic LLM Stack.md:34` desk stack is subscription or local. The 4.6 page still calls the prices "a card, not a stack change" (`:29`).
- Wrong-Door Log Hermes/Ollama row (`:23`) is a dated miss under 2026-05, not a current-roster claim.
- Agent Glossary Codex CLI / Codex cloud entries (`:384-390`) are industry names with a September audit date, not "this vault runs Codex."
- `PRDs/**` Ollama mentions remain product-plan "later swap, not now."

---

## 3) Dead wikilinks

Resolved against tracked files (stem for bare names; full path when the link contains `/`). `raw/**` and `private/**` targets skipped (20 hits, all `raw/` — not dead). Heading-only `[[#…]]` skipped. `\|` aliases unescaped before resolve. Design catalog files with em-dashes in the filename exist and match; they are not dead.

### Persist from packet #3 (1)

- **DL-4 (persist)** `wiki/Concepts/Selfhood.md:39` → `wiki/Concepts/Meiwaku Has No Revenue Line`
  - No tracked file by that stem or path. `wiki/Concepts/Meiwaku.md` exists; `Selfhood and the Ledger.md` is the repair page already linked on the same line. Still looks like a planned sibling that was never added.

### New (0)

### Resolved (0)

---

## 4) Sourceless

Exact H2 `## Sources` required. **33 / 363** inclusive missing it (packet #3: 29 / 355 glob + 3 wiki-root). Nested: **30 / 359**. Singular H2 `## Source`: **0**. `wiki/Glossary.md:86` is still `## Source Note` (glossary entry, not a Sources section).

New wiki pages with Sources: Probability Distributions, Agent Glossary, Agent Wrong-Door Log, Grok Bot Primer, How to Use the Claude Tools, The Writing Pipeline, The Woke Mind Virus. Only the Woke Mind Virus **bank** missed.

Redirects among the misses: **0**.

### New (1)

- `wiki/Research/Woke Mind Virus Bank.md` (`type: research`; "Evidence for a page that does not exist yet")

### Persist (32 = 29 glob + 3 wiki-root)

Same 29 nested misses as packet #3, plus the three wiki-root notes. Clusters unchanged: 8 condensed doctrine pages, 7 research banks (now 8 with the new Woke Mind Virus Bank), 4 Systems/AI operating notes besides the condensed page, Fitness (2), Travel (2), Worldviews hub, The Cold Open, The Same Model Twice, The Personal Uniform, How Foreign Words Become Chinese, Techniques - Learning Craft.

### Full list (30 nested + 3 wiki-root)

Nested (30):

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
- wiki/Research/Woke Mind Virus Bank.md *(new)*
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
- wiki/Worldviews & the Political Order/Worldviews & the Political Order.md
- wiki/Writing Craft/The Cold Open.md

Wiki-root (3; persist from packet #2):

- wiki/Glossary.md (`## Source Note` at :86, not `## Sources`)
- wiki/ICS Program Map.md
- wiki/Timeline.md

`wiki/Bibliography.md` still has `## Sources`.

---

## 5) Mold

Instruction/config only (`AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/`). History sections ("What's Gone", Evolution, changelog) exempt. Wiki C-2 remains resolved. `hermes/` was not touched this range.

### Persist from packet #1 (6)

Line numbers re-checked; they did not move (GROK.md this range only rewrote the sentence-rhythm bullet at `:22`).

- **M-1 (persist)** `GROK.md:11` — "Latest `hermes/skills/l3-to-l2-voice-converter/references/style-feedback.md` (living before/after refinements)" — presents the hermes/ tree as the living voice-standard location.
- **M-2 (persist)** `GROK.md:65` — "When using these standards (in chat, Grok Build, Hermes, or any remote session)" — Hermes listed as a current session type beside Grok Build.
- **M-3 (persist)** `README.md:75` — "e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex" — Codex presented as a live schema consumer. Extra cite this range (not a new ID): `AGENTS.md:23` now lists Codex in the live pick-list ("picking Claude Code vs Cowork vs … vs Grok Build vs Codex vs Copilot vs Devin") before sending the reader to Agent Glossary.
- **M-4 (persist)** `tools/wiki-cleanup-ritual.md:16` — "**AI-agnostic** — any agent (Claude, Grok, ChatGPT, Hermes, others) can read this prompt and execute the steps."
- **M-5 (persist)** `tools/publish-snapshots.md:15` — same Hermes-in-the-agent-list phrasing, plus Quartz live trigger (`npx quartz build`).
- **M-6 (persist)** `hermes/` tree, present tense as a live TUI/runtime. Representative (lines unchanged; tree still 27 tracked files):
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:27` — "Inside Hermes TUI, you can say things like:"
  - `hermes/skills/l3-to-l2-voice-converter/SKILL.md:74` — "This skill stays pure Hermes/Grok — no external scripts."
  - `hermes/skills/curator/SKILL.md:4,24` — "Lightweight Hermes skill stub" / "Recommended inside Hermes TUI"
  - `hermes/skills/evolution/README.md:50` — "Now Working in Hermes TUI"
  - `hermes/skills/kb-synthesis-orchestrator/setup.md:11` — "Add the `kanban` toolset to your orchestrator profile in `~/.hermes/config.yaml`"

`CLAUDE.md` does not present Hermes/Ollama/Codex as live. `AGENTS.md:413` only lists `hermes/` as a denylist path (plus the new `:23` Codex pick-list under M-3). No Ollama in instruction/config. No new mold ID this sweep.

`02 - System/L3-Brief-Policy-Options.md` mentions `outputs/L3/Hermes/` as a folder name / "legacy" — not counted.

---

## Packet #3 scorecard

| ID | Packet #3 | Packet #4 |
|---|---|---|
| C-1 Quartz vs Astro | persist | **persist** (Astro cites moved to AGENTS.md:406-408 / :423; Quartz leftovers same files/lines) |
| C-4 Current roster AGENTS.md vs stack table | persist | **persist** (stack now adds Claude Code + no-API ruling; AGENTS three-model block untouched) |
| DL-4 Selfhood → Meiwaku Has No Revenue Line | persist | **persist** (`:39` unchanged; no such file) |
| Sourceless | 29/355 glob + 3 wiki-root | **30 nested + 3 wiki-root (33/363)**; +1 new bank; 0 resolved |
| Mold GROK/README/tools/hermes | persist (6) | **persist** (same files; GROK.md:11/:65 untouched) |
| Near-duplicates | 0 | **0** |

---

## Four-packet action scorecard (packets 1–4)

This was the assigned packet-4 extra: which checks Wedge acted on, and a proposal to drop the ones he never touched.

| Check | #1 | #2 | #3 | #4 | Acted on? |
|---|---|---|---|---|---|
| Near-duplicates | 4 | 5 | 0 | 0 | **Yes.** ND-1..4 gone by #2; leftover 30-Day stubs (ND-5..9) deleted by #3. Clear. |
| Contradictions | 3 | 4 | 2 | 2 | **Partial.** C-2/C-3 (Hermes live vs retired, missing AGENTS section) resolved in #3 by deleting the claiming pages. C-1 (Quartz leftovers) untouched all four packets. C-4 (AGENTS three-model vs stack) untouched since it appeared in #2; the stack page moved, AGENTS.md's roster block did not. |
| Dead wikilinks | 2 | 3 | 1 | 1 | **Yes, except DL-4.** DL-1/2 resolved by #2; DL-3/5 resolved by #3. DL-4 (planned Meiwaku sibling) has sat since #2. |
| Sourceless | 222 | 71/338 | 29/355 + 3 root | 33/363 | **Yes.** 222 → 71 → 29 was the big cleanup. This week: one new research bank, nothing of the persist list gained `## Sources`. |
| Mold | 16 (then grouped to 6) | 6 | 6 | 6 | **No.** M-1..6 are the same files and essentially the same lines as packet #1. The 16→6 drop was auditor grouping of the `hermes/` tree into one representative (M-6), not a vault edit. `hermes/` is still denylisted and unpublished. |

**Propose dropping: the mold check.** Four Mondays, zero edits. GROK.md still names Hermes as a session type and points at `hermes/skills/…` as living voice standards; README still uses Codex as the schema example; the two `tools/` prompts still list Hermes next to Claude/Grok; the `hermes/` tree still talks as a live TUI. Wedge is publishing Astro, running Cowork / Grok Build / Grok Bot, and denylisting `hermes/`. Repeating M-1..6 every week is noise.

Optionally park, not drop:
- **C-1** as a known tools/ leftover (the live site is Astro; `setup-site.sh` / `publish-snapshots.md` / `ledger.mjs` / `publish-guard.mjs` header are the rot). Keep it if a Quartz-shaped script running against this tree would still be a real incident.
- **DL-4** as a planned page that was never added. One line in Selfhood.md. Easy to keep as a single persist item without a full dead-link sweep if the sweep is ever trimmed.
- **C-4** I would **not** park. The stack page moved this week (Claude Code seat, no-API ruling) and AGENTS.md's "three models: Claude, Grok, GPT" block is now the stale half of a live operator doc, including the GPT workbench paths. That still mis-routes a session.

Keep weekly: near-duplicates (cheap, and it caught the stub wave in #2), contradictions (C-4 is still live), dead wikilinks (one persist, cheap), sourceless (the persist list is now a stable cluster — condensed pages, research banks, a few operating notes — still worth a count even if the full dump gets shorter).

---

*Sweep: tracked public tree only. `_archive/` excluded from merge pressure. `raw/**` and `private/**` targets not dead. No repo writes.*
