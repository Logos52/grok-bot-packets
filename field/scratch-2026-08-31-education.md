# Field education hunt — packet 18 scratch (2026-08-31)
Window: ~2026-08-24 → 2026-08-31. Lane: language / tutors / graded+generated input / wiki-craft. Combined ≥6 to keep. Alert = would Wedge copy a mechanism into a file/setting/routine THIS WEEK.

## Candidates

### 1) sangkwun — KIIP Study (KEEP)
- who: sangkwun (HN); product KIIP Study
- url: https://www.kiipstudy.com · https://news.ycombinator.com/item?id=49475164
- date: 2026-08-28
- tags: education, tutor-loop, generated-input, coverage-ceiling, teach-once
- portable/evidence/combined: 4 / 4 / 8
- practice: Named maker built exam practice for Korea’s Social Integration Program (KIIP): placement → intermediate → comprehensive formats, vocab from official KIIP textbooks, not TOPIK-generic Korean. Core gate: every wrong/right answer ships an explanation in the learner’s L1 (16 languages) so the Korean stem is not the bottleneck to understanding *why*. Vocab path uses “invisible” SRS (wrong cards resurface more; no deck management UI). Product explicitly aims at the 60% pass line, not perfection — a coverage-ceiling that matches immigration milestones. Offline after one content download; no account/ads. First-party site + maker HN comment both opened.
- alert-line: **yes** — copy “L1 explain-on-grade + pass-threshold not 100%” into a language tutor skill/routine this week (especially for Wedge’s Vietnam/Taiwan/Philippines multilingual context).

### 2) rryoung98 — Declaude / speak-english.tenken.co (KEEP, portable gate)
- who: rryoung98 (HN); Tenken; based on gvzdv/claudish-to-english
- url: https://speak-english.tenken.co/ · https://news.ycombinator.com/item?id=49443296
- date: 2026-08-26
- tags: education, taste-gate, killed-claim, teach-once, human-gate
- portable/evidence/combined: 4 / 4 / 8
- practice: Team writing a quantum-chemistry *course* burned tokens fighting Claude-speak despite skills, system prompts, and subagents — tics returned (whack-a-mole). Solution: separate post-process rewriter (Qwen2.5-14B on their GPUs) that strips assistant-voice while keeping meaning/code/structure; Claude Code plugin hook, MCP, and document drop. Skills alone = killed-claim for style control; harness-level taste gate after generation. Education-adjacent (course materials), not a language classroom, but the portable mechanism is the point.
- alert-line: **yes** — add a “plain-English / no-assistant-voice” post-filter (or Grok Bot skill) for any generated graded-input / tutor copy when prompt rules drift.

### 3) Jason Corso — flipped classroom + mastery-first AI tutor rules (KEEP)
- who: Jason Corso (Toyota Professor of AI, U. Michigan; Voxel51 co-founder)
- url: https://time.com/article/2026/08/26/why-i-stopped-fighting-ai-in-my-classroom-and-started-teaching-with-it/ (first-party blocked; full practice text recovered via https://eng.pressbee.net/show4848324.html mirror + WebSearch highlights)
- date: 2026-08-26
- tags: education, human-gate, tutor-loop, teach-once, reveal-schedule
- portable/evidence/combined: 4 / 4 / 8
- practice: Named professor *runs* the setup: weekly 2h recorded lecture + article in Perusall graded on engagement (viewing, comments, peer answers; paste-spam flagged). Live time is 1h lecture + industry guests + breakouts + in-person quiz where students grade themselves and get credit only if someone argues the logic. Fall plan: cold-call debate of papers. AI rules he gives students: Mastery-First (solve manually, then AI-check divergence); AI as Problem-Generator (new practice items); Brain Dump Standard (never blank-page AI write — dump ideas, AI organize, human refine/rewrite). Frame: AI is expertise amplifier, not labor-saving for novices.
- alert-line: **yes** — copy Mastery-First + Brain-Dump-before-AI + “credit only if you argue the logic” into tutor/classroom gates this week (pairs with Segar-style QC thinking).

## Bounce one-liners
- bounce | https://www.iatrox.com/blog/chatgpt-is-not-an-ai-tutor-educational-guardrails | 2026-08-29 product hub / argument-essay (attempt-first prompt is portable but no named runner of a classroom/tutor; PNAS citation essay)
- bounce | https://dev.to/mathias_ihwe_c3b880689587/why-most-python-courses-fail-and-how-i-built-one-that-works-spent-months-learning-python-but-4faj | thin curriculum pitch, not a runnable tutor/language setup with evidence
- bounce | https://abelchen.dev/projects/lexiloop-app | strong i+1/CEFR reader practice but dated 2026-04-04 (outside 7-day window)
- bounce | https://dev.to/gde/skills-over-system-prompts-building-an-anki-tutor-with-the-antigravity-sdk-2o8f | excellent practice-mode deny(rate_card) Anki tutor, but published 2026-06-19 (out of window)
- bounce | https://dev.to/codeyourreality/i-wired-claude-to-my-flashcard-app-via-mcp-heres-what-that-actually-looks-like-46h0 | 2026-04-25 out of window
- bounce | https://dev.to/harshini_hegde_1ab5ee3606/mentori-turning-documents-into-interactive-ai-tutors-with-gemini-live-26nl | hackathon architecture walkthrough, 2026-03 out of window
- bounce | https://dev.to/hammer_nexon_0e3907d1ade2/how-to-create-a-custom-ai-tutor-from-any-youtube-channel-3ahd | generic tutorial / library, 2026-02 out of window
- bounce | https://blog.aieducator.tools/posts/best-ai-tutors-for-students-2026 | ranking list (already seen Dan Fitzpatrick)
- bounce | https://www.forasoft.com/blog/article/ai-tutors-adaptive-learning-2026 | vendor build playbook (already seen)
- bounce | https://coursiv.io/blog/grok-for-students-2026 | library / already seen
- bounce | https://studycardsai.com/blog/best-flashcard-app-for-language-learning | ranking guide library
- bounce | https://www.edutopia.org/article/ai-tutors-work-guardrails/ | how-to essay / library, not named runner practice in window
- bounce | https://dev.to/jawagar_raj_e41371bc8599f/french-language-institute-in-vellore-structured-french-learning-for-beginners-students-and-3dla | institute marketing / library
- bounce | greelitbooks / grokbot.dev CoS use cases | off-lane GTM; portable human-gate already known; do not lead
- bounce | already-kept this week (skip reopen): Segar Anki QC, brandonc7 ReadPlusOne, Ibrahim SubSmith, Haruna Learn Leap, UniUI, Telnyx Harpreet, Darwesh kids, Ryan Ahamer, Machinezoo, Pocket Linguist, et al. per skip list

## Fetch failures
- TIME first-party https://time.com/article/2026/08/26/why-i-stopped-fighting-ai-in-my-classroom-and-started-teaching-with-it/ — curl returned empty; WebFetch/jina blocked or empty; Internet Archive temporarily offline. Recovered full practice text via PressBee Middle East mirror + WebSearch highlights; bank deposited the mirror, not TIME.
- https://r.jina.ai/ for several URLs returned 401 AuthenticationRequiredError (bad IP reputation).
- X connector DOWN (MCP user-X failed_to_load) — skipped pin timelines as instructed.
- DEV.to search/feed_content API returned 0 results for education queries; used `/api/articles?tag=…&top=7` instead.
- HN Algolia `Anki` query is noisy (substring matches); filtered manually. No new in-window Anki Show HN beyond already-kept Segar/ReadPlusOne/SubSmith.

## Bank deposits
- raw/learning/2026-08-31-sangkwun-kiip-study-exam-format-korean-practice.md ← https://www.kiipstudy.com
- raw/learning/2026-08-31-sangkwun-show-hn-kiip-study-exam-practice.md ← HN 49475164
- raw/learning/2026-08-31-rryoung98-tenken-declaude-claude-english-to-plain-english.md ← https://speak-english.tenken.co/
- raw/learning/2026-08-31-rryoung98-show-hn-declaude.md ← HN 49443296
- raw/learning/2026-08-31-iatrox-chatgpt-is-not-an-ai-tutor.md ← iatrox bounce
- raw/learning/2026-08-31-jason-corso-why-i-stopped-fighting-ai-in.md ← PressBee mirror of Corso TIME piece

## Queries actually run (live)
WebSearch: `"AI tutor" OR "AI teacher" "I built"… 2026`; `"Grok Bot" (tutor OR language OR Anki…) 2026`; `"I built" tutor/Anki 2026 -Telnyx`; Show HN Anki/graded/i+1 Aug 2026; `"my students" OR "I teach" AI/Anki Aug 25–31`; Grok Bot I-built/routine last week; Lexiloop/Mogoru/iatrox dates; Corso TIME author.
HN Algolia (created_at_i > 1787529600 = 2026-08-24): language learning, Anki, AI tutor, graded reader, i+1, Show HN tutor, SRS stories, language tutor, Show HN language/Anki/flashcard/SRS, tutor, flashcard, Anki Claude, spaced repetition, learning app, language app, Korean, Japanese learn, Spanish stories, flashcards, comprehensible, immigration test, quantum chemistry, Perusall, classroom AI, `"I built" (tutor OR Anki OR language)`.
DEV.to: `/api/articles?tag={ai,education,language,learning,tutor,anki,machinelearning}&top=7`; search/feed_content (empty).
grokbot.dev RSS: education-keyword sweep (only stock-valuation “teach a bot” hit, already SEEN / off-lane).
No packet file written; field-seen.json not edited.

## Scoreboard for packet compiler
education keeps this hunt: **3** (KIIP Study; Declaude taste-gate; Corso mastery-first classroom). Empty streak remains broken (packet 17 had 3). Prefer leading with KIIP (on-lane language) then Corso (classroom gates) then Declaude (portable taste-gate for generated course/tutor text).
