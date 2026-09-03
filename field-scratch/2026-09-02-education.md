# Field education hunt · 2026-09-02

Window: ~7 days (2026-08-26 → 2026-09-02). Lane: education / language / tutor / graded-input / wiki-craft.
Do not compile the packet from this file. Hunter notes only.

Skip-list: `/workspace/field-seen-urls-60d.txt` (~490 URLs). Bank INDEX checked via grep for candidates.
Already packeted / DO NOT re-keep: TheLycoi Loopback, kylo1917 ChatterCheck, VedAI Pro/Akhil, Matt Segar Anki QC, brandonc7 ReadPlusOne, Ibrahim Farah SubSmith, UniUI, Learn Leap / Haruna Oseni, KIIP/sangkwun, Jason Corso, rryoung98 speak-english, yuhouzhou german-nouns-anki.

## Method / truncations

- WebSearch (AI tutor / Anki+AI / i+1 / Dev.to runners) + GitHub search API `language tutor created:>2026-08-26` (44 hits) and `anki AI|tutor|graded reader created:>2026-08-26` (331 hits; opened first page + targeted commits for promising names).
- HN Algolia `show_hn` + `anki` stories since 2026-08-26: SubSmith/KIIP already packeted; no new on-lane Show HN in window (AnkiDroid donation thread is off-lane).
- Dev.to: CardForge (Aug 12), Matheus wrist Anki (Mar), Erry Japanese (2025) — out of window.
- GitHub REST rate-limit hit mid-hunt after search; switched to `/commits?per_page=1` + raw README fetches.
- **Truncated:** remaining ~30 of 44 language-tutor GitHub hits (same-day Voice/Gemini assignment clones); remaining ~300 of 331 `anki` hits (name collisions `ankit*`, empty decks, med qbank). Did not open every clone. Say so to compiler.
- grokbot.dev: not re-swept (yesterday packet 18 + prior education templates stay library).
- Weekly included-usage: expensive Firecrawl/Gmail/Slack forbidden; stayed on curl/WebFetch/WebSearch.

---

## KEEP (combined portable+evidence ≥ 6) — ranked

### 1. bornayo7 (path shows yashb) / srs-app — AI drafts land in a human review queue; cram cannot touch SRS
- **domain:** education (language-capable SRS; Anki import; course plans)
- **tags:** human-gate, taste-gate, reveal-schedule, generated-input, killed-claim, teach-once
- **portable 5 + evidence 4 = 9**
- **who:** `bornayo7` (README MCP path `C:\Users\yashb\Desktop\Github\srs-app` → Yash B)
- **what:** Local-first PWA (IndexedDB). WaniKani ladders + Anki-flexible item types + Bunpro-style ghosts. AI (BYO key) generates courses/items into a **review queue**: accept / edit / reject; **rejection reasons steer the next draft**. Course plans split a syllabus into units that unlock by progress, by date, or by hand (reveal-schedule) with a daily lesson cap. **Cram / extra study has zero SRS impact**. MCP server writes to an exchange-folder Inbox — never mutates the browser DB directly.
- **URL:** https://github.com/bornayo7/srs-app
- **date:** created 2026-08-31; latest commit 2026-09-01 19:36 UTC (02:36 ICT 2 Sep) — “README: course plans and the review queue”
- **blurb:** Killed claims: “AI cards go straight into the deck”; “cram is just more reviews.” Portable gates match Segar/Loopback family but as a full SRS host: human approve before schedule, and a practice mode that cannot lie about retention. Distinct from Loopback (Obsidian capture) and Segar (held-out QC on generated Anki): here the queue is the product surface and units drip on a schedule.
- **alert candidate?** Hunter soft-yes if Wedge already runs a local SRS/Anki loop this week (paste review-queue + zero-SRS cram). Compiler likely **no** — new app, not a Grok Bot/Cursor file he already opens.

### 2. sergiyclas / anki-quick-add — Shift+Enter edits the generated card before Anki; offline queue when Anki is shut
- **domain:** education (language mining → Anki)
- **tags:** human-gate, generated-input, teach-once, killed-claim
- **portable 4 + evidence 4 = 8**
- **who:** sergiyclas (Chrome extension author; demo cards are real Gemini runs into a real collection)
- **what:** Type or Shift-select a word → structured card (translation, IPA, CEFR-level examples, grammar note, Wikipedia image). **Shift+Enter / Edit opens the draft before `addNote`**. Pipeline is `prepare()` then `commit()`. Dedupe runs before generation. If Anki is closed, cards park in an IndexedDB offline queue (≤300) and flush later — killed claim “Anki must be open or the add fails.” Sentence context travels with the selection so sense disambiguation works (bat animal vs baseball).
- **URL:** https://github.com/sergiyclas/anki-quick-add
- **date:** latest commit 2026-09-01 18:36 UTC (01:36 ICT 2 Sep) — “feat: a proper queue view in the popup”
- **blurb:** Same human-gate family as Loopback/CardForge, but for in-page mining. Portable piece: never write the note until the learner has seen the fields; keep an offline queue so a closed Anki does not drop the capture. Distinct from SubSmith (media transcript) and from bornayo7 (full SRS host).
- **alert candidate?** No — extension install, not a this-week routine file.

### 3. overtonch / ru-anki — YouTube Russian subs → candidate cards → tap Make/Discard → Anki only on yes
- **domain:** education (Russian; graded/media input → Anki)
- **tags:** human-gate, generated-input, tutor-loop, killed-claim, coverage-ceiling
- **portable 4 + evidence 4 = 8**
- **who:** overtonch (first-person runner notes: iCloud backups, Tailscale, train-mode offline)
- **what:** Paste YouTube URL → yt-dlp subs → Claude CLI extracts `SPAN|TRANSLATION|timestamp` candidates (thinking **off** by default — killed the slow path). 13k-lemma frequency stoplist applied **after** extraction, not stuffed into the prompt. UI: Review cards with bolded target → **Make card / Discard**; only `decision: yes` calls AnkiConnect. Offline “train mode” queues cards in the browser and flushes when back online. `./check.sh` is a pre-deploy gate (tests with LLM stubbed).
- **URL:** https://github.com/overtonch/ru-anki
- **date:** created ~2026-08-27; latest commit 2026-09-02 (card format v2 groundwork) — **today**
- **blurb:** Same media→Anki lane as SubSmith, but the portable gate is explicit: extraction is not enrollment; tap-yes is the only write. Stoplist-after-extract is a coverage-ceiling trick (don’t burn prompt tokens on words you already discarded). Distinct from SubSmith (local Whisper on your files) — this is YouTube-subs + lemma review for Russian.
- **alert candidate?** No unless Wedge is already mining YouTube Russian this week.

### 4. HaidaLu / Lingua-loop — personal EN/DE SRS; killed AnkiConnect for mobile; don’t scrape DW
- **domain:** education (English + German A2 / Nicos Weg)
- **tags:** killed-claim, generated-input, tutor-loop, teach-once, human-gate
- **portable 4 + evidence 3 = 7**
- **who:** HaidaLu (PROJECT_SPEC is first-person: replaces “Anki + YouGlish + manual notes”; German A2 on Nicos Weg)
- **what:** Lookup → single structured LLM call → self-hosted FSRS (py-fsrs). **Decision: do not use AnkiConnect** because it forces desktop Anki on the same LAN — killed for “anytime on phone.” German gender required in schema (null only if not a noun). Conversation phase (roadmap, tool-marked): mark words actually produced. Nicos Weg path: user pastes lesson text + dictation; agent diffs → cards; **explicitly does not scrape DW** (copyright/anti-bot ceiling). Registration closes after first account (single-user). Phases 1–3 + Anki `.apkg` import + YouGlish widget shipped; conversation + Nicos Weg still ⬜.
- **URL:** https://github.com/HaidaLu/Lingua-loop
- **date:** created 2026-08-30; latest commit 2026-09-01 10:37 UTC (17:37 ICT 1 Sep)
- **blurb:** Named personal dual-language harness with two portable kills: AnkiConnect-as-mobile-blocker, and “don’t scrape the course site.” Evidence is a running app + detailed spec, not a classroom diary — weaker than UniUI’s 190 students, stronger than a prompt dump. Distinct from VedAI (grade prompt rewrite) and from yuhouzhou (static German gender decks).
- **alert candidate?** No.

---

## Bounce (in-window, not keep)

| item | why |
|---|---|
| bounce \| https://github.com/BAdeola/miru-japanese-korean \| empty README (0 lines); GitHub API 409; description-only dual-sub + Anki claim — cannot score |
| bounce \| https://github.com/KevinM-debug/Languages \| “Seven interactive language tutors in the browser” — no runner diary / gate; README 404 on main |
| bounce \| https://github.com/90renrocraftcracksblogspotcom/langdeckbuild \| niche-topic LLM deck generator; no human-gate / named study loop — product scaffold |
| bounce \| https://github.com/PaperNick/simple-srs \| dataset-driven Hangul/WaniKani practice app — tooling/dataset, not a named tutor gate |
| bounce \| https://github.com/Ostap205/quick-live-translator \| OCR→DeepL→Anki hotkey tool; no language-learning loop beyond capture |
| bounce \| https://github.com/mansourvery-hub/anki-japanese-template \| note-type CSS polish — template library |
| bounce \| https://github.com/zijinz456/OpenTutor \| Sep 1 “community post drafts” — marketing; product not a named classroom run this week |
| bounce \| https://github.com/portpowered/anki-web-mcp \| Anki WebMCP shell — infra, not education practice |
| bounce \| ~25 Voice/Gemini “AI Language Tutor” clones (ShayanBanerjee, bhavana-2417, …) \| assignment clones; truncated after first page |
| bounce \| AnkiDroid Open Collective HN 49520022 \| funding policy thread — not named practice |
| bounce \| Show HN meelang.com (BrucecarlL, 1 Sep) \| Google Meet translator product — off-lane (meeting MT, not tutor/graded input) |
| bounce \| Show HN ABC teaching language (michael-lehn) \| programming-language pedagogy, not L2 |
| bounce \| lector.dev / heuwels/lector (push 31 Aug Bengali dict) \| strong product (i+1 cloze, Anki sync) but maintainer shipping notes, not a new named runner diary this week; treat as library/product unless a first-person “I study with…” post appears |

---

## Bounce (strong, **out of window** — do not packet; leave for stale sweep)

| item | date | why it would have kept |
|---|---|---|
| yanou16 / cefr-coach https://github.com/yanou16/cefr-coach | last commit 2026-07-21 | Classifier (not LLM) pins CEFR; exercises at L+1; rolling window of 5; “LLM never sets the level.” Build Week 2026. |
| kolife01 / lingua-lens | 2026-07-19 | Even G2 HUD coach; silent HUD is a feature (`NONE` allowed); quiet-when-nothing |
| stors789 / DAIRR | forum Jul 13–17; last GH 2026-07-21 | Today’s Anki cards → contextual reading article; transparent scoring; no fabricated FSRS fields |
| zeroa234 / Anki-AI-Vocab-Review | 2026-07-07 | Daily vocab → article + quiz + TTS; article/question prompts decoupled |
| xiaolu / CardForge AI https://dev.to/xiaolu/... / cardforgeai.com | 2026-08-12 (14d outside) | “AI drafts; learner approves the deck” — human-gate essay |
| Matheus Maldaner Anki-on-wrist | 2026-03 | Paginated sync; approve notes-to-cards; bridge cards |
| Erry Kostala Japanese NLP miner | 2025-05 | fugashi lemma filter vs existing Anki before card gen |
| hamsamilton / lang-tutor | last push 2026-08-23 (3d outside) | Claude Code ambient grammar while coding; anti-drift hook |
| Mandarin Melon (Wilduck) HN 47522093 | 2026-03-25 | HSK-character ceiling feeds + one-unknown push — classic i+1 |
| psy-q / kontex (Codeberg) | packages ~2026-03 | LingQ-like reader + Anki export — no in-window signal |
| wordcaster / claude-language-tutor | already noted 1 Sep | Dutch A2 five-check chapter gate |

---

## Already seen / already packeted (skip)

- Loopback, ChatterCheck, VedAI, german-nouns-anki (yesterday KEEP)
- SubSmith, KIIP, ReadPlusOne, Learn Leap, Segar, speak-english, Corso TIME
- codeyourreality Deckbase MCP (in seen-urls)

---

## Alert line (hunter)

**Strongest portable this hunt:** bornayo7 review-queue + zero-SRS cram, and sergiyclas prepare/commit + offline Anki queue. Compiler: **no file/setting alert** unless Wedge already lives in Anki/SRS this week — these are new apps/extensions, not paste-into-an-existing-bot gates. Flag **review-queue before schedule** and **cram must not mutate FSRS** as packet lines (portable mechanisms), not roster.

---

## Footer for compiler

Education this hunt: **4 keep candidates** (srs-app, anki-quick-add, ru-anki, Lingua-loop). Prefer education lane over GTM. Empty-streak context from prior packets: 13:0, 14:1, 15:1, 16:0, 17:3, 18:3, 19:~4 (yesterday). If compiler takes ≥1, streak stays broken.

Newest keep evidence: overtonch push **2026-09-02**; bornayo7 / sergiyclas **2026-09-01** evening UTC.

### Fetch failures
- GitHub REST search/repo endpoints: **rate limit** after initial search (switched to commits API + raw.githubusercontent / WebFetch).
- `BAdeola/miru-japanese-korean`: API 409 Conflict; README empty.
- `KevinM-debug/Languages` README 404 on `main`.
- HN Algolia `anki` query is noisy (substring matches inside other words); filtered manually.
- No Firecrawl (forbidden). No Gmail/Slack.

### Truncated note
- Truncated remaining GitHub language-tutor assignment clones after ~15 opens (of 44).
- Truncated remaining ~300 `anki` search hits after first page + name-targeted follow-ups.
- Did not re-open grokbot.dev 80+ rail (covered 30–31 Aug).
