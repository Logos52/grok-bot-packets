# Field education hunt — 2026-09-27 (Asia/Taipei cron; box America/New_York Sat Sep 26 evening ET)

Window: `created:>2026-09-25` / `created:2026-09-26` / `created:2026-09-27` (GitHub MCP `cursor-github` search_repositories; split OR queries ≤5 ops; raw.githubusercontent.com README fetches → `/workspace/field/edu0927/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (`seen-gh-repos-lower.txt` ~336 + prompt list). Do NOT re-keep yesterday: ishmum123/japanese, workwithlucas/frenchteacher, ishmum123/korean. Overflow already SEEN: equwal/subread-anki, Carlos09Or/Final-Mandarin, met-tk/Tampo, Nemuidere/LyricDeck, topherhunt/ditto, rachelw320/language_learning_app, DavisGoglin/spectrogram, giovannipivatoo/memoro, bishoppawn1/spanish-practicing, MathewDMoore/habla-ecuador, eranoix/kids-study-app, henwill8/AnkiCardUnlock, ishmum123/vocab-engine. Prior: yhyy135/babello, pronnmark/frenchfries, Miso-Soup98/kotoba-study, natha-ui/hanbit, …

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. kioxr / D-Learn — score 10 · [education·tutor-loop·immersion·reveal-schedule·teach-once·prefer-DE]
- one-line packet shape: **macOS Electron** screen-aware German companion: hold hotkey → screenshot of whatever's on screen (Nicos Weg / PDF / site) + voice Q → Groq Whisper STT + vision model answers by **macOS offline voices** (DE voice for German, EN/AR for explanations) in a live overlay; every asked word → **FSRS** vocab deck (gender colour, cloze from screen sentence, memory hooks). Full **A1→B2 course** beside the helper: Today plan (reviews / new words / grammar / speaking / listening / input), **48 grammar topics**, Goethe-style writing corrections, spoken role-plays, dictation, mistake notebook, core vocab by Goethe theme, 8-month B2 roadmap. 100% free-tier (Groq) + system voices. | https://github.com/kioxr/D-Learn | created 2026-09-26
- Distinct-from: syedmuhammadtaha55/German_Vocab (browser A1 904-word drill studio, no screen vision) — this is **screen-context tutor + full CEFR course**. Distinct from workwithlucas/frenchteacher (FR voice PWA) — DE + vision overlay + FSRS from screen mining. Distinct from DoDoDeutsch prior watch.

### 2. crsolver / kanji-battle — score 10 · [education·teach-once·reveal-schedule·prefer-JA]
- one-line: Browser **pixel-art** kanji recognition RPG: JLPT **N5→N1** worlds, chapters of 20; study 5 → type-meaning test → final round; **typo-tolerant** answers; reverse 4-robot pick; **Daily Review** SRS (overdue/leeches first); chapter pass gates (80% first-try + 70% remembered across 2 encounters); **boss duels** for confused pairs (6-in-a-row retires mixup); XP/streak/stats/collection; IndexedDB + export/import; offline WebAudio + procedural art; **2,495** kanji from KanaDojo (AGPL). Vitest'd rules. | https://github.com/crsolver/kanji-battle | created 2026-09-26
- Distinct-from: ishmum123/japanese (A1–B1 frequency vocab + graded passages + kana/kanji stages) — this is **kanji-recognition game with mixup-boss SRS**, not vocab/passages. Distinct from met-tk/Tampo (WinUI FSRS vocab desk).

### 3. cuongtq17 / hanyu — score 9 · [education·teach-once·immersion·i-plus-one·generated-input·prefer-ZH]
- one-line: Static **Hànyǔ Lab** — Mandarin by AJ Hoge **Effortless English**: lesson = album of unlock tracks (main dialogue → phrases/shadow → mini-story Q&A → POV retell → grammar spotlight *after* stories → practice drills → hands-free listen-again); **ears first** (no transcript until several listens); deep learning (target 7 listening days); phrases not isolated words; three-direction SRS phrase shelf; Edge/MiniMax audio pipeline (`tools/voice.py`); first album **你好，邻居！**; method + adding-a-lesson docs; local progress/export. Honest: only first album shipped so far. | https://github.com/cuongtq17/hanyu | created 2026-09-26
- Distinct-from: Carlos09Or/Final-Mandarin (HSK1 recognition blocks) — this is **audio-led Effortless English album curriculum**. Distinct from Anna023000/chinese-by-ear (Lesson-01 static review page).

## Overflow (≥6, below top-3 SETUP slots)

### syedmuhammadtaha55 / German_Vocab (Taha's Lehrer) — score 9 (overflow; prefer-DE A1 desk)
- 904 A1 words (StudyGerman.io ∩ Goethe Start Deutsch 1): Today plan, SM-2 Review, drills (der/die/das rules, Hear it, Dictation with äöüß, Say it + Shadow speech-recog, Fill gap, Build sentence V2); offline browser; article/case tables. Prefer-DE but overlaps D-Learn lane — desk-only no screen mining. | https://github.com/syedmuhammadtaha55/German_Vocab | created 2026-09-26

### cointugboat8211 / deutsch-ueben — score 8 (overflow; prefer-DE PWA; no README)
- PWA: placement → lessons path (units with items+sentences → generated exercises + speech), Daily Review, Conversation, Reading, AI Tutor; ~28KB lessons-data. Prefer-DE; thinner docs than German_Vocab / D-Learn. | https://github.com/cointugboat8211/deutsch-ueben | created 2026-09-26

### EricWay1024 / book-watcher — score 8 (overflow; prefer-ZH immersion EPUB)
- `uv run` local library: EPUB → sentence-by-sentence neural TTS shown as subtitles; Mandarin+English per-sentence voice; Watch/Read modes share position; mark/copy/listen-from-here; pace learning; fullscreen tap zones. Prefer immersion reader twin under babello. | https://github.com/EricWay1024/book-watcher | created 2026-09-26

### soullovers2019-cloud / japanese-sensei-bot — score 8 (overflow; prefer-JA Telegram N5)
- Telegram Bun/TS sensei: JLPT N5 12 thematic lessons ×5 words; form→meaning→usage; bi-directional MC; progress/weak words/streak; pre-baked `knowledge/analyses.json` (no API for course); free-word parse cached; Google TTS. Meta UI Russian. | https://github.com/soullovers2019-cloud/japanese-sensei-bot | created 2026-09-26

### keenanallaf-blckarrw / rooted-arabic — score 8 (overflow; Levantine/MSA — off prefer-L2)
- Roots+pattern vocab, graded reading tap-gloss, Levantine neural audio (edge-tts bundled), SM-2, Script Lab, Claude Artifact chat (Pages copy sans chat). Twin of rachelw320 EA; Arabic not JA/ZH/DE/VI/KO/FR/ES prefer. | https://github.com/keenanallaf-blckarrw/rooted-arabic | created 2026-09-26

### umeshchhabra / japanese-learning — score 7 (overflow; prefer-JA Genki-L3 kana chapter)
- Static Pages Genki I Lesson 3 supplement: 200 Qs, 4 reading labs, 5 listening labs (normal/slow WAV), verb charts, PDF pack; kana-only; export/import progress. Single chapter. | https://github.com/umeshchhabra/japanese-learning | created 2026-09-26

### Xthnavas / cognado — score 7 (overflow; prefer-FR/IT from ES cognates; no README)
- Static cognate trainer: 109 IT + 109 FR words in pattern categories (-ción→-zione etc.) + false-friend traps; browser TTS; XP/streak/review. Prefer-ES bridge into FR. | https://github.com/Xthnavas/cognado | created 2026-09-26

### agregoire / italian-words — score 7 (overflow; Apple Books→Anki IT/FR miner)
- Mac CLI: Apple Books highlights → AnkiConnect cards (sentence front; FR gloss + dict back; reversed cloze); Claude for enrichment; dedupe. Strong immersion miner; IT off prefer; Mac+AnkiConnect. | https://github.com/agregoire/italian-words | created 2026-09-26

### ericwwng / oshiete — score 7 (overflow; prefer-JA Chrome sentence tutor)
- MV3: select JA → floating popup / side panel → OpenAI gpt-4o-mini grammar breakdown; key local. Tutor-loop utility, no curriculum. | https://github.com/ericwwng/oshiete | created 2026-09-26

### Jcraxker / learn-speak — score 7 (overflow; prefer-ES/EN voice tutor hackathon MVP)
- Expo: EN↔ES level+topic+timer session; Gemini + expo-speech + mic; RevenueCat. Near frenchteacher; 6h hackathon WIP. | https://github.com/Jcraxker/learn-speak | created 2026-09-26

### liviaaguiarcc / HanLevel — score 7 (overflow; prefer-KO i+1 leveler; no README)
- Kiwi tokenize → Korean Learners' Dictionary grade (초/중/고) scores for text difficulty. Vocab component only so far (grammar markers excluded for later). Portable i+1 gate; incomplete product. | https://github.com/liviaaguiarcc/HanLevel | created 2026-09-26

### Anna023000 / chinese-by-ear — score 6 (overflow; prefer-ZH Lesson-01 static)
- Static Pages Lesson 01: vocab/grammar/practice; hide pinyin/EN; click-reveal answers; local audio file pick + zh-CN TTS. Thin single-lesson. | https://github.com/Anna023000/chinese-by-ear | created 2026-09-26

### sazardev / omarchy-english-toolkit — score 7 (overflow; offline EN Arch stack — off prefer-L2)
- Offline EN: LTeX grammar, sdcv dict, Lute reader+TTS, Ollama conversation, 2141 Anki grammar notes. Strong stack; EN not prefer. | https://github.com/sazardev/omarchy-english-toolkit | created 2026-09-26

### Krocosr / vocab — score 6 (overflow; self-hosted EN dict while reading)
- Docker: lookup → sqlite save with book tags → review cards; dictionaryapi.dev + Wiktionary. Generic L1/L2 shell. | https://github.com/Krocosr/vocab | created 2026-09-26

### reepiceep / greek-tutor — score 7 (overflow; Biblical Greek Mounce — off prefer-L2)
- Vite Mounce Basics ch4–18: FSRS-ish daily, flashcards, εἰμί/preposition drills, memory hooks. Strong mechanism; Ancient Greek niche. | https://github.com/reepiceep/greek-tutor | created 2026-09-26

## Promote-watch
- **NEW watch:** kioxr/D-Learn / crsolver/kanji-battle / cuongtq17/hanyu (KEEP)
- **NEW watch:** syedmuhammadtaha55/German_Vocab, cointugboat8211/deutsch-ueben, EricWay1024/book-watcher, soullovers2019-cloud/japanese-sensei-bot
- **NEW watch:** Xthnavas/cognado, liviaaguiarcc/HanLevel (promote when grammar component lands), umeshchhabra/japanese-learning
- **NEW watch:** WineQZX/japanese-conversation-coach (demo-rules prototype — recheck when real AI backend)
- Prior watches stay SEEN; do not re-keep yesterday packs.

## Bounce (library / spam / thin / off-lane)
- Flutter default README shells: Aissa-cmd/escargo ("new Flutter project")
- School/marketing sites: AnderwanSAM/optimum-french (TCF/TEF center site), SreekalaC/CoffeeWithMyFriend (static tutor promo)
- Study-hour trackers not L2 content: ochoa-emilia/deutsch-c1-plan (600h to C1 timer + Firebase)
- Programming tutorials / C-language-learning / Nextjs-Tutorial / Vulkan / STM32 / jenkins-tutorial
- Ankit*/Ankita* portfolios; SRS* content spam (mako104/srs*, wrightjulian24/srst, …)
- Generic flashcard shells: lllcr6/Flashcard-Study-Studio, adelson70/flashcardsapp, p-prakapienka/kartka, aryankeluskar/duo-lingo (iPhone Duo origami flashcards — not L2 curriculum)
- Medical/surgery/hardware flashcards; IELTS EN vocab dumps; Quizlet solvers (suicide4668/Dominate-Quizlet)
- Japan tourism / Korean BBQ / IPTV Deutschland / crypto jangteo / game patches
- Peer tutoring platforms / math tutors / Security+ flashcards / Power BI tutors
- dusxo012315-ai/english-tutor (EN personal app — off prefer; large README but EN)
- Loyal-Blue/russian-tutor (offline GGUF Russian — UI ready, native inference stub)
- piotrkukucharski/VocabCatcher (314b thin README)
- Rarukuu/korean-quiz (index.html only, 443b — empty shell)

## Fetch failures (no README / empty / rate-limit on dir list)
- Rarukuu/korean-quiz — no README; only tiny index.html
- Cathy-Niu/Chinese-Vocabulary-Flashcard---Book-8, Diwas37/hsk5-mock-exam, huyhung2412/hsktiengtrung, naconterde/hsktc — no README
- Yahai/rhythm-deutsch, justgyro/kanjidoku, DestinyGeorge/memori-k, preethatx-janna/AejuTutor, jahanvitiwariUX/Faux-ami-French-Game, muraokazu/jissen-kokugo-flashcard, tiagozero/Japanese, AmberEimlb/S2-french — no README
- cointugboat8211/deutsch-ueben, Xthnavas/cognado, liviaaguiarcc/HanLevel — no README; recovered via index.html / analyzer.py / data.js (saved under edu0927/)
- GitHub REST rate-limit hit once when listing deutsch-ueben/js/data via unauthenticated curl; recovered via raw.githubusercontent.com

SETUP_COUNT=3
alert=no
