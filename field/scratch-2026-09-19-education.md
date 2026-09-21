# Field education hunt — 2026-09-19 scratch (Saturday)
Window: ~2026-09-18 00:00 UTC → now (also late Sep 17 NEW URLs not already kept). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): Multysquid/shisu-ko 10, anaidyss/zh-notes 9, CloudcoreZZH/shici-android 8. Thu KEEP skip: ColinHouse/kotoba-studio → **kotobako** rename, lavich/Tavelori, Hanayou/benkyou. Wed KEEP skip: bee-san/jlpt-levels-yomitan, dothuan-git/kotonoha-anki, onuross/anki-llm-pipeline. Overflow promote-watch continue (same URLs).

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; repos in `seen-gh-repos-lower.txt`; Fri/Thu/Wed KEEP; noisy Ankit*/FSR/DLSS/portfolio false positives.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) graywzc / live-trans (LiveTrans) — live JA captions + furigana + EN on own GPU — PRIMARY
- who: graywzc (named **LiveTrans**)
- url: https://github.com/graywzc/live-trans
- date: created **2026-09-18** (~22:21Z); window through **2026-09-19** ~00:15Z (CI + release badge active)
- tags: education·immersion·generated-input·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·immersion·generated-input·quiet-when-nothing] score=10 | graywzc / live-trans (LiveTrans) | macOS live Japanese captions for system audio (BlackHole): Mac captures + draws; **Whisper large-v3 + ollama** on **your own GPU** over ssh (Tailscale OK); furigana over kanji + English under; auto Multi-Output Device switch; idle timeout frees GPU; brew cask + Releases + CI. Distinct from Fri shisu-ko (YouTube→Yomitan DOM mine) and overflow livemandarin (ZH call captions) — **JA live furigana+translate captions, local GPU**. | https://github.com/graywzc/live-trans
- why distinct: NEW URL day-0; JA prefer; immersion twin but different language + furigana/LLM-split vs livemandarin.
- bank: `2026-09-19-graywzc-livetrans-live-japanese-captions-furigana-en` (**deposited** learning; body `/workspace/field/bank-bodies/2026-09-19-live-trans.txt`)

### 2) hherb / hanzitutor (Hanzi Tutor) — offline stroke geometry grader + SM-2 — STRONG
- who: hherb (named **Hanzi Tutor**)
- url: https://github.com/hherb/hanzitutor
- date: created **2026-09-18** (~14:18Z); window through ~23:59Z
- tags: education·tutor-loop·quiet-when-nothing·teach-once·human-gate
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·quiet-when-nothing·teach-once] score=10 | hherb / hanzitutor (Hanzi Tutor) | Offline Tauri/Rust+Svelte desktop: write simplified hanzi (mouse/stylus); grades **shape + placement + stroke order** via Hungarian pairing + Kendall inversions (no ML/network at runtime); Trace vs Recall modes; 7574 teachable chars / 775 lessons; personal vocab list; **SM-2** review queue; corrupt JSON **refuses overwrite**; 136+ tests + full-dataset selfcheck. Distinct from Fri shici (EN-ZH FSRS phone dict) and zh-notes (lesson CLI) — **fail-honest offline handwriting tutor**. | https://github.com/hherb/hanzitutor
- why distinct: NEW URL day-0; ZH prefer; geometric stroke-order portable gate not on roster.
- bank: `2026-09-19-hherb-hanzi-tutor-offline-stroke-order-shape` (**deposited**; body `/workspace/field/bank-bodies/2026-09-19-hanzitutor.txt`)

### 3) Candice-Bennett / Carrot_Chunker (Carrot Chunker) — ZH book→HanLP→freq-gate Anki — STRONG (day-0)
- who: Candice-Bennett (named **Carrot Chunker**)
- url: https://github.com/Candice-Bennett/Carrot_Chunker
- date: created **2026-09-18** (~20:23Z); pushed ~22:32Z
- tags: education·generated-input·i-plus-one·quiet-when-nothing·human-gate
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·generated-input·i-plus-one·quiet-when-nothing] score=9 | Candice-Bennett / Carrot_Chunker | Pre-learn vocab from a Chinese `.txt`/`.epub` before reading: clean → **HanLP** segment → min_count / percentile / **top_cutoff_rank** frequency gates → Yomitan/CC-CEDICT lookup → CSV with Hanzi/Pinyin/def/count/rank + **bolded example from your book**; optional **AnkiConnect dedupe**; chapter picker (`第…章`). Distinct from Fri zh-notes (lesson vault CLI) and overflow eudic-anki-sync (sync bridge) — **own-book i+1 Anki prep runner**. | https://github.com/Candice-Bennett/Carrot_Chunker
- why distinct: NEW URL day-0; ZH prefer; book-sourced frequency-gated mining not on roster.
- bank: `2026-09-19-candice-bennett-carrot-chunker-chinese-book-epub-hanlp` (**deposited**; body `/workspace/field/bank-bodies/2026-09-19-carrot-chunker.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### heyanLE / manga_anki — score 9 (overflow; JA manga OCR→Anki factory)
- url: https://github.com/heyanLE/manga_anki
- date: created **2026-09-18** (~15:00Z)
- tags: education·immersion·human-gate·quiet-when-nothing·generated-input
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Per-manga project factory: local pages → manga-ocr → Sudachi → freq filter → **assistant Chinese gloss/review gate** → JLPT reference (non-official, fail-honest) → Anki/HTML; validate before replace `output/current`; 21 tests. Strong immersion twin — overflow to diversify (live captions + handwriting already fill slots); **swap candidate over #3** if JA manga mine preferred over ZH book chunker.

### CodeTrainerMan / typingchinese (Pinyin Type) — score 9 (overflow; ZH typing + FSRS)
- url: https://github.com/CodeTrainerMan/typingchinese
- date: created **2026-09-18** (~09:53Z); demo typingchinese.club
- tags: education·tutor-loop·teach-once·i-plus-one
- portable / evidence / combined: **4 / 5 / 9**
- alert: **no**
- one-liner: Browser ZH typing: follow/dictation/self-test/write-from-meaning; full/initials/tones; graded articles; mistakes → **FSRS**; localStorage; 14 UI langs. Strong typed-retrieval — overflow under handwriting+book-prep ZH stack; swap over #3 if interactive typing preferred.

### Keno42 / language-learning-audio (audiolesson) — score 8 (overflow; audio-first production)
- url: https://github.com/Keno42/language-learning-audio
- date: created **2026-09-18**; pushed through ~23:18Z
- one-liner: Prompt → **silence for spoken answer** → model answer TTS; expanding reactivation inside lesson + persistent learner model; curricula fr-en / fr-ja / is-en. Portable production-gate — not prefer-lang primary (FR/IS) → overflow; note fr-ja curriculum adjacent.

### egriff90 / simple-language-learning (Sentences) — score 8 (overflow; DE cloze literature)
- url: https://github.com/egriff90/simple-language-learning
- date: created **2026-09-18** ~23:56Z (day-0)
- one-liner: Cloze from Gutenberg classics (Kafka/Storm/…) + simple SRS; DE 420 + PT 247 cards; ß/ss equivalent; drip 10/day. **DE prefer** graded input — overflow (thin vs top immersion/write picks); swap over #3 if DE literature cloze wanted.

### TuanTuan2507 / meikipop-vietnamese — score 8 (overflow; VI meikipop + JLPT quiz)
- url: https://github.com/TuanTuan2507/meikipop-vietnamese
- date: created **2026-09-18**
- one-liner: Screen-OCR JA dict fork + N2/N3/N4 mimikara resources + learning_quiz GUI. Prefer-adjacent JA — overflow (fork + VI L1; not day-0 mechanism unique enough for slot).

### danielt998 / mandarin-game (Hanzi Hop) — score 7 (overflow)
- url: https://github.com/danielt998/mandarin-game
- one-liner: Mobile-first ZH sentence-match + Nuance Lab contrast cards; Tatoeba fallback; localStorage. Thin vs typingchinese/hanzitutor → overflow.

### Dj-Polyester / JP-Organizer — score 7 (overflow; MCP Anki org tooling)
- url: https://github.com/Dj-Polyester/JP-Organizer
- one-liner: MCP→AnkiConnect JA deck hierarchy (mimetics/idioms/collocations) with JMdict-first + LLM fallback handshake. Strong tooling — not learner practice loop → overflow/library-adjacent.

### schuerzli / JapaneseDrills — score 7 (overflow; Android conjugation)
- url: https://github.com/schuerzli/JapaneseDrills
- one-liner: Kotlin Compose verb/adj conjugation quiz (romaji+furigana); no public README (CLAUDE.md only). Thin day-0 → overflow.

### zmzmzzmm / jlpt-n1-daily — score 7 (overflow; AI regenerating N1 sets)
- url: https://github.com/zmzmzzmm/jlpt-n1-daily
- one-liner: 4 built-in N1 sets then OpenAI generates next (avoid last-3 themes); access-code gate. Generated-input adjacent — cloud-key dependent → overflow.

### xbzz1018 / learningloop — score 7 edge (ZH FSRS agent harness demo)
- url: https://github.com/xbzz1018/learningloop
- one-liner: Personal learning assistant with FSRS + HITL plan approval + ZH skills; more harness showcase than named L2 practice → edge overflow.

### sensai7 / blue-sora — score 7 (overflow; Aozora corpus→reader pipeline)
- url: https://github.com/sensai7/blue-sora
- one-liner: Public-domain JA literature ingest → difficulty metrics → static reader/EPUB/PDF. Strong wiki-craft pipeline — early site; overflow vs live practice runners.

### float3 / ankiquest — score 6 (library/gamification)
- url: https://github.com/float3/ankiquest
- one-liner: XP/quests for Anki review logs (no card content) — not L2 named practice → bounce/library.

### Promote-watch continues (same URLs — do not re-keep)
- shahsanket2107/livemandarin — **2026-09-18** ~16:53Z push — continue overflow (ZH call captions); LiveTrans is JA twin this hunt.
- fobeetsai/japanese-reader — push **2026-09-18** ~02:06Z — continue promote.
- rin-7777777/jlpt-exam-runner — idle since Sep 17 create window — continue.
- mShono/finn_cards — **2026-09-18** ~13:14Z push — polish continue.
- yuktun/japanese-study — **2026-09-18** ~23:40Z — content wiki continue.
- pekoqq/ReadLoops — still idle since **2026-09-16**.
- gillisandrew/ancci — idle since **2026-09-14**.
- Dilnazzzz/bridge — **still idle** since 2026-09-10.
- anonymouspartner/capybara-anki — **2026-09-18** ~15:35Z polish — continue.
- xmonkey/paperback — idle since Sep 17 — continue.
- ydd0729/eudic-anki-sync / Daiwa-Scholars…/n2-grammar-drill / gehbfarr5/ielts-vocab-automation / piggyham/BlinkWord / bannysway/grab-series-vocab — same-URL continue.

### Same-URL / Fri+Thu+Wed KEEP watches (do not re-keep)
- Multysquid/shisu-ko / anaidyss/zh-notes / CloudcoreZZH/shici-android — Fri KEEP skip.
- ColinHouse/kotobako (rename of kotoba-studio) / lavich/Tavelori / Hanayou/benkyou — Thu KEEP skip.
- bee-san/jlpt-levels-yomitan / dothuan-git/kotonoha-anki / onuross/anki-llm-pipeline — Wed KEEP skip.

## BOUNCE list (url | why)
- https://github.com/bee-san/yomitan-export-to-zip | Yomitan ZIP rebuild tooling — not learner practice loop
- https://github.com/jimbuschman/cozmo-stack | Anki Cozmo robot RE — not L2
- https://github.com/jacobcassidy/anki-cassidy-swe-editor-addon | SWE flashcard editor hotkeys — not L2
- https://github.com/AndrewBuildsNYU/archway-flashcards | lecture→Anki CSV — not prefer-lang
- https://github.com/Ninas-Nexus/ANKICARDS | empty/thin HTML
- https://github.com/michaelatamuk/openjiuwen-knowledge | AI-eng knowledge base w/ Anki export — not L2
- https://github.com/elatier/lithuanian-a2-anki | Lithuanian — not prefer-lang
- https://github.com/29556forTaruy/Anki | generic Anki-alike scaffold
- https://github.com/ankita-majhi/ankita-portfolio | Ankit* portfolio FP
- https://github.com/ankitsharma957685-alt/Ankit-kumar | Ankit* FP
- https://github.com/ankitdas37/ANKIT.DEV-portfolio | Ankit* FP
- https://github.com/ankitmishra105/ankit-mishra.github.io | Ankit* FP
- https://github.com/Amirsaifi786/ankitbirthday | Ankit* FP
- https://github.com/ankit-git-30/ANKIT-SMAS-python-assignment | Ankit* FP
- https://github.com/guguker/ML-Cards | ML study cards — not L2
- https://github.com/dhivya-1010/OA-Simulation | FSR pressure sensors — FP
- https://github.com/kennethwaldmer-ship-it/optidrop | OptiScaler FSR/DLSS — FP
- https://github.com/romanticocobra39/Zkanji | download-bait marketing README
- https://github.com/Churrisurf/Conversational-AI | thin LangChain+VOICEVOX tutor script; no README
- https://github.com/dngs/voice_recall | single HTML voice-recite compare; no README
- https://github.com/abdomoss113-dot/German-French-Learning-App | README 404
- https://github.com/dmbina/jlpt-n4-companion | README essentially empty
- https://github.com/Methyldioxymethamphetamine/jlpt_learning_app | unnamed thin Kotlin
- https://github.com/hitlarlalon38-cpu/N4-JLPT-flashcards | thin
- https://github.com/kong123485-beep/JLPT | thin HTML
- https://github.com/jlptmasterjm-cpu/jlpt-data-1 | content backup dump
- https://github.com/Iskanderrus/anki-cards-collector | collector tooling
- https://github.com/nicholasbeskow/manhattanki-data | card pool data only
- https://github.com/float3/ankiquest | Anki XP gamification — not L2 practice
- https://github.com/akhilmadipalli/Bilingle | Omegle-for-languages day-0 empty
- https://github.com/MehenniInes/myna-lingo | generic platform claim
- false-positive Ankit*/portfolio / FSR/DLSS / git-tutorial / immersion-HUD / baptism | name/topic noise
- X / Gmail / Slack / Firecrawl | not used this hunt

## FETCH NOTES
- `gh` CLI unauthenticated on box → GitHub MCP `search_repositories` + `curl` API with User-Agent; search dumps under `/workspace/field/edu0919/s01–s08-*.json`; READMEs under `edu0919/readmes/`; KEEP API meta under `edu0919/api/`.
- Search rate: unauthenticated ~10/min; paced sleeps; remaining dipped to 2 then recovered. Truncated noisy Ankit*/FSR/portfolio hits (listed bounce).
- s07 korean/deutsch/finnish anki created:>2026-09-17 returned **0** clean hits (prefer-lang anki sparse this window; DE covered via Sentences cloze).
- Promote-watch atoms: finn_cards Sep 18 push; yuktun Sep 18; livemandarin Sep 18; japanese-reader Sep 18; capybara Sep 18; ReadLoops idle Sep 16; ancci idle; bridge still Sep 10.
- Truncations / misses: German-French-Learning-App README 404; jlpt-n4-companion empty README; Conversational-AI / voice_recall no README; JapaneseDrills README absent (used CLAUDE.md); meikipop-vietnamese README still upstream-shaped (quiz code present).
- Bank deposits: **succeeded** for live-trans, hanzitutor, Carrot_Chunker → `raw/learning/2026-09-19-*` + INDEX. Bodies at `/workspace/field/bank-bodies/2026-09-19-{live-trans,hanzitutor,carrot-chunker}.txt`.
- scratch-seen-urls.txt / seen-gh-repos-lower.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) live-trans **10**, (2) hanzitutor **10**, (3) Carrot_Chunker **9**.
- Overflow scored ≥6 not in top-3: manga_anki **9**, typingchinese **9**, language-learning-audio **8**, Sentences **8**, meikipop-vietnamese **8**, Hanzi Hop **7**, JP-Organizer **7**, JapaneseDrills **7**, jlpt-n1-daily **7**, learningloop **7**, blue-sora **7**; livemandarin/japanese-reader/jlpt-exam-runner/finn_cards/yuktun continue; ancci/bridge idle; capybara/paperback continue.
- **Swap notes:** (a) prefer manga_anki **9** over Carrot #3 if JA manga OCR→Anki human-gate wanted; (b) prefer typingchinese **9** over Carrot if interactive ZH FSRS typing preferred; (c) prefer Sentences **8** over Carrot if DE literature cloze preferred; (d) do **not** re-keep Fri/Thu/Wed KEEP or kotobako rename. Do **not** drop #1 or #2 without reason.
- Explicit bounce-deltas on prior keeps: Fri three KEEP = skip; Thu three = skip (kotobako rename); Wed three = skip.
- Alert-line item: **none**.

## PACKET READY
1. [education·immersion·generated-input·quiet-when-nothing] score=10 | graywzc / live-trans (LiveTrans) | Live JA captions with furigana+EN via local GPU Whisper/ollama over ssh; BlackHole system audio. | https://github.com/graywzc/live-trans
2. [education·tutor-loop·quiet-when-nothing·teach-once] score=10 | hherb / hanzitutor (Hanzi Tutor) | Offline stroke shape/placement/order grader (Hungarian+Kendall) + SM-2; refuse-overwrite corrupt stores. | https://github.com/hherb/hanzitutor
3. [education·generated-input·i-plus-one·quiet-when-nothing] score=9 | Candice-Bennett / Carrot_Chunker | ZH book/epub → HanLP → frequency gates → Anki CSV with book examples + AnkiConnect dedupe. | https://github.com/Candice-Bennett/Carrot_Chunker

## Result for compiler: 3 KEEP
1. graywzc/live-trans — 10 — LiveTrans JA live captions furigana+EN local GPU
2. hherb/hanzitutor — 10 — offline ZH handwriting stroke grader + SM-2
3. Candice-Bennett/Carrot_Chunker — 9 — ZH book→freq-gate Anki prep
