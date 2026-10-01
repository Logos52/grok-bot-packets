# Field education hunt — 2026-10-01 (Asia/Taipei cron; box America/New_York Wed Sep 30 evening ET)

Window: `created:>2026-09-29` / `created:2026-09-30` / `created:2026-10-01` (GitHub MCP `cursor-github` search_repositories; split OR queries ≤5 ops; raw.githubusercontent.com README/index fetches → `/workspace/field/edu1001/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (`seen-gh-repos-lower.txt` 307→434 + prompt list). Do NOT re-keep yesterday packet 48: ttiyana/korean-fast-track, jarod85/Chinese-Learning-App-Lock-Phone-Samsung, RudyBoe/kanji-trainer. Overflow already SEEN: Ellisdeeman/n5-vocab-quest, Dev-moe-kyawaung/TOPIKII-Level-3-pro-v3.0, mobashirrahman/glossline-android, yorkwahaha/kana-run, priyasureshgermany/deutsch-lernen, and earlier seen list. Skip Dev-moe TOPIKII-App / Level-3-premium siblings.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. stagfoo / jlptbenkyo — score 10 · [education·SRS·i-plus-one·tutor-loop·reveal-schedule·prefer-JA]
- one-line packet shape: Offline-first **Android JLPT N5–N3 desk** (Flutter/Dart, Obtainium-friendly): **one SM-2 SRS queue** mixing 3,526 words + 612 kanji + 145 grammar; **graded reading** (sentence tagged by hardest kanji; above-N3 excluded by default); device JA TTS listening; speak-record vs reference; KanjiVG stroke writing; **52 daily real-world challenges** (café/directions/decline invite…) scored to fit *currently mid-deck* vocab (phrases folded until opened). Ships 4.9 MB SQLite APK, **never networks**. Content from open-anki-jlpt-decks + kanji-data + jmdict-simplified + KanjiVG; authored grammar/challenges fail-loud on script contamination. | https://github.com/stagfoo/jlptbenkyo | created 2026-09-30
- Distinct-from: Ellisdeeman/n5-vocab-quest (single-file vocab PWA) — this is **full skills desk + deck-fitted daily production**. Distinct from RudyBoe/kanji-trainer (same-reading graph) — cumulative N5–N3 + grammar + challenges, not kanji-only navigation. Distinct from ttiyana/korean-fast-track (KO web FSRS desk) — JA Android offline SM-2.

### 2. ahmadasrizalmi / Japanese-Reader-AI (Komorebi Reader) — score 9 · [education·immersion·reveal-schedule·SRS·prefer-JA]
- one-line: Offline-first **Android immersion reader** (Kotlin Compose + Room; APK in `releases/`): paste/import JA → chat-bubble canvas; **furigana + ID gloss on-tap** (clean until touch); auto-save tapped words into study deck; speaker play/stop TTS (no auto-play); dynamic JLPT N5–N1 difficulty from kanji weight; optional Cloudflare Edge + DeepSeek BYOK. Screenshots + v1.2.0 APK/AAB shipped. | https://github.com/ahmadasrizalmi/Japanese-Reader-AI | created 2026-09-30
- Distinct-from: GeorgeAzma/ruby (Chrome furigana overlay, reference-only license) — this is **phone reader + auto vocab SRS**. Distinct from conao3/rust-overhear / HadrienT/live-subs (live audio mining) — text immersion desk, not system-audio ASR.

### 3. mansourvery-hub / anki-chinese-template — score 8 · [education·reveal-schedule·immersion·prefer-ZH]
- one-line: Ultra-compact **Simplified Chinese sentence-mining Anki note type** (port of anki-japanese-template): front is pure retrieval (Chinese only, never Pinyin); back = target → **tone-coloured Pinyin** → compacted definition → sentence context; `P`/`X`/`C` reveal keys; `#listening` audio-gated front; **Mature Word Mode** (desktop, interval≥365d → word-only front via AnkiConnect); AnkiDroid-safe (no false media errors). Dense mobile+desktop card, Anki remains the SRS. | https://github.com/mansourvery-hub/anki-chinese-template | created 2026-09-30
- Distinct-from: jarod85 HanziLock (phone human-gate production) — this is **mining card chrome**, not lock-screen. Distinct from Laraib2004/learnmandarin (speaking PWA course) — note-type for Yomitan/mined sentences.

## Overflow (≥6, below top-3 SETUP slots)

### HadrienT / live-subs — score 9 (overflow; prefer-JA immersion·heavy)
- Firefox extension + LAN GPU server: YouTube live audio → kotoba-whisper JA (p50 ~0.32s) → local LLM EN overlay; ahead-mode (~6s behind live); channel glossaries; SRT/VTT export. Measured V100 stack; nothing leaves LAN. Same immersion-mining class as rust-overhear — heavy local GPU. | https://github.com/HadrienT/live-subs | created 2026-09-30

### Eason-Xi / pocket-nihongo — score 9 (overflow; prefer-JA SRS·hardware-locked)
- FoloToy AI Passport firmware: fully offline kana (104×2) + 153 N5 words, pre-baked JA voice, 4 quiz styles, **0–5 box SRS**, NVS progress, washi UI. Portable SRS/quiz gates — but **device-locked** to FoloToy hardware. Sibling pocket-korean same day. | https://github.com/Eason-Xi/pocket-nihongo | created 2026-09-30

### Eason-Xi / pocket-korean — score 8 (overflow; prefer-KO SRS·hardware-locked)
- Same Passport: Hangul letters (40) + 167 vocab + 28 situation phrases + quizzes; Edge-TTS audio pack optional; miss-returns-3-later; ZH UI. Hardware-locked twin of pocket-nihongo. | https://github.com/Eason-Xi/pocket-korean | created 2026-09-30

### JobsKits / JpKanji — score 8 (overflow; prefer-JA dictionary·reveal)
- Offline PySide6 **日语汉字点读** desk: KANJIDIC2 13k + JMdict 218k + Tatoeba examples; on/kun/nanori + red furigana; ZH gloss via bundled Argos offline MT; click-kana TTS; Mac DMG / Win EXE packagers. Lookup+teach desk more than daily SRS loop. | https://github.com/JobsKits/JpKanji | created 2026-09-30

### angelengineer / japanese-web — score 8 (overflow; prefer-JA tutor-loop)
- Static **活用 conjugation drill** to N3 (Spanish UI/meanings): 108 real form combos; romaji/IME input; misses return in 4 turns; Notion-sourced verbs + hand ES example rewrites; localStorage accuracy. Live Pages-ready. | https://github.com/angelengineer/japanese-web | created 2026-09-30

### sakurakojapanesetutor0317 / kana-renshu — score 8 (overflow; prefer-JA stroke·PWA)
- Single-folder PWA: hiragana/katakana + JLPT N5–N1 kanji stroke animate/trace, device JA TTS, picture-word + reading quizzes; SW offline; KanjiVG/KANJIDIC2/open-anki-jlpt data. | https://github.com/sakurakojapanesetutor0317/kana-renshu | created 2026-09-30

### sameerakmal / MedDeutsch — score 8 (overflow; prefer-DE niche tutor-loop)
- Local-first Vite SPA: nursing **A1/A2 clinical German** — gender/articles, scenario quizzes, mistake list → active-recall review → mastery; de-DE TTS; no account. Live Vercel demo. Domain-narrow (medical) but clean learn→miss→review loop. | https://github.com/sameerakmal/MedDeutsch | created 2026-09-30

### MarioEstebanMateo / JapaneseLearningApp (ことば) — score 7 (overflow; prefer-JA Genki quiz)
- Vite React **Genki I L1–12** Spanish desk: vocab / verb forms (ます/past/て) / sentence translation MC; ruby readings; kanji review flip; grammar notes from chapter text. Thin README; evidence is `src/App.jsx` + `genki_data.json`. No durable SRS/localStorage. | https://github.com/MarioEstebanMateo/JapaneseLearningApp | created 2026-09-30

### satasuk03 / hanzi-rush — score 7 (overflow; prefer-ZH game·SRS-light)
- Vite static HSK 1–6 mini-games desk (TH+EN): Meaning Rush (misses back in 4; TTS) + Hanzi Gacha collection; 4,991 words; more juice/gacha than tutor curriculum. | https://github.com/satasuk03/hanzi-rush | created 2026-09-30

### yuhouzhou / german-prepositions-anki — score 7 (overflow; prefer-DE Anki content)
- 439-card A1–C1 **Präpositionen** master suite (verbs/adj/nouns/NVR); frequency order; case colour pills; da-/wo- compounds; hierarchical level/prep/case tags; shipped `.apkg`. Sibling of seen german-nouns-anki. | https://github.com/yuhouzhou/german-prepositions-anki | created 2026-09-30

### XPLassal / deutsch-a1-anki — score 7 (overflow; prefer-DE Anki content)
- Goethe A1 Wortliste (~617) → Neo-Brutal sticker Anki `.apkg` with RU fields, typed check, article colour; genanki pipeline. Content pack not interactive tutor. | https://github.com/XPLassal/deutsch-a1-anki | created 2026-09-30

### duntaegi / JLPT-N1-voca — score 7 (overflow; prefer-JA vocab PWA)
- iPad PWA: 4,045 N1 words / 41 days; MC + flip cards + wrong-notebook (2-correct clear); device JA TTS; Excel merge keeps progress; backup/restore. No README product essay — Korean install notes + shipped SPA. | https://github.com/duntaegi/JLPT-N1-voca | created 2026-09-30

### jackson9413 / polyglot-pathforge — score 7 (overflow; roadmap·generated-plan)
- Local Flask+SQLite: paste learner brief → CEFR phase roadmap + immersion tactics + SRS waves + risk flags + 0–100 readiness (36 languages, no LLM). Planner, not daily tutor loop. | https://github.com/jackson9413/polyglot-pathforge | created 2026-09-30

### werzou8-oss / lyntopik — score 7 (overflow; prefer-KO graded essay corpus)
- Single-file static: TOPIK 大作文 news→精读→argument transfer corpus (ZH UI); localStorage. Sibling topik-essay-corpus. Content desk more than SRS app. | https://github.com/werzou8-oss/lyntopik | created 2026-09-30

### CarlosPuyana / kana-study — score 6 (overflow; prefer-JA thin desk)
- Angular web: kana/kanji/vocab/mazos/RUSH modules; localStorage+IndexedDB; GH Pages deploy. Thin README (module list only). | https://github.com/CarlosPuyana/kana-study | created 2026-09-30

### daferur-lang / speak-fluent — score 7 (overflow; EN speaking·FSRS — off prefer-L2)
- PWA: EN shadowing pitch-curves + spoken FSRS phrases + Gemini voice chat; IndexedDB; strong portable gates but **target L2 is English**. | https://github.com/daferur-lang/speak-fluent | created 2026-09-30

### Emil0001 / rinae-korean-learning-platform — score 6 (overflow; prefer-KO SaaS·courses gated)
- Full-stack Next.js KO platform (RU learners): exercises, vocab SRS, TOPIK tests, admin AI gen. Live site; **courses not publicly displayed yet**; account/Postgres. Watch when course content opens. | https://github.com/Emil0001/rinae-korean-learning-platform | created 2026-09-30

### yongseokmoh / japanese-kana-mastery — score 6 (overflow; prefer-JA kana SPA)
- Single HTML 五十音 smart-mode desk (KO chrome). No README; product is index.html. Thin vs kana-renshu/kana-run. | https://github.com/yongseokmoh/japanese-kana-mastery | created 2026-09-30

### ColtonKawamura / anki-kanji-notes — score 6 (overflow; JA Anki helper CLI)
- macOS CLI fills empty Immersion-deck Notes with Jisho on/kun for each kanji in Reading field; edits collection.anki2 directly (Anki closed). Tool, not tutor. | https://github.com/ColtonKawamura/anki-kanji-notes | created 2026-09-30

### 0xhillen / hanzi-stroke-video — score 6 (overflow; ZH stroke skill)
- Codex skill: one hanzi → fixed-layout stroke-order animation video. Generation tool, not learner loop. | https://github.com/0xhillen/hanzi-stroke-video | created 2026-09-30

### iruom / anki-popup — score 6 (overflow; Anki companion)
- Native macOS floating random-note companion (Vibrancy, click-audio). Study rhythm aid, L2-agnostic. | https://github.com/iruom/anki-popup | created 2026-09-30

### JaeUngJang / hangulpace — score 6 (overflow; prefer-KO typing)
- GH Pages Next build: Korean typing test for learners. README 404; built site only. | https://github.com/JaeUngJang/hangulpace | created 2026-09-30

## Promote-watch
- **NEW watch:** stagfoo/jlptbenkyo · ahmadasrizalmi/Japanese-Reader-AI · mansourvery-hub/anki-chinese-template (KEEP)
- **NEW watch:** HadrienT/live-subs, Eason-Xi/pocket-nihongo, Eason-Xi/pocket-korean, JobsKits/JpKanji, angelengineer/japanese-web, sakurakojapanesetutor0317/kana-renshu, sameerakmal/MedDeutsch
- **NEW watch:** Emil0001/rinae-korean-learning-platform — recheck when `/courses` public
- **NEW watch:** BoldKenobi/japanese_study_app — title-only README; large TS tree; recheck when README lands
- **NEW watch:** Rafacv23/kaku — Bun SRS/kana/grammar claim, short README
- **NEW watch:** ojs-fisher/deutsch-lernen — size-1 desktop DE practice claim; README 404
- **NEW watch:** youme930/-cheoeum-gana- — confusable kana handwriting compare (SPA shell → src/)
- Prior packet 48 KEEPs stay SEEN; do not re-keep.

## Bounce (library / spam / thin / off-lane)
- Thapa Sensei JFT marketing mocks (Basic-Mock-Test-Set-2, Basic-Full-Mock-Test)
- Japan tourism / trip / rail-pass / sushi restaurant / ramen map / Kanazawa tips / fuel-me-japan
- Game/localization: wow-forever-japanese, Chill-With-You voice mod, Outbreak-Tracker, Idoly-style, kanab kids game
- Anki name-spam / FakeAnki / NiseAnki / Ankita portfolios / interview-adjacent
- STEM/ML “learning”, ComfyUI TTS, LLM microcopy, wine Anki, Hebrew Anki, KelimeDefteri EN vocab
- jzuluagaga/hanziapp — classroom Workshop-1 folder only
- nuriqbal10 Irodori kanji worksheets (PDF practice sheets, not interactive tutor)
- nam9514 hangul→katakana converter; ebahnx hangul-name-lab/drag toys; MANGOCURLY fly-hangul connectome viz
- Dev-moe TOPIKII-App / Level-3-premium siblings of already-SEEN pro-v3.0
- ishidaken0108 youtube-anki-dictation — EN immersion→Anki (off prefer; Gemini mining)
- KEQingFeng/weread-guizang — WeRead→Anki tooling (ZH reading export, not L2 tutor)
- parse-nip/milc-deck-agent — Anki occlusion for Cursor agents (tooling)
- sameerbajaj/ankiweb-cli — generic AnkiWeb CLI
- sohamshewani Leitner Java lib / flashcard-generator — generic SRS library
- Mario Esteban size huge but Genki quiz without durable SRS → overflow not bounce
- Flutter/empty shells; size-0 stubs (kanji-zamurai, sakura-japanese-learning, My-Hanzi, TSPC-Chinese-Learning-App, anuyesugi Kanji)

## Fetch failures (no README / empty / rate-limit)
- ojs-fisher/deutsch-lernen, jzuluagaga/hanziapp, truongvinh-dev-fullstack/korean-learning, 190408nguyenan-ops/Hanzi_flashcard, vup1120/chinese_learning_for_kids, chanchan9741-hash/JLPT, MrWengKB/HanziQuery, anjalapriandhip-glitch/Kanji-N4, wataamee777/nandoku-kanji, iibiibah/hiragana-battle, shivamsrivastav0504-maker/N5-Japanese-Learning-Tool, apu-japanese-learning/apu-japanese-tools, yoshsemail-glitch/sakura-japanese-learning — README 404
- Recovered via index.html: JaeUngJang/hangulpace, werzou8-oss/lyntopik, yongseokmoh/japanese-kana-mastery, youme930/-cheoeum-gana-, MarioEstebanMateo (shell), BoldKenobi (shell), KuroNekoLi/personal-learning-app-pages
- ahmadasrizalmi/Japanese-Reader-AI search size=0 but full README+releases present
- duntaegi/JLPT-N1-voca search size=0 but Korean install README present

## Banked (learning lane)
- https://github.com/stagfoo/jlptbenkyo → raw/learning/2026-09-30-stagfoo-jlpt-benkyo-offline-android-n5-n3.md
- https://github.com/ahmadasrizalmi/Japanese-Reader-AI → raw/learning/2026-09-30-ahmadasrizalmi-komorebi-reader-japanese-reader-ai-offline.md
- https://github.com/mansourvery-hub/anki-chinese-template → raw/learning/2026-09-30-mansourvery-hub-chinese-anki-note-template-sentence-mining.md

KEEP_COUNT=3
alert=no
