# Field education hunt — 2026-09-21 scratch (Monday)
Window: ~2026-09-19 00:00 UTC → now (also late Sep 19–20 NEW URLs not already kept). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch for packet compiler.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): yulaoshizuikeai/wenyan-fsrs-recitation 10, 0xluden/note-furigana 9, sangpham2710/german 9. Sat KEEP skip: graywzc/live-trans, hherb/hanzitutor, Candice-Bennett/Carrot_Chunker. Fri KEEP skip: Multysquid/shisu-ko, anaidyss/zh-notes, CloudcoreZZH/shici-android. Thu KEEP skip: ColinHouse/kotobako, lavich/Tavelori, Hanayou/benkyou. Wed KEEP skip: bee-san/jlpt-levels-yomitan, dothuan-git/kotonoha-anki, onuross/anki-llm-pipeline. Overflow promote-watch continue (same URLs): manga_anki, typingchinese, language-learning-audio, simple-language-learning, hanzi-steps, jlpt-quiz, MMDL.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; repos in `seen-gh-repos-lower.txt`; Fri/Thu/Wed/Sat/Sun KEEP; noisy Ankit*/FSR/portfolio false positives; empty Rabbit_Hole.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) lifelonglearning123 / chineseleading_hsk (读报) — ZH news immersion HSK-gated + graded rewrite — PRIMARY
- who: lifelonglearning123 (named **读报**)
- url: https://github.com/lifelonglearning123/chineseleading_hsk
- date: created **2026-09-20** (~20:49Z)
- tags: education·immersion·generated-input·i-plus-one·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·immersion·generated-input·i-plus-one·quiet-when-nothing] score=10 | lifelonglearning123 / chineseleading_hsk (读报) | ZH news reader at **HSK 4**: NetEase Entertainment + China News Service feeds; word-seg via CC-CEDICT FMM (not Intl.Segmenter); **pinyin rubies only above your level**; tap → offline gloss/HSK/char breakdown; optional model explanation (collocations + i+1 example sentences, cached); **Rewrite at HSK 4** graded-reader mode (facts/names/numbers kept); My words flashcards with source sentence; “already know” adapts display off syllabus. Distinct from Sat Carrot_Chunker (book→Anki CSV) and Sun wenyan (classical cloze FSRS) — **live-news immersion + level-gated rubies + graded rewrite**. | https://github.com/lifelonglearning123/chineseleading_hsk
- why distinct: NEW URL day-0; ZH prefer; news immersion + HSK rewrite not on roster.
- bank: `2026-09-21-lifelonglearning123-读报-chinese-news-reader-hsk-gated` (learning)

### 2) Seonhaesoo / nihongo-dojo (日本語道場 / 일본어 도장) — KO→JA 12-week N5 PWA — STRONG
- who: Seonhaesoo (named **日本語道場**)
- url: https://github.com/Seonhaesoo/nihongo-dojo
- date: created **2026-09-20** (~14:39Z); Pages live
- tags: education·tutor-loop·generated-input·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·generated-input·teach-once] score=10 | Seonhaesoo / nihongo-dojo (日本語道場) | Offline PWA for Korean absolute beginners: **84-day / 12-week** syllabus hiragana→**JLPT N5**; 220 kana + stroke trace; ~860 vocab with KO false-friend notes; 104 N5 kanji KO音↔JA音; 53 grammar lessons w/ 8-item quizzes; reading×10 + listening×8 (TTS); weekly tests + 2 mock exams; **SRS** review; conjugation drills (ます/て/ない); JSON content + validate.mjs; zero deps; localStorage backup. Distinct from Sat live-trans (live captions) and Fri shisu-ko (YouTube→Yomitan) — **full KO-scaffolded N5 curriculum tutor**. | https://github.com/Seonhaesoo/nihongo-dojo
- why distinct: NEW URL day-0; JA prefer + KO L1 scaffold; named curriculum runner.
- bank: `2026-09-21-seonhaesoo-日本語道場-12-week-ko-ja-n5` (learning)

### 3) yong9875 / AnkiSub — video/audio subtitle→Anki immersion slicer — STRONG
- who: yong9875 (named **AnkiSub**)
- url: https://github.com/yong9875/AnkiSub
- date: created **2026-09-20** (~21:35Z)
- tags: education·immersion·generated-input·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·immersion·generated-input·quiet-when-nothing] score=9 | yong9875 / AnkiSub | Anki add-on: movies/TV/audiobooks → cards with **128kbps MP3 + screenshot**; embedded + external SRT/VTT/ASS; **bilingual subtitle alignment** by timestamp overlap; 200ms acoustic padding; SFX-tag filter; merge adjacent fragments ≤400ms; preview table + batch select; deck named after media; FFmpeg auto-locate / one-click download; Anki 23.10–26.x Qt6. Distinct from overflow manga_anki (manga panels) and Keno42 audio — **general immersion media slicer with bilingual align**. | https://github.com/yong9875/AnkiSub
- why distinct: NEW URL day-0; portable immersion gate for JA/ZH/any; named Anki runner.
- bank: `2026-09-21-yong9875-ankisub-video-audio-subtitle-slicer-for` (learning)

## Scored but NOT in top-3 SETUP slots (overflow)

### c6823821-sketch / shici-recite-app — score 9 (overflow; classical poetry FSRS — ZH twin under 读报 slot)
- url: https://github.com/c6823821-sketch/shici-recite-app
- date: created **2026-09-20**
- one-liner: Expo RN **诗词背诵**: ~21.7k offline poems (诗经/唐诗/宋词/全宋词); original/hint/blind modes; FSRS v6; local notes + optional API gloss; 今日荐诗 with local-candidate gate; fill-诗/词/曲 meter scoring (couyun + rhyme books). Strong ZH classical twin — overflow under 读报 (news immersion fills ZH primary); **swap over #3** if poetry FSRS preferred over AnkiSub; distinct from Sun wenyan (文言 progressive cloze textbooks) — poetry corpus + meter compose.

### lzzxccxxzzz / jitendex-yomitan-zh — score 8 (overflow; JA→ZH Yomitan dict pack)
- url: https://github.com/lzzxccxxzzz/jitendex-yomitan-zh
- one-liner: Unofficial Jitendex JP→ZH for Yomitan; 435k terms / 764k localized fields via local Qwen; Releases zip import. Library/wiki-craft — overflow (not interactive tutor).

### MQLite / hanzi-flip-classroom — score 8 (overflow; L1 primary classroom 识字)
- url: https://github.com/MQLite/hanzi-flip-classroom
- one-liner: Three.js 汉字奇遇岛 classroom proj: 汉语乐园/中文乐园 decks, flip + 组词 + 句子小火车; stroke replay; editable banks. L1 literacy classroom — edge of L2 lane → overflow.

### Vinger-lee / leap-framework — score 8 (overflow; MCP tutoring runtime FSRS — not prefer-lang L2 setup)
- url: https://github.com/Vinger-lee/leap-framework
- one-liner: State-driven agentic tutoring MCP (58 tools, FSRS retention, 260 tests). Portable mechanism but **not** a named JA/ZH/KO practice runner → overflow / gate-only.

### Loki-0228 / EZ-Reader — score 7 (overflow; EN reading for ZH speakers + Anki)
- url: https://github.com/Loki-0228/EZ-Reader
- one-liner: Edge/Chrome MV3 reader + DeepSeek gloss + Anki export. EN-for-ZH — not prefer-lang primary → overflow.

### CoderShibay / deutsch-lernen — score 7; ifelsetrueseal / jlpt-study — score 7; alanabdulkalaam25 / AniNLP — score 7; shogotomita / lingo-cards — score 7
- deutsch-lernen: thin static 1k DE cards (weaker than Sun german A1 Trainer).
- jlpt-study: Next.js JLPT radical mnemonic (KO desc); no README — AGENTS/TODO only; 215 hand examples → thin evidence.
- AniNLP: anime SRT → JLPT vocab stats dashboard (analyze-only).
- lingo-cards: multilingual SRS (HE/ES/FR/ZH ~1500) — thin vs named prefer curriculum.

### Promote-watch continues (same URLs — do not re-keep)
- heyanLE/manga_anki · CodeTrainerMan/typingchinese · Keno42/language-learning-audio · egriff90/simple-language-learning
- Weather-Mister/hanzi-steps · pandemonium0225/jlpt-quiz · ebriggsjohnson/MMDL
- shahsanket2107/livemandarin · fobeetsai/japanese-reader · rin-7777777/jlpt-exam-runner · mShono/finn_cards · yuktun/japanese-study · pekoqq/ReadLoops · gillisandrew/ancci · Dilnazzzz/bridge

### Same-URL KEEP watches (do not re-keep)
- Sun: wenyan-fsrs-recitation / note-furigana / german
- Sat: live-trans / hanzitutor / Carrot_Chunker
- Fri: shisu-ko / zh-notes / shici-android
- Thu: kotobako / Tavelori / benkyou
- Wed: jlpt-levels-yomitan / kotonoha-anki / anki-llm-pipeline

## Bounce
- Ankit* portfolios / FSR Parkinson / Escape-Immersion game / KoreaTariffAtlas (customs HSK) / Candice-Bennett/Rabbit_Hole (**empty repo**) / DecentCoders/Hsk4 thin static flashcards / anki-radar (Anki sync forum scout, not L2) / agyspeak (CLI voice buddy, not L2 named) / study-apps (成考 EN exam) / ai-language-tutor-v2 generic Gemini scenarios / german-learning-hub-vat-calculator thin / colanekojp training-portal (school portal) / n2-vocab thin list / HanziFlow / vh4/n2 (already overflow yesterday) / jlpttt empty / PiperTTS / anki-whatsapp

## Fetch notes
- GitHub MCP `search_repositories` + raw.githubusercontent.com READMEs (api.github.com unauth → rate-limit; Rabbit_Hole 409 empty)
- Dumps under `/workspace/field/edu0921/` (READMEs for KEEP + overflow; jlpt-study AGENTS/TODO)
- User-Agent FieldBot; window created:>2026-09-19 (+ created:2026-09-19 scan for late Sep 19 NEW)
- Truncated: remaining noisy Ankit*/java-learning / CAD / DL tutorials

## Result for compiler
- KEEP recommend TOP 3: chineseleading_hsk (读报) 10 · nihongo-dojo 10 · AnkiSub 9
- Overflow watch: shici-recite-app 9 · jitendex-yomitan-zh 8 · hanzi-flip-classroom 8 · leap-framework 8
- Alert: **none**
- EDU_COUNT for packet footer: **3**
