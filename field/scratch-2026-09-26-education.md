# Field education hunt — 2026-09-26 (Asia/Taipei cron; box America/New_York)

Window: created:2026-09-25 / created:2026-09-26 / created:>2026-09-24 (GitHub MCP `cursor-github` search_repositories; raw.githubusercontent.com README fetches → `/workspace/field/edu0926/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (~295 repos + scratch-seen-urls). Do NOT re-keep yesterday: yhyy135/babello, pronnmark/frenchfries, Miso-Soup98/kotoba-study. Yesterday overflow already SEEN: natha-ui/hanbit, lukskrp/cobaltium-desktop, HanifCarroll/iina-language-learning-plugin, anzorein/rt-jpn-ocr, deserteaglemj/habla-spanish, milksuger/MandarinLearnApp, zhenke-dev/kindle-words, brndnsmth/romlingo, eddieelorza/english-os, acrot0/anki-forge, Lanternko/karaoke-jp, greyindex/jitendex-yomitan-id, ksyasuda/hachidori-docker, runnithan/claudex-learn. Prior keeps/watches stay SEEN.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. ishmum123 / japanese — score 10 · [education·teach-once·i-plus-one·generated-input·reveal-schedule·prefer-JA]
- one-line packet shape: Static JA A1–B1 vocab trainer pack on shared `vocab-engine` submodule: **2000 words + 1590 kanji units + 60 graded reading passages** (20/level); skippable **かな** hiragana/katakana primer; kanji stage gates written form (`pronFirst` until mastered, then kanji); tap-to-gloss passages; browser `ja-JP` TTS (no recorded audio); rule-fixed Tatoeba/Sudachi links + QA seeds; live https://ishmum123.github.io/japanese/ ; `build.sh` → self-contained trainer. Honest: vocab base for B1, not full JLPT N3 (no grammar/listening/speaking course); passage Qs machine-authored, not native-reviewed. | https://github.com/ishmum123/japanese | created 2026-09-25
- Distinct-from: Miso-Soup98/kotoba-study (N5–N2 grammar library + FSRS + TED精读) — this is **frequency-band vocab + kana/kanji stages + graded passages**, not textbook grammar FSRS. Distinct from xun1607/jpLearn (generic .apkg PWA).

### 2. workwithlucas / frenchteacher — score 9 · [education·tutor-loop·teach-once·human-gate·prefer-FR]
- one-line: FR voice conversation PWA (CECRL): **speak → browser Web Speech (`fr-FR`) live transcript → Claude streaming teacher → Fish Audio TTS**; 20 curriculum blocks; localStorage progress (block, last rule, recurring errors ≥2 sessions); FR/PT mic toggle for meta-questions; post-session Claude summary advances **one** block; Netlify functions hold keys; `APP_ACCESS_CODE` gate. ~$0.45–0.70 / 30-min session. Chrome/Edge; Safari flaky; Firefox no STT. | https://github.com/workwithlucas/frenchteacher | created 2026-09-25
- Distinct-from: pronnmark/frenchfries (6-gear FR verb FSRS chat drills, zero API) — this is **voice CECRL conversation tutor + Fish/Claude**, not verb-gear desk.

### 3. ishmum123 / korean — score 9 · [education·teach-once·i-plus-one·generated-input·prefer-KO]
- one-line: KO twin of the japanese pack on same `vocab-engine`: **2000 A1–B1 words + 60 graded passages** + skippable **한글** Hangul primer (47 units); browser `ko-KR` TTS; NIKL grade floors; 1,692 generated polite sentences marked `src:gen` + rule-fixed homograph links; live https://ishmum123.github.io/korean/ ; v1.1–v1.2 QA rounds 2026-09-25. Honest: vocab base for TOPIK 3, not full grammar/listening. | https://github.com/ishmum123/korean | created 2026-09-25
- Distinct-from: natha-ui/hanbit (Hangul→hanja child path + daily generated stories) — this is **A1–B1 frequency vocab trainer + Hangul primer + graded Read tab**. Distinct from uminrae/korean-flashcards / TOPIK mocks.

## Overflow (≥6, below top-3 SETUP slots)

### equwal / subread-anki — score 9 (overflow; Android immersion miner)
- One tap → AnkiDroid card: word + reading + definition + sentence + screenshot + word/sentence audio; works from any app text-select / share / SubRead Dictionary/Overlay; local-only (no network permission); optional accessibility capture. Prefer-immersion twin under babello/context-deck. | https://github.com/equwal/subread-anki | created 2026-09-25
- Distinct-from: equwal/subread-dictionary (prior watch) — this is **Anki card writer**, not the dictionary. Distinct from DeepanshuPal/context-deck (browser YT/Netflix miner).

### Carlos09Or / Final-Mandarin — score 8 (overflow; prefer-ZH HSK1)
- Static HSK 1 (150 words): Cards + 10 thematic practice blocks (meaning / hanzi-pinyin / listening / association / type-hanzi / mixed) + Write Hanzi + Situations; human-gate Next (no auto-advance); local progress. Prefer-ZH but thin vs mandarin-drill. | https://github.com/Carlos09Or/Final-Mandarin | created 2026-09-25

### met-tk / Tampo — score 8 (overflow; prefer-JA WinUI FSRS)
- Windows WinUI3 JA vocab + FSRS v4 desktop; word-list slices; ZH/EN/JA UI; installer. Prefer-JA but Windows-only. | https://github.com/met-tk/Tampo | created 2026-09-25

### Nemuidere / LyricDeck — score 8 (overflow; RU/JA lyrics→Anki)
- Local Flask: LRCLIB lyrics → lemma cards → .apkg / AnkiConnect; optional JA mode (fugashi+UniDic+JMdict, pitch number); Claude optional. Prefer immersion song mining. | https://github.com/Nemuidere/LyricDeck | created 2026-09-25

### topherhunt / ditto — score 8 (overflow; dictation FSRS — IT/EN/NL/GA)
- Dictation trainer: listen → type letter-level diffs → meaning check → FSRS review; scaffolded words→chunks→sentences; live ditto.topherhunt.com. Strong mechanism; langs off JA/ZH/KO/FR/ES prefer. | https://github.com/topherhunt/ditto | created 2026-09-25

### rachelw320 / language_learning_app — score 8 (overflow; Egyptian Arabic PWA)
- 369 EA cards, SM-2 + 5-day mastery, fuzzy transliteration (Levenshtein 0.72), ElevenLabs audio, offline-bundled deck. Dialect niche (not MSA). | https://github.com/rachelw320/language_learning_app | created 2026-09-25

### DavisGoglin / spectrogram — score 7 (overflow; JA pitch accent mic)
- Browser pitch contour + optional spectrogram vs reference; live pages. Honest LLM-made caveat. | https://github.com/DavisGoglin/spectrogram | created 2026-09-25

### giovannipivatoo / memoro — score 7 (overflow; Android FSRS-6 Anki — not L2-specific)
- Kotlin Anki-compatible FSRS-6 + optional DeepSeek open-answer. Generic SRS shell. | https://github.com/giovannipivatoo/memoro | created 2026-09-25

### bishoppawn1 / spanish-practicing — score 6 (overflow; thin ES greetings MC)
- 98 Quizlet-sourced greetings MC static Pages app. Prefer-ES but recognition-only thin. | https://github.com/bishoppawn1/spanish-practicing | created 2026-09-25

### MathewDMoore / habla-ecuador — score 6 (overflow; Ecuador ES prototype)
- Static Ecuadorian lexicon prototype; ~10 learner-ready entries; evidence badges planned. Early. | https://github.com/MathewDMoore/habla-ecuador | created 2026-09-25

### eranoix / kids-study-app — score 7 (overflow; EN kids Electron — off prefer-L2)
- Grade-calibrated tests + karaoke read-aloud + FSRS-5 mistake cards; mock LLM. Strong runner, L1 school not L2. | https://github.com/eranoix/kids-study-app | created 2026-09-25

### henwill8 / AnkiCardUnlock — score 6 (overflow; Anki maturity unlock addon)
- Unlocks harder cards / sentences once notes mature. Utility, not curriculum. | https://github.com/henwill8/AnkiCardUnlock | created 2026-09-25

## Promote-watch continues (same URLs — do not re-keep)
- Prior watches: Rabbit_Hole, manga_anki, typingchinese, live-text-for-video, opennihongo, tower-of-words, localspeech, DoDoDeutsch, …
- **NEW watch:** equwal/subread-anki (overflow 9 — promote if immersion miner preferred over KO pack)
- **NEW watch:** Carlos09Or/Final-Mandarin (HSK1 practice studio)
- **NEW watch:** met-tk/Tampo / Nemuidere/LyricDeck / topherhunt/ditto / rachelw320 EA
- **NEW watch:** SparklingTea/Espanol-Helper, tkk-fk/kanji4-flashcard, lliuasi/mandarin-airport-interactive, JvMeraki/korean-app, Cornil3/Spanish-tutor, RaulCirigliano/Desarrollo-Web-Aprendiendo-Japones (README miss / thin)
- **NEW watch:** kike9978/mandarina (Vite template README only)
- **NEW watch:** xiwuwuyangtai-coder/yomitan-spot-map (no README)
- **NEW watch:** ishmum123/vocab-engine (shared engine submodule — library unless ships alone)

## Bounce (library / spam / thin / off-lane)
- Truncated Ankit*/Ankita*/ankit-* portfolios; HartLuvsCoding/fsr-sensors (hardware FSR ≠ FSRS)
- Hugelidus/atlas — FSRS study app for school subjects (Probabilidad), not L2
- Programming-language learning notes / Exercism / C tutorials
- Japan tourism archives (jiantailanglin266-rgb/*), Korean food/diner shells
- Sign-language ML / NLP homework / forensics handbooks (UROCK)
- Tutorial repos / university projet-tutore / dermatology tutorial
- Generic flashcard shells (Karticky, Flashcardapp, Back_Flashcards, Flashcard-V2)
- YTM_Immersion (YouTube Music skin), production-ml-lab (ML immersion not L2)
- phinn/kinet-lang privacy page; clairekiu/anki-reddit-vocabulary thin

EDU_COUNT=3
alert=no
