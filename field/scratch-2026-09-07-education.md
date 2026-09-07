# Field education hunt — 2026-09-07 scratch (Monday)
Window: ~2026-09-05 00:00 UTC → now (prefer pushes 2026-09-06 / 2026-09-07). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday packet KEEP (SKIP re-keep unless NEW distinct mechanism): nihongo-sensei 10, sillon 10, monosai 9. Overflow: saitenka 9, yuval576 7.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) overtonch / ru-anki — Speaking **Activate** mode — PRIMARY (NEW mechanism on prior keep)
- who: overtonch (first-party LEARNING.md learner diary + `app/activate.py` shipped 2026-09-06)
- url: https://github.com/overtonch/ru-anki · `LEARNING.md` · `app/activate.py` · `app/data/activate/verbs.json.gz`
- date: Activate commits **2026-09-06T16:40–16:55Z** (verb-government gym, productive-vocab track, CEFR slider, prompt-as-thought, skip-I-know). LEARNING.md knowledge base same day. Prior keep was YouTube→Make/Discard only.
- tags: education·tutor-loop·teach-once·i-plus-one·reveal-schedule·human-gate
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·tutor-loop·teach-once·i-plus-one·reveal-schedule] score=9 | overtonch / ru-anki Activate | Silent phone pocket drill that closes the **passive→active gap**: app names a TARGET + a concrete English *thought to express* (not an instruction); learner forms Russian silently/typed, then checks. Two shipped tracks — **verb-government gym** (220-verb bundled curriculum, hardness-ranked so English-speaker traps come first; SM-2-lite) and **productive-vocabulary** (newest-frequent from `freq`, active-word count on Level tab). **CEFR ladder** a1→b2+ pitches prompt complexity; `mix` sets verb/word ratio; per-day new-item budget; focused LLM check on typed attempts; skip/"I know this". Frame-gym track planned. Distinct from prior ru-anki Keep (YT→candidates→Make/Discard) and from Speak reformulation mode (Sep 2) — this is **finite curriculum production tutor** with CEFR-gated prompts. | https://github.com/overtonch/ru-anki
- why distinct: NEW mechanism vs yesterday/prior — production tutor-loop over verb government + productive vocab, not mining or recognition SRS.
- bank: `2026-09-07-overtonch-ru-anki-learning-md-activate-passive` (LEARNING.md+Activate); prior `2026-09-02-overtonch-ru-anki-youtube-…` left as mining keep.

### 2) serjflint / saitenka — STRONG (yesterday overflow → **fill a SETUP slot today**)
- who: serjflint
- url: https://github.com/serjflint/saitenka
- date: continued Sep 6 activity — subtitle provider languages (#503), run-path cache by profile language (19:25–19:31Z); mining audio/quality already banked Sep 5–6. Created 2026-07-21.
- tags: education·i-plus-one·human-gate·teach-once·killed-claim
- portable / evidence / combined: **4 / 5 / 9**
- alert: **no**
- one-line packet shape: [education·i-plus-one·human-gate·teach-once·killed-claim] score=9 | serjflint / saitenka | mpv immersion workstation — FSRS-aware subtitle coloring with **N+1** highlight, Yomitan-style multi-dict tooltip composited **inside** mpv OSD, one-key/bulk Anki mine; readings/pitch from dictionaries never LLM. Sep 6: multi-language subtitle providers keyed by profile. Killed: fragile browser-texthooker+overlay; “known = ever seen”. Distinct from monosai (story gen) and nihongo-sensei (voice exact-card) — **in-mpv FSRS N+1 + grounded mine**. | https://github.com/serjflint/saitenka
- why fill today: still only overflow from packet 24; no newer immersion SETUP beat it; lane cap yesterday preferred tutor-loops (nihongo/sillon/monosai). **Yes — promote to a SETUP slot** if compiler wants 3 education lines and is not re-shipping yesterday’s three.
- bank: already `2026-09-06-serjflint-saitenka-mpv-immersion-workstation-with-fsrs`.

### 3) pricees / note-buddy — STRONG (wiki-craft / human-gate)
- who: pricees (OSS’d + cron entry 2026-09-06)
- url: https://github.com/pricees/note-buddy
- date: created/open-sourced **2026-09-06** (mermaid, source-image embed, cron.sh unattended entry); pushes through 23:15Z.
- tags: education·human-gate·taste-gate·wiki-craft·teach-once
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·human-gate·taste-gate·wiki-craft·teach-once] score=8 | pricees / note-buddy | Photograph handwritten page → Claude Code (no API key) → **Obsidian always**; Anki **only when the page literally says “Anki”** (margin/header; does not guess from content). Content-hash ledger = no double-transcribe; source photo embedded under `## Source`; hand-drawn diagrams → mermaid; Anki cards back-link `obsidian://`; Anki-down still completes Obsidian + `--retry-failed`. Companion `danki.py` = URL/PDF/text → reviewed cards. Cron-safe unattended path. Distinct from sergiyclas prepare/commit and AgriciDaniel YT→wiki — this is **page-inscribed opt-in Anki** over wiki-craft capture. | https://github.com/pricees/note-buddy
- why distinct: portable human-gate is the literal word on the page, not a UI Make/Discard after LLM proposes.
- bank: `2026-09-07-pricees-note-buddy-handwritten-page-obsidian-always`.

## Scored but NOT in top-3 SETUP slots (overflow)

### mikub97 / repetita — score 6 (overflow / watch)
- url: https://github.com/mikub97/repetita
- date: created+scaffold **2026-09-06T22:46–23:04Z** — engine types, graders, SM-2 + FSRS-6 + Leitner backends; agent working-context docs.
- tags: education·teach-once·killed-claim
- portable / evidence / combined: **4 / 2 / 6**
- alert: **no**
- one-liner: open SRS engine — one note → many direction-cards (recognition/production/listening/spelling); **CI quarantines exercises that give away their own answer**; courses as YAML. Pre-alpha extracted from private daily-use app (PT→PL). Evidence thin (day-1 public scaffold).
- why not top-3: mechanism promising but public evidence is scaffold-only; watch for first real course + learner loop.
- bank: `2026-09-07-mikub97-repetita-hackable-srs-engine-one-note`.

### smolkaj / jolito — score 7 (overflow / product)
- url: https://github.com/smolkaj/jolito · https://joli.to
- date: dual-voice / study-session refs through **2026-09-06T23:01Z**
- tags: education·tutor-loop·human-gate·teach-once
- portable / evidence / combined: **3 / 4 / 7**
- alert: **no**
- one-liner: named runner (Mexico City / IH Condesa) Mexican-Spanish SRS PWA — keyboard typed recall + self-grade, ear-first dual voices, Anki import, offline lexicon. Solid practice app; fewer novel portable gates than Activate/saitenka/note-buddy.
- bank: `2026-09-07-smolkaj-jolito-mexican-spanish-typed-recall-srs`.

### yuval576 / ankiAI-Sentence-coloring — score 7 (still overflow)
- Sep 5–6 polish (offline verb details, queue-only resume under Anki lock). No new SETUP beyond yesterday’s overflow note.

## BOUNCE list (url | why)
- https://github.com/crnchwrpsupreem/nihongo-sensei | yesterday KEEP 10; Sep 6–7 = hourly `Update public tutor context` only — **no new mechanism**
- https://github.com/myqzurdux3/sillon | yesterday KEEP 10; Sep 6 `attendre/avouer/corriger` voice-command precision — polish on propose/dispose loop, not new SETUP
- https://github.com/tobiaslrn/monosai | yesterday KEEP 9; Sep 6 suspended-card exclusion + reader/enrichment fixes — polish
- https://github.com/sergiyclas/anki-quick-add | already kept; only Sep 5 offline-translator / Test-button docs
- https://github.com/joshgummersall/ankix | already kept; warm-model/gloss README only
- https://github.com/bornayo7/srs-app | already kept; Sep 6 UI/GIF/unlock polish
- https://github.com/mansourvery-hub/CompreDef | already kept; v1.1.1–1.1.4 regression-release churn
- https://github.com/ankimcp/anki-mcp-server | already kept; no commits since Sep 4
- https://github.com/0x00000024/korean-anki-pro | new Sep 6 deck generator (LLM dict + TTS + illust) — content pipeline, weak human-gate vs Make/Discard
- https://github.com/a-sinkevich/book2anki | already bounced; still auto book/YT→deck
- https://github.com/amerharb/sawt | audio-first micro-apps (week/flag/color…); product suite version bumps, not tutor-loop diary
- https://github.com/savethebeesandseeds/caatuu | local-first playful language worlds; Android publish churn — product platform, thin named gate
- https://github.com/monsieur-trenton/concordance | Sep docs/roadmap milestone — platform marketing, not runner practice
- https://github.com/hajisensai/Fushi | immersion suite; Sep 6 icon/installer art — product polish
- https://github.com/Kodomoppoi/LANGUAGE-STORIES | no activity since Sep 2 merge
- https://github.com/EhsanShahbazii/Anki-Vocab | VS Code vocab extension branding/icon — thin
- https://github.com/tamerlanmustafa/wordwise | movie-script vocab product UI (practice staircase)
- https://github.com/CiscoPonce/Harmonix | lyrics learning app / Play Store docs
- https://github.com/nicholasbeskow/morsanki-data | schedule.json churn for Morse Anki addon — data not practice gate
- https://github.com/Samson312/WortFrosch | init-only German app scaffold
- https://github.com/FrostySL/anki-card-forge · Lilislv/Setsuna · Nikodem5/mcp-anki · MCP clones | prior bounce / empty / off-lane
- grokbot.dev education ≥80 | not re-swept this hunt (sibling lane); no claim of new hits
- X / Firecrawl | skipped (down / disallowed)

## FETCH NOTES
- GitHub Search API: OK early (`gh-api-search-20260907.json` 50 hits; `gh-api-search2-20260907.json` 40 hits). Later **core API rate-limit remaining=0** (unauthenticated); switched to **commits.atom + raw.githubusercontent.com**.
- `gh auth`: not logged in — no authenticated quota.
- saitenka `commits/master.atom` → empty/404; **`commits/main.atom` OK**.
- Watchlist atoms07/: nihongo (hourly), sillon, monosai, overtonch (Activate), bornayo7, CompreDef, ankix, sergiyclas, ankimcp (none since Sep4), yuval576.
- New candidate atoms: repetita, note-buddy, korean-anki-pro, Fushi, caatuu, concordance, sawt, jolito, wordwise, morsanki-data, Harmonix, Anki-Vocab, WortFrosch.
- WebSearch: mostly known Anki MCP / Yomitan / AnkiForgeAI — no fresh named tutor diary beyond GitHub hits.
- Bank: deposited Activate LEARNING, note-buddy, repetita, jolito. saitenka already deposited 2026-09-06. Same-source re-deposit of github.com/overtonch/ru-anki **dup’d** to Sep-2 mining entry — used raw LEARNING.md URL instead.
- HTML GitHub search / Firecrawl / X MCP: not used.

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) overtonch Activate **9**, (2) saitenka **9** (promote yesterday overflow), (3) note-buddy **8**.
- Overflow scored ≥6 not in top-3: jolito 7, yuval576 7, repetita 6.
- Explicit bounce-deltas on prior keeps: nihongo hourly corpus, sillon voice-cmds, monosai suspended-card, CompreDef 1.1.x, bornayo7 UI.
- **saitenka fill?** Yes — still overflow-only from yesterday; no stronger *new* immersion SETUP appeared; Activate is stronger as *new tutor-loop* but does not replace saitenka’s N+1 mining niche. Promote saitenka into a SETUP slot today.
- Alert-line item: **none**.
- Do not re-ship nihongo-sensei / sillon / monosai unless compiler deliberately refreshes prior packet lines.

No packet file written. field-seen.json not edited.
