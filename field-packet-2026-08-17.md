## Field packet · 2026-08-17

### SETUPS
- [agentic·persistent-computer] score=8 | Adam Holt | Tailscale on the Bot computer + SSH tunnel to localhost:1340; `listAgents` / `sendPrompt` against a live install (undocumented gateway). | gate: never expose 1340; treat the gateway token as a password | new | https://forum.cursor.com/t/grok-bot-can-i-send-it-a-message-from-outside/168199
  date: 2026-08-12 22:13 UTC (05:13 ICT 13 Aug)

### FAILURES
- [coverage-ceiling] score=9 | GrokUser841719 | Gmail (then Drive, Calendar, Slack): View-only Google grant still shows write tools ON (Send / create_file / create_event / chat:write). `create_draft` / `create_file` / `create_event` 403 after the client tries to upscope; Google held. Connectors are account-wide, not per-Bot. | https://forum.cursor.com/t/grok-bot-gmail-multi-account-connector-shows-write-tools-on-for-view-only-tokens-and-attempts-oauth-upscope/168575
- [coverage-ceiling] score=9 | Frank Watts | Agent Computer egresses AWS us-west-2. `ezyparts.bntnz.co.nz` Imperva Error 16 before any login form (no captcha to take over). Rebuild still lands US AWS; no region picker. | https://forum.cursor.com/t/grok-bot-computer-is-us-aws-only-nz-trade-sites-behind-imperva-hard-block-it/168271
- [coverage-ceiling] score=8 | manolito nora | HARD SILENCE RULE in agent profiles: Builder 133× `SendMessage(".")`, then Atlas/Chief ~198× `Shell true` as a silent-end. Profile/memory text cannot stop it. | https://forum.cursor.com/t/grok-bot-agents-spam-sendmessage-on-agent-fyi-and-post-tool-turns-burns-usage/168211

### KILLED
- View-only / “read-only” connector is a lock · GrokUser841719: UI and catalog show write ON; the Google token is the real lock; clicking the upscope prompt would let a “read-only” mailbox send · https://forum.cursor.com/t/grok-bot-gmail-multi-account-connector-shows-write-tools-on-for-view-only-tokens-and-attempts-oauth-upscope/168575
- “Bot has its own computer” beats geo-WAF · Frank: Imperva hard-block, no human challenge to clear; takeover has nothing to click · https://forum.cursor.com/t/grok-bot-computer-is-us-aws-only-nz-trade-sites-behind-imperva-hard-block-it/168271
- persona text can enforce quiet · manolito: HARD SILENCE still `.` then `true` · https://forum.cursor.com/t/grok-bot-agents-spam-sendmessage-on-agent-fyi-and-post-tool-turns-burns-usage/168211
- local MCP / corp-VPN MCP · Steven Hertz (Workflowy stdio), Jay Graves (1Password ENOENT), Gabriel Paixão (custom remote OAuth `fetch failed`): cloud path is public HTTPS only; localhost is unreachable · https://forum.cursor.com/t/does-grok-bot-support-local-mcp-e-g-workflowy/168182 · https://forum.cursor.com/t/grok-bot-cannot-spawn-1password-mcp-1password-mcp-enoent/168358 · https://forum.cursor.com/t/grok-bot-custom-remote-mcp-oauth-never-starts-fetch-failed-same-url-works-in-cursor-ide/168188
- separate Bot windows isolate logins · GrokUser841719 16 Aug follow-up: Bot B inherits cookies without seeing Bot A’s screen (docs already killed this 13 Aug; UX still teaches the opposite) · https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476
- second Gmail account for a specialist Bot · Brennen Harris: Added then reverts; Ops cannot have its own inbox (GTM; portable gate only) · https://forum.cursor.com/t/grok-bot-second-gmail-google-workspace-account-flashes-added-then-reverts-to-authorize/168351

### Footer
Education this window: 0. Anki tutor Jun 19 (gde / Antigravity), VisionSolve Mar, Kling Apr, Alaa Aug 4, CodeTrain architecture Aug 1, Ethan demo-honesty (packet 16): out of window or already kept. InferHaven index: no new post past the two seen essays. Taalhammer n+1, Tom Daccord hyperrealistic tutors (Feb/Mar), EspaLuz (May): out of window.
1 setup + 3 failures. Newest: GrokUser841719 2026-08-16 19:31 UTC (02:31 ICT 17 Aug).
X still dead. Education pins still empty.
Docs/essays: x.ai pages have no Last-Modified (Next cache). InferHaven Last-Modified is request time. Not treated as updated since 2026-08-16.

Bounce: Debbie O’Brien getting-started (DEV.to 14 Aug / debbie.codes); Jay Vermont 23-routines LinkedIn (GTM); James Burnham (no setup); AY Automate second-hand Lipsky/Jowett Beehiiv–Salesforce (GTM); Adam Stanco GTM roster (not opened); forum 168114 / 168500 load-reconnect; 168527 iPhone spinner; 168191 approval-card crash (fixed 0.18.0); 168245 iOS foreground mute; 168212 Google N-handoffs (sibling of session-fence kill); 168052 IBKR OAuth (folded into MCP kill); 168180 Always-allow ExternalShell (settings bug, not a new gate); Palmer grocery/DoorDash (seen; not pasted).

Fetch failures: x.com/mattyp 403; fxtwitter tweet-list endpoints 404 (profiles only for karpathy, mattyp, JoePro, ericzakariasson, mikegonz, cpinto, dubbaumann, AlexFinn, yrzhe_top); jina.ai x.com 403. X MCP dead. YouTube Lipsky/Jowett not opened as first-party text.


## Addendum (same run)
### FAILURES
- [coverage-ceiling] score=9 | GrokUser841719 | Gmail (then Drive, Calendar, Slack): View-only Google grant still shows write tools ON. create_draft / create_file / create_event 403 after client tries to upscope; Google held. Connectors are account-wide, not per-Bot. | https://forum.cursor.com/t/grok-bot-gmail-multi-account-connector-shows-write-tools-on-for-view-only-tokens-and-attempts-oauth-upscope/168575
- [coverage-ceiling] score=9 | Frank Watts | Agent Computer egresses AWS us-west-2. ezyparts.bntnz.co.nz Imperva Error 16 before any login form. Rebuild still US AWS; no region picker. | https://forum.cursor.com/t/grok-bot-computer-is-us-aws-only-nz-trade-sites-behind-imperva-hard-block-it/168271
- [coverage-ceiling] score=8 | manolito nora | HARD SILENCE RULE in profiles: Builder 133× SendMessage("."), then Atlas/Chief ~198× Shell true. Profile text cannot stop it. | https://forum.cursor.com/t/grok-bot-agents-spam-sendmessage-on-agent-fyi-and-post-tool-turns-burns-usage/168211

### KILLED
- View-only connector is a lock · UI/catalog show write ON; Google token is the real lock; clicking upscope would let a “read-only” mailbox send
- “own computer” beats geo-WAF · Imperva hard-block, no challenge to clear
- persona text can enforce quiet · HARD SILENCE still "." then true
