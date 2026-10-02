# Field education hunt — 2026-10-02 (Asia/Taipei cron; box America/New_York Thu Oct 1 evening ET)

Window: `created:>2026-09-30` / `created:2026-10-01` / `created:2026-10-02` (GitHub MCP `cursor-github` search_repositories; split OR queries ≤5 ops; raw.githubusercontent.com README/index fetches → `/workspace/field/edu1002/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (`seen-gh-repos-lower.txt` 434→615 + prompt list). Do NOT re-keep yesterday packet 49: stagfoo/jlptbenkyo, ahmadasrizalmi/Japanese-Reader-AI, mansourvery-hub/anki-chinese-template. Prior KEEPs stay SEEN: ttiyana/korean-fast-track, jarod85/Chinese-Learning-App-Lock-Phone-Samsung, RudyBoe/kanji-trainer, Ellisdeeman/n5-vocab-quest, Dev-moe-kyawaung/TOPIKII-Level-3-pro-v3.0, mobashirrahman/glossline-android, yorkwahaha/kana-run, priyasureshgermany/deutsch-lernen. Yesterday overflow already SEEN (live-subs, pocket-nihongo/korean, JpKanji, japanese-web, kana-renshu, MedDeutsch, …) — do not re-KEEP; may reappear as overflow only with NEW strong evidence (none did).

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. 4b626y8v7w-del / mandarinpath — score 10 · [education·SRS·i-plus-one·reveal-schedule·prefer-ZH]
- one-line packet shape: Offline-first **Mandarin PWA** (Safari → Home Screen; no account/network after install): **10 units / 66 lessons / 1,572 exercises / 889 SM-2 cards** — tones-first minimal pairs → 250 frequency words → situation phrases → mispronunciation drill → sentence building → numbers/measure words; **five practice modes** (SM-2 · Tone Trainer · Flip Match · 4-grade flashcards · graded 田字格 handwriting for 120 chars); slow TTS default 0.7×; miss-retry capped at two rounds; research-backed first SRS gap (~9 days); export progress; GH Pages live. | https://github.com/4b626y8v7w-del/mandarinpath | created 2026-10-01
- Distinct-from: mansourvery-hub/anki-chinese-template (mining card chrome in Anki) — this is **full offline curriculum desk + SM-2**. Distinct from jarod85 HanziLock (phone human-gate production) — graded lessons + tone trainer, not lock-screen. Distinct from Ca1Fancy/hanzi-quest (RU iPad game) — tones-first pedagogy + honest stroke limitations.

### 2. danielsan163 / kana-kanji-srs — score 9 · [education·SRS·tutor-loop·prefer-JA]
- one-line: Windows **WaniKani/Bunpro-style Electron SRS** shipping `Kana-Kanji-SRS-Setup-1.0.0.exe`: Levels 1–3 kana → **~2,200 JLPT kanji (N5→N1)** in ~20-kanji levels → ~5,000 vocab + ~240 phrases unlock when component kanji hit Guru; Apprentice→Burned stages with demote-on-miss; romaji→kana typing; meaning/on/kun prompts; Tatoeba examples + KanjiVG strokes; JA Windows TTS; `%APPDATA%` progress + 14-day backups; open data (KANJIDIC2 / open-anki-jlpt / JMdict / Tatoeba). | https://github.com/danielsan163/kana-kanji-srs | created 2026-10-01
- Distinct-from: stagfoo/jlptbenkyo (offline Android N5–N3 multi-skill desk) — this is **desktop WaniKani progression to N1** with installer. Distinct from RudyBoe/kanji-trainer (same-reading graph) — full SRS queue + vocab/phrases gated on kanji Guru. Distinct from Ellisdeeman/n5-vocab-quest (thin N5 PWA) — multi-level Electron with shipped EXE.

### 3. Senko3141 / Haru-Cards — score 9 · [education·SRS·tutor-loop·prefer-KO]
- one-line: Offline-first **Korean Hangul + FSRS PWA** (React/TS/Vite; GH Pages + home-screen install): **six guided Hangul lessons** (vowels/consonants/blocks/vocab, all open); **233 starter cards** (205 everyday + school/club phrases) with **TS-FSRS** due prioritization (daily goals never lock content); KO device TTS + optional romanization; IndexedDB progress + JSON backup/restore; Playwright e2e + Pages CI; no account. Live: https://senko3141.github.io/Haru-Cards/ | https://github.com/Senko3141/Haru-Cards | created 2026-10-01
- Distinct-from: ttiyana/korean-fast-track (KO web FSRS desk, prior KEEP) — this is **Hangul pedagogy + phrase pack + iPhone PWA path**. Distinct from Emil0001/rinae (SaaS, courses gated) — local-only, content ships. Distinct from Eason-Xi/pocket-korean (hardware-locked Passport) — browser/PWA portable.

## Overflow (≥6, below top-3 SETUP slots)

### Habibeprojects / hasna — score 9 (overflow; prefer-DE content·Anki·offline)
- Single-file offline PWA **Deutsch für Hasna**: A1→B2, **1,169 hand-written entries** with EN+AR (RTL switch), articles/plurals/principal parts + example sentences; flashcard trainer with spaced queue; 77 grammar cards; **2,067 Piper mp3s**; downloadable **2,087-card `.apkg`** (13 subdecks); SW offline. Strong DE content desk — overflow because SETUP slots filled by ZH/JA/KO runners. | https://github.com/Habibeprojects/hasna | created 2026-10-01

### aini9027 / jp-study-lookup — score 8 (overflow; prefer-JA immersion·tool)
- Chrome extension: highlight JA on any page/PDF (incl. scanned OCR via local Tesseract) → readings, meanings, POS, JLPT, deinflection, kanji breakdown, sentence gloss; local hiragana convert; shipped zip Releases. Lookup tool, not daily SRS desk. | https://github.com/aini9027/jp-study-lookup | created 2026-10-01

### Wyzmic / Aobana-Reibun — score 8 (overflow; prefer-JA immersion·Anki)
- Anki add-on: batch/review fill of **example sentences + audio + images** from Nadeshiko / Immersion Kit / local Aobana; AnkiWeb code 1429349152; Qt6. Sentence-mining companion, Anki remains SRS. | https://github.com/Wyzmic/Aobana-Reibun | created 2026-10-01

### Jo-Mako-Anki / japanese-definitions — score 8 (overflow; prefer-JA Anki·offline)
- Offline Anki add-on: JMdict definitions + furigana + POS; batch populate + Choose Definition UI; deinflection; `.ankiaddon` Releases. Card-fill tool. | https://github.com/Jo-Mako-Anki/japanese-definitions | created 2026-10-01

### JobsKits / JobsKanjiByJap — score 8 (overflow; prefer-JA dictionary·reveal)
- Sibling of yesterday JobsKits/JpKanji: offline PySide6 **日语汉字点读** with ZH gloss/Argos MT, KANJIDIC2 13k + JMdict 218k + Tatoeba; Mac/Win packagers. Lookup desk, not daily SRS. | https://github.com/JobsKits/JobsKanjiByJap | created 2026-10-01

### olafkrawczyk / japanese-reading-helper — score 8 (overflow; prefer-JA immersion·reveal)
- Chrome helper for NHK Easy-style reading: 文節 phrase breaks, particle highlight+context gloss, hover furigana (hidden until hover), jisho on hold; local kuromoji. Reveal-schedule reading aid. | https://github.com/olafkrawczyk/japanese-reading-helper | created 2026-10-01

### vanirvan / kadle — score 8 (overflow; prefer-JA stroke·on-device-AI)
- Vite PWA **Kana Doodle**: client-side ONNX ResNet (JIS X 0208, 14.5 MB CacheStorage) grades handwriting; deck selector + vocab mode; privacy-first. SRS/kanji/audio on roadmap. | https://github.com/vanirvan/kadle | created 2026-10-01

### anhquan27it / kotoba — score 7 (overflow; prefer-JA·VI chrome·thin content)
- Next.js **VI→JA lesson desk** with furigana toggle, exercises, flashcard SRS (1–4 grade), progress export; GH Pages path. Evidence: only **N4 lesson 15** shipped so far — template strong, corpus thin. | https://github.com/anhquan27it/kotoba | created 2026-10-01

### Fantastic-Jing / wortsprint-german-vocabulary — score 7 (overflow; prefer-DE sentence·ZH UI)
- Static `WortSprint/index.html`: German **B1.1** sentence-based staged practice + flash quizzes + custom groups + JSON backup; ZH chrome. Personal course notes bundled. | https://github.com/Fantastic-Jing/wortsprint-german-vocabulary | created 2026-10-01

### DaWy / pinyin-lyrics — score 7 (overflow; prefer-ZH/JA/KO immersion)
- Android floating **synced lyrics** with pinyin / JA romaji / KO RR; HSK tone colors; APK Releases. Immersion overlay, not tutor loop. | https://github.com/DaWy/pinyin-lyrics | created 2026-10-01

### hieubuiVMUS2K4 / hanziWriting — score 7 (overflow; prefer-ZH stroke·VI)
- Vite React **Hanzi Writer** stroke-order desk for VI learners; Pleco import; local progress; quiz hide-hints modes. Stroke skill, light SRS. | https://github.com/hieubuiVMUS2K4/hanziWriting | created 2026-10-01

### jbThanhNguyen / luyen-n5 — score 7 (overflow; prefer-JA·VI N5 quiz)
- Single-file N5 vocab Quizlet-style (293 words) + kana tables + 49 kanji; miss-repeat; CSV attempt logs for ML. Live Netlify. | https://github.com/jbThanhNguyen/luyen-n5 | created 2026-10-01

### Ca1Fancy / hanzi-quest — score 7 (overflow; prefer-ZH game·iPad PWA)
- RU iPad PWA: lessons/Quest/Pinyin/Listening/Writing/Boss; Hanzi Writer; TXT/CSV import; SW cache. Game juice over curriculum. | https://github.com/Ca1Fancy/hanzi-quest | created 2026-10-01

### Harsimar17 / Deutsch-Vocab-Trainer-V2 — score 7 (overflow; prefer-DE SaaS-heavy)
- Spring Boot A1–B1 trainer: server-side SRS drills, B1 stories, Phasentests; Firebase anon + Firestore; Gemini sentences optional. Portable mechanisms exist but **account/backend required**. | https://github.com/Harsimar17/Deutsch-Vocab-Trainer-V2 | created 2026-10-01

### johnmorrisdotca / bushu — score 7 (overflow; prefer-JA radical tool)
- TS multi-radical kanji lookup (RADKFILE 253 radicals / 6,355 kanji). Library tool, not tutor loop. Sibling hikidashi (era dates, numerals, verb forms, readings). | https://github.com/johnmorrisdotca/bushu | created 2026-10-01

### alpenmilch411 / syosetsu-downloader — score 6 (overflow; prefer-JA immersion·tool)
- Polite Syosetu chapter downloader → plain text with furigana or EPUB3. Corpus pipeline, not learner desk. | https://github.com/alpenmilch411/syosetsu-downloader | created 2026-10-01

### makrem255 / hanzisrs-android — score 6 (overflow; prefer-ZH Android·thin product essay)
- Kotlin Compose + Room + SM-2 unit tests + stroke canvas; optional Gemini proxy. README is AI Studio boilerplate — content/curriculum evidence weak vs mandarinpath. | https://github.com/makrem255/hanzisrs-android | created 2026-10-01

### GuillaumeAB / hanziflow — score 6 (overflow; prefer-ZH aspirational README)
- Claims HelloChinese+Anki hybrid HSK1–5 with SM-2 + hanzi-writer. `package.json`/src paths 404 at fetch time — watch until tree matches README. | https://github.com/GuillaumeAB/hanziflow | created 2026-10-01

### itsjeremywang / chinese-phrases — score 6 (overflow; prefer-ZH flashcards)
- Two-character phrase flashcards (audio/pinyin/breakdown/examples); recovered via `index.html` (README 404). Thin desk. | https://github.com/itsjeremywang/chinese-phrases | created 2026-10-01

### yuji19371-rgb / kanji-rush · rgaior / kanji-flashcard · nchnn / KanaQuiz · AlessandroGrassi1998 / kana-cards · hanklcoglu / kana-dojo · RuolinLai / JapaneseKanaTrainer · FlavioLorenzi / kanji-quiz-n4 · hush0205-design / hangul-car-game · jabborov / korean_vocabulary — score 6 (overflow; thin SPA/quiz shells)
- Recovered index.html / short README kana-kanji-hangul quiz desks; localStorage at best; below SETUP bar vs Haru-Cards / kana-kanji-srs.

### gcns37 / KanjiApp — score 6 (overflow; prefer-JA huge single HTML)
- 1.5 MB `index.html` recovered (README 404). Opaque product essay — treat as thin until documented.

### xdtcssdi123 / abdrop — score 6 (overflow; EN Ebbinghaus·off prefer-L2)
- Vue3/Nuxt+Capacitor Anki-compatible Ebbinghaus app; target L2 unclear/EN-leaning. | https://github.com/xdtcssdi123/abdrop | created 2026-10-01

### NgarumaVTC / swahili — score 6 (overflow; off prefer-L2 Anki content)
- 4,455 Goethe-A1-style Swahili Anki cards. Off JA/ZH/DE/VI/KO/FR/ES prefer set. | https://github.com/NgarumaVTC/swahili | created 2026-10-01

### mkusm / pokemon-firered-jp-anki — score 6 (overflow; prefer-JA game immersion Anki)
- Pokémon FireRed JA immersion deck. Content pack. | https://github.com/mkusm/pokemon-firered-jp-anki | created 2026-10-01

### ai68298100 / siyuan-lv-cards · siyuan-exam — score 6 (overflow; SiYuan FSRS tooling·L2-agnostic)
- SiYuan flashcard/exam cockpit with FSRS. Knowledge-base tooling, not L2 tutor. | https://github.com/ai68298100/siyuan-lv-cards | created 2026-10-01

### MedievalMonk / vocab-trainer — score 6 (overflow; EN FSRS PWA)
- Local-first **English** vocab FSRS PWA. Off prefer-L2. | https://github.com/MedievalMonk/vocab-trainer | created 2026-10-01

### johnmorrisdotca / hikidashi — score 6 (overflow; prefer-JA text utils)
- Drawer of JA text tools (era dates, numerals, verb dictionary forms, readings). Utility. | https://github.com/johnmorrisdotca/hikidashi | created 2026-10-01

### inspiredcn / kanjian — score 6 (overflow; prefer-ZH thin PWA)
- Offline PWA with only **火/水** card sets (11 cards). Seed, not curriculum. | https://github.com/inspiredcn/kanjian | created 2026-10-01

### z-pw / hanpath-hsk-characters — score 6 (overflow; ZH data dump)
- HSK 3.0 character JSON/CSV (pinyin/radical/strokes). Data, not tutor. | https://github.com/z-pw/hanpath-hsk-characters | created 2026-10-01

### PeachSlayer123 / Chinese-learning-site · bourne2398 / jlpt-n4-infographics · tt1145142222 / chinese-learning-skills · scottino2019-glitch / HanziLab · asekhqw1427-oss / bd10-mandarin-learning-hub · narithkgame2 / kidlingo · xobett / nonbiri-nihongo · stephenhunter / toddler-words · Nuvejo / Nordlicht-Mock — score 6 or bounce-border
- Personal weekly-words / infographic hub / Claude skills / puzzle games / React classroom shell / kids train game / leisure JA site / toddler EN+JA / physio DE mock — portable mechanism thin or off-lane; kept at floor for SEEN hygiene.

## Promote-watch
- **NEW watch:** 4b626y8v7w-del/mandarinpath · danielsan163/kana-kanji-srs · Senko3141/Haru-Cards (KEEP)
- **NEW watch:** Habibeprojects/hasna — overflow 9; promote if DE SETUP slot opens
- **NEW watch:** aini9027/jp-study-lookup · Wyzmic/Aobana-Reibun · Jo-Mako-Anki/japanese-definitions · vanirvan/kadle · JobsKits/JobsKanjiByJap · olafkrawczyk/japanese-reading-helper
- **NEW watch:** anhquan27it/kotoba — recheck when lessons beyond N4#15 land
- **NEW watch:** GuillaumeAB/hanziflow — README claims HSK1–5 SM-2; tree incomplete at fetch
- **NEW watch:** makrem255/hanzisrs-android — product essay vs AI Studio shell
- **NEW watch:** Eindall/kanadrill — Discord/Postgres SaaS shell; SRS not yet productized
- **Still watch (README improved but not KEEP):** Rafacv23/kaku — honest README now (“most of the above is not built yet”); Bun+Turso scaffold — stay promote-watch
- **Still watch:** BoldKenobi/japanese_study_app — README still title-only (20b)
- **Still watch:** ojs-fisher/deutsch-lernen — README still 404
- **Still watch:** youme930/-cheoeum-gana- — index.html still thin SPA shell
- **Still watch:** Emil0001/rinae-korean-learning-platform — courses still gated / not public content
- Prior packet 49 KEEPs stay SEEN; do not re-keep. Yesterday overflow (live-subs, pocket-*, JpKanji, …) stay SEEN overflow, not re-KEEP.

## Bounce (library / spam / thin / off-lane)
- Anki name-spam / Ankit portfolios / FakeAnki siblings (yujikim0911kaisei-wq Anki-* / Super-Anki, Ankit* personal sites, wedding/Airbnb Ankit clones)
- Japan tourism / unrelated “kanal/kanata” name collisions (pixel-gun, birthday-kanah, water-canal Turkish, Uwaga-kanar, hustle-city Mama Kana Farm, Kanami Reporter, companion-module-kanata)
- Game/localization / STEM “learning” / ML ASR (codeswitch-dpo, nihao-chinese-ml object-detect, from-zero-ai engineering courses, zakiyamaaaaa software-engineer RPG)
- Fonts only: toiucorp/EZGM Hangul/CJK typeface
- Empty/size-0 shells: Neo-Nafiz/Kanata, adityasingh06-05/kanapon-android, kunzxn/XUEYAN-s-Learning, scriptman007/kanji_sensei_mobile-, Moeze2/kanji-leason-*, indomurakk-jpg/Japanese-learning, baohuyxxi/furigana-word (15b), javier9302/kanji-learning-app (20b), HanakoMatcha/Kanji_Garden (69b README), nghianguyen2710/JapaneseLearning (19b)
- Converters / IME / music players: Mrfartam/KanaSwitcher, hakrosabir/Sindhi-Pinyin-Keyboard, VaporFOXChanber/kanade, ShambeXI/LSTranslate, SafetyFA/noctalia-pinyin-plus, Yezi-Mooyee diceware, pojinYang/naiwa-text, betona1/vaveling-hanzi-printer, icoaplus/kanji-print-maker, Stewarhot/pinyin-typing-practice (elderly IME)
- HSK/content spam / tourism / Free Fire banners: hanzihanmodz Banner-Free-Fire, darvinhuang WATERVIN, zwanru29 ai-korean-survey
- Interview/generic flashcards / country Anki (Parapoxvirus/cotw) / Medicin-Anki / SiYuan tooling kept at overflow floor only when L2-agnostic
- Flutter/empty / classroom Workshop shells: asekhqw1427 Learning-hub twin, JINHUA611 kids-chinese, qoethics/Chinese-Learning thin
- EN-target / off prefer: MedievalMonk vocab-trainer, chu0127 english-vocab, SparklingTea english-vocab, speak-fluent class already SEEN

## Fetch failures (no README / empty / rate-limit)
- README 404 then recovered via index.html: itsjeremywang/chinese-phrases, yuji19371-rgb/kanji-rush, rgaior/kanji-flashcard, nchnn/KanaQuiz, gcns37/KanjiApp, hush0205-design/hangul-car-game, jabborov/korean_vocabulary, youme930/-cheoeum-gana-
- Still fail: kunzxn/XUEYAN-s-Learning, ojs-fisher/deutsch-lernen
- helptreephilic/NihonDa-Practo README 140b near-empty; baohuyxxi/furigana-word 15b; javier9302 20b; HanakoMatcha 69b; nghianguyen2710 19b; BoldKenobi still 20b
- GitHub REST API rate-limit hit on unauthenticated `api.github.com/repos/.../contents` probes; raw.githubusercontent.com fetches continued fine
- Habibeprojects/hasna has `.env.local` in tree listing (do not fetch/exfil); app itself is static HTML+audio

## Banked (learning lane)
- https://github.com/4b626y8v7w-del/mandarinpath → raw/learning/2026-10-01-4b626y8v7w-del-mandarinpath-offline-first-mandarin-pwa-tones.md
- https://github.com/danielsan163/kana-kanji-srs → raw/learning/2026-10-01-danielsan163-kana-kanji-srs-wanikani-style-electron.md
- https://github.com/Senko3141/Haru-Cards → raw/learning/2026-10-01-senko3141-haru-cards-offline-first-korean-hangul.md

KEEP_COUNT=3
alert=no
