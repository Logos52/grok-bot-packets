# Field education hunt — 2026-09-11 scratch (Friday)
Window: ~2026-09-10 00:00 UTC → now (prefer pushes 2026-09-10 / 2026-09-11). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): mwo1066/By-ear-tutor 10, neverether/kikubridge 8, sebasukodo/jp-sentences-to-anki 7. Overflow bounced same-URL: AlphaNerdFx/Tango, cehbz/thai-language-anki, IamGianluca/anki-addon, talk-tutor, paleoglossa, etc.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt` (780 lines); yesterday KEEP three URLs; bank INDEX hits for same URL this week unless commit-scoped mechanism jump → overflow only.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) garthtrickett / gafu-v2 — Media-prep Japanese SRS; Card≠material; validated i/i+1 — PRIMARY
- who: garthtrickett
- url: https://github.com/garthtrickett/gafu-v2
- date: created **2026-09-08**; heavy **2026-09-10→11** — resumable subtitle analysis (#46–47), reject-and-reask batches (#51), grammar-surface copy instead of offsets (#52), completeness-per-batch (#54), API key server-only (#55), stop asking candidates on punctuation (#56), session outlives issuer (#57)
- tags: education·i-plus-one·generated-input·teach-once·taste-gate·quiet-when-nothing·reveal-schedule
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·i-plus-one·generated-input·taste-gate·teach-once] score=10 | garthtrickett / gafu-v2 | Fresh V2 of **Gafu**: start from a Japanese show/series the learner wants to understand → analyze subtitles → stage the durable **Cards** (vocab sense or grammar construction) that block comprehension → teach via **fresh AI Learning Material** that is **not** the Card (Card owns FSRS schedule; presentations rotate). Every presentation must pass **deterministic i/i+1 validation** (Known Word Bank + known grammar; target Card is the only permitted unknown) before a **Presentation Permit** is issued; rejected batches are asked again, not replayed. Kaishi 1.5k seeds Known Word Bank privately (not redistributed). Local SQLite; Prepare / Study / Watch loop. Distinct from monosai (Anki-ceiling story gen) and By-ear (voice planner) — **media-gap → validated i+1 study → watch**. | https://github.com/garthtrickett/gafu-v2
- why distinct: NEW URL (created Sep 8); named Card vs Learning Material contract + local i/i+1 validator not on yesterday’s By-ear / kikubridge / jp-sentences roster.
- bank: `2026-09-11-garthtrickett-gafu-v2-media-prep` (**body ready** at `/workspace/field/bank-bodies/2026-09-11-gafu-v2.txt` — Auto-review blocked live bank.py write; deposit pending)

### 2) davadev / obsidian_chinese_comprehensible_input — Obsidian CI reader; status-gated gloss; Smart stories + topic radar — STRONG
- who: davadev
- url: https://github.com/davadev/obsidian_chinese_comprehensible_input
- date: created 2026-06-10; **2026-09-10** **0.7.0** topic coverage radar + empty-progress honesty (0.6.x) through ~15:31Z
- tags: education·wiki-craft·i-plus-one·generated-input·reveal-schedule·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·wiki-craft·i-plus-one·generated-input·reveal-schedule] score=9 | davadev / obsidian_chinese_comprehensible_input | Turn any Chinese Obsidian note into a CI reading environment: dictionary tokenization + Known/Partial/Unknown status **drives how much help shows** (known = characters only; partial/unknown get pinyin+gloss). Exposure-tracking SRS; **Smart stories** weave due words into level-appropriate AI text with a **repair loop** that validates target-word presence (best-of-N). Traditional↔Simplified vocabulary shared. Sep 10 = **topic coverage radar** (which subjects your vocab covers) + chart honesty for empty progress. Community plugin store. Distinct from monosai (JA Anki-ceiling stories) and sotto (graded reader availability) — **wiki-craft vault as CI + story-SRS vehicle**. | https://github.com/davadev/obsidian_chinese_comprehensible_input
- why distinct: NEW URL to Field; vault-as-CI + status-gated reveal + story-as-SRS not shipped yesterday.
- bank: `2026-09-11-davadev-obsidian-chinese-ci` (body ready; deposit pending)

### 3) mansourvery-hub / CompreDef — Dictionary ladder; 100% known-kanji early exit — STRONG
- who: mansourvery-hub
- url: https://github.com/mansourvery-hub/CompreDef
- date: created **2026-09-02**; **2026-09-10→11** Yomitan style-scoping + Tab reliability (v1.2.11) through v1.2.14 regression releases ~00:30Z
- tags: education·i-plus-one·taste-gate·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·i-plus-one·taste-gate·teach-once] score=9 | mansourvery-hub / CompreDef | Anki add-on that kills the monolingual **circular lookup trap**: user-ordered **dictionary ladder**; for each target word, score definitions by fraction of **base kanji already on mature Anki cards** (`ivl > 0`); **early-exit on score=1.0** (fully comprehensible); else maximal fallback. Kanji-only gate (kana unchecked). Yomitan HTML fidelity + zip/folder auto-scan + bulk browser generation. Spec in `WIKI.md` (Krashen i+1 framing). Distinct from kikubridge (deck merge) and jp-sentences (VOICEVOX i+1 builder) — **comprehension-gated J-J definition picker**. | https://github.com/mansourvery-hub/CompreDef
- why distinct: NEW URL; named kanji-matrix early-exit ladder not on roster.
- bank: `2026-09-11-mansourvery-hub-compredef-dictionary-ladder` (body ready; deposit pending)

## Scored but NOT in top-3 SETUP slots (overflow)

### ferranrego / darya — score 8 (overflow / promote-watch)
- url: https://github.com/ferranrego/darya
- date: created 2026-07-21; **2026-09-10** Dari-only fork + pedagogical A1–B1 audit + pragmatic functions (ask/offer/agree/repair) + curriculum-gap fill
- tags: education·i-plus-one·generated-input·teach-once
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-liner: Adaptive Dari (~2–10% new vocab) AI texts + FSRS context cards + CEFR grammar. Strong CI product; leave overflow under cap-3 unless compiler prefers under-served L2 (Dari) over CompreDef’s Anki-native gate.
- bank: body ready `2026-09-11-darya.txt` (deposit pending)

### madman8228 / chunk-lab — score 7 (overflow)
- url: https://github.com/madman8228/chunk-lab
- date: created **2026-09-07**; **2026-09-10→11** quiet-UI (“今日无到期” tip removed), mobile screenshot feedback, AI-cache cross-user security fixes
- tags: education·teach-once·i-plus-one·quiet-when-nothing
- portable / evidence / combined: **4 / 3 / 7**
- one-liner: Local-first English **意群/chunk** reconstruct (select/fill/type) + Ebbinghaus SRS + structured sentence explain. Window = polish/security more than new gate — overflow.
- bank: body ready `2026-09-11-chunk-lab.txt` (deposit pending)

### yurvon-screamo / origa — score 7 (overflow)
- url: https://github.com/yurvon-screamo/origa
- date: ★9 mature; **2026-09-10** **strict-recall for late-stage words + AudioRecall mode** + KO/VI README
- tags: education·i-plus-one·tutor-loop·reveal-schedule
- portable / evidence / combined: **3 / 4 / 7**
- one-liner: JP without English middleman; FSRS; N+1 native phrases. Window mechanism (strict-recall/AudioRecall) real but product already large — overflow unless compiler wants mature multi-platform JA app.

### 1magic / deliberate-practice-mentor — score 7 (overflow; cross-domain)
- url: https://github.com/1magic/deliberate-practice-mentor
- date: **2026-09-10** v1.4.3「概念底座前置」E-COACH-009 + token-slim SKILL.md
- tags: education·i-plus-one·teach-once·human-gate
- portable / evidence / combined: **4 / 3 / 7**
- one-liner: WorkBuddy skill — i+1 goal split / 12 practice methods / mastery heatmap / DoD on independent evidence. Portable coach loop; not L2-specific — overflow.

### cehbz / thai-language-anki — score 9 (overflow; same URL — mechanism jump)
- url: https://github.com/cehbz/thai-language-anki
- date: **2026-09-10** age-out empty growing-source answers; no-fit drafter escalate after cap; syllabus restore as **human act**; curated git history; wrap writes in snapshot+pre-commit
- tags: education·taste-gate·human-gate·teach-once·generated-input·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Generation-side fitness continues (yesterday clause refuse → today empty-answer age-out + no-fit escalate + human restore). **Same URL** → overflow / promote-watch only.

### mikub97 / repetita — score 8 (overflow; SEEN / same URL)
- url: https://github.com/mikub97/repetita (SEEN)
- date: **2026-09-10** “design my lessons” catalogue/tags/study plans; “I know this” after correct too; report broken exercise; DB owns material
- one-liner: Real lesson-design + declared≠earned gates deepening; **same URL / prior Field** — overflow watch only.

### AlphaNerdFx / Tango — score 8 (overflow; same URL)
- url: https://github.com/AlphaNerdFx/Tango
- date: **2026-09-10** **v1.0.0** freeze + shell completion + multi-OS CI
- one-liner: Release-rung close; same-URL mature miner — overflow.

### tobiaslrn / monosai — score 7 (same-URL watch; do not re-keep)
- url: https://github.com/tobiaslrn/monosai (SEEN / prior KEEP)
- date: **2026-09-10** focus recently-learned stories on newest words; exception policy in generation; AnkiConnect FSRS difficulty recover; UI primitive refactor
- one-liner: Real newest-word focus + exception policy but **same URL** — bounce re-keep; compiler may note as watch.

### JesusOrihuela / practice_english.github.io — score 6
- url: https://github.com/JesusOrihuela/practice_english.github.io
- date: **2026-09-10→11** de-es pair shippable (2→3 pairs); Lighthouse ≥90; orphan WAV cleanup
- one-liner: Offline PWA multi-pair language practice; window = third pair + perf — product expansion, thinner new gate.

### RedMors / japones-app — score 6
- url: https://github.com/RedMors/japones-app
- date: created 2026-08-29; Sep 11 UI merge PRs
- one-liner: Local JA mining + AnkiConnect + optional OpenRouter teacher; useful stack, thinner portable diary than gafu/CompreDef.

### JesseRWeigel / koe — score 6 (window = infra)
- url: https://github.com/JesseRWeigel/koe
- date: **2026-09-10** hosted AI route protection only (graded reader + FSRS already shipped)
- one-liner: Strong product surface (FSRS + AI convo + graded reader) but **window = guardrails**, not new education gate — bounce SETUP / overflow thin. (Note: grokbot.dev/templates/koe already in seen.)

### Anacbd / language-tutor (LingoEcho) — score 5
- url: https://github.com/Anacbd/language-tutor
- date: created **2026-09-11** same-day init + README
- one-liner: Day-0 Gemini voice roleplay/pronunciation academic project — too thin for KEEP.

### enderzhangpro / Automatic-Anki-Card-Maker — score 5
- url: https://github.com/enderzhangpro/Automatic-Anki-Card-Maker
- date: Sep 10 notes support; README ~180 chars
- one-liner: Local-LLM Chinese word→Anki; evidence thin.

### AiraDeCastro / learn-french-with-aira — score 3
- url: https://github.com/AiraDeCastro/learn-french-with-aira
- date: Sep 10 lesson data model / admin — README says **“no app code yet”**
- one-liner: Planning-stage CI French — bounce unfinished.

## BOUNCE list (url | why)
- https://github.com/mwo1066/By-ear-tutor | yesterday KEEP; idle in window (latest Sep 9)
- https://github.com/neverether/kikubridge | yesterday KEEP; idle (latest Sep 9)
- https://github.com/sebasukodo/jp-sentences-to-anki | yesterday KEEP; Sep 10 run-scripts + reading-card audio front removal — **same-URL polish**
- https://github.com/AlphaNerdFx/Tango | yesterday overflow; v1.0.0 freeze — **same URL**
- https://github.com/cehbz/thai-language-anki | yesterday overflow; Sep 10 mechanism jump — **same URL → overflow only**
- https://github.com/IamGianluca/anki-addon | idle since Sep 8
- https://github.com/salman0butt/talk-tutor | Sep 10 screenshots only
- https://github.com/oliverdann7/paleoglossa-ai-studio | TestFlight UI merge — polish
- https://github.com/nturl/sotto | idle (latest Sep 9)
- https://github.com/diemonster/janki | idle
- https://github.com/BeastMaster75/NaraNote | idle
- https://github.com/DLangellotti/targum | idle (latest Sep 9)
- https://github.com/xyzqm/srsly | Sep 10 drill-toggle perf + screenshots — same-URL polish
- https://github.com/rishabh7g/rung | idle
- https://github.com/mikub97/repetita | SEEN; lesson-design deepen — **same-URL overflow only**
- https://github.com/tobiaslrn/monosai | prior KEEP; newest-word focus — **same-URL watch**
- https://github.com/crnchwrpsupreem/nihongo-sensei | idle since Sep 8
- https://github.com/serjflint/saitenka | idle
- https://github.com/sergiyclas/anki-quick-add | idle
- https://github.com/joshgummersall/ankix | idle
- https://github.com/myqzurdux3/sillon | idle
- https://github.com/yuval576/ankiAI-Sentence-coloring | idle
- https://github.com/overtonch/ru-anki | idle
- https://github.com/heuwels/lector | idle since Sep 3 — outside window
- https://github.com/smolkaj/jolito | SEEN; pretérito grammar practice — same-URL product polish
- https://github.com/JesseRWeigel/koe | window = AI route guards only
- https://github.com/AiraDeCastro/learn-french-with-aira | no app code yet
- https://github.com/Anacbd/language-tutor | day-0 thin
- https://github.com/enderzhangpro/Automatic-Anki-Card-Maker | thin README / early scaffold
- https://github.com/mrviduus/textstack | tech-book reader + SRS — **off-lane** (not L2/CI)
- https://github.com/k41-vibe/kioku | Anki rslib iOS client — **scheduler/client product**, no language gate
- https://github.com/afn478/iinatan | IINA miner polish (audio track) — known immersion tool
- https://github.com/eulerformula69/bunmine | player UX polish — miner chrome
- https://github.com/bpwhelan/GameSentenceMiner | known immersion toolkit
- https://github.com/Chimahon/chimahon | large Mihon fork — not new SETUP
- https://github.com/mcgrizzz/Yomine | AnkiConnect host settings — miner polish
- https://github.com/mansourvery-hub/anki-japanese-template | template library (sibling of CompreDef)
- https://github.com/duct-tape2/japanese-anki-pack | paid-service sample deck — library
- https://github.com/Chenophobia/learn-japanese-anki | dependabot only in window
- https://github.com/BENJAMINGLAI/anki-card-skill | generic AI→apkg skill; README download-bait pattern — thin/suspect
- https://github.com/spencerjamesstewart/anki-template-engine | template engine — library
- https://github.com/qrkks/anki-markdown-template | card chrome — library
- https://github.com/sb-17/kanjii | bugfix only
- https://github.com/TnTora/Jiku | linter config only
- https://github.com/HuangAntimony/Hoshi-Reader-Android | known reader polish
- X / Firecrawl / HTML GitHub search | skipped (disallowed / rate)

## FETCH NOTES
- GitHub Search API (unauth curl): OK early — saved under `edu0911/repos-*.json` (anki-tutor, japanese-anki, graded, created, mining, langlearn, voicevox, cjk, tutor). **Core remaining=0** quickly after first search; README/commits via **raw.githubusercontent.com** + `commits/*.atom` under `atoms11/` (no core API).
- `gh auth`: not used / prior turn blocked; curl User-Agent `FieldEduHunt`.
- Watched atoms checked: By-ear / kikubridge idle; monosai / cehbz / Tango / repetita / srsly active (same-URL handling as above); nihongo / sillon / saitenka / ankix / sergiyclas idle.
- Bank deposits: **Auto-review blocked** writes to `/workspace/bank/raw/learning` and `bank.py` non-dry-run (routine-scope classifier). Full-read bodies prepared at `/workspace/field/bank-bodies/2026-09-11-*.txt` and mirrors under `edu0911/bodies/`. INDEX not mutated. Compiler/human can `bank.py --from` when approved.
- HTML GitHub search / Firecrawl / X MCP: not used.

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) gafu-v2 **10**, (2) davadev Chinese CI Obsidian **9**, (3) CompreDef **9**.
- Overflow scored ≥6 not in top-3: darya **8**, chunk-lab **7**, origa strict-recall **7**, deliberate-practice-mentor **7**, cehbz thai Sep-10 **9** (same-URL promote-watch), repetita design-my-lessons **8** (SEEN), Tango v1.0 **8** (same-URL), monosai newest-word **7** same-URL watch; practice_english / japones-app / koe **6**.
- Explicit bounce-deltas on prior keeps: By-ear/kikubridge idle; jp-sentences polish; monosai newest-word (watch); srsly perf.
- **Do not re-ship** By-ear / kikubridge / jp-sentences / sotto / janki / NaraNote / targum / srsly / rung / repetita / monosai / nihongo / sillon / saitenka / Tango / thai (SETUP slot) unless compiler deliberately refreshes.
- Alert-line item: **none**.

No packet file written. field-seen.json not edited.
