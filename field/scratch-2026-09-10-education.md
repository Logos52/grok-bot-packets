# Field education hunt — 2026-09-10 scratch (Thursday)
Window: ~2026-09-09 00:00 UTC → now (prefer pushes 2026-09-09 / 2026-09-10). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): nturl/sotto 9, diemonster/janki 9, BeastMaster75/NaraNote 8. Overflow bounced same-URL: mikub97/repetita 9, cehbz/thai-language-anki 8, rh20051/WaniSieve 7, s4s4s4s/sat-srs 7, Micheon 7, LearnWithNoura 7, ahadiff 7, SmarterTypeField 6, turna 6, freesurf language-tutor 6, targum/srsly/rung polish-only same URL.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt` (53 github hosts listed); bank INDEX hits for same URL this week unless commit-scoped mechanism jump.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) mwo1066 / By-ear-tutor — Voice-only Vietnamese; code-planned turns; literal scaffold — PRIMARY
- who: mwo1066
- url: https://github.com/mwo1066/By-ear-tutor
- date: created **2026-08-07**; heavy **2026-09-09** content audit (~18:37–18:51Z) — “An audit that turns 1278 words into a shortlist of 83” + cupboard candidate cleanup + glossary correction
- tags: education·tutor-loop·i-plus-one·teach-once·reveal-schedule·quiet-when-nothing·generated-input·human-gate
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·reveal-schedule·teach-once·i-plus-one·quiet-when-nothing] score=10 | mwo1066 / By-ear-tutor | **Voice-only** language tutor (nothing typed/read): mic opens on its own, silence ends the turn. Teaches **Northern Vietnamese** today; engine is language-agnostic (`content/` only). Portable gates measured from Paul Noble transcripts: **never “repeat after me”** (0/25 min) — always “how would you say ___?”; words taught **because a sentence needs them** (phrase never surfaces before its parts — code-enforced); **literal scaffold** spoken one beat before production (“literally: you healthy not?”); **levels decay but never reach zero** (recurrence in words-met, not calendar). **Curriculum is decided in code**, not by the LLM — model gets exactly one instruction per turn (introduce / recall / literal+ask). Two voices: L1 tutor + native Minh who only says target. Dev honesty: `--from=` and `--fresh` **save nothing** so they cannot mark unheard items as taught; offline `smoke_test.py`; `SPEC.md` ~60 rules; `METHOD.md` keeps the recording counts. Sep 9 = content shortlist audit, not product chrome. Distinct from talk-tutor (SaaS Gemini Live chat) and sotto (graded reader + availability gate) — **ear-first sentence-building with planner≠model**. | https://github.com/mwo1066/By-ear-tutor
- why distinct: NEW URL to Field; Vietnamese L2 + portable planner/literal/never-retire gates not on yesterday’s sotto/janki/NaraNote roster.
- bank: `2026-09-10-mwo1066-by-ear-tutor-voice-only-vietnamese`

### 2) neverether / kikubridge — Premade JA decks → one Kiku note type; idempotent merge — STRONG
- who: neverether
- url: https://github.com/neverether/kikubridge
- date: created **2026-09-09**; same-day headless setup docs, converter/manifest, provenance footer plugin (through ~09:37Z)
- tags: education·teach-once·human-gate·quiet-when-nothing
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·teach-once·human-gate] score=8 | neverether / kikubridge | Converts premade Japanese decks (Kaishi 1.5k, Ankidrone Essentials, …) into **one Kiku note type**; merges the same word across decks into a **single note with several example sentences**; **idempotent re-run** (only drift touched; review history never affected; reserved manual fields survive). Provenance kept as **tags** + optional card footer plugin showing source deck. Built for **headless Anki in Docker** over AnkiConnect + self-hosted sync; also works against desktop AnkiConnect. `plan` before `import`; new decks = one converter file. Honest AI-built disclaimer. Distinct from janki (lesson-photo miner) and WaniSieve (level/burned sieve) — **multi-deck → one note-type with safe merge + provenance**. | https://github.com/neverether/kikubridge
- why distinct: NEW URL same day; deck-ownership / merge-without-duplicate portable loop not shipped yesterday.
- bank: `2026-09-10-neverether-kikubridge-premade-ja-anki-decks-kiku`

### 3) sebasukodo / jp-sentences-to-anki — Bring your i+1 JSON; local VOICEVOX → .apkg — STRONG
- who: sebasukodo
- url: https://github.com/sebasukodo/jp-sentences-to-anki
- date: created **2026-09-09T17:04Z**; init + docs + example field-name fix through **17:45Z**
- tags: education·i-plus-one·generated-input·teach-once
- portable / evidence / combined: **4 / 3 / 7**
- alert: **no**
- one-line packet shape: [education·i-plus-one·generated-input] score=7 | sebasukodo / jp-sentences-to-anki | Bring a JSON of **i+1 Japanese sentences** (exactly one new word each — script **does not check**; assumes you already built them that way) → local **VOICEVOX** TTS (no upload, no API keys) → ready `.apkg`. Card layout emphasizes the target word (highlight + separate word audio + sentence audio); optional **audio-first** card type or `both`. Honest about card-type lock-in (switching later = new note type / review reset). ffmpeg optional (else huge WAVs). Distinct from monosai (story gen from known Anki vocab) and Tango (YT transcript miner) — **learner-supplied i+1 sentences + local JP TTS deck builder**. | https://github.com/sebasukodo/jp-sentences-to-anki
- why distinct: brand-new URL; named i+1 card contract + local VOICEVOX pipeline not on yesterday’s keeps.
- bank: `2026-09-10-sebasukodo-jp-sentences-to-anki-i-1`

## Scored but NOT in top-3 SETUP slots (overflow)

### AlphaNerdFx / Tango — score 8 (overflow / promote-watch)
- url: https://github.com/AlphaNerdFx/Tango
- date: created 2026-06-30; **2026-09-09** v0.12.0 docs + 1346-test release notes + sort-key honesty
- tags: education·generated-input·quiet-when-nothing·i-plus-one
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-liner: YouTube → transcript (prefer manual) → spaCy POS filter → **three-condition fuzzy morph duplicate check** against existing Anki deck → .apkg / doctor / docker. Strong immersion→Anki gate; NEW to Field skip-list but mature product — leave overflow under cap-3 unless compiler prefers miner over kikubridge/jp-sentences.
- bank: `2026-09-10-alphanerdfx-tango-youtube-transcript-spacy-fuzzy-morph`

### cehbz / thai-language-anki — score 9 (overflow; same URL as yesterday — mechanism jump)
- url: https://github.com/cehbz/thai-language-anki
- date: **2026-09-09** ~13:58–15:31Z — clause store; draft as clauses; **refuse a deck whose sentence fails introducibility**; curated survive migrate re-run; introducible word ids
- tags: education·taste-gate·human-gate·teach-once·generated-input
- portable / evidence / combined: **5 / 4 / 9** (was 4/4/8 yesterday)
- alert: **no**
- one-liner: generation-side fitness now refuses un-introducible sentences at deck boundary. Same URL → overflow / promote-watch only.
- bank: `2026-09-10-cehbz-thai-language-anki-sep-9-clause` (commit-window scoped)

### IamGianluca / anki-addon — score 7 (overflow; cross-domain)
- url: https://github.com/IamGianluca/anki-addon
- date: **2026-09-08** curator evals (code-block vs inline by role); planning docs
- tags: education·human-gate·taste-gate·teach-once
- portable / evidence / combined: **4 / 3 / 7**
- one-liner: LLM note refactor + cluster curator with **no write access** until human batch-approves; session traces. Strong human-gate, not L2-specific — overflow only.
- bank: `2026-09-10-iamgianluca-anki-ai-curator-llm-note-refactor`

### salman0butt / talk-tutor — score 6
- url: https://github.com/salman0butt/talk-tutor
- date: created 2026-09-08; **2026-09-09** AI-quality foundation + feedback reliability + README rewrite
- tags: education·tutor-loop
- portable / evidence / combined: **3 / 3 / 6**
- one-liner: Gemini Live SaaS voice tutor (placement quiz, SRS vocab, Practice My Mistakes). Product-complete; fewer named portable gates than By-ear.

### oliverdann7 / paleoglossa-ai-studio — score 6
- url: https://github.com/oliverdann7/paleoglossa-ai-studio
- date: **2026-09-09** TestFlight UI / mobile review polish (i+1 recommendations already shipped earlier)
- one-liner: ancient-language immersive reader product; window = mobile polish, not new gate.

### jhhr / anki_addons — score 6
- url: https://github.com/jhhr/anki_addons
- date: **2026-09-09** related_card_disperse bury-across-decks cache fixes
- one-liner: addon monorepo tooling; sibling-bury useful but not a language SETUP.

### zubko / wanikani-explore-export — score 6
- url: https://github.com/zubko/wanikani-explore-export
- date: pushed **2026-09-09**
- one-liner: WaniKani explore → Anki with component cards; solid personal tool, thinner portable diary than kikubridge.

### tobiaslrn / monosai — score 7 (same-URL watch; do not re-keep)
- url: https://github.com/tobiaslrn/monosai (SEEN)
- date: **2026-09-09** vocabulary browser + **disambiguate words by Anki meaning field**, not surface form only
- one-liner: real mechanism (meaning-keyed known-set) but **same URL / prior KEEP** — bounce re-keep; compiler may note as watch.

### nturl / sotto — same-URL polish (do not re-keep)
- **2026-09-09** tap-to-save vocabulary from tutor conversations + mobile tutor recovery — incremental on yesterday KEEP.

## BOUNCE list (url | why)
- https://github.com/nturl/sotto | yesterday KEEP; Sep 9 tap-to-save / mobile tutor recovery — **same-URL polish**
- https://github.com/diemonster/janki | yesterday KEEP; no Sep 9 commits (last Sep 8)
- https://github.com/BeastMaster75/NaraNote | yesterday KEEP; no Sep 9 commits (last Sep 8 batch kanji)
- https://github.com/DLangellotti/targum | prior KEEP; Sep 9 “disagree with the offer” / words-on-every-door — **same-URL quiet refinements**
- https://github.com/xyzqm/srsly | prior KEEP; Sep 9 French conjugation engine + card-wait fix — **same-URL language expansion**
- https://github.com/rishabh7g/rung | prior KEEP; Sep 9 **removes** exit ritual (“Practice session climbs the rung”) + L5 Voice content — **same URL; gate subtraction / content**
- https://github.com/mikub97/repetita | yesterday overflow; no Sep 9 commits
- https://github.com/tobiaslrn/monosai | SEEN / prior KEEP; meaning-field disambiguation — **same-URL watch, do not re-keep**
- https://github.com/crnchwrpsupreem/nihongo-sensei | hourly public-tutor-context churn through Sep 8 — no new mechanism
- https://github.com/serjflint/saitenka | prior; Sep 8 perf/telemetry — immersion workstation already shipped
- https://github.com/sergiyclas/anki-quick-add | idle since Sep 5
- https://github.com/myqzurdux3/sillon | idle since Sep 7
- https://github.com/joshgummersall/ankix | idle since Sep 5
- https://github.com/bornayo7/srs-app | Sep 9 docs “plan SRS overhaul” only — no shipped gate
- https://github.com/ankimcp/anki-mcp-server | SEEN; dependency bumps / notesInfo schema — **library/MCP**
- https://github.com/yuval576/ankiAI-Sentence-coloring | idle since Sep 5
- https://github.com/overtonch/ru-anki | idle since Sep 7
- https://github.com/hajisensai/Fushi | SEEN immersion suite; packaging churn
- https://github.com/MuggleWu/miki | FSRS-6 Anki-alt + MCP — **scheduler product, no language gate** (also bounced yesterday)
- https://github.com/mikemazzetti/ankicardmaker | Claude→AnkiMCP card maker + AnkiWeb backup; decks are **NeetCode/STEM** — off-lane
- https://github.com/lyuehh/chinese-character-anki | CSV/AnkiWeb dump from chinese.getbuzzi.com — **dataset / library**
- https://github.com/SlyNinjutsu07/quizlet-to-anki-generator | early Quizlet→apkg scaffold; CLI “not wired up yet” — **thin / unfinished**
- https://github.com/icem0/anki-mcp | headless Anki MCP sidecar — **library / infra**
- https://github.com/rockyxwall/mcp-anki-connect | AnkiConnect MCP — **library**
- https://github.com/AluiQT/anki-pitch-tool | personal backend/quiz-on-Anki-cards learning tool — **off-lane**
- https://github.com/heuwels/lector | strong LingQ-alt reader; master atom last commit **2026-09-03** — **outside window mechanism**
- https://github.com/AsrorbekQ/teleport | Xteink e-reader firmware + Anki-style cards — hardware fork, thin language gate
- https://github.com/EnPriseWithEase/chess-puzzle | chess Anki template — **off-lane**
- https://github.com/mfaridzia/swaralingo | speaking practice web app; Sep 10 header polish — product chrome
- https://github.com/ksyasuda/SubMiner | mature mpv+Yomitan miner; activity in window but known product
- https://github.com/Chimahon/chimahon | Mihon immersion fork ★192 — large product, not new SETUP this window
- https://github.com/bpwhelan/GameSentenceMiner | known immersion toolkit polish
- https://github.com/0xzerolight/anki_miner | known miner polish
- https://github.com/mansourvery-hub/anki-japanese-template | card template library
- https://github.com/Uncorrected-nova574/playtranslate | thin / previously suspect
- X / Firecrawl / HTML GitHub search | skipped (disallowed / 429)

## FETCH NOTES
- GitHub Search API (unauth): OK early — saved under `edu0910/repos-*.json` (anki-lang, japanese-anki, langlearn-anki, anki-mcp, tutor-voice, graded, cjk-thai, immersion, sea, created-after). Search remaining stayed available; **core remaining=0** after README/commits API fan-out → **403**.
- Fallback: `raw.githubusercontent.com` READMEs + `commits/*.atom` under `atoms10/` (candidates + watchlist).
- `gh auth`: not logged in; no token.
- Commit search (`commits-anki.json`) polluted by far-future committer dates / non-Anki “reader” hits — not used for ranking.
- Bank deposits (lane learning, via grok-bot/Field): By-ear, jp-sentences-to-anki, kikubridge, Tango, IamGianluca, cehbz Sep-9 clause note. INDEX updated OK (no Auto-review block).
- Bodies also mirrored under `/workspace/field/bank-bodies/` and `/workspace/field/edu0910/bodies/`.
- HTML GitHub search / Firecrawl / X MCP: not used.

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) By-ear-tutor **10**, (2) kikubridge **8**, (3) jp-sentences-to-anki **7**.
- Overflow scored ≥6 not in top-3: Tango **8**, cehbz thai Sep-9 **9** (same-URL promote-watch), IamGianluca **7**, talk-tutor **6**, paleoglossa **6**, jhhr anki_addons **6**, wanikani-explore-export **6**; monosai meaning-key **7** same-URL watch only.
- Explicit bounce-deltas on prior keeps: sotto tap-save; targum disagree-offer; srsly FR conjugation; rung **exit-ritual removal**; NaraNote/janki idle Sep 9.
- **Do not re-ship** sotto / janki / NaraNote / targum / srsly / rung / repetita / monosai / nihongo / sillon / saitenka / overtonch unless compiler deliberately refreshes.
- Alert-line item: **none**.

No packet file written. field-seen.json not edited.
