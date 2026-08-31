# Field · latest

## Alert · 2026-08-30
Matt Segar: Anki build with Claude Code — escape HTML cutoffs, fact_key dedupe, score against held-out questions before trusting coverage. https://segar.me/blog/posts/anki_cards_claude_code.html · copy the QC gate this week

## Field packet · 2026-08-30

### SETUPS
- [education·generated-input·taste-gate·teach-once] score=10 | Matt Segar | Clinical EP boards. Built 468 notes / 1,386 Anki cards with Claude Code. First 52 imported "clean"; Anki HTML ate `<250 msec` cutoffs (invisible until review). Kept: escape `<`/`>` in packaging; `fact_key` (topic::parameter) so multi-source facts merge and flag numeric conflicts; grade deck against 50 held-out real questions (own review said good; questions said 56% + named holes); QC script as hard gate (`issues=0`); prose cards fail ~15× more than number cards ("therefore" giveaways). Agent loop vs chat paste is the mechanism. | https://segar.me/blog/posts/anki_cards_claude_code.html
  date: 2026-08-23
- [education·i-plus-one·generated-input] score=9 | brandonc7 / ReadPlusOne | Runs own Spanish mornings ~2 months. Generates stories ~95% known vocab + target words. Tap unknown → SRS into *future stories* (not a separate Anki deck). Nouns/adjectives → lemma; verbs keep tense/mood. Separate validator rejects drafts that leave known vocab; retry. Gate: graded readers labeled B1 vary wildly; Anki cards weren't stickier for him than story reappearance. | https://news.ycombinator.com/item?id=49433095
  date: 2026-08-26 · product https://readplusone.com/
- [education·generated-input] score=8 | Ibrahim Farah / SubSmith | Japanese learner years. Failure: hop video ↔ transcript ↔ dictionary ↔ screenshots ↔ audio ↔ Anki. Built desktop app: local Whisper on *your* files, edit timestamps, hover dict, one-click Anki with sliced audio + optional screenshot. Not streaming-tied. Asks whether account-before-trial is friction. Show HN ~71 pts. | https://news.ycombinator.com/item?id=49476894
  date: 2026-08-28 · product https://subsmith.app

### FAILURES
- [agentic·coverage-ceiling·killed-claim] score=10 | Ber77 | Bot templates: preview shows skill under Context → Skills (full body). Publish + Add to Grok Bot: imported manifest has `"skills": []`. Instructions, memories, routines, plugins arrive; skill never lands (manifest, Plugins → Yours, SKILL.md, / menu). Own round-trip + two third-party templates. Share page has no skill copy path. Grok Bot 0.30.0 Windows. Preview ≠ delivered. | https://forum.cursor.com/t/grok-bot-templates-preview-shows-skills-but-the-export-ships-skills-skills-are-never-delivered/169911
  date: 2026-08-29 13:39 UTC (20:39 ICT 29 Aug)
- [agentic·coverage-ceiling·killed-claim] score=10 | Jake Sun | Settings → Computer shows Mac connected, Always allow; ListMachines sometimes {connected:true}. Same turn: "no registered machines when turn started." Shell can succeed once, then disconnected; CopyFromBox never worked even after a good Shell. Staff (Dean Rie): timeout removes machine from roster ~1 min; machine set fixed at turn start. Settings green ≠ usable this turn. Wait ~1 min; if stuck Cmd+Q + `pkill -f local-exec-daemon`. | https://forum.cursor.com/t/grok-bot-local-computer-execution-looks-connected-in-settings-but-is-not-actually-usable-for-file-i-o/169877
  date: 2026-08-29 02:36 UTC (09:36 ICT 29 Aug)

### KILLED
- import-clean means the cards are safe · Matt Segar: Anki HTML ate `<250 msec` cutoffs; escape in packaging; score against held-out questions · https://segar.me/blog/posts/anki_cards_claude_code.html
- graded-reader level label means matched input · brandonc7: B1 labels vary wildly; validate drafts against *your* known vocab · https://news.ycombinator.com/item?id=49433095
- template preview skills will arrive on import · Ber77: preview shows skill; export ships `"skills": []`; no copy path on share page · https://forum.cursor.com/t/grok-bot-templates-preview-shows-skills-but-the-export-ships-skills-skills-are-never-delivered/169911
- Settings "connected" / one good Shell means local I/O works · Jake + Dean: timeout drops machine from roster ~1 min; CopyFromBox can fail while Shell just succeeded · https://forum.cursor.com/t/grok-bot-local-computer-execution-looks-connected-in-settings-but-is-not-actually-usable-for-file-i-o/169877

### Footer
Education this window: 3 (Segar, ReadPlusOne, SubSmith). Packet 13:0; 14:1; 15:1; 16:0; empty streak broken.
3 setups + 2 failures (cap 5). Newest kept: Ber77 / Jake 2026-08-29 — inside 5 days, no stale-sweep canary.
Packet 17 revised after background education+failure sweeps (first draft had education 0 + install siblings; replaced).
grokbot.dev: sixth sweep. RSS lastBuild 2026-08-29 23:23 UTC (06:23 ICT 30 Aug). New calendar delta: topic-to-branded-carousel (✦72, ContentDrips — human-gate before publish, off-lane), PostOnce / ContentDrips / BulkPublish plugins (library), templates news (Brief). Unseen 80+ haul is older catalog Aug 18–22 (Avid mine-machine ✦91, nyk one-prompt team ✦88, Robin coach ✦81, Avi masterclass ✦81) — out of freshness window for lead; bounce. No new in-window 80+ practice to lead.

X still dead for pin timelines. Education SEARCH + HN produced the three keeps above.
Bounce: jsolly Always-allow Details shows literal `[3397 chars omitted]` (human-gate sibling | cannot fully read what you approve) https://forum.cursor.com/t/grok-bot-always-allow-card-shows-literal-3397-chars-omitted-in-details/169902; Biniam desktop black/empty while iOS bots live (install/network sibling | staff: recreate computer will not help; hotspot/DNS) https://forum.cursor.com/t/grok-bot-desktop-never-joins-existing-ios-bots-latest-app-stuck-on-black-screen/169940; Russ chat-up / local hook never registers (Jake sibling) https://forum.cursor.com/t/grok-bot-cannot-access-my-local-computer/169924; Mike8 Phantom reauth mints new default address (crypto off-lane) https://forum.cursor.com/t/phantom-in-grok-bot-is-a-mess/169930; David Stredansky Cloud Agents missing in Cursor list until opened (feature gap) https://forum.cursor.com/t/cloud-agents-created-in-grok-bot-not-displayed-in-cursor/169939; topic-to-branded-carousel (gate | ContentDrips, ✦72) https://grokbot.dev/use-cases/topic-to-branded-carousel/; PostOnce / ContentDrips / BulkPublish plugins (library); grok-bot-templates-explained (Brief | product news) https://grokbot.dev/news/grok-bot-templates-explained/; Avid/nyk/Robin/Avi Aug 18–22 80+ (out of window); Yun-Ta Tsai paper→animation ✦66 (glance only); Pocket Linguist / Darwesh / Ryan Ahamer / Robert Machinezoo (seen or out of window).
Fetch failures: X pin timelines; urllib 403 on grokbot (curl OK). Truncated: remaining unseen RSS plugins and older usecase rail.
Retire signal: education counts recent — 13:0, 14:1, 15:1, 16:0, 17:3. Empty streak broken. Retire: no.
