# Field education hunt — 2026-09-03 scratch
Window: ~2026-08-27 → 2026-09-03. Lane: language / tutors / graded+generated input / wiki-craft / Anki+SRS / i+1. Combined ≥6 + NAMED runner to keep. Do NOT write packet; field-seen.json untouched.

## KEEP candidates

### 1) anatoly314 (Anatoly Tarnavsky) / ankimcp — Anki MCP Server (PRIMARY)
- who: Anatoly Tarnavsky (`author` in package.json); org/repo `ankimcp/anki-mcp-server`; site ankimcp.ai
- url: https://github.com/ankimcp/anki-mcp-server · https://ankimcp.ai
- date: push/commit 2026-08-31 20:15 UTC (03:15 ICT 1 Sep) — v0.25.0 `forgetCards`/`setDueDate` harden; in ~7d window
- tags: education·tutor-loop·human-gate·killed-claim·coverage-ceiling·teach-once
- portable/evidence/combined: 5 / 5 / 10
- one-line packet shape: [education·tutor-loop·human-gate·killed-claim·coverage-ceiling·teach-once] score=10 | anatoly314 (Anatoly Tarnavsky) / ankimcp | MCP server (50 tools) so an AI runs a live Anki tutor-loop: `sync` → `get_due_cards` → `present_card` → `rate_card`, with explanations in the chat. Schedule surgery is separated from grading: `forgetCards` / `setDueDate` move or reset a card **without** logging a review — README kills using `Again` to “bury deeper” (that records a real lapse and tanks ease). Stats honesty gate: `counts` = due-today capped by daily new/review limits (browser mirror); `states` = true new/learning/review/suspended/buried ignoring limits. Remote path prefers authenticated managed Tunnel (OAuth device-flow approve → `~/.ankimcp/credentials.json` 0600) over open ngrok. `deleteNotes` destructive+confirmation. Killed: “rate Again to reschedule”; “deck `review` count = mature cards”; “expose Anki with an unauthenticated public URL.” Distinct from bornayo7 srs-app (owns the SRS host + AI review queue), overtonch ru-anki (YouTube-subs → Make/Discard), sergiyclas anki-quick-add (in-page prepare/commit), Loopback (Obsidian capture→Anki), Segar (held-out QC), SubSmith (Whisper on your files), UniUI (subject-engine verify), ReadPlusOne (i+1 stories) — this is a tutor over your existing Anki review queue plus schedule tools that refuse to fake reviews. | https://github.com/ankimcp/anki-mcp-server
- why distinct: tutor-loop on **your** Anki due queue + explicit no-fake-review schedule tools; not a new SRS host, not mining, not held-out card QC.

### 2) mansourvery-hub / CompreDef
- who: mansourvery-hub (README + WIKI first-party)
- url: https://github.com/mansourvery-hub/CompreDef
- date: created 2026-09-02 · push 2026-09-02 23:50 UTC (06:50 ICT 3 Sep) — ZIP/Yomitan HTML + 100% CPU fix
- tags: education·i-plus-one·coverage-ceiling·teach-once·killed-claim·generated-input
- portable/evidence/combined: 5 / 4 / 9
- one-line packet shape: [education·i-plus-one·coverage-ceiling·teach-once·killed-claim] score=9 | mansourvery-hub / CompreDef | Anki add-on: ordered **dictionary ladder** (children’s → HS → advanced Yomitan dicts). Early-exit: first definition whose kanji are all already known in Anki (`interval > 0`) wins; else maximal-comprehension fallback. Zero LLM, offline, deterministic. Bulk generate from Browser / editor button. WIKI frames it as Krashen i+1 against the monolingual circular-lookup trap. Killed: “monolingual def = always advanced dict”; “LLM rewrite is required for comprehensible defs.” Distinct from bornayo7 (AI course units → review queue), overtonch (lemma extract → Make/Discard), sergiyclas (page word → structured card), Loopback/Segar/SubSmith/UniUI/ReadPlusOne — definition selection gated by **your known-kanji set**, not card enrollment. Distinct from mansour `anki-japanese-template` (UI note type only; bounced yesterday as “mansour template”). | https://github.com/mansourvery-hub/CompreDef
- why distinct: i+1 applies to **definition text** via known-kanji early-exit ladder, not to story generation or review-queue drafting.

### 3) joshgummersall / ankix
- who: joshgummersall
- url: https://github.com/joshgummersall/ankix
- date: push 2026-09-01 22:17 UTC (05:17 ICT 2 Sep) — resume-to-exact-word merge; created 2026-07-20 (update in window)
- tags: education·generated-input·teach-once·human-gate·killed-claim
- portable/evidence/combined: 4 / 4 / 8
- one-line packet shape: [education·generated-input·teach-once·human-gate·killed-claim] score=8 | joshgummersall / ankix | Local-first CLI: Kindle `vocab.db` / YouTube subs (`yt-dlp`) / web article → **contextual** defs from a local Ollama `ankix` model (sentence with target bolded, not bare dict) → AnkiConnect. `--dry-run` preview; re-run skips headwords already in the target deck; Kindle path marks WORDS mastered after sync and snapshots `vocab.db` with undoable restore. Killed: “Kindle Vocabulary Builder is a review system” (it isn’t — ankix closes the loop into Anki); “definition without sentence context.” Distinct from overtonch ru-anki (Claude CLI + UI Make/Discard for Russian lemmas), SubSmith (local Whisper on your media), sergiyclas (in-page Shift-select), bornayo7 (full SRS PWA), Loopback/Segar/UniUI/ReadPlusOne — Kindle/YouTube/web lookup → local Ollama contextual note with dry-run + Kindle progress watermark. | https://github.com/joshgummersall/ankix
- why distinct: source is Kindle vocab.db + local Ollama context defs; overtonch is YouTube-subs Claude extract with explicit Make/Discard UI.

## BOUNCE list (url | why)
- https://github.com/mansourvery-hub/anki-japanese-template | already bounced yesterday as “mansour template”; UI/note-type polish, no new portable gate beyond CompreDef
- https://github.com/portpowered/anki-web-mcp | already bounced (portpowered WebMCP); Anki-against-a-website, thin named-run diary
- https://github.com/heuwels/lector | already bounced (lector product ship); no new runner diary this window
- https://github.com/doasfrancisco/anki-skill | out of window (last commit 2026-02-16); otherwise strong human-gate approve-before-AnkiConnect + leech/quality rules
- https://github.com/polyphilz/ccflash | out of window (last commit 2026-03-29); interactive review-before-upload density dial
- https://github.com/crisak/anki-connect-skill | out of window (2026-04-18); curl skill library
- https://github.com/nailuoGG/anki-mcp-server | stale vs ankimcp primary (last atom ~2026-07); library/duplicate lane
- https://github.com/AlphaNerdFx/Tango | YouTube→apkg auto pipeline; weaker human-gate than overtonch Make/Discard; created 2026-06, packaging push only
- https://github.com/enderzhangpro/Automatic-Anki-Card-Maker | thin README (180B); local-LLM Chinese word→card with no gate/failure diary
- https://github.com/BrayanGuti/RecallBook | Duolingo+Anki clone pitch; no named practice/gates
- https://github.com/Factbact/cbt-anki-inbox | empty/no README
- https://github.com/HyunD-init/daily-language | no README; Korean/English daily app shell
- https://github.com/ErickMain/anki-kotoba-export | real addon (clipboard-default vs cookie API; forgotten-today/leech presets) but off-lane typing-site export, not language-input/tutor; cap if packet needs a 4th
- https://github.com/Shashwathkolhar/anki-x-qbank | strong human-gate unsuspend-from-qbank but **med AnKing**, not language lane
- https://github.com/Jumprocks1/mining-helper | mpv mining; setup page still TODO; created Feb, release fix push only
- https://github.com/hajisensai/Fushi | immersion product suite (194★); product ship, not new named diary this window
- https://github.com/1Selxo/Mangatan | Mangayomi fork / product; not new runner diary
- https://github.com/Olexify/Kitsumi | browser extension product; thin first-party practice writeup
- https://github.com/KakkoiDev/nihongo-it-anki | AI-audio IT vocab deck content; library/deck drop
- https://github.com/yuhouzhou/german-nouns-anki | already in seen; CEFR German noun decks
- https://github.com/Sushmitagadgi/LearnAI | adaptive tutor scaffold — treat as assignment-clone class until named classroom run
- https://github.com/nathanoc/typst-to-latex | Anki Typst→LaTeX addon; tooling not education practice
- https://github.com/DNT-Khoa/leetknight | LeetCode+Anki scaffold; off-lane
- https://github.com/dabajabaza/anki-deck-gen-tgbot | empty/thin telegram deck gen
- https://github.com/GitCrush/anki-dmr | deck licensing infra; not learner practice
- https://easyinput.app/ · https://sspai.com/post/109416 | graded-reader product + older sspai “I built”; marketing site, no fresh 7d runner diary (Hack Stack Dec 2024)
- https://tkdlabs.com/posts/flashcards-blog/ | Tom Korean Anki workflow — dated **2025-12-31**, outside window
- https://medium.com/@henri_w_91/automating-russian-language-learning-with-openclaw-via-the-rurussian-mcp-537ccbf4b44c | RuRussian MCP product/docs tone; no dated named failure/kept-run in window; overlaps overtonch Russian lane
- https://medium.com/data-science-collective/how-ai-can-become-your-personal-language-tutor-8e8b42c1b6b6 · https://towardsdatascience.com/how-ai-can-become-your-personal-language-tutor/ | n8n Mandarin study-partners essay; date unclear / not confirmed in-window first-party run
- https://medium.com/@bisbis.kamil/building-a-conversational-ai-to-teach-an-underrepresented-language-8dd118d17562 | Darija fine-tune writeup; date/window unconfirmed; fine-tune diary more than portable tutor gate
- https://dev.to/b1fe7066aefjbingbong/how-to-actually-learn-a-language-with-ai-in-2026-41fo | generic 2026 how-to listicle / library
- https://dev.to/pocket_linguist/i-built-an-ai-language-tutor-heres-what-i-learned-about-nlp-1656 | already seen
- https://abelchen.dev/projects/lexiloop-app | already seen; Apr 2026 out of window
- Voice/Gemini classroom assignment clones · OpenTutor marketing · meelang Meet translator | instructed avoid
- HN Anki query noise (Ankit Gupta H-1B; AnkiDroid donation) | not education practice; SubSmith Show HN already kept prior packet

## FETCH FAILURES
- GitHub REST **core** rate-limit remaining=0 for unauthenticated (reset ~1788395440); used Search API + raw.githubusercontent.com + commits `*.atom` for dates/READMEs instead of `/repos` metadata.
- GitHub HTML scrape for `datetime=` / Created returned empty (JS-rendered sidebar) — dates taken from Search API `created_at`/`pushed_at` + atom `<updated>`.
- `gh` not authenticated (`gh auth status` → not logged in).
- X / pin timelines not attempted (prior packets: MCP failed_to_load).
- Medium/@henri and Towards Data Science Mandarin tutor: partial WebSearch synthesis only; full first-party date not locked — bounced rather than half-kept.
- EasyInput sspai full post date not re-fetched beyond search snippets (pre-window signals).

## Truncated / rate-limit note
- Truncated: remaining noisy GitHub `anki` name-collisions and language-tutor assignment clones after the promising shortlist; did not exhaust ~300+ anki substring repos.
- Search API quota was available (10/10) and used; core API blocked mid-hunt — no further `/repos/{owner}/{repo}` or commits REST.
- Steering: wrapped with anatoly314/ankimcp as primary KEEP; stopped further hunting.

## Scoreboard for packet compiler
education keeps this hunt: **3** (ankimcp primary; CompreDef; ankix). Prefer lead ankimcp (tutor-loop over live Anki + no-fake-review schedule tools), then CompreDef (i+1 definition ladder), then ankix (Kindle/YouTube→local Ollama contextual notes).
No packet file written. field-seen.json not edited.
