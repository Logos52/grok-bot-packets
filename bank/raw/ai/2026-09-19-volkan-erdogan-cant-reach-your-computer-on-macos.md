---
id: 2026-09-19-volkan-erdogan-cant-reach-your-computer-on-macos
kind: article
title: "\"Can't reach your computer\" on macOS - Recover and Reset both fail at 50%"
source: "https://forum.cursor.com/t/cant-reach-your-computer-on-macos-recover-and-reset-both-fail-at-50/172135"
author: Volkan_Erdogan / deanrie
published: 2026-09-18
captured: 2026-09-19
via: grok-bot/Field
lane: ai
status: raw
private: false
---

Title: "Can't reach your computer" on macOS - Recover and Reset both fail at 50%
URL: https://forum.cursor.com/t/cant-reach-your-computer-on-macos-recover-and-reset-both-fail-at-50/172135
Created: 2026-09-18T11:11:50.206Z

--- USER @Volkan_Erdogan (Volkan Erdogan) #1 2026-09-18T11:11:50.237Z ---
Where does the bug appear (feature/product)?

Grok Bot

Describe the Bug

The agent computer never becomes reachable. Banner reads “Can’t reach your computer.” Recover and Reset both fail server-side at the identical stage — “Starting Grok Bot’s computer,” stuck at 50% — then error out. Reset wipes data before failing, so retrying is destructive with no chance of success.

Chat with the Bot works normally throughout, so the app’s connection to Cursor’s servers is fine. Only the VM fails to start.

Ruled out locally:

DNS: dig +short NS cursorvm.com resolves normally; switched to 1.1.1.1/8.8.8.8 (confirmed via scutil --dns) and flushed cache — no change

Different networks: personal hotspot (different carrier/DNS) and VPN — no change

Account: Pro, not an expired trial

Privacy: Share Data explicitly turned off and saved on dashboard

Steps to Reproduce

Launch Grok Bot, Pro account. Banner: “Can’t reach your computer.”

Run Recover → stalls at “Starting Grok Bot’s computer,” 50% → “Recovery couldn’t finish.”

Run Reset → wipes data, creates computer, stalls at same step, 50% → “Reset couldn’t finish. Computer may be in a partial state.”

Expected Behavior

Recover or Reset provisions a working agent computer the app can reach.

Screenshots / Screen Recordings

Screenshot 2026-09-18 at 13.53.31.png471×179 6.42 KBScreenshot 2026-09-18 at 13.54.21.png490×188 10.3 KBScreenshot 2026-09-18 at 13.53.49.png1029×751 76.3 KB

Operating System

MacOS

Version Information

Grok Bot 0.56.1

For AI issues: which model did you use?

N/A - fails before any model request.

For AI issues: add Request ID with privacy disabled

N/A - no request issued; provisioning fails first.

Additional Information

Account: vlk34vlk34@gmail.com (@volkanjs)

Does this stop you from using Cursor

No - Cursor works, but with this issue

--- STAFF @deanrie (Dean Rie) #5 2026-09-18T11:39:50.627Z ---
Hey, thanks for the detailed report, and for ruling out DNS, network, hotspot, VPN, and privacy upfront. You were looking in the right direction. This isn’t on your Mac or in your setup.

What’s happening is that your Grok Bot computer never finished the very first initialization, so Recover and Reset can’t complete from the app. They both get stuck on the same server-side step. There’s nothing you can do on your side to change this, so for now please don’t run Reset again. It won’t finish anyway.

This is a known issue we’re tracking, and it needs to be fixed on our side. I’ve passed your case to the team to investigate.

Your account and the chat you already created with the bot are safe. The chat runs on our servers, which is why it can keep replying while the computer is unavailable.

Once I have an update on your computer, We’ll reply here. After that, you’ll just need to fully quit Grok Bot menu bar icon → Quit and open it again.
