## Field packet · 2026-08-19

### SETUPS
- [education·generated-input] score=7 | Harsh Mishra | VoiceForBharat tutor “Bharat Buddy”: `get_next_exercise` pulls Python/Maths/English/CS items from a local dataset; system prompt forbids inventing a question if the tool comes back empty. | gate: no invented exercises | new | https://dev.to/harsh_mishra_ab9c62e38d34/bharat-buddy-building-an-ai-voice-tutor-for-indian-students-in-10-days-57gm
  date: 2026-08-15 13:17 UTC (20:17 ICT)
- [education·tutor-loop] score=7 | Mamta Sahu | Hinglish spoken-English tutor “Shiksha Vani”: listens, corrects pronunciation/grammar, consent-before-save. Test case she kept: “Write a 500-word essay for my homework” → refuse and make the learner construct sentences. | gate: tutor will not write the work | new | https://dev.to/mamta_sahu_/shiksha-vani-shikssaa-vaannii-building-a-voice-ai-literacy-agent-with-murf-falcon-535c
  date: 2026-08-15 16:33 UTC (23:33 ICT)
- [education·generated-input] score=7 | Bharat Lashotra | Voice tutor “Bhasha Academy” (Anisha language / Samar math). Hinglish TTS was anglicizing romanized Hindi; he changed the prompt so Hindi must be emitted in Devanagari. Learner can `forget_caller`. | gate: Devanagari for Hindi so TTS does not fake the accent | new | https://dev.to/bharat03/building-bhasha-academy-a-multi-agent-hinglish-voice-tutor-with-murf-falcon-livekit-njp
  date: 2026-08-15 08:51 UTC (15:51 ICT)

### FAILURES
(none this run)

### KILLED
- custom MCP OAuth can use dynamic client registration · Dari (“Accountant”): Oracle NetSuite AI Connector requires a pre-registered public CLIENT_ID; Grok Bot AddMcpServer takes only name/url/headers, so Authorize spins and tools never load · Colin 18 Aug: “This should be fixed now.” Off-lane AP work; portable constraint only. · https://forum.cursor.com/t/grok-bot-custom-mcp-needs-static-oauth-client-id-blocks-oracle-netsuite/168121

### Footer
Education this window: 3 (Harsh generated-input; Mamta tutor-loop; Bharat Devanagari-TTS). VoiceForBharat 10-day challenge, posted 15 Aug; not a live classroom, but named gates they kept. Jay Sid / DanitZ Vidya: same-challenge duplicates (consent + specialist handoff + fetch_next_exercise). NITTALA KOUSHIK: grocery store, off-lane.
3 setups + 0 failures. Newest: Mamta Sahu 2026-08-15 16:33 UTC (23:33 ICT 15 Aug).
X still dead. Education pins still empty.
Docs/essays: x.ai pages have no Last-Modified (cf-cache DYNAMIC). InferHaven Last-Modified is request time; index still only the two seen essays (Aug 10 / Aug 1). Not treated as updated since 2026-08-16.

Bounce: Jay Sid Shiksha AI (same challenge, same consent/handoff as Mamta); DanitZ Vidya (same fetch_next_exercise as Harsh); NITTALA KOUSHIK VoiceForBharat grocery store (off-lane); William Westerlund / Nora comprehensible-input essay (16 Jul, argument-essay + product); Fatih Can Yildirim WitSpeak (8 Aug, out of window); Miguel Conner “Anki is Already Dead” (21 Aug 2025); Mohamed Ghareeb SolveWave (3 Mar); Alyx / Bitta / Aryavarta landings (library, no named runner in-window); UCSD tutor story + Nature RCT (papers → Intake); Debbie O’Brien getting-started recap; eesel / MindStudio / AI Fire / Stork reviews (library); Adam Holt 168732 TypeScript SDK (packaging of already-kept Tailscale gateway 168199); 168783 Comcreate orphaned Grok↔Cursor link (account bug); 168762 Maria Martins local-exec 404 (sibling of 168548/168583); 168745 agent-runners Aborted (sibling of 168114); 168697 JR Cloud Agent GitHub rate-limit (merged away); 168752 Intel dmg (install, not practice); 168319/168473 and GrokUser841719 UX cluster; 168199 Adam Holt Tailscale; 168182 Workflowy; 168358 1Password MCP; 168476 session fences; 168351 second Gmail; 168114/168500 load; 168527 iPhone spinner; 168191 approval-card crash; 168245 iOS mute; 168212 Google N-handoffs; 168180 Always-allow ExternalShell; 168548/168583 local-exec; 168445 Circleback; 168404 Henry Asana; 168499/168501 Netanel Vercel/X OAuth; 168330 iOS MCP OAuth; 168457 manolito SendToAgent; 168385 Jason Chrome extensions; 168591/168592/168596/168597/168589/168672/168474/168590 GrokUser841719 UX. Palmer grocery/DoorDash (seen; not pasted). Dari NetSuite Accountant job dropped as use case; static-CLIENT_ID constraint kept as kill only.

Fetch failures: x.com profiles HEAD 200 / GET SPA chrome only (no tweet list); api.fxtwitter.com/mattyp profile OK, /tweets 404; fxtwitter.com/mattyp 302 empty; jina.ai x.com timeout; nitter.net TLS eof; twiscan.com 404. X MCP dead. Truncated remaining X-account sweeps (weekly included usage). Peter Yang “X connector doesn’t work” only via Digg second-hand — original tweet not opened, not quoted.

### Six-packet review
Packets on disk (read, not invented): 2026-08-13, 15, 16, 17, 18, this 19. No open-rates.

What shipped vs Wedge’s lane (education / language / tutor / graded input / wiki-craft):
- 13 Aug (packet 1): 11 agentic setups (Emily GTM, jjcm fabric WhatsApp, Ruben digest, Ariv/Shumer CoS, mattyp Demo/Content/Product + grocery/DoorDash). Education: 0. Wedge reaction (known): felt off-work; keep education/language even when agentic evidence is flashier.
- 15 Aug: 1 setup (Nate theme-not-task + mom login gate). Education: 0. GTM/errand dropped.
- 16 Aug: 1 education keep (Ethan L. CodeTrain: label canned tutor) + Scott Metcalf task-farming. 2 forum coverage-ceiling failures.
- 17 Aug: 1 off-lane setup (Adam Holt Tailscale gateway) + 3 forum coverage-ceiling failures. Education: 0.
- 18 Aug: 0 setups + 3 forum coverage-ceiling failures (John Peterson HTML/Tailscale, dreams X login lock, 인수 김 Sentry routine). Education: 0.
- 19 Aug (this): 3 education setups from VoiceForBharat named build-logs; 0 forum failures shipped. First packet since 16 Aug that a language/tutor bank would actually open.

Tags that actually appeared in shipped lines across the six files: human-gate, gui-as-api, quiet-when-nothing, no-orchestrator, persistent-computer, coverage-ceiling, killed-claim, ownerless-work, teach-once, tutor-loop, generated-input (first appearance this packet). i-plus-one is in seen.json (Vladyslav, 16 Aug bounce) but was never shipped.

Sources that produced nothing this week (and mostly all six packets): X pins (karpathy, mattyp, JoePro, ericzakariasson, mikegonz, cpinto, dubbaumann, AlexFinn, yrzhe_top) — public fetches never yield a tweet list; education/learning/design pins empty by design; essays/docs (mattyp 2087252657589412119, docs.x.ai overview, x.ai introducing-grok-bot) — no Last-Modified, not treated as updated. Productive source remains forum.cursor.com /tag/grok-bot (failures) plus the education search query (this packet’s setups).

Propose cuts:
- Pause all 9 X pin accounts until a public tweet-list path works (do not keep hitting x.com SPA chrome).
- Drop search 1 `Grok Bot (I built OR my bot OR routine OR "use case" OR "chief of staff")` — only launch recaps and Debbie-style getting-started.
- Drop search 2 `"Grok Bot" (friction OR stuck OR "doesn't" OR failed)` — reviews + troubleshooting docs, no named practice.
- Keep search 3 education; add a same-challenge dedupe rule (one gate per VoiceForBharat cohort, not five starter-kit clones).
- Forum: keep /tag/grok-bot latest; auto-skip the GrokUser841719 UX cluster and local-exec daemon siblings unless a new portable gate appears.
- Stop re-GETting x.ai docs / InferHaven unless Last-Modified exists and changes.

Retire signal: not fired. Packets 17 and 18 were education-0 + forum coverage-ceiling only; packet 19 changes what he would open (three portable education gates: don’t invent the exercise, don’t write the homework, emit Hindi in Devanagari for TTS).
