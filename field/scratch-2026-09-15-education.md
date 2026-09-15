# Field education hunt — 2026-09-15 scratch (Tuesday)
Window: ~2026-09-14 00:00 UTC → now (also late Sep 13 if truly new URL not kept yesterday). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): RobHelgeson/japanese-stories 10, alessio-palumbo/japartner 10, constkolesnyak/gigaku-lang 9. Overflow promote-watch: mShono/finn_cards 9 (still idle), Dilnazzzz/bridge 9 (still Sep 10), pekoqq/ReadLoops 9 (focus-UI polish only), mlboryczka/french-flashcards 8, DeanYoon/n1-kanji 8, gillisandrew/ancci 7→8 (deck-defined types in window — overflow promote, not top-3 L2 tutor).

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; yesterday KEEP three URLs; same-URL watches (cherkasoviy/nihongo-tutor, mansourvery-hub/anki-japanese-template, suiginko/Shiori, TANREN, ankerspiel, Auto-Kanji, gafu, CompreDef, davadev CI, mural, french-tutor, games-lang, PhiCorvi, Hana, etc.).

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) VinciusGoulart / japones-jlpt — Claude Code mesa+trajeto JA tutor; AnkiConnect feedback; never-invent + 60-min hard stop — PRIMARY
- who: VinciusGoulart
- url: https://github.com/VinciusGoulart/japones-jlpt
- date: created **2026-09-06**; window = **2026-09-14** Fase-1 week-3 curriculum (たい / のがすき) + writing targets; **2026-09-15** school-PDF / private journal gitignore (~00:28Z). In real use since **2026-08-03** per README.
- tags: education·tutor-loop·human-gate·quiet-when-nothing·teach-once·generated-input
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·human-gate·quiet-when-nothing·teach-once] score=10 | VinciusGoulart / japones-jlpt | Named Claude Code Japanese study system (zero→JLPT N3). Two fronts: **Mesa** 1h/day terminal `/estudo` (one grammar point, active sentence production, auto Anki cards) + **Trajeto** ~2h phone Anki/audio without Claude. Pipeline: mesa → vocab TSV → `.apkg` via AnkiConnect → AnkiWeb → phone; next-day `/progresso` **reads the real Anki collection** (queue/retention/minutes) and steers with numbers not vibes. Portable gates: **never invent Japanese**; **60 minutes and stop**; new-card throttle if overdue reviews >~200; bad-day = trajeto alone (quiet-when-nothing). Public method, private diary/state. Distinct from nihongo-tutor (Telegram FSRS+Sudachi), japartner (spoken goal-deadline), 13rianK/japanese-tutor (skill-only) — **mesa/trajeto split with Anki-truth feedback loop**. | https://github.com/VinciusGoulart/japones-jlpt
- why distinct: NEW URL; full curriculum+Anki measurement loop not on yesterday’s roster.
- bank: `2026-09-15-vinciusgoulart-japones-jlpt-claude-code-ja-tutor` (**deposited** learning lane; body `/workspace/field/bank-bodies/2026-09-15-japones-jlpt.txt`)

### 2) bee-san / hachidori — definition blur by lookup-count OR mature Anki (ivl≥21d) — STRONG
- who: bee-san (named; “personally been using this for months”)
- url: https://github.com/bee-san/hachidori
- date: created **2026-09-02**; window = **2026-09-14** frequency-inline + compact Sanseido gloss + lookup-failure copy + Chrome release automation through ~18:57Z (★10).
- tags: education·reveal-schedule·teach-once·quiet-when-nothing·i-plus-one
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·reveal-schedule·teach-once·i-plus-one] score=9 | bee-san / hachidori | Opinionated local-first Japanese dictionary Chrome extension (hoshidicts / Hoshi-reader lineage). Killer portable gate: **Definition blur** — hide definitions/furigana until recall; qualify by **lookup-count threshold** (At least / Below) and/or **mature Anki** (review card, interval ≥ **21 days**, expression-field match via read-only AnkiConnect). Hover or timed reveal; timed deadline continues across Back. Also: custom definitions, experimental desktop media mining (sentence audio+gif), Hachidori Relay sharing. Distinct from Yomitan / yomi-overlay / lexiglance (lookup tools without forced-recall blur) and mansour Mature Word Mode (Anki template front only) — **immersion-lookup reveal schedule gated on lookup history + Anki maturity**. | https://github.com/bee-san/hachidori
- why distinct: NEW URL; lookup-count + mature-Anki blur not on yesterday’s KEEP.
- bank: `2026-09-15-bee-san-hachidori-ja-dictionary-lookup-count-mature` (**deposited**; body `/workspace/field/bank-bodies/2026-09-15-hachidori.txt`)

### 3) takashi955 / lessonloop — OCR course→practice; unconfirmed items stay out; exam scope ≠ daily SRS — STRONG (day-0)
- who: takashi955
- url: https://github.com/takashi955/lessonloop
- date: created **2026-09-14** (~19:40Z); single ship commit “Add native LessonLoop iOS prototype”; README says verified **2026-09-13** Xcode 26.6 / five XCTests pass.
- tags: education·human-gate·tutor-loop·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·human-gate·tutor-loop·quiet-when-nothing] score=9 | takashi955 / lessonloop | Native SwiftUI iOS prototype: turn language-course handouts into daily practice (JA samples + FR meanings). Photo/camera **on-device OCR**; candidates start **unselected**; missing meanings and **unconfirmed items stay out of practice**; source text preserved apart from corrections. Practice = recall → reveal → rate; “To clarify” add-meaning confirm; Say-aloud record is temporary/discarded. **Exam mode** practises scoped lessons **without changing daily review dates**. Scheduler deliberately simple (10m/1d/3d) — not FSRS. No cloud/AI translation hooked. Distinct from japartner (spoken Capture), french-flashcards (tutor proposes cards), DeanYoon n1-kanji (cloud cron) — **OCR import human-gate + exam-scope isolation**. | https://github.com/takashi955/lessonloop
- why distinct: NEW URL; day-0 confirm-before-practice OCR loop.
- bank: `2026-09-15-takashi955-lessonloop-ios-ocr-course-materials-with` (**deposited**; body `/workspace/field/bank-bodies/2026-09-15-lessonloop.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### yuktun / japanese-study — score 8 (overflow; school-PDF authority wiki-craft)
- url: https://github.com/yuktun/japanese-study
- date: created **2026-09-12**; window = Year-2/3 lesson migration + flashcard nav **2026-09-14→15**
- tags: education·wiki-craft·teach-once·quiet-when-nothing
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-liner: Minna-no-Nihongo school revision archive; **school PDF authoritative** — AI explanations must be labelled supplementary (`contentSource: ai_derived`) and must never overwrite school fields; omit rather than invent. Strong provenance gate but more content migration than learner loop → overflow under tutor-loop preference.

### gillisandrew / ancci — score 8 (overflow / promote-watch; deck-defined card types)
- url: https://github.com/gillisandrew/ancci
- date: **2026-09-12→14** deck-defined card types + purge non-authoring/reviewing + Release 0.5.1; treat suspended-while-studying as marked
- tags: education·human-gate·teach-once·quiet-when-nothing
- one-liner: Claude Code Anki authoring plugin; cards/types are deck properties; `/ancci:review` fixes flagged/suspended. Mechanism upgraded in window — **promote-watch fire** — but general Anki tooling (agentic-AI example deck), not prefer-L2 tutor → overflow not top-3.

### MattFor / lexiglance — score 7 (overflow; system-wide Yomitan)
- url: https://github.com/MattFor/lexiglance
- date: created **2026-09-14**; public Release v1.0.0→v1.0.1 same day
- tags: education·reveal-schedule·teach-once
- one-liner: Linux/Windows system-wide popup dictionary (AT-SPI/UIA + OCR); Yomitan dict format; JA/KO/RU/UK/EL; AnkiConnect. Strong immersion tooling — thinner portable gate than hachidori blur → overflow.

### mazdiaz / jiten-migaku-miner — score 7 (overflow; Jiten→Migaku knownness workspace)
- url: https://github.com/mazdiaz/jiten-migaku-miner
- date: pushed **2026-09-13** random practice; **2026-09-15** Next.js+Postgres owner-auth migration
- one-liner: Private JA vocab workspace: Jiten CSV + Migaku known TXT; K/M/S/L review; mining queue; read-only Anki snapshot. Named practice — infra-heavy, blur/i+1 thinner than KEEP → overflow.

### chachaprince1 / anime-episode-to-anki — score 7 (overflow; classroom installer)
- url: https://github.com/chachaprince1/anime-episode-to-anki
- date: **2026-09-14** guided student installer + ImmersionKit Full Card Miner combo
- one-liner: Chrome ext: episode vocab → Yomitan dictionaries → Anki; auto-drops particles/fillers before human review. Classroom packaging — solid but thinner generalizable gate.

### lfreeman / ankix — score 7 (overflow; dry-run Anki CLI for Claude Code)
- url: https://github.com/lfreeman/ankix
- date: created **2026-09-14**
- one-liner: fastanki-backed CLI; every write is preview until `--no-dry-run`; AnkiWeb sync without desktop/AnkiConnect. Distinct from joshgummersall/ankix (SEEN). Capture-while-learning — general, not L2-specific → overflow.

### Morgawr / kechimochi — score 6 (overflow; immersion tracker)
- url: https://github.com/Morgawr/kechimochi
- date: **2026-09-14→15** E-Ink theme, fonts, Android sync fixes, library UX
- one-liner: Local-first JA immersion time tracker + media library. Logging not tutor-loop.

### dcambur / yomi-overlay — score 6 (overflow; macOS OCR Yomitan)
- url: https://github.com/dcambur/yomi-overlay
- date: window = minor target-picker fix **2026-09-14**; last mechanism Aug
- one-liner: ScreenCaptureKit OCR overlay dictionary (furigana-stripped). Tooling sibling to lexiglance.

### Same-URL / yesterday KEEP watches (do not re-keep)
- RobHelgeson/japanese-stories (pushed Sep 14 story ratings — yesterday KEEP skip)
- alessio-palumbo/japartner (pushed Sep 14 appearance/recording polish — yesterday KEEP skip)
- constkolesnyak/gigaku-lang (yesterday KEEP skip)
- cherkasoviy/nihongo-tutor / mansour anki-template / Shiori — prior KEEP
- pekoqq/ReadLoops — Sep 14 focus-mode UI polish only; still overflow EN CET-4
- mShono/finn_cards — **still idle** since 2026-09-11
- Dilnazzzz/bridge — **still idle** since 2026-09-10
- bee-san/bees-ultimate-grammar-dictionary — prior overflow; this hunt’s hachidori is a **different URL**
- eternalisfine/Hana — Sep 13 tests clear; thinner than japartner / japones-jlpt
- 0xzerolight/anki_miner — spaCy pack polish; SEEN pattern

## BOUNCE list (url | why)
- https://github.com/RobHelgeson/japanese-stories | yesterday KEEP
- https://github.com/alessio-palumbo/japartner | yesterday KEEP
- https://github.com/constkolesnyak/gigaku-lang | yesterday KEEP
- https://github.com/mShono/finn_cards | idle Sep 12–15; overflow promote-watch (not bounce — still score 9)
- https://github.com/Dilnazzzz/bridge | still Sep 10; overflow
- https://github.com/pekoqq/ReadLoops | same-URL polish; overflow
- https://github.com/codehaseyo/korean-comprehensible-input | resource list only (no runnable setup)
- https://github.com/PeterDessev/Shiori | last commit Jul 2026; outside window; name-collision with suiginko/Shiori
- https://github.com/haeslerc/anki-setup | Anki/Yomitan config dump; no README mechanism
- https://github.com/Ceidoux/SmartJisho | milestone-1 FastAPI kanji scaffold
- https://github.com/BrockBadeaux14/AnkiVoice | college planning docs / fixtures; no ship
- https://github.com/demirrepo/learnist | Flutter stub README
- https://github.com/suspiciousMans/language-learning | programming-language paths (not L2)
- https://github.com/Vicram123/voxoira | generic browser STT/translator product
- https://github.com/Pirate-Hunter-Zoro/Atlas | CS tutoring board; off-lane
- https://github.com/tarikrital/tilmidh-agent | Moroccan primary school PWA; off-lane
- https://github.com/ncreighton/c5127abb-language-learning-quiz-and-tra | spam/generated SaaS stubs
- https://github.com/cheklatm712-art/cat-studio | 202-byte README
- https://github.com/knmseo/Japanese-Learning | Vite template leftover
- https://github.com/Mdiqram/German-Language-Learning | file upload; no README
- https://github.com/seyedali1996lb-svg/subtitle-to-anki | empty / no README
- https://github.com/1Selxo/Mangatan | large product fork; not named new gate in window
- https://github.com/teto/rikai.nvim | neovim dict; flake bump only
- https://github.com/hudzax/amai-lyrics | Spicetify furigana lyrics; tooling
- https://github.com/RyuuNeko1107/ja-furigana-dict | dict packaging chore
- https://github.com/joshgummersall/ankix | SEEN (distinct from NEW lfreeman/ankix)
- X MCP | dead — skipped

## FETCH NOTES
- GitHub Search API (UA `FieldBot`): unauthenticated; core 60/hr exhausted early — recovered after ~13m reset. Search quota 10/min used carefully. Saved under `edu0915/search-*.json` (created-anki2, pushed-ci, pushed-ja2, created-tutors, pushed-tutor-l2, created-l2c validation-fail on complex OR).
- README path: raw.githubusercontent.com under `edu0915/readmes/` (no Firecrawl). Commit windows via `commits/*.atom` (no Firecrawl / no X).
- Promote-watch atoms: finn_cards last **2026-09-11**; bridge **2026-09-10**; ancci **2026-09-14** Release 0.5.1 (deck-defined types — mechanism upgrade, overflow); ReadLoops Sep 14 focus UI only.
- HTML GitHub search pages returned empty (bot wall); atom + Search API + WebSearch used instead.
- Bank deposits: **succeeded** for japones-jlpt, hachidori, lessonloop → `raw/learning/2026-09-15-*` + INDEX rows. Bodies at `/workspace/field/bank-bodies/2026-09-15-{japones-jlpt,hachidori,lessonloop}.txt`.
- Truncations / misses: haeslerc/anki-setup, Mdiqram/German-Language-Learning, seyedali subtitle-to-anki, RichardZuidam/loop-language-studio, Logiquo interference-recorder README miss/empty.
- scratch-seen-urls.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) japones-jlpt **10**, (2) hachidori **9**, (3) lessonloop **9**.
- Overflow scored ≥6 not in top-3: yuktun/japanese-study **8**, ancci **8** (promote-watch fire), lexiglance **7**, jiten-migaku-miner **7**, anime-episode-to-anki **7**, lfreeman/ankix **7**, kechimochi **6**, yomi-overlay **6**; finn_cards **9** / bridge **9** still idle; ReadLoops **9** polish-only same-URL.
- **lessonloop vs yuktun for #3:** prefer lessonloop for human-gate practice loop; promote yuktun over lessonloop if compiler wants school-PDF wiki-craft provenance over day-0 iOS prototype. Do **not** drop #1 or #2.
- Explicit bounce-deltas on prior keeps: yesterday three KEEP = skip (even with Sep 14 polish); CompreDef/gafu/thai/darya/monosai/origa = same-URL only; finn_cards/bridge still idle.
- Alert-line item: **none**.

## Result for compiler: 3 KEEP
1. VinciusGoulart/japones-jlpt — 10 — mesa+trajeto Claude JA tutor; Anki-truth loop; never-invent + 60-min stop
2. bee-san/hachidori — 9 — definition blur by lookup-count OR mature Anki (≥21d)
3. takashi955/lessonloop — 9 — OCR import confirm-gate; exam scope ≠ daily SRS
