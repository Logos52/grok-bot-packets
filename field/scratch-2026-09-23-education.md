# Field education hunt — 2026-09-23 (Asia/Saigon)

Window: created:2026-09-21 / created:2026-09-22 / created:>2026-09-21 (GitHub MCP `user-GitHub-xai` search_repositories). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3–5 education SETUPS**.

Skip SEEN (164 repos + scratch-seen-urls). Do NOT re-keep: tkober/kanji-trainer, hasharmujahid/deutsch-karten, Addicted2BayesianEpistemology/Parseh. Yesterday overflow already SEEN: rowland/mal, gabortardos/deutschmeister, heeyezzz/anki-flashcard, ruangustavo/pi-polyglot, ei06125/AnkiLinkedLearning, guoer11/ai-language-learning. Rabbit_Hole SEEN watch-only.

Same-URL KEEP watches (do not re-keep): chineseleading_hsk, nihongo-dojo, AnkiSub, wenyan-fsrs-recitation, note-furigana, german, live-trans, hanzitutor, Carrot_Chunker, shisu-ko, zh-notes, shici-android, kotobako, Tavelori, benkyou, jlpt-levels-yomitan, kotonoha-anki, anki-llm-pipeline.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. CaiqueGo / graded-reader — score 10 · [education·i-plus-one·generated-input·reveal-schedule·human-gate]
- one-line packet shape: Graded English reader that rewrites **any** pasted/URL text to a CEFR band, measures lemma coverage in code (analyze exit 1 = below threshold → retry), click-to-card (word/phrase), daily FSRS review queue (space reveal, 1–4 grade, undo, new-card cap), dashboard retention ladder, `reader export` → Anki CSV (`#tags column:3`, HTML-safe escape). Adaptation via local `claude` CLI **with tools stripped** (`--tools ""`) — untrusted article text cannot Write/Bash; same path as terminal `/adapt`. uv + spaCy `en_core_web_sm`; M0–M5 + web adapt marked ready; ruff/mypy/pytest gates. | https://github.com/CaiqueGo/graded-reader | created 2026-09-22
- Distinct-from: Parseh (Ilya Frank glossed immersion toolkit) — this is **coverage-gated graded rewrite + own FSRS + Anki export**, not Frank gloss layers. Distinct from kanji-trainer WK quiet-gate.

### 2. Mifune-Shioriko / ir4anki — score 9 · [education·teach-once·human-gate·reveal-schedule]
- one-line: Self-hosted Incremental Reading front door on **existing Anki** via AnkiConnect (no fork/migration). Markdown notes folder → heading chunks → hand-write QA/cloze into Anki with exact provenance in local sqlite; segment tree for recursive splits. **Preview gate (先看后考):** new cards land suspended; low-stakes read (Q shown, A hidden, no grade) → approve/defer; approved unsuspend **next day** so first graded review follows sleep (FSRS from real recall, not recognition illusion); daily release budget. Quick vs focus pacing (env-overridable). FastAPI + SolidJS/MD3; systemd user install. | https://github.com/Mifune-Shioriko/ir4anki | created 2026-09-22
- Distinct-from: anki-llm-pipeline / AnkiLinkedLearning (generate/mine cards) — this is **IR + delayed first grade** on the collection you already have.

### 3. RC-APC / Foreign-Language-Video-Learning-Assistant-B- — score 9 · [education·immersion·tutor-loop·reveal-schedule]
- one-line: MV3 Chrome/Edge extension: Bilibili + YouTube CC → clickable sentence list, dual-track (auto-prefer non-Chinese original), line shadowing with pause toggle, per-line audio download (tabCapture webm), click-word lookup / double-click save. Offline-first local dictionary import (GBK/UTF-8) + lemmatization; Eudic deep-link; online fallback. Vocab notebook with Leitner boxes (10m/1h/1d/3d/7d) + standalone `vocab.html`; all in `chrome.storage.local` — no account. Honest JA limit (space-less → whole sentence unit). | https://github.com/RC-APC/Foreign-Language-Video-Learning-Assistant-B- | created 2026-09-22
- Distinct-from: yong9875/AnkiSub (subtitle→Anki cards) — this is **in-browser shadow→lookup→Leitner notebook** without requiring Anki for the core loop. Distinct from live-trans (live speech).

## Overflow (≥6, below top-3 SETUP slots)

### sm-pranav / Nihongo-N5-JLPT-Study-App — score 9 (overflow; JA N5 single-file)
- Offline one-HTML N5: 222 kana / 99 kanji / 729 vocab / 96 grammar + mock exam; SM-2 daily limits; conjugation drill **shows rule on every mistake** (teach-once); missed exam items pushed to review; `NM.selfTest()` 39 checks; honest “no listening” gate. Strong JA prefer — overflow under graded-reader/ir4anki/video slots; **swap over #3** if offline beginner N5 preferred over video immersion. | https://github.com/sm-pranav/Nihongo-N5-JLPT-Study-App | created 2026-09-21
- Distinct-from: Seonhaesoo/nihongo-dojo (KO→JA N5 curriculum app) — this is **zero-to-N5 offline single-file + self-test honesty**.

### uminrae / korean-flashcards — score 8 (overflow; KO Yonsei float)
- Windows PyQt6 always-on-top KO cards: Yonsei 1–6 bundled **4,677 words** (11 fields + 4,069 hanja), J/K known/weak weighting, conjugation + particle highlight + pronunciation rules, edge-tts cache, clipboard translate drawer, heatmap. Prefer-KO twin under N5/video. | https://github.com/uminrae/korean-flashcards | created 2026-09-22
- Distinct-from: rowland/mal (macOS KO YAML banks) — this is **Yonsei curriculum float + J/K gate on Windows**.

### equwal / subread-dictionary — score 8 (overflow; JA Android Yomitan popup)
- Android process-text / share popup that reads Yomitan format-3 zips; longest-prefix lookup + Yomitan deinflector; local audio `android.db` (same as yomidevs local-audio); AGPL; `:core` Kotlin no-Android for reuse. Immersion mining on phone. | https://github.com/equwal/subread-dictionary | created 2026-09-22
- Distinct-from: bee-san/jlpt-levels-yomitan (dict level tagging) — this is **Android popup runner for Yomitan dicts**.

### creeperboo / anki-interactive-quiz — score 7 (overflow; force-Again quiz cards)
- Anki add-on: MC / T-F / cloze answered on review screen; wrong or “don’t know” → **forced Again** (overrides keyboard 3 / Good bar); mobile degrades to self-rate. Portable human-gate but EN/ZH study-tool not L2-curriculum. | https://github.com/creeperboo/anki-interactive-quiz | created 2026-09-22

### shogotomita / lingo-cards — score 6 (overflow; ES/FR/ZH/HE static SRS)
- Vanilla static SRS ~1500 cards/lang tourism+daily with conjugations; localStorage. Thin vs deutsch-karten. | https://github.com/shogotomita/lingo-cards | created 2026-09-21

### 3ammaar / armada-yomitan — score 6 (overflow; niche hardware)
- AYN Thor / Armada OS bottom-screen OCR + Yomitan + Anki mining; heavy AI-written disclaimer; JA dicts only tested. | https://github.com/3ammaar/armada-yomitan | created 2026-09-22

### argrig666 / anki-pronounce-selected — score 6 (overflow; TTS micro-addon)
- Anki Alt+C Edge neural TTS with lang auto-detect + conjugation-person field match; Linux/mpv. Useful micro but not a curriculum runner. | https://github.com/argrig666/anki-pronounce-selected | created 2026-09-22

### coracherry517 / babelgarden — score 6 (overflow / promote-watch; wiki-craft roadmap)
- Open language community: public diaries anyone can correct, no DMs; CEFR/FSRS/TOPIK/JLPT/HSK goals on roadmap; Next+Supabase live site. Mechanism nice, feature depth still early. | https://github.com/coracherry517/babelgarden | created 2026-09-21

### Arcade0101 / tcj-japanese — score 6 (overflow; personal furigana wiki)
- Class review sheets + quizzes with furigana/English toggles; Claude `/tcj` pipeline. Personal notes site, not portable product. | https://github.com/Arcade0101/tcj-japanese | created 2026-09-21

### zaykha / Personal-Flashcard-JLPT (Kotoba) — score 6 (overflow)
- Next/Firebase JLPT vocab SRS with CSV/XLSX import + merge-preserving SRS. Solid but generic Firebase flashcard. | https://github.com/zaykha/Personal-Flashcard-JLPT | created 2026-09-21

## Promote-watch continues (same URLs — do not re-keep)
- Candice-Bennett/Rabbit_Hole (SEEN — HanLP/HSK→Anki for Carrot_Chunker; watch-only)
- Prior watches from scratch-2026-09-21/22: manga_anki, typingchinese, language-learning-audio, simple-language-learning, hanzi-steps, jlpt-quiz, MMDL, shici-recite-app, jitendex-yomitan-zh, hanzi-flip-classroom, leap-framework, gillisandrew/ancci
- **NEW watch:** babelgarden (community diary-correct loop — revisit when reading/FSRS ship)
- **NEW watch:** equwal/subread-dictionary (if Android JA mining becomes roster need)

## Bounce (library / spam / thin / off-lane)
- Truncated Ankit* name spam + AnkiDeckSearch portfolios (kai324620-create/Anki exercise, Ankita* profiles, nursing-home, etc.)
- Daii1414/yomitan-dictionaries — Telegram dict catalog (library)
- abebr/awesome-language-learning-roadmaps-persian — Persian roadmap list (library)
- SokolskyNikita/brainscape-language-cards — Brainscape CSV dumps + audit workspaces (library)
- AshrafFinstein/vaani-ai-language-learning — Phase-1 scaffold only (auth/dashboard)
- minhtri2710/road-to-english — pre-launch stub README
- Zoehong11/anki — 46-byte README (“german workflow” claim, empty)
- VrishaanganVS/Wortwerk — stock create-next-app README
- Joel05-max/german-a1-c2-lms — README 404 / unauth API rate-limit on contents
- asutekku/sabiyomi — excellent furigana/romaji **library/CLI** (not a study runner) → library bounce
- ethanwchen/anki-fly — novelty mascot (prior bounce)
- bakterian/AnkiDectEditor — bulk AnkiWeb editor (utility, not L2)
- Matchmaking / CodeAlpha internship shells / Dominate-Quizlet spam / StudyIA generic / programming-language homework
- abubakirbatyrbek-boop/kz-language — ZH for Kazakh/Russian LMS (Supabase); curriculum but thin EN docs / off prefer-lang framing → soft bounce
- viscontti/Puska — furigana karaoke claim but README 404
- hanqinilnix/ankiweb, naiaraamorim/flashcard-anki, Folli69/Anki-ish-kort — thin personal decks

## Fetch notes
- MCP: `user-GitHub-xai` search_repositories worked (preferred). Unauth `api.github.com` hit rate-limit late on Joel05-max contents — used raw.githubusercontent.com for READMEs.
- Queries split: anki language / SRS Japanese / HSK Anki / JLPT / deutsch Anki / language learning / flashcard Python / immersion|graded|furigana|yomitan|FSRS / japanese|kanji / chinese HSK|vietnamese|deutsch|french / yomitan|furigana|jlpt created:2026-09-21|22.
- `/workspace/field/edu0923` was a 0-byte **file** at start; removed and recreated as directory. READMEs saved under `/workspace/field/edu0923/<owner>-<repo>-readme.md`.
- Bank deposits (lane learning, via grok-bot/Field) for TOP 3 KEEP only; INDEX was empty for those URLs before deposit.
- Ankit* / payment-hsk / SEO trainer spam truncated as instructed.

## Result for compiler
- **KEEP:** CaiqueGo/graded-reader 10 · Mifune-Shioriko/ir4anki 9 · RC-APC/Foreign-Language-Video-Learning-Assistant-B- 9
- **EDU_COUNT:** 3
- **Overflow watch:** Nihongo-N5 9 · korean-flashcards 8 · subread-dictionary 8 · anki-interactive-quiz 7 · lingo-cards 6 · armada-yomitan 6 · anki-pronounce-selected 6 · babelgarden 6 · tcj-japanese 6 · Kotoba/JLPT 6
- **alert:** none
