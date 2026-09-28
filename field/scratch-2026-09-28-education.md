# Field education hunt — 2026-09-28 (Asia/Taipei cron; box America/New_York Sun Sep 27 evening ET)

Window: `created:>2026-09-26` / `created:2026-09-27` / `created:2026-09-28` (GitHub MCP `cursor-github` search_repositories; split OR queries ≤5 ops; raw.githubusercontent.com README fetches → `/workspace/field/edu0928/`). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / immersion / i+1. Prefer JA/ZH/DE/VI/KO/FR/ES with named runner + portable mechanism. Combined ≥6 to keep. Cap: **at most ~3 SETUPS** for packet compiler.

Skip SEEN (`seen-gh-repos-lower.txt` ~354→379 + prompt list). Do NOT re-keep yesterday packet 45: kioxr/D-Learn, crsolver/kanji-battle, cuongtq17/hanyu. Overflow already SEEN: syedmuhammadtaha55/German_Vocab, cointugboat8211/deutsch-ueben, EricWay1024/book-watcher, soullovers2019-cloud/japanese-sensei-bot, keenanallaf-blckarrw/rooted-arabic, umeshchhabra/japanese-learning, Xthnavas/cognado, agregoire/italian-words, ericwwng/oshiete, Jcraxker/learn-speak, liviaaguiarcc/HanLevel, Anna023000/chinese-by-ear, sazardev/omarchy-english-toolkit, Krocosr/vocab, reepiceep/greek-tutor.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1. isa-aguilar / poligloti — score 10 · [education·tutor-loop·teach-once·prefer-DE·prefer-FR]
- one-line packet shape: **Local-first** patient AI speaking teacher (DE/EN/FR): talk or type; ≤3 gentle corrections/turn (teach-once); 9 practice modes (free chat, role-play, paste-text talk, read-aloud + minimal pairs, email/chat sim, idioms, book page-by-page, CEFR syllabus lessons); placement → 8 skills scored, weekly focus, level-up tests, **SRS vocab** return; plain-text learner folder you own; Docker local Ollama+speaches (Whisper STT + Piper TTS per L2) or any OpenAI-compatible cloud. | https://github.com/isa-aguilar/poligloti | created 2026-09-27
- Distinct-from: workwithlucas/frenchteacher (FR voice PWA) — this is **multi-L2 speaking desk with CEFR progress + local models**. Distinct from kioxr/D-Learn (DE screen-vision course) — speaking-first corrections, not screen mining. Distinct from Jcraxker/learn-speak (hackathon ES/EN Expo) — full syllabus + local-first.

### 2. t0rrentialrain / sentence-mining — score 9 · [education·i-plus-one·generated-input·immersion·prefer-KO]
- one-line: Claude Code **skill + Python** toolkit: Korean video (YouTube/IG/TikTok/Twitter/local) → yt-dlp + Soniox ASR + kiwipiepy tokenize → built-in **i+1 diff** vs known words (exactly one new word) → AnkiConnect cards; **Bank mode** mines local subs2srs `.apkg` for natural sentences+audio+screenshots; **Replace** swaps bad sentences in place (history field + relearn); **Audit** flags non-words / wrong-sense / dupes with `nid:` queries. | https://github.com/t0rrentialrain/sentence-mining | created 2026-09-27
- Distinct-from: liviaaguiarcc/HanLevel (KO text difficulty grader only) — this is **video→i+1 Anki miner**. Distinct from EricWay1024/book-watcher (ZH EPUB TTS) — KO sentence mining + AnkiConnect. Companion overflow: t0rrentialrain/cik-content-pipeline (CI Korean channel → apkg + known-word comprehension ranking).

### 3. NabiBukhsh-AI / lernbuch — score 9 · [education·teach-once·reveal-schedule·prefer-DE]
- one-line: Web **Lernbuch** (lernbuch.vercel.app) A1→B1 German study units: Overview → Vocab → Grammar → Classwork → Homework → Quiz; **never a bare noun** (article+plural colour-coded); cases marked under changed words; **Satzklammer drawn** under every example; every answer ships a *why*; mistakes strike-through wrong → highlight right; homework staged hints (nudge→rule→answer, free); **SRS** on missed words/rules; weak-skill named drills; vocab+grammar banks; cheatsheets; exam mode (Strasse≈straße note vs strict). Free, no email. | https://github.com/NabiBukhsh-AI/lernbuch | created 2026-09-27
- Distinct-from: kioxr/D-Learn (screen-aware Electron + FSRS from screen) — this is **visual grammar teach-once curriculum**. Distinct from syedmuhammadtaha55/German_Vocab (A1 SM-2 desk drills) — full lesson loop + Satzklammer/case visibility. Distinct from Wildchiken/vocab-de (FSRS article trainer overflow) — lesson+grammar first, not vocab-only.

## Overflow (≥6, below top-3 SETUP slots)

### Wildchiken / vocab-de — score 9 (overflow; prefer-DE FSRS desk)
- Browser offline German vocab: FSRS (85/90/95% retention), three card types (meaning / der·die·das auto-grade+speed / spelling unlock), article ending rules + compound head on miss, Goethe-list paste import, EN/ZH UI, optional Node SQLite or Cloudflare D1 sync. Prefer-DE but overlaps D-Learn/German_Vocab desk lane — thinner than Lernbuch curriculum. | https://github.com/Wildchiken/vocab-de | created 2026-09-27

### jonaylor89 / Parlo — score 9 (overflow; tutor-loop walk voice)
- Android Kotlin hands-free **Gemini Live** walk tutor: earbuds + pocket; barge-in; language/dialect/level/scenario/correction pickers; voice `save_vocab` / `switch_language`; session history+recap; encrypted key; strong MockWebServer tests. Any L2 via Gemini; no curriculum. | https://github.com/jonaylor89/Parlo | created 2026-09-27

### gaborkalmar83 / bilingua-tutor — score 9 (overflow; prefer-DE grammar map Android)
- Android store-ready sibling of LinguaMap: 331 offline grammar rules (NL/DE/FI/HU/EN) with *why*; Sentence Lab (verdict+roles+rules ✓/✕); Lucy conversational tutor (one mistake/turn); Reader; SM-2 or AnkiDroid; on-device Gemma 4 E2B default; 14 UI langs; Play one-off unlock. Heavy Play/Gemma path. | https://github.com/gaborkalmar83/bilingua-tutor | created 2026-09-27

### viola-delia / taiwan-mandarin-app — score 8 (overflow; prefer-ZH TOCFL PWA)
- Single-file offline PWA: Taiwan Mandarin (trad + zhuyin/pinyin), TOCFL levels, placement, lessons, Practice (review/flashcards/match/saved), Stories read-aloud, Daily Life role-plays, Hanzi Writer strokes, backup/restore. Distinct from cuongtq17/hanyu (Effortless English audio albums). | https://github.com/viola-delia/taiwan-mandarin-app | created 2026-09-27

### t0rrentialrain / cik-content-pipeline — score 8 (overflow; prefer-KO immersion batch)
- Resumable pipeline for Comprehensible Input Korean YT channel → per-line audio apkg + personalized watch order by *predicted comprehension* vs known words (kiwipiepy + KoFREN) + CEFR grading. Twin of sentence-mining. | https://github.com/t0rrentialrain/cik-content-pipeline | created 2026-09-27

### pedroaz / call-nina — score 8 (overflow; prefer-DE Codex desk)
- Local-first Electron DE path: SQLite learner folder, writing correction, reading/grammar, vocab review, Codex Voice handoff (no auto audio); MIT. Strong product docs; ChatGPT/Codex desktop required for AI. | https://github.com/pedroaz/call-nina | created 2026-09-27

### iqingyoung / openlango — score 8 (overflow; EN harness — off prefer-L2)
- Modular Next harness: CEFR five-dim θ, Article RSS→graded EN articles, Basic FSRS vocab + 102 grammar, Coach text/voice cascade, Anki apkg export, Docker. Strong portable gates; target L2 is English. | https://github.com/iqingyoung/openlango | created 2026-09-27

### Varsha0714 / startklar-deutsch — score 8 (overflow; prefer-DE Goethe exam)
- Phone-first Goethe A1/A2 practice: adaptive daily plan, Hören via device TTS, ~450 Goethe-theme words + SRS + der/die/das, reading/writing/speaking, EN help toggle. | https://github.com/Varsha0714/startklar-deutsch | created 2026-09-27

### shps961421-lang / n2-learning — score 8 (overflow; prefer-JA N2 Claude loop)
- Personal JLPT N2 sprint site: quiz→blindspot JSON→regenerate items (50% blindspot / 20% review / 30% new); built-in SRS cards; edge-tts listening from week 4; Claude Code 檢討 loop. | https://github.com/shps961421-lang/n2-learning | created 2026-09-27

### amuraru / deutsch — score 7 (overflow; prefer-DE telc A2/B1)
- Single `index.html` telc A2/B1 trainer: practice + timed mock; Lesen/Sprachbausteine/Hören (Web Speech) + Schreiben/Sprechen self-assess; localStorage progress. Original format content (links official telc mocks). | https://github.com/amuraru/deutsch | created 2026-09-27

### TomCardeLo / kana-practice — score 7 (overflow; prefer-JA kana from ES phonetics)
- Static ES→kana phonetic adapter (not translation) + romaji transcription drill with per-kana stats, row filters, Playwright tests. Starter kana only. | https://github.com/TomCardeLo/kana-practice | created 2026-09-27

### lstux / Slovingo-de-fr — score 7 (overflow; prefer-DE for FR kids)
- Slovingo Markdown course DE←FR for kids 8+: fiches/series/dialogues/exercises; 44 fiches in 6 series shipped; family experiment. Content pack not full app. | https://github.com/lstux/Slovingo-de-fr | created 2026-09-27

### OMKAR140706 / DeutschMate — score 6 (overflow; prefer-DE Gradio Gemini)
- Gradio Gemini DE companion: tool-calling save/retrieve vocab in SQLite + TTS; no FSRS yet. Thin vs Lernbuch/Call Nina. | https://github.com/OMKAR140706/DeutschMate | created 2026-09-27

### Ahsansabir143 / goethe-coach — score 7 (overflow; prefer-DE; no README)
- Recovered via `index.html`: Goethe A1·A2 25-day coach web app (article colours, drills). No README. | https://github.com/Ahsansabir143/goethe-coach | created 2026-09-27

### Therockasocka842 / language-learning-platform (LinguaArc) — score 6 (overflow; multi-track thin)
- Mandarin/JA/PR Spanish/FR/IT teaching-first dashboards; short README only. | https://github.com/Therockasocka842/language-learning-platform | created 2026-09-27

## Promote-watch
- **NEW watch:** isa-aguilar/poligloti · t0rrentialrain/sentence-mining · NabiBukhsh-AI/lernbuch (KEEP)
- **NEW watch:** Wildchiken/vocab-de, jonaylor89/Parlo, gaborkalmar83/bilingua-tutor, viola-delia/taiwan-mandarin-app
- **NEW watch:** pedroaz/call-nina (Codex path), t0rrentialrain/cik-content-pipeline, iqingyoung/openlango (EN but strong harness)
- **NEW watch:** kalorz/yomibu — WaniKani sync/offline status only; **reading-practice deferred** — recheck when generator lands
- **NEW watch:** Domingax/lekto (immersive reading — no README this pass), rponte357-pixel/japones-n5 + mon-atelier-francais (404 README), extube/notext (TUI — 404)
- Prior packet 45 KEEPs stay SEEN; do not re-keep.

## Bounce (library / spam / thin / off-lane)
- HSK*/hsk{aa,bw,c,d,ej,ff,h,hl,my,pt,t,vg,vu,z}* bulk `content` spam repos
- Goethe appointment bots; MailWizz deutsch; Deutschland Faktencheck / Stipendium DB / Ladeatlas
- xiaoh-mao/jlpt — Windows desktop of **official** 公式問題集 pages+audio (~370MB) — useful UI but copyright redistribution risk → bounce from KEEP
- goskey-mode/kanji-srs — Japanese **school homework** family SRS (photos of worksheet mistakes), not L2 learner product
- nobeatd/hangul-game — L1 Korean phonology card game for kids (자음/모음), not L2 hangul
- germanow/anki-idioms-trainer — EN idiom production from Anki (off prefer-L2)
- saleemsabeer/anki-lecture-pipeline / EricBriscoe/eidetic / ikristina/anki-mcp — generic Anki tooling, not L2 curriculum
- Programming / C_language_learning / Ziglings / cybersec tutors / STEM tutors / IELTS / aviation English / NorskLive / Slovene Anki / Finnish motorcycle quiz
- Game translations (Pokemon Gamma Emerald Deutsch, Danganronpa ES, Rubinite ES); Japan tourism / Korean food / Garry's Mod / truck DualSense immersion
- Flutter default shells; Ankit*/srs* content spam; peer tutoring platforms; EN Speaking Monkey / NotebookLM English tutor
- zachxwalton/Anki-Dolly-Grammar — 165b stub README
- ship-it-iesis/kanji-app — 11b README; amr-f-ramadan/eman-deutsch — 14b; hiaur/exctract_french_vocab — 23b
- chinoconmichelle/chinoconmichelle.github.io — class flashcards for one teacher (thin mechanism)

## Fetch failures (no README / empty / rate-limit)
- Ann928tech/Deutsch-Ai-tutor-, bastian3003/deutsch-lernen, Housseen/deutsche-regeln, pyhyper/TDict, Ommi14/KanjiApp, toshositsu-aikawa/kanji-gakusyu, kani-pixel/todoufuken-kanji, fritecocabigmac-debug/deutsch-quest, bilallzrague10-star/b2-deutsch, 6bzyfywm77-maker/deutsch-schule-, xavirodriguez/mandarin — no README (404)
- rponte357-pixel/mon-atelier-francais, rponte357-pixel/japones-n5, Domingax/lekto, extube/notext, igonzalezsecadas/pi-learn — no README this pass
- Ahsansabir143/goethe-coach — no README; recovered `index.html` → edu0928/Ahsansabir143-goethe-coach-index.html

SETUP_COUNT=3
alert=no
