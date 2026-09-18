# Field education hunt — 2026-09-18 scratch (Friday)
Window: ~2026-09-17 00:00 UTC → now (also late Sep 16 NEW URLs not already kept). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): ColinHouse/kotoba-studio 10, lavich/Tavelori 9, Hanayou/benkyou 8. Note: **kotoba-studio 301→ ColinHouse/kotobako** (same created 2026-09-16T00:27Z) — rename, not a new mechanism. Wed KEEP skip: bee-san/jlpt-levels-yomitan, dothuan-git/kotonoha-anki, onuross/anki-llm-pipeline. Overflow promote-watch continue (same URLs).

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; repos in `seen-gh-repos-lower.txt`; yesterday/Wed KEEP; noisy Ankit*/FSR/DLSS/portfolio false positives.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) Multysquid / shisu-ko — live JA YouTube Whisper→Yomitan DOM→one-key Anki mine — PRIMARY
- who: Multysquid (named **Shisu-ko**)
- url: https://github.com/Multysquid/shisu-ko
- date: created **2026-09-17** (~23:40Z); window through **2026-09-18** ~00:20Z (0.2.0 + AGENTS.md architecture invariants)
- tags: education·immersion·generated-input·teach-once·quiet-when-nothing·i-plus-one
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·immersion·generated-input·teach-once] score=10 | Multysquid / shisu-ko | Firefox+local server: **Whisper** (large-v3 / kotoba-whisper / CPU) transcribes YouTube JA ahead of playhead → cues as **real DOM text** for **Yomitan**; hover pauses; one key (or Alt+Shift+M) mines screenshot+sentence MP3 to **AnkiConnect** (or Downloads). Cache per video; native or Docker+GPU. Distinct from kotobako (Galgame/anime capture+FSRS companion) — **live YouTube subtitle generation for dictionary+mine**. | https://github.com/Multysquid/shisu-ko
- why distinct: NEW URL day-0; YouTube Whisper→DOM immersion not on yesterday roster; Anki optional for live subs.
- bank: `2026-09-18-multysquid-shisu-ko-live-japanese-youtube-subtitles` (**deposited** learning; body `/workspace/field/bank-bodies/2026-09-18-shisu-ko.txt`)

### 2) anaidyss / zh-notes — offline ZH lesson-notes CLI; note file = Anki source of truth — STRONG
- who: anaidyss (named **zh-notes**)
- url: https://github.com/anaidyss/zh-notes
- date: created **2026-09-17** (~13:58Z); window through ~17:08Z (capture guards, word-choice, readme/manual)
- tags: education·wiki-craft·human-gate·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·wiki-craft·human-gate·quiet-when-nothing] score=9 | anaidyss / zh-notes | Offline Chinese lesson-notes CLI: pinyin/hanzi → CC-CEDICT (+optional BKRS) → one Obsidian-ruby markdown line; **same line builds Anki** (no separate word DB). Portable gates: `zh -q` **refuses** when ambiguous; `zh -i` picker / Mod+Shift+Z own-meaning; HSK 2.0/3.0 tags; undo/find/ruby. Distinct from kotonoha-anki (JA↔VI hand cards) and shici (EN-ZH FSRS app) — **lesson vault as single source of truth**. | https://github.com/anaidyss/zh-notes
- why distinct: NEW URL day-0; ZH prefer; quiet-refuse + wiki-craft not on roster.
- bank: `2026-09-18-anaidyss-zh-notes-offline-chinese-lesson-notes` (**deposited**; body `/workspace/field/bank-bodies/2026-09-18-zh-notes.txt`)

### 3) CloudcoreZZH / shici-android (拾词) — offline Android EN-ZH ECDICT + FSRS-6; fail-closed 考研 frequency — STRONG (day-0)
- who: CloudcoreZZH (named **拾词**)
- url: https://github.com/CloudcoreZZH/shici-android
- date: created **2026-09-17** (~16:30Z); v0.1.0 release same day
- tags: education·quiet-when-nothing·teach-once·tutor-loop
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·quiet-when-nothing·teach-once·tutor-loop] score=8 | CloudcoreZZH / shici-android (拾词) | Native offline Android EN↔ZH dictionary+study (ECDICT + FSRS-6). Portable: **考研义项频率 explicitly missing** — keeps original sense order, never fakes exam-frequency from generic ECDICT tags; re-add creates **independent** learning task (join-count sorts due queue); learn≠review; interrupt-safe idempotent grading; zero network/ads/telemetry. APK release + 25 automated tests. Distinct from zh-notes (lesson CLI) and BlinkWord (desktop selection) — **fail-closed offline EN-ZH FSRS phone runner**. | https://github.com/CloudcoreZZH/shici-android
- why distinct: NEW URL day-0; fail-closed frequency honesty + re-add-as-new-task; ZH UI prefer-adjacent.
- bank: `2026-09-18-cloudcorezzh-拾词-offline-android-en-zh-ecdict` (**deposited**; body `/workspace/field/bank-bodies/2026-09-18-shici-android.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### shahsanket2107 / livemandarin — score 9 (overflow; ZH live call captions)
- url: https://github.com/shahsanket2107/livemandarin
- date: created **2026-09-17** (~18:27Z); rename+SEO README ~21:38Z
- tags: education·immersion·generated-input·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Apple Silicon local Mandarin↔English live captions for any Mac audio (Meet/Zoom/Teams/FaceTime/mic) via ScreenCaptureKit + Qwen3-ASR; nothing leaves machine. Strong immersion twin to shisu-ko — overflow to diversify packet (YouTube mine vs call captions); **swap candidate over #3** if ZH immersion preferred over EN-ZH FSRS phone.

### fobeetsai / japanese-reader — score 8 (overflow; 閱讀高手 flagship window)
- url: https://github.com/fobeetsai/japanese-reader
- date: created 2026-09-07; **material window 2026-09-17→18** (master.html 閱讀高手: 941 grammar + karaoke shadowing + SRS)
- tags: education·reveal-schedule·i-plus-one·immersion·tutor-loop
- one-liner: JA reading suite (ZH-TW): JLPT 8138-word color, 941 grammar drawer, **kana frost-mask reveal-on-hover**, particle hierarchy protect, dual-sub Trancy modes, karaoke TTS + shadowing, SRS flashcards. Strong reveal-schedule gate — overflow (created Sep 7; mega-suite); swap over #3 if JA reading preferred.

### rin-7777777 / jlpt-exam-runner — score 8 (overflow; exam runner ≠ bank)
- url: https://github.com/rin-7777777/jlpt-exam-runner
- date: created **2026-09-17** (~05:23Z)
- one-liner: Pure-frontend JLPT mock **runner** (no built-in AI/questions): import meta-driven JSON papers → timed exam (auto-submit) vs practice (per-item reveal); JLPT pass = total≥pass AND each section≥min; ZH explanations; Capacitor APK. Portable human-gate import + quiet-when-nothing — overflow under top-3 immersion/wiki picks.

### ydd0729 / eudic-anki-sync — score 7 (overflow; Eudic→Anki tooling)
- url: https://github.com/ydd0729/eudic-anki-sync
- date: created **2026-09-17**; Releases exe + dry-run + reverse-delete confirm
- one-liner: Local 欧路生词本 incremental sync to AnkiConnect with MDX-faithful card backs; dry-run; reverse sync needs confirm. Strong quiet tooling — overflow (sync bridge not tutor-loop).

### Daiwa-Scholars-… / n2-grammar-drill — score 7 (overflow; 25s pace + distractor autopsy)
- url: https://github.com/Daiwa-Scholars-Two-Thousand-Twenty-VIBE/n2-grammar-drill
- date: created **2026-09-17**; Shin Kanzen Master N2 ch.1–7; live Pages
- one-liner: 23 authentic-pattern MCQs; **~25s** speed benchmark; English distractor autopsy; missed-only retry. Portable pace+autopsy gate — thin corpus → overflow.

### emeryray2002 / flashcard-go-go — score 7 (overflow; typed-answer FSRS-6, not L2)
- url: https://github.com/emeryray2002/flashcard-go-go
- date: created **2026-09-17**; local macOS Go binary + JSON; typed answers grade Good/Hard from evidence
- one-liner: Portable typed-retrieval grade gate — not language-specific → overflow.

### bigfe-efe / dilhane — score 7 (overflow; offline JA for Turkish L1)
- url: https://github.com/bigfe-efe/dilhane
- date: created 2026-08-25; window kanji cards+test **2026-09-17**
- one-liner: Offline PWA hiragana→Genki I→N5 with TR explanations + KanjiVG strokes. Prefer JA but TR L1 / not day-0 → overflow.

### meichuanyi / anka — score 6 (library/product; Anki-reborn Rust+FSRS+MCP)
- url: https://github.com/meichuanyi/anka
- one-liner: .apkg-compatible FSRS core + MCP — library not named L2 practice → bounce/library.

### nikhiltomar2712 / sumi-JP-dork — score 6 (overflow; quiet kanji HTML room)
- url: https://github.com/nikhiltomar2712/sumi-JP-dork
- date: created **2026-09-17**; tap-reveal + writing grid
- one-liner: Aesthetic JLPT kanji drill single-file — thin vs benkyou working-set → overflow.

### ValeraZSD / terramentor — score 7 edge (prove-before-complete; not L2)
- url: https://github.com/ValeraZSD/terramentor
- one-liner: Local mastery engine refuses topic complete until demonstrated; cold second-pass answer-key gate. Not L2 language → edge overflow.

### Promote-watch continues (same URLs — do not re-keep)
- mShono/finn_cards — **2026-09-17** ~11:31Z drop-stale-forms-on-edit + deck-scoping tests — polish, no new distinct mechanism for fourth slot.
- pekoqq/ReadLoops — last **2026-09-16** ~21:36Z — continue promote; EN CET-4.
- yuktun/japanese-study — **2026-09-17** Year-3/4 lesson audits + flashcard JSON fixes — content wiki continue.
- gillisandrew/ancci — still idle since **2026-09-14** Release 0.5.1.
- Dilnazzzz/bridge — **still idle** since 2026-09-10.
- cute6v / maitodesu / ColorlessBoy/sokonanoda-lang — no new distinct-mechanism warrant.
- anonymouspartner/capybara-anki — **2026-09-17** spelling-card/export polish — still overflow couple stack.
- xmonkey/paperback — Sep 17 type-face / empty-card fixes — continue overflow.
- gehbfarr5/ielts-vocab-automation / piggyham/BlinkWord / bannysway/grab-series-vocab — same-URL continue.

### Same-URL / yesterday+Wed KEEP watches (do not re-keep)
- ColinHouse/kotoba-studio → **renamed to kotobako** (301); same created stamp + ZH false-friend/FSRS loop — **SKIP** (not a new mechanism).
- lavich/Tavelori / Hanayou/benkyou — yesterday KEEP skip.
- bee-san/jlpt-levels-yomitan / dothuan-git/kotonoha-anki / onuross/anki-llm-pipeline — Wed KEEP skip.

## BOUNCE list (url | why)
- https://github.com/ColinHouse/kotobako | rename of yesterday KEEP kotoba-studio (301); same mechanism
- https://github.com/ColinHouse/kotoba-studio | redirects to kotobako
- https://github.com/nguyenductoan251106/ausdrucka | Next.js bootstrap README only; DE writing trainer claim unevidenced
- https://github.com/Mohamed-Ezz82/Duitsch-Trainer | AI Studio Gemini scaffold only
- https://github.com/whotf-ash/German-trainer | Next.js bootstrap only
- https://github.com/eamonackom2-oss/DueuschSprint | README 404
- https://github.com/kevinmarathon3/wort-hop | README 404
- https://github.com/SnailArmstrong/anki-word-highlighter | README 404 ("ai slop" self-label in search desc)
- https://github.com/Uncorrected-nova574/playtranslate | download-bait / thin marketing README; not trustworthy first-party practice
- https://github.com/Kabutooki/Kokyo-Anki | Japanese civics『公共一問一答』drill PWA — not L2 language
- https://github.com/changoverthinking/JLPT-Super | upload-churn PWA + Supabase; weak named portable gate
- https://github.com/codeMeol/jlpt-kanji-app | thin Flutter N5 write-then-reveal; roadmap-heavy
- https://github.com/morrettwi/manabu | generic gamified JA SRS prototype (SM-2)
- https://github.com/DeuterioX/JLPT-FlashCard | prior bounce; still thin
- https://github.com/meichuanyi/anka | Anki-reborn library/MCP — not L2 named practice
- https://github.com/IsthisLee/korean-kit | Claude Code Korean writing-tools plugin (taste-gate for tooling) — not learner practice loop
- https://github.com/Otavio-Emanoel/Vocabula | EN lock-screen SM-2 ambient — not prefer-lang
- https://github.com/Jxck007/JLPT-Seat-Watcher | seat availability monitor — not study
- https://github.com/derisean-cmd/JLPTcalc | score calculator only
- https://github.com/ZongrongLi/fahrtheorie | DE driving-theory quiz — not L2 language learning
- false-positive Ankit*/portfolio / FSR/DLSS / Excel Anki / Linux flashcards / CompTIA / 50-states | name/topic noise
- X / Gmail / Slack | not used this hunt

## FETCH NOTES
- `gh` CLI unauthenticated on box → `curl` to `api.github.com/search/repositories` (spaced ~7s; search limit 10/min). First burst hit rate-limit (280-byte error dumps) then recovered with User-Agent.
- Search dumps under `/workspace/field/edu0918/s01–s15-*.json`; READMEs under `edu0918/readmes/`; atoms under `edu0918/atoms/`; repo API meta under `edu0918/api/`.
- Promote-watch atoms refreshed: finn_cards Sep 17 polish; ReadLoops idle since Sep 16; yuktun Year-3/4 audits; bridge still Sep 10; ancci idle; capybara/paperback Sep 17 polish.
- Truncations / misses: DueuschSprint / wort-hop / anki-word-highlighter README 404; ausdrucka/Duitsch-Trainer/German-trainer scaffold-only; playtranslate marketing-bait.
- Bank deposits: **succeeded** for shisu-ko, zh-notes, shici-android → `raw/learning/2026-09-18-*` + INDEX. Bodies at `/workspace/field/bank-bodies/2026-09-18-{shisu-ko,zh-notes,shici-android}.txt`.
- scratch-seen-urls.txt / seen-gh-repos-lower.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) shisu-ko **10**, (2) zh-notes **9**, (3) shici-android **8**.
- Overflow scored ≥6 not in top-3: livemandarin **9**, japanese-reader **8**, jlpt-exam-runner **8**, eudic-anki-sync **7**, n2-grammar-drill **7**, flashcard-go-go **7**, dilhane **7**, sumi **6**; finn_cards/ReadLoops/yuktun continue; ancci idle; bridge still idle; capybara/paperback continue.
- **Swap notes:** (a) prefer livemandarin **9** over shici #3 if ZH call-immersion wanted alongside YouTube mine; (b) prefer japanese-reader or jlpt-exam-runner over shici if JA reading/exam-runner preferred; (c) do **not** re-keep kotobako rename. Do **not** drop #1.
- Explicit bounce-deltas on prior keeps: yesterday three KEEP = skip (kotoba-studio→kotobako rename); Wed three = skip.
- Alert-line item: **none**.

## PACKET READY
1. [education·immersion·generated-input·teach-once] score=10 | Multysquid / shisu-ko | Live Whisper JA YouTube subtitles as DOM for Yomitan; one-key screenshot+audio mine to AnkiConnect. | https://github.com/Multysquid/shisu-ko
2. [education·wiki-craft·human-gate·quiet-when-nothing] score=9 | anaidyss / zh-notes | Offline ZH lesson CLI; note file sole Anki source; `-q` refuses ambiguous; picker/own-meaning gates. | https://github.com/anaidyss/zh-notes
3. [education·quiet-when-nothing·teach-once·tutor-loop] score=8 | CloudcoreZZH / shici-android (拾词) | Offline Android EN-ZH ECDICT + FSRS-6; fail-closed missing 考研 frequency; re-add = new task. | https://github.com/CloudcoreZZH/shici-android

## Result for compiler: 3 KEEP
1. Multysquid/shisu-ko — 10 — JA YouTube Whisper→Yomitan→Anki mine
2. anaidyss/zh-notes — 9 — ZH lesson-notes CLI wiki-craft + quiet refuse
3. CloudcoreZZH/shici-android — 8 — offline EN-ZH FSRS fail-closed phone runner
