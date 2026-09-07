# Field education hunt — 2026-09-06 scratch
Window: ~2026-08-30 → 2026-09-06. Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS** for packet (lane preference). Do NOT write packet; field-seen.json untouched.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) crnchwrpsupreem / nihongo-sensei — PRIMARY
- who: crnchwrpsupreem (first-party publisher + ChatGPT Project contract)
- url: https://github.com/crnchwrpsupreem/nihongo-sensei · live bundle `tutor-data/current/`
- date: publisher push **2026-09-05T23:23Z** (06:23 ICT 6 Sep) — status Ready; generation `2d5b7c9ad5c82866`; 100 reviewed / 100 active; review_events 298. Repo created 2026-08-22; hourly-ish public tutor-context updates all day Sep 5.
- tags: education·tutor-loop·generated-input·teach-once·i-plus-one·reveal-schedule·human-gate
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·generated-input·teach-once·i-plus-one·reveal-schedule] score=10 | crnchwrpsupreem / nihongo-sensei | Phone-only Anki reviews → Windows/Linux mini-PC syncs AnkiWeb, extracts **read-only**, publishes a public tutor bundle (`manifest.json`, `voice-corpus.txt` FRESH/REINFORCE/MATURE, sharded cards, `tutor-policy.json`). ChatGPT Project boots with verbatim corpus load (must report `generation_id` + counts) then Voice practice: exact-card meaning + exact-JP recall in file order; only after full coverage may **controlled variations** swap exactly one reviewed lexical item (labelled “generated variation”, never Anki material). Untouched cards excluded. Killed: tutor-from-memory if corpus missing; shuffle/skip FRESH; treat KNOWN WORDS as drill queue; invent grammar in variations. Distinct from ankimcp (live MCP over Anki tools), bornayo7 (owns SRS host), monosai (reader/story gen) — this is **Anki→published corpus→ChatGPT voice tutor** with an exact-then-generate gate. | https://github.com/crnchwrpsupreem/nihongo-sensei
- why distinct: source-of-truth is the learner’s reviewed Anki, but the tutor never writes Anki; practice order and variation ceiling are machine-published policy.
- bank: README already `2026-09-04-crnchwrpsupreem-nihongo-sensei-publisher-…`; instructions deposited `2026-09-06-crnchwrpsupreem-nihongo-sensei-chatgpt-project-instructions-exact`.

### 2) myqzurdux3 / sillon — STRONG
- who: myqzurdux3 (first-party FR+EN READMEs; 198 JVM + 15 instrumented AnkiDroid tests)
- url: https://github.com/myqzurdux3/sillon
- date: push **2026-09-05T21:32Z** (04:32 ICT 6 Sep) — voice-stack hardware tests + mic/service fixes; created 2026-08-26.
- tags: education·tutor-loop·human-gate·taste-gate·killed-claim·teach-once
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·human-gate·taste-gate·killed-claim] score=10 | myqzurdux3 / sillon | Android hands-free Anki review while driving: due card → spoken rephrased question → listen → judge → announce proposed grade → **one-word spoken override** before Anki write. Four gates: (1) **model proposes, code disposes** — LLM returns JSON only; code validates/clamps/recomputes grade, never touches the collection; (2) **writes lag one card** so « reviens » can undo (AnkiDroid API has no undo); (3) **journal mode default** — first drives log what *would* have been graded before trusting the schedule; (4) **failure ≠ silence** (mic/network/AnkiDroid refuse are spoken + journaled). LaTeX prépa cards spoken as math, not “backslash cos”. Killed: LLM direct Anki write; silent fail→everything Again; hand-copied command cheatsheet (commands generated from parser). Distinct from ankimcp present/rate MCP loop and nihongo-sensei ChatGPT voice — this is **in-car voice tutor over live AnkiDroid due queue** with deferred write + journal dry-run. | https://github.com/myqzurdux3/sillon
- why distinct: portable tutor-loop gates on AnkiDroid (propose/dispose, lag-write, journal-first, no silent fail), not immersion mining or story gen.
- bank: `2026-09-06-myqzurdux3-sillon-hands-free-voice-anki-review`.

### 3) tobiaslrn / monosai — STRONG (3rd SETUP slot)
- who: tobiaslrn
- url: https://github.com/tobiaslrn/monosai · https://tobiaslrn.github.io/monosai/
- date: push **2026-09-05T21:48Z** (04:48 ICT 6 Sep) — Words screen + reader tap/hold; created 2026-08-17.
- tags: education·i-plus-one·generated-input·teach-once·human-gate
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·i-plus-one·generated-input·teach-once·human-gate] score=9 | tobiaslrn / monosai | Beginner Japanese PWA: generate very simple stories from ~**50 reviewed Anki expressions** + chosen grammar level; also paste any text → furigana, spacing, unknown-word highlights, in-reader dictionary. Anki is **read-only** (AnkiConnect or local `.apkg`/`.colpkg`; never changes cards/history). AI optional BYOK OpenRouter (translate / grammar / TTS / story gen); core reader+dict+Anki work offline after first open. Killed: “need AI to use the reader”; write-back into Anki from generated stories. Distinct from nihongo-sensei (voice exact-card tutor), saitenka (mpv mine), bornayo7 (owns SRS) — this is **Anki-known-vocab ceiling → graded/generated reading input**. | https://github.com/tobiaslrn/monosai
- why distinct: i+1 applies to **story generation / reading** gated by reviewed Anki vocab, not review scheduling or mining.
- bank: `2026-09-06-tobiaslrn-monosai-anki-grounded-japanese-beginner-reader`.

## Scored but NOT in top-3 SETUP slots (notes for compiler / overflow)

### serjflint / saitenka — score 9 (overflow / next-packet)
- url: https://github.com/serjflint/saitenka
- date: push 2026-09-05T21:50Z — mining audio bound + quality loops; created 2026-07-21 (★5, mature docs).
- tags: education·i-plus-one·human-gate·teach-once·killed-claim
- portable / evidence / combined: **4 / 5 / 9**
- alert: **no**
- one-liner: mpv immersion workstation — FSRS-aware subtitle coloring with **N+1** highlight, Yomitan-style multi-dict tooltip composited **inside** mpv OSD (no second window), one-key/bulk Anki mine; readings/pitch from dictionaries never LLM. Killed: fragile browser-texthooker+overlay chain; “known = ever seen” (uses live FSRS state). Distinct from bounced Jumprocks mining-helper and SubMiner Electron — in-mpv FSRS N+1 + grounded mine.
- why not top-3 SETUP: strong product/practice but closer to immersion-mining tooling than a new tutor-loop SETUP; lane cap prefers nihongo + sillon + monosai. Prefer as overflow if packet wants a 4th education line.
- bank: `2026-09-06-serjflint-saitenka-mpv-immersion-workstation-with-fsrs`.

### yuval576 / ankiAI-Sentence-coloring — score 7 (overflow / cap)
- url: https://github.com/yuval576/ankiAI-Sentence-coloring
- date: created+push 2026-09-05; Windows-first personal prototype for Russian Core 5000 fields.
- tags: education·generated-input·tutor-loop·teach-once
- portable / evidence / combined: **3 / 4 / 7**
- alert: **no**
- one-liner: permanent RU↔EN sentence color spans saved into note fields (offline after sync) + vocab library that does **not** count lookups as learned + optional Luna tutor; dry-run/checkpoint/circuit-breaker on batch coloring. Portable ceiling: Core-5000 field layout / personal prototype.
- why not top-3: narrower deck coupling + prototype framing; overlaps overtonch Russian lane less cleanly than sillon/monosai gates.
- bank: `2026-09-06-yuval576-anki-ai-sentence-coloring-permanent-ru`.

### sergiyclas / anki-quick-add — commit `18b9289` offline translation fix — score n/a (already kept; bounce delta)
- url: https://github.com/sergiyclas/anki-quick-add/commit/18b9289e3cd95ddd671aa1ad72ccb3faa23f76a9
- date: 2026-09-05T04:46Z — “fix: stop refusing an offline translation the browser is ready to do”; sibling commits = 100-sentence eval defects + Test button docs (2.2.0).
- tags: (prior keep) generated-input·human-gate
- portable / evidence: polish on **already kept** sense-in-context `8920200` (packet 2026-09-05).
- alert: **no**
- recommendation: **BOUNCE** as incremental fix, not a new SETUP. Do not re-keep.

### joshgummersall / ankix — warm gloss model — score n/a (already kept; bounce delta)
- url: https://github.com/joshgummersall/ankix (PR #12 warm-model-on-startup; README “gloss” definition 2026-09-05T21:01Z)
- date: 2026-09-05 — keep model loaded / warm at startup; teach-once naming of “gloss”.
- portable / evidence: performance + glossary polish on **already kept** Sep-3 ankix (Kindle/YouTube→local Ollama contextual notes).
- alert: **no**
- recommendation: **BOUNCE** as polish, not a new SETUP.

## BOUNCE list (url | why)
- https://github.com/ankimcp/anki-mcp-server | already kept (forgetCards/setDueDate + omit-answers #63 banked); Sep 4 commits = NestJS 12 / chore — no new SETUP
- https://github.com/mansourvery-hub/CompreDef | already kept dictionary ladder; v1.1.0 Yomitan `/termEntries` + MV3 keepalive = bridge polish, same portable gate
- https://github.com/bornayo7/srs-app · https://github.com/overtonch/ru-anki | already kept; no new in-window SETUP delta
- https://github.com/amarcozzi/anki-mcp · https://github.com/diotima-garden/anki-mcp · https://github.com/portpowered/anki-web-mcp · https://github.com/rockyxwall/anki-connect-mcp | already seen/bounced; thin or duplicate MCP lane
- https://github.com/mansourvery-hub/anki-japanese-template | already bounced (UI note type)
- https://github.com/sergiyclas/anki-quick-add (18b9289 + 2.2.0 eval fixes) | already kept sense-in-context; offline-translator polish only
- https://github.com/joshgummersall/ankix (warm model / gloss README) | already kept; perf polish only
- https://github.com/Lilislv/Setsuna | thin product README; no named gate diary
- https://github.com/a-sinkevich/book2anki | auto book/YT→deck; weak human-gate vs Make/Discard / prepare-commit
- https://github.com/FrostySL/anki-card-forge | lecture→cards forge; off language-tutor lane / assignment-adjacent
- https://github.com/Nikodem5/mcp-anki | empty (no README on main/master)
- https://github.com/Bojackson123/lecture-parser | lecture study parser; not language lane
- https://github.com/andersonlizarazo/Anki-WarmTemplate · https://github.com/BCFCODE/AnkiNoteTypes · deck drops / Heisig / genetics-anki | library/content, not practice gates
- https://github.com/cidade360/mneme-memory-forge · https://github.com/opennote-org/opennote | memory/notebook MCP, not education lane
- https://github.com/alphaparkinc/genpark-spaced-repetition-anki-flashcard-knowledge-synthesizer-skill | skill library synthesizer
- grokbot.dev education use-cases score≥80 | **none new** (see grokbot scratch); templates = library bounce
- X / Twitter education pins | not swept (X MCP down; instructed skip)

## FETCH FAILURES
- GitHub HTML search `anki pushed:>2026-09-01` → **HTTP 429** (used Search API + commits.atom + raw README instead).
- `mansourvery-hub/CompreDef` commits/`main`.atom → 404; **master**.atom worked.
- `doasfrancisco/anki-skill` commits/`main`.atom → 404.
- `Nikodem5/mcp-anki` README main/master → 404 (empty repo).
- `a-sinkevich/book2anki` README on `main` → 404; `master` OK.
- X MCP / Firecrawl: not used (down / disallowed).
- Unauthenticated `gh` not required; Search API returned 200 for both queries.

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) nihongo-sensei 10, (2) sillon 10, (3) monosai 9.
- Overflow scored ≥6 not recommended under 3-SETUP cap: saitenka 9, yuval576 7.
- Explicit bounce-deltas on prior keeps: sergiyclas `18b9289`, ankix warm-model.
- Alert-line item: **none**.
- Empty education streak: broken if compiler takes the 3 SETUPS (prior 21:1 → this hunt 3).

No packet file written. field-seen.json not edited.
