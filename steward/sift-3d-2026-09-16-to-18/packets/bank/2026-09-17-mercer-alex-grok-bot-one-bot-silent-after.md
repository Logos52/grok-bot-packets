---
id: 2026-09-17-mercer-alex-grok-bot-one-bot-silent-after
kind: article
title: "Grok Bot: one bot silent after image_gen — restart this bot's runner only, do NOT Reset"
source: "https://forum.cursor.com/t/grok-bot-one-bot-silent-after-image-gen-restart-this-bots-runner-only-do-not-reset/171840"
author: Mercer_Alex
published: 2026-09-16
captured: 2026-09-17
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot: one bot silent after image_gen — restart this bot's runner only, do NOT Reset
https://forum.cursor.com/t/grok-bot-one-bot-silent-after-image-gen-restart-this-bots-runner-only-do-not-reset/171840
Author: Mercer_Alex
Published: 2026-09-16

## USER @Mercer_Alex · 2026-09-16T09:25:52.207Z · #1
Describe the Bug One specific Grok Bot stopped responding after an image_gen / drawing tool call. Other bots on the same Agent Computer still work. This bot’s desktop is operable when I take over. Messages in this bot’s original conversation do not get a reply on desktop and mobile. “Stop now” also gets no reply. Sending in this conversation currently fails. This is NOT a weekly usage-limit case. SuperGrok Plus usage is still available. Please restart ONLY this bot’s runner. Do NOT Reset / rebuild / Update the Agent Computer. Do NOT delete the bot. Conversation history is extremely important and MUST remain on the original bot. Steps to Reproduce Open Grok Bot (desktop and mobile), SuperGrok Plus. Open bot: 世界でいっちばんかわいい愛ちゃん Conversation / Agent ID: e62dac71-7430-4632-aa38-122a861711f8 Bot was asked to draw a picture (image_gen / command, not a webpage). After that tool call, the bot never replied. Send “Stop now”, “hello”, or any short message in the same conversation. Result: no bot reply. On both desktop and mobile, messages in this conversation fail to send / never get a response. Take over this bot’s Agent Computer desktop: it is operable. Other bots on the same computer still reply normally. Duplicate of this bot can talk, but has no conversation history (expected). Original bot must be kept. Expected Behavior The original bot should reply again in the same conversation after the hung image_gen turn is cleared. Please restart only this bot’s runner so the original chat continues. Do not Reset / rebuild the Agent Computer. Do not delete the bot. Do not create a replacement computer. History must stay on the original bot. Operating System Windows 10/11 Version Information Grok Bot desktop Version：0.53.0 For AI issues: which model did you use? Grok Bot default (not Cursor Sonnet). Bot used image_gen / drawing tool, then went silent. For AI issues: add Request ID with privacy disabled Conversation / Agent ID: e62dac71-7430-4632-aa38-122a861711f8 No requestId on failed sends (messages do not complete). Additional Information Plan: SuperGrok Plus. Usage remaining: yes (checked in Grok Bot Settings → Usage). Not a quota issue. Bot name: 世界でいっちばんかわいい愛ちゃん Conversation / Agent ID: e62dac71-7430-4632-aa38-122a861711f8 Hard requirements: Restart this bot’s runner only Do NOT Reset / rebuild / Update the Agent Computer Do NOT delete the bot Conversation history MUST remain on the original bot Already tried with no fix: Stop now Short messages (hello) Take over computer (desktop works) Update Agent Computer (other bots still fine) New chat / group with this bot Duplicate bot (copy works but history is missing; original must be restored) Same failure on desktop and mobile. Does this stop you from using Cursor No - Cursor works, but with this issue

## USER @Mercer_Alex · 2026-09-16T10:17:42.002Z · #7
Thanks for restoring the account and the topic. Quick recap in case this got buried while the post was hidden: One bot stopped after an image_gen / drawing call. Other bots on the same computer still work, and I can take over this bot’s desktop. Usage is still available, so this doesn’t look like a weekly limit. Could you restart only this bot’s runner? Please don’t Reset or rebuild the Agent Computer, and please don’t delete the bot — the original conversation history needs to stay on it. Bot: 世界でいっちばんかわいい愛ちゃん ID: e62dac71-7430-4632-aa38-122a861711f8

## USER @Mercer_Alex · 2026-09-16T10:23:55.347Z · #8
Update: the original bot is responding again in the same conversation. History is still there. No further action needed — please don’t Reset or rebuild the Agent Computer. Thanks for restoring the topic earlier.

## STAFF @deanrie · 2026-09-16T10:39:09.534Z · #9
Hey, glad the bot is replying again and the history is still there. You don’t need to do anything else, and you were right not to run Reset since it really wasn’t needed in this case. Quick reason: the part that processes this bot’s replies runs on our side, not on the Agent Computer. That’s why the computer looked fine and other bots kept responding. Only the background step for this specific bot got stuck, and any messages after it got queued behind it. The chat history is stored on our side, so it never went anywhere. We’re tracking this issue. If this bot goes quiet again after a tool call, send the time of the last message and the bot ID here and I’ll take a look.

## STAFF @Colin · 2026-09-16T11:21:41.164Z · #10
2 posts were merged into an existing topic: Some of the bots became unresponsive (failed to send on my messages to them)
