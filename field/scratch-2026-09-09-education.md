# Field education hunt — 2026-09-09 scratch (Wednesday)
Window: ~2026-09-08 00:00 UTC → now (prefer pushes 2026-09-08 / 2026-09-09). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): DLangellotti/targum 9, xyzqm/srsly 9, rishabh7g/rung 8. Overflow: mikub97/repetita 8, cehbz/thai-deck-eval 7, Leon2k909/Micheon 7, LearnWithNoura 7 (STEM), DsDG1/turna 6.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) nturl / sotto — Voice-first graded reader + availability-gated tutor — PRIMARY
- who: nturl
- url: https://github.com/nturl/sotto · live https://readsotto.app
- date: created **2026-09-04**; heavy verification / paid-flow / voice-recovery / landing work through **2026-09-08T23:20Z**
- tags: education·i-plus-one·generated-input·tutor-loop·quiet-when-nothing·human-gate·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·i-plus-one·tutor-loop·quiet-when-nothing·generated-input] score=9 | nturl / sotto | Open-source **voice-first graded-reader**: narrated stories, **tap-to-translate**, save→SRS review, plus a **voice tutor about the passage** (explain / quiz / discuss). Reading path works with **every voice model unreachable**; tutor probes `/health` first and surfaces a clear unavailable panel with a **“Read alone”** exit (local / browser-WebGPU / BYOK / cloud paths named) — quiet-when-nothing. Hosted PWA needs no account for reading; self-host `docker compose` or BYOK OpenAI. Honest status: seeded books are **AI-drafted** (`reviewStatus: "draft"`) with no human language review yet; `docs/verification.md` tracks PASS/PARTIAL/FAIL against a 35-row brief after an adversarial review. Distinct from monosai (story gen ceiling) and targum (Hebrew CI bilingual) — **graded narrated reader + tutor-availability gate**. | https://github.com/nturl/sotto
- why distinct: NEW URL this window; portable graded-input + tutor quiet-when-nothing not on yesterday’s roster.
- bank: `2026-09-09-nturl-sotto-voice-first-graded-reader-tap`

### 2) diemonster / janki — Textbook/photo → Anki with named human gates — STRONG
- who: diemonster
- url: https://github.com/diemonster/janki
- date: **2026-09-08** batch extraction + “require complete extraction of every supplied table page” + verified Claude subscriptions + independent vocab decks + rendered card previews (through ~21:50Z); prior Sep 7 reading-hold / kanji / audio LFS
- tags: education·human-gate·teach-once·taste-gate·i-plus-one
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·human-gate·teach-once·taste-gate] score=9 | diemonster / janki | Local workbench: PDF/photo of the Japanese you’re actually studying → named paid model read (file/provider/purpose shown **before** send) → **you check every proposed card** against the page. Portable gates: **reading hold** (blank/contradicted reading waits — no guess); **coverage** (every promised table row accounted for, separate from “is the Japanese good”); **meaning in this lesson** vs dictionary facts; polite/casual as two slots not translations; **one study-deck ownership** (same word in another source adds history, doesn’t duplicate). Repo is SoT; `.apkg` rebuilds update notes. Sep 8 ships complete-table extraction + independent vocab decks + Assistant card previews. Distinct from note-buddy (page-inscribed) and anki-quick-add — **lesson-source human-gate miner**. | https://github.com/diemonster/janki
- why distinct: NEW URL; named reading-hold + coverage + deck-ownership gates, not polish on yesterday’s keeps.
- bank: `2026-09-09-diemonster-janki-textbook-photo-anki-workbench-with`

### 3) BeastMaster75 / NaraNote — Collect-what-you-meet + stroke-order self-check — STRONG
- who: BeastMaster75
- url: https://github.com/BeastMaster75/NaraNote
- date: created **2026-09-03**; **2026-09-08** batch kanji addition + kanji sentence tracking; stroke-order numbering + Anki export + in-app review landed Sep 4
- tags: education·i-plus-one·teach-once·human-gate·generated-input
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·i-plus-one·teach-once·human-gate] score=8 | BeastMaster75 / NaraNote | Companion for the half Anki is bad at: **paste Japanese from anywhere** → tokenize with readings/meanings; save unknowns **with the sentence they came from**. Already-saved words **dim** so any paste quietly shows coverage. Kanji page: components link onward + *your* collection/history. Handwriting: draw from meaning/readings, then reveal with **your strokes numbered in the order you made them** vs correct stroke order (self-marking is how bad habits set in — gate against that). Optional in-app SRS; **Anki export is a door** (re-export updates same cards). Early, single-machine, no accounts. Distinct from srsly handwriting gym (ZH stroke grade) and WaniSieve (batch filter) — **meet→collect with known-dim + stroke-order reveal**. | https://github.com/BeastMaster75/NaraNote
- why distinct: NEW URL; collect+dim+stroke-order-numbering portable loop not on yesterday’s roster.
- bank: `2026-09-09-beastmaster75-naranote-japanese-collect-what-you-meet`

## Scored but NOT in top-3 SETUP slots (overflow)

### mikub97 / repetita — score 9 (overflow / promote-watch; same URL as yesterday)
- url: https://github.com/mikub97/repetita
- date: **2026-09-08** ~17:05–18:02Z — **“I know this”** (declared≠earned; no review-log write), card **retirement** policy actually wired, **offline answers kept** + opaque handles, mount on another app’s path, choice-form client fix (was silently skipping 546/676)
- tags: education·teach-once·killed-claim·human-gate·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9** (was 4/4/8 yesterday — mechanism jump on same URL)
- alert: **no**
- one-liner: declared-knowledge button that refuses to corrupt scheduler evidence + retirement as store policy + offline durability. Same URL → leave **overflow** unless compiler wants engine over sotto/janki/NaraNote learner loops.
- bank: prior CHANGELOG deposit; new `2026-09-09-mikub97-repetita-sep-8-i-know-this` (commit-scoped)

### cehbz / thai-language-anki — score 8 (overflow; generator companions)
- url: https://github.com/cehbz/thai-language-anki
- date: **2026-09-08** — compile one note per adopted sentence (cloze last-used word); draft sentences for coverage; refuse deck without curated frequency corpus; orthographic marks ≠ vocab
- tags: education·taste-gate·human-gate·teach-once·generated-input
- portable / evidence / combined: **4 / 4 / 8** (was 4/3/7 — generation-side commits landed)
- alert: **no**
- one-liner: evaluator fitness function now paired with sentence-compile / coverage-draft companions; still meta quality-gate more than learner loop — overflow.
- bank: prior eval deposit; new `2026-09-09-cehbz-thai-language-anki-sep-8-sentence`

### rh20051 / WaniSieve — score 7
- url: https://github.com/rh20051/WaniSieve
- date: **2026-09-08T19:34Z** “Add files via upload” (first public dump)
- tags: education·i-plus-one·quiet-when-nothing
- portable / evidence / combined: **4 / 3 / 7**
- alert: **no**
- one-liner: Fugashi tokenize Japanese `.txt` → sieve against WaniKani → AnkiConnect. README says “above level”; `main.py` actually sieves against **burned** vocab list — portable ceiling idea, thin single-script evidence. Overflow.
- bank: `2026-09-09-rh20051-wanisieve-fugashi-tokenize-wanikani-burned-sieve`

### s4s4s4s / sat-srs — score 7
- url: https://github.com/s4s4s4s/sat-srs
- date: **2026-09-08** late — Logic section as **one-shot** (no FSRS) + lesson strip + other_senses
- tags: education·teach-once·reveal-schedule·human-gate
- portable / evidence / combined: **4 / 3 / 7**
- one-liner: PWA FSRS-6 SAT cloze cards living in Obsidian vault via GitHub; Sep 8 adds a Logic chapter that is **one-shot explanation, not spaced** — portable teach-once split. L1 exam vocab, not L2 language lane — overflow.

### Leon2k909 / Micheon — score 7 (watch)
- url: https://github.com/Leon2k909/Micheon
- date: continuous **2026-09-08** v1.2.1089–1091 — Russian UI catches up; verb game / own sets speak course language; Russian reader opens every country course
- tags: education·tutor-loop·teach-once
- portable / evidence / combined: **3 / 4 / 7**
- one-liner: offline Electron multi-lang tutor product expansion (RU interface + course-speaking games). Solid product; fewer novel portable gates than sotto/janki.

### TahaKhanM / LearnWithNoura — score 7 (off-lane)
- url: https://github.com/TahaKhanM/LearnWithNoura
- date: **2026-09-08** session-evidence verify + lesson-runtime docs; auth/lifecycle harden
- tags: education·tutor-loop·reveal-schedule·human-gate
- one-liner: voice tutor + deterministic board; **STEM/kid whiteboard**, not language — overflow only if cross-domain.

### AGI-is-going-to-arrive / ahadiff — score 7 (off-lane note)
- url: https://github.com/AGI-is-going-to-arrive/ahadiff
- date: **2026-09-08** v1.4.0 — snapshot/document learning + **active transfer practice**
- tags: education·tutor-loop·teach-once·reveal-schedule
- one-liner: learn-from-diff/doc with quiz-before-reveal + FSRS review. Strong teach-once, but **code/diff learning**, not language/Anki lane — overflow only.

### DerDemystifier / SmarterTypeField — score 6
- url: https://github.com/DerDemystifier/SmarterTypeField
- date: **2026-09-08–09** multi-type-field support + ADR retain script tag
- one-liner: Anki `{{type:}}` ignore case/accents/punct — useful typed-recall tolerance; small addon, not a full SETUP.

### DsDG1 / turna — score 6
- url: https://github.com/DsDG1/turna
- date: **2026-09-08** reveal-animation polish + test bugs
- one-liner: Turkish Flutter + embedded Anki Rust kernel; thin new gate this window.

### freesurf-ecosystem / language-tutor — score 6
- url: https://github.com/freesurf-ecosystem/language-tutor
- date: **2026-09-08** Together AI / self-host STT+LLM+TTS English tutor pipeline
- one-liner: voice tutor product scaffold; no named language learning gate diary beyond ASR→correct→TTS.

## BOUNCE list (url | why)
- https://github.com/DLangellotti/targum | yesterday KEEP; Sep 8 = health-queue honesty, Rashi refuse-for-missing, mail encoding — **polish / quiet refinements, same URL**
- https://github.com/xyzqm/srsly | yesterday KEEP; Sep 8 = ES conjugation engine, ZH teach-before-test, 田字格 paper — **strong new drills but same URL** (do not re-keep per window rule)
- https://github.com/rishabh7g/rung | yesterday KEEP; Sep 8 = L4 Nuance closes on nine courses (360 modules) + shown-key hyphen tooling — **content expansion, not new exit-ritual mechanism**
- https://github.com/crnchwrpsupreem/nihongo-sensei | hourly public-tutor-context churn — no new mechanism
- https://github.com/serjflint/saitenka | prior KEEP; activity in window but immersion-workstation already shipped
- https://github.com/tobiaslrn/monosai | prior KEEP; no distinct new SETUP this window
- https://github.com/ksyasuda/SubMiner | mature mpv+Yomitan+Anki miner (N+1 annotations); Sep 8 = **docs refresh only** — saitenka-adjacent product
- https://github.com/gufyhvvyfycyddy-code/LinguaCafe-local | LinguaCafe fork/review branch; FSRS datetime / fail-soft import — **product polish / upstream library**
- https://github.com/46daishi/tomoyo | README still Tauri template; thin / scaffold
- https://github.com/reedmarler/KanjiQuest | JLPT SRS SPA; Sep 8 = profile sync / quest UI — **generic flashcard product**
- https://github.com/Uncorrected-nova574/playtranslate | README-only Sep 8; download links look spammy — **thin / suspect**
- https://github.com/yoshisao14/yomitan-hover-anki | still “Add files via upload”; README one-liner — **too thin**
- https://github.com/0xzerolight/anki_miner | packaging/i18n/audit fixes — **release polish** on known miner
- https://github.com/MuggleWu/miki | FSRS-6 Anki-alt UI (child windows, deck columns) — **scheduler product, no language gate**
- https://github.com/neoanki2/neoanki2 | Again-repair rounds — scheduler polish
- https://github.com/jvsena42/loopky | general “learn anything” Kotlin SRS; deps/DI — product polish
- https://github.com/peijungwu0302-Wu/toeic-vocab-pwa | cinematic image generation for TOEIC cards — **content pipeline / art**, not learner gate
- https://github.com/mansourvery-hub/anki-japanese-template | card layout CSS — template library
- https://github.com/bpwhelan/GameSentenceMiner | post-release packaging — known immersion toolkit polish
- https://github.com/gievano/kayara-anki | LICENSE chore only
- https://github.com/yurvon-screamo/origa | no commits since 2026-09-05 in atom
- https://github.com/VeyDlin/NektoTranslate | novel auto-translate reader release packaging — product, thin learning gate
- https://github.com/gpanakkal/incremental-reading-obsidian | IR plugin polish (scroll/search) — general IR, not language
- https://github.com/aislamsilvalol-ctrl/noema | KT research / EdNet ablations — research engine library
- https://github.com/mord58562/theankidote | medical Anki reference — off-lane
- https://github.com/5mdld/anki-jlpt-decks | JLPT deck dataset — **library**
- X / Firecrawl | skipped (dead / disallowed)

## FETCH NOTES
- GitHub Search API: OK early — `edu0909/search-repos.json` (30), `search-japanese-anki.json` (20), `search-fsrs-tutor.json` (20), `search-ankiconnect.json` (20). Later **core remaining=0** (unauth); switched to **commits/*.atom + raw.githubusercontent.com**.
- `gh auth`: not logged in.
- Atoms under `atoms09/`: sotto, WaniSieve, LinguaCafe-local, tomoyo, origa, playtranslate, KanjiQuest, NaraNote, SubMiner, toeic-vocab-pwa, sat-srs, language-tutor, janki, anki_miner, SmarterTypeField, miki, neoanki2, ahadiff, repetita, thai-language-anki, Micheon, LearnWithNoura, turna, srsly, targum, rung, kayara-anki, yomitan-hover-anki, incremental-reading-obsidian, loopky, noema, anki-japanese-template, GameSentenceMiner, NektoTranslate, hifz-trainer.
- Repo meta API for sotto: **403 rate limit**; used search JSON created/pushed fields instead.
- WaniSieve: README claims level filter; code path is `get_burned_vocab` — noted in overflow.
- Bank: deposited sotto, janki, NaraNote, WaniSieve, repetita I-know-this (commit-scoped), thai sentence-compile (commit-scoped) under `--lane learning --via grok-bot/Field`. Prior repetita/thai README deposits left intact (dup on same URL).
- HTML GitHub search / Firecrawl / X MCP: not used.
- Rate-limit: core reset epoch ~1788914517 (UTC); search stayed available (~10/min).

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) sotto **9**, (2) janki **9**, (3) NaraNote **8**.
- Overflow scored ≥6 not in top-3: repetita **9** (same-URL promote-watch), thai-deck **8** (generator companions), WaniSieve **7**, sat-srs **7**, Micheon **7**, LearnWithNoura **7** (off-lane), ahadiff **7** (off-lane), SmarterTypeField **6**, turna **6**, freesurf language-tutor **6**.
- Explicit bounce-deltas on prior keeps: targum health/Rashi polish; srsly conjugation/田字格 (same URL — do not re-keep); rung L4 content wave; SubMiner docs; nihongo hourly.
- **Do not re-ship** targum / srsly / rung / overtonch / saitenka / note-buddy / nihongo / sillon / monosai unless compiler deliberately refreshes.
- Alert-line item: **none**.

No packet file written. field-seen.json not edited.
