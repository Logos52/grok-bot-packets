---
id: 2026-09-08-rishabh7g-rung-hindi-marathi-offline-ladder-pwa
kind: article
title: rung — Hindi→Marathi offline ladder PWA; exit rituals; verified content
source: "https://github.com/rishabh7g/rung"
author: rishabh7g
published: 2026-09-08
captured: 2026-09-08
via: grokbot/Field
lane: learning
status: raw
private: false
---

# rung

A ladder of checkpoints for learning a language — not a timeline. First pair:
**Hindi (L1) → Marathi (L2)**. A fully offline, installable, mobile-first PWA:
no backend, no accounts, no audio, no runtime AI. Built by one person, for one
friend.

*rung* (formerly *Shidi*, शिडी — Marathi for "ladder") names the core metaphor: a
fixed sequence of 10 modules ("rungs"), each exited through its own ritual — every
sentence guessed right at least once in practice, then two fresh sentences understood.

## Start here

| Doc | What it is |
|---|---|
| [`docs/PRD-engineering.md`](docs/PRD-engineering.md) | Canonical engineering PRD — features F1–F9, phases P0–P5 |
| [`docs/PRD-design.md`](docs/PRD-design.md) | Canonical design PRD — flows, screens, components, tone |
| [`docs/01-plan.md`](docs/01-plan.md) | Implementation plan: stack, layout, data contracts, Devanagari primer. **Read before your first ticket.** |
| [`design/`](design/) | Design mockups + tokens (added by Rishabh as milestone D completes) |
| [`docs/design-contract.md`](docs/design-contract.md) | How to build UI against the design package — tokens, prototype fidelity, mobile rules |
| [`docs/04-font-notes.md`](docs/04-font-notes.md) | What bundling Mukta + Barlow proved: the specimen, glyph coverage, shipped font bytes (#85) |
| [`docs/05-pwa-notes.md`](docs/05-pwa-notes.md) | The PWA: manifest, precache byte tables, the airplane-mode gate and its screenshots, what still needs a phone (#90) |

## Development

**Prerequisites:** Node **22.22.2+ or 24.15+** (`engines.node`; CI runs 24) and npm. No
other runtime, no backend, no env vars. The floor is jsdom 30's, not ours — on Node 20
every test file fails to import before it asserts anything.

```bash
npm install
npm run dev     # http://localhost:5173
```

| Script | What it does |
|---|---|
| `npm run dev` | Vite dev server with HMR |
| `npm run build` | Typecheck (`tsc -b`) then production build into `dist/` |
| `npm run preview` | Serve the built `dist/` locally |
| `npm run typecheck` | TypeScript only — strict + `noUncheckedIndexedAccess` |
| `npm run test` | Vitest (jsdom + Testing Library), single run |
| `npm run lint` | ESLint (flat config), Prettier-compatible |
| `npm run format` | Prettier write across the source tree |
| `npm run content:validate` | Schema v5 + cross-checks over `content/*/modules/*.json` |
| `npm run content:build` | Builds `public/content/` from `content/` — strict by default |
| `npm run content:prompt -- <courseId> <moduleId>` | Renders the authoring prompt for one module into `.prompts/` (gitignored). Needs the prior module's index — run a dev `content:build` first |
| `npm run icons:build` | Regenerates `public/icons/*.png` from the header rails mark. Committed output; run it only when the mark changes |

### `scripts/verify.sh` — one line, or one failure

The gate before every PR (docs/01-plan.md §8). Run it from anywhere; it finds the repo root
itself:

```bash
scripts/verify.sh          # everything
scripts/verify.sh --fast   # everything except BUILD
```

A green run says exactly one thing, and exits 0:

```
TYPES ok | LINT ok | TEST 142/142 ok | CONTENT ok | BUILD ok
```

| Step | Exit | Command |
|---|---|---|
| TYPES | 10 | `npm run typecheck` |
| LINT | 20 | `npm run lint`, then `npx prettier --check .` — **either one failing is exit 20** |
| TEST | 30 | `npm run test`; the segment carries vitest's own count |
| CONTENT | 40 | `npm run content:build` — schema validation, word index and the strings check in one |
| BUILD | 50 | `npx vite build`; omitted entirely with `--fast` |

Steps run in that order and the **first failure stops the run**, so a red run names exactly one
thing: `FAIL <STEP> (exit <code>)`, the last 20 lines of that step's log, and the path to the
whole log. Nothing else is printed — no progress chatter to scroll past, on either colour.

```
FAIL TYPES (exit 10)

src/App.tsx(9,9): error TS2322: Type 'number' is not assignable to type 'string'.

log: /home/rrish/dev/shidi/.verify/types.log
```

Every step writes `.verify/<step>.log` (gitignored), and **the directory is wiped at the start of
every run** — so a missing log is proof that step never ran: the failure above leaves `types.log`
and nothing else.

Two things worth knowing before you read a result:

- **BUILD is `vite build`, not `npm run build`.** The npm script's `prebuild` would re-run tsc and
  `content:build`, so a content failure would resurface as `FAIL BUILD` long after CONTENT passed.
  The harness runs each thing once, under its own name.
- **CONTENT judges the exit code, never the output.** A strict build correctly ships nothing today
  (see the gate table below) and exits 0 — that is `CONTENT ok`, not an empty-output failure.

The harness has its own tests (`scripts/verify.test.ts`): they run it in a tmp dir against fake
`npm`/`npx` shims, because a test that really shelled out to `npm run test` would run vitest inside
vitest.

**This is the gate.** Run `bash scripts/verify.sh` locally before merging to `main`; there is no
CI job. There is deliberately no separate lint/test/build pipeline to keep in sync. When a run is
red, each step's full log is in `.verify/<step>.log`.

### The content gate — why `dev` and `build` see different content

`content:build` runs automatically as `predev` and `prebuild`, and it is the thing that
decides what a build is allowed to contain (PRD-engineering §3, §6.2, [D4]):

| | modules shipped |
|---|---|
| `npm run build` (`prebuild`, **strict — no flags**) | only `verified: true` **and** not `fixture: true`, from non-fixture courses |
| `npm run dev` (`predev`, `--with-unverified --with-fixtures`) | everything that validates |

**Strict is production truth: a learner build can never contain unreviewed or sample
content.** `verified: true` means a module has been reviewed and cleared to ship, and
`verifiedBy`/`verifiedAt` name who or what reviewed it and when — `tools/validate.ts`
rejects a verified module that carries no signature. **Since 2026-09-07 an authoring wave
ships `verified: true` by default**, in the same change as its review doc: the LLM review is
the review, it runs on the owner's standing authority, and `verifiedBy` says so in words. The
old two-step — author `false`, flip later — recorded nothing the signature does not, and left
correct content out of a learner build for no gain. On **2026-08-13** hi-mr
L1-M1..M10 were flipped to `verified: true` on the repo owner's explicit authority,
backed by an **LLM linguistic review** (`docs/07-llm-review-L1-M1-M5.md`,
`docs/07-llm-review-L1-M6-M10.md`, and the third pass that re-reviewed all ten blind,
`docs/08-marathi-third-review.md`), so `npm run build` now ships the full L1 ladder.
**The native-speaker gate is a separate, stricter bar and is still unmet.** The three
issues that tracked it (#64, #110, #111) were closed by the owner on 2026-08-13, so the
**22 open questions in `docs/08-marathi-third-review.md`** — which supersede the two
earlier lists — plus the **8 added by `docs/15-llm-review-hi-mr-surfaces.md`** (30 in
all) are the only remaining record of what a native reviewer still owes.

**hi-mr climbs to two levels (#425, #434, #443, 2026-09-07) — the first content above L1 in any
course.** All ten L2 rungs — `L2-M1`…`L2-M10`, _Conversations_ — are authored against the briefs
of #295 (`docs/26-hi-mr-L2-brief-decisions.md`) and carry `verified: true` on the same standing
authority as L1, backed by `docs/49-llm-review-hi-mr-L2.md`; a strict `npm run build` now emits
`hi-mr: 20 modules (L1-M1..M10, L2-M1..M10)` and the cumulative index runs 222 → 441 surfaces.
The level proves the whole chain on a second rung: the id grammar of #417, the prompt CLI crossing
the level boundary, the M1–M3 enrichment law reading the module number rather than the level, and
`prerequisites` staying inside the level while the seal rule carries the cross-level dependency.
`register: "formal"` (#422) carries the तुम्ही tier the L1 briefs had to smuggle into `usage`.
What L2 teaches: the imperative pair and the -इए tier Marathi does not have (M1), तो/ती/ते and
the genitive (M2), the full agreement grid (M3), the glued -ला and -ने (M4), the hosting and
refusal scripts (M5), the -ऊ या suggestion frame (M6), the spoken continuous बोलतोय (M7),
सापडणे against मिळणे and the -त नाही frame (M8), -पेक्षा and की/किंवा (M9), and the ergative
त्याने/तिने/त्यांनी that L1-M5 fenced off, in four-sentence accounts (M10). **The native gate is
still unmet**: docs/49 ends in open questions 49–70, which now stand beside the L1 chain's own.

**hi-mr reaches three levels (#452, #461, #470, #479, 2026-09-07) — the first L3 anywhere.** All
ten L3 rungs — `L3-M1`…`L3-M10`, _Fluency_ — are authored against the briefs of #452
(`docs/50-hi-mr-L3-brief-decisions.md`, the first level in this repo planned against a verified
level above L1) and carry `verified: true` on the same standing authority, backed by
`docs/51-llm-review-hi-mr-L3.md`. A strict `npm run build` emits
`hi-mr: 30 modules (L1-M1..M10, L2-M1..M10, L3-M1..M10)`, and the cumulative index runs
441 → 633 surfaces. What L3 teaches: the -ऊन converb that lets a day be told at length (M1), the
genitive as a system where L2-M2 taught one frame (M2), मला वाटतं and की (M3), जर … तर with one
counterfactual frame (M4), reported speech on म्हणणे against L2-M10's सांगितलं (M5), the three
feeling-verbs (M6), दुखणे with the body part as its subject (M7), भरणे's three jobs (M8), आहे
against असते (M9), and in M10 nothing new at all — **+1 surface for the whole module**, which is
what "written unaided" is supposed to look like. The passive stays out of L3 by decision; L1-M9's
`बोललो` stays the pinned index miss it has been since docs/15. **The native gate is still unmet**:
docs/51 ends in open questions 71–96.

**The surface pass (#282, 2026-08-24) closed the gap between what hi-mr teaches and what it
shows** — the twin of en-es's #281. Seven surfaces appeared in variation lines and were taught by
no word row; five now resolve (`झोपणार` on M4's झोपतो row, `दुकानाजवळ` on M7's दुकान row, `जाऊ` on
M6's जाणार row, `येऊ` with the plain-future persons on M6's येईन row, `आम्ही` beside `आपण` on
M10's row — the M2 तू/तुम्ही precedent), and two are recorded exemptions that would only resolve by
landing on a row headed by a different word (`पाच`, a sibling number; `बोललो`, a verb L1 never
teaches). M6 and M10 got their honest paradigm answer: three M6 rows now carry shape lists, and
every `[]` left behind is a per-row decision on the record — M6's own rule says -णार never
changes, and M10's re-teach rows leave each paradigm on the first-teach row that owns its index
key. **Additions only**: the hi-mr index grew 206 → **215** surfaces with 0 keys lost and 0 keys
moved. `tools/content-build.test.ts` now sweeps every hi-mr variation line against its own
module's index and pins the three remaining misses (the proper noun `प्रिया` and the two
exemptions), so a new variation that resolves nowhere fails the suite. The reasoning, row by row,
is `docs/15-llm-review-hi-mr-surfaces.md`.

**No fixture course again (#273, 2026-08-24; then #331, #337 and #343, 2026-08-30).** All seven
courses ship — en-fr, en-it and en-ru were each authored behind the gate and graduated the same
way, below — and no module in the repo
is unverified, so `npm run dev` and `npm run build` contain the same modules — the two
relaxations are still enforced and still tested (`tools/content-build.test.ts` builds synthetic
fixture rows and unverified modules and watches them be dropped), they simply have nothing in
this repo to relax. The two most recent courses were each authored behind them, one after the
other. The fourth: **hi-en — Hindi (L1) → English
(L2)** entered as #267's manifest row with `fixture: true`, a 3 × 10 ladder
(`content/hi-en/levels.json`) and a Hindi strings bundle, so until #273 a strict build reported
`hi-en: 0 modules — fixture course, excluded by the gate` and did not emit the course, while a
dev build admitted it (`--with-fixtures`) and shipped whatever was authored. The ten L1 briefs landed with
#269 (`tools/course-briefs.ts`, header section "hi-en: the four decisions a brief must settle" —
Hindi in every teaching field, no `glossEn`, `literal` in English order, contractions as single
index surfaces). **#270 authored L1-M1 and L1-M2** (`content/hi-en/modules/`, 17 + 15 word rows,
`maxSpan` 2 for `I'm` · `I am` / `Good morning` / `thank you`), flipped both rungs to
`hasContent: true`, and reviewed them in `docs/11-llm-review-hi-en-L1-M1-M2.md`. **#271 authored
L1-M3, L1-M4 and L1-M5** (14 + 25 + 15 word rows; the cumulative index now runs 23 → 39 → 56 → 90
→ 108 surfaces, M1–M2's counts having moved by two because M5 extended M1's one `be` row with
`was · were` in M1's own file, as the briefs require), flipped all three, and reviewed them in
`docs/12-llm-review-hi-en-L1-M3-M5.md`. Both reviews are LLM reviews on the owner's authority,
each ending in its open questions for a fluent-English pass; `src/course/hiEnAuthored.test.tsx`
is the dev-build smoke over all five rungs (no browser runs on this host), and
`tools/content-build.test.ts` pins which row every seam key (`be`, `to`, `do`, `the`, `have`,
`in` / `on` / `at`, `get up`, `did`, …) lands on. **#272 authored L1-M6…M10** (Tomorrow, Where things are, Numbers & shopping,
Feelings & opinions, Connected talk — 16 + 17 + 17 + 16 + 13 word rows; the cumulative index now runs
108 → 126 → 148 → 171 → 188 → **202** surfaces, `maxSpan` 3 for `in front of` / `Can I have`), flipped
all five — **all ten L1 rungs are authored** — and reviewed them in
`docs/13-llm-review-hi-en-L1-M6-M10.md`. Whole surfaces: `going to`, `there is` / `there are`,
`next to`, `in front of`, `how much` / `how many`, `Can I have`, `See you`; `because` / `so` one row
each; `it` / `it's`, `where`, `this` (M8), `that` (M9), the joiners `and` / `but` / `also` / `then`;
M10's turns are 2–3 sentences in one `display` (`minWordsPerSentence: 2`, no schema change).
Graduation (#273) followed the en-es/en-ar path — below.

**The spoken-English pass (2026-09-05, `docs/39-llm-review-hi-en-spoken-english.md`)** rewrote 41 of
the 100 heroes to what a native says rather than what a textbook prints: `I'm` from M1-S02 (the
first pass had withheld it until M2 so that `am` could be "the lesson"), `What's` / `Where's` /
`There's` / `She's` / `They're` / `We're` / `That's` / `isn't` as their own rows, M6's plans as
`be + -ing` and `going to` with `will` kept for promises (`I'll call you tomorrow`), `go to bed
late` in place of `sleep late` (which means the opposite in English), `worked from home`, `had
rice`, `on Mondays`, `some tea`, `Do you take sugar?`, `I'm good, thanks`, `I like coffee too`,
`Bye`. The Hindi cues moved to the same register (टीचर, स्टूडेंट, थैंक यू, गुड मॉर्निंग, बाय). The
cumulative index now ends at **259** surfaces; `I'll` lists `I will` beside itself, and `will` has
its own row on M6-S10.

**The same pass ran on the other eight courses the same day**, one auditor and one implementer per
course in parallel, each recorded in its own file: hi-mr (`docs/40`, 17 heroes — the two nonsense
कारण sentences, `मजा आली` for `आनंद झाला`, `गाणी` for `संगीत`, spoken futures in the Hindi cues),
en-es (`docs/41`, 21 — `la India`, `¿Cuánto es?`, a reason that holds in M9), en-ar (`docs/42`, 13 —
`sa-` not `sawfa` in production, `jawʿān`, the `-t` of the numeral construct), en-fr (`docs/43`, 9 —
`je rentre`, `Trois pommes, s'il vous plaît`, `et puis`), en-it (`docs/44`, 14 — `Cosa` for
`Che cosa`, `d'acqua`, `Sabato` without the habitual article), en-ru (`docs/45`, 15 — one `ya` per
sentence, `Mne khleb, pozháluysta`, `A u vas?`), en-de (`docs/46`, 19 — `Ich finde das Buch gut` and
the withdrawn "dass is never optional" rule, `Einen Kaffee, bitte`, `Und Ihnen?`), en-ko (`docs/47`,
37 — the object marker off orders and counters, `jeo-neun` dropped from the default hero, `geunde`
for `hajiman`, `gongbuhada` for a day's study). Every deliberate register decision (tú, vous, Sie,
vy, `-yo`, spoken-simple MSA, hi-mr's spoken neuter) held; what each pass changed, kept and asks the
owner to ratify is in its file. No native reviewer has read any of it.

**en-es ships (#195, 2026-08-13) — the product has two courses.** All ten L1 rungs —
`L1-M1`…`L1-M10` — are authored and carry `verified: true` on the same
LLM-review-plus-owner-authority basis as hi-mr's, so dropping `fixture: true` from the en-es row
in `content/courses.json` was the whole change: a strict `npm run build` now emits
`public/content/en-es/` with levels, strings, ten modules and ten cumulative indexes, and the
emitted `courses.json` lists **hi-mr and en-es**. The course is written **pan-Hispanic**: no
`vosotros`, no region-only vocabulary, both norms named where they differ, and no currency word
picked. Its L2/L3 ladders stay `draft: true` — placeholder lists, nothing authored.

**No native Spanish speaker has read a word of it.** The bar en-es clears is LLM review plus the
owner's authority, exactly hi-mr's, and the **79 open questions** across
`docs/07-llm-review-en-es-L1-M1-M2.md`, `docs/07-llm-review-en-es-L1-M3-M5.md`,
`docs/07-llm-review-en-es-L1-M6-M10.md` and `docs/14-llm-review-en-es-surfaces.md` are what a native
reviewer still owes — dialect first. Graduating the course ships LLM-reviewed Spanish to learners;
it does not close that gap.

**The surface pass (#281, 2026-08-24) closed the gap between what en-es teaches and what it
shows.** Thirteen surfaces appeared in variation lines and were taught by no word row, and two
modules — L1-M5, the past tense, and L1-M10 — shipped `forms: []` on every row. Ten of the thirteen
now resolve (`te gusta`/`le gusta`, `te gustan`/`le gustan`, `quiere`, `española`, `están`, `son`,
`trabajaré`, `hablar`, the `hasta …` goodbyes), three are recorded exemptions that would only
resolve by landing on a row headed by a different word (`profesor`, `buenas tardes`, `hermano`), and
M5's nine verb rows plus M10's three now carry their taught paradigms. **Additions only**: the
en-es index grew 197 → **227** surfaces with 0 keys lost and 0 keys moved — every pre-existing
surface still resolves to the same `{moduleId, sentenceId, wordIdx}`. `tools/content-build.test.ts`
now sweeps every en-es variation line against its own module's index and pins the ten remaining
misses (two proper nouns, four forward references, the four tokens of the three exemptions), so a
new variation that resolves nowhere fails the suite. The reasoning, row by row, is
`docs/14-llm-review-en-es-surfaces.md`.

**en-ar ships (#202, 2026-08-13) — the product has three courses, and one of them is a new
script.** Ten L1 rungs authored against ten briefs (#198–#201), reviewed in `docs/07-llm-review-
en-ar-L1-M1-M2.md`, `docs/09-llm-review-en-ar-L1-M3-M5.md` and
`docs/10-llm-review-en-ar-L1-M6-M10.md`, and shipping on the same LLM-review-plus-owner-authority
bar. **No native Arabic speaker has read a word of it either.** It is **Modern Standard Arabic**,
register pinned to spoken-simple MSA (pause forms, no case endings, no dialect substitutions), and
`scriptMode: romanized`: every sentence prints in ALA-LC-flavoured Latin with the Arabic script
beneath it as recognition only. That quiet line is `dir="rtl"` and `lang="ar"` (#196) and draws in
bundled Noto Naskh Arabic (#197). Its L2/L3 ladders stay `draft: true`.

One honest defect ships with it: the romanization's **ā ī ū ḥ ṣ ḍ ṭ ẓ ʾ ʿ render in the system
face, not Mukta** — Mukta's `unicode-range` stops at U+00FF and it has no glyph past it, so the
marks fall through by design. Mixed-face, not tofu; the options are a face decision
(docs/04-font-notes.md §4.1).

**The surface pass (#283, 2026-08-24) closed the gap between what en-ar teaches and what it
shows** — the third of the family, after en-es's #281 and hi-mr's #282, and the only one with no
paradigm half: no en-ar module ships `forms: []` across the board, so only the gap list moved.
Eleven surfaces appeared in variation lines and were taught by no word row — above all the
**feminine second-person …-īn cluster** every "to a woman" line displays. Eight now resolve, each
on a row of the same word (`tuḥibbīn` on M1's uḥibb, `tadhhabīn` on M4's adhhab, `sa-tadhhabīn` on
M6's sa-adhhab, `tatakallamīn` on M10's atakallam, `masāʾ al-khayr` whole on M2's greeting row,
`sayyāratān` on M8's sayyārāt, `bi-riyāl` and `sa-ashtarī` on their M8 rows), and two are recorded
exemptions: `marḥaban` (a sibling greeting sharing no word with its row — the en-es
`buenas tardes` ruling) and `ṣabāḥ an-nūr`, the reply the **additions-only invariant itself locks
out** — indexing it would hand its hyphen part `an` to M2 and steal M3-S03's own key, so it stays
prose (module rule 5), with bare `ṣabāḥ` a forward reference that resolves from M4 on.
**Additions only**: the en-ar index grew 275 → **283** surfaces with 0 keys lost and 0 keys moved.
`tools/content-build.test.ts` now sweeps every en-ar variation line against its own module's index
and pins the six remaining misses (two proper nouns, the two exemptions' four tokens), so a new
variation that resolves nowhere fails the suite — which is what #287's third-variation pass
inherits, with the four …-īn keys it wants already in the index. The reasoning, row by row, is
`docs/16-llm-review-en-ar-surfaces.md`, and its 8 open questions join the 61 across the three
earlier en-ar reviews.

**hi-en ships (#273, 2026-08-24) — the fourth course, and the first whose L2 is English.** Ten L1 rungs authored against ten briefs (#269 — `tools/course-briefs.ts`,
"hi-en: the four decisions a brief must settle": Hindi in every teaching field, no `glossEn`,
`literal` in English order, contractions as single index surfaces), reviewed in
`docs/11-llm-review-hi-en-L1-M1-M2.md`, `docs/12-llm-review-hi-en-L1-M3-M5.md` and
`docs/13-llm-review-hi-en-L1-M6-M10.md`, and shipping on the same LLM-review-plus-owner-authority
bar as the other three. Dropping `fixture: true` from the hi-en row in `content/courses.json` —
plus the L1 `draftNote` that called the ladder a fixture — was the whole change: a strict
`npm run build` now emits `public/content/hi-en/` with levels, strings, ten modules and ten
cumulative indexes, and the emitted `courses.json` listed **hi-mr, en-es, en-ar and hi-en** (en-it
joined them at #337). No
sentence carries a `glossEn`, by decision rather than omission: #268 made the gloss optional where
`l2Tag` is `en`, because an English gloss of an English hero line would print the line twice. The
chrome is Hindi (`revealLabel` = अंग्रेज़ी दिखाओ) and the Settings switcher offers the pair as
`hindi → english`. Its L2/L3 ladders stay `draft: true` — placeholder lists, nothing authored.

**No native or fluent-English reviewer has read a word of it.** The bar hi-en clears is LLM review
plus the owner's authority, exactly the other three courses', and the **88 open questions** (20 +
30 + 38) across the three review docs are what a fluent-English pass still owes — register and
naturalness first. Graduating the course ships LLM-reviewed English to Hindi speakers; it does not
close that gap.

**en-ru ships (#343, 2026-08-30) — the product has five courses, and the fifth is the first
written in a non-Latin script the app had to bundle a face for.** Ten L1 rungs authored against
ten briefs (#339 — `tools/course-briefs.ts`, "en-ru: the six decisions a brief must settle":
`вы` for the whole of L1, a fixed case plan with the instrumental deferred, perfective-only past,
the zero copula as a delta to celebrate, `ё` and the case endings as index seams), reviewed in
[`docs/28-llm-review-en-ru-L1-M1-M2.md`](docs/28-llm-review-en-ru-L1-M1-M2.md),
[`docs/29-llm-review-en-ru-L1-M3-M5.md`](docs/29-llm-review-en-ru-L1-M3-M5.md) and
[`docs/30-llm-review-en-ru-L1-M6-M10.md`](docs/30-llm-review-en-ru-L1-M6-M10.md), and shipping on
the same LLM-review-plus-owner-authority bar as the other four. 100 sentences, 120 comprehension
pool items, three variations on every sentence and a 215-surface cumulative index, with zero
unresolved tokens.

**It could not ship until the app could draw it.** Mukta bundles no Cyrillic, and en-ru is a
`native` course — the Cyrillic IS the hero line, not a quiet secondary one. #325 bundled the face
(Source Sans 3's `cyrillic` subset, already second in `--font-devanagari`) and mapped `ru` in
`SCRIPT_BY_LANGUAGE_TAG`; this graduation is the moment its cut grows from a near-empty
placeholder over the real repertoire: **source-sans-3 5,484 → 20,280 bytes**. The `unread-script`
payload row — script subsets bundled ahead of the course that reads them — drops from 3 files to
**zero** as those cuts move into `course:en-ru`, which is that row working exactly as designed.

Budget: `course:en-ru` **101.9 KiB** gzip (26 files) against a 360 KiB `COURSE_LIMIT`,
`precache:en-ru` 317.2 KiB, `shell` 215.3 KiB. `course:hi-mr` stays 345.6 KiB — adding a fifth
course moved no other course's row. The chrome is English (`revealLabel` = "Reveal the Russian")
and the Settings switcher offers it to an English reader as **Russian**. Its L2/L3 ladders stay
`draft: true` — placeholder lists, nothing authored.

**No native or fluent-Russian reviewer has read a word of it.** The bar en-ru clears is LLM review
plus the owner's authority, and the **78 open questions** across the three review docs are what a
fluent-Russian pass still owes. Four of them are decisions a native might overturn wholesale — the
`вы`-only register, `Как дела?` inside it, the perfective-only past, and the deferred instrumental
— and the riskiest single line is `Ещё чай, пожалуйста`, which may want the partitive `чаю` that
L1 deliberately does not teach. **Every `sound` line in the course was written from description,
never from listening**, and the intonation claims underpinning M2 are the least safe of them.
Graduating the course ships LLM-reviewed Russian to English speakers; it does not close that gap.

The payload budget holds, because #207 made it per learner: `course:en-es` **71.3 KiB** gzip
against 360 and `course:en-ar` **96.6 KiB** against 360, with `course:hi-mr` **byte-identical**
at 337.9 KiB across both graduations — a Spanish learner is never charged for hi-mr's Devanagari
or for Arabic, and vice versa. en-es's one shared cost was `shell` 210.4 → **214.2 KiB**: Mukta's
`latin` subsets are cut over the union of shipped courses, so Spanish's accented glyphs are in the
bytes every learner downloads. en-ar's shared cost was **negative** — `shell` **214.6 KiB**, down
1.4, because Naskh had been charged to `shell` while en-ar was a fixture and now has an owner
(docs/05-perf-notes.md §4.4, §4.5).

hi-en is the heaviest row in the product, and it holds: `course:hi-en` **347.3 KiB** gzip against
360 (12.7 KiB of headroom), `precache:hi-en` **563.0 KiB** against 590. A Hindi-chrome course is
charged the Mukta Devanagari subset exactly as hi-mr is (`SCRIPT_BY_LANGUAGE_TAG`: `hi` →
`devanagari`) — ≈ 85 KiB of JSON plus ≈ 261 KiB of face — and its Hindi teaching prose, three
UTF-8 bytes a character, makes its JSON ≈ 8 KiB heavier than hi-mr's. hi-en's shared cost lands
on hi-mr, not on `shell`: `tools/font-subset.ts` cuts the Devanagari faces over the union of
shipped courses, so hi-en's repertoire grew the subset both Hindi courses download —
`course:hi-mr` 336.3 → **338.7 KiB** (+2.4, its first move across three graduations), `shell`
214.5 → 214.6, `course:en-es` and `course:en-ar` unchanged (docs/05-perf-notes.md §4.6).

**en-it — English (L1) → Italian (L2)** was the fifth, and it followed the same path one issue
later: #332's manifest row with `fixture: true`, the ratified 3 × 10 ladder copied from en-es and
an English strings bundle differing from en-es's in one word (`revealLabel` = "Reveal the
Italian"), with no `modules/` folder at all — a state both halves of the pipeline already
tolerated (`tools/validate.ts` skips a course directory with no `modules/`; `content-build.ts`
reports `en-it: 0 modules — nothing authored yet`). The ten L1 briefs landed with #333
(`tools/course-briefs.ts`, header section "en-it: the five decisions a brief must settle" — the
`tu` / `Lei` register decision, the elision apostrophe as an index seam, accents as letters,
multi-token surfaces, homograph owners). **#334 authored L1-M1 and L1-M2** (21 + 14 word rows,
`maxSpan` 2 for `mi chiamo` / `mi piace` / `mi piacciono`), **#335 L1-M3…M5** (15 + 15 + 13),
**#336 L1-M6…M10** (13 + 17 + 13 + 11 + 12); the cumulative index runs 37 → 55 → 76 → 105 → 128 →
161 → 185 → 207 → 223 → **245** surfaces, `maxSpan` 3 for `un po' di`, `un chilo di` and
`a che ora`. Every sentence carries three variations and every module twelve pool items, authored
in from the first rung rather than retrofitted (#288, #292). `src/course/enItAuthored.test.tsx` is
the dev-build smoke over all ten rungs — no browser runs on this host — and
`src/course/types.test.ts` walks every en-it display the way the resolver does, so an apostrophe
surface with no word row behind it fails the suite by name.

**en-it ships (#337, 2026-08-30) — the product has five courses.** Ten L1 rungs authored against
ten briefs, reviewed in `docs/28-llm-review-en-it-L1-M1-M2.md`,
`docs/29-llm-review-en-it-L1-M3-M5.md` and `docs/30-llm-review-en-it-L1-M6-M10.md`, and shipping on
the same LLM-review-plus-owner-authority bar as the other four. Dropping `fixture: true` from the
en-it row in `content/courses.json` — plus the L1 `draftNote` that called the ladder a fixture —
was the whole change: a strict `npm run build` now emits `public/content/en-it/` with levels,
strings, ten modules and ten cumulative indexes, and the emitted `courses.json` lists **hi-mr,
en-es, en-ar, hi-en and en-it**. The chrome is English (`revealLabel` = "Reveal the Italian") and
the Settings switcher offers the pair as `english → italian`. Its L2/L3 ladders stay `draft: true`
— placeholder lists, nothing authored. The course-wide register decision ships with it: **the
whole of L1 speaks `tu`**, `Lei` is written in no display string, and politeness is carried by
`vorrei` and `per favore` instead (the reasoning is in the briefs' header).

**No native or fluent-Italian reviewer has read a word of it.** The bar en-it clears is LLM review
plus the owner's authority, exactly the other four courses' — and the **66 open questions** (16 +
20 + 30) across the three review docs are what a fluent-Italian pass still owes — naturalness and
the `tu`-only decision first, then the pronunciation glosses, none of which their author can hear.
Graduating the course ships LLM-reviewed Italian to English speakers; it does not close that gap.

Its payload is the lightest of the five and it holds: `course:en-it` **74.3 KiB** gzip against 360
(285.7 KiB of headroom), `precache:en-it` **289.7 KiB** against 590 — Italian is Latin, and neither
`en` nor `it` maps to a course face in `SCRIPT_BY_LANGUAGE_TAG`, so the course is charged content
only, exactly as en-es is. Every other course row is **byte-identical** across the graduation
(`course:hi-mr` 345.6, `course:en-es` 76.6, `course:en-ar` 115.7, `course:hi-en` 353.3). The one
shared cost is `shell` 214.8 → **215.4 KiB** (+0.6): Mukta's `latin` subsets are cut over the union
of shipped courses, so Italian's accented glyphs — `è à ì ò ù é` — are now in the bytes every
learner downloads. `COURSE_LIMIT` was not touched.

**en-fr ships (#331, 2026-08-30) — the product has five courses, and the fifth is the first
authored to the retrofitted standards from its first rung.** Ten L1 rungs authored against ten
briefs (#327 — `tools/course-briefs.ts`, "en-fr: decisions a brief must settle": the `vous`
register taken course-wide, elision as an index seam, accents as letters, multi-token surfaces,
intonation questions, and an owner for every homograph), reviewed in
`docs/28-llm-review-en-fr-L1-M1-M2.md`, `docs/29-llm-review-en-fr-L1-M3-M5.md` and
`docs/30-llm-review-en-fr-L1-M6-M10.md`, and shipping on the same LLM-review-plus-owner-authority
bar as the other four. Dropping `fixture: true` from the en-fr row in `content/courses.json` —
plus the L1 `draftNote` that called the ladder a fixture — was the whole change: a strict
`npm run build` now emits `public/content/en-fr/` with levels, strings, ten modules and ten
cumulative indexes (171 surfaces through L1-M10, `maxSpan` 4), and the emitted `courses.json`
lists **hi-mr, en-es, en-ar, hi-en and en-fr**. Every sentence carried a `glossEn` until #405
took the gloss off every English-L1 course (see below). The chrome is English (`revealLabel` =
"Reveal the French") and the Settings switcher offers the pair as `english → french`. Its L2/L3
ladders stay `draft: true` — placeholder lists, nothing authored.

**en-de ships (#365, 2026-08-30) — the product has eight courses, and the catalogue is fully
graduated: no row carries `fixture: true` any more.** Ten L1 rungs authored against ten briefs
(#361 — `tools/course-briefs.ts`, "en-de: decisions a brief must settle"), across three parallel
authoring issues (#362 L1-M1–M2, #363 L1-M3–M5, #364 L1-M6–M10) and reviewed in
[`docs/31-llm-review-en-de-L1-M1-M2.md`](docs/31-llm-review-en-de-L1-M1-M2.md),
[`docs/29-llm-review-en-de-L1-M3-M5.md`](docs/29-llm-review-en-de-L1-M3-M5.md) and
[`docs/33-llm-review-en-de-L1-M6-M10.md`](docs/33-llm-review-en-de-L1-M6-M10.md), on the same
LLM-review-plus-owner-authority bar as the other seven. Dropping `fixture: true` from the en-de row
in `content/courses.json` — plus the L1 `draftNote` that called the ladder a fixture — was the
whole change: a strict `npm run build` now emits `public/content/en-de/` with levels, strings, ten
modules and ten cumulative indexes, and the emitted `courses.json` lists all eight courses. The
chrome is English (`revealLabel` = "Reveal the German") and the switcher offers the pair as
`english → german`. Its L2/L3 ladders stay `draft: true`.

**German is the first course that had to plan around what the surface folder THROWS AWAY.** Every
earlier course planned around what `src/engine/surface.ts` KEEPS — Spanish accents, Russian `ё`,
the Italian elision apostrophe. Rule 4 lowercases every token, and German capitalises every noun,
so `Sie`/`sie` and `Essen`/`essen` merge into one index key each. That is decision 2 of the brief
and the reason en-de's brief section is the longest of the eight. The consequence is a handful of
DELIBERATE duplicate rows — `nicht`, `dienstag` and `in` — pinned in `src/course/types.test.ts` as
`FORCED_DUPLICATES` with an ownership map asserting one row per surface. `in` is the one worth
naming: L1-M1 teaches it locative (`Ich wohne in Berlin`) and L1-M7 teaches it with motion and the
accusative (`Ich gehe in den Park`), and the word index is first-occurrence-wins, so M1's note has
to name both seats or M7's learners get a note that is false of the sentence in front of them.

**No native or fluent-German reviewer has read a word of it.** The bar en-de clears is LLM review
plus the owner's authority, exactly the other seven courses'.

The payload holds: `course:en-de` **96.9 KiB** gzip against a 360 KiB `COURSE_LIMIT`,
`precache:en-de` **315.3 KiB** against 590. German is Latin on both sides, so `de` maps to no
course face in `SCRIPT_BY_LANGUAGE_TAG` — that table is unchanged by this graduation — and the
course is charged content only. Its shared cost is `shell` 217.4 → **218.4 KiB** (+1.0): the
emitted manifest gained a row, and Mukta's `latin` subsets are cut over the union of shipped
courses, so `ä ö ü ß Ä Ö Ü` are now in the bytes every learner downloads. That coverage was
verified by reading the generated cmaps rather than inferred from `unicode-range` — all seven
glyphs present in `mukta-latin` at 400, 600 and 700. `course:hi-mr` stays **345.9 KiB**, unchanged
by the graduation.

Two standards the older courses had retrofitted onto them are baked into en-fr from L1-M1: **three
variations on every sentence** (#288's bar) and **twelve comprehension items per module** (#292's).
The payload below is therefore honest already — no retrofit growth is coming.

**No native or fluent-French reviewer has read a word of it.** The bar en-fr clears is LLM review
plus the owner's authority, and the **33 open questions** (10 + 11 + 12) across the three review
docs are what a fluent-French pass still owes — naturalness, register and the pronunciation
glosses first, since nobody has heard any of them. Three of those questions are about the register
decision itself: `vous` course-wide means a learner finishes L1 able to buy bread and unable to
speak to a friend.

The payload holds with room to spare: `course:en-fr` **74.6 KiB** gzip against 360,
`precache:en-fr` **291.8 KiB** against 590 — the lightest course in the product after en-es, and
for the same reason. French is Latin on both sides, so `fr` maps to no course face in
`SCRIPT_BY_LANGUAGE_TAG` and the course is charged content only. Its shared cost is `shell`
214.8 → **217.2 KiB** (+2.4): the emitted manifest gained a row, and Mukta's `latin` subsets are
cut over the union of shipped courses, so French's accented glyphs are in the bytes every learner
downloads. `course:hi-mr` **345.6 KiB**, `course:en-es` **76.6 KiB**, `course:en-ar`
**115.7 KiB** and `course:hi-en` **353.3 KiB** are all unchanged by the graduation.

The two relaxations are independent (`--with-unverified`, `--with-fixtures`), and either
one makes the output a **dev build**, which says so twice over: the run prints
`CONTENT ⚠ DEV BUILD — includes … content; NOT shippable` as its first and last line, and
the emitted `public/content/courses.json` carries `"devBuild": true` plus a `devBuildNote`.
A strict build has neither key, so an artefact can never quietly pass for a learner build —
check `devBuild` before you trust a bundle.

`public/content/` is generated and gitignored: clean-recreated on every run, module files
copied verbatim, `levels.json` re-emitted with `hasContent` **derived from what actually
shipped** (the authored flag is never trusted), and `courses.json` filtered to courses that
shipped at least one module.

**en-ko ships (#380, 2026-08-30) — the product has nine courses, and this is the first one that
was BORN conforming to the no-reading rule.** English (L1) → Korean (L2). Ten L1 rungs authored
against ten briefs (#376 — `tools/course-briefs.ts`, "en-ko: the decisions a brief must settle"),
across three authoring issues (#377 L1-M1–M2, #378 L1-M3–M5, #379 L1-M6–M10) and reviewed in
[`docs/35-llm-review-en-ko-L1-M1-M2.md`](docs/35-llm-review-en-ko-L1-M1-M2.md),
[`docs/36-llm-review-en-ko-L1-M3-M5.md`](docs/36-llm-review-en-ko-L1-M3-M5.md) and
[`docs/37-llm-review-en-ko-L1-M6-M10.md`](docs/37-llm-review-en-ko-L1-M6-M10.md), on the same
LLM-review-plus-owner-authority bar as the other eight. Dropping `fixture: true` from the en-ko
row and the L1 `draftNote` was the whole change: a strict `npm run build` emits
`public/content/en-ko/` with levels, strings, ten modules and ten cumulative indexes, and the
emitted `courses.json` lists all nine courses. The chrome is English (`revealLabel` = "Reveal the
Korean") and the switcher offers the pair as `english → korean`. Its L2/L3 ladders stay
`draft: true`.

**Hangul never reaches a learner-facing surface, and it never had to be taken back out.**
`docs/design-contract.md`'s "rung teaches speech, not script" (#353) ends with a forward rule — a
new non-Latin course is romanized from its first commit, never retrofitted — and en-ru is what the
rule was written against: it shipped `scriptMode: "native"` and cost six issues (#353–#360) and
959 Cyrillic `display` strings to undo. en-ko settled its romanization BEFORE its manifest row
existed ([`docs/34-en-ko-romanization-decisions.md`](docs/34-en-ko-romanization-decisions.md),
#373), so the row's `romanizationNote` was true the moment it landed. `checkScriptMode` reports
**zero errors across all ten modules**; `src/course/types.test.ts` extends that to what the build
cannot see, failing on Hangul inside an English `note`, `rule` or `sound` line. The scheme is
Revised Romanization, transcribing pronunciation, with one named deviation: a particle or the
copula is joined to its host by a hyphen and the host keeps its isolation shape — `chaek-eul`,
`jeo-neun`, `haksaeng-ieyo` — so `surfaceIndexKeys` gives the bare noun an index key of its own.
Without it, an agglutinative language would have left `chaek` ("book") with no row a learner could
ever tap.

**The honest defect, found before authoring rather than after (#375): the quiet Hangul `script`
line renders from a system font.** `@fontsource/noto-sans-kr` splits Korean across ~120 numbered
range files per weight and `tools/font-subset.ts` is built on one source file per target, so
bundling a Hangul cut is a pipeline change and not a target addition. It was not made. Measured on
the shipped build: the course's `script` fields carry **126 distinct Hangul syllables** and
**0 of 126** appear in any generated cut, so `--font-script-fallback` falls through to `system-ui`.
On a phone that is a real Korean face; on a stripped Linux it is tofu. This is the same shape of
defect en-ar has carried since #202, with the difference that it was measured and recorded before
the first module was written.

Budget, reported and not gated — `COURSE_LIMIT` has not existed in `tools/payload-budget.ts` since
#304, and `npm run budget` fails only on attribution (`unmetered` must hold zero files) and the
precache audit. Three older paragraphs above still quote it; they are the record of what was
believed then. `course:en-ko` **103.9 KiB** gzip (29 files), `precache:en-ko` **322.8 KiB** (48
files). `course:hi-mr` stays **345.9 KiB** — adding a ninth course moved no other course's row.
The shared cost is `shell` 217.4 → **218.9 KiB** (+1.5), which is the emitted manifest gaining a
row and that row's `romanizationNote`. `SCRIPT_BY_LANGUAGE_TAG` is **unchanged**: unlike `ar` and
`ru`, whose romanizations are charged a `latin-ext` cut for their diacritics, this one is pure
ASCII and is charged nothing. Verified by reading the generated cmaps rather than inferring from
`unicode-range`: every ASCII character the course's `display` strings use, the particle hyphen
included, is present in `mukta-latin` at 400, 600 and 700.

**No native or fluent-Korean reviewer has read a word of it.** The bar en-ko clears is LLM review
plus the owner's authority, exactly the other eight courses'. The **20 open questions** (6 + 7 + 7)
across the three review docs are what a fluent-Korean pass still owes — naturalness of the
comprehension turns first, then the speech-level judgements, then the pronunciation lines, since
nobody has heard any of them.

**Five levels per course (2026-09-07, `docs/48-five-level-ladder-plan.md`).** Every course's
`levels.json` now lists L4 "Nuance — say it the way they do" and L5 "Voice — your own words, at
length" under L1–L3, ten rungs each, `draft: true` and `hasContent: false` — proposed lists awaiting
the ratification #112 gave L2/L3, and nothing above L1 is authored anywhere. The id grammar was the
only thing in the way: `content/schema/module.schema.json`'s three id patterns, `parseModuleId` in
`tools/validate.ts` and `tools/content-build.ts`, and `priorModuleId` in `tools/generate-prompt.ts`
all said `L[1-3]`, and the last of those returned `null` for `L4-M1` — an L4 prompt would have
rendered as a course's first module, with no allowed vocabulary. All four say `L[1-5]` now, and
`tools/module-ids.test.ts` pins the grammar at both ends on a real module re-numbered. Nothing in
`src/` needed a change: the engine, the strip, the store and the export format read the list, and
`src/course/types.test.ts` now pins every ladder at five levels of ten. The strip was measured at
five cells before the lists landed — 72 px a cell at 360 px, the sealed label flush to its edge
(`docs/images/ladder-five-levels-360.png`). The stale "Dev fixture course" wording on six courses'
L2/L3 `draftNote`s went in the same edit; those courses graduated on 2026-08-30.

### The word index — and the rule it enforces

Every shipped module also gets `public/content/<courseId>/index/<moduleId>.json`: each L2
surface form (a word's `display` plus every entry of its `forms` — romanized for romanized
courses, never the `script` line) mapped to the word entry that **teaches** it,
`{moduleId, sentenceId, wordIdx}`. It is **cumulative in the shape the app reads** — L1-M2's
index is L1-M1's plus what M2 adds, because a module never re-teaches what an earlier one taught
— and **first occurrence wins**, so the pointer names where the learner met the word. The run
notes each one: `index L1-M2: 47 surfaces`. This is what the "why" resolver reads (PRD §6.3).

**The emitted file is a delta (#424, 2026-09-07).** Cumulative *files* are quadratic in the
ladder: hi-mr's thirty modules were 1.2 MB raw, and nine courses at fifty modules would each have
shipped ~2.9 MB, every byte of it warmed for offline. Each file now carries only the surfaces its
own module is the first to teach, marked `delta: true`, alongside the ladder it sits in
(`cumulativeThrough`) and the folded totals; `loadIndex` fetches that ladder's deltas and folds
them earliest-first, which is what preserves first-occurrence-wins. Everything above `content.ts`
— the resolver, the why panel, the tests — sees the cumulative shape and always has.
hi-mr's index set went **1.2 MB → 79 KB raw** (`course:hi-mr` 542.0 → 468.5 KiB gzip); the other
eight sit at 20–31 KB. `tools/delta-index.test.ts` pins the equality that makes this safe: for
every module of every course, fold(deltas) is the cumulative index key for key and entry for
entry.

Two consequences worth knowing before you author content:

- **A comprehension-pool item may only use taught words.** Every whitespace-split token of
  every pool item must resolve in that module's cumulative index, or the build fails naming
  the course, module, item id and token. Sentences' own `variations` and `mistake` lines do not
  fail a build — a mistake is wrong L2 *by design*, and a variation may carry a proper noun (#61)
  — but they are **reported** since #491 (`shown but untaught: 7 surfaces — …`) and ratcheted by
  `tools/shown-surfaces.test.ts`, so the count can fall and never rise. The standing list, and
  what a sweep of it would decide, is `docs/52-shown-surface-findings.md`.
- **`normalizeSurface` is the one definition of "same word"** — `src/engine/surface.ts`, NFC
  + edge punctuation stripped (`आहात?` → `आहात`), case and apostrophes untouched (#116). The
  emitter imports it, and so does the runtime resolver (`src/engine/wordIndex.ts`, #94). Never
  copy it: a second copy is a word that silently has no "why".

### The strings contract — 70 keys, no fallback copy

Every course ships one `strings.json` carrying **all** the microcopy the shell renders, because
the shell has none of its own (PRD §4). So the build validates it against the canonical key list
in `src/course/stringsKeys.ts` — the only list in the repo, which the app's `Strings` type derives
from — and a bundle that fails takes the whole build down with it (PRD §6.5): a missing key is a
blank screen for the learner, not an English word.

The list lives in the **course layer** and the build imports it, not the other way round: the
runtime is the side that must not break, and a `tools/` module the app bundle imports is how a
second copy of the list gets born. `src/course/stringsKeys.test.ts` fails if either table is ever
declared twice.

`tools/strings-check.ts` runs per course, flattens the nested file onto dot-paths
(`ritual.check.copy`), and reports four things, always naming course **and** key:

- **missing key** — the 70 canonical paths must all be there;
- **empty or non-string value** — a present-but-blank key is a missing key with extra steps;
- **unknown key** — the typo tripwire; `ritual.check.plate` would otherwise sit quietly beside a
  missing `plateLabel`;
- **placeholder mismatch** — a value carries exactly its canonical `{placeholders}`
  (`{sentenceCount} {maxWords} {ordinal} {n} {nextModule} {to} {from} {level} {remaining}
  {total} {count} {phase}`), so a translation cannot
  drop `{ordinal}` or invent `{name}`.

Adding a key is one edit to `src/course/stringsKeys.ts` plus a line in each of the three bundles —
in that order, because the build will tell you exactly which course you forgot. The list grew that
way nine times: five keys the frozen screens forced (PR #120), three the Ladder forced (#86 —
`ladder.pendingLine`, `ladder.ownership`, `ladder.sealedToast`; only the last still exists), seven the staged rung card forced
(#87 — `rungCard.startModule`, `.freshNote`, `.practice`, `.revisitModule`, `.exitRitual`,
`.module`, `.practiceEarlier`: a label for every control across the four [D22] stages), three
the module list forced (#88 — `module.helper`, `module.openFull`, `module.trapNote`), four
Sentence Detail forced (#89 — `sentence.trapHead`, `.pocketIt`, `.prev`, `.next`: the trap
callout's heading, the mnemonic's label and the two pager buttons), four the reveal card forced
(#93 — `mark.gotIt`, `.missed`, `.prompt`, `.next`: the two self-mark segments [D11], the question
above them and the Next that does not exist until one is chosen) and two the "why" panel forced
(#94 — `why.show`, `.hide`: the toggle's two labels, because it names what it will do) and seven
the session forced (#96, cut to that count by #388/#389 — `practice.*`: the hub's title, the count
of cards the next tap serves and the one Start label, and the summary's title, its one score line,
its way on to the ritual and its way back) and two lossless resume forced (#99 — `practice.resumeContinue`,
`.resumeNew`: the two ways out of an open session) and two the
press-and-hold forced (#101 — `ritual.confirm.done`, `.toComprehension`: what the control says
once it is signed, and the way on to part 2 — the prototype writes both in English for every
course, which is the shell owning a learner-facing sentence) and five the Verdict forced
(#103 — `verdict.checkSentence`, `.checkChecked`, `.checkComprehension`, `.honesty`, `.toLadder`:
the three checklist lines the ritual ends on, the honesty line under them, and the CTA that climbs
back to the ladder). All fifty-six are
**draft values pending the Sync-3 freeze** (#71). The alternative each time was a
learner-facing line hardcoded in the shell, which is the one thing this list exists to prevent.

`why.openFull` is deliberately **not** `module.openFull`: one opens a sentence from a browsing
list, the other leaves a running session for it. A course may well word them the same; sharing the
key would mean it could never word them differently — the call #93 made for `mark.next` against
`sentence.next`, and #97 for `read.prev`/`read.next` against Sentence Detail's pager.

### The course layer — what boots first

The app knows a manifest, not a language pair (PRD-engineering §8 F0). Boot order is
**manifest → provider → screens**, and no screen mounts until there is an active course:

- `src/course/manifest.ts` — `loadCourses()` fetches `${BASE_URL}content/courses.json` once
  (the cache is the promise, so concurrent callers share one request) and parses the **emitted
  envelope**: `{courses: [...]}`, plus `devBuild: true` on a relaxed build. The authored
  `content/courses.json` keeps the PRD §4 bare-array shape — only the build output is wrapped,
  and `src/` never reads the authored tree. Anything wrong — offline, 404, not JSON, wrong
  shape, **no courses** — throws a `ManifestError`, which is the tripwire, not an edge case: a
  strict build ships zero courses today, so `npm run build` really does render the
  content-error screen.
- `src/course/CourseProvider.tsx` — resolves the active course and exposes
  `{course, courses, devBuild}` through `useCourse()`. It owns the loading and error screens
  (`BootScreens.tsx`), so everything below it already has a course.
- `src/course/strings.ts` — `loadStrings(courseId)` fetches that course's bundle (once per
  course; the cache is the promise again), reads the canonical dot-paths out of the nested file
  and hands screens `useStrings()`. Access is **non-optional** — `strings['retry.title']` is a
  `string` — because the build refuses to ship an incomplete bundle, so there is no fallback copy
  to write. The provider loads it as part of boot: a screen that has mounted has its words.
  `interpolate(value, {…})` fills `{placeholders}`; a name with no value is left verbatim and
  warned rather than blanked, because a silent gap reads as finished copy.
- `src/course/content.ts` — the rest of the course's files: `loadLevels(courseId)`,
  `loadModule(courseId, moduleId)`, `loadIndex(courseId, moduleId)`, and the hooks
  `useLevels()` / `useModule(id)` / `useIndex(id)` that read them for the active course and
  return `{data, loading, error}`. Same rules as the two loaders above — the cache is the
  promise, keyed by URL (so course scoping is free and a failure is never cached), `BASE_URL`
  read per call — and the same tripwire posture: `schemaVersion: 5`, the expected arrays are
  arrays, and the file's own ids match what was asked for, because a wrong-file-served is
  exactly what a build cannot catch. Everything throws `ContentError {url, reason}`, which the
  screens hand to the same `ContentErrorScreen` the provider uses.
- `src/course/types.ts` — schema v5 as TypeScript: `ModuleContent`, `Levels`, `WordIndex`.
  Derived from `content/schema/module.schema.json` and the four modules that exist, not from a
  sketch — including the enrichment fields (`literal`, `trap`, `sound`, `variations`, `mistake`,
  `usage`, `register`, `mnemonic`), module-level `rules` with `deconstruction.rules` as indices
  into them, `complexity`, `exitTest` and `fixture`. `types.test.ts` reads every authored module
  and ladder off disk and fails naming any key no type declares, so the mirror cannot rot.
- `resolveActiveCourse(courses, persistedId?)` is a **pure function**: the persisted course when
  it is still in the manifest, else the first entry with a `console.warn`. It never writes, so a
  fallback does not erase the stored id (Invariant 8). The id it reads is `state.activeCourse`
  (#82) — the provider subscribes to the store, so `setActiveCourse` re-boots the layer with the
  new course's strings and content, which is what the P4 switch flow (#106) will hang off.

Adding a course stays "a folder plus a manifest row": nothing in the shell names a course id.

### Shell purity — the guard that keeps that true

`src/shellPurity.test.ts` scans every shipped file under `src/` for a course's script — Devanagari
(hi-mr) or Arabic (en-ar) — and fails naming file and line. Copy that got hardcoded is copy no
course can translate, so the rule is mechanical rather than a review habit, and it counts comments
too: a doc comment is where a pasted string waits before it becomes code. Script examples belong
in tests, which the scan skips along with `src/test/` fixtures.

English shell furniture (the boot error copy, later a Settings header) stays permitted — the guard
is about course scripts, not about English. The exemption list in that file is **empty**; the one
entry anyone anticipates is the `/dev/type` font page (#85), and adding it will be a conscious
line in that ticket's diff.

### The silence guard — the app plays nothing and records nothing

`src/silence.test.ts` is the same shape of scan for invariant **[D1]** ("the app plays no audio,
records nothing", PRD-engineering §1): no shipped file under `src/` may name a sound API —
playback (`Audio` and its contexts, `<audio>`, `<video>`), synthesis (`speechSynthesis`,
`SpeechSynthesisUtterance`) or capture (`MediaRecorder`, `getUserMedia`) — and a violation fails
naming file, line and API.

It landed with the **Read phase** (#97, retired by #388) because that phase was where the
temptation landed: it asked the learner to say the sentence out loud, and the obvious "help" is a
play button — a synthesised Marathi voice, or a recorder to compare yourself against. The
temptation did not retire with the phase; every practice card still asks for the learner's own
voice. Both are the app saying the line *for*
the learner (Invariant 3), and neither could be right offline for a pronunciation nobody has
signed off. Comments count, as in #80 and #82, and the exemption list is **empty and stays empty**:
there is no file that gets to make a sound. Its own tests plant one violation per API, so a
pattern that stops matching cannot pass as a clean tree.

### The state layer — one document, keyed by course

`src/state/` is zustand + persist over a single `localStorage` document, `rung:state`, whose shape
is PRD-engineering §8 F8 **verbatim**: `{stateVersion: 12, activeCourse, courses: {<courseId>:
{modules, production, reviewQueue, sessionCount, studied, session}}, settings}`. Everything a
learner earns hangs under `courses[<courseId>]`, which is what makes **course switching never
destroy progress** (Invariant 8): a switch moves a pointer, and a course whose content is missing
from a build keeps its subtree, its ladder and its stored id until the folder comes back.

Two things are not in the shape and never will be: **anything the learner wrote** (Invariant 4 —
the v2 state had an `attempts` array; v6 has nothing of the kind) and **any calendar**. The one
date in the whole document is `passedAt` on a passed module.

- `src/state/types.ts` — the shape, plus `STATE_VERSION`. Nothing else declares it.
- `src/state/clock.ts` — `Clock = () => string` and `systemClock`, **the only place in the app
  that constructs a date**. Actions that need a stamp take a `Clock` and default to it, so the
  engine stays pure and testable without fake timers. `clock.test.ts` scans every shipped file
  under `src/` and fails naming the file and line that reached for the wall clock — the same
  mechanical guard as shell purity, for the same reason.
- `src/state/store.ts` — `useAppStore`, persisted with `version: 6` and a wired `migrate` stub
  (its doc comment is the contract for the real v5 → v6 wrap, which ships with export/import in
  P4). It stays **thin, and free of rules**: `ensureCourse` (idempotent — an existing course
  returns the same object, so no write can blank a ladder), `setActiveCourse` (a bare pointer swap;
  the learner-facing switch flow with its toast is #106), `setSetting`, `setLadder` /`markStudied` /
  `passRitual` (progression, below — every rule they obey is derived in the engine),
  `recordProduction` (the counters, below), the session's three (`startSession`, `recordReview`,
  `setSession` — below), and `_reset()` for dev and tests. `completeRitual` (#103) adds none of its
  own: it calls `passRitual` and rides its single write.

`store.test.ts` pins the initial shape against the literal the PRD prints, so drift is a red test
rather than a discovery; the rest of it proves per-course isolation, a round trip through storage,
and that a v5 payload reaches `migrate`.

### The progression engine — every ladder truth, derived

`src/engine/progression.ts` (pure TypeScript: no React, no storage, no clock) answers the four
questions the Ladder asks, and stores none of the answers — a stored level status is a second source
of truth waiting to disagree with the modules it summarises (PRD-engineering §8 F1: "level status
derived, never stored"):

| | |
|---|---|
| `deriveStatuses(input)` | every module by status — `locked` · `unlocked` · `in_progress` · `exit_available` · `passed` |
| `levelSealed(input, level)` | the **seal rule** (PRD-design §5): a level unlocks only when *every* module of the previous level is passed |
| `currentRungId(input)` | the first non-passed rung of the first unsealed, incomplete level — `null` on a finished ladder |
| `rungStage(input, id)` | the staged rung card [D22]: `!hasContent` → `pending`, `!studied` → `fresh`, `exitAvailable` → `exit_ready`, else `studied` |

`ladderFromLevels(levels)` turns a course's `levels.json` into the engine's ladder; the two live
facts arrive as **injected predicates** — `studied(id)` (the per-course flag) and `exitAvailable(id)`
(every sentence produced ≥ 2×, below). `progressionInput(state, courseId)` in the store assembles one
from what a course actually holds, and the screens derive from the same input the store guards with.

Sealing counts a rung whose module has not been authored yet — hi-mr ships 2 of L1's 10 today, so L2
stays sealed until the other 8 exist and are passed. That is the rule working: there is nothing to
climb through a rung with no module.

**One unlock path (Invariant 1).** `passRitual(courseId, moduleId, clock?)` is the only action in the
app that writes `modules`. It throws unless the module *is* that course's current rung — a rung
further up, a module already passed, a sealed level, or a course whose ladder the store has not been
handed all refuse and write nothing — and it stamps `passedAt` from the injected `Clock`.
`markStudied` marks, and cannot unlock: reading every module in the ladder leaves every status
exactly where it was.

`src/state/unlockPath.test.ts` is that promise's mechanical half, in three parts: it slices every
action out of `store.ts` **by name** and fails if more than one contains a write to `modules`; it
*calls* every action against a course with a passed rung and fails if any but `passRitual` changes
the map (the call table is asserted to cover the store's whole action surface, so a new action
cannot skip the check by being new); and it scans every shipped file for a `setState` call, because
an action list is not a gate if a screen can write past it.

### The production counters — the one number that opens the exit ritual

`exit_available` is a single line of the PRD — "all sentences self-marked got-it ≥ 2×"
(PRD-engineering §8 F1) — and it is the thing standing between the learner and the rung's exit
ritual. Three pieces carry it (#95), on purpose: the rule is pure, the write is one action, and the
join between them is a hook, because the answer needs a fact from each side of the app.

| | |
|---|---|
| `src/engine/exit.ts` | pure — `exitAvailable(sentenceIds, production)` (every id ≥ `MARKS_PER_SENTENCE`, which is 1) and `started(sentenceIds, production)` (any id ≥ 1), plus `PRODUCTIONS_PER_SENTENCE`, the `2` the module list's dots and its `n / 20` count read too |
| `recordProduction(courseId, sentenceId)` | the store's counter action: `production[sentenceId] += 1`, and nothing else |
| `src/screens/useExitAvailable.ts` | the join — this course's counters (state) against the current rung's sentence ids (content, loaded through the content layer's cache), handed to `progressionInput` as the real predicate |

**An empty sentence list answers `false`**, never the vacuous "every sentence of nothing". That is
what a caller says while a module file is in flight, or when it will not load at all, and answering
"ready" there would open the exit ritual on a module nobody has read. The same reasoning is why the
hook answers for **one module — the rung it was given**: the engine only ever asks about the current
rung, and a module whose sentences have not been loaded is a module nobody can claim is finished.

**The counters only ever count up.** There is no decrement, no reset, no undo and no ceiling: the
only arithmetic in the action is `+ 1`. A number that can fall is a rung that can close again under
a learner who did nothing wrong — and undo is not missing by oversight, because the mark commits on
Next rather than on the tap ([D11]), which is where a mis-tap is corrected. A count above two is
kept as it is: two is what the ritual asks for, not a cap on practice.

`src/state/productionCounters.test.ts` is that promise's mechanical half, in the same three parts as
`unlockPath.test.ts`: it slices every action out of `store.ts` **by name** and fails if more than one
writes `production`, then reads that one for any arithmetic that could lower a counter (`--`, `-=`,
a subtraction, a reset, a `delete`, even a careful `Math.max(0, …)` floor); it *calls* every action
the store exposes against a seeded counter — twice through, so a refusal is covered too — and fails
if any of them moves it, or moves it down; and it scans every shipped file for a counter write
outside the store. Introduce `Math.max(0, produced - 1)` in the action and thirteen tests go red.

**Routing (PRD-engineering §8 F4): only Produce got-its count.** A Review-phase mark feeds the
Leitner queue (`applyMark` — a box and a countdown) and never these counters; they are different
numbers in different places, because Review measures what is being kept and production measures what
is being built. The distinction belongs to the caller — the self-mark control is deliberately
identical in Review, Produce and Comprehension and cannot see a phase — so the session machine
(#96, below) is the one caller, and it calls `recordProduction` from its Produce branch and
`recordReview` from its Review branch. The Ladder and the module list only read what they write.

### The Leitner scheduler — due in sessions, never in days

`src/engine/leitner.ts` (#92) is the review queue's whole brain: three boxes, intervals **1 → 3 → 7
sessions** (`BOX_INTERVALS`), and no calendar anywhere in it (PRD-engineering §8 F4; Invariant 2).
An item's countdown falls by one when a session *starts* and by nothing in between, so three weeks
away costs the learner nothing — the queue is exactly where they left it.

| | |
|---|---|
| `tickSession(queue)` | one session closer to due for every item, **floored at 0** — a long absence is not a forty-item backlog |
| `dueItems(queue, max = 5)` | what Review serves: `dueInSessions <= 0`, most urgent first, capped |
| `applyMark(queue, id, gotIt)` | got it → up one box (3 is the ceiling), due in that box's interval; missed → **box 1, due 1** |
| `enrol(queue, ids)` | absent ids in at box 1 / due 1; idempotent, so a replayed pass never resets a box |

The order is PRD F4's, "strictly by due-ness then module recency": most overdue first, then the
**newest module first**, then the module's own sentence order. Recency is read **numerically** —
`'L1-M10-S01' < 'L1-M9-S01'` as text, so a raw string sort would file the module the learner just
passed behind the one before it, for the rest of the course. It is a total order over distinct ids,
which is why the same queue serves the same list whichever order it happens to be stored in (50
seeded permutations assert it).

**Enrolment policy: a sentence enters review when its module is PASSED** — production ends,
maintenance begins. Until then the sentences are the current rung's Produce work (the ≥ 2×
counters), and scheduling them for review too would be the same work twice under two names. The
call site is the exit ritual's pass action (`completeRitual`, #103), which enrols in the very write
that marks the module passed; this module states the policy and stays pure — no React, no storage,
no clock, every function returning a new array.

### The app shell — one frame, three headers, one flag

`src/shell/` is the chrome every screen renders inside (#84; PRD-design §4 [D8, D21]), and
`src/screens/` is the eight screens themselves — stubs today, each naming the ticket that builds
it. The IA is the whole route table, and the table is data (`src/shell/routes.tsx`): `App` builds
the `<Routes>` from it and `AppShell` matches the location against it, so a screen the router
knows about and the chrome does not cannot happen.

| | |
|---|---|
| `/` | Ladder (#86) — home, first run, and where an unknown route lands |
| `/module/:id` · `/sentence/:id` · `/ritual` · `/comprehension` · `/verdict` | children of the active rung: **back header** to the Ladder |
| `/practice` · `/settings` | the other two tabs: **brand header** |

**HashRouter, not BrowserRouter.** The product is a static, zero-backend, installable PWA — a
deep link under a history router needs a server rewrite and there is no server to ask.
`#/module/L1-M1` survives a refresh and an offline cold start.

**Immersion is one boolean, and it lives in a context** (`src/shell/immersive.tsx`), never in the
store: `src/state/` is the persisted document whose shape is the export contract (#82), and "a
session is on screen right now" is not something to restore into a build that is showing the
Ladder. Raising it hides the bottom nav **entirely** and puts a `--tap-min` pause ✕ top right —
always, because an immersive screen with no way out is the failure the shell exists to prevent.
The ✕ ends the session and lands on the Practice hub; so does leaving the route, so the Android
back button cannot walk out of a session and leave the nav hidden. What a session *is* — the
phases, the marks and the per-course snapshot — is the session machine (#96, below); resuming into
that snapshot is lossless resume (#99, further below), and the ✕ is one of the ways in.

**Phone-correct layout**, and the two rules that keep it that way: the app column is `100dvh`
(never `100vh` — a mobile URL bar shrinks the viewport and `100vh` does not notice) and never
scrolls; `<main>` is the one scroll area, `overflow-y: auto; overflow-x: hidden;
overscroll-behavior: contain`. Every safe area is written `max(var(--space-N),
env(safe-area-inset-*))` — a phone gets its real inset, and a desktop browser, where every inset
is 0, still gets the design's padding. `src/shell/layout.test.ts` pins both from the CSS source,
because jsdom resolves neither `env()` nor `max()`; the numbers themselves are checked in a
browser at 360px and 430px, which is the ticket's acceptance criterion.

Two rules the scaffold bakes in, before you write a component:

- **Tokens only.** `src/main.tsx` imports `design/tokens.css` *in place* — `design/`
  is read-only and re-copied wholesale, so importing it directly means token updates
  land with zero copy step. Style with `var(--*)`; no hard-coded hex, px or font names
  anywhere in `src/` (`docs/design-contract.md`) — `src/styleContract.test.ts` scans every
  stylesheet the app ships and fails naming the file and line, the same mechanical shape as
  shell purity and the clock guard.
- **One brand constant.** `src/brand.ts` exports `BRAND` — the only place the product
  name lives. Page title, manifest and export filenames all read from it.
- **Content has a contract.** `content/schema/module.schema.json` (JSON Schema draft
  2020-12) is the frozen shape of a module; `tools/validate.ts` adds the checks a schema
  cannot express (filename ↔ id, the 10-sentence / pool ≥ 6 budget and its `fixture: true`
  relaxation, full enrichment for M1–M3, rule-index ranges). Run `npm run content:validate`
  before opening any content PR — one line per file, then `CONTENT <n>/<m> ok`.
- **Content ships through a gate.** `tools/content-build.ts` runs that validator over every
  module and emits `public/content/` — see the gate table above. Never import from `content/`
  in `src/`: the app reads `public/content/` (via `fetch`), which is the only tree the gate
  has approved.

### The Ladder — the home screen, and nothing it renders is stored

`src/screens/LadderScreen.tsx` (#86, remade by #396-#399; PRD-design §5, §7 [D16]) is where the
engine becomes a screen: the position line, a compact strip of level chips, the current rung's
card, and the rungs of the active level under it. Every one of those is **derived on render** —
`deriveStatuses`, `currentRungId`, `levelSealed` off the very `progressionInput` the store guards
`passRitual` with (#83). A count on this screen and a rule in that action cannot disagree, because
they are one derivation.

[ladder-mid-360.png](docs/images/ladder-mid-360.png) — mid-climb at 360px.

**The action comes first, and the position is stated once** (#396, #397). The screen used to open
with "You are learning Spanish." — true on every render forever — then a position line, then three
tall level cells carrying names and taglines for two levels whose modules are not authored, then
"Level 1 · 7 of 10 rungs still to climb", which is the position line inverted. The rung card came
after all of it and after every rung already climbed, so at 360px mid-climb its `Practice` CTA
fell below the fold on a 1.56-screen page. Now the card is the first thing in the body, the strip
is one row of chips, and the same fact is not asked to be read two ways. The list under the card
is still the whole ladder in ladder order; the current rung appears there as a row, because the
card above it IS that rung.

Three things it is responsible for keeping true:

- **A locked rung is not a control.** No link, no button, no `tabindex` — the row is text, a
  hollow marker and a lock at 50% opacity. "The ladder is visible; the rungs are sealed"
  (PRD-design §3.2) is a DOM fact, asserted per rung in `LadderScreen.test.tsx`, not a CSS one:
  `pointer-events: none` would still leave a link for a screen reader to offer.
- **A sealed level answers honestly, in counts.** Only sealed cells are `<button>`s (the active
  cell is the screen you are on; a control with nothing to do is not one), and tapping one raises
  the shared toast (`src/shell/Toast.tsx` — the timer is the control, the region is always mounted
  so a screen reader hears the change, and #106's course-switch toast reuses both) with the sealed
  level and how many rungs below it remain.
- **Counts, never time.** No `%`, no date, no streak, no "due" — asserted over the rendered screen
  in both a fresh and a mid-journey state.
- **The one celebration is a moment, not a state.** A verdict hands the screen a one-shot flag and
  the newly opened rung plays the unlock beat once; the Ladder spends the flag as it lands, so a
  reload has nothing to replay and a revisit never carried one (#103, below).

Loading that ladder and handing it to the store is `src/screens/useProgression.ts`, which the
Ladder and the module list both start with: it fetches `levels.json`, calls `setLadder` from an
effect when it resolves — which is what gives `passRitual` a rung to check against — joins on the
real `exitAvailable` predicate (`useExitAvailable`, above: the current rung's counters against its
sentence ids, so no screen has an injection point to get it wrong with), and returns the assembled
`progressionInput` plus a `ready` flag. Screens draw nothing until that flag is up
(`aria-busy`), because an empty input would render a *finished* ladder. It is a hook rather than
a line in the Ladder because a deep link (`#/module/L1-M1`) reaches a guarded screen with the
Ladder never having mounted.

Two deliberate divergences from the prototype, both recorded in the code that makes them:

- **Course prose is 18px Mukta, not an 11.5px caption.** The prototype renders the rung jobs and
  the toasts in English for every course; in the product they are course copy, and
  design/tokens.md §2 is absolute — all Devanagari is Mukta, never below `--devanagari-min-size`.
  A caption token would set Hindi in Barlow, which draws no Devanagari at all. The ramp has no
  caption-sized Devanagari slot and cannot have one below the floor.
- **The position line is the screen's first row**, not part of the header: the shell's brand header
  is screen-agnostic (#84). #117 reconciles both.

### The staged rung card — one clear action, and never a gate

`src/screens/ladder/RungCard.tsx` (#87; PRD-design §6.2 [D22], PRD §8 F1) is the current rung as a
blueprint object — radius 0, a hairline, `--shadow-sm`, the four `+` registration marks — holding
the kicker, the title at `--text-rung-title`, the job, and **one CTA set, chosen by the stage**:

| `rungStage()` | primary | beside it |
|---|---|---|
| `fresh` | "Start with the module" → `/module/:id` | the note: read it once, Practice picks up from there |
| `studied` | "Practice" → `/practice` | ghost "revisit the module" → `/module/:id` |
| `exit_ready` | "Exit ritual — open" → `/ritual` | Practice and Module drop to secondary |
| `pending` | — (nothing to open) | the `pendingAuthoring` note + ghost "practice earlier rungs" |

The stage is `rungStage(input, id)` off the same `progressionInput` every other number on the
screen derives from — so it moves when the facts do: `markStudied` on first module open flips
`fresh` → `studied` (#88), and the got-it that brings every sentence of the rung to 2× flips
`studied` → `exit_ready` (#95 — read live off the counters, not injected). Nothing about the card
is stored, and it holds no state of its own.

**The stage guides; it never gates** (the invariant, PRD-design §6.2). The bottom nav's Practice
tab is untouched at every stage — asserted per stage in `LadderScreen.test.tsx` — three of the
four stages offer Practice from the card itself, and no stage locks a route. The primary is the
one **filled** object in the whole view (`--cta-height` 48px, solid accent); secondaries are
`--btn-secondary-height`, ghosts `--ghost-height` and always `white-space: nowrap`
(design/tokens.md §3, §4).

Every label is the course's (`strings.json` — the seven `rungCard.*` keys above), so the card
carries no learner-facing English of its own; `ladder/RungCard.test.tsx` renders all four stages
and fails if the prototype's wording reaches the screen. The card's title is deliberately **not**
a link any more: the primary CTA is the way into a rung, and a `pending` rung has no module to
open at all.

Two more divergences from the prototype, on top of the Ladder's:

- **The card's copy and its button labels are Mukta at the 18px floor**, not 11–12px Barlow and
  14px Barlow Condensed. Same reason as the Ladder's prose, one step further: a CTA label is
  course copy too, and hi-mr's is Devanagari. Raised with the rest for #117.
- **The two `exit_ready` secondaries are `--btn-secondary-height` (46px)**, where the prototype
  writes 44 inline; design/tokens.md §4 is the rule of record and both clear `--tap-min`.

### The module list — read the rung, and nothing else

`src/screens/ModuleScreen.tsx` (#88; PRD-design §6.4, PRD §8 F2) is a rung's ten sentences,
browsable and quiet: nothing to answer, nothing to get wrong, no control that judges anything.
Four things it owes, and each is a test:

- **A guard.** `/module/:id` is a real deep link — HashRouter, installable PWA — so any id can
  arrive. A locked rung, an id the ladder does not list, and a rung whose module this build never
  shipped all land back on the Ladder (`replace`, so the bad entry leaves no back-stack trace).
  That is the same answer the rung card gives by having no link to offer.
- **`markStudied`, once, on first open.** The `studied` flag is what flips the rung card behind it
  from "Start with the module" to "Practice" [D22], so *opening this screen* is what moves the
  Ladder. It is idempotent in the store, which is what lets an effect fire it; the test proves the
  call count is 1 across re-renders, and that reading a rung passes nothing (Invariant 1).
- **Rows, each a door into Sentence Detail.** A row is the L2 `display`, its `cue` (+ the quiet
  `script` line in romanized courses), its production dot and a chevron — hairline-separated, not
  framed (#403: ten registration-marks plates in a column were ten things each claiming to be the
  one object on the screen, and the frame plus its padding was most of the list's height). The
  cards used to expand in place; #217 made every card a link instead, so the details live in
  exactly one screen. `module/ProductionDots.tsx` draws each sentence's 6px dot off
  `production[sentenceId]` (0 / 1), and the header's `n / 10` counts the same map — both
  **read-only** here, live off what `recordProduction` writes (#95), so a column of full dots down
  the list is the exit ritual unlocking, one sentence at a time.
  [module-rows-360.png](docs/images/module-rows-360.png) — mid-climb at 360px, 1.41 screens where
  the plates were 1.72.
- **Where the learner was.** The scroll offset survives a detour into Sentence Detail, in
  **`sessionStorage`** (`module/moduleView.ts`, `rung:module-view:<course>:<module>`) and never
  in the store: `src/state/` is the export contract (#82), and where a list was scrolled to is
  this visit's UI, not something the learner earned. The shell publishes its one
  scroll area through `src/shell/scrollArea.tsx` — the screen asks the frame for it rather than
  hunting the DOM for something that scrolls.

Three divergences from the prototype, on top of the Ladder's and the card's:

- **The screen's head row is the kicker, the title and the count**, not a header: the shell owns
  the back chevron and the screen's name (#84), and the prototype's own list is its scroll area
  where here the shell's `<main>` is the app's only one. #117 reconciles both.
- **Course prose is Mukta at the 18px floor** — the helper line, the cue, the literal, the trap
  note, the "open full" label and, third recurrence, **the word chips** (design/tokens.md §6 writes
  9.5–11px). Same wall as #86 and #87: §2 forbids Devanagari below `--devanagari-min-size` and a
  caption token sets it in Barlow, which draws none. Flagged again on #117; no token invented.
- **"Open full" is `--btn-secondary-height` (46px)** where the prototype writes 42 inline, the same
  call PR #139 made for the rung card's pair.

The one place the app overrides a font shorthand's family is the quiet script line, which takes
`--font-script-fallback` (design/tokens.md §2) — so `src/styleContract.test.ts` bans a face by
*name* and allows `font-family: var(--…)`, which is the opposite of one.

### Sentence Detail — two tiers, one order each, and the mnemonic last

`src/screens/SentenceScreen.tsx` (#89, tiered by #401; PRD §8 F3 [D10], PRD-design §6.4, §7) is
one sentence taken apart. Since #414 the screen file holds only the guards, the ladder hand-over
and the composition; each of the ten sections is its own component under `src/screens/sentence/`
(`HeroSection` … `MnemonicSection`), beside the disclosure (`Deeper`), the pager (`SentencePager`)
and the hand-over hook (`useLadderHandOver`). **The order is the feature**, and within each tier
it is frozen:

> always: hero → words → trap · [go deeper] · mnemonic
> deeper: gloss → rules → sound → variations → mistake → usage

The first tier is what a sentence *is* — the line, its words, the one thing that will bite — and
it ends on the one thing worth carrying away, the mnemonic under the course's own "pocket it". The
second is everything else the course has to say, behind one control (`sentence.deeper` /
`sentence.less` — an action, never a question, #390's lesson), in the order it always had. A
learner who opens a second sentence finds the same shape in the same place, which is the whole
point of freezing it; every section carries a `data-section`.

It used to be ten sections in one column — **2.97 screens at 360px for every sentence of every
module**, since every optional block ships on every sentence — and most of the lower half restated
the upper: the gloss says the literal, a word's note says its rule, the trap and the note both warn
off the same mistake. That was the reading path a first-time learner walked ten times a module.
Closed, `L1-M1-S01` is 1.3 screens. The disclosure lives on the detail, which is keyed by id, so
prev/next remounts it shut: depth asked for on sentence 3 was not asked for on sentence 4.

[sentence-closed-360.png](docs/images/sentence-closed-360.png) ·
[sentence-deeper-360.png](docs/images/sentence-deeper-360.png) — closed, and opened, at 360px.

Four more things it owes:

- **A section with nothing in it renders nothing.** No heading, no empty plate, no "not available".
  Enrichment is optional in the schema past M3, so an M4+ module may ship as hero + gloss + words +
  rules and nothing else — and that is a simple sentence, not a broken screen (asserted against a
  sparse fixture). The gloss obeys the same rule since #268, settled by #405: `glossEn` is
  optional in the schema, required by the build where neither language of the pair is English
  (hi-mr — there it is a third language) and forbidden where either is: hi-en's hero already
  reads in English, and on the seven en-* courses the cue is the English reading and `literal`
  the word-for-word one. All 700 en-* glosses came off — 572 repeated the cue or the literal (24
  were literals mislabelled `lit.` and moved into `literal`), and the 128 that carried a note
  tail had the tail moved into a word `note` where the note did not already say it. The gloss
  section draws whatever is present — gloss and literal, literal alone, or nothing — and branches
  on presence, never on a course id (`docs/design-contract.md`).
- **Amber exactly once.** The interference trap is the only loud object on the screen
  (design/tokens.md §7 rule 2); the mistake plate is deliberately **neutral** — `--mistake-border`
  / `--mistake-bg`, struck text — because a common mistake is information about the language, not
  a warning about the learner. The test **reads the stylesheet**: every rule carrying an
  `--interference-*` token must be a `.trap*` selector, and the mistake rules must carry neither
  that nor the self-marks' red.
- **`deconstruction.rules` are indices**, resolved through the module's own ordered `rules` array
  (PRD §7). An index the module has not got renders nothing at all and the rest of the section
  still draws: the build checks the ranges (`tools/validate.ts`), and a learner's screen is not
  where a content bug should surface.
- **Prev/next inside the module, and the back chevron to the module.** The pager is bounded by the
  module's own list (`disabled` at both ends, `--btn-secondary-height`) and navigates with
  `replace`, because paging is one screen rather than ten destinations. Where "back" goes is the
  route table's answer (`shell/routes.tsx` → `backTarget`), not the header's: Sentence Detail is
  the one child of a rung that returns to its **module**, which restores the offset and the open
  cards #88 remembered. Every sentence opens at its own top.

`screens/TagChip.tsx` is the delta-learning tag as a shared component — `free` · `delta` ·
`interference`, one token pair each, and **the name is always a text node**: a chip that said
"interference" only in amber says nothing to a screen reader, to a greyscale screenshot or to
anyone who cannot separate amber from steel. It is the one chip in the app at the design's own
size (`--text-micro`, inside §6's 9.5–11px band) because its label is English furniture and no
Devanagari can land in it. The word rows and the rules both wear it, and so does Practice's "why"
row (`src/components/WhyRow.tsx`, #94).

Divergences from the prototype, on top of the module list's:

- **The whole screen is course prose at the 18px Mukta floor** — the cue, the literal, the word
  cues and notes, the forms, the rules, the trap, the sound note, the variations, the mistake's
  why, the usage, the mnemonic and the two pager labels, where the prototype writes 11.5–14.5px.
  Fourth recurrence of #86's wall, same answer: build to §2's floor, flag it on **#117**, invent no
  token. The hero (`--text-l2-hero`) and the word rows (18px, weight 600) match the prototype
  exactly.
- **The two course-copy labels are not kickers.** `sentence.trapHead` and `sentence.pocketIt` are
  the course's words, and uppercasing + tracking a Devanagari string is not a style the design
  package has — so they render as course prose in `--color-accent-700` where the prototype writes a
  10px condensed kicker. The eight structural section labels (`WORD BY WORD`, `RULES USED` …) stay
  English furniture at `--text-kicker-sm`, in the register of the `M1 · SENTENCE 02` kicker.
- **The pager is sticky, not fixed.** The prototype pins it below its own scroll area; the app has
  exactly one scroll area, so the bar sticks to the bottom of the screen's column — same
  one-handed affordance, one scroll area. The head row (kicker + production dots) is the screen's
  first row for the same reason the module list's is (#84, #117).
- **The position reads `3 / 10`**, not the prototype's "3 of 10": counts, never a sentence the
  shell would have to own an English word for.

### The reveal card — the gate is a hidden Next, not a disabled one

`src/components/RevealCard.tsx` (#93; PRD §8 F4 [D11], PRD-design §6.3, §7) is the interaction the
whole product is b
