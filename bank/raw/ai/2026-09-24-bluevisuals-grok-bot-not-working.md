---
id: 2026-09-24-bluevisuals-grok-bot-not-working
kind: article
title: Grok bot not working
source: "https://forum.cursor.com/t/grok-bot-not-working/172529"
author: Bluevisuals
published: 2026-09-21
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok bot not working
URL: https://forum.cursor.com/t/grok-bot-not-working/172529
Created: 2026-09-21T16:26:03.024Z

## Post #1 @Bluevisuals (2026-09-21T16:26:03.054Z)
I am not able to use grok bot it says cant reach your ocmputer i tried to reinstall it restart my pc and even waited an day for it but i am not able ot use it please help me i am using windows image 238×114 1.6 KB

## Post #2 @deanrie (2026-09-24T08:06:15.426Z)
Hey, thanks for the report. Good news: on our side, your Grok Bot computer is online, and the bot, files, and logins look fine. Your PC is reaching our servers normally, but the network you’re on can’t resolve your computer’s address via DNS lookup. That lookup happens on your network, not in the app. That’s why Grok Bot shows “Can’t reach your computer”. Reinstalling, restarting the PC, or using Reset won’t change this, so no need to hit Reset again. It looks like the app connected shortly after you posted, right when the network changed. If it’s working now, you’re all set. If the issue comes back, try these steps in order: Open Windows Settings &gt; Network and internet, choose your active connection Wi-Fi or Ethernet, then next to DNS server assignment click Edit. Switch to Manual, enable IPv4, set 1.1.1.1 as Preferred DNS and 8.8.8.8 as Alternate DNS, then Save. Open Command Prompt and run ipconfig /flushdns . Fully quit Grok Bot right click the tray icon &gt; Quit, then open it again. If it still says “Can’t reach your computer”, connect your PC to a different network for a minute, like a phone hotspot, and check if it connects there. Let me know how it goes. If step 5 works on the other network but not on your normal one, tell me your ISP and router model and we’ll dig in.
