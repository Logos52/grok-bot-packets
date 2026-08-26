# Knowledge Base Review Packet #1
**Canary:** HEAD `6b23e6baae49ef93e1ee86c5e81fa25c8bf5f598` — 2026-08-12 (2026-08-12 15:30:20 +0700)
**Baseline:** first run (no prior HEAD)
**Scope notes:** Tracked `wiki/**/*.md` = 328 pages. Public tracked tree only; `raw/**` and `private/**` targets excluded from dead-link flags. Instruction/config mold sweep: `AGENTS.md`, `CLAUDE.md`, `GROK.md`, `README.md`, `tools/**`, `scripts/**`, `hermes/**`. `_archive/**` excluded from near-duplicate merge pressure.

## Counts
- Near-duplicates: 4
- Contradictions: 3
- Dead wikilinks: 2
- Sourceless: 222
- Mold: 16
- Note: no Ollama live-tool phrasing found in instruction/config surfaces (Ollama appears in wiki pages covered under Contradictions).

## 1. Near-duplicates

### ND-1: Obsidian Dashboard ↔ Obsidian Dashboard - Surface Everything That Matters Today in One Note
- `wiki/Systems/Obsidian Dashboard.md`
- `wiki/Self Management/Obsidian Dashboard.md`
- Why: Identical topic; Systems page is already an explicit redirect stub to Self Management — leftover duplicate path.

### ND-2: Grok - How to Remember Everything You Read ↔ How to Remember Everything You Read
- `wiki/Concepts/Grok - How to Remember Everything You Read.md`
- `wiki/Learning Craft/Reading & Retention.md`
- Why: Concepts stub states it was folded into Reading & Retention; empty model-specific page is merge/delete cleanup.

### ND-3: Suicidal Empathy (Book) ↔ Suicidal Empathy
- `wiki/Books/Suicidal Empathy.md`
- `wiki/Concepts/Suicidal Empathy.md`
- Why: Nearly identical thesis/opening doctrine (calibrated vs suicidal empathy, truth suppression, blank-slate felons); book note vs concept note overlap enough to pressure a clearer split or merge.

### ND-4: Marginal Gains ↔ Marginal Gains in Practice
- `wiki/Dimensions/Mindset/Marginal Gains.md`
- `wiki/Dimensions/Mindset/Marginal Gains in Practice.md`
- Why: Companion pair with overlapping stacking/1% doctrine; Practice page partly restates Marginal Gains — consolidation or sharper role split candidate.

### Reviewed and not flagged (false-positive guard)
- `*, Condensed` ↔ full hub pairs (e.g. Agentic Engineering, Story Craft, Mindset) — intentional condensed layer, not merge candidates.
- Bear Hunter System Aim / Shoot / Skin ↔ parent — sibling parts of one system.
- `30-Day Challenge – X` ↔ dimension hub `X` — challenge pages vs standing dimension pages; related naming, different jobs.
- Research banks (`Blog Craft` / `Two Egos` / `Self-Talk` / Bridge) — shared boilerplate openings, different lanes; not merges.
- Mandarin ↔ Vietnamese Language Learning Resources — parallel templates, different languages.
- Red Team Training (experience) ↔ Red Teaming (method) — related, not duplicates.

## 2. Contradictions

### C-1: Site engine is Quartz vs Astro (logos52.github.io)
- **Astro (current):** `AGENTS.md:403-405` — section "Static Site (Astro)"; "Astro builds from `src/`..."
- **Astro (current):** `README.md:126` — "built with Astro"
- **Astro (current):** `.gitignore:63` — "Quartz caches (engine removed; public/ is now Astro's TRACKED static dir)"
- **Quartz (stale live instructions):** `tools/publish-snapshots.md:15` — "for the Quartz site (`logos52.github.io`)... before `npx quartz build`"
- **Quartz (stale live instructions):** `tools/publish-snapshots.md:19` — "in Quartz `ignorePatterns`"
- **Quartz (stale live instructions):** `tools/publish-snapshots.md:64` — "then runs `npx quartz build` to publish"
- Why: Same public site cannot be both Astro-built and Quartz-built; publish-snapshots still instructs the retired engine.

### C-2: Hermes / Ollama presented as current primary stack vs explicitly retired
- **Retired (authoritative stack page, updated 2026-08-12):** `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:22` — Primary agent = Claude Cowork (Fable 5)
- **Retired:** `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:36` — "Hermes 3 via Ollama — ... It was retired within weeks..." (under `## What's Gone`)
- **Retired:** `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md:41` — May 2026 Hermes 3 8B via Ollama "Retired within weeks"
- **Live/current phrasing:** `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md:17` — "shifting toward using **Hermes** (the agent) as the primary actor"
- **Live/current phrasing:** `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md:45-47` — "Hermes (the agent tool) is the main interface" / "local `hermes3:8b` model via Ollama"
- **Live/current phrasing:** `wiki/Systems/AI & Agentic Systems/Hermes Agent.md:33` — "Use Hermes when the work has history..."
- Why: August stack page retires Hermes+Ollama; May-dated Hermes pages still read as operating doctrine without retirement banners.

### C-3: Hermes Access Boundaries claimed in AGENTS.md but absent
- **Claim:** `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md:58` — "Strict read/write boundaries are now defined in [[AGENTS.md#hermes-access-boundaries-security-model|AGENTS.md → Hermes Access Boundaries]]"
- **Counter:** `AGENTS.md` has no "Hermes Access Boundaries" / "Session Summary Habit" section (only `AGENTS.md:410` listing `hermes/` among not-published paths)
- Why: Factual status claim about where security boundaries live does not match the current AGENTS.md surface.

### Not flagged
- `wiki/Tsumugu/Tsumugu.md:16` "published Quartz wiki" — refers to the separate `tsumugu-wiki` repo / `/tsumugu-wiki` site (still documented as Quartz in `projects/tsumugu/docs/`), not the main KB Astro site.

## 3. Dead wikilinks

Scanned 3072 `[[wikilinks]]` across tracked wiki pages; markdown links to `.md` targets: 0 unresolved. Targets under `raw/**` and `private/**` excluded by design.

### DL-1
- `wiki/Story Craft/The Rogue's Code.md:106` → `[[01 - Workbench/Character Blueprint - How Two Minutes Sets Every Scene That Follows|Character Blueprint]]`
- Why: target not in tracked tree. (`01 - Workbench/*` is gitignored except `README.md` / `Workbench.md`; not in the raw/private exempt list, so reported — severity closer to intentional-private than a broken public wiki page.)

### DL-2
- `wiki/Story Craft/The Rogue's Code.md:107` → `[[01 - Workbench/When the Frame Cannot See the Choice - Diagnostic Reading of Character|When the Frame Cannot See the Choice]]`
- Why: same as DL-1.

### Not flagged
- Site routes like `/tsumugu/cast/ruan-cao` (HTML under `public/tsumugu/cast/`) — not `.md` wiki-page links.
- Design catalog pages with em-dash filenames — resolve correctly against tracked tree once Unicode paths are handled.

## 4. Sourceless

Primary rule: missing exact H2 `## Sources`.
- **Count:** 222 / 328 tracked wiki pages
- **With `## Sources`:** 106
- **Singular `## Source` only (not counted as compliant):** `wiki/Learning Craft/Reading & Retention.md`
- **`## Bibliography` only:** (none)
- Other nearby headings seen but non-compliant: `## Source Note` (`wiki/Glossary.md`), `## Source-Finding`, `## Resource Catalog`

Full list (222):

- `wiki/Concepts/30-Day Challenge – Mindset.md`
- `wiki/Concepts/Accuracy Before Speed.md`
- `wiki/Concepts/Cave Theory.md`
- `wiki/Concepts/Declarative, Procedural, and Conditional Knowledge.md`
- `wiki/Concepts/Four Stages of Competence.md`
- `wiki/Concepts/Grok - How to Remember Everything You Read.md`
- `wiki/Concepts/How to Unlearn Old or Bad Habits Efficiently.md`
- `wiki/Concepts/Learning Styles Myth and Multimodal Learning.md`
- `wiki/Concepts/Reverse Causality.md`
- `wiki/Concepts/The Accretion Frame.md`
- `wiki/Concepts/The Same Model Twice.md`
- `wiki/Concepts/The Shortcut Problem.md`
- `wiki/Concepts/Wabi-Sabi.md`
- `wiki/Decision Making/Changing Decisions.md`
- `wiki/Decision Making/Choice Throttling.md`
- `wiki/Decision Making/Decision Making.md`
- `wiki/Decision Making/Decisional Delays.md`
- `wiki/Decision Making/Expectancy in Wicked Environments.md`
- `wiki/Decision Making/Good Decisions.md`
- `wiki/Decision Making/Positional Decisions and Expected Value.md`
- `wiki/Decision Making/The Uncertainty-Opportunity Tradeoff.md`
- `wiki/Design/Design Expansion — Reading & Resources.md`
- `wiki/Design/Design Two-Track Extraction.md`
- `wiki/Design/Design, Condensed.md`
- `wiki/Dimensions/30-Day Challenges.md`
- `wiki/Dimensions/30-Day Challenges/Deep Processing.md`
- `wiki/Dimensions/30-Day Challenges/Mindset.md`
- `wiki/Dimensions/30-Day Challenges/Retrieval.md`
- `wiki/Dimensions/30-Day Challenges/Self-Management.md`
- `wiki/Dimensions/30-Day Challenges/Self-Regulation.md`
- `wiki/Dimensions/Deep Processing.md`
- `wiki/Dimensions/Deep Processing/Aim.md`
- `wiki/Dimensions/Deep Processing/Bear Hunter System - Aim.md`
- `wiki/Dimensions/Deep Processing/Bear Hunter System - Shoot.md`
- `wiki/Dimensions/Deep Processing/Bear Hunter System - Skin.md`
- `wiki/Dimensions/Deep Processing/Bear Hunter System.md`
- `wiki/Dimensions/Deep Processing/Best-attempt Encoding.md`
- `wiki/Dimensions/Deep Processing/Chunking as a Technique - Good chunking at different levels, and how to layer importance and meaningfulness.md`
- `wiki/Dimensions/Deep Processing/Deep Processing Practice.md`
- `wiki/Dimensions/Deep Processing/Deep Processing for Research.md`
- `wiki/Dimensions/Deep Processing/Higher-Order Learning.md`
- `wiki/Dimensions/Deep Processing/Hipshot.md`
- `wiki/Dimensions/Deep Processing/Importance-Based Chunking.md`
- `wiki/Dimensions/Deep Processing/Inquiry-Based Learning.md`
- `wiki/Dimensions/Deep Processing/Interleaving for Complex Problem Solving.md`
- `wiki/Dimensions/Deep Processing/Knowledge Mastery - From Recognition to Usable Knowledge.md`
- `wiki/Dimensions/Deep Processing/Layers of Learning.md`
- `wiki/Dimensions/Deep Processing/Live Learning Events.md`
- `wiki/Dimensions/Deep Processing/Mindmaps.md`
- `wiki/Dimensions/Deep Processing/Non-Linear Note-Making.md`
- `wiki/Dimensions/Deep Processing/Note-Taking.md`
- `wiki/Dimensions/Deep Processing/Order Control.md`
- `wiki/Dimensions/Deep Processing/Prestudy.md`
- `wiki/Dimensions/Deep Processing/Problem-First Learning.md`
- `wiki/Dimensions/Deep Processing/ReCOVer System.md`
- `wiki/Dimensions/Deep Processing/Schema Construction, Assimilation, and Reorganization.md`
- `wiki/Dimensions/Deep Processing/Schema.md`
- `wiki/Dimensions/Deep Processing/Shoot.md`
- `wiki/Dimensions/Deep Processing/Skin.md`
- `wiki/Dimensions/Deep Processing/Survive and Thrive.md`
- `wiki/Dimensions/Deep Processing/Syntopical Reading - Learning from Multiple Dense Resources.md`
- `wiki/Dimensions/Deep Processing/Thinking on Paper.md`
- `wiki/Dimensions/Dimension Practice Tracks.md`
- `wiki/Dimensions/Dimensions of Learning.md`
- `wiki/Dimensions/Mindset.md`
- `wiki/Dimensions/Mindset/Compounding vs Additive Gains.md`
- `wiki/Dimensions/Mindset/Confidence Calibration.md`
- `wiki/Dimensions/Mindset/Fixed vs Growth Mindset.md`
- `wiki/Dimensions/Mindset/Locus of Control.md`
- `wiki/Dimensions/Mindset/Loss Aversion.md`
- `wiki/Dimensions/Mindset/Marginal Gains in Practice.md`
- `wiki/Dimensions/Mindset/Marginal Gains.md`
- `wiki/Dimensions/Mindset/Mindset, Condensed.md`
- `wiki/Dimensions/Mindset/Motivation.md`
- `wiki/Dimensions/Mindset/Neuroticism.md`
- `wiki/Dimensions/Mindset/Perfectionism and Overthinking.md`
- `wiki/Dimensions/Mindset/The Learning Zone and the Reversion Response.md`
- `wiki/Dimensions/Retrieval.md`
- `wiki/Dimensions/Retrieval/Breaching Questions.md`
- `wiki/Dimensions/Retrieval/Cramming.md`
- `wiki/Dimensions/Retrieval/Encoding and Retrieval.md`
- `wiki/Dimensions/Retrieval/Flashcards.md`
- `wiki/Dimensions/Retrieval/Group Study.md`
- `wiki/Dimensions/Retrieval/Interleaving - Multiple Angles and Session Design.md`
- `wiki/Dimensions/Retrieval/Interleaving Table.md`
- `wiki/Dimensions/Retrieval/Method of Loci.md`
- `wiki/Dimensions/Retrieval/Multipass System.md`
- `wiki/Dimensions/Retrieval/Opportunistic Retrieval.md`
- `wiki/Dimensions/Retrieval/Reconstruction - Retrieval Beyond Recall.md`
- `wiki/Dimensions/Retrieval/Reverse Explanation.md`
- `wiki/Dimensions/Retrieval/Revision.md`
- `wiki/Dimensions/Retrieval/Rote Learning and Memorisation.md`
- `wiki/Dimensions/Retrieval/Spaced Interleaved Retrieval.md`
- `wiki/Dimensions/Retrieval/WPW.md`
- `wiki/Dimensions/Self-Management.md`
- `wiki/Dimensions/Self-Management/How to Ask for Feedback.md`
- `wiki/Dimensions/Self-Management/Kolbs Experiential Cycle.md`
- `wiki/Dimensions/Self-Management/Performance Goals.md`
- `wiki/Dimensions/Self-Management/Reverse Goal Setting.md`
- `wiki/Dimensions/Self-Management/Skills Audit.md`
- `wiki/Dimensions/Self-Regulation.md`
- `wiki/Dimensions/Self-Regulation/Building the Radar.md`
- `wiki/Dimensions/Self-Regulation/Common Traps.md`
- `wiki/Dimensions/Self-Regulation/How to Maintain Sustainable Energy Under Pressure.md`
- `wiki/Dimensions/Self-Regulation/How to shift your brain to be motivated (when you don't feel like it).md`
- `wiki/Dimensions/Self-Regulation/Measuring Learning.md`
- `wiki/Dimensions/Self-Regulation/Metacognition - The Control Layer.md`
- `wiki/Dimensions/Self-Regulation/Metacognition as a Skill.md`
- `wiki/Dimensions/Self-Regulation/Opening the Black Box of Learning.md`
- `wiki/Dimensions/Self-Regulation/Pacing Skill Development.md`
- `wiki/Dimensions/Self-Regulation/The Technique Is Only as Good as the Thinking It Produces.md`
- `wiki/Dimensions/Upgrading Your Dimensions.md`
- `wiki/Domains/AI & Tooling/The Right vs Wrong Way to Work With AI.md`
- `wiki/Domains/Miscellaneous/Exam Execution.md`
- `wiki/Domains/Miscellaneous/Exam Technique.md`
- `wiki/Domains/Miscellaneous/How to diagnose and fix exam mistakes.md`
- `wiki/Domains/Miscellaneous/How to prepare for ultra high-volume exams.md`
- `wiki/Experiences/Experiences.md`
- `wiki/Fashion/The Personal Uniform.md`
- `wiki/Fitness/Movement as Accretion.md`
- `wiki/Fitness/The Treadmill Library.md`
- `wiki/Glossary.md`
- `wiki/ICS Program Map.md`
- `wiki/Language Research/How Foreign Words Become Chinese.md`
- `wiki/Language Research/Language Research.md`
- `wiki/Language/Aim-Shoot-Skin for Language Learning.md`
- `wiki/Language/Attention is Important.md`
- `wiki/Language/Character Primer.md`
- `wiki/Language/Chinese/Chinese Characters, Condensed.md`
- `wiki/Language/Freeflow Immersion.md`
- `wiki/Language/Hacking Comprehension Menu.md`
- `wiki/Language/Immersion Metalayers.md`
- `wiki/Language/Interactive Immersion.md`
- `wiki/Language/Noticing Game.md`
- `wiki/Language/Preparation.md`
- `wiki/Language/Refold Grammar Primers.md`
- `wiki/Language/Three Pillars of Language Learning.md`
- `wiki/Language/YouTube Immersion Account.md`
- `wiki/Learning Craft/Clinical Learning System.md`
- `wiki/Learning Craft/Microlearning System.md`
- `wiki/Learning Craft/Reading & Retention.md`
- `wiki/Learning Craft/Theme-First Text Analysis.md`
- `wiki/Minimalism/Environment Design.md`
- `wiki/Minimalism/Exit Strategy For Objects.md`
- `wiki/Minimalism/Minimalism, Condensed.md`
- `wiki/Minimalism/Ownership Cost.md`
- `wiki/Minimalism/Product Reduction.md`
- `wiki/Minimalism/Wanting Less.md`
- `wiki/Money/Define Enough.md`
- `wiki/Money/Investing and Budgeting Mindsets.md`
- `wiki/Money/Money as Life Energy.md`
- `wiki/Money/Money, Condensed.md`
- `wiki/Money/The Almanack of Naval Ravikant.md`
- `wiki/Money/The Savings Rate Is the Master Lever.md`
- `wiki/Money/Time Beats Timing.md`
- `wiki/Red Team/The Twitter Test.md`
- `wiki/Research/Blog Craft Research Bank.md`
- `wiki/Research/Self-Talk Research Bank.md`
- `wiki/Research/Self-Talk and the Two Egos Bridge Bank.md`
- `wiki/Research/Two Egos Research Bank.md`
- `wiki/Resources/Mandarin Chinese Language Learning Resources.md`
- `wiki/Resources/Vietnamese Language Learning Resources.md`
- `wiki/Self Management/Attention Management - Preserving Flow.md`
- `wiki/Self Management/Building a Schedule That Survives.md`
- `wiki/Self Management/Flow State.md`
- `wiki/Self Management/Habits, Productive Routines & PEER.md`
- `wiki/Self Management/Hyper-Focus and Hyper-Distractibility.md`
- `wiki/Self Management/OFF-Rest Timing.md`
- `wiki/Self Management/Obsidian Dashboard.md`
- `wiki/Self Management/Priority 0+1 System.md`
- `wiki/Self Management/Procrastination - a System Problem.md`
- `wiki/Self Management/Study Scheduling.md`
- `wiki/Self Management/Task Management.md`
- `wiki/Self Management/Techniques in School.md`
- `wiki/Self Management/Time Management, Attention & Scheduling.md`
- `wiki/Story Craft/Arc Types.md`
- `wiki/Story Craft/Character Voice.md`
- `wiki/Story Craft/Companion Arcs and Party Banter.md`
- `wiki/Story Craft/Diagnosing a Character.md`
- `wiki/Story Craft/Foils and Pairings.md`
- `wiki/Story Craft/Interiority Through Action and Object.md`
- `wiki/Story Craft/Motif and Symbol.md`
- `wiki/Story Craft/Premise and Controlling Idea.md`
- `wiki/Story Craft/Round Characters and the Telling Detail.md`
- `wiki/Story Craft/Seeding and Payoff.md`
- `wiki/Story Craft/Setting as Character.md`
- `wiki/Story Craft/Stakes Without Mortality.md`
- `wiki/Story Craft/Story Craft, Condensed.md`
- `wiki/Story Craft/Story Craft.md`
- `wiki/Story Craft/Story Under a Vocabulary Ceiling.md`
- `wiki/Story Craft/The Change Arc.md`
- `wiki/Story Craft/The Character Web.md`
- `wiki/Story Craft/The Iceberg and World as Pressure.md`
- `wiki/Story Craft/The Low Point and Catharsis.md`
- `wiki/Story Craft/The Moral Core.md`
- `wiki/Story Craft/The Wound and the Lie.md`
- `wiki/Story Craft/Tonal Modulation.md`
- `wiki/Syntheses/Are You Learning, or Just Using Techniques.md`
- `wiki/Syntheses/Balancing Multiple Interests - Breadth v Focus.md`
- `wiki/Syntheses/First Principles of Learning.md`
- `wiki/Syntheses/How Top Performers Learn.md`
- `wiki/Syntheses/ICS System.md`
- `wiki/Syntheses/Learning, Condensed.md`
- `wiki/Syntheses/Minimally Viable Learning System.md`
- `wiki/Syntheses/Prestudy, BHS, and SIR - Turning Information into Usable Structure.md`
- `wiki/Syntheses/The 30-Day Plan.md`
- `wiki/Systems/AI & Agentic Systems/Agentic Engineering, Condensed.md`
- `wiki/Systems/AI & Agentic Systems/Claude Fable.md`
- `wiki/Systems/AI & Agentic Systems/Current Agentic LLM Stack.md`
- `wiki/Systems/AI & Agentic Systems/Gbrain and Lossless.md`
- `wiki/Systems/AI & Agentic Systems/Grok Bot Fleet Structures.md`
- `wiki/Systems/AI & Agentic Systems/Hermes Agent.md`
- `wiki/Systems/AI & Agentic Systems/Hybrid Model Workflows, Grok + Hermes.md`
- `wiki/Systems/AI & Agentic Systems/Least-Cost Interpretation.md`
- `wiki/Systems/Obsidian Dashboard.md`
- `wiki/Techniques/Technique Training & Fundamentals.md`
- `wiki/Techniques/Techniques - Learning Craft.md`
- `wiki/Timeline.md`
- `wiki/Travel/Reading as Local.md`
- `wiki/Travel/Warm Countries, Cold Countries.md`
- `wiki/Tsumugu/Tsumugu.md`
- `wiki/Workflows/Knowledge Base as Thinking Partner.md`

## 5. Mold check

Retired tools watched as LIVE in instruction/config: **Hermes**, **Ollama**, **Codex**.
History / What's Gone / Evolution sections exempt. Wiki retirement narrative on `Current Agentic LLM Stack.md` exempt (correct history).
**Ollama:** no live-tool hits in instruction/config surfaces (see Contradictions for wiki).

### M-1
- `GROK.md:65`
- Snippet: When using these standards (in chat, Grok Build, Hermes, or any remote session): Explicitly load this file...
- Why: Lists Hermes alongside live runtimes as a place these standards are used.

### M-2
- `GROK.md:11`
- Snippet: Latest `hermes/skills/l3-to-l2-voice-converter/references/style-feedback.md` (living before/after refinements)
- Why: Presents the Hermes skill tree path as the living authority for voice refinements.

### M-3
- `README.md:75`
- Snippet: CLAUDE.md for Claude Code or AGENTS.md for Codex
- Why: Presents Codex as a current schema consumer / active agent stack option.

### M-4
- `tools/wiki-cleanup-ritual.md:16`
- Snippet: any agent (Claude, Grok, ChatGPT, Hermes, others) can read this prompt and execute the steps
- Why: Names Hermes as a live executor for the cleanup ritual.

### M-5
- `tools/publish-snapshots.md:15`
- Snippet: any agent (Claude, Grok, ChatGPT, Hermes, others)... Manually triggered before `npx quartz build`
- Why: Names Hermes as a live agent option (also couples to retired Quartz publish path).

### M-6
- `hermes/skills/evolution/SKILL.md:24`
- Snippet: This system is designed to run inside Hermes.
- Why: Present-tense instruction to run the evolution system inside Hermes.

### M-7
- `hermes/skills/evolution/SKILL.md:26`
- Snippet: Ready for first end-to-end run inside the Hermes TUI.
- Why: Current-status framing treats Hermes TUI as the active runtime.

### M-8
- `hermes/skills/evolution/README.md:13`
- Snippet: designed to run inside Hermes. It remains fully functional and available.
- Why: States the Hermes-hosted system remains fully functional/available.

### M-9
- `hermes/skills/evolution/README.md:100`
- Snippet: Open Hermes TUI (Grok-4.3 available).
- Why: Step-by-step activation checklist opens with launching Hermes TUI.

### M-10
- `hermes/skills/evolution/README.md:127`
- Snippet: The heavy evolutionary system is ready for experimental use in the Hermes TUI when desired.
- Why: Present readiness claim for Hermes TUI use.

### M-11
- `hermes/skills/evolution/run-generation/SKILL.md:24`
- Snippet: When user says inside Hermes TUI: "Run a generation..."
- Why: Executable procedure keyed to Hermes TUI invocations.

### M-12
- `hermes/skills/evolution/evaluate-variant/runner.md:3`
- Snippet: executable loop inside the Hermes TUI
- Why: Runner procedure assumes Hermes as the execution environment.

### M-13
- `hermes/skills/l3-to-l2-voice-converter/SKILL.md:27`
- Snippet: Inside Hermes TUI, you can say things like:
- Why: Live invocation guidance for Hermes TUI.

### M-14
- `hermes/skills/kb-synthesis-orchestrator/setup.md:6`
- Snippet: hermes kanban create kb-synthesis
- Why: CLI instructions for the Hermes tool.

### M-15
- `hermes/skills/kb-synthesis-orchestrator/setup.md:11`
- Snippet: Add the `kanban` toolset... in `~/.hermes/config.yaml`
- Why: Configures live Hermes user config.

### M-16
- `hermes/skills/curator/SKILL.md:24`
- Snippet: Natural Language (Recommended inside Hermes TUI)
- Why: Recommends Hermes TUI as the invocation surface.

### Mold cluster note
The entire `hermes/` tree (27 files) is written as a present-tense Hermes runtime skill pack. Items M-6–M-16 are the strongest live-instruction spores; many sibling lines repeat the same TUI/invocation pattern and were not each enumerated.

---
**Audit method:** read-only; `git ls-files -z` as tracked universe; automated wikilink resolution (path/stem/basename/alias/`\|`); title+opening near-dup scoring with human false-positive filter; rg + spot verification for contradictions/mold.
**Repo mutations:** none.
**Packet written:** `/workspace/corpus-audit-packet1.md`
