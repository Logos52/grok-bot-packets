# Field education hunt — 2026-09-20 scratch (Sunday)
Window: ~2026-09-19 00:00 UTC → now (also late Sep 18 NEW URLs not already kept). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch for packet compiler.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): graywzc/live-trans 10, hherb/hanzitutor 10, Candice-Bennett/Carrot_Chunker 9. Fri KEEP skip: Multysquid/shisu-ko, anaidyss/zh-notes, CloudcoreZZH/shici-android. Thu KEEP skip: ColinHouse/kotobako, lavich/Tavelori, Hanayou/benkyou. Wed KEEP skip: bee-san/jlpt-levels-yomitan, dothuan-git/kotonoha-anki, onuross/anki-llm-pipeline. Overflow promote-watch continue (same URLs): manga_anki, typingchinese, language-learning-audio, simple-language-learning.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; repos in `seen-gh-repos-lower.txt`; Fri/Thu/Wed/Sat KEEP; noisy Ankit*/FSR/portfolio false positives.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) yulaoshizuikeai / wenyan-fsrs-recitation (文言背诵 / WenYan Recitation) — classical ZH FSRS-5 + progressive cloze — PRIMARY
- who: yulaoshizuikeai (named **文言背诵**)
- url: https://github.com/yulaoshizuikeai/wenyan-fsrs-recitation
- date: created **2026-09-19** (~13:18Z); Releases + CI badge active
- tags: education·tutor-loop·generated-input·i-plus-one·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·generated-input·i-plus-one·quiet-when-nothing] score=10 | yulaoshizuikeai / wenyan-fsrs-recitation (文言背诵) | Offline native Android: high-school classical Chinese (文言) recitation — **11 textbook modules / 100 poems** incl. gaokao **72必背**; dual track (flip flashcards + **5-level progressive cloze** L0原文→L4全盲); **FSRS-5** Again/Hard/Good/Easy with live interval badges; book picker + heatmap streak; 80 unit tests + GitHub Actions APK Releases; 100% offline. Distinct from Sat hanzitutor (stroke geometry) and Carrot_Chunker (book vocab Anki) — **classical ZH progressive-cloze FSRS tutor**. | https://github.com/yulaoshizuikeai/wenyan-fsrs-recitation
- why distinct: NEW URL day-0; ZH prefer; progressive cloze + FSRS-5 classical corpus not on roster.
- bank: `2026-09-20-yulaoshizuikeai-wenyan-fsrs-recitation-classical-chinese` (learning)

### 2) 0xluden / note-furigana — note.com JA furigana + real examples never generated — STRONG
- who: 0xluden (named **note furigana**)
- url: https://github.com/0xluden/note-furigana
- date: created **2026-09-19** (~18:50Z)
- tags: education·immersion·generated-input·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·immersion·generated-input·quiet-when-nothing] score=9 | 0xluden / note-furigana | Chrome/Brave extension for **note.com** articles: furigana over kanji in title+body only (`note.com/<user>/n/<id>`); hover → JP→EN meaning + JLPT level + up to 3 **real** example sentences; kuromoji.js bundled offline for split/readings; Jisho for gloss; Tatoeba→Massif fallback; **examples never LLM-generated**; chrome-extension `path.join` patch documented; `node test.js`. Distinct from Sat live-trans (system-audio captions) and Fri shisu-ko (YouTube→Yomitan) — **note.com immersion + corpus-only examples**. | https://github.com/0xluden/note-furigana
- why distinct: NEW URL day-0; JA prefer; note.com-scoped immersion gate.
- bank: `2026-09-20-0xluden-note-furigana-note-com-extension` (learning)

### 3) sangpham2710 / german (German A1 Trainer) — DE conjugation/cases + FSRS + Anki — STRONG
- who: sangpham2710 (named **German A1 Trainer**)
- url: https://github.com/sangpham2710/german
- date: created **2026-09-19** (~09:34Z)
- tags: education·tutor-loop·generated-input·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·tutor-loop·generated-input·teach-once] score=9 | sangpham2710 / german (German A1 Trainer) | Local DE A1 trainer: verb conjugation (933 sentences / 311 verbs by Netzwerk chapters), listening (numbers/umlauts/phone), Akk/Dat cases, number writing; **FSRS** SRS state; Anki generator from **CEFR Goethe + Netzwerk**; DWDS/Wiktionary enrichment pipeline; TUI menu; DE/EN toggle. Distinct from Sat overflow simple-language-learning (DE cloze literature) — **interactive DE production games + Anki export**. | https://github.com/sangpham2710/german
- why distinct: NEW URL day-0; **DE prefer**; production-game + FSRS + Anki pipeline.
- bank: `2026-09-20-sangpham2710-german-a1-trainer-fsrs-anki` (learning)

## Scored but NOT in top-3 SETUP slots (overflow)

### Weather-Mister / hanzi-steps — score 9 (overflow; TW Mandarin curriculum + stroke)
- url: https://github.com/Weather-Mister/hanzi-steps
- date: created **2026-09-19**
- one-liner: Traditional Chinese / Taiwanese Mandarin progressive course (Units 1–4): AnimCJK ZhHant glyphs + Hanzi Writer stroke matcher; Sinica frequency vocab goal; character intro/trace/missing-strokes; structural validation + D1 progress. Strong ZH twin — overflow under wenyan slot (classical FSRS already fills ZH primary); **swap over #3** if TW curriculum preferred over DE games.

### pandemonium0225 / jlpt-quiz — score 8 (overflow; Notion→quiz, no AI)
- url: https://github.com/pandemonium0225/jlpt-quiz
- one-liner: Own Notion JA articles/grammar → daily GitHub Actions quiz rebuild to Pages; bolded vocab cloze + grammar distractors; no LLM; TW 07:00 cron. wiki-craft — overflow.

### ebriggsjohnson / MMDL — score 8 (overflow; macOS Dictionary→Anki)
- url: https://github.com/ebriggsjohnson/MMDL
- one-liner: Anki addon fills fields from local Dictionary.app; curated 现代汉语规范词典 preset (pinyin/POS/defs); no overwrite by default; Fill Deck undoable. Library-adjacent ZH Anki glue — overflow.

### klb299 / cet4-word-miner — score 7 (overflow; CET-4 EN for ZH speakers)
- url: https://github.com/klb299/cet4-word-miner
- one-liner: CET-4 exam corpus → freq-gated vocab with real exam sentences → HTML/Anki. EN-for-ZH — not prefer-lang primary → overflow.

### aayushhh13 / jlpt-kotoba-card — score 7; vh4 / n2 — score 7; HanziFlow — score 6 (thin/static HSK cards)
- overflow / bounce thin flashcard shells.

### Promote-watch continues (same URLs — do not re-keep)
- heyanLE/manga_anki · CodeTrainerMan/typingchinese · Keno42/language-learning-audio · egriff90/simple-language-learning
- shahsanket2107/livemandarin · fobeetsai/japanese-reader · rin-7777777/jlpt-exam-runner · mShono/finn_cards · yuktun/japanese-study · pekoqq/ReadLoops · gillisandrew/ancci · Dilnazzzz/bridge

### Same-URL KEEP watches (do not re-keep)
- Sat: live-trans / hanzitutor / Carrot_Chunker
- Fri: shisu-ko / zh-notes / shici-android
- Thu: kotobako / Tavelori / benkyou
- Wed: jlpt-levels-yomitan / kotonoha-anki / anki-llm-pipeline

## Bounce
- Ankit* portfolios / FSR Region-Templates / ogs-to-anki (Go game) / sm2-fsrs-convert (library converter) / medhara_ios (PKM not L2) / Zenew (university course FSRS, not L2 prefer) / ReCast (EN speaking for ES speakers) / cloze-bridge (generic cloze tooling) / spanish-anki / spanish-flashcards / EnglishWords / anki-whatsapp / PiperTTS thin / jlpttt empty / n5-suhbat no README

## Fetch notes
- GitHub MCP `search_repositories` + raw.githubusercontent.com READMEs (api.github.com/readme → 403; unauth meta → rate-limit after searches)
- Dumps under `/workspace/field/edu0920/` (search-anki via MCP; search-ja/ko/de/zh/immersion curl; READMEs)
- `gh` unauth; User-Agent FieldBot
- Window created:>2026-09-18 / 2026-09-19
- Truncated: remaining noisy Ankit*/ncreighton Notion spam / Linux-Quest / CAD tutors

## Result for compiler
- KEEP recommend TOP 3: wenyan-fsrs-recitation 10 · note-furigana 9 · german 9
- Overflow watch: hanzi-steps 9 · jlpt-quiz 8 · MMDL 8 · cet4-word-miner 7
- Alert: **none**
- EDU_COUNT for packet footer: **3**
