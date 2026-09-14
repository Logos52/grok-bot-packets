---
id: 2026-09-13-jamie-burt-grok-bot-0-47-0-on
kind: article
title: "Grok Bot 0.47.0 on Ubuntu 24.04: first-time setup fails with ENAMETOOLONG writing sand-client-<huge token>"
source: "https://forum.cursor.com/t/grok-bot-0-47-0-on-ubuntu-24-04-first-time-setup-fails-with-enametoolong-writing-sand-client-huge-token/171438"
author: jamie_burt
published: 2026-09-12
captured: 2026-09-13
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot 0.47.0 on Ubuntu 24.04: first-time setup fails with ENAMETOOLONG writing sand-client-<huge token>
URL: https://forum.cursor.com/t/grok-bot-0-47-0-on-ubuntu-24-04-first-time-setup-fails-with-enametoolong-writing-sand-client-huge-token/171438
Created: 2026-09-12T15:37:55.336Z

## @jamie_burt 2026-09-12T15:37:55.373Z
Describe the Bug
Use category Grok Bot if the form asks.

Copy everything below the line.

Title: Grok Bot 0.47.0 on Ubuntu 24.04: first-time setup fails with ENAMETOOLONG writing sand-client-<huge token>

Where the bug appears (feature/product): Grok Bot

Describe the Bug

Official Linux package grok-bot 0.47.0 (amd64) fails first-time setup after browser sign-in at Auth | Cursor - The best way to code with AI.

The app shows:

Grok Bot couldn’t finish setting up

edge/handler-failed: ENAMETOOLONG: name too long, open ‘/home/jamie/.config/Grok Bot/sand-client-<very long token>’

The last path component is longer than Linux NAME_MAX (255 bytes). The client is using a long session/device token as a filename. Setup dies on a local open(), not on reaching the cloud computer.

Screenshot of the dialog is attached. The on-screen path is already truncated; I am not pasting the full token.

Steps to Reproduce

Install grok-bot 0.47.0 on Ubuntu 24.04. Package status: ii grok-bot 0.47.0 amd64. Binary: /usr/bin/grok-bot → /opt/Grok Bot/grok-bot.
Sign in through the browser login flow (Auth | Cursor - The best way to code with AI).
Continue first-bot setup.
Setup dialog shows ENAMETOOLONG and Try again.

Expected Behavior

Sand-client state is stored under a short name (hash or directory). First bot / agent computer is created.

Operating System

Linux (Ubuntu 24.04)

Linux jamie-ThinkPad-T470s 7.0.0-31-generic #31~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Aug 10 09:38:02 UTC 2 x86_64 x86_64 x86_64 GNU/Linux

ThinkPad T470s. Config dir: /home/jamie/.config/Grok Bot (space in the directory name).

Version Information

ii  grok-bot  0.47.0  amd64
/usr/bin/grok-bot -> /etc/alternatives/grok-bot
real binary: /opt/Grok Bot/grok-bot
package files dated 9 Sep 2026

grok-bot --version does not print a version. It starts Electron and emits:

(node:…) ExperimentalWarning: vm.USE_MAIN_CONTEXT_DEFAULT_LOADER is an experimental feature and might change at any time

Local state after the failed setup (12 Sep 2026, 16:19–16:21 BST)

~/.config/Grok Bot contains Electron state including blob_storage, Cache, Code Cache, Cookies, Crashpad, and box-secrets-push-state.v1.json. The failing path is the oversized sand-client-<token> name shown in the dialog.

Already tried

Clicked Try again
Inspected ~/.config/Grok Bot and the /opt/Grok Bot install tree

Additional Information

Linux cannot create a filename that long. Please hash the id for the basename, or write the token as file contents under sand-client/<short-id>.

Happy to share more files from that config dir privately if you specify which are safe.

Does this stop you from using Cursor?

No — Cursor works, but with this issue. Grok Bot first-time setup does not complete.

Steps to Reproduce
see post

Screenshots / Screen Recordings
Screenshot at 2026-09-12 16-35-24.png1920×1080 155 KB

Operating System
Linux

Version Information
0.47.0 amd64

Does this stop you from using Cursor
No - Cursor works, but with this issue
