# Field education hunt — 2026-09-25 (Asia/Taipei cron; box America/New_York)

Window: created:2026-09-24 / created:2026-09-25 / created:>2026-09-23 (GitHub MCP `cursor-github` search_repositories — `user-GitHub-xai` unavailable this run; raw.githubusercontent.com README fetches → `/workspace/field/edu0925/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (176 repos + scratch-seen-urls). Do NOT re-keep yesterday: DeepanshuPal/context-deck, MarionLiew/anki-tutor, sezmow/habla. Yesterday overflow already SEEN: ChenZhuo4649/live-text-for-video, ljhoo24/kanji-furigana, tomvannuenen/mandarin-drill, kimsungchul7719/topik1-mock-test, xun1607/jpLearn, greggman/g-sho, persianoff/WordDrift, HotlineAHK/yomitan-fishaudio-bridge, chachaprince1/the-6k-extension, Drifter1997/dictionary-cli, GamosiDEV/Youtube2Anki, gustanas/llm-anki-convo, crlucenap/flashcards_fr. Prior keeps/watches stay SEEN.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. yhyy135 / babello — score 10 · [education·immersion·generated-input·i-plus-one·human-gate]
- one-line packet shape: Browser-only podcast immersion (rename from Duolistening 2.x): paste RSS → BYO OpenAI-compatible **transcription** (timestamped) + **text** models; lyric-style scroll with per-word highlight; translate only the segment you are listening to; **local Kuromoji furigana + POS coloring** (no key); writing coach returns L1 gloss / errors / native rewrite; IndexedDB bookshelf (keys/transcripts/audio stay in browser); 8 UI langs (ZH/EN/JA/KO/ES/FR/DE); Cloudflare Workers proxy (~200 LOC) only for CORS/range/redirect podcast bytes — page is static PWA. Honest limits: no chat history on Ask-AI; export JSON for backups; iOS audio-while-background caveat. | https://github.com/yhyy135/babello | created 2026-09-24
- Distinct-from: DeepanshuPal/context-deck (video/subtitle encounter-graph miner + AnkiConnect) — this is **podcast RSS → lyric listen + write**, not YouTube/Netflix mining. Distinct from RC-APC video assistant.

### 2. pronnmark / frenchfries — score 9 · [education·tutor-loop·reveal-schedule·teach-once·prefer-FR]
- one-line: Zero-build FR verb engine: **6 gears** (Présent / Passé composé / Imparfait / Futur / Conditionnel / Subjonctif) not 21 textbook tenses; chat-bubble drill (grey prompt → blank reply → tap reveal + Web Speech FR audio → swipe Again/Good); EN→FR flashcards with gear-disambiguated English prompts; FSRS-4.5 in `js/fsrs.js` (Again→3m relearning; Good→90% retention intervals); 15 verbs × 6 gears × 6 persons = 540 forms + 90 hand-written threads; `node tools/check-data.mjs` integrity gate; localStorage + SW PWA; `open index.html`. | https://github.com/pronnmark/frenchfries | created 2026-09-24
- Distinct-from: sezmow/habla (full ES curriculum + production-gated ladder) — this is **FR verb 6-gear teach-once + FSRS chat drills**, not multi-skill ES course. Distinct from crlucenap/flashcards_fr (thin FR desk, no spacing).

### 3. Miso-Soup98 / kotoba-study — score 9 · [education·reveal-schedule·immersion·teach-once·prefer-JA]
- one-line: JA textbook PWA: **622 N5–N2 grammar + 1,244 bilingual example sentences** (original numbering/pages preserved) + click-to-read TTS (Nanami/Keita MP3 samples + browser fallback) + vocab notebook + **ts-fsrs@5.4.2** (0.9 retention, ≤10 new/day) + 120-min daily plan + Tokyo-TZ diary; v0.3 TED/日刊精读 (150×2 private corpus: hover gloss → FSRS, A/B loop regions on original audio). Cloudflare D1/R2 sync; official deploy uses **ChatGPT Sites login** (fork needs own Site — local mock auth for `npm run dev`). Honest: N1/fill-in/listening cards not yet; TED OCR largely unchecked. | https://github.com/Miso-Soup98/kotoba-study | created 2026-09-24
- Distinct-from: seonhaesoo/nihongo-dojo / pandemonium0225/jlpt-quiz (quiz shells) — this is **full grammar library + FSRS + bilingual 点读 + optional TED精读**. Distinct from xun1607/jpLearn (generic Anki .apkg PWA).

## Overflow (≥6, below top-3 SETUP slots)

### natha-ui / hanbit — score 8 (overflow; prefer-KO graded + daily generated)
- Hangul→hanja by 훈음 → words → grammar → graded stories/tests; **daily trending words + stories** pipeline (KRDICT levels; optional Claude stories else KO Wikipedia openers); lock-screen word (Android wallpaper/widgets incl. Z Flip cover; iPhone Scriptable); web course is the app; APK wraps speech/widgets. Prefer-KO twin — **swap over #3** if KO daily-input preferred over JA textbook FSRS. | https://github.com/natha-ui/hanbit | created 2026-09-24
- Distinct-from: uminrae/korean-flashcards / kimsungchul7719/topik1-mock-test — this is **child-path Hangul/hanja + daily generated stories**, not TOPIK mocks.

### lukskrp / cobaltium-desktop — score 8 (overflow; CI desktop, Finnish-first)
- Electron+React local-first: 5-mode chat tutor, personal lexicon (17 rule engines + LangDex), SM-2 Anki-style review, interlinear EPUB reader, scenario packs (21 pairs, Finnish-based), MT→LLM gloss tiers, offline Piper/espeak + whisper.cpp STT; BYO OpenAI-compatible LLM. Win installer; Linux/mac build-from-source. Prefer-niche CI twin under babello slots. | https://github.com/lukskrp/cobaltium-desktop | created 2026-09-24
- Distinct-from: babello (podcast lyric web) — this is **desktop CI workspace + EPUB interlinear + lexicon SRS**.

### HanifCarroll / iina-language-learning-plugin (Neden) — score 8 (overflow; Mac IINA tutor-loop)
- Pre-release IINA plugin: select SRT/VTT phrase → pause → stream OpenAI-compatible explanation + follow-ups; replay cue without re-billing; Keychain keys; Swift HTTPS helper; `bun run release:check`. macOS/IINA beta only. Prefer immersion twin under context-deck. | https://github.com/HanifCarroll/iina-language-learning-plugin | created 2026-09-24
- Distinct-from: context-deck (browser YT/Netflix miner) — this is **native IINA sidebar tutor on local video+subs**.

### anzorein / rt-jpn-ocr — score 8 (overflow; JA game OCR→furigana tablet)
- PC screenshot (AHK) → Pi FastAPI OCR (tesseract/rapidocr/Groq) → fugashi+UniDic + jamdict → WS tablet UI with ruby furigana + Yomitan-style cards + IndexedDB favorites; Telegram photo bypass. Prefer-JA immersion hardware path — swap if game mining preferred. | https://github.com/anzorein/rt-jpn-ocr | created 2026-09-24
- Distinct-from: ChenZhuo4649/live-text-for-video (Mac Vision OCR→Yomitan DOM) — this is **Pi game OCR pipeline + tablet UI**, not Chrome Live Text.

### deserteaglemj / habla-spanish — score 8 (overflow; LatAm ES — NOT sezmow/habla)
- Account-free LatAm Spanish: 24 units A1–B1, dialogues/stories, roleplay turns, spaced review (supported≠independent), mission prepare/rehearse/adapt/debrief; Mac companion (Apple Intelligence Spanish coach + call translation via BlackHole). Live: https://habla-spanish-nu.vercel.app | https://github.com/deserteaglemj/habla-spanish | created 2026-09-24
- Distinct-from: **sezmow/habla** (yesterday KEEP; production-gated memory ladder + Claude partner) — same product name, **different author/repo**; this adds mission loop + Mac AI companion. Do not re-keep as #3 over sezmow without staff note.

### milksuger / MandarinLearnApp — score 7 (overflow; ZH for ID, early)
- Indonesian-first Mandarin PWA: exact-source audio only (no synth fallback), stylus writing, HSK 1–3 structural paths + 56 authored daily-life words; Cloudflare D1 accounts required. Prefer-ZH×ID but content still thin vs mandarin-drill. | https://github.com/milksuger/MandarinLearnApp | created 2026-09-24

### zhenke-dev / kindle-words — score 7 (overflow; Kindle+ESP32 FSRS-6)
- FSRS-6 in C on ESP32-S3 AP; Kindle Paperwhite browser client; 6550-word book; CSV export for param training. Clever hardware SRS, EN-vocab-on-Kindle not prefer-L2 curriculum. | https://github.com/zhenke-dev/kindle-words | created 2026-09-24

### brndnsmth / romlingo — score 7 (overflow; agent retro-game L2 framework)
- Codex/Claude Code framework: patch localized retro games into learn-through-play experiences (AGENTS.md guided setup). Meta tool for agents, not a shippable learner app. | https://github.com/brndnsmth/romlingo | created 2026-09-24

### eddieelorza / english-os — score 7 (overflow; EN local OS — off prefer-lang)
- Local FastAPI+React English OS: FSRS vocab, reading/podcast/writing/speaking, Personal English Model, Ollama/Anthropic. Strong runner but L2=English (off JA/ZH/KO/FR/ES prefer). | https://github.com/eddieelorza/english-os | created 2026-09-24

### acrot0 / anki-forge — score 6 (overflow; generic PDF→Anki CLI)
- BYO-key textbook→Anki CLI/UI with dry-run + duplicate skip. Solid miner, no L2 curriculum. | https://github.com/acrot0/anki-forge | created 2026-09-24

### Lanternko / karaoke-jp — score 6 (overflow; JA karaoke renderer)
- Mora wipe + furigana karaoke video generator (Mel-Band/GAME/fugashi). Singing practice tool, not SRS/curriculum runner. | https://github.com/Lanternko/karaoke-jp | created 2026-09-24

### greyindex / jitendex-yomitan-id — score 6 (overflow; JA–ID Yomitan dict library)
- Unofficial Jitendex Indonesian top-20% for Yomitan (GPT-drafted, unreviewed). Dict pack, not runner. | https://github.com/greyindex/jitendex-yomitan-id | created 2026-09-24

### ksyasuda / hachidori-docker — score 6 (overflow; headless Hachidori/Yomitan server)
- Docker Hachidori WASM + relay: import Yomitan ZIPs, WS share, no Chrome/Anki required. Infra for immersion stack. | https://github.com/ksyasuda/hachidori-docker | created 2026-09-24

### runnithan / claudex-learn — score 6 (overflow; Claude Code topic SRS — not L2-specific)
- Sources→cited lessons→path→SRS quiz inside Claude Code. Portable teach-once but generic (guitar/chess/Spanish), not named L2 curriculum. | https://github.com/runnithan/claudex-learn | created 2026-09-24

## Promote-watch continues (same URLs — do not re-keep)
- Candice-Bennett/Rabbit_Hole (SEEN — watch-only)
- Prior watches: manga_anki, typingchinese, language-learning-audio, simple-language-learning, hanzi-steps, jlpt-quiz, MMDL, shici-recite-app, jitendex-yomitan-zh, hanzi-flip-classroom, leap-framework, gillisandrew/ancci, babelgarden, equwal/subread-dictionary, ChenZhuo4649/live-text-for-video, ABakdi/sublight, jasonasknow-cloud/topik-news, Uncommon-lineofleastresistance5475/lexiglance, leonardtschora/yeswekanji
- **NEW watch:** rafaself/opennihongo (local-first JA platform — monorepo/Nx scaffold README only; revisit when learner loop ships)
- **NEW watch:** fumbleforce/tower-of-words (offline JA RPG commute study — thin README)
- **NEW watch:** Gustaf998/localspeech (privacy conversation practice — short README)
- **NEW watch:** Linu5-byte/japanese-grammar-flashcards (404 README)
- **NEW watch:** mdtofayel/DoDoDeutsch / menglibinghe/DeutschLernen / r66ad/vokabeltrainer-deutsch / orvixstudio/-deutsch-b1-trainer (DE stubs)
- **NEW watch:** shubhamsinghcol/smart-search (Anki Browser NL search addon — utility)

## Bounce (library / spam / thin / off-lane)
- Truncated Ankit*/Ankita*/ankit-* portfolios and Anki-Flashcards-Software/.github org spam
- FSRS library/demo: onlyoon/flashcard-schema (404), PrzemekKozinski/fsrs-demo, alder-jetty/recall-scheduler, xt9jr0qdo9/fsrsf
- SenmuuuuW/dsh-diagnostic-tutor — DeepSeek Harness host-locked diagnostic tutor (same family as prior alei37/dsh bounce)
- XiXiHUAWEI/ZYCT — Socratic **math** mistake tutor (education off language lane)
- TruMai/tutoring-slot-scheduling-api / Ana-Rojas88/tutoria_* / angelzemanate37-commits/tutorial-pc-virtual — tutoring scheduling / React tutorial homework
- phinn/kinet-memory / sneg1357wp/toeic-anki / Persie0/AnkiFlutter / uvarovaleksei/dsl-to-yomitan-english-dictionaries — empty/404 README
- dcowsill/cdn-citizenship-anki — Canadian citizenship exam deck (geo/civics)
- bayhuseyinkocak/Testing-Exam-with-FSRS-Algorithm — exam FSRS shell
- carver/tab-squasher / u-mmmmk/Pomodoro-Bar / sebb7y/anki-speedup / luqmanae/steady-pomodoro — Anki UX micros
- Coding-Kocur/zhongwen — static ZH Anki deck for PL learners (content pack)
- CodeAlpha / internship language-app shells (Shashank-coder-sudo, AswaniRR, nidhisahani26, minji401, nada-elasasy, musical-sniffle)
- badallsingh/Linguaflow / jamil314/silver-tongue / ttgxxiixiv/Eslacity / EmilKoskinen/ParlaPRO / tefaz/German-fill-in-the-blank-quiz — thin/generic shells
- illanazarov326-wq/finnish-language-learning — personal FI markdown course notes (library)
- geekfujiwara/japanese-input — Astelio IME (input method, not study)
- ToTo-40417/exllm-exword — Casio EX-word tiny JA LLM runtime (hardware novelty)
- HSKGO123/HSKGO123 / qinkartbalriyes/anki / noitru2005-yhn/anki — content stubs
- Matchmaking / programming-language homework / restaurant / TF2 / pharmacy / IRPF tax / agentfaehig-de onboarding
- samvallad33/vestige-gemini / udayasri10435/CogniPath — FSRS as memory infra for non-L2
- luckysolanki902/decko — engineering courses SRS (off language)

EDU_COUNT=3
alert=no
