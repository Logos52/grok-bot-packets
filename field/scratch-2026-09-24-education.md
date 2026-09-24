# Field education hunt — 2026-09-24 (Asia/Saigon)

Window: created:2026-09-22 / created:2026-09-23 / created:>2026-09-22 (GitHub MCP `user-GitHub-xai` search_repositories; raw.githubusercontent.com README fetches → `/workspace/field/edu0924/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (176 repos + scratch-seen-urls). Do NOT re-keep yesterday: CaiqueGo/graded-reader, Mifune-Shioriko/ir4anki, RC-APC/Foreign-Language-Video-Learning-Assistant-B-. Yesterday overflow already SEEN: sm-pranav/Nihongo-N5-JLPT-Study-App, uminrae/korean-flashcards, equwal/subread-dictionary, creeperboo/anki-interactive-quiz, shogotomita/lingo-cards, 3ammaar/armada-yomitan, argrig666/anki-pronounce-selected, coracherry517/babelgarden, Arcade0101/tcj-japanese, zaykha/Personal-Flashcard-JLPT. Prior keeps/watches stay SEEN (kanji-trainer, deutsch-karten, Parseh, mal, deutschmeister, anki-flashcard, pi-polyglot, AnkiLinkedLearning, ai-language-learning, chineseleading_hsk, nihongo-dojo, AnkiSub, wenyan-fsrs-recitation, note-furigana, german, hanzi-steps, jlpt-quiz, MMDL, Rabbit_Hole watch-only).

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. DeepanshuPal / context-deck — score 10 · [education·immersion·generated-input·human-gate]
- one-line packet shape: Local-first immersion workspace: YouTube/Netflix subtitle click→definition (hover pauses video) + local video/audio+SRT/VTT mining; **encounter graph** (term → episode/timestamp/sentence/clip, append-only) so Anki cards are disposable views of history, not the history. Offline Wiktionary packs (17 langs→EN) or import Yomitan zips (JMdict); JA/ZH via browser word segmenter; ffmpeg frames+line audio; **Send to Anki** via AnkiConnect (skip existing; deleted-in-Anki marked, never auto-readd) or TSV + `contextdeck://` deep-link Mac app. Chrome MV3 extension ↔ localhost only (fixed extension ID). Honest DRM: Netflix text+link only, no protected capture. Node 20+; `npm start` → `127.0.0.1:4173`; e2e against YT/Netflix-shaped pages. | https://github.com/DeepanshuPal/context-deck | created 2026-09-22
- Distinct-from: RC-APC/Foreign-Language-Video-Learning-Assistant-B- (in-browser shadow→Leitner notebook, no Anki required) — this is **encounter-graph miner + AnkiConnect + optional Yomitan/Wiktionary**, not Leitner boxes. Distinct from yong9875/AnkiSub (subtitle→cards without durable encounter history).

### 2. MarionLiew / anki-tutor — score 9 · [education·tutor-loop·human-gate·reveal-schedule]
- one-line: Agent skill + CLI on **existing Anki/FSRS** (AnkiConnect): one fixed **Concept** per note; every due review the agent writes a **fresh** question so you practice transfer, not the answer key. Wrong → minimal hint → retry → new transfer variant; strict `Again` even after post-hint recall. Source Library (PDF/DOCX/MD ingest + SHA provenance); TutorSession state machine (≤8 Q / 20 min); strategy goals require explicit user confirm; `passive_review.py` cron (≤3 due, first question only). Hermes skill install paste; offline pytest with mock AnkiConnect. Anki stays sole scheduler — no second mastery DB. | https://github.com/MarionLiew/anki-tutor | created 2026-09-23
- Distinct-from: Mifune-Shioriko/ir4anki (IR chunking + preview/next-day first grade) — this is **live generative quizzes on fixed concepts + transfer check**, not suspended-preview IR. Distinct from AnkiLinkedLearning / anki-llm-pipeline (card generation).

### 3. sezmow / habla — score 9 · [education·tutor-loop·reveal-schedule·prefer-ES]
- one-line: Spanish production-first web app: curriculum (2 levels / 12 units / 39 lessons) + per-item memory ladder (10m→1d→3d→7d→14d→30d→60d, hardness-scaled) with power forgetting curve; **recognition alone cannot climb far** — mastery needs recall/production/listening/speaking + long-delay evidence. Lesson builder Learn→Understand→Recall→Produce→Speak→Use; answer checker (accents/typos/token alignment); ser/estar mistake taxonomy; guided on-device roleplays; optional Claude conversation partner behind local server (Pages demo runs without it). Adaptive placement + demo learner simulated ~4 weeks through real engine. Vitest on pure TS engine; localStorage + SW offline. Live: https://sezmow.github.io/habla/ | https://github.com/sezmow/habla | created 2026-09-22
- Distinct-from: shogotomita/lingo-cards (static tourism SRS) — this is **full ES curriculum + production-gated spacing**. Distinct from deutsch-karten (DE flashcards).

## Overflow (≥6, below top-3 SETUP slots)

### ChenZhuo4649 / live-text-for-video — score 9 (overflow; Mac OCR→Yomitan DOM)
- Pause any Chromium video → Apple Vision OCR → selectable DOM text layer tuned for **Yomitan hover** (width calibration, CJK space fix, Shadow-DOM avoided). `./install.sh` registers Native Messaging host; macOS 13+ only; measured ZH/JA subtitle quality; DRM black frames honest. Prefer-JA immersion twin under context-deck/habla slots — **swap over #3** if Mac Yomitan video mining preferred over ES curriculum. | https://github.com/ChenZhuo4649/live-text-for-video | created 2026-09-23
- Distinct-from: RC-APC video assistant (CC/subtitle text) — this is **hard-sub OCR Live Text for Chrome**, not caption tracks.

### ljhoo24 / kanji-furigana — score 8 (overflow; JA personalized furigana reader)
- Chromium extension: Readability extract + local Kuromoji → furigana aligned to okurigana; modes 항상표시 / 가려서연습 / 표시안함; on-device Chrome Translator JA→KO; reading/meaning/listen state + JSON backup; `activeTab` only (no persistent site perms). Releases ZIP load-unpacked. Prefer-JA graded-reading adjacent. | https://github.com/ljhoo24/kanji-furigana | created 2026-09-23
- Distinct-from: 0xluden/note-furigana (note annotation) — this is **page reader + hide-to-practice + personal known-word state**.

### tomvannuenen / mandarin-drill — score 8 (overflow; ZH-TW speaking FSRS)
- Personal PWA “說 Mandarin”: EN prompt → say aloud → grade; Listen/Read unlock after two correct speak days; pattern cards fill slots from seen vocab; edge-tts `zh-TW-YunJheNeural` + coach MP3 override; Traditional-only gate (opencc reject Simplified); ts-fsrs vendored; Claude Code week-ingest → `items.json` → `uv run tools/build.py`. Prefer-ZH speaking twin. | https://github.com/tomvannuenen/mandarin-drill | created 2026-09-23
- Distinct-from: lifelonglearning123/chineseleading_hsk (HSK curriculum) — this is **Taiwan Traditional production drill + coach pipeline**.

### kimsungchul7719 / topik1-mock-test — score 7 (overflow; KO TOPIK for VI)
- 10 full TOPIK I mocks (70 Q each: listen 30 / read 40), countdown + OMR + auto grade (1급 80 / 2급 140), VI explanations + vocab + listen scripts; creative items not NIIED past papers. Prefer-KO×VI. | https://github.com/kimsungchul7719/topik1-mock-test | created 2026-09-22

### xun1607 / jpLearn (Thẻ) — score 7 (overflow; Anki .apkg PWA)
- Mobile web Anki clone: Dexie schema, ts-fsrs 1–4, Worker `.apkg` import (v11+v18 traps documented), Shadow DOM notetype + furigana/cloze/type filters, media via SW, PWA persist. Honest v18 qfmt/afmt gap. | https://github.com/xun1607/jpLearn | created 2026-09-23

### greggman / g-sho — score 7 (overflow; static Jisho + AnkiConnect)
- Static JA–EN dict (JMdict/KANJIDIC shards, radical + handwriting WebGPU/WASM); AnkiConnect [+] add; GitHub Pages deploy. Strong dict runner — overflow vs study SETUPS. | https://github.com/greggman/g-sho | created 2026-09-23

### persianoff / WordDrift — score 6 (overflow; Android TV vocab overlay)
- TV overlay flashcards (EN/DE/UK/RU) over screensaver/YouTube + phone companion (mDNS edit dict). Immersion-adjacent ambient SRS. | https://github.com/persianoff/WordDrift | created 2026-09-23

### HotlineAHK / yomitan-fishaudio-bridge — score 6 (overflow; Yomitan TTS micro)
- Local GUI HTTP bridge: Fish Audio voices (incl. clones) → Yomitan Custom URL JSON; disk cache; Win/Linux binaries. Useful immersion audio micro, not a curriculum runner. | https://github.com/HotlineAHK/yomitan-fishaudio-bridge | created 2026-09-24

### chachaprince1 / the-6k-extension — score 6 (overflow; JPDB/ImmersionKit installer)
- One-click Win/Mac installer that walks Chrome Developer-mode load for anime study cards (JPDB episodes + ImmersionKit→Anki without IK account). Setup glue more than mechanism depth. | https://github.com/chachaprince1/the-6k-extension | created 2026-09-22

### Drifter1997 / dictionary-cli — score 6 (overflow; EN Wayland HUD)
- Offline Webster FTS5 CLI + Mako notify / Sway floating HUD + Anki TSV export + quiz — EN immersion for games/movies, not L2 prefer-lang. | https://github.com/Drifter1997/dictionary-cli | created 2026-09-23

### GamosiDEV / Youtube2Anki — score 6 (overflow; YT→PT Anki AI)
- Streamlit/Python: YT transcript → OpenRouter AI → PT-BR gloss cards + .apkg/.tsv. Solid miner but EN→PT generic AI deck path. | https://github.com/GamosiDEV/Youtube2Anki | created 2026-09-23

### gustanas / llm-anki-convo (While) — score 6 (overflow; Anki inline in Codex)
- Node CLI: AnkiConnect practice/review HTML into Codex conversation wait time; real grades via AnkiConnect. Clever micro, not L2 curriculum. | https://github.com/gustanas/llm-anki-convo | created 2026-09-23

### crlucenap / flashcards_fr (Quickcards) — score 6 (overflow; FR desk, thin SRS)
- CustomTkinter FR→ES auto-translate + session shuffle (no spaced intervals); wordfreq French gate. Prefer-FR but mechanism thin vs deutsch-karten. | https://github.com/crlucenap/flashcards_fr | created 2026-09-23

## Promote-watch continues (same URLs — do not re-keep)
- Candice-Bennett/Rabbit_Hole (SEEN — watch-only)
- Prior watches: manga_anki, typingchinese, language-learning-audio, simple-language-learning, hanzi-steps, jlpt-quiz, MMDL, shici-recite-app, jitendex-yomitan-zh, hanzi-flip-classroom, leap-framework, gillisandrew/ancci, babelgarden, equwal/subread-dictionary
- **NEW watch:** ChenZhuo4649/live-text-for-video (if Mac JA hard-sub mining becomes roster need — already overflow-scored)
- **NEW watch:** ABakdi/sublight (Whisper+llama local captions — Milestone 00 docs only; revisit when M09 language-learning ships)
- **NEW watch:** jasonasknow-cloud/topik-news (TOPIK 4–6 daily KO news — one-line README; revisit when generator ships)
- **NEW watch:** Uncommon-lineofleastresistance5475/lexiglance (system-wide Yomitan popup claim; README stub `# lexiglance` only — related name to SEEN mattfor/lexiglance; revisit if code lands)
- **NEW watch:** leonardtschora/yeswekanji (Streamlit FR-gloss kanji flip prototype — no SRS yet)

## Bounce (library / spam / thin / off-lane)
- Truncated Ankit* / AnkiDeckSearch / Ankita* portfolios (ankitpoonia9914-web/ANKIT, Ankita-bagalakotimath/Ankita, yujikim0911kaisei-wq/AnkiDeckSearchReview*, kai324620-create/Anki exercise, Zoehong11/anki empty “german workflow”)
- CreeperBeatz/jmdict-kanjidic-bg — Bulgarian JMdict/KANJIDIC gloss dataset (library, not runner)
- Qxy0happy/fsrs-dual-optimizer / realjesse/csharp-fsrs — FSRS library ports
- chealyC/jlpt.api — thin FastAPI scaffold (N3–N5 endpoints, no curriculum UI)
- abebr/awesome-language-learning-roadmaps-persian — Persian roadmap list (library; prior bounce)
- AshrafFinstein/vaani-ai-language-learning — Phase-1 scaffold (prior bounce)
- minhtri2710/road-to-english — still stub README (~313 B; prior bounce)
- ABakdi/sublight — excellent plan vault but **docs-only M00**; language-learning is M09
- nasrudinz/MULAKE-releases — portable multilingual IME/on-screen keyboard (utility, not study)
- thalessantospsi-a11y/anki-turbinado — Brazilian concurso FSRS LMS (off prefer-lang / exam-CRM)
- alei37/dsh-cet6-tutor — CET-6 EN for CN learners inside DeepSeek DSH Cordis (host-locked; EN exam off prefer)
- chupikx228/ai-card-generator — generic FSRS demo decks (no L2 curriculum)
- pederbr/anki-farm — review→farm crop gamification novelty
- CodeAlpha / internship language-app shells (Aishwarya362, nishaahirrao731-maker, …)
- HSK spam content stubs (KangLaoShi/HSK4_*.dilfuza, u8bsq1nohh/jlpt “content”, nuriacalvo-teacher/hsk1–2 thin class pages)
- jlvalport/capitals-anki-srs — world capitals (geo, not L2)
- ethangreeney/atlas — country/flag FSRS (geo)
- SmartRichardSg/japanese-3-words-a-day — title-only stub
- Joe97400/mandarin-pocket-study / hifarhad/deutsch / topik-news — empty/near-empty READMEs
- Matchmaking / StudyIA / programming-language homework / Dart-Language-Learning / KoreanChess / WrapAndRoll restaurant

EDU_COUNT=3
alert=no
