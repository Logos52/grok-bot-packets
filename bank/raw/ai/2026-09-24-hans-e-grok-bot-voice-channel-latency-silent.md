---
id: 2026-09-24-hans-e-grok-bot-voice-channel-latency-silent
kind: article
title: Grok Bot Voice channel latency / silent hang after tools complete
source: "https://forum.cursor.com/t/grok-bot-voice-channel-latency-silent-hang-after-tools-complete/172844"
author: Hans_E
published: 2026-09-24
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot Voice channel latency / silent hang after tools complete
URL: https://forum.cursor.com/t/grok-bot-voice-channel-latency-silent-hang-after-tools-complete/172844
Created: 2026-09-24T02:29:18.580Z

## Post #1 @Hans_E (2026-09-24T02:29:18.611Z)
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Bug report — Grok Bot Voice channel latency / silent hang Product: Grok Bot (desktop) — Voice calls Severity: High (call feels stuck; user ends call thinking nothing happened) Frequency: Ongoing since Voice launch; reproduced again Wed Sep 23, 2026 ~9:18–9:28 PM ET Summary On a voice call, the assistant completes work (Notion reads/writes, routine updates) but spoken/text replies on the voice channel arrive late or appear not to arrive. From the caller’s side the call hangs for several minutes on tasks that should take ~30–60 seconds. User ends the call and later finds the work already done. What happened tonight (timeline, America/New_York) ~9:18 PM — Voice call: find Writing Voice Style Guide + Content Calendar in Notion; wire into weekly Fathom pipeline. Draft + approve an X post (“Test before you launch”). Approved post: add to Clear Story Labs Content Calendar in Notion (calendar entry only). Notion page create succeeded (page id 3e52f70e-3252-81a1-be70-f82892a74062). Assistant also re-fetched and SQL-queried the Content Calendar and confirmed the row: Topic “Test before you launch”, Status Not started, Tags Twitter, Suggested publish date 2026-09-24. Caller still saw no progress on the call for several minutes (~almost 10), ended the call, and could not find the row (likely looking at filtered “In Progress” view; entry is Not started). After call closed, catch-up in chat confirmed the entry existed all along. Expected Voice channel returns a clear result within seconds of the tool completing (or a fast “working…” then the result). Caller should not have to end the call to learn whether the action succeeded. Actual Long silence / pending feel on voice while backend work already finished. Repeated “is it done?” prompts from the call side. Caller loses trust that the action ran. Impact Wastes call time Causes abandoned calls User thinks jobs failed when they succeeded Forces re-verification loops that make the lag worse Ask Please investigate voice inbound → agent reply delivery latency (and any queueing/ack gaps) so spoken answers don’t stall after tools return. Happy to share call id if useful: voice:call-995d68f1-57c2-4f46-bb40-965ff2ed39b7 Steps to Reproduce Start a voice call. Ask the assistant to find the Writing Voice Style Guide and Content Calendar in Notion and wire them into the weekly Fathom pipeline. Draft and approve an X post, then add it to the Clear Story Labs Content Calendar in Notion. Observe that the Notion page creation and follow-up reads/SQL query complete, but the voice call provides no progress or result for several minutes; end the call and verify later in chat that the work succeeded. Operating System Other Version Information Grok Bot desktop — Voice calls; exact version not provided Does this stop you from using Cursor No - Cursor works, but with this issue

## Post #2 @mohitjain (2026-09-24T06:37:27.361Z)
Hey @Hans_E ! Every task on that call actually completed on our side within seconds, including the Content Calendar entry (“Test before you launch”, Not started, publish 2026-09-24). Nothing failed. What lagged was getting the spoken result back into the call, and that mostly happened while the app was in the background (for example, when you switched over to Notion to check). The call also looks like it came from the Grok Bot iPhone app, where spoken results can stall if the app is backgrounded or the screen locks. Two things that help: keep the app in the foreground with the screen on while you wait, and update it from the App Store when a newer version is available (a recent update improves how results are delivered while the phone is locked or backgrounded). This is an issue we’re tracking. If you get a chance, try keeping the app foregrounded on your next call and let me know whether the result comes through promptly.

## Post #3 @Hans_E (2026-09-24T17:58:28.444Z)
Thanks for this! In case it helps, the app was always in the foreground. I was actually staring at it most of the time while I was walking. Only once or twice during the several minutes did I switch over to Notion just to see if the entry had been made. If it hadn’t, I queried the bot for an update, and it would just assure me that it’s still working on it, etc. Sounds like you guys are on it, but thought I would just add that nuance in case it rules anything out.
