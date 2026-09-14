# Field education hunt — 2026-09-14 scratch (Monday)
Window: ~2026-09-13 00:00 UTC → now (prefer pushes 2026-09-13 / 2026-09-14). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Prefer JA/ZH/KO/FI/DE/IT. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): cherkasoviy/nihongo-tutor 10, mansourvery-hub/anki-japanese-template 9, suiginko/Shiori-ai-japanese-tutor 8. Overflow promote-watch: mShono/finn_cards 9 (still idle), Dilnazzzz/bridge 9 (still Sep 10), leibnitz27/ittutor 8, gillisandrew/ancci 7, bee-san grammar 7 (Sep 13 README/HJGP lock polish only), thegeneralist01/anki-multidefine 7.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; yesterday KEEP three URLs; same-URL watches (CompreDef, TANREN, Auto-Kanji, ankerspiel, gafu/thai/darya/repetita/origa/monosai, nihongo-sensei, sillon, etc.).

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) RobHelgeson / japanese-stories — AnkiMorphs known-word graded readers; tap-reveal furigana; new-word budget framed in-sentence — PRIMARY
- who: RobHelgeson
- url: https://github.com/RobHelgeson/japanese-stories
- date: created **2026-09-12**; **2026-09-13** linked-reader rebuild + tap-reveal gesture + level-5 story + gist progress sync through ~21:30Z
- live: https://robhelgeson.github.io/japanese-stories/
- tags: education·i-plus-one·reveal-schedule·taste-gate·wiki-craft·quiet-when-nothing·teach-once
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·i-plus-one·reveal-schedule·taste-gate·wiki-craft] score=10 | RobHelgeson / japanese-stories | Short Japanese stories written entirely inside a fixed known-word set derived from a real Anki collection (**AnkiMorphs** lemmas past a **21-day** interval). Declared **new-word budget**; each new word must be introduced in a framing sentence before plain use. Self-contained vertical reader: **tap kanji → furigana**, double-tap → meaning (English one gesture further — anti-gloss-leak); red sesame = leech, teal = approved new. Offline HTML; optional secret-gist progress sync. Authoring craft: AUTHORING.md + corpus.json + Ichiran segmentation + `check.py` validates every token is known or decomposes into known pieces. Distinct from nihongo-tutor (FSRS Telegram i+1), Shiori (ZH-L1 chat tutor), Denchirocio/japanese-stories (handwrite Kotoba) — **AnkiMorphs-ceiling graded readers with reveal-on-demand furigana**. | https://github.com/RobHelgeson/japanese-stories
- why distinct: NEW URL; known-word story craft + gesture reveal schedule not on yesterday’s roster.
- bank: `2026-09-14-robhelgeson-日本語-known-word-stories-ankimorphs-gated` (**deposited** learning lane; body `/workspace/field/bank-bodies/2026-09-14-japanese-stories.txt`)

### 2) alessio-palumbo / japartner — local-first JA spoken tutor; goal+deadline roadmaps; Capture human-gate — STRONG
- who: alessio-palumbo
- url: https://github.com/alessio-palumbo/japartner
- date: created **2026-09-13**; same-day roadmap / mission briefs / guided practice commits through ~20:01Z (public stamp ~23:46Z)
- tags: education·tutor-loop·human-gate·teach-once·quiet-when-nothing·generated-input
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·tutor-loop·human-gate·teach-once·quiet-when-nothing] score=10 | alessio-palumbo / japartner | Local-first personal Japanese tutor (Go/Wails + Ollama + whisper.cpp + VOICEVOX + SQLite). Plans daily practice around a **goal and deadline**; Today assembles a bounded lesson (due reviews, new/weak expressions, conversation targets, captured gaps). **Start** prepares a 5–10 min mission brief once (local fallback); **Today never needs an LLM to open**. **Capture** after real-world speaking gaps: generate editable drafts, **approve only useful ones** (PDF/CSV import also review-gated). Learner-confirmed mission success — not automated proficiency. Distinct from nihongo-tutor (Telegram FSRS+Sudachi), Shiori (browser ZH→JA chat), Hana (always-listen VOICEVOX) — **goal-deadline spoken tutor with gap-capture human-gate**. | https://github.com/alessio-palumbo/japartner
- why distinct: NEW URL; roadmap + Capture approve gate not on yesterday’s KEEP.
- bank: `2026-09-14-alessio-palumbo-japartner-local-first-ja-tutor-goal` (**deposited**; body `/workspace/field/bank-bodies/2026-09-14-japartner.txt`)

### 3) constkolesnyak / gigaku-lang — DE/JA Netflix→Migaku→Anki; i+1 card clarity scoring — STRONG (prefer DE/JA; day-0 ship)
- who: constkolesnyak
- url: https://github.com/constkolesnyak/gigaku-lang
- date: created **2026-09-14** (day-0 public); README documents a mature personal toolkit
- tags: education·i-plus-one·generated-input·teach-once·quiet-when-nothing
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·i-plus-one·generated-input·teach-once] score=9 | constkolesnyak / gigaku-lang | macOS immersion toolkit: unifies known words from **Language Reactor + Migaku IndexedDB + AnkiMorphs**; rips Netflix seasons via Language Reactor in a **background tab (never plays video)** into Migaku SRT; German ASR proofread + RU gloss via one `claude -p` transport. Killer portable gate: **`gigaku clarity` rates i+1 cards by how obvious the unknown word is from the sentence** — Anki add-on studies the clearest card per word. Companion `games-lang` catalogues Steam games by DE/JA language intensity. Distinct from anki_miner / PhiCorvi (audio tooling) — **sentence-clarity selection for i+1 immersion cards**. | https://github.com/constkolesnyak/gigaku-lang
- why distinct: NEW URL; clarity-scored i+1 deck building for DE/JA. (Compiler may swap #3 → ReadLoops if CET-4 ZH→EN i+1 FSRS preferred over day-0 personal toolkit.)
- bank: `2026-09-14-constkolesnyak-gigaku-de-ja-netflix-migaku-anki` (**deposited**; body `/workspace/field/bank-bodies/2026-09-14-gigaku-lang.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### pekoqq / ReadLoops — score 9 (overflow; ZH-L1→EN CET-4 i+1+FSRS)
- url: https://github.com/pekoqq/ReadLoops
- date: created **2026-09-13**; v2.3.0 polish same day through ~23:25Z
- tags: education·i-plus-one·generated-input·reveal-schedule·teach-once
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: AI articles with 95–98% vocab coverage (6–15 new/article); lookup 1→2→3× auto-vocab; reading-driven FSRS. Strong mechanism but **target EN (CET-4)** — left overflow under prefer JA/ZH/KO/FI/DE/IT *as L2*. Promote over gigaku if compiler wants pip-shipped i+1+FSRS over day-0 immersion CLI.

### mlboryczka / french-flashcards — score 8 (overflow; FR)
- url: https://github.com/mlboryczka/french-flashcards
- date: **2026-09-13** tutor audit nineteen fixes + feedback log
- tags: education·tutor-loop·human-gate·teach-once
- one-liner: Notebook→cards + FSRS; tutor chat **proposes** cards, client inserts under RLS (model never writes DB); session queue reserves new/spot-check before due. Solid — FR not prefer-langs → overflow.

### DeanYoon / n1-kanji — score 8 (overflow; KO→JA Scriptable)
- url: https://github.com/DeanYoon/n1-kanji
- date: created 2026-08-30; window = cron N1 word+example accumulation **2026-09-13**
- tags: education·quiet-when-nothing·generated-input·teach-once
- one-liner: Cloud-only OpenRouter generation (Actions); iPhone/Windows **never call LLM** — read Gist slots only. Weak-track half-slots. Prefer KO L1 but window = content cron more than new gate → overflow.

### mShono / finn_cards — score 9 (overflow / **still promote-watch**; idle)
- url: https://github.com/mShono/finn_cards
- date: last mechanism **2026-09-11** — **still idle Sep 12–14**
- one-liner: FST Finnish curriculum unlock. No new window commits → do not promote this hunt.

### Dilnazzzz / bridge — score 9 (overflow; still window-edge Sep 10)
- url: https://github.com/Dilnazzzz/bridge
- one-liner: Socratic cognate EN→FR; still no Sep 13+ push.

### Chuloo / mural — score 7 (overflow; conversation product)
- url: https://github.com/Chuloo/mural
- date: created 2026-09-12; **2026-09-13** DE/IT/PT/ZH modules; ★281
- one-liner: Voice conversation + recall bars; thinner portable gate than #1–#3.

### Malgsx / french-tutor (Miette) — score 7 (overflow; family FR prototype)
- url: https://github.com/Malgsx/french-tutor
- date: created **2026-09-13**; Live voice + avatar same day
- one-liner: Parent-supervised FR voice practice; demo-without-AI; not public service — thinner generalizable gate.

### constkolesnyak / games-lang — score 7 (overflow; catalogue)
- url: https://github.com/constkolesnyak/games-lang
- date: created **2026-09-13**
- one-liner: Steam games scored by DE/JA language intensity. Selection tool adjacent to gigaku — not a learner loop.

### XnoahR / PhiCorvi — score 7 (overflow; Yomitan VOICEVOX bridge)
- url: https://github.com/XnoahR/PhiCorvi
- date: **2026-09-13** v1.6.0 word+sentence audio
- one-liner: Useful immersion audio tooling; not tutor-loop.

### Same-URL / yesterday KEEP watches (do not re-keep)
- cherkasoviy/nihongo-tutor (pushed Sep 13 — yesterday KEEP skip)
- mansourvery-hub/anki-japanese-template (pushed Sep 13 — yesterday KEEP skip)
- suiginko/Shiori — no new mechanism check needed (yesterday KEEP)
- bee-san/bees-ultimate-grammar-dictionary — Sep 13 README/HJGP lock polish; already overflow
- origa / darya / nihongo-sensei / saitenka — same-URL active
- finn_cards / bridge / ittutor / ancci / anki-multidefine — promote-watch idle or already scored

## BOUNCE list (url | why)
- https://github.com/cherkasoviy/nihongo-tutor | yesterday KEEP
- https://github.com/mansourvery-hub/anki-japanese-template | yesterday KEEP
- https://github.com/suiginko/Shiori-ai-japanese-tutor | yesterday KEEP
- https://github.com/mShono/finn_cards | idle Sep 12–14; overflow promote-watch (not bounce — still score 9)
- https://github.com/Dilnazzzz/bridge | still Sep 10; overflow
- https://github.com/bee-san/bees-ultimate-grammar-dictionary | SEEN; README polish only
- https://github.com/AiraDeCastro/learn-french-with-aira | prior evidence conflict; still thin
- https://github.com/liukai97/Japanese_tutor | README 404; still scaffold
- https://github.com/eternalisfine/Hana | local JA VOICEVOX tutor; window = tests clear — thinner than japartner
- https://github.com/meokisama/aozora | EPUB+Yomitan+Anki; window = docs restated
- https://github.com/0xzerolight/anki_miner | SEEN pattern; window polish
- https://github.com/jasperket/clanki | Anki MCP — tooling
- https://github.com/sommepo/anki-remote-reviewer | remote review chrome — tooling
- https://github.com/ferryheath/sm2-fsrs-bridge | converter CLI — tooling
- https://github.com/gedlanni/eimoe-japanese-time | static JLPT N3 self-study pages — content
- https://github.com/jsonpassion/J180 | JLPT vocab content books — content pipeline
- https://github.com/sandraschi/japanophile-mcp | culture/travel workstation — off-lane
- https://github.com/doonch/FlashType | 76-byte README
- https://github.com/suj1e/elysia | scenario app; admin/auth polish — thin L2 gate
- https://github.com/christianmaish337-ui/lingo-levelling | empty/toy HTML
- https://github.com/samyuktaathreya/learning-mandarin | 139-byte README
- https://github.com/aa910113/dojo | README 404
- https://github.com/leoon-hu/jiaci | ZH vocab FSRS site — thinner than ReadLoops
- https://github.com/dickwu/wordbrain | EN vocab graph; dependency chore
- https://github.com/codegeasse1/kotoba-learn | 12-lang Android; product
- https://github.com/amerharb/sawt | audio-first; version bumps
- https://github.com/zitons/LDOCE5pp-EnCn-for-Yomitan | dict packaging
- https://github.com/Blackphi6/yt-furigana-extension | YT furigana chrome
- X MCP | dead — skipped

## FETCH NOTES
- GitHub Search API (UA `FieldBot`): OK across anki / japanese-tutor / language-learning / FSRS / yomitan / CI / furigana-JLPT / SRS + created:>2026-09-12 passes. Saved under `edu0914/search-*.json`. Search remaining recovered to 10 after minute; core ended ~15.
- README path: raw.githubusercontent.com under `edu0914/readmes/` (no Firecrawl). Atoms under `atoms14/` for promote-watch + KEEP candidates.
- Promote-watch atoms: finn_cards last 2026-09-11; bridge 2026-09-10; ittutor 2026-09-11; ancci 2026-09-12; bee-san 2026-09-13 README/HJGP; anki-multidefine 2026-09-12.
- HTML GitHub search: not used. Firecrawl / X MCP: not used.
- Bank deposits: **succeeded** for japanese-stories, japartner, gigaku-lang → `raw/learning/2026-09-14-*` + INDEX rows. Bodies at `/workspace/field/bank-bodies/2026-09-14-*.txt`.
- Truncations / misses: liukai97/Japanese_tutor, aa910113/dojo, tomeu-reader, zavoritniigor-ui/ai-ebook-reader, tanghaotian/socratic-tutor README 404; christianmaish lingo-levelling README 404; FlashType README empty.
- scratch-seen-urls.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) japanese-stories **10**, (2) japartner **10**, (3) gigaku-lang **9**.
- Overflow scored ≥6 not in top-3: ReadLoops **9** (**swap for #3** if EN CET-4 i+1+FSRS preferred), french-flashcards **8**, n1-kanji **8**, mural **7**, french-tutor/Miette **7**, games-lang **7**, PhiCorvi **7**; finn_cards **9** / bridge **9** still idle promote-watch.
- **gigaku vs ReadLoops for #3:** prefer gigaku for DE/JA + i+1 clarity gate; promote ReadLoops over gigaku if compiler distrusts day-0 personal toolkit dumps or wants pip-released i+1+FSRS. Do **not** drop #1 or #2.
- Explicit bounce-deltas on prior keeps: yesterday three KEEP = skip; CompreDef/gafu/thai/darya/monosai/origa = same-URL only; finn_cards still idle.
- Alert-line item: **none**.

## Result for compiler: 3 KEEP
1. https://github.com/RobHelgeson/japanese-stories
2. https://github.com/alessio-palumbo/japartner
3. https://github.com/constkolesnyak/gigaku-lang

No packet file written. field-seen.json not edited.
