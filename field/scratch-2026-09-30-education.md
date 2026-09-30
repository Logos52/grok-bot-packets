# Field education hunt — 2026-09-30 (Asia/Taipei cron; box America/New_York Tue Sep 29 evening ET)

Window: `created:>2026-09-28` / `created:2026-09-29` / `created:2026-09-30` (GitHub MCP `cursor-github` search_repositories; split OR queries ≤5 ops; raw.githubusercontent.com README/index fetches → `/workspace/field/edu0930/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (`seen-gh-repos-lower.txt` 262→307 + prompt list). Do NOT re-keep yesterday packet 47: Laraib2004/learnmandarin, Takoodachi/kotodama, kalaiguna/deutsch-adk-coach. Overflow already SEEN: annabelleonardi/lyric-mandarin, johnhodgson140-ai/mandarin-learning, julianlee314-hue/ziyuan, revucio24-web/yalla-deutsch, humble26/bili-fav-review, khodiboev/souldehangugobot, janosszaboaipm-design/goethecoach-claude-skill, Isuri-Nethmini/N4-Q4-Kanji-Vocabulary-Trainer, and earlier seen list.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. ttiyana / korean-fast-track — score 10 · [education·SRS·immersion·i-plus-one·generated-input·prefer-KO]
- one-line packet shape: **Frequency-first Korean** web app (Vite+React 19): **FSRS-6** review (read/listen/EN→KO card modes, keyboard grades) + **Hangul Lab** (jamo audio, 초성/중성/종성 builder, 8 받침 sound-change rules, timed drill) + **10 situation dialogues** (café/taxi/pharmacy… shadow or hide-your-lines) + **drama lines** (~110 반말↔polite twins) + **song-Korean rules** + **Decoder** (paste subtitle/lyric → tokenize/romanise/speech-level/coverage; unknowns drop into deck). ~960 items (424 core + 39 grammar + 150 subtitle-glue); localStorage first, optional Netlify Blobs sync code (no account/PII); device `ko-KR` TTS. | https://github.com/ttiyana/korean-fast-track | created 2026-09-29
- Distinct-from: khodiboev/souldehangugobot (Telegram Seoul Korean 1A–6B content pack, Uzbek UI) — this is **frequency+subtitle ladder + real FSRS-6 + situations/drama/songs in one desk**. Distinct from uminrae/korean-flashcards (thin flash) — full method stack with Decoder mining.

### 2. jarod85 / Chinese-Learning-App-Lock-Phone-Samsung (HanziLock · 汉字锁) — score 9 · [education·human-gate·tutor-loop·SRS·prefer-ZH]
- one-line: **Android Mandarin practice gate** (Samsung S24 FE–tuned Accessibility lock): at scheduled resets, other apps stay closed until you clear *N* words — each word needs **say it** (speech/tones or typed pinyin) → **English meaning** → **use in a sentence** (Claude grades online; offline = rebuild example from tiles). Misses logged as losses + correct answer with audio; **Leitner** SRS (misses back in minutes → 75-day fade); bundled CC-CEDICT (~120k) + Pleco import; calls/alarms/priority email keep working; Master PIN skip. | https://github.com/jarod85/Chinese-Learning-App-Lock-Phone-Samsung | created 2026-09-29
- Distinct-from: Laraib2004/learnmandarin (self-contained speaking PWA course) — this is **phone-level human-gate + three-step production**. Distinct from johnhodgson140-ai/mandarin-learning (AnkiConnect/Azure speak desk) — lock-screen session, not desktop Anki.

### 3. RudyBoe / kanji-trainer — score 9 · [education·reveal-schedule·SRS·prefer-JA]
- one-line: Phone-first **kanji retention via vocabulary graph** (live https://rudyboe.github.io/kanji-trainer/): see word in kanji → reveal per-kanji reading-in-this-word (rendaku/gemination aware) + meaning → Missed pile or move on; **tap any kanji** to jump to next word preferring **same reading** → other reading → N+1 link word. 2,691 N5–N3 words + 1,215 N2 links (JMdict/KANJIDIC); light points/streak (not Anki replacement); **+ Anki** TSV export; local-only progress; home-screen installable. | https://github.com/RudyBoe/kanji-trainer | created 2026-09-29
- Distinct-from: Takoodachi/kotodama (Leitner kana/kanji/vocab PWA desk) — this is **same-reading graph navigation**, not box SRS. Distinct from Isuri N4 trainer (static N4 drill) — broader N5–N3 + reading-chain mechanic. Distinct from tkober/kanji-trainer (seen earlier, different owner).

## Overflow (≥6, below top-3 SETUP slots)

### Ellisdeeman / n5-vocab-quest — score 9 (overflow; prefer-JA JLPT vocab PWA)
- Single-file PWA (~450KB index.html): **JLPT N5–N1** vocab trainer with spaced repetition (Leitner signals), meaning/reading quizzes, kana levels, neural/device audio, service worker, open-anki-jlpt-decks data. No README (404); product evidence is the shipped SPA. | https://github.com/Ellisdeeman/n5-vocab-quest | created 2026-09-29

### Dev-moe-kyawaung / TOPIKII-Level-3-pro-v3.0 — score 9 (overflow; prefer-KO exam desk)
- Offline-first TOPIK II **Level 3** PWA (React+Vite+Zustand+IndexedDB): 100 grammar + 300+ vocab with **SM-2 SRS**, mock exam (listening/reading/writing), rule-based writing checker, shadowing recorder, study-plan from exam date, KO+Myanmar UI. Original practice sets (not official papers). Sibling v1/v2/pro variants same day — keep this fullest. | https://github.com/Dev-moe-kyawaung/TOPIKII-Level-3-pro-v3.0 | created 2026-09-29

### mobashirrahman / glossline-android — score 8 (overflow; prefer-DE immersion→Anki)
- Android companion to GlossLine Chrome: share/paste German article → read in DE → tap word for lemma/IPA/glosses/conj·decl tables (Kaikki) → save sense → **AnkiDroid** (parity-tested templates) or TSV. No full-page MT; article stays German. 105 unit tests. | https://github.com/mobashirrahman/glossline-android | created 2026-09-29

### yorkwahaha / kana-run — score 8 (overflow; prefer-JA SRS game)
- Godot 4.7 **五十音疾走**: SRS-weighted kana parkour (romaji↔kana, word blanks, reverse read, boss confusable sets); confusion-group distractors; dodge-to-retry; relics; 208-sound mastery map; Traditional Chinese chrome; fully procedural (no asset pack). Real SRS under a runner, not tourism. | https://github.com/yorkwahaha/kana-run | created 2026-09-29

### priyasureshgermany / deutsch-lernen — score 8 (overflow; prefer-DE exam+grammar)
- Offline Pages app: **telc A1 + B1** practice, 25 Gesprächsthemen (A1/A2/B1 versions + B1 models), **Wörter erkennen** (hand-tagged texts → type/case/role/TeKaMoLo colour + practice mode); device de-DE TTS; reveal-on-tap answers; SW update-by-button. Live https://priyasureshgermany.github.io/deutsch-lernen/. | https://github.com/priyasureshgermany/deutsch-lernen | created 2026-09-29

### conao3 / rust-overhear — score 8 (overflow; immersion sentence-mining)
- Linux Tauri **system-audio** dual-subtitle desk (PipeWire monitor → april-asr interim + whisper.cpp final → translate → ring-buffer replay → SQLite vocab → **Anki** with audio clip). Player/site-agnostic immersion mining. Heavy local stack (nix flake). | https://github.com/conao3/rust-overhear | created 2026-09-29

### SenseiIssei / ma — score 8 (overflow; human-gate·teach-once·SRS; JA decks bundled)
- iPhone Screen Time **Ma 間**: app gate → breath → Leitner exercises (8 types) → open or leave. Bundled hiragana / everyday JA / sentence-building (+ Zen/Stoicism/etc.) EN+DE; teach-before-quiz lessons (≤3 new). Portable human-gate, not a pure L2 curriculum. | https://github.com/SenseiIssei/ma | created 2026-09-29

### GeorgeAzma / ruby — score 7 (overflow; prefer-JA immersion overlay)
- Chrome MV: offline JMdict+kuromoji **English or furigana above every JA word** on any site; hover swap; no network. Strong immersion companion — **source published for reference only (no redistrib license)**. | https://github.com/GeorgeAzma/ruby | created 2026-09-29

### Yukitchy / dokkai-dojo — score 7 (overflow; prefer-JA graded reading packs)
- JLPT N5–N1 **読解** drill box: engine (furigana toggle, exam mode+timer, evidence highlight, print PDF) + `packs/` content + `rules/generate.md` + janome `check.py` level gates. Size 0 on search index but README+structure present; thin until packs grow. | https://github.com/Yukitchy/dokkai-dojo | created 2026-09-29

### mohammadrezwankhan / myfrenchbd-demo — score 7 (overflow; prefer-FR local-first)
- Local-first French for Bangla/EN readers: 6 A1–B1 lessons, practice activities, device progress, portable single-HTML build + SW tests. Honest demo limits (uncalibrated orientation, no AI assess). Live Pages demo. | https://github.com/mohammadrezwankhan/myfrenchbd-demo | created 2026-09-29

### mohammadrezwankhan / mygermanbd-demo — score 7 (overflow; prefer-DE local-first)
- Sibling: 12 beginner micro-lessons, 24 DE/EN/BN review cards with 1/3/7/14/30-day schedule, Germany Explorer research routes (explicitly unverified). Same local-first / demo-honest framing. | https://github.com/mohammadrezwankhan/mygermanbd-demo | created 2026-09-29

### Titus753 / Russisch-Tutor — score 7 (overflow; RU offline PWA — off prefer-L2)
- Слово за слово: offline RU PWA (cards SRS, MC, type-in, listening, alphabet); IndexedDB; CSP-hard; Playwright E2E. Portable gates strong; target L2 is Russian (not JA/ZH/DE/VI/KO/FR/ES). | https://github.com/Titus753/Russisch-Tutor | created 2026-09-29

### cchabanois / cartable — score 7 (overflow; lesson→Anki tool)
- Phone-camera lesson photos → vision AI drafts Anki cards (+ edge-tts audio) → review → Anki add-on or `.apkg`. Built for FR→ES vocab; human-gate review before deck. Tool, not tutor loop. | https://github.com/cchabanois/cartable | created 2026-09-29

### nathanschaumann / graded-readers — score 7 (overflow; EN graded + FR; generated-input scorer)
- 52 PD retellings at 5 levels with open Python scorer (sentence-length + Guiraud caps); 10 Very Hard have French; static site. EN-primary graded input + portable leveler. | https://github.com/nathanschaumann/graded-readers | created 2026-09-30

### jitensha2 / kid-a-nihongo — score 6 (overflow; prefer-JA school vocab)
- Plain HTML/JS school J1–J3 JA vocab+kanji PWA; localStorage; spreadsheet→data.js pipeline. Thin personal curriculum. | https://github.com/jitensha2/kid-a-nihongo | created 2026-09-29

## Promote-watch
- **NEW watch:** ttiyana/korean-fast-track · jarod85/Chinese-Learning-App-Lock-Phone-Samsung · RudyBoe/kanji-trainer (KEEP)
- **NEW watch:** Ellisdeeman/n5-vocab-quest, Dev-moe-kyawaung/TOPIKII-Level-3-pro-v3.0, mobashirrahman/glossline-android, yorkwahaha/kana-run
- **NEW watch:** priyasureshgermany/deutsch-lernen, conao3/rust-overhear, SenseiIssei/ma
- **NEW watch:** Yukitchy/dokkai-dojo — recheck when packs/`n5.json`… land more content
- **NEW watch:** alamin1408/hibiki — README title-only stub (195b); recheck when product lands
- **NEW watch:** shahinamani/french-learning-for-world — explicit “nothing usable yet” (plan/rules only)
- **NEW watch:** surla/kaerutype — README stub (127b)
- Prior packet 47 KEEPs stay SEEN; do not re-keep.

## Bounce (library / spam / thin / off-lane)
- HSK* content spam (`bmvxc4d127/hskvm`, `allenchad35/hskof`, `nerinshen7/hskhub`, MeowyPouncer/hsk-mailgun-…)
- Goethe/DE appointment, VPN-IP Germany/France/China, Deutsche IPTV, job-search Germany, BMW sentiment, wholesale energy
- Game translations / 汉化 / 한글화 (Idoly Pride, Idol Janshi, NS2 Spanish, VotV Korean patch)
- Programming/STEM tutors (dsa-tutor, systemsage, TutorialVR, sca26-qcsc-tutorial, academy-tutor-course)
- Interview Anki spam (tomaszs/*-interview-flashcards-free series)
- frobmann/Korean-APP — default create-next-app README only
- MarcelWeissgerberIT/FrenchSkool — Sachsen school multi-subject desk; FR is one sub-app, not L2 product
- hisea/stc — Simple Technical Chinese **writing style guide**, not learner product
- loverxy1205-hub/zhongbu — Chinese culture/divination reflection site, not L2
- Optcgbean/chinese-learning — kids Robux-reward Chinese fun desk (thin/gamified chores)
- Irin125a/chinese-app — RU UI personal 汉字 word list PWA (thin)
- ElineGames/lingo-fox — tiny PolyGlot Master DE+Thai flash HTML
- thapasensei/Basic-Mock-Test-Set-1 — JFT mock marketing site
- eas15022004/french-articles-lesson — SPA shell (root-only index, no built assets in tree for fetch)
- wachendnacht/fonoloteria — Spanish phoneme lottery mini-game
- alwayslistening86-pixel/edu-course-library — GCSE/degree **generic tutor** course pack (STEM/school, not L2)
- deutschmitsaleki-cmyk/DeutschmitsalekiB1-bot — empty README (24b)
- Flutter/empty shells; Japan tourism; sword-polish Notion; LearnSinhala size-0; nekocha VRChat JA size-0

## Fetch failures (no README / empty / rate-limit)
- AnmolKanwar/deutsch-drill. — README 404 (trailing-dot repo name awkward)
- rodeyuvraj2-svg/JPN-Academy, SandySuo0411/JLPTN2, NewfolderGames/nekocha, ChanuthDGamer/LearnSinhala, khaled3433/deutsch-lernen-A1 — README 404 / empty
- Ellisdeeman/n5-vocab-quest, Optcgbean/chinese-learning, ElineGames/lingo-fox, thapasensei/Basic-Mock-Test-Set-1, Irin125a/chinese-app, wachendnacht/fonoloteria — README missing; recovered via `index.html` → edu0930/*
- GitHub REST `api.github.com/repos/...` rate-limited mid-pass (403); created dates taken from earlier MCP search envelopes instead
- alamin1408/hibiki — README stub only (195b)

KEEP_COUNT=3
alert=no
