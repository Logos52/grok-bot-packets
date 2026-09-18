# Field education hunt — 2026-09-16 scratch (Wednesday)
Window: ~2026-09-15 00:00 UTC → now (also late Sep 14 if truly new URL not kept). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): VinciusGoulart/japones-jlpt 10, bee-san/hachidori 9, takashi955/lessonloop 9. Overflow promote-watch: mShono/finn_cards (was idle → **window activity**), Dilnazzzz/bridge (still Sep 10), pekoqq/ReadLoops (was UI polish → **vocab-gap mechanism**), gillisandrew/ancci (already promote-fired), yuktun/japanese-study 8 (lesson audits continue).

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; yesterday KEEP three URLs; BeastMaster75/NaraNote SEEN; noisy tutor-OR false positives (golang/go etc).

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) bee-san / jlpt-levels-yomitan — reproducible fail-closed Yomitan JLPT N5–N0 meta; never fabricate absent evidence — PRIMARY
- who: bee-san (same author as yesterday hachidori KEEP; **different URL**)
- url: https://github.com/bee-san/jlpt-levels-yomitan
- date: created **2026-09-15**; window = fail-closed immutable release pipeline + Yomitan importer verify + publish through ~20:08Z; package `REVISION=2026.09.15`
- tags: education·wiki-craft·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·wiki-craft·teach-once·quiet-when-nothing] score=10 | bee-san / jlpt-levels-yomitan | Reproducible Yomitan term-metadata dictionary: every normalized Jitendex `(written, reading)` lexeme → N5…N1 or project **N0** (“harder than N1”, never unknown placeholder). Pipeline: pinned Jitendex census → direct evidence → conservative fallback (absent features stay absent, **not fabricated**) → isolated residual adjudication → exact-census finalize → Yomitan package. Release fails closed on stale explanations, source-set drift, corpus collapse, or inventory mismatch; packaging binds lexeme/classification/registry/lock into `artifact-manifest.json`; verified via real Yomitan `DictionaryImporter`. Distinct from hachidori (lookup-count/mature-Anki **blur**) — **lexeme JLPT meta as audited teach-once wiki-craft for immersion lookup**. | https://github.com/bee-san/jlpt-levels-yomitan
- why distinct: NEW URL; fail-closed JLPT meta packaging not on yesterday’s roster (hachidori is reveal-schedule, this is classification provenance).
- bank: `2026-09-16-bee-san-jlpt-levels-for-yomitan-reproducible-fail` (**deposited** learning lane; body `/workspace/field/bank-bodies/2026-09-16-jlpt-levels-yomitan.txt`)

### 2) dothuan-git / kotonoha-anki — private JA→VI FSRS trainer; bidirectional; AI draft deliberately not built — STRONG
- who: dothuan-git (named single-user allowlisted practice)
- url: https://github.com/dothuan-git/kotonoha-anki
- date: created **2026-09-06**; window = meaning-first mode, JSON import, missed-today recap, unlimited daily caps, import-preview exclude, learning-step in showings — through **2026-09-16** ~00:12Z
- tags: education·tutor-loop·human-gate·quiet-when-nothing·teach-once
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·tutor-loop·human-gate·quiet-when-nothing] score=8 | dothuan-git / kotonoha-anki | Private Japanese vocabulary trainer with **Vietnamese** meanings (washi/wabi-sabi UI). FSRS (`ts-fsrs`); reviews ask every word **both sides**, one grade for the pair; works offline (idb outbox + PWA). Auth.js Google with **single `ALLOWED_EMAIL`** (unset ⇒ nobody). Words enter by hand / dict / share sheet / JSON import; import preview can **strike words off** before commit. Explicit **Not built**: `POST /api/draft` AI meaning/example — fields exist, nothing fills them, no Anthropic key read. Distinct from japones-jlpt (Claude mesa+Anki-truth) and ancci (agent Anki authoring) — **JA↔VI FSRS personal trainer with intentional non-AI quiet**. | https://github.com/dothuan-git/kotonoha-anki
- why distinct: NEW URL; VI L2 meanings + deliberate AI abstention not on roster.
- bank: `2026-09-16-dothuan-git-kotonoha-private-ja-vi-fsrs-trainer` (**deposited**; body `/workspace/field/bank-bodies/2026-09-16-kotonoha-anki.txt`)

### 3) onuross / anki-llm-pipeline — PDF→AnkiConnect; EN autonomous / DE hybrid human-in-loop — STRONG (day-0)
- who: onuross (HTW Dresden CS; named personal DE/EN pipeline)
- url: https://github.com/onuross/anki-llm-pipeline
- date: created **2026-09-15** (~21:49Z initial release); README polish ~22:01Z
- tags: education·human-gate·generated-input·teach-once·quiet-when-nothing
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·human-gate·generated-input·teach-once] score=8 | onuross / anki-llm-pipeline | PDF→normalize→Gemini enrich→Edge-TTS→**AnkiConnect** cloze inject. Portable split: **English = 100% autonomous**; **German = hybrid human-in-the-loop** because gender/case cloze errors are costly — Pro fallback TXT for manual LLM when API/rate demands it. Philosophy: data quality > blind full-automation. Part 1 cron/launchd batches; Part 2 `ankipush` is intentional (Anki must be local). DE article colorization in Anki template; JA glue util for fragmented cloze HTML. Distinct from lfreeman/ankix (dry-run CLI) and lessonloop (OCR course import) — **language-aware autonomy ceiling with DE human-gate**. | https://github.com/onuross/anki-llm-pipeline
- why distinct: NEW URL; day-0 DE hybrid gate vs EN full-auto.
- bank: `2026-09-16-onuross-anki-llm-pipeline-pdf-ankiconnect-en` (**deposited**; body `/workspace/field/bank-bodies/2026-09-16-anki-llm-pipeline.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### mShono / finn_cards — score 9 (overflow / promote-watch **FIRE**)
- url: https://github.com/mShono/finn_cards
- date: was idle since Sep 11; window **2026-09-15** PRs: `learn-n-plus-one`, `srs-shared-write-back`, `fst-pos-per-lemma`, note-dedup race
- tags: education·i-plus-one·teach-once·human-gate·tutor-loop
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Kielikaveri FI Telegram bot — FST-verified forms (never LLM-invented). Window adds **/learn n+1 path**, shared SRS write-back, POS-per-lemma via FST. Same URL already banked/promote-watched → **overflow promote-fire**, not a fourth top-3 slot (prefer NEW URLs #1–#3). Compiler may swap #3 for finn_cards if FI tutor-loop preferred over DE pipeline day-0.

### pekoqq / ReadLoops — score 9 (overflow / promote-watch **FIRE**; EN CET-4)
- url: https://github.com/pekoqq/ReadLoops
- date: **2026-09-15** `feat(vocab): 词汇差距闭环 —— 考试词表 + 定级测试 + 重遇机制 + 蒸馏修正`; KB/PDF/MinerU stack Sep 14; PyPI 2.3.1
- tags: education·generated-input·i-plus-one·reveal-schedule·tutor-loop
- one-liner: Controlled AI graded articles (95–98% coverage) + FSRS; **new vocab-gap closed loop** (exam wordlist + placement + re-encounter + style distillation) — no longer UI-polish-only. Still EN CET-4 lane → overflow under prefer JA/ZH/KO/FI/DE/IT.

### yuktun / japanese-study — score 8 (overflow; continue)
- url: https://github.com/yuktun/japanese-study
- date: window = Year-1 lesson audits + flashcard swipe through **2026-09-15** ~23:01Z
- one-liner: School-PDF authority wiki-craft; audits continue — still content migration > tutor-loop → overflow.

### cute6v / spoken-tutoring-prototype — score 7 (overflow; EN research PoC)
- url: https://github.com/cute6v/spoken-tutoring-prototype
- date: created **2026-09-15** (single initial commit)
- tags: education·tutor-loop·teach-once
- one-liner: Master's dissertation spoken tutor with explicit **LSFC** (Learner-State Feedback Connector) separating forward feedback from backward state routing; Whisper optional; DeepSeek + rule fallback. Research PoC / not production named daily practice → overflow.

### maitodesu / jlpt-grammar-decks — score 7 (overflow; reveal-schedule slides)
- url: https://github.com/maitodesu/jlpt-grammar-decks
- date: created **2026-09-15**; furigana ruby click-toggle
- one-liner: N5–N3 grammar as 47 standalone HTML chapter decks (~6,500 slides); practice answers hidden until stepped. Strong reveal-schedule content ship — thinner runnable tutor loop than KEEP → overflow.

### ColorlessBoy / sokonanoda-lang — score 6 (overflow; edge education)
- url: https://github.com/ColorlessBoy/sokonanoda-lang
- date: heavy window pushes through **2026-09-16** (Lean teaching kernel / course / VS Code)
- one-liner: Self-contained Lean-4 teaching dialect; real kernel grades proofs. Education-adjacent but **not L2 language** → edge overflow / library-adjacent.

### gillisandrew / ancci — score 8 (overflow; no new since Sep 14)
- still prior promote-fire; atom last **2026-09-14** Release 0.5.1 — no new window mechanism today.

### Dilnazzzz / bridge — score 9 (overflow; **still idle** since 2026-09-10)
- no window commits.

### Same-URL / yesterday KEEP watches (do not re-keep)
- VinciusGoulart/japones-jlpt / bee-san/hachidori / takashi955/lessonloop — yesterday KEEP skip
- BeastMaster75/NaraNote — SEEN; Sep 15 Docker/auth polish only
- MattFor/lexiglance, mazdiaz/jiten-migaku-miner, lfreeman/ankix, chachaprince1/anime-episode-to-anki, Morgawr/kechimochi — prior overflow; not re-scored as new KEEP

## BOUNCE list (url | why)
- https://github.com/VinciusGoulart/japones-jlpt | yesterday KEEP
- https://github.com/bee-san/hachidori | yesterday KEEP (this hunt’s jlpt-levels-yomitan is a **different URL**)
- https://github.com/takashi955/lessonloop | yesterday KEEP
- https://github.com/Ceidoux/SmartJisho | early FastAPI+Postgres kanji search milestone; Anki export aspirational — thin (yesterday bounce confirmed; still scaffold)
- https://github.com/Mangrover007/yomitan-setup | personal setup dump; README 404 / single “setup” commit
- https://github.com/DeuterioX/JLPT-FlashCard | created today; README 404; atom returned HTML wall — no runnable evidence
- https://github.com/FredrikFlo/AnkiChineseImporter | created Sep 15; README 404; atom HTML wall — no evidence
- https://github.com/Meridasia/Japanese-Text-Analysis | KanjiCoverage Julia JLPT kanji % tool — analysis/library not learner loop
- https://github.com/Meridasia/test | duplicate of above
- https://github.com/HongPhuc2511/japanese-learning-platform | Django/React product scaffold; thin README
- https://github.com/Jaysese125/japanese-learning-journey | learning portfolio docs — not a setup
- https://github.com/TheNomet/language-tutor | empty desc / stub
- https://github.com/NikityaoS/language_tutor | stub
- https://github.com/alexandraHospital/language_tutor | stub
- https://github.com/IronWrathX/- | off-lane stub
- https://github.com/Sumdiboii/jlpt-n3-cheatsheet (and n4/n5) | cheatsheet dumps
- https://github.com/BrockBadeaux14/AnkiVoice | still planning/fixtures (prior bounce)
- https://github.com/shef-broski/intro-to-anki | booklet / library
- https://github.com/devDhiraj-H/Anki_fast_cards | generic card-gen ext; thin
- https://github.com/marqp/Obsidian_to_Anki | Obsidian fork; not L2 tutor
- https://github.com/FelipeNava393/Anki_English | personal EN Anki system stub
- https://github.com/meetthehorizon/jee-anki | JEE/STEM — off-lane
- https://github.com/anprowh/anki-media-compressor | tooling
- https://github.com/api-evangelist/anki | API profile — library
- https://github.com/golang/go | false positive from tutor OR query
- https://github.com/donkuri/kaishi | long-lived deck; not new named window setup
- https://github.com/bpwhelan/GameSentenceMiner | long-lived immersion toolkit polish
- https://github.com/Chimahon/chimahon | Mihon fork polish — SEEN-pattern product
- https://github.com/colanekojp/JLPT-N1-raining-camp | static N1 camp site
- https://github.com/derisean-cmd/JLPTcalc | score calculator
- X / Gmail / Slack | not used this hunt

## FETCH NOTES
- HTML GitHub search pages: **429 Too many requests** (edu0916/search-1..12.html). Prefer parent Search API JSONs: `search-pushed-anki-ja.json`, `search-created.json`, `search-pushed-ci.json`, `search-pushed-tutor.json` + sparse `api-jlpt-created.json` / `api-anki-pushed.json`.
- Core REST remaining=0 most of hunt — **no core API**; evidence via `commits.atom` + `raw.githubusercontent.com` READMEs under `edu0916/` and `edu0916/readmes/`.
- Promote-watch atoms: finn_cards **2026-09-15** n+1/SRS fire; bridge **still 2026-09-10**; ReadLoops **2026-09-15** vocab-gap; yuktun lesson audits; ancci idle since Sep 14.
- Truncations / misses: DeuterioX + FredrikFlo atom returned GitHub HTML shell (no entries); Mangrover/DeuterioX/Fredrik README 404; MattFor/lexiglance README 404 (prior).
- Bank deposits: **succeeded** for jlpt-levels-yomitan, kotonoha-anki, anki-llm-pipeline → `raw/learning/2026-09-16-*` + INDEX. Bodies at `/workspace/field/bank-bodies/2026-09-16-{jlpt-levels-yomitan,kotonoha-anki,anki-llm-pipeline}.txt`.
- scratch-seen-urls.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) jlpt-levels-yomitan **10**, (2) kotonoha-anki **8**, (3) anki-llm-pipeline **8**.
- Overflow scored ≥6 not in top-3: finn_cards **9** (promote-fire), ReadLoops **9** (promote-fire EN), yuktun **8**, ancci **8** idle, cute6v **7**, maitodesu **7**, sokonanoda-lang **6**; bridge **9** still idle.
- **Swap note:** prefer finn_cards over anki-llm-pipeline for #3 if compiler wants FI FST tutor-loop with new n+1 over day-0 DE hybrid ETL. Do **not** drop #1.
- Explicit bounce-deltas on prior keeps: yesterday three KEEP = skip; SmartJisho still thin; NaraNote SEEN polish.
- Alert-line item: **none**.

## Result for compiler: 3 KEEP
1. bee-san/jlpt-levels-yomitan — 10 — fail-closed Yomitan JLPT N5–N0 meta; never fabricate; wiki-craft
2. dothuan-git/kotonoha-anki — 8 — private JA→VI FSRS; bidirectional; AI draft not built
3. onuross/anki-llm-pipeline — 8 — PDF→AnkiConnect; EN auto / DE hybrid human-gate
