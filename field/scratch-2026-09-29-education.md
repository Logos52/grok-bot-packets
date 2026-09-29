# Field education hunt — 2026-09-29 (Asia/Taipei cron; box America/New_York Mon Sep 28 evening ET)

Window: `created:>2026-09-27` / `created:2026-09-28` / `created:2026-09-29` (GitHub MCP `cursor-github` search_repositories; split OR queries ≤5 ops; raw.githubusercontent.com README/index fetches → `/workspace/field/edu0929/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (`seen-gh-repos-lower.txt` ~379→530 + prompt list). Do NOT re-keep yesterday packet 46: isa-aguilar/poligloti, t0rrentialrain/sentence-mining, NabiBukhsh-AI/lernbuch. Overflow already SEEN: Wildchiken/vocab-de, jonaylor89/Parlo, gaborkalmar83/bilingua-tutor, viola-delia/taiwan-mandarin-app, t0rrentialrain/cik-content-pipeline, pedroaz/call-nina, iqingyoung/openlango, Varsha0714/startklar-deutsch, shps961421-lang/n2-learning, amuraru/deutsch, TomCardeLo/kana-practice, lstux/Slovingo-de-fr, OMKAR140706/DeutschMate, Ahsansabir143/goethe-coach, Therockasocka842/language-learning-platform, iqingyoung/openlango, and earlier seen list.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. Laraib2004 / learnmandarin (Shuō Ba 说吧) — score 10 · [education·tutor-loop·teach-once·generated-input·prefer-ZH]
- one-line packet shape: **Speaking-first** offline Mandarin PWA (no account/server): **Tone Lab** (minimal-pair ear + sandhi rules) → **FSRS-5** sentence cards (250) with recall-probability Library → **pattern drills** (32 grammar frames × 217 random slot fills, target &lt;4s conversational latency) → **two-way conversations** (ZH→EN listen then EN→ZH produce; partner audio-first, Chinese hidden until commit; 10 dialogues / 81 turns). Characters optional (39 components / 69 hanzi on own FSRS). Speech scoring character-by-character via Mandarin recogniser. Static files + service worker; 103 tests; iPhone-first layout. | https://github.com/Laraib2004/learnmandarin | created 2026-09-28
- Distinct-from: viola-delia/taiwan-mandarin-app (TOCFL trad/zhuyin PWA reading+practice) — this is **Mainland speaking production + FSRS sentences**. Distinct from johnhodgson140-ai/mandarin-learning (personal AnkiConnect+Azure Shuō) — self-contained course, no Mac/Anki required. Distinct from cuongtq17/hanyu (audio albums) — interactive drills + speech.

### 2. Takoodachi / kotodama — score 9 · [education·SRS·prefer-JA]
- one-line: Dark minimal **Japanese practice PWA** (Next.js): mix hiragana/katakana rows, JLPT kanji (524 across N5–N1), words/phrases/sentences; MC / reading / typing; **Leitner SRS** boxes 0–5; example sentence per word/kanji (first-meet always shown); Ghost mode = 20 weakest; study heatmap + mastery radar; offline after first visit (SW caches library + font slices); device TTS; Vitest content-integrity; live https://takoodachi.github.io/kotodama/. | https://github.com/Takoodachi/kotodama | created 2026-09-28
- Distinct-from: TomCardeLo/kana-practice (ES→kana phonetic starter) — full kana+kanji+vocab+sentence desk. Distinct from shps961421-lang/n2-learning (personal N2 Claude sprint) — general JLPT practice PWA with offline. Distinct from Isuri N4 trainer (overflow N4-only static) — broader levels + PWA.

### 3. kalaiguna / deutsch-adk-coach — score 9 · [education·tutor-loop·teach-once·prefer-DE]
- one-line: **Voice-first German B2 coach** on Telegram (Cloud Run + Gemini multimodal): send .ogg voice notes — coach hears directly (no paste-to-IDE). Per turn: categorize into **11 fixed mistake categories**, mandatory **B2-Umformulierung**, **one question per turn** (teach-once). Session vocab/mistakes/stats → Firestore on `/finish`. Roadmap: ADK multi-agent (conversation/quiz/grammar/vocab/exam). MIT; CLI test without Telegram; evolved from deutsch-genai-coach / deutsch-lernpaket. | https://github.com/kalaiguna/deutsch-adk-coach | created 2026-09-28
- Distinct-from: isa-aguilar/poligloti (local multi-L2 speaking desk ≤3 corrections) — this is **always-on Telegram B2 voice with telemetry**. Distinct from pedroaz/call-nina (Codex Electron DE desk) — phone voice notes, no desktop AI required. Distinct from NabiBukhsh-AI/lernbuch (visual A1–B1 curriculum) — conversation coach, not lesson book.

## Overflow (≥6, below top-3 SETUP slots)

### annabelleonardi / lyric-mandarin — score 9 (overflow; prefer-ZH immersion songs)
- Chrome MV3: YouTube/NetEase Chinese songs → synced lyrics, **HSK 1–9 colour grading**, click-lookup pinyin+def, AI cultural insights (optional key), flashcard deck → **Anki CSV export**. Sample content works without API. | https://github.com/annabelleonardi/lyric-mandarin | created 2026-09-28

### johnhodgson140-ai / mandarin-learning (Shuō 说) — score 8 (overflow; prefer-ZH AnkiConnect speak)
- Personal Mandarin speaking+reading PWA (GitHub Pages): Azure Speech pronunciation, **AnkiConnect** Mac sync + AnkiMobile file import/export, daily stories from deck words, Firebase progress. Strong runner but personal-deck / Azure setup vs Shuō Ba self-contained course. | https://github.com/johnhodgson140-ai/mandarin-learning | created 2026-09-28

### julianlee314-hue / ziyuan — score 8 (overflow; prefer-ZH Taiwan zhuyin garden)
- 字園 Zìyuán: Traditional Taiwan Mandarin character garden — **Zhuyin-first, not HSK**; local SRS garden / watering quiz / lesson tray; Pages seed + frozen 1,200 plot ledger; EN↔中文 chrome. Live https://julianlee314-hue.github.io/ziyuan/. Distinct from taiwan-mandarin-app (full TOCFL PWA) — character-garden metaphor + zhuyin primacy. | https://github.com/julianlee314-hue/ziyuan | created 2026-09-28

### revucio24-web / yalla-deutsch — score 8 (overflow; prefer-DE for Arabic L1)
- Situation-first DE A1/A2 web+PWA for Arabic speakers (RTL): 5 city areas · 30 missions · 180 words · 8 task types; XP/stars/word-mastery 1–5 + due-based review; device TTS; localStorage only; content generated/validated by Python script + Vitest invariants. | https://github.com/revucio24-web/yalla-deutsch | created 2026-09-28

### humble26 / bili-fav-review — score 8 (overflow; prefer-ZH immersion→SRS)
- Bilibili favourites → subtitle pull → LLM cards → **SM-2** active-recall review → Anki `.apkg` export; GUI + CLI; Windows installers; demo mode without login. Portable immersion+SRS (ZH media), not a curriculum. | https://github.com/humble26/bili-fav-review | created 2026-09-28

### khodiboev / souldehangugobot — score 8 (overflow; prefer-KO Seoul Korean Telegram)
- Telegram Seoul Korean **1A–6B** companion (Uzbek UI): 12 books · 133 units · 1942 vocab · 442 grammar · 267 dialogues; **reveal-schedule** spoilers for translations; JSON lessons, no AI/DB; Docker. Strong content pack; L1 is Uzbek. | https://github.com/khodiboev/souldehangugobot | created 2026-09-28

### janosszaboaipm-design / goethecoach-claude-skill — score 8 (overflow; prefer-DE exam tutor skill)
- Free Claude skill: Goethe A1–C2 Lesen/Schreiben/Sprechen tasks + 4-criteria scoring + micro-drills + L1 interference files (incl. VI/AR). No Hören (chat). Product bridge to goethecoach.de. Portable teach-once exam loop. | https://github.com/janosszaboaipm-design/goethecoach-claude-skill | created 2026-09-28

### Isuri-Nethmini / N4-Q4-Kanji-Vocabulary-Trainer — score 7 (overflow; prefer-JA N4 desk)
- Static local N4/NAT Q4 trainer: 2049 items; smart drill + reading/kanji/meaning/type; Match/Sprint games; timed exam; **exam-date interval ladder**; browser progress. | https://github.com/Isuri-Nethmini/N4-Q4-Kanji-Vocabulary-Trainer | created 2026-09-28

### AnastasiaYap / yybijika — score 7 (overflow; prefer-ZH notes→Android)
- 盈盈笔记卡: personal notes PDF → content.db pipeline → Kotlin Compose Android; per-skill mastery; registry-driven exercises; enrich/review staging for gloss/example/pinyin. Portable content/progress split. | https://github.com/AnastasiaYap/yybijika | created 2026-09-28

### Guidufox / anki-apkg-builder — score 7 (overflow; prefer-JA immersion Anki tool)
- Local browser Immersion Deck Builder (Python+SQLite): JA cards → Recognition+Recall → real `.apkg` via genanki; offline; optional local model. Editor tool, not tutor loop. | https://github.com/Guidufox/anki-apkg-builder | created 2026-09-28

### Maditor / Japo — score 7 (overflow; prefer-JA→VI immersion overlay)
- Windows real-time JA Whisper ASR → VI (+romaji/EN) sidebar subs from system audio; Cloudflare/Gemini translation. Immersion companion for VI learners of JA. | https://github.com/Maditor/Japo | created 2026-09-28

### sleepman305 / daily-vocab — score 7 (overflow; prefer-ZH/VI Leitner PWA)
- Offline PWA: EN–VI + HSK 1–9 ZH–VI (85k EN / 11k HSK bundled); Leitner boxes; daily goal/streak. Live Pages. Vocab desk not speaking. | https://github.com/sleepman305/daily-vocab | created 2026-09-28

### wiltobuild / RuneSpeak — score 7 (overflow; prefer-ES game tutor)
- Spanish dungeon crawler: 52 beginner challenges with explanations; seeded encounters; local autosave; TTS. Fun thin curriculum. | https://github.com/wiltobuild/RuneSpeak | created 2026-09-28

### popam3143-prog / LearnDeutsch (Wortgarten) — score 7 (overflow; prefer-DE A1 flash)
- Plain HTML Wortgarten: 256 DE vocab cards (1.1/1.2 lessons), article checking, picture clues, missed review, themes; no build. | https://github.com/popam3143-prog/LearnDeutsch | created 2026-09-28

### 4z54kzrtpm-design / b2-deutsch-quest — score 7 (overflow; prefer-DE B2 PWA)
- Mobile PWA: B2 vocab/Redemittel, sentence writing vs model, Sprechen with browser de-DE speech recognition + self-check (no AI grammar grade). | https://github.com/4z54kzrtpm-design/b2-deutsch-quest | created 2026-09-28

### jyleong / mandarin-srs — score 6 (overflow; prefer-ZH TUI)
- Rust ratatui TUI: see 汉字 → type English → grade; HSK 1–4 decks; local JSON progress. Thin but clean reveal-schedule. | https://github.com/jyleong/mandarin-srs | created 2026-09-28

### jmacaday0923 / benkyo — score 6 (overflow; prefer-JA foundation)
- Next.js JLPT SRS foundation (Postgres SM-2, N5 seed, EN/JA i18n, CI). Phase 1 complete — product thin until later phases. | https://github.com/jmacaday0923/benkyo | created 2026-09-28

### calinrus-dev / kanjizen-showcase — score 6 (overflow; prefer-JA kana gesture)
- Expo/RN showcase: hiragana + MECA recall + Flick gesture; open romaji evaluator + tests. Full SRS path still private. | https://github.com/calinrus-dev/kanjizen-showcase | created 2026-09-28

### wy2627962897 / diandu-english — score 7 (overflow; EN immersion harness — off prefer-L2)
- Obsidian + local Kokoro TTS + AI card-maker → Anki with audio. Strong portable gates; target L2 is English. | https://github.com/wy2627962897/diandu-english | created 2026-09-28

### Oletol / CEFR_Text_Checker — score 6 (overflow; EN graded-input grader)
- Offline browser CEFR-J/Octanove EN text leveler for teachers (vocab/sentence/grammar dims + adapt advice). EN focus. | https://github.com/Oletol/CEFR_Text_Checker | created 2026-09-28

### sassamahha / studyriver-worksheet — score 6 (overflow; JA worksheet Claude skill)
- Claude/ChatGPT skill: printable A4 kana/kanji tracing + quizzes from chat. Family/school worksheets, not full tutor. | https://github.com/sassamahha/studyriver-worksheet | created 2026-09-28

### uranbekanarbaev / free-hsk-3.0-mock-tests — score 6 (overflow; prefer-ZH exam packs)
- Organised official-sample HSK 3.0 PDF+MP3 packs by level with start.html. Content redistribution of samples + marketing to hsk-tutor.com — useful but library-ish. | https://github.com/uranbekanarbaev/free-hsk-3.0-mock-tests | created 2026-09-28

## Promote-watch
- **NEW watch:** Laraib2004/learnmandarin · Takoodachi/kotodama · kalaiguna/deutsch-adk-coach (KEEP)
- **NEW watch:** annabelleonardi/lyric-mandarin, johnhodgson140-ai/mandarin-learning, julianlee314-hue/ziyuan, revucio24-web/yalla-deutsch
- **NEW watch:** humble26/bili-fav-review, khodiboev/souldehangugobot, janosszaboaipm-design/goethecoach-claude-skill
- **NEW watch:** LucasL05/NPlusOne_JapaneseInContext — notes claim Anki + NHK Easy + Kuromoji n+1 Android tool; repo is tracer-bullet poc (`poc/Main.kt` stub, README title-only) — **recheck when UI/matching land**
- **NEW watch:** SilentAuroras/VocabLens — description ZH/JA article HSK/JLPT analyzer; **README-only stub (91b), no code yet**
- **NEW watch:** pillared/hanzi-strokes, krouis/kansei, tarikdemiroren/kami-tori-grammar, FakeForest/tcf-canada-study — no/404 README this pass
- Prior packet 46 KEEPs stay SEEN; do not re-keep.

## Bounce (library / spam / thin / off-lane)
- HSK*/hsk{aa,…}* and `content`-only JLPT stubs (end3waste/jlptj, rizskhiye22-png/jlpt, PhucBigData/hsk-master, tbtvietnam-hsk/hsk3-luyentap, …)
- Goethe/DE appointment, IPTV “deutsche TV”, Deutschebank.github.io, Deutschland RP / Exitgame-Deutsch
- Unlocked piracy mirrors (Homicipher / Zkanji / Grammatica Full Version Unlocked)
- Game translations (gen1recomp ES); programming tutors (tutor-vibe-coding); EN CEFR prediction ML; sign-language / NMT revival
- Anki tooling spam (spotify-to-anki, nyc-transit-anki, anki-typst, markdown-to-anki, BCM lecture unsuspender) without L2 curriculum
- NanashiAngsnake/japanese-learning — grammar SRS showcase **without proprietary dataset**; Stripe paywall; ARR license
- Ngochung1772k4/hugmo — GitHub desc said TOPIK/Korean; README is generic Quizlet-clone (VI) → bounce mismatch/thin
- kimjusnu/looks-like-korean — KO prose AI-detection metrics, not learner product
- AtsushiSakai/Enoki — on-device JA IME, not L2 tutor
- monstorjohan-png/lughati — Arabic platform scaffold; noureldinfayed/fliessenddeutsch303-art — academy **management** SaaS
- Flutter/empty shells; Duolingo-like empty; talkabee.com empty; greek_anki off prefer-L2
- alibarati613/german-vocab-quiz (62b), saidridaoui/deutschLernen (19b), amaroki (27b), Arwanasser78/fsp-apotheker (79b), isharathoria/japanese-n4-roadmap (131b title)

## Fetch failures (no README / empty / rate-limit)
- FakeForest/tcf-canada-study, krouis/kansei, tarikdemiroren/kami-tori-grammar, pillared/hanzi-strokes, trickster-2005/Deutsch-Learning-Tool, khaled3433/DeutschA1, atallaramy/Deutsch-lernen, DeveloperCameron/spanish-flashcards, crazyblockswin/talkabee.com, learntodosomething/Duolingo-like-language-learning-project, cju21c/jlpt-n4-app, TheAnswer27/Japanese-Learning, dmrock/deutscherl — no README (404)
- Recovered via index.html: july31st-star/kanji, eeshanoor/deutsch, shannenkhin/languages, Nero1100/jlpt-grammar, okckj0406-cloud/learn-korean-app, ra2781682-commits/DeutschB2, amclarence-ops/Kanji-Flashcards → edu0929/*-index.html (thin/game/content; bounce or watch)
- LucasL05/NPlusOne_JapaneseInContext — README title-only (27b); notes+poc fetched instead
- SilentAuroras/VocabLens — README stub only (no other files)

SETUP_COUNT=3
alert=no
