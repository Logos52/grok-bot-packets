---
id: 2026-09-24-palan-grok-bot-0-55-0-reset
kind: article
title: Grok Bot 0.55.0 — Reset/Recover failed
source: "https://forum.cursor.com/t/grok-bot-0-55-0-reset-recover-failed/171969"
author: Palan
published: 2026-09-17
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot 0.55.0 — Reset/Recover failed
URL: https://forum.cursor.com/t/grok-bot-0-55-0-reset-recover-failed/171969
Created: 2026-09-17T06:32:56.889Z

## Post #1 @Palan (2026-09-17T06:32:56.919Z)
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Hi Cursor team, Grok Bot on Windows cannot connect to my Agent Computer. Reset and Recover both fail in the app. Please check and restore the existing cloud computer without deleting my Bots, files, or logins. Environment App: Grok Bot 0.55.0 (Windows) OS: Windows 11 (10.0.26200) Account is signed in Bots are still visible in the app What I see in the app Reset failed: “The reset couldn’t finish. Grok Bot’s computer may be in a partial state — retry to run the reset again.” Recover failed: “The recovery couldn’t finish, so Grok Bot’s computer may still be unreachable. Your Bots, files, and logins are safe.” Steps to Reproduce Open Grok Bot 0.55.0 on Windows 11 and sign in. The app cannot reach Grok Bot’s Computer. Reset and Recover both fail. Fully quit Grok Bot (all processes in Task Manager) and relaunch. The computer is still unreachable. Retry Reset and Recover. Both fail with the same errors. Expected Behavior Grok Bot should reconnect to the existing cloud computer. If Reset/Recover is needed, it should finish and restore the same Bots, files, and logins. It should not stay in a partial/unroutable state. Screenshots / Screen Recordings Screenshot 2026-09-17 134421.png 527×187 7.61 KB Screenshot 2026-09-17 134728.png 546×190 7.63 KB Operating System Windows 10/11 Version Information Grok Bot 0.55.0 (Windows 11, 10.0.26200) For AI issues: which model did you use? N/A — this is a Grok Bot cloud computer connection failure, not a model response issue. For AI issues: add Request ID with privacy disabled N/A — no model Request ID. This is a Grok Bot Agent Computer / Reset / Recover failure. Does this stop you from using Cursor No - Cursor works, but with this issue

## Post #2 @mohitjain (2026-09-17T07:21:26.138Z)
Hey @Palan , thanks for the report, and sorry about this. Your Bots, files, and logins are safe - your computer is healthy on our side. The problem is that your network can’t look up the computer’s address (a hostname under cursorvm.com ), even though cursor.com loads fine. So please stop pressing Reset/Recover for now (each press just rebuilds it without helping). Fix on Windows: Settings &gt; Network &amp; internet &gt; your active Wi-Fi/Ethernet &gt; Hardware properties &gt; DNS server assignment &gt; Edit &gt; Manual &gt; turn on IPv4 &gt; Preferred 1.1.1.1 , Alternate 8.8.8.8 &gt; Save. Open PowerShell and run ipconfig /flushdns . Quit Grok Bot from the system tray, wait about a minute, reopen, and send “hello” to a Bot. Quick way to confirm it’s the network: open Grok Bot on your phone on mobile data, or put the PC on a phone hotspot - if it connects there, it’s the DNS on your main connection. Reply here if it still won’t connect after the DNS change and I’ll dig in further.

## Post #3 @Palan (2026-09-18T01:15:27.508Z)
Hi, I tried the way you suggested and still face the problem. Is that any others way to fix it? image 672×542 12.8 KB

## Post #4 @Daniel_Liversidge (2026-09-18T02:23:23.174Z)
Hi Support, I’m experiencing a similar issue: all my Grok Bots fail to respond, and my routines are not running. I have already: Restarted Grok Bot. Used “Reset Grok Bot’s Computer”. Tested again with a simple new message. The issue persists after these steps. I saw the advice above about DNS, but I haven’t confirmed whether that is the cause in my case. Could you please investigate my account’s Agent Computer and advise whether this is a connection issue or requires server-side recovery? If recovery or rebuilding is necessary, please preserve my existing Bots, chats, files and logins, and confirm before taking any action that could delete data. Please let me know what diagnostic information you need. Thanks, Daniel

## Post #5 @Palan (2026-09-21T05:46:29.340Z)
Update (Sep 21, 2026) The issue is still present after a full local wipe, reinstall, and additional local repair. What I already did locally Fully uninstalled Grok Bot and deleted local app data, including: AppData\Roaming\Grok Bot C:\Users\User\.grokbot config/daemon files updater leftovers Reinstalled Grok Bot 0.55.0 on Windows 11 (now installed at C:\Program Files\Grok Bot ) Signed back in Fixed local .grokbot folder permissions ( EPERM on daemon discovery) Cleared stale local-exec daemon files and relaunched the app Tried your DNS and WIFI fix The Windows client now launches and stays signed in. Local API access is fine. Current client errors after reinstall sand.box_reachability : outcome=network , cause=ControlPortCallError , methods listAgents / events / getHostSettings / setBoxSecrets base_url_kind=unknown sand.box_secrets.push : outcome=failed , error_class=host_unreachable sand.desktop.edge_failed : ConnectError.Internal ( box-host / host-settings ) sand.box_migration_watch : phase=dropped , error_class=Internal , consecutive failures &gt; 1000 Cloud computer endpoints are still dead Cluster: us9.cursorvm.com These hosts still return: HTTP/1.1 404 Not Found Server: awselb/2.0 The request could not be routed Request This is not a local install/config problem. Please restore or rebind this account’s Grok Bot Agent Computer on the backend so it routes again on us9.cursorvm.com . Please preserve existing Bots, files, and logins. Local Reset/Recover and reinstall cannot fix this while ELB returns “The request could not be routed.”

## Post #6 @mohitjain (2026-09-24T10:13:24.071Z)
@Palan your computer is healthy again on our side and all your Bots, files, and logins are intact. It was rebuilt on a new address, and the “could not be routed” error was your desktop still pointing at the old one. That part is resolved on our end. To reconnect: fully quit Grok Bot (tray icon &gt; Quit, then end any leftover Grok Bot processes in Task Manager), wait a minute, reopen, and message a Bot. If it still says “could not be routed” after that, reply here and I’ll rebind it from our side. @Daniel_Liversidge checked yours too. Your computer is asleep on our side with no errors recorded against it, and your Bots, files, and logins are stored separately from the computer, so they stay safe even if it needs rebuilding. Fully quit Grok Bot the same way, reopen, and message a Bot to wake it. If your Bots still don’t respond after that, reply here and I’ll rebuild your computer from our side.
