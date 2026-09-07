---
id: 2026-09-05-jumpsuitgroup-grokbot-failing-to-connect-to-cloud
kind: article
title: Grokbot failing to connect to cloud agent
source: "https://forum.cursor.com/t/grokbot-failing-to-connect-to-cloud-agent/170486"
author: jumpsuitgroup
published: 2026-09-03
captured: 2026-09-05
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grokbot failing to connect to cloud agent

URL: https://forum.cursor.com/t/grokbot-failing-to-connect-to-cloud-agent/170486

Created: 2026-09-03T16:19:04.852Z

## Post 1 — @jumpsuitgroup (2026-09-03T16:19:04.914Z)

Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Environment:

macOS, Cursor Desktop (latest)

Grok Bot desktop app

Repo: private GitHub repo (JSG CMS)

Issue: When I ask Grok Bot to launch a Cloud Agent, it fails with:

“Cloud agents are not supported in Privacy Mode (Legacy).”

However, my Privacy Settings are set to the current Privacy Mode (not Legacy). The setting reads: “Privacy Mode — Active — No training. Code may be stored for Cloud Agent, Team Rules, and other features.” (screenshot attached).

Key finding: Launching a Cloud Agent from Cursor Desktop (Cloud dropdown) works perfectly on the same account, same repo, same moment. Only the Grok Bot launch path is broken.

Steps to reproduce:

Confirm Privacy Mode is set to current (not Legacy) in Cursor Settings → Privacy

Launch a Cloud Agent from Cursor Desktop → works

Ask Grok Bot to launch a Cloud Agent on the same repo → fails with “Privacy Mode (Legacy)” error

Expected behavior: Grok Bot should read the current privacy setting and launch the Cloud Agent successfully, the same as Cursor Desktop does.

Likely cause: Grok Bot appears to be reading a stale or incorrect privacy mode flag for my account. Signing out/in and toggling the privacy setting did not resolve it.

Steps to Reproduce
try making a grokbot > cursor cloud connection - CleanShot 2026-09-03 at 12.17.23 · CleanShot Cloud

Expected Behavior
trying to have grokbot run a cloud agent in cursor.

Screenshots / Screen Recordings
CleanShot 2026-09-03 at 12.15.40@2x.png1602×8070 1.52 MB

Operating System
MacOS

Version Information
Environment:

macOS, Cursor Desktop (latest)

Grok Bot desktop app

Repo: private GitHub repo (JSG CMS)

Issue: When I ask Grok Bot to launch a Cloud Agent, it fails with:

For AI issues: which model did you use?
Grokbot (not sure)

Does this stop you from using Cursor
Yes - Cursor is unusable

## Post 5 — @deanrie (2026-09-03T18:21:47.353Z)

Hey, thanks for the detailed report and for the screenshot of your Privacy settings. I can see you’re set to the current Privacy Mode, so everything looks correct.

Good news: this isn’t related to your settings, and it’s not something on your side. It looks like something changed on our side in a recent release. Because of that, launching Cloud Agent specifically through Grok Bot incorrectly hits the “Privacy Mode (Legacy)” check, even though your account isn’t in it. That’s why launching from Cursor Desktop works, but launching from Grok Bot doesn’t, exactly like you described.

You don’t need to change anything. Signing out and back in, switching privacy mode, or resetting won’t help and aren’t needed. We’re tracking this. Please try launching Cloud Agent from Grok Bot again a bit later, and if you still see the Privacy Mode (Legacy) error, reply here with the time of your attempt and I’ll double-check.
