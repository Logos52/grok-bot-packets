# Field · latest

## Alert · 2026-08-28
none

## Field packet · 2026-08-28

### SETUPS
- [education·tutor-loop·generated-input] score=7 | Haruna Oseni (Learn Leap) | Built Learn Leap because he kept pasting research-paper questions into ChatGPT with no shared context. Upload your own material; the tutor teaches from that file set and can make quizzes, flashcards, and exams against it. Show HN 22 Aug; still early. Gate: the corpus is the course, not a general model — if the material is not in the upload, the tutor has no lesson. | https://news.ycombinator.com/item?id=49397663
  date: 2026-08-22 08:07 UTC (15:07 ICT 22 Aug) · product https://learnleap.xyz
- [agentic·human-gate] score=8 | Teslaconomics | Day-1 personal CFO on Grok Bot with full read on personal + business banks, credit cards, Apple Card, and X Money. Morning ask: cash on hand split personal/business, every card bill by due date, green/red cover-in-full with exact shortfall, daily nudge while still red, three-month spend as pie charts from chat. Off-lane money; keep is the fence — he still has to say yes before it pays, moves money, or does anything actionable, and he prefers it that way. Friction he ate: banks treated the Bot computer as a new device (phone call) and idle sessions force re-login. Not a roster pick. | https://x.com/Teslaconomics/status/2092837438146351407
  date: 2026-08-27 04:51 UTC (11:51 ICT 27 Aug) · catalog https://grokbot.dev/use-cases/personal-cfo-bank-access/ (✦80)

### FAILURES
- [agentic·human-gate·killed-claim] score=7 | Jonathan Zalesne | Building comment.io against Grok Bot webhooks: a signed webhook starts a routine, the Bot does the work, then Auto Review still blocks a predeclared outbound (exact URL/method or tool) unless a recent typed chat turn mentions the target. Standing routine text does not count as intent; the webhook that woke the run does not either. So unattended "external event → Bot works → one declared side effect" is unreliable. Ask: allowlist follow-ups on that webhook routine; verified delivery is the approval for that list only; Require Approval still wins. Not a shipped rule change — a named failure shape for anyone wiring Slack/GitHub/email-out wakes. | https://forum.cursor.com/t/webhook-triggered-grok-bot-routine-should-count-as-user-intent-for-predeclared-outbound-actions/169720
  date: 2026-08-27 16:21 UTC (23:21 ICT 27 Aug)

### KILLED
- paste into a general chat while you read · Haruna Oseni: tutor that already holds the uploaded papers; quizzes and flashcards from that corpus · https://news.ycombinator.com/item?id=49397663
- bank access means the Bot may pay · Teslaconomics: full read, yes-before-pay/move, daily red reminders until green · https://x.com/Teslaconomics/status/2092837438146351407
- webhook wake + routine text = Auto Review intent for outbound · Jonathan Zalesne: they do not; typed chat still required unless product adds a per-trigger allowlist · https://forum.cursor.com/t/webhook-triggered-grok-bot-routine-should-count-as-user-intent-for-predeclared-outbound-actions/169720

### Footer
Education this window: 1 (Haruna Oseni / Learn Leap — tutor from your own material). Packet 13 was education 0; 14 broke the empty streak; today stays at 1.
2 setups + 1 failure. Newest kept: Teslaconomics 2026-08-27 04:51 UTC (11:51 ICT 27 Aug) — inside 5 days, no stale-sweep canary.
Packet 15 (6-packet review already shipped 19 Aug).
grokbot.dev: fourth sweep. Catalog lastBuild 2026-08-27 18:59 UTC (01:59 ICT 28 Aug). Page 1 new-or-reshuffled since yesterday: track-the-grok-bot-team (76, Ben Lang), ai-search-lead (71), personal-cfo-bank-access (80, Teslaconomics — kept), house-memory-bot (78, Morgan Linton). 80+ opened first-party this run: personal-cfo-bank-access only (other 80+ on the rail were already in field-seen from packets 12–14). Below-80 opened: track-the-grok-bot-team (Ben's post is "follow these seven people"; catalog invented the daily seen-log bot — bounced), house-memory-bot (Morgan: "just came up with" — idea, not a run — bounced), ai-search-lead (Eric Osiu Aug 18 wishlist of bots to build, not a run; primary out of window). Plugin tables treated as library (PDF.ai, Pallyy, PhoneZero, Appllama, OmniSocials, Search1API, and the rest of the unseen plugin rail). Off-lane money (Teslaconomics CFO) gated; not a roster pick.

X still dead: api.fxtwitter.com user tweets 404 for pins (karpathy, mattyp). Specific-status fxtwitter still works (Teslaconomics, Ben, Morgan, Eric). Education pins still empty; education SEARCH produced Learn Leap (keep) plus library/out-of-window bounces.
Docs/essays: docs.x.ai/grok-bot/overview and x.ai/news/introducing-grok-bot answer 200 with no Last-Modified; not re-read. mattyp status not re-fetched beyond seen.
Bounce: track-the-grok-bot-team (catalog | Ben follow-list ≠ run); house-memory-bot (idea | Morgan "just came up with"); ai-search-lead (wishlist | Eric Aug 18); Lena Brooks homework-vs-exam essay (library | study summary + generic friction tips, not a named classroom she runs) https://dev.to/lenabrooks/when-ai-makes-homework-faster-but-learning-worse-a-practical-way-to-rebuild-student-workflows-5ci7; Charlie Xu MonkeyCode bootcamp lab (library/outreach | product disclosure, not Wedge-lane language tutor) https://dev.to/hackjs_7468/a-bootcamp-lab-for-stress-testing-ai-coding-models-on-a-0-budget-12fe; Ilya Selivanov lookup-dependency essay (library) https://dev.to/ilyatech/reducing-dependency-on-lookups-strategies-for-beginner-programmers-to-internalize-concepts-and-42f8; Andrew Will Promova tutor post Jul 3 (out); Pallavi / VoiceForBharat / EspaLuz / UniUI already seen or out; KFC WRITERS tutoring spam (library); ogc16 ZH classroom posts (Yuedu exclude); Roan Monteiro shared-computer deep dive Aug 20 (out of 7d window; killed-claim already banked via docs); forum 169763 Mac unsupported on Intel 13.7 (install); 169679 Bohan weekly→On-Demand no warning (billing → Brief); 169746 Cloud Agent Fast ignores Bot default (sibling capability); 169754 open cloud-agent in browser (feature); 169752/169676/169663 first-setup/reconnecting siblings; 169684 Origin codebase access (help); 169658 usage vs Cursor plan (billing); plugins PDF.ai/Pallyy/PhoneZero/Appllama/OmniSocials/Search1API (library).
Fetch failures: pin timeline fxtwitter 404; learnleap.xyz is a JS shell (product URL logged; practice taken from Show HN text). Truncated: remaining unseen RSS plugins and older usecase rail after the four new page-1 cards.
Retire signal: education counts recent — 13:0, 14:1, 15:1. Empty streak not running. Retire: no.
