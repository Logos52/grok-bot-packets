---
id: 2026-09-05-george-burchell-grok-bot-0-39-0-on
kind: article
title: Grok Bot 0.39.0 on Windows — existing computer not reattached after sign-in; all Bots missing
source: "https://forum.cursor.com/t/grok-bot-0-39-0-on-windows-existing-computer-not-reattached-after-sign-in-all-bots-missing/170607"
author: George_Burchell
published: 2026-09-04
captured: 2026-09-05
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot 0.39.0 on Windows — existing computer not reattached after sign-in; all Bots missing

URL: https://forum.cursor.com/t/grok-bot-0-39-0-on-windows-existing-computer-not-reattached-after-sign-in-all-bots-missing/170607

Created: 2026-09-04T15:10:03.730Z

## Post 1 — @George_Burchell (2026-09-04T15:10:03.809Z)

Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Where does the bug appear?

Grok Bot desktop app on Windows

Description

My established Grok Bot installation suddenly began displaying:

“Can’t Reach Grok Bot’s Computer”

“A firewall, VPN, or proxy such as Zscaler may be blocking the connection”

“*.cursorvm.com”

After signing out and signing back into the same Cursor account, the app now remains on:

“Reconnecting to your computer… Retrying…”

It also says “No saved Bots yet.” All my existing Bots and their conversations appear to be missing.

I believe the Bots may still exist remotely, but the desktop application is no longer receiving the gateway/computer descriptor needed to reconnect to the previously assigned computer.

Environment

Windows 11, build 26200.9168 / 25H2
Grok Bot stable version 0.39.0
Cursor Privacy Mode is Active
Incident occurred September 4, 2026, approximately 16:48–16:54 CEST

Troubleshooting already completed

Fully quit and restarted Grok Bot
Signed out and signed back in
Verified locally that the account ID before and after signing in is identical
Confirmed Privacy Mode is Active in the Cursor dashboard
Restarted the application after changing/checking Privacy Mode
Confirmed the assigned *.us8.cursorvm.com hostname resolves using:

Default DNS
Cloudflare 1.1.1.1
Google 8.8.8.8

Confirmed TCP port 443 connects successfully
Confirmed HTTPS/TLS reaches the assigned host
Confirmed Windows is using a direct connection with no WinHTTP proxy
No active VPN/filter adapter was found
No hosts-file block was found
No Grok-specific Windows Firewall rule was found

Relevant local findings

Before signing out, the local Grok Bot data contained my Bot roster and saved messages.
Before signing out, gateway-descriptor.json existed.
Signing out cleared the local roster and gateway descriptor.
After signing back into the same account, gateway-descriptor.json has not been reissued.
After a clean restart, the local execution daemon does not start and the app does not attempt a connection to the previously assigned host.
The app exits cleanly and there is no crash dump or queued Sentry crash report.
The application updated from version 0.36.0 to 0.39.0 around this incident.

Requested resolution

Please check the backend association between my account and my existing Grok Bot computer, and reissue/restore its gateway descriptor so the existing computer and Bots can reconnect.

DATA-PRESERVATION REQUEST:

Please do not reset, recover, reprovision, replace, or recreate the computer/Bots without asking me first. They contain important conversations, files, logins, and established routines. I specifically need the existing environment reattached if possible.

I can privately provide the exact assigned cursorvm hostname and additional local diagnostic details to Cursor staff.

Steps to Reproduce

Open Grok Bot 0.39.0 on Windows 11.
Sign in using the same Cursor account previously associated with the existing Grok Bot computer.
Wait for the desktop application to load.
The application displays “Can’t reach your computer” and remains on “Retrying…”.
Click Retry. The connection still does not return.
Fully quit and reopen the application. The same problem remains.
Signing out and back into the same account also does not restore the connection.

The problem is consistently reproducible whenever Grok Bot is opened. I have not clicked “Recover computer” because it warns that installed applications and packages will be removed.

Expected Behavior
Grok Bot should reconnect to my existing computer and load all of my previously created Bots, conversations, files, logins, and routines.

The existing computer should be reattached without recovery, reprovisioning, or deletion of any installed applications, packages, or Bot data.

Screenshots / Screen Recordings
Screenshot 2026-09-04 163335.png690×647 16.9 KBScreenshot 2026-09-04 161400.png1910×1131 207 KBScreenshot 2026-09-04 170055.png1313×960 24.3 KB

Operating System
Windows 10/11

Version Information
Application: Grok Bot desktop

Grok Bot Version: 0.39.0 (Stable)

Operating System: Windows 11 25H2

OS Build: 26200.9168

Previous Grok Bot Version: 0.36.0

Additional Information
The application now explicitly says: “Your Bots are safe — they just can’t be loaded right now.” This indicates that the existing computer and Bots are still registered, but the application cannot connect to them.

Before signing out, local Grok Bot data contained my Bot roster, saved messages, and a gateway descriptor. After signing out and signing back into the same account, the gateway descriptor was not reissued.

Network checks succeeded: the assigned *.us8.cursorvm.com hostname resolves correctly, TCP port 443 is reachable, and HTTPS/TLS connects successfully. No proxy, active VPN/filter adapter, hosts-file block, or Grok-specific Windows Firewall rule was found.

Please check the backend association between my account and the existing Grok Bot computer and restore/reissue the gateway descriptor.

IMPORTANT DATA-PRESERVATION REQUEST: Please do not recover, reset, reprovision, replace, or recreate the computer without obtaining my approval first. It contains important Bots, conversations, files, logins, installed applications, packages, and established routines.

Does this stop you from using Cursor
No - Cursor works, but with this issue

## Post 5 — @Colin (2026-09-04T15:21:24.779Z)

Hi @George_Burchell

Can you restart Grok Box and see if the issue has been resolved?

## Post 6 — @George_Burchell (2026-09-04T15:24:47.771Z)

RESOLVED / WORKAROUND FOUND:

I installed the Grok Bot Android application and signed into the same account. The Android app asked whether I wanted to sync with my computer. After accepting, the Windows Grok Bot application reconnected and all of my existing Bots, messages, and routines returned intact.

I did not use “Recover computer,” reinstall the Windows application, or recreate any Bots.

This suggests that initiating computer sync from Android refreshed or restored the backend association/gateway descriptor for the existing computer.
