## Field packet · 2026-08-18

### SETUPS
(none this run)

### FAILURES
- [coverage-ceiling] score=9 | John Peterson | Tailscale hop (read-only) to his own mini, then an interactive HTML report as a chat download. JSON write on the Bot computer succeeds. One-shot HTML/JS (or the Python that builds it) is rejected: “executable content could not be bound to this review.” Copying that JSON over the same tailnet to his Mac is blocked as an “outbound transfer to an external remote host.” In-chat feedback: unavailable in privacy mode. | https://forum.cursor.com/t/grok-bot-computer-cannot-finish-a-normal-workflow-details/168682
  date: 2026-08-17 21:44 UTC (04:44 ICT 18 Aug)
- [coverage-ceiling] score=9 | dreams | Agent kept submitting X login for @dreams_asi on the Bot computer. That machine now gets “We’ve temporarily limited your login”; email path says incorrect password. Same account logs in on his own devices. Limit did not lift after a day. Kevin (17 Aug): try a new agent and log in yourself rather than asking the agent. | https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541
  date: 2026-08-16 07:26 UTC (14:26 ICT); staff 2026-08-17 21:08 UTC (04:08 ICT 18 Aug)
- [coverage-ceiling] score=8 | 인수 김 (셀로실장) | Sentry Routines on project haccp-selo: issueCreated and issueAny stayed at lastRunAt null / “No runs yet.” Direct ingest HTTP 200; existing Sentry→Telegram path delivered both tests in ~1 min. Manual Run now succeeded but had no issue payload (“user pressed Run now”). | https://forum.cursor.com/t/grok-bot-sentry-routine-auto-trigger-failure/168421
  date: 2026-08-14 15:57 UTC (22:57 ICT); tests 2026-08-15 00:27–00:38 KST

### KILLED
- “Bot has its own computer” can write a report and move files on your tailnet · John: one-shot HTML/JS treated as unbound executable; Tailscale hop treated as a leak to a random host · https://forum.cursor.com/t/grok-bot-computer-cannot-finish-a-normal-workflow-details/168682
- Agent Computer is a normal X client · dreams: agent burned the login; human login on that machine still limited; staff workaround is a new agent + you type it · https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541
- event-triggered Routine fires when the source fires · 인수 김: Sentry created the issue and Telegram rang; Grok Bot never woke · https://forum.cursor.com/t/grok-bot-sentry-routine-auto-trigger-failure/168421
- Update Agent Computer preserves browser setup · Jason Robertson (Jarvis): 1Password Chrome extension gone after update; bot will not type a password, so bank logins stuck · https://forum.cursor.com/t/grok-bot-chrome-extensions-disappear-after-a-computer-update/168385

### Footer
Education this window: 0. Anki tutor Jun 19 (gde / Antigravity), VisionSolve Mar, Kling Apr, Alaa Aug 4, CodeTrain architecture Aug 1, Ethan demo-honesty (packet 16): out of window or already kept. InferHaven index: still only the two seen essays (Aug 10 / Aug 1). Taalhammer n+1, Tom Daccord hyperrealistic tutors (Feb/Mar), EspaLuz (May): out of window.
0 setups + 3 failures. Newest: John Peterson 2026-08-17 21:44 UTC (04:44 ICT 18 Aug).
X still dead. Education pins still empty.
Docs/essays: x.ai pages have no Last-Modified (cf-cache DYNAMIC). InferHaven Last-Modified is request time. Not treated as updated since 2026-08-16.

Bounce: Debbie O’Brien recaps (DEV.to getting-started / flight-booking; LinkedIn); Kartik Chilkoti commentary (no setup); Andrea Lowitz GTM roster + grocery (not pasted); Jay Vermont 23-routines (GTM, prior); AY Automate / Adam Stanco GTM (prior); forum 168199 Adam Holt Tailscale (skip); 168182 Workflowy / 168358 1Password MCP (skip; Jason’s Chrome-extension wipe kept as kill only); 168476 session fences / 168351 second Gmail / 168114 load outage (skip); 168527 iPhone spinner; 168191 approval-card crash (fixed 0.18.0); 168245 iOS foreground mute; 168212 Google N-handoffs; 168052 IBKR OAuth; 168180 Always-allow ExternalShell; 168548 / 168583 local-exec daemon flap; 168445 Circleback “connector reported no details” (Joel; staff 17 Aug; no named job); 168404 Henry Asana `${env:ASANA_CLIENT_ID}` unsubstituted (fold into cloud-MCP kill); 168499/168501 Netanel Vercel/X plugin OAuth; 168330 iOS MCP OAuth no return; 168457 manolito SendToAgent≠ownership (Travel refusals; feature request); 168591/168592/168596/168597/168589/168672/168474/168590 GrokUser841719 UX (edit trail, group Computer view, emoji, delete, hover, iOS usage/select, Cmd+Shift+V). Palmer grocery/DoorDash (seen; not pasted).

Fetch failures: x.com/karpathy WebFetch 403; fxtwitter.com/mattyp 500; jina.ai x.com hung; x.com/mattyp HEAD 200 (profile chrome only, no tweet list). X MCP dead. LinkedIn named-practice search returned recaps/commentary only.


## Addendum (same run)
### FAILURES
- [coverage-ceiling] score=9 | John Peterson | Tailscale hop (read-only) to his mini, then an interactive HTML report as a chat download. JSON write on the Bot computer succeeds. One-shot HTML/JS is rejected as unbound executable. Copying that JSON over the same tailnet to his Mac is blocked as an outbound transfer to an external host. | https://forum.cursor.com/t/grok-bot-computer-cannot-finish-a-normal-workflow-details/168682
- [coverage-ceiling] score=9 | dreams | Agent kept submitting X login for @dreams_asi on the Bot computer. That machine now gets “temporarily limited your login.” Same account works on his own devices. Kevin (17 Aug): try a new agent and log in yourself. | https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541
- [coverage-ceiling] score=8 | 인수 김 | Sentry Routines issueCreated/issueAny stayed at no runs. Direct ingest 200; Sentry→Telegram delivered in ~1 min. Manual Run now had no issue payload. | https://forum.cursor.com/t/grok-bot-sentry-routine-auto-trigger-failure/168421

### KILLED
- Bot computer can write a report and move files on your tailnet · HTML/JS treated as unbound executable; Tailscale hop treated as a leak
- Agent Computer is a normal X client · agent burned the login; staff workaround is a new agent + you type it
- event-triggered Routine fires when the source fires · Sentry created the issue and Telegram rang; Grok Bot never woke
