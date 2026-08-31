# grokbot.dev sweep · packet 18 · 2026-08-31 ICT

Feed: /tmp/grokbot-feed.json generated 2026-08-30T22:34:11Z (05:34 ICT 31 Aug), 485 items.
RSS lastBuildDate Sun, 30 Aug 2026 22:34:18 GMT (05:34 ICT 31 Aug).
Delta vs packet 17 lastBuild 2026-08-29T23:23:00Z (06:23 ICT 30 Aug): 62 items (2 use-case, 1 plugin, 14 collection, 45 template, 0 news).
field-seen.json: 351 entries; none of the new herd/reply-guard/thekuchh URLs were listed. Not edited.
X MCP: DOWN (failed_to_load) as briefed. fxtwitter tweet payloads worked this run (unlike packet 16). r.jina.ai 403 on X URLs.
80+ rule: no new 80+ in the delta (new use-cases have awesome_score=null). Newest 80+ in feed are older catalog already seen 2026-08-26..29 (Gaurav calendar CRM 80, hedge fund 82, personal CFO 80, etc.). Not re-opened.

## Candidates (keep-worthy)

None in-lane. Education/tutor/graded-input/wiki-craft: 0 named-run practice this sweep.

Off-lane named practice that clears combined >= 6, **not roster**, do not lead:

### Jason Calacanis (@Jason) — reply-guard
- url: https://grokbot.dev/use-cases/reply-guard/
- x: https://x.com/Jason/status/2094095953812717647
- date: 2026-08-30T16:12:36Z (23:12 ICT 30 Aug)
- domain: agentic
- mechanism: human-gate, killed-claim
- portable: 4 · evidence: 4 · combined: 8
- Page opened. Named runner quote (page "as seen on x"): "It reviews my replies for suspected burner accounts (under 100 followers/under a year old) and flags people who use insults in their replies." Full fxtwitter text adds: "Keep it classy, fun and intelligent in my replies, because I'm going to auto-nuke under-one-year-old burners/psyop accounts that insult people." Jason built it; first-person; thresholds are his (100 followers / under a year). Grokbot how-to: connect X plugin, set those floors, return FLAGGED vs CLEAN. Curator prompt (explicitly "reconstructed … not their verbatim text") adds a human-gate the runner did not claim: disagreement/criticism stay CLEAN; when unsure put it in CLEAN and say why; "Do not hide, mute, block or reply to anyone on your own. Your job is the flagged list; the action is mine." Why-it's-cool even says "nobody gets auto-nuked on a bot's hunch" — which is the opposite of Jason's auto-nuke line. Portable keep: classify ≠ act, and a reconstructed "approve first" is not evidence the live bot waits. Failure/what-they-kept: none reported (no missed-flag story, no false-positive). Off-lane X-moderation / large-account firehose. Do not recommend for roster.
- alert-line: **no** — Wedge would not change a file, setting, or routine this week for reply triage on X.

## Bounce one-liners

bounce | https://grokbot.dev/use-cases/herd-your-bots/ | @herdrdev | vendor template, not a run report (page quote: "we made you a template, ready to go: Shepherd, the bot that herds your bots"); curator prompt has portable human-gate + quiet-when-nothing ("Do NOT stop, restart, reset, or reconfigure any bot on your own — propose the fix and wait for my go. When nothing is wrong, say so in one line"); fleet, not roster
bounce | https://x.com/herdrdev/status/2094129284885467399 | @herdrdev quoting @theaaron | product launch; quoted theaaron is a rate-limit workaround (install CLI agents on the Grok Bot VM, herdr manages sessions so Grok Bot limits are only coordination) — persistent-computer adjacent, not Shepherd fleet-check practice, not roster
bounce | https://grokbot.dev/marketplace/shepherd/ | @herdrdev | same tweet as herd-your-bots, template table
bounce | https://grokbot.dev/plugins/x-for-grok-bot/ | x.ai | plugin table / official X connector; Brief sibling of already-banked https://x.ai/news/grok-bot-and-x ; prompt says never post without explicit yes — library
bounce | https://grokbot.dev/marketplace/ | status notice marketplace-launch-2026-08 | Brief/library: grokbot now indexes Shareable Bots; do not alert
bounce | https://grokbot.dev/news/ | status notice news-launch-2026-08 | Brief/library: grokbot now publishes News; do not alert
bounce | 14 collections added 2026-08-30 | grokbot curator | library as a group: team-you-didnt-hire, award-travel, content-machine, fill-the-pipeline, founder-os, get-found, household-hq, look-after-yourself, never-overpay, reclaim-your-inbox, second-brain, ship-while-you-sleep, start-here, x-account-management (no named runner)
bounce | thekuchh education cluster (9 templates, 2026-08-30 ~16:43Z) | @thekuchh | library, not named-run: X posts are numbered share slogans + "add this template in grok bot" (1 consumption autopsy … 6 retrieval exam, skip 7, 8–10); grokbot pages are curator blurbs ("shared by @thekuchh") with instructions+workflow, no gate/failure/what-they-kept. Pages opened: retrieval-exam, just-in-time-curriculum, struggle-gate, feedback-clock, doing-gap, consumption-autopsy, action-loop, stuck-cycle, connection-audit. Struggle-gate's 10-minute withhold is a tutor-loop-shaped *idea* only. Catalog mismatch: status 2094103797270503600 tweets "8. compounding forecast" but grokbot filed it as Connection Audit (bookmark-pile). Not practice.
bounce | https://grokbot.dev/marketplace/tutor/ | @anandVragav | glance; library shareable bot (picture-then-check lesson); no named-run/gate; not in field-seen; added 2026-08-29T08:53 (pre-cutoff)
bounce | https://grokbot.dev/marketplace/homework-checker/ | @kevinace | glance; library (Google Classroom missing-work recap); no named-run; pre-cutoff 2026-08-28
bounce | https://grokbot.dev/marketplace/learn-math-ml-video-teacher/ | @JeffreyLind | glance; library (renders lessons as videos; never publishes); no named-run; pre-cutoff
bounce | https://grokbot.dev/marketplace/storiesbot/ | @viticci | glance; library (search 17y MacStories corpus); knowledge-craft-shaped catalog entry, no gate/failure; pre-cutoff
bounce | https://grokbot.dev/marketplace/dewey/ | @Vixlio | in-window template (2026-08-29T23:30Z) but not education — Gmail triage, send stays with you; library/off-lane
bounce | https://grokbot.dev/marketplace/onboarding-coach/ | @tpgoebel | glance; library (first-hour Grok Bot onboarding); no named-run; added 2026-08-29T16:31 (pre-cutoff, not in field-seen)
bounce | remaining new templates (36, default library) | various | no named-run of a setup they keep: copywriter / engenheiro-audiovisual / minerador-de-conteudo / social-media (@adamuchigabriel), 4-panez (@SuddenlyJon), austin-parent (@ChadWittman), clipmaker (@r40_io), nyc-parent + wholefoods (@DennisonBertram), theta-vantage-desk, researchy, chief-health, whatsapp-digest, steward, product-idea-stress-test, commercial-taste, grok-bot-knower, lina, grokart, patch, se-call-bot, review-this, workshop-facilitator, pulse, tech-lead, rewardsmaxxing, rentals, teslascope, raily, receipt-scanner-expense-tracking, alexis-grail-scout, situation-monitor, funhouse, agent-looper
bounce | unseen 80+ older catalog | Gaurav / RohOnChain / Teslaconomics / etc. | already seen 2026-08-26..29; not re-opened

## Fetch failures

- X MCP: failed_to_load (as briefed); did not use it.
- r.jina.ai: HTTP 403 on https://x.com/Jason/status/2094095953812717647, https://x.com/thekuchh/status/2094103773832737075, https://x.com/herdrdev/status/2094129284885467399.
- fxtwitter (api.fxtwitter.com): HTTP 200 with full tweet text for Jason, herdrdev (incl. quoted @theaaron), and all 9 thekuchh statuses listed above. Used those.
- grokbot.dev: curl -A Mozilla HTTP 200 on both use-case APIs+HTML, plugin API, 9 thekuchh template APIs+HTML, 6 glance template APIs. No urllib.
- thekuchh tweet 7: not in grokbot feed (numbering 1–6 then 8–10); not fetched.
- Did not open remaining 36 non-education template HTML pages (default library).
- Did not re-download feed (reused /tmp/grokbot-feed.json).

## Bank deposits made

Grep of /workspace/bank/INDEX.md was empty for these URLs, then:

- `2026-08-31-jason-calacanis-screen-your-x-replies-for-burners` · grok-bot · https://grokbot.dev/use-cases/reply-guard/
- `2026-08-31-jason-calacanis-made-a-killer-new-grok-bot` · grok-bot · https://x.com/Jason/status/2094095953812717647
- `2026-08-31-herdrdev-herd-your-whole-fleet-of-grok` · grok-bot · https://grokbot.dev/use-cases/herd-your-bots/
- `2026-08-31-herdrdev-shepherd-template-the-bot-that-herds` · grok-bot · https://x.com/herdrdev/status/2094129284885467399

Not banked: plugin table, 14 collections, thekuchh template catalog, glance templates (library, not named practice).

## Compiler notes (not a packet)

- Do not write packet files from this scratch. Do not edit field-seen.json.
- Education this grokbot window: 0. thekuchh is the only education-shaped delta and it is a shareable-bot dump.
- Portable gates only (one line each, not lead): Shepherd curator prompt = human-gate + quiet-when-nothing; Jason curator prompt = human-gate (but runner said auto-nuke — killed-claim that reconstructed approve-first is the live policy); X plugin prompt = never post without explicit yes.
- Both new use-case pages actually opened (quotes above). thekuchh cluster opened enough to call library vs practice.
