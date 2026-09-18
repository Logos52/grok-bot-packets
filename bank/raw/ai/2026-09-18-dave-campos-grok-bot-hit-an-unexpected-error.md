---
id: 2026-09-18-dave-campos-grok-bot-hit-an-unexpected-error
kind: article
title: Grok Bot hit an unexpected error
source: "https://forum.cursor.com/t/grok-bot-hit-an-unexpected-error/172070"
author: Dave_Campos
published: 2026-09-17
captured: 2026-09-18
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot hit an unexpected error
URL: https://forum.cursor.com/t/grok-bot-hit-an-unexpected-error/172070
Created: 2026-09-17T19:19:25.745Z

--- @Dave_Campos 2026-09-17T19:19:25.778Z ---
Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
I cannot communicate with my Grok Bot COS agent. The screen on Grokbot ios app says “Grok Bot hit an unexpected error” then “ Try again”.

It has been like this for almost 20 hours. I updated the Bot computer but that didnt help.

I can communicate w another agent on my staff and it says it can communicate with my COS agent.

Steps to Reproduce
Log into my ios app and tap on the agent icon.

Expected Behavior
I should be able to see my COS agent chats.

Screenshots / Screen Recordings
IMG_8386.png1125×2436 76.9 KB

Operating System
iOS

Version Information
Grok Bot 1.10.0 (9930)

For AI issues: which model did you use?
Grok Bot

Does this stop you from using Cursor
No - Cursor works, but with this issue

--- @kevinn 2026-09-17T20:46:35.923Z ---
Hey @Dave_Campos, thanks for the report, and sorry about this one. What you are seeing is an issue in the iOS app itself, not your Bot computer, which is why updating the computer did not change anything. When a chat contains a particular pattern of messages, the current App Store build of the iOS app fails to draw that chat and shows the “Grok Bot hit an unexpected error” screen. Your COS agent is fine on our side (it is still running and finishing its work, which is also why your other agent can reach it).

A fix for the app is already in the next iOS release, which is in testing now, so please install the App Store update when it appears.

In the meantime, two things that work today:

The Grok Bot desktop app (Mac or Windows) opens this chat normally, so you can read and message your COS agent from there.
Keep relaying through your other agent, as you have been doing.
