---
id: 2026-09-11-reinerkuestner-grok-bot-macos-initial-setup-fails
kind: article
title: "Grok Bot macOS: Initial setup fails – Agent Computer unreachable (Bot name >255 costume)"
source: "https://forum.cursor.com/t/grok-bot-macos-initial-setup-fails-agent-computer-unreachable/171270"
author: ReinerKuestner
published: 2026-09-10
captured: 2026-09-11
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot macOS: Initial setup fails – Agent Computer unreachable (Bot name >255 costume)
Source: https://forum.cursor.com/t/grok-bot-macos-initial-setup-fails-agent-computer-unreachable/171270
Author: ReinerKuestner
Published: 2026-09-10

## @ReinerKuestner 2026-09-10T17:13:34

Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Grok Bot cannot finish the initial setup on my Mac.

Error:

“Grok Bot couldn’t finish setting up. Can’t reach your computer right now.”

I have already:

fully quit and restarted Grok Bot

reinstalled the Grok Bot app

tested with my iPhone Personal Hotspot

confirmed normal internet connectivity

confirmed that us8.cursorvm.com is reachable via curl

Curl returns:

HTTP/1.1 404 Not Found

Server: awselb/2.0

Settings cannot be opened, so I cannot use Recover Agent Computer or Update Agent Computer.

The issue persists after reinstalling.

Cursor Status is also currently showing a service degradation affecting Cloud Agents. I’m not sure whether this is related to my issue.

Could you please check whether the Agent Computer assigned to my account is stuck and recover/rebuild it on the backend if necessary?

macOS: Tahoe 26.5.2

Grok Bot version: 0.47.0

Steps to Reproduce
Install and launch Grok Bot on macOS.

Sign in with my Cursor account.

Start the initial Grok Bot setup/onboarding.

Wait while Grok Bot tries to set up the Agent Computer.

The setup fails with the message:

“Grok Bot couldn’t finish setting up. Can’t reach your computer right now.”

Click Try Again — the same error appears again.

Attempt to open Settings — Settings do not open.

Reinstall Grok Bot and repeat the setup — the same error still occurs.

Network connectivity is working normally.

Tested via iPhone Personal Hotspot.

curl -I https://us8.cursorvm.com returns HTTP/1.1 404 Not Found, confirming the server is reachable.

Operating System
MacOS

Version Information
Grok Bot for macOS – Version 0.47.0

Does this stop you from using Cursor
Yes - Cursor is unusable

## @kevinn 2026-09-10T17:46:13 [STAFF]

Hi @ReinerKuestner  thanks for the detailed report, and sorry for the trouble.

Good news first: your Agent Computer is healthy and reachable, and the status page entry you saw is unrelated to this. What is failing is the very last step of setup, creating your first Bot. That step currently rejects a Bot name longer than 255 characters, and the setup screen unfortunately reports that as a connection problem.

Could you try this:

- Quit Grok Bot completely (Grok Bot menu, then Quit Grok Bot).
- Open Grok Bot again and sign in. Setup starts over from the beginning.
- When you reach the “Create your first Bot” screen, type only a short name into the Name field, for example “Assistant” (a few words at most).
- Click the create button.

Once the Bot exists, send it your full instructions as the first chat message. That is where longer text belongs. If setup still fails with a short name, reply here and I will dig further. An update that caps the name automatically is also on the way.
