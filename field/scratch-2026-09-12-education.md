# Field education hunt — 2026-09-12 scratch (Saturday)
Window: ~2026-09-11 00:00 UTC → now (prefer pushes 2026-09-11 / 2026-09-12). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): garthtrickett/gafu-v2 10, davadev/obsidian_chinese_comprehensible_input 9, mansourvery-hub/CompreDef 9. Overflow bounced same-URL: cehbz/thai, mikub97/repetita, AlphaNerdFx/Tango, monosai, darya, chunk-lab, origa, etc.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt` (~826 lines); yesterday KEEP three URLs; bank INDEX hits for same URL this week unless commit-scoped mechanism jump → overflow only. Prior recent: By-ear, kikubridge, jp-sentences-to-anki, nihongo-sensei, sillon, monosai, anki-quick-add, etc.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) Traderhs / TANREN — Local-first JA trainer for Korean L1; answer-is-grade; VOICEVOX+pitch; rounds — PRIMARY
- who: Traderhs
- url: https://github.com/Traderhs/TANREN
- date: created **2026-08-31**; **2026-09-11** **v1.0.0** + VOICEVOX mora splits + **gate enrichment generation** + edit entries during study + pitch retry + Windows release packaging through ~10:34Z
- tags: education·i-plus-one·tutor-loop·teach-once·taste-gate·quiet-when-nothing·generated-input
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·tutor-loop·teach-once·taste-gate·generated-input] score=9 | Traderhs / TANREN | Local-first **Japanese** trainer aimed at **Korean** L1: reading / writing / listening / **pitch** mixed so the same cue cannot carry every card. **Answer is the grade** — local semantic models + deterministic rules accept meaning-equivalent answers (polysemy scored per sense; remembered edge-case overrides); no Again/Hard/Good self-rating. Add a JA entry → background **reading analysis + lexical pitch + VOICEVOX** audio (multi-voice). Study as **rounds** (50-entry steps, cumulative every 500): correct leaves the round, misses stay — narrow until only unknowns remain. Sep 11 = **v1.0.0** + enrichment-generation **gate** + mora-split fixes + in-study edit. Distinct from gafu (media-gap→validated i+1 material), By-ear (voice planner), monosai (Anki-ceiling stories), CompreDef (J-J ladder) — **KO→JA active-recall trainer with semantic grading + VOICEVOX pitch**. | https://github.com/Traderhs/TANREN
- why distinct: NEW URL to Field; named answer-is-grade + round-narrowing + VOICEVOX enrichment gate not on yesterday’s gafu / Chinese-CI / CompreDef roster.
- bank: `2026-09-12-traderhs-tanren-local-first-japanese-trainer-for` (**deposited** learning lane; body also at `/workspace/field/bank-bodies/2026-09-12-tanren.txt`)

### 2) candemircan / ankerspiel — Nightly rotate Anki examples so Card≠sentence memorized — STRONG
- who: candemircan
- url: https://github.com/candemircan/ankerspiel
- date: created **2026-09-08**; **2026-09-11** persist **refresh history per note** so an interrupted nightly run resumes without replaying; Sep 10 Capricorn calendar + orphan-audio prune
- tags: education·generated-input·teach-once·quiet-when-nothing·reveal-schedule
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·generated-input·teach-once·quiet-when-nothing] score=9 | candemircan / ankerspiel | Nightly job against AnkiConnect: take cards due next day (+ configurable new notes), ask any OpenAI-compatible LLM for **fresh example sentences**, synthesize audio with local **Kokoro** TTS, write into an `ankerspiel` note type — so you do **not** memorize the example while progressing the deck. History `k` prior sentences shown as “avoid these.” `migrate` preserves FSRS/review state; `doctor` preflights AnkiConnect/provider/TTS/ffmpeg; optional ntfy report. Language-agnostic config (demo = DE B1 Goethe). Sep 11 = **persist refresh history per note** for interrupted runs. Distinct from monosai (story gen under Anki ceiling) and jp-sentences (VOICEVOX builder) — **presentation rotation owned by schedule, card identity stays the word**. | https://github.com/candemircan/ankerspiel
- why distinct: NEW URL; Card≠example rotation + resume-safe history not shipped yesterday.
- bank: `2026-09-12-candemircan-ankerspiel-nightly-fresh-anki-example-sentences` (**deposited**; body `/workspace/field/bank-bodies/2026-09-12-ankispiel.txt`)

### 3) NikhilDhanda / Auto-Kanji-Breakdown — In-Anki expandable kanji trees; reveal on back — STRONG (JA lane)
- who: NikhilDhanda
- url: https://github.com/NikhilDhanda/Auto-Kanji-Breakdown
- date: created **2026-09-10**; **2026-09-11** public beta docs / AnkiWeb **1554975596** / v0.9.0-beta.1 (window = docs ship of already-used personal tool)
- tags: education·reveal-schedule·teach-once·quiet-when-nothing
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·reveal-schedule·teach-once] score=8 | NikhilDhanda / Auto-Kanji-Breakdown | Anki add-on that injects **expandable kanji component trees** (KanjiVG structure + KANJIDIC2 readings/meanings/radicals/stroke/frequency) into existing Japanese note types — no HTML/CSS editing. Settings pick note type + JA fields; recommended display on **Back** so the answer comes first. Desktop generates; mobile reviews synced offline; Yomitan/AnkiConnect mining can auto-generate on configured note types. Honesty note: study aid for recognition, not etymology authority. Distinct from CompreDef (definition ladder) and gafu (i+1 material validator) — **in-review kanji decomposition without leaving Anki**. | https://github.com/NikhilDhanda/Auto-Kanji-Breakdown
- why distinct: NEW URL; in-card expandable breakdown + back-of-card reveal not on roster. (Window is docs/public beta more than new algorithm — still strongest unused JA Anki add-on in window.)
- bank: `2026-09-12-nikhildhanda-auto-kanji-breakdown-expandable-kanji-component` (**deposited**; body ready)

## Scored but NOT in top-3 SETUP slots (overflow)

### mShono / finn_cards (Kielikaveri) — score 9 (overflow / promote-watch; under-served L2)
- url: https://github.com/mShono/finn_cards
- date: **2026-09-11** Unlock forms **only on Good or Easy**; curriculum **never closes forms**; order session queue by curriculum (Sep 10: gate form introduction behind curriculum; FST via omorfi/`uralicNLP` — LLM never invents forms)
- tags: education·i-plus-one·taste-gate·teach-once·tutor-loop
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Morphology-gated Finnish — FST-verified inflection cards + curriculum unlock on earned grades. Stronger portable gate than Auto-Kanji’s window; left overflow under cap-3 **JA preference** — compiler may swap #3 for this if FST/curriculum gate preferred over kanji trees.
- bank: `2026-09-12-mshono-finn-cards-kielikaveri-fst-verified-finnish` (**deposited**)

### mansourvery-hub / CompreDef — score 9 (overflow; same URL — mechanism jump)
- url: https://github.com/mansourvery-hub/CompreDef
- date: **2026-09-11** **Wiki algorithm rewrite, ladder-free** — density scoring across all defs; mastery as interval/365 continuum (`interval ≥ 365` = 1.0); picker module + v1.2.15–17
- tags: education·i-plus-one·taste-gate·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Yesterday’s KEEP evolved: ordered dictionary ladder → **ladder-free global density rank** + continuous mastery. **Same URL** → overflow / promote-watch only.

### garthtrickett / gafu-v2 — score 9 (overflow; same URL — mechanism jump)
- url: https://github.com/garthtrickett/gafu-v2
- date: **2026-09-11** Split Learn vs Review queues; review = understood-or-not with target coloured; teach from **stored material only** (study never generates first exposure); chain batched Cards after grade; end encounter when teaching seen
- one-liner: Real teach-once / reveal-schedule deepen on yesterday PRIMARY. **Same URL** → overflow only.

### cehbz / thai-language-anki — score 9 (overflow; same URL)
- url: https://github.com/cehbz/thai-language-anki
- date: **2026-09-11** review is not a writing command; introducible cap; draft picture search phrases; drop Production card with no picture; assess-first recordings
- one-liner: Generation-side fitness continues. **Same URL** → overflow promote-watch.

### ferranrego / darya — score 8 (overflow; same URL)
- url: https://github.com/ferranrego/darya
- date: **2026-09-11** philologist passes; re-exposure ratchet; pronunciation crutch fades; grammar labels on texts; compound-verb half-tap wrong-word report
- one-liner: CI product deepening; **same URL** (yesterday overflow).

### mikub97 / repetita — score 8 (overflow; SEEN / same URL)
- url: https://github.com/mikub97/repetita
- date: **2026-09-11** exercise type is a file; Create tab writes in-app; store snapshots; sourced material carries licence
- one-liner: Content-type extensibility real; **same URL / prior Field** — overflow watch only.

### yurvon-screamo / origa — score 7 (overflow; same URL)
- url: https://github.com/yurvon-screamo/origa
- date: **2026-09-11** AudioRecall follows reveal pattern (self-assessment after audio); startup rkyv perf
- one-liner: Reveal-pattern fix on AudioRecall; window mostly perf after Sep-10 strict-recall — **same URL**.

### tobiaslrn / monosai — score 6 (same-URL watch; do not re-keep)
- url: https://github.com/tobiaslrn/monosai
- date: **2026-09-11** home/library/settings tabs (+ revert to single library); cloud-session build hooks
- one-liner: UI chrome; **same URL** — bounce re-keep.

### extra-large-onions / obsidian-language-learning — score 7 (overflow; fresh created)
- url: https://github.com/extra-large-onions/obsidian-language-learning
- date: created **2026-09-11**; chapter `.chapter.md` page turns + `korean` annotated token blocks + SM-2 review line in-chapter + voice record keys + export bundle
- tags: education·wiki-craft·reveal-schedule·teach-once
- portable / evidence / combined: **4 / 3 / 7**
- one-liner: Vault-as-lesson (pageable chapters + grammar annotate + in-note SRS). Day-0 but substantial README — overflow; watch vs davadev Chinese CI.

### kai987 / Japanese-N1-Immersive-Sparring-Partner — score 7 (overflow)
- url: https://github.com/kai987/Japanese-N1-Immersive-Sparring-Partner
- date: created **2026-09-08**; daily N1 content sync through Sep 12; JA-only / JA-ZH gloss / explanation toggles; retry keeps prior answers; validated daily JSON import
- one-liner: 99-day N1 immersive reader with ZH support + honest persistence. Content app more than portable gate — overflow.

### nono0529 / kotoba-local — score 7 (overflow)
- url: https://github.com/nono0529/kotoba-local
- date: created **2026-09-09**; Sep 11 UX polish; offline iPhone PWA + FSRS + JLPT N5–N1 for Chinese learners
- one-liner: Solid local-first JA vocab PWA; thinner new portable gate than TANREN/ankerspiel — overflow.

### jackylin2026 / englishpod_to_anki — score 7 (overflow)
- url: https://github.com/jackylin2026/englishpod_to_anki
- date: created **2026-09-10**; Sep 11 corpus honesty (skip incomplete / unreadable PDF; recognise lesson by recording; refresh in place)
- one-liner: Corpus→Anki with refuse-incomplete + Markdown OCR gate between PDF and cards. Useful pipeline; EN-podcast specific — overflow.

### franzlin / linguashelf — score 7 (overflow; window idle since Sep 8)
- url: https://github.com/franzlin/linguashelf
- date: created **2026-09-08**; last push Sep 8 — AI English graded reader (EPUB/PDF→units, click ZH gloss, auto difficulty)
- one-liner: Strong CI graded-reader product but **outside push window** (fresh-created OK); leave overflow unless compiler wants EN graded shelf.

### Cecilita17 / LinguaFlow — score 6
- url: https://github.com/Cecilita17/LinguaFlow
- date: **2026-09-11** YouTube transcript reader + gloss + chat voice + reading progress bookmarks
- one-liner: Immersion reader/chat polish; thinner named gate.

### pbyrne413 / AnkiEnricher — score 6
- url: https://github.com/pbyrne413/AnkiEnricher
- date: created **2026-09-11**; French audio/images enricher with dry-run + backup + tag repair
- one-liner: Safe enrichment CLI; tooling more than learner gate.

### liu-li-huan-ying / drill — score 6
- url: https://github.com/liu-li-huan-ying/drill
- date: **2026-09-11** bulk example backfill for offline CN vocab FSRS app
- one-liner: Window = data cleaning; product exists — overflow thin.

### AndreaBonn / impara-italiano — score 6
- url: https://github.com/AndreaBonn/impara-italiano
- date: **2026-09-11** measure library word floor; fill C1/C2 gaps; spent-budget ≠ dead network
- one-liner: Curriculum honesty (word floor measured not promised); product expansion — thinner new gate.

## BOUNCE list (url | why)
- https://github.com/garthtrickett/gafu-v2 | yesterday KEEP; Learn/Review split — **same-URL → overflow only**
- https://github.com/davadev/obsidian_chinese_comprehensible_input | yesterday KEEP; **idle** in window (latest Sep 10)
- https://github.com/mansourvery-hub/CompreDef | yesterday KEEP; ladder-free rewrite — **same-URL → overflow only**
- https://github.com/mwo1066/By-ear-tutor | prior KEEP; idle (latest Sep 9)
- https://github.com/neverether/kikubridge | prior KEEP; idle (latest Sep 9)
- https://github.com/sebasukodo/jp-sentences-to-anki | prior KEEP; idle (latest Sep 10)
- https://github.com/crnchwrpsupreem/nihongo-sensei | idle (latest Sep 8)
- https://github.com/myqzurdux3/sillon | idle (latest Sep 7)
- https://github.com/tobiaslrn/monosai | prior KEEP; UI tabs — **same-URL watch**
- https://github.com/AlphaNerdFx/Tango | idle since Sep 10 v1.0
- https://github.com/cehbz/thai-language-anki | same-URL mechanism jump → overflow only
- https://github.com/mikub97/repetita | SEEN; same-URL overflow only
- https://github.com/ferranrego/darya | same-URL overflow
- https://github.com/madman8228/chunk-lab | window = security/test polish early Sep 11
- https://github.com/yurvon-screamo/origa | same-URL AudioRecall/perf
- https://github.com/AiraDeCastro/learn-french-with-aira | README still “no app code yet”; early planning (atom shows reader commits — evidence conflict / unfinished)
- https://github.com/jon-jc/kotoba-studio | JA/EN voice **dev workbench** — off-lane (agent IDE, not L2 tutor)
- https://github.com/Alienware2000/better-office-hours | course voice tutor (STEM office hours) — off-lane
- https://github.com/Blueturboguy07/freelingo | Duolingo-class clone; window = Xcode/CI infra
- https://github.com/AndrewDongminYoo/peak-fanout | reminder infra day-0 — not L2 gate
- https://github.com/behmke12/polyglot-quest-agent | day-0 RPG scaffold
- https://github.com/RolandR19/French-PodGen- | day-0 README upload only
- https://github.com/ebriggsjohnson/heisig-chinese-anki-deck | file upload; no README
- https://github.com/yoshisao14/yomitan-hover-anki | 86-byte README; idle since Sep 8
- https://github.com/doonch/FlashType | 2013 archival dump
- https://github.com/f-rehmandev/AI-Powered-Anki | thin README
- https://github.com/Rhythm-Kachhwaha/AnkiMiner | no README; subtitle WIP
- https://github.com/daisuke30/lingogate | no README fetched; UI chrome
- https://github.com/zavoritniigor-ui/ai-ebook-reader | no README; format bugfixes
- https://github.com/BlablaDingens/anki-gemini-agent-2 | no README; Streamlit Spanish Anki agent day-0
- https://github.com/BlablaDingens/spanisch-anki-agent | no README
- https://github.com/soyami/zotero-pick2anki | EN Zotero→Anki mining chrome — library/tool
- https://github.com/k41-vibe/kioku | Anki rslib iOS client — scheduler product, no L2 gate
- https://github.com/JeffShanCha/inkslash | Chinese Obsidian slash menu — not L2
- https://github.com/long2004at/hengya | dental FSRS — off-lane
- https://github.com/MuggleWu/miki | generic Anki-alt FSRS — no L2 gate
- https://github.com/leoon-hu/jiaci | CN vocab SaaS day-0
- https://github.com/tomada1114/english-vocab-app | day-0 FSRS scaffold (same-day build)
- https://github.com/cjvnjde/chatgpt-english-mcp | MCP English workspace — tool not tutor loop
- https://github.com/mikemazzetti/ankicardmaker | cloud Anki sync backup only in window
- X / Firecrawl / HTML GitHub search | skipped (disallowed / thin)

## FETCH NOTES
- GitHub Search API (unauth curl, UA `FieldEduHunt/2026-09-12`): OK early — saved under `edu0912/repos-*.json` (anki, ja-anki, zh, thai, ci, fsrs, lang, ja-tutor, ci2, obs, sea). Complex OR `created` query **422** (too many operators). Search remaining recovered mid-hunt (~10); **core remaining=0** after README/rate_limit probes — README/commits via **raw.githubusercontent.com** + `commits/*.atom` under `atoms12/` (47 atoms, 41 READMEs).
- `gh auth`: not logged in; curl only.
- Watched atoms: gafu / CompreDef / thai / darya / repetita / monosai / origa **active** (same-URL handling above); davadev Chinese CI / By-ear / kikubridge / jp-sentences / nihongo / sillon / Tango **idle**.
- Bank deposits: **succeeded** for TANREN, ankerspiel, Auto-Kanji-Breakdown, finn_cards → `raw/learning/2026-09-12-*` + INDEX rows. Bodies also at `/workspace/field/bank-bodies/2026-09-12-*.txt` and `edu0912/bodies/`.
- HTML GitHub search / Firecrawl / X MCP: not used. Created-date HTML scrape empty (JS page); used Search API `created_at` instead.
- Truncations: `repos-created.json` validation error only; thai search total=0; some READMEs miss (lingogate, AnkiMiner, ai-ebook-reader, BlablaDingens, heisig deck).

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) TANREN **9**, (2) ankerspiel **9**, (3) Auto-Kanji-Breakdown **8**.
- Overflow scored ≥6 not in top-3: finn_cards **9** (promote-watch / swap candidate), CompreDef ladder-free **9** same-URL, gafu Learn/Review **9** same-URL, thai Sep-11 **9** same-URL, darya **8** same-URL, repetita exercise-type-file **8** SEEN, origa AudioRecall **7**, obsidian-language-learning **7**, N1 sparring **7**, kotoba-local **7**, englishpod_to_anki **7**, linguashelf **7** (idle push), LinguaFlow / AnkiEnricher / drill / impara-italiano **6**.
- Explicit bounce-deltas on prior keeps: davadev idle; By-ear/kikubridge/jp-sentences/nihongo/sillon idle; monosai UI chrome (watch); gafu/CompreDef/thai = same-URL overflow only.
- **Do not re-ship** gafu / davadev Chinese CI / CompreDef / By-ear / kikubridge / jp-sentences / monosai / nihongo / sillon / Tango / thai (SETUP slot) / repetita unless compiler deliberately refreshes.
- Alert-line item: **none**.

## Result for compiler: 3 KEEP
1. https://github.com/Traderhs/TANREN
2. https://github.com/candemircan/ankerspiel
3. https://github.com/NikhilDhanda/Auto-Kanji-Breakdown

No packet file written. field-seen.json not edited.
