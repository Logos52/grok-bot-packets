---
id: 2026-09-12-thomas2018-desktop-grok-bot-webhook-routine-shows
kind: article
title: Desktop Grok Bot webhook routine shows no POST URL / crsr_ key (Windows 0.47.0)
source: "https://forum.cursor.com/t/desktop-grok-bot-webhook-routine-shows-no-post-url-crsr-key-windows-0-47-0/171324"
author: thomas2018
published: 2026-09-11
captured: 2026-09-12
via: grok-bot/Field
lane: ai
status: raw
private: false
---

Title: Desktop Grok Bot webhook routine shows no POST URL / crsr_ key (Windows 0.47.0)
URL: https://forum.cursor.com/t/desktop-grok-bot-webhook-routine-shows-no-post-url-crsr-key-windows-0-47-0/171324
Created: 2026-09-11T08:16:43.348Z
Author: thomas2018

--- @thomas2018 | 2026-09-11T08:16:43.413Z ---
Where does the bug appear (feature/product)? Grok Bot Describe the Bug I created a webhook-triggered routine via the Bot. Opening the routine details on Windows desktop only shows: Enabled toggle, Instructions, “When a webhook fires”, empty run history. There is no gray box with the three click-to-copy fields (POST to URL, Secret crsr_…, Authorization header). Deep links for webhook-url/key/header also do not surface credentials. I am not on iOS—this is desktop 0.47.0. Recreating the routine does not help. The Bot cannot see or emit the URL/key, so external callers cannot use the webhook. Related: Webhook url missing on ios says credentials are desktop-only, but desktop still lacks the fields here. Also filed in-app feedback requesting a reply. Steps to Reproduce Ask a Grok Bot to create a routine with webhook trigger type webhook. On Windows desktop Grok Bot, open agent → Routines → that routine. Observe trigger text only; no POST URL / crsr_ / Authorization fields. Expected Behavior Desktop trigger card shows POST URL, sender key, and Authorization header for copy. Operating System Windows 10/11 Version Information 0.47.0 x64 Additional Information Suspected Bot-created webhook routines may not provision credentials to the client so the UI block never mounts. Does this stop you from using Cursor No - Cursor works, but with this issue

--- @deanrie [CursorStaff] | 2026-09-11T09:30:19.292Z ---
Hey, thanks for the detailed report and the link to the iOS thread. You’re right, those fields are actually missing, and it’s not something on your end. New bots store their routines on the server (that’s the note saying “This Bot keeps its routines on the server” in the routine panel), and for these routines the desktop app currently doesn’t fetch or show the webhook URL, key, or Authorization header. Recreating the routine doesn’t change this, and the bot itself can’t provide those values either, so deep links open an empty panel. This is a known issue we’re already tracking, and I’ve added your report to it. Unfortunately, there’s no way to get the URL or key for this kind of routine right now. As a temporary workaround, if you need to wake the bot from something external, Slack message triggers work right now (ask the bot to create a routine that runs when a message is posted in a channel you control) or you can use a schedule. I’ll reply here when there’s an update.
