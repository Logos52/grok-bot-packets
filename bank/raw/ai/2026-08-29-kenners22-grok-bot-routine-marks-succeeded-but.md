---
id: 2026-08-29-kenners22-grok-bot-routine-marks-succeeded-but
kind: article
title: Grok Bot routine marks succeeded but never posts a chat bubble
source: "https://forum.cursor.com/t/grok-bot-routine-marks-succeeded-but-never-posts-a-chat-bubble/169841"
author: kenners22
published: 2026-08-28
captured: 2026-08-29
via: grok-bot/Field
lane: ai
status: raw
private: false
---

I hit a Grok Bot routine bug. A scheduled routine can mark succeeded and still never show a message in the agent chat. The work ran. Status is ok. I get no chat bubble. From my side it looks like the routine never ran.

The prompt already said the agent has to message me in that chat, even if there's nothing new, and not finish a run with no message.

What I saw:
- The scheduler fired on time
- Status was ok
- Internal notes were updated
- No chat bubble. The agent later confirmed it never sent one. There was no visible routine wake in the chat. A brief only showed up later as a hidden completion payload, not a visible message.

Other due routines that morning also fired and marked ok. The clocks work. This is a delivery bug, not a missed cron.

A stay-quiet-if-nothing routine plus a hidden completion looks the same as a dead routine. Don't treat hidden completion as something I actually saw.

Please fix:
1. If the prompt says I should get a message, the routine wake has to show in the agent chat, not only as hidden completion.
2. status=ok should mean that message was sent when the prompt requires one.
3. Reading run status alone can't tell a silent-success from a real pass.

I need routines to actually talk to me.
Grok Bot Version 0.29.0, MacOS. One-post thread, no staff reply as of fetch.
