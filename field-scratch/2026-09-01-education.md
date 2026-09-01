# Field education hunt · 2026-09-01

Window: ~7 days (2026-08-25 → 2026-09-01). Lane: education / language / tutor / graded-input.
Do not compile the packet from this file. Hunter notes only.

Skip-list: `/workspace/field-seen-urls-60d.txt` (463 URLs). Bank INDEX checked first.
Already in window / already packeted (do not re-keep): KIIP Study (sangkwun, 31 Aug), ReadPlusOne (brandonc7, 30 Aug), SubSmith (Ibrahim Farah, 30 Aug), Jason Corso TIME classroom (31 Aug), Declaude (rryoung98, 31 Aug), Learn Leap (Haruna Oseni, 28 Aug).

## Method / truncations

- WebSearch queries 1–4 as specified.
- HN Algolia via WebFetch (Shell curl of a multi-query loop was Auto-review blocked as an invented sweep; used the user-listed Algolia URLs instead).
- GitHub search `language tutor created:>2026-08-24` (44 hits). Opened the first 15. Rest of the page was same-day “AI Voice Language Tutor” assignment clones (Gemini + TTS). **Truncated there.**
- GitHub search `anki created:>2026-08-24` (395 hits). Opened first 15; most were name-false-positives (`ankit*`) or empty decks. **Truncated after the first page.**
- grokbot.dev RSS: WebFetch 500 this run. Did not re-open the 80+ rail (yesterday’s packet already swept it). Education templates (Tutor / Homework Checker / StoriesBot / Dewey) stay library.
- Bank deposit of Loopback README attempted; Shell Auto-review rejected. Not in bank this run — Field compiler can deposit from the GitHub URL.

---

## KEEP (combined portable+evidence ≥ 6)

### 1. TheLycoi / Loopback — Obsidian capture, human-gate Anki, fail-loop to source
- **domain:** education (wiki/knowledge-craft; Anki; not a language classroom)
- **tags:** human-gate, generated-input, tutor-loop, killed-claim, coverage-ceiling, quiet-when-nothing
- **portable 5 + evidence 4 = 9**
- **who:** TheLycoi (vault owner; design note is first-person “this vault”, “the owner asked to keep”)
- **what:** Obsidian plugin + (separate) Anki add-on. Highlight → local capture with provenance. Drafting is a *separate* command (never on the capture path). Review queue: human approve / edit-then-approve / discard. Approve is the only write to Anki. Failing cards (add-on half) flag the vault page that produced them.
- **URL:** https://github.com/TheLycoi/obsidian-loopback
- **date:** created 2026-08-28, still pushing 2026-08-31 23:17 UTC (06:17 ICT 1 Sep)
- **blurb:** Capture is local disk I/O only — no model, no AnkiConnect, no network — so a keystroke still lands the passage when the model or Anki is down. Drafting never rides capture; a slow LLM cannot add latency to the one-second budget. No card reaches Anki without a human pressing approve on that specific draft (no confidence threshold, no batch auto-approve). Inbox that only fills is treated as a failure: drafts older than 30 days sit in a stale section (visible, not silent expiry), and capture is *refused* once >50 drafts are pending. Duplicate search is collection-wide and blocks the write. Raw PDF captures require a page number; a card with no digest page behind it is marked `noPageBehind` so it cannot pretend it can be reformulated. Killed claims: “AI drafts go straight into Anki”; “capture can wait on the model”; “stale drafts expire themselves.”
- **alert candidate?** Hunter yes (portable human-gate + coverage-ceiling Wedge could paste into an Anki/Obsidian routine). Compiler likely **no** — new plugin, not a Grok Bot / Claude Code / Cursor file or setting he already runs this week. Distinct from Matt Segar’s held-out copy QC (packet 17): Segar is generate-then-QC; Loopback is source-attached capture + never-auto-export + fail-back-to-page.

### 2. kylo1917 / ChatterCheck (repo: lesson-copilot) — live-call copilot for human language tutors
- **domain:** education
- **tags:** human-gate, tutor-loop, persistent-computer, teach-once
- **portable 4 + evidence 3 = 7**
- **who:** kylo1917 (GitHub). Repo description: “standalone copilot for language tutors: flags recurring student mistakes and tracks per-student progression and vocabulary.” Product name on the live page: ChatterCheck.
- **what:** Sits beside a tutor’s call. Records/transcribes locally (“your records stay on this device”). Highlights moments worth a look; the tutor reviews and tags later. Per-student file: progression + glossary. Import / backup / settings.
- **URL:** https://github.com/kylo1917/lesson-copilot · live https://kylo1917.github.io/lesson-copilot/
- **date:** created 2026-08-25, pushed 2026-08-31 13:06 UTC (20:06 ICT 31 Aug)
- **blurb:** The bot does not teach the student. It watches a human tutor’s live session, flags recurring mistakes, and keeps a running glossary per student so the next lesson starts from what already broke. Review-and-tag is the gate: transcription is not auto-feedback to the learner. Local-only storage is the privacy ceiling. Evidence is the shipping page + repo description, not a diary of N students — weaker than UniUI’s 190 FUTO students, stronger than a prompt dump.
- **alert candidate?** No. Wedge is not running live tutor calls this week. Portable gate (human tags the moments; bot does not talk to the student) is worth a packet line, not a file change.

### 3. Chokkarapu Akhil / VedAI Pro — rewrite the system prompt per grade, then quiz what was weak
- **domain:** education
- **tags:** tutor-loop, generated-input, i-plus-one, teach-once
- **portable 4 + evidence 3 = 7**
- **who:** Chokkarapu Akhil (LinkedIn in README)
- **what:** Grade-adaptive tutor. System prompt rewrites itself per grade, board, subject, and language. Class 1–6: analogies + 120-word cap. Class 7–12: headings, tables, exam points. Same question, different answer. Exit quiz of three MCQs from the transcript; weak topics stored and resurfaced next day. TTS English/Hindi/Telugu.
- **URL:** https://github.com/Akhil271-bot/Vedi-AI---Pro-
- **date:** created 2026-08-27, pushed 2026-08-31 10:10 UTC (17:10 ICT 31 Aug)
- **blurb:** Named person audited three gaps (grade-blind replies, text-only, wait-for-silence STT) and kept a prompt rewrite as the harness, not a bigger model. The portable piece is the exit-quiz → next-day resurface loop, plus a hard 120-word cap for young grades (coverage-ceiling on explanation length). Prototype (localStorage, Gemini key in the browser). Not a classroom run. Distinct from UniUI (subject engine verify) and from Learn Leap (tutor from uploaded corpus).
- **alert candidate?** No. Prototype, not a tool Wedge runs. Do not roster.

### 4. yuhouzhou / German noun Anki decks — dual subdecks kill sibling burying
- **domain:** education
- **tags:** teach-once, generated-input, killed-claim
- **portable 3 + evidence 3 = 6** (floor)
- **who:** Yu Hou Zhou (`yuhouzhou`)
- **what:** 4,052 German nouns, A1–C1, 8,104 cards. Two independent subdecks per level (`1. Gender` / `2. Plural`) so Anki’s default sibling-burying cannot hide the second card the same day. Morphological plural highlighting (umlaut + suffix). 2-tier glanceable gender rule (`Suffix -keit → 100% feminine`) or the rule box is hidden for root nouns.
- **URL:** https://github.com/yuhouzhou/german-nouns-anki
- **date:** created 2026-08-31
- **blurb:** Killed claim is “one note, two cards, study both today” under stock Anki — burying makes that a lie, so they split into subdecks. The rule engine is teach-once (pattern, not per-noun prose). Evidence is a built deck + tests, not a log of the author’s reviews. Borderline keep because it is a dataset with a real gate, not a diary. Prefer over generic “Anki dump” because the burying workaround is portable to any language with two faces per lemma.
- **alert candidate?** No. Deck import, not a this-week file/setting. If Wedge already Anki-reviews German, the dual-subdeck trick is a one-line deck convention, still not an alert.

---

## Bounce (in-window, not keep)

| item | why |
|---|---|
| ElewaSTEM / ondinookello96 https://github.com/ondinookello96/elewastem | Hackathon submission (All Things Agentic). L1 African-language STEM tutor is on-lane in spirit, but the README is vendor/compliance marketing (ETHOS/OASIS/TRACK acronyms, 8 DPAs, 53 modules). No named classroom run, no gate they kept after a failure. Library. |
| tomer3333 AI-Learning-Platform https://github.com/tomer3333/AI-Learning-Platform | “Private Arabic language tutor, handwritten assignment analysis.” No README. homework-frontend/backend only. Cap: cannot score without a write-up. |
| ~10 “AI Voice Language Tutor” GitHub clones 2026-08-31 (ShayanBanerjee, bhavana-2417, AddankiBhagavan, Madhu1539, kavyabaswa555, maddalivaishnavi6, CambridgeinstitutetechnologyBLR-Dhanush, …) | Same assignment, 0 stars, no runner, no gate. Truncated after first 15 of 44. |
| Zidi / Lushegs01 | Tutor *matchmaker*, not a tutor they run. |
| varbaia / ZZhouWJ | Product slogan, no practice. |
| Talk-Gyan / aslam-paasa | Empty repo. |
| immersive-mongolian | Empty (size 0). |
| nreusse heisig-hanzi-simplified | Deck dump for German Heisig books. No gate beyond “here are cards.” Dataset. |
| ronald-luo anki-gamepad, Ficello Anki-Image-Editor, mansourvery-hub anki-japanese-template | Tooling or empty. No named study loop. |
| Shashwathkolhar anki-x-qbank | Med-school AnKing unsuspend. Off-lane. |
| jasenzhang1 Mathlingo | “Duolingo/Anki but for math.” No run. |
| hectorcflores my-anki | Kindle highlights SRS. Thin, not language. |
| davidfitzgerald1579-boop Anki-tool | No description. |
| lym11248 Ask HN translation pipeline 2026-08-31 | Structural HTML chunking so LLMs do not silently drop content. Useful, not education/tutor. |
| Kids outlearn AI (MIT TR, 26 Aug) | Essay/paper. Library. |
| Jess Temporal Grok Bot squad 31 Aug https://jtemporal.com/i-built-my-ai-squad-in-grok-bot/ | Off-lane GTM. |
| engineeredai.net / mavgpt.ai / bnwai Substack “turn chatbot into tutor” | How-to prompt libraries. No named run this week. |
| Lesso.me | Vendor. No runner. |
| AnkiMCP ankimcp.ai | Vendor docs. |

---

## Bounce (strong, **out of window** — do not packet; leave for a later stale sweep)

Yesterday already marked Lexiloop / gde Anki Antigravity as out-of-window. Same treatment:

| item | date | why it would have kept |
|---|---|---|
| wordcaster / claude-language-tutor https://github.com/wordcaster/claude-language-tutor | created 2026-05-19, last push 2026-05-20 | Daily Dutch A2 DUO since May 2026. Four-phase session, persistent errors, **five-check chapter gate** before advance, `progress.md` swap. Polyglot skill not validated on a second learner. Strongest out-of-window education item this hunt. |
| ystyleb / cefr-reading-coach https://github.com/ystyleb/cefr-reading-coach | 2026-04-24 | Claude Code skill. Real articles rewritten to 12 CEFR sub-levels (A1.1→C2.2). Next session built around yesterday’s one stumble. i-plus-one + tutor-loop. |
| ayameira / nihongo-dojo | last push 2026-07-13 | Local tutor + Anki collection import so chat uses words already in the deck. |
| hamsamilton / lang-tutor | last push 2026-08-23 (2 days outside) | Claude Code plugin: grammar/idiom while coding. Near-window. |
| remenoscodes / claude-language-coach | 2026-02 | Ambient coaching in Claude Code; Dutch added in a PR. |
| tianshuo / trainingllm | Mar 2026 | Internal intern ITS: never reveal answer until max failures; cheating attempts do not count. |
| SalaevAl Playling / Language Audio Trainer | HN 2026-08-20 | Screen-off phrase trainer. |
| onurcel Excuse My French | HN 2026-08-20 | Rule-based French generator (no LLM in the core). Kept deterministic transforms. |
| Salim_wariz Nattly | HN 2026-08-21 | Meaning → Attempt → Native alternatives → Reuse. Flashcards killed for production. |
| LexSiga Languageme | HN 2026-08-20 | Claude Code dripping. |
| gde Anki Antigravity | already in seen-urls | Skills over system prompts; practice mode **blocks `rate_card`** so cram cannot mutate FSRS. Strong. Out of window. |

---

## Already seen this window (skip)

- https://www.kiipstudy.com / HN 49475164
- https://readplusone.com / HN 49433095
- https://subsmith.app / HN 49476894
- https://segar.me/blog/posts/anki_cards_claude_code.html
- https://learnleap.xyz / HN 49397663
- TIME Corso + PressBee mirror
- https://speak-english.tenken.co / HN 49443296
- https://dev.to/gde/skills-over-system-prompts-building-an-anki-tutor-with-the-antigravity-sdk-2o8f
- https://dev.to/codeyourreality/i-wired-claude-to-my-flashcard-app-via-mcp-heres-what-that-actually-looks-like-46h0
- grokbot.dev tutor / homework-checker / storiesbot / just-in-time-curriculum / learn-math-ml-video-teacher

---

## Alert line (hunter)

**Flag Loopback** as the only copy-this-week candidate: human-gate on Anki export, capture that cannot wait on the model, 50-draft coverage ceiling, fail-back-to-source-page. Compiler should still say **no** unless Wedge is already in an Obsidian+Anki loop this week (Segar QC was hunter-flagged 30 Aug and compiler declined). ChatterCheck / VedAI / German nouns: no.

---

## Footer for compiler

Education this hunt: 4 keep candidates (Loopback, ChatterCheck, VedAI Pro, German-noun dual-subdeck). Empty-streak context from packet 18: 13:0, 14:1, 15:1, 16:0, 17:3, 18:3. If compiler takes ≥1, streak stays broken.

Newest keep: Loopback push 2026-08-31 23:17 UTC (06:17 ICT 1 Sep).

Fetch failures: grokbot.dev RSS 500; Shell HN curl blocked; r.jina not used; tomer3333 and lesson-copilot had no README (lesson-copilot is a single `index.html`).

Truncated: remaining 29 of 44 GitHub language-tutor repos (assignment clones); remaining ~380 GitHub `anki` hits (name collisions).
