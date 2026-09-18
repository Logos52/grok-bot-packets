# Field education hunt — 2026-09-17 scratch (Thursday)
Window: ~2026-09-16 00:00 UTC → now (also late Sep 15 if truly NEW URL not kept). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): bee-san/jlpt-levels-yomitan 10, dothuan-git/kotonoha-anki 8, onuross/anki-llm-pipeline 8. Overflow promote-watch: mShono/finn_cards 9 (promote-fired Sep 16), pekoqq/ReadLoops 9 (promote-fired), yuktun/japanese-study 8, gillisandrew/ancci 8 idle, Dilnazzzz/bridge still idle Sep 10, cute6v/spoken-tutoring-prototype 7, maitodesu/jlpt-grammar-decks 7, ColorlessBoy/sokonanoda-lang 6.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; repos in `seen-gh-repos-lower.txt`; yesterday KEEP three URLs; noisy tutor-OR false positives.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) ColinHouse / kotoba-studio — local-first JA Galgame/anime sentence-mining companion; FSRS + optional Anki — PRIMARY
- who: ColinHouse (named personal JA tool; ZH-L1 UI)
- url: https://github.com/ColinHouse/kotoba-studio
- date: created **2026-09-16** (~00:27Z); window through **2026-09-16** ~23:35Z (EPUB light-novel import, KANJIDIC2 progress, in-game overlay, capture/hook gates, restore concurrency fix)
- tags: education·immersion·i-plus-one·tutor-loop·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·immersion·i-plus-one·tutor-loop·teach-once] score=10 | ColinHouse / kotoba-studio | Local-first Japanese companion for **Chinese-L1** learners: capture Galgame/anime lines (screenshot + original audio) → inbox word confirm → **FSRS** review on desktop/phone PWA. Portable mechanisms: kanji→reading cards by default; **中日同形** false-friend auto-flag; spoken-contraction boundary labels (ちゃう←てしまう…); post-session 3-min quiz; SQLite+media backup; optional JSON/.apkg/**AnkiConnect** export (Anki not required). Hook ingest (Textractor/LunaTranslator) + Windows in-game overlay. Distinct from kotonoha-anki (JA↔VI hand entry) and GameSentenceMiner (toolkit polish) — **context-preserving immersion mining with ZH-aware annotations and FSRS-native loop**. | https://github.com/ColinHouse/kotoba-studio
- why distinct: NEW URL day-0; immersion capture→FSRS not on yesterday roster; ZH false-friend + contraction teach-once.
- bank: `2026-09-17-colinhouse-kotoba-studio-local-first-ja-galgame` (**deposited** learning lane; body `/workspace/field/bank-bodies/2026-09-17-kotoba-studio.txt`)

### 2) lavich / Tavelori (Lexi) — offline Greek FSRS trainer; syllabus schedule + syllable-assembly gate before writing — STRONG
- who: lavich (named Lexi / tavelori.app)
- url: https://github.com/lavich/Tavelori
- date: created **2026-09-16** (~05:06Z); window through ~20:30Z (on-demand lesson packages; group lessons into courses)
- tags: education·tutor-loop·human-gate·teach-once·quiet-when-nothing·generated-input
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·tutor-loop·human-gate·teach-once] score=9 | lavich / Tavelori (Lexi) | Local PWA Greek vocab trainer (no account/server): schedule-driven lesson sets, on-demand versioned lesson packages (reject partial/corrupt installs), cards with art+IPA+reading breakdown, five exercise types + **FSRS**. Portable gate: **syllable-assembly must clear twice before free writing**; writing errors re-lock to assembly; practice mode trains skill **without moving FSRS intervals**. Content = YAML words/lessons; Quizlet import with preview/dedupe. Distinct from benkyou (JLPT multi-choice drill) and finn_cards (FI FST) — **syllabus-timed EL tutor with production-skill gate before spelling**. | https://github.com/lavich/Tavelori
- why distinct: NEW URL; Greek not on roster; syllable-before-writing + schedule lessons are portable tutor-loop gates (even though EL ∉ prefer JA/ZH/KO/FI/DE/IT — mechanism quality).
- bank: `2026-09-17-lavich-tavelori-lexi-offline-greek-fsrs-trainer` (**deposited**; body `/workspace/field/bank-bodies/2026-09-17-tavelori.txt`)

### 3) Hanayou / benkyou — offline JLPT N5–N1 kanji/vocab drill PWA; working-set rotation — STRONG (day-0)
- who: Hanayou (named Benkyō PWA)
- url: https://github.com/Hanayou/benkyou
- date: created **2026-09-16** (~07:55Z); initial release + quiz/info-drawer polish ~08:06Z
- tags: education·teach-once·quiet-when-nothing·tutor-loop
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·teach-once·quiet-when-nothing·tutor-loop] score=8 | Hanayou / benkyou | Installable **offline** JLPT kanji+vocab drill PWA (no accounts/server; IndexedDB + clipboard backup). 10 lists N5→N1 kanji/vocab; each group quizzed in **6 directions** (kanji↔yomi↔English) as 4-choice; **working set ~20** unfinished groups so new material repeats; maxed groups retire. Per-list answer-target **frozen at start** (reset to change). Info drawer: KanjiVG strokes, readings, Tanaka examples — out of the way until swipe. Distinct from jlpt-grammar-decks (HTML reveal slides) and jlpt-levels-yomitan (meta packaging) — **runnable offline working-set JLPT drill**. | https://github.com/Hanayou/benkyou
- why distinct: NEW URL day-0; working-set + locked-rules portable; JA prefer-lang.
- bank: `2026-09-17-hanayou-benky-offline-jlpt-kanji-vocab-drill` (**deposited**; body `/workspace/field/bank-bodies/2026-09-17-benkyou.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### anonymouspartner / capybara-anki — score 9 (overflow; couple L2 closed-loop)
- url: https://github.com/anonymouspartner/capybara-anki
- date: created **2026-09-15**; window through **2026-09-17** ~00:03Z (Anki scheduling behaviours import; migration D17/D18; PostgREST paging)
- tags: education·tutor-loop·human-gate·teach-once
- portable / evidence / combined: **4 / 5 / 9**
- alert: **no**
- one-liner: Self-owned SRS for one couple learning each other’s languages — offline reviewer + page scanner + pronunciation, Postgres dual-write with Capybara Telegram bot; closes one-way AnkiDroid dead-end. Strong evidence (Playwright + live deploy) but personal couple stack / UKR-adjacent → overflow under prefer JA/ZH/KO/FI/DE/IT; compiler may swap #3.

### xmonkey / paperback — score 8 (overflow; pen-paper Anki writeback)
- url: https://github.com/xmonkey/paperback
- date: created 2026-06-30; window **2026-09-16/17** (include-new-cards option; `[[type:]]` face split + bury/suspend exclude)
- tags: education·human-gate·teach-once·quiet-when-nothing
- one-liner: AnkiConnect → printable dictation worksheets → manual 1–4 grade (default **Again**) → ease writeback; OCR photo-grade exists but marked not-for-daily. Distinct active-recall modality — NEW URL not previously kept → overflow (prefer day-0 JA #3); swap candidate over benkyou if pen-paper gate wanted.

### gehbfarr5 / ielts-vocab-automation — score 9 (overflow; EN evidence-aware)
- url: https://github.com/gehbfarr5/ielts-vocab-automation
- date: created **2026-09-16**; window admissions/budgets/IPA through ~17:20Z
- one-liner: Goodnotes three-color highlight → local Vision OCR → agent with **fail-closed missing CEFR evidence** → dual learning budgets → AnkiConnect readback. Strong quiet-when-nothing / human-gate — EN IELTS lane → overflow (mirrors yesterday jlpt-levels fail-closed spirit).

### piggyham / BlinkWord — score 8 (overflow; EN/ZH selection→FSRS)
- url: https://github.com/piggyham/BlinkWord
- date: created **2026-09-16** v0.1
- one-liner: Windows Electron selection-translate popup → vocab book → ts-fsrs review; importance bump on re-save. EN-leaning with ZH UI → overflow under prefer list.

### bannysway / grab-series-vocab — score 8 (overflow; corpus-first TV vocab)
- url: https://github.com/bannysway/grab-series-vocab
- date: window **2026-09-16** agent-skill + matrix corpora (Friends / NYPD Blue / Your Lie in April EN)
- one-liner: Measured 35.9% episode-deck duplicates → **corpus-first headword library** then Anki/MD/web views; no subtitle text shipped. EN immersion → overflow; related profile `bannysway/bannysway`.

### Promote-watch continues (same URLs — do not re-keep)
- mShono/finn_cards — Sep 16 review-starvation + deck-routing polish after n+1 fire — **still overflow**, no new distinct mechanism for fourth slot.
- pekoqq/ReadLoops — Sep 16 placement-test precision + mobile/Tailscale — continue promote; EN CET-4.
- yuktun/japanese-study — Year-2 lesson audits + flashcard filters/random through Sep 16 ~21:57Z — content wiki continue.
- gillisandrew/ancci — still idle since Sep 14 Release 0.5.1.
- Dilnazzzz/bridge — **still idle** since 2026-09-10.
- cute6v / maitodesu — no new window activity beyond prior day-0.
- ColorlessBoy/sokonanoda-lang — course-outline P1–P3 Sep 16 — still not L2 language → edge overflow.

### Same-URL / yesterday KEEP watches (do not re-keep)
- bee-san/jlpt-levels-yomitan / dothuan-git/kotonoha-anki / onuross/anki-llm-pipeline — yesterday KEEP skip (onuross README polish only Sep 16).
- VinciusGoulart/japones-jlpt / bee-san/hachidori / takashi955/lessonloop — older KEEP skip.

## BOUNCE list (url | why)
- https://github.com/bee-san/jlpt-levels-yomitan | yesterday KEEP
- https://github.com/dothuan-git/kotonoha-anki | yesterday KEEP
- https://github.com/onuross/anki-llm-pipeline | yesterday KEEP
- https://github.com/elcarer/immersion | ECS/game sprite refactor — not L2 immersion
- https://github.com/ia2213/mural-gemini | README points at Chuloo/mural fork surface; multi-provider voice tutor — EN/ES product; evaluate as library/overflow not top-3 this hunt
- https://github.com/jibranpcccc/japanese-jlpt-n1-n3-grammar-kanji-hub | directory dump; README 404
- https://github.com/ao100605/kana-compass | README 404
- https://github.com/jonnunez03/japanese-learning-app | empty README
- https://github.com/Brown-University-Library/matching-game | stub “match em”
- https://github.com/anupKanere/japanora | N5 platform scaffold / product
- https://github.com/devcadujapan/JLPT_Cards-Vocabulario | card dump first commit
- https://github.com/SureshSurkheti/jlpt-practice | long-lived mock-exam site UI polish — not new named mechanism
- https://github.com/zarnthyr/card-janitor | Anki cleanup add-on (destructive) — tooling not tutor-loop
- https://github.com/AliceLiddell01/CrowdAnki_V2 | CrowdAnki fork scaffolding
- https://github.com/Sthabiso10/recall-srs | headless FSRS React library — not L2 named practice
- https://github.com/mojunbeiming/obsidian-fsrs-flashcards | Obsidian plugin library
- https://github.com/iv-re/fsrs-dart | FSRS port library
- https://github.com/marqp/Obsidian_to_Anki | Obsidian fork; not L2 tutor
- https://github.com/DeuterioX/JLPT-FlashCard | prior bounce; thin
- https://github.com/Sumdiboii/jlpt-n4-cheatsheet | cheatsheet (and n5 sibling)
- https://github.com/cct2277256745-source/ielts-vocab | thin desktop IELTS app vs automation sibling
- false-positive Ankita/portfolio / music-theory / DSA / Linux flashcards | name/topic noise
- X / Gmail / Slack | not used this hunt

## FETCH NOTES
- `gh` CLI unauthenticated on box → used `curl` to `api.github.com/search/repositories` (200) + `raw.githubusercontent.com` READMEs + `commits.atom`.
- Search dumps under `/workspace/field/edu0917/curl-*.json`; READMEs/atoms under `edu0917/readmes/` + `edu0917/atom-*.xml`.
- Promote-watch atoms refreshed: finn_cards Sep 16 polish; ReadLoops placement+mobile; yuktun Year-2 audits; bridge still Sep 10; ancci idle; yesterday KEEP atoms idle-of-mechanism.
- Truncations / misses: jibranpcccc hub README 404; ao100605/kana-compass README 404; jonnunez03 empty README; elcarer/immersion README 404 (game ECS).
- Bank deposits: **succeeded** for kotoba-studio, Tavelori, benkyou → `raw/learning/2026-09-17-*` + INDEX. Bodies at `/workspace/field/bank-bodies/2026-09-17-{kotoba-studio,tavelori,benkyou}.txt`.
- scratch-seen-urls.txt / seen-gh-repos-lower.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) kotoba-studio **10**, (2) Tavelori **9**, (3) benkyou **8**.
- Overflow scored ≥6 not in top-3: capybara-anki **9**, ielts-vocab-automation **9**, paperback **8**, BlinkWord **8**, grab-series-vocab **8**; finn_cards/ReadLoops/yuktun continue; ancci idle; bridge still idle.
- **Swap notes:** (a) prefer paperback or capybara-anki over benkyou for #3 if Anki writeback / couple closed-loop preferred over JLPT drill PWA; (b) if prefer-lang hard gate drops Greek, promote benkyou to #2 and paperback to #3, keep Tavelori as overflow. Do **not** drop #1.
- Explicit bounce-deltas on prior keeps: yesterday three KEEP = skip.
- Alert-line item: **none**.

## PACKET READY
1. [education·immersion·i-plus-one·tutor-loop·teach-once] score=10 | ColinHouse / kotoba-studio | Local-first JA Galgame/anime line capture (shot+audio) → inbox → FSRS; ZH false-friend + contraction annotations; optional AnkiConnect; Anki not required. | https://github.com/ColinHouse/kotoba-studio
2. [education·tutor-loop·human-gate·teach-once] score=9 | lavich / Tavelori (Lexi) | Offline Greek FSRS PWA; schedule lessons; syllable-assembly gate before writing; practice mode does not move intervals. | https://github.com/lavich/Tavelori
3. [education·teach-once·quiet-when-nothing·tutor-loop] score=8 | Hanayou / benkyou | Offline JLPT N5–N1 kanji/vocab drill PWA; 6-direction quizzes; working-set ~20; locked per-list targets; KanjiVG drawer. | https://github.com/Hanayou/benkyou

## Result for compiler: 3 KEEP
1. ColinHouse/kotoba-studio — 10 — JA immersion mining + FSRS; ZH-aware annotations
2. lavich/Tavelori — 9 — Greek Lexi FSRS; syllable-before-writing + syllabus
3. Hanayou/benkyou — 8 — offline JLPT working-set drill PWA
