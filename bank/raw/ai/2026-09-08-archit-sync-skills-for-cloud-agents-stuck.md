---
id: 2026-09-08-archit-sync-skills-for-cloud-agents-stuck
kind: article
title: "\"Sync Skills for Cloud Agents\" stuck — Grok Bot-started Cloud Agents don't get synced skills"
source: "https://forum.cursor.com/t/sync-skills-for-cloud-agents-stuck/170899"
author: Archit
published: 2026-09-07
captured: 2026-09-08
via: grokbot/Field
lane: ai
status: raw
private: false
---

# "Sync Skills for Cloud Agents" stuck
URL: https://forum.cursor.com/t/sync-skills-for-cloud-agents-stuck/170899
Created: 2026-09-07T13:20:26.701Z

## Post 1 @Archit (2026-09-07T13:20:26.758Z)
Where does the bug appear (feature/product)?
Cursor Agents Window

Describe the Bug
The “Sync Skills for Cloud Agents” option is stuck on the syncing step and never finishes. As a result, Cloud Agents don’t get access to my local skills. This makes my Grok Bot experience worse because I want Grok Bot to hand off coding work to Cloud Agents that can use my local skills to maintain code quality.

Steps to Reproduce
In my Cursor Agents Window, when I go to Settings → Agents → Context and Tools → Sync Skills for Cloud Agents, and enable the toggle, it went from “Syncing 0 of 58” to “Syncing 58 of 58” but it’s stuck there.

I could verify that my Cloud Agents did not get access to those 58 local skills, so it has not finished syncing. I tried cancelling it, toggling the option off and on, and restarting the app multiple times but nothing worked.

Expected Behavior
It finishes syncing all local skills seamlessly without getting stuck.

Screenshots / Screen Recordings
Screenshot 2026-09-07 at 9.17.32 AM.png1370×240 14.3 KB

Operating System
MacOS

Version Information
Version: 3.19.13

VS Code Extension API: 1.128.0

Commit: dd066f332fcea7382764400fde902f61920648d0

Date: 2026-09-04T17:41:16.065Z

Layout: Agent Window

Build Type: Stable

Release Track: Default

Electron: 42.10.0

Chromium: 148.0.7778.280

Node.js: 24.18.1

V8: 14.8.178.38-electron.0

xterm.js: 6.1.0-beta.291

OS: Darwin arm64 25.5.0

Does this stop you from using Cursor
No - Cursor works, but with this issue

## Post 5 @deanrie [CursorStaff] (2026-09-07T17:03:18.127Z)
Hey, thanks for the detailed report. I can see in your screenshot that the row is enabled and it’s stuck on Syncing 58 of 58.

First, the good news. Sync has already downloaded all 58 skills, the setting is enabled, and nothing was deleted from ~/.cursor/skills. The row gets stuck on the final verification step after the download, which is why it never moves past Syncing 58 of 58. This is a known issue and we’re tracking it. I’ve added your case to it. I don’t have an exact timeline yet.

About Cloud Agents not seeing the skills. Right now, only Cloud Agents started from the Cursor desktop app pick up synced skills, from the Agents Window or the IDE. Agents started from Grok Bot don’t get them yet. I’ve shared this gap with the team too. As a temporary workaround, start the Cloud Agent from the Agents Window and it should pick up your synced skills.

To help confirm which step it’s stuck on, please send one line from the log:

In Cursor Agents Window, press Cmd+Shift+P and run Developer: Toggle Developer Tools.
Open the Console tab.
In the filter at the top, type Skills migration.
Copy the lines that show up here. They look like Skills migration: the destination is not serving the migrated skills yet …

Also, can you confirm where the Cloud Agents you tested were started from, Grok Bot, cursor.com, or the Agents Window?

## Post 7 @Archit (2026-09-07T17:27:51.967Z)
I see this in the Console tab. You are right, I see “destination is not serving the migrated skills yet”

Screenshot 2026-09-07 at 1.19.28 PM1420×234 35.4 KB

Yes, the Cloud Agents I tested were started from Grok Bot.

I can verify that local skills/commands work for Cloud Agents from the Agents Window. But they are not accessible on the Web cursor.com/agents.

## Post 8 @deanrie [CursorStaff] (2026-09-07T18:27:49.945Z)
Thanks, the log line is exactly what we need. reason=missing confirms the hang happens at the final verification step, after all 58 skills have already loaded into the store. This is the same issue we’re tracking, and I’ve added your case to it.

On the second point, what you’re seeing matches what we see too. Right now, synced skills are only picked up by cloud agents started from the desktop Agents Window. Agents started from Grok Bot and from the web at cursor.com/agents don’t get them yet. This isn’t anything in your setup, everything is enabled and the files are in the store. I’ve flagged this gap to the team separately.

As a temporary workaround, start the cloud agent from Agents Window. You already confirmed skills and commands are available there. I’ll post here when there’s an update on either item.

## Post 9 @Archit (2026-09-07T18:39:57.712Z)
Awesome, thank you @deanrie!
