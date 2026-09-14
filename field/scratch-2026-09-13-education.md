# Field education hunt — 2026-09-13 scratch (Sunday)
Window: ~2026-09-12 00:00 UTC → now (prefer pushes 2026-09-12 / 2026-09-13). Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Cap: **at most 3 education SETUPS**. Scratch only — field-seen.json / latest.md / field-packet-* untouched.

Yesterday KEEP (SKIP re-keep unless NEW distinct mechanism on a **different URL**): Traderhs/TANREN 9, candemircan/ankerspiel 9, NikhilDhanda/Auto-Kanji-Breakdown 8. Overflow Sep 12: mShono/finn_cards 9 (promote-watch), mansourvery-hub/CompreDef ladder-free same-URL, gafu/thai/darya/repetita/origa/monosai same-URL watches.

Skip: URLs in `/workspace/field/scratch-seen-urls.txt`; yesterday KEEP three URLs; prefer NEW repos/URLs over same-URL watch bumps. Prior recent: gafu-v2, obsidian_chinese_comprehensible_input, By-ear, kikubridge, jp-sentences-to-anki, nihongo-sensei, sillon, monosai, anki-quick-add, kotoba-local, englishpod_to_anki, linguashelf, etc.

## KEEP candidates (ranked) — recommend TOP 3 for packet

### 1) cherkasoviy / nihongo-tutor — FSRS JA Telegram tutor; i+1 Sudachi gate; intra-session spacing excluded from FSRS; no romaji — PRIMARY
- who: cherkasoviy
- url: https://github.com/cherkasoviy/nihongo-tutor
- date: created **2026-09-05**; **2026-09-12** content-seed + AI-route plan + deploy runbook + proxy-headers fix through ~20:44Z (Phase 1 kana bootcamp + FSRS live)
- tags: education·i-plus-one·tutor-loop·teach-once·generated-input·quiet-when-nothing·human-gate
- portable / evidence / combined: **5 / 5 / 10**
- alert: **no**
- one-line packet shape: [education·i-plus-one·tutor-loop·teach-once·generated-input] score=10 | cherkasoviy / nihongo-tutor | Named Japanese tutor (Telegram bot + Mini App) built on SLA research: **FSRS** scheduling, **retrieval-only after first exposure**, **i+1 sentence selection** via Sudachi lemmas (known set + exactly one new), **production / recognition / listening** as separate cards, **recasts** not red-pen lectures. Kana bootcamp gates the rest; **no romaji rendered anywhere** (RU UI; Polivanov internal only). Killer portable gate: **within-session expanding spacing** (intro → immediate check → cloze ≥5 steps later → wrap-up) with **only wrap-up written to FSRS** — massed intra-session touches logged `intra_session=True` and excluded from the optimizer. Seeded RNG session replay; backlog gate zeroes new items; self-claimed kana is *seeded not skipped* (scheduler verifies). Distinct from TANREN (KO→JA answer-is-grade + VOICEVOX), ankerspiel (Card≠sentence rotation), Auto-Kanji (in-card trees), finn_cards (FST Finnish) — **JA FSRS tutor with i+1 morphology gate + FSRS-honest intra-session spacing**. | https://github.com/cherkasoviy/nihongo-tutor
- why distinct: NEW URL; FSRS-honest intra-session spacing + Sudachi i+1 + no-romaji kana gate not on yesterday’s roster.
- bank: `2026-09-13-cherkasoviy-nihongo-tutor-fsrs-i-1-telegram` (**deposited** learning lane; body `/workspace/field/bank-bodies/2026-09-13-nihongo-tutor.txt`)

### 2) mansourvery-hub / anki-japanese-template — Mature Word Mode (ivl≥365 → word-only front) + pure-retrieval front — STRONG (JA Anki)
- who: mansourvery-hub
- url: https://github.com/mansourvery-hub/anki-japanese-template
- date: created **2026-09-01**; **2026-09-11** pure-retrieval front / quiet hierarchical back; **2026-09-12** editorial calm redesign (~21:02Z)
- tags: education·reveal-schedule·teach-once·quiet-when-nothing·taste-gate
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-line packet shape: [education·reveal-schedule·teach-once·quiet-when-nothing] score=9 | mansourvery-hub / anki-japanese-template | Ergonomic JA sentence-mining note type: front is **pure retrieval** (sentence/expression only — no badges, dashboards, grading chrome). Back is a quiet reading hierarchy (target → reading → compacted Yomitan meaning → context; secondary under `More ▾`). **Mature Word Mode**: when review interval ≥ 365 days (live AnkiConnect / AnkiDroid JS read), front collapses to **Expression only** so old cards stop testing the word and start testing sentence recognition — anti-overlearning. Listening forced only by `#listening` tag or audio-only field shape; empty fields collapse; zero-reflow furigana. Distinct from CompreDef (definition density ladder — same author, **different URL/mechanism**), Auto-Kanji (component trees), TANREN (active trainer) — **in-Anki reveal/maturity schedule owned by the card template**. | https://github.com/mansourvery-hub/anki-japanese-template
- why distinct: NEW URL (not CompreDef); Mature Word Mode + pure-retrieval front not shipped yesterday.
- bank: `2026-09-13-mansourvery-hub-anki-japanese-template-mature-word-mode` (**deposited**; body `/workspace/field/bank-bodies/2026-09-13-anki-japanese-template.txt`)

### 3) suiginko / Shiori-ai-japanese-tutor — ZH-L1 adaptive JA AI tutor; ruby+pitch; deinflect; bilingual fade N0→N1 — STRONG (day-0 but lane-exact)
- who: suiginko
- url: https://github.com/suiginko/Shiori-ai-japanese-tutor
- date: created **2026-09-12**; same-day v0.1.1 + Android + enriched README through ~14:06Z
- tags: education·tutor-loop·i-plus-one·teach-once·wiki-craft
- portable / evidence / combined: **4 / 4 / 8**
- alert: **no**
- one-line packet shape: [education·tutor-loop·i-plus-one·teach-once] score=8 | suiginko / Shiori-ai-japanese-tutor | Local-first **AI Japanese private tutor for Chinese L1**: full-sentence **ruby furigana** + pitch-accent polyline; built-in **deinflector** (活用 → 辞书形); JLPT ladder **N0(五十音)→N1** with **dynamic bilingual ratio** (ZH scaffolding fades into JA-only as level rises); vocab/grammar states 初学→温习→熟练 + flashcard self-test. API keys + chat stay in browser local storage. Day-0 public ship but mechanism is complete and lane-exact (ZH→JA tutor-loop). Distinct from nihongo-sensei (Anki→ChatGPT voice), sillon (voice propose+override), monosai (Anki-ceiling stories), nihongo-tutor (#1 FSRS Telegram) — **ZH-L1 adaptive chat tutor with morphological deinflection + bilingual fade**. | https://github.com/suiginko/Shiori-ai-japanese-tutor
- why distinct: NEW URL; ZH→JA adaptive bilingual-fade + deinflect not on roster. (Compiler may swap #3 for finn_cards if FST/curriculum gate preferred over day-0 AI tutor.)
- bank: `2026-09-13-suiginko-shiori-zh-l1-adaptive-ai-japanese` (**deposited**; body `/workspace/field/bank-bodies/2026-09-13-shiori.txt`)

## Scored but NOT in top-3 SETUP slots (overflow)

### mShono / finn_cards (Kielikaveri) — score 9 (overflow / **promote-watch**; under-served L2)
- url: https://github.com/mShono/finn_cards
- date: last mechanism push **2026-09-11** (Unlock forms only on Good/Easy; curriculum never closes forms) — **idle in Sep 12–13 window**
- tags: education·i-plus-one·taste-gate·teach-once·tutor-loop
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Morphology-gated Finnish — FST-verified inflection + curriculum unlock on earned grades. Still stronger portable gate than day-0 Shiori on raw mechanism; left overflow under cap-3 **JA preference** + no new window commits. **Compiler should promote #3 → finn_cards** if FI/FST diversity preferred over another JA tutor.
- bank: already deposited 2026-09-12

### Dilnazzzz / bridge — score 9 (overflow; window edge Sep 10)
- url: https://github.com/Dilnazzzz/bridge
- date: created **2026-09-10**; last push **2026-09-10** (cognate network, hands-free voice, MCP, eval harness) — just outside Sep 12–13 push window; mechanism new to Field
- tags: education·tutor-loop·teach-once·i-plus-one·human-gate·generated-input
- portable / evidence / combined: **5 / 4 / 9**
- alert: **no**
- one-liner: Socratic cognate tutor (EN→FR first): code owns curriculum/memory/scheduling; model owns only conversation; **never gives the answer**; syllabus graph unlock; story mode ~95% from owned words; pronunciation scored by sound not spelling. Strong portable gates — overflow for window-edge + EN/FR not prefer JA/ZH/KO/FI/DE.

### leibnitz27 / ittutor (Interrogami) — score 8 (overflow; IT blank-recall)
- url: https://github.com/leibnitz27/ittutor
- date: created **2026-09-03**; **2026-09-11** authoritative grammar lookup + kinship possessive fix (idle Sep 12–13)
- tags: education·tutor-loop·teach-once·taste-gate
- one-liner: Blank-input Italian drills (no word banks); per-token feedback; **mutation system** varies one dimension after correct; retry queue. Solid teach-once — IT not prefer-langs; window idle → overflow.

### gillisandrew / ancci — score 7 (overflow; authoring tool)
- url: https://github.com/gillisandrew/ancci
- date: **2026-09-12** v0.5.0 — purge non-authoring; deck-defined card types
- one-liner: YAML→AnkiConnect authoring with human review/sync skills. Wiki-craft adjacent; not a learner gate — overflow.

### bee-san / bees-ultimate-grammar-dictionary — score 7 (overflow; JA wiki-craft)
- url: https://github.com/bee-san/bees-ultimate-grammar-dictionary
- date: **2026-09-12** HJGP + nihongokyoshi re-scrape + Bunpro V2
- one-liner: 12-source unified Yomitan grammar dict with progressive disclosure. Reference merge more than tutor-loop — overflow.

### thegeneralist01 / anki-multidefine — score 7 (overflow; DE/RU/FR enricher)
- url: https://github.com/thegeneralist01/anki-multidefine
- date: created **2026-09-12**; AnkiWeb **755799523**
- one-liner: Monolingual DWDS/Larousse/etc. define + cloze examples + audio. Safe enricher; thinner learner gate than Mature Word Mode.

### matheusmendes720 / mandarin-tutor (Lingua) — score 6 (overflow)
- url: https://github.com/matheusmendes720/mandarin-tutor
- date: **2026-09-12** voice-loop polish; README thin (platform = pronunciation + FSRS + voice agent)
- one-liner: Voice-first Mandarin stack exists but README/docs are platform overview; less named L2 gate than #1–#3.

### MuggleWu / miki — score 6 (overflow; Anki-alt)
- url: https://github.com/MuggleWu/miki
- date: **2026-09-12** Android keyboard/safe-area; FSRS-6 event-sourced
- one-liner: Solid Anki alternative; **no language-specific gate** — bounce as education SETUP.

### M-elkadeem / anki-vocab-ai — score 6 (overflow; DE batch gen)
- url: https://github.com/M-elkadeem/anki-vocab-ai
- date: created **2026-09-12**; gTTS audio same day
- one-liner: German vocab→Anki batch + dedupe + gTTS. Useful CLI; day-0 tooling.

### enderzhangpro / Automatic-Anki-Card-Maker — score 6 (overflow)
- url: https://github.com/enderzhangpro/Automatic-Anki-Card-Maker
- date: **2026-09-12** default defs from CC-CEDICT
- one-liner: Local-LLM ZH word→Anki; thin README; generation pipeline.

### Same-URL watches (do not re-keep)
- mansourvery-hub/CompreDef, garthtrickett/gafu-v2, cehbz/thai-language-anki, ferranrego/darya, mikub97/repetita, yurvon-screamo/origa, tobiaslrn/monosai — active or idle; **same URL → overflow only**
- Traderhs/TANREN, candemircan/ankerspiel, NikhilDhanda/Auto-Kanji-Breakdown — **yesterday KEEP; skip**

## BOUNCE list (url | why)
- https://github.com/Traderhs/TANREN | yesterday KEEP
- https://github.com/candemircan/ankerspiel | yesterday KEEP
- https://github.com/NikhilDhanda/Auto-Kanji-Breakdown | yesterday KEEP
- https://github.com/mansourvery-hub/CompreDef | same-URL (ladder-free already overflow Sep 12)
- https://github.com/garthtrickett/gafu-v2 | same-URL
- https://github.com/mShono/finn_cards | idle Sep 12–13; overflow promote-watch (not bounce — still score 9)
- https://github.com/tobiaslrn/monosai | same-URL UI
- https://github.com/serjflint/saitenka | SEEN; mpv immersion workstation polish
- https://github.com/DsDG1/turna | SEEN
- https://github.com/extra-large-onions/obsidian-language-learning | SEEN
- https://github.com/karpinski1994/chinese-anki | personal Hanzi Movie mnemonic deck (1 card documented) — content not portable gate
- https://github.com/caocaochan/hydcd-yomitan | ZH dictionary packaging / Light edition — tooling
- https://github.com/chachaprince1/anime-episode-to-anki | class-site→Yomitan→Anki extension; setup chrome
- https://github.com/AiraDeCastro/learn-french-with-aira | README still claims “no app code”; commits show reader — evidence conflict / early
- https://github.com/cheezy/reachy-language-tutor | robot + FSI Italian lessons — hardware demo off-lane
- https://github.com/0xzerolight/anki_miner | mature JA/ZH/KO miner; window = macOS wheel floor — polish
- https://github.com/JoshiMinh/Hakkutsu | immersion extension; last meaningful Sep 9
- https://github.com/mcgrizzz/Yomine | mining accuracy/Anki settings — product polish
- https://github.com/bee-san/hachidori | JA dict keybinds — product polish
- https://github.com/oboroge0/hayamimi | CPU ASR/subtitles — tool not tutor-loop
- https://github.com/abdullahbutt/wordfeather | Goethe study notes site — content dump
- https://github.com/anberw612-stack/language-tutor | Agent Skill ZH→EN/JA pedagogy; thin Sep 8 ship — overflow-thin
- https://github.com/samuelabc/japanese-tutorial | static Astro lessons for ZH L1 — content site
- https://github.com/rixcian/lexo | self-hosted FSRS Anki-alt — no L2 gate
- https://github.com/AndreaBonn/impara-italiano | IT course continuing; thinner new gate
- https://github.com/f-rehmandev/AI-Powered-Anki | EN→target Anki gen webapp
- https://github.com/liukai97/Japanese_tutor | scaffold stage 0 only
- https://github.com/johntsui-gif/chinese-tutor | no README; PWA reader chrome
- X MCP | dead — skipped

## FETCH NOTES
- GitHub Search API (UA `FieldBot`): early OK — saved under `edu0913/search-*.json` + `s-*.json` / `s2-*.json`. Search limit 10/min; **core remaining hit 0** mid-hunt (~60/hr) → switched to **raw.githubusercontent.com README** + `commits/*.atom` under `atoms13/` (no API). Search recovered after minute reset for tutor-lang / created-anki passes.
- X-RateLimit (search): started remaining 9→0 then reset; core exhausted until ~reset timestamp — README/atom path carried the hunt.
- HTML GitHub search: 429 once; not relied on.
- Firecrawl / X MCP: not used (disallowed / dead).
- Bank deposits: **succeeded** for nihongo-tutor, anki-japanese-template, Shiori → `raw/learning/2026-09-13-*` + INDEX rows. Bodies also at `/workspace/field/bank-bodies/2026-09-13-*.txt`.
- Truncations / misses: GioPalusa/itaLearn README 404; LeftBrain-RightNode README 404; some day-0 tutors README-less; `created:>2026-09-08` OR query returned empty once (quota/parse).
- scratch-seen-urls.txt appended with evaluated NEW URLs this hunt. **field-seen.json untouched.**

## Scoreboard for packet compiler
- education KEEP setups recommended this hunt: **3** — (1) nihongo-tutor **10**, (2) anki-japanese-template **9**, (3) Shiori **8**.
- Overflow scored ≥6 not in top-3: finn_cards **9** (**promote-watch / swap for #3**), bridge **9** (window-edge), ittutor **8**, ancci **7**, bees-grammar-dict **7**, anki-multidefine **7**, mandarin-tutor/Lingua **6**, miki **6**, anki-vocab-ai **6**, Automatic-Anki-Card-Maker **6**.
- **finn_cards vs #3:** prefer Shiori for JA/ZH lane + NEW window URL; promote finn_cards over Shiori if compiler wants FI/FST diversity or distrusts day-0 AI tutors. Do **not** drop #1 or #2 for finn_cards.
- Explicit bounce-deltas on prior keeps: TANREN/ankerspiel/Auto-Kanji = yesterday KEEP skip; CompreDef/gafu/thai/darya/monosai = same-URL only; By-ear/kikubridge/jp-sentences/nihongo-sensei/sillon idle.
- Alert-line item: **none**.

## Result for compiler: 3 KEEP
1. https://github.com/cherkasoviy/nihongo-tutor
2. https://github.com/mansourvery-hub/anki-japanese-template
3. https://github.com/suiginko/Shiori-ai-japanese-tutor

No packet file written. field-seen.json not edited.
