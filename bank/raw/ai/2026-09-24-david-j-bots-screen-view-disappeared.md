---
id: 2026-09-24-david-j-bots-screen-view-disappeared
kind: article
title: Bot's screen view disappeared
source: "https://forum.cursor.com/t/bots-screen-view-disappeared/172836"
author: David.J
published: 2026-09-23
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Bot's screen view disappeared
URL: https://forum.cursor.com/t/bots-screen-view-disappeared/172836
Created: 2026-09-23T23:57:04.754Z

## Post #1 @David.J (2026-09-23T23:57:04.785Z)
Where does the bug appear (feature/product)? Grok Bot Describe the Bug On macOS, Grok Bot 0.58.0, bots screen view disappeared. Can’t preview the screen anymore, as well as click on it to access the bot screen view. I could probably prompt, but then it would spend usage. Steps to Reproduce Open a bot → top right corner → option not showing anymore. Operating System MacOS Version Information Grok Bot 0.58.0 Does this stop you from using Cursor No - Cursor works, but with this issue

## Post #2 @kevinn (2026-09-24T00:44:37.252Z)
Hey @David.J , thanks for the report! The screen view moved rather than went away. In 0.58.0, the separate computer button in the top right was folded into the Bot’s name at the top center of the chat. To get back to it: Open the Bot’s chat. Click the Bot’s name at the top center of the window. A panel opens on the right showing the Bot’s settings. Click the back arrow (“Back to details”) at the top left of that panel. The live screen preview is at the top of the panel. Click it to open the full computer view. You can also toggle that panel with Cmd+Shift+I .

## Post #3 @David.J (2026-09-24T01:12:23.652Z)
Hi @kevinn I just found out actually and I was about to update that post, haha. Thank you! (we can close the thread)
