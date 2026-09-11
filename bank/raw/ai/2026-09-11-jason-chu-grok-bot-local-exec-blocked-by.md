---
id: 2026-09-11-jason-chu-grok-bot-local-exec-blocked-by
kind: article
title: Grok Bot local-exec blocked by F-Secure on Windows (DeepGuard / Temp one-shot PS >10s)
source: "https://forum.cursor.com/t/grok-bot-local-exec-blocked-by-f-secure-on-windows-folder-exclusions-ineffective/171219"
author: Jason_Chu
published: 2026-09-10
captured: 2026-09-11
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot local-exec blocked by F-Secure on Windows (DeepGuard / Temp one-shot PS >10s)
Source: https://forum.cursor.com/t/grok-bot-local-exec-blocked-by-f-secure-on-windows-folder-exclusions-ineffective/171219
Author: Jason_Chu
Published: 2026-09-10

## @Jason_Chu 2026-09-10T04:17:27

Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Grok Bot local execution on Windows is blocked by F-Secure.

Symptoms:

- Chat works; Computers may show the PC as connected.
- Local commands fail with “unavailable / isn’t connected” (sometimes “temporarily unreachable”).
- Fully disabling F-Secure + relaunching Grok Bot restores local exec.
- Turning F-Secure back on breaks it again.

What did NOT help:

- Excluding these folders in F-Secure:

- %LOCALAPPDATA%\Programs\Grok Bot
- %USERPROFILE%.grokbot

- “Always allow” local execution in Grok Bot settings

Environment:

- OS: Windows 11
- Grok Bot version: [fill]
- F-Secure version: [fill]
- Enabled components (please note which are ON):

- DeepGuard: [ON/OFF]
- Firewall: [ON/OFF]
- Browsing protection / HTTPS scanning: [ON/OFF]
- Virus protection / realtime scanning: [ON/OFF]

Request:

Please treat this as an F-Secure incompatibility with the local-exec channel (not file scanning), and provide a documented allowlist or fix. Happy to run more tests if needed.

Related: Grok Bot 0.27.0 Windows – local host permanently “isn’t connected” after clean registration + new identity (server-side?) - #12 by deanrie

Steps to Reproduce

- Install/open Grok Bot on Windows with F-Secure enabled (Virus protection / DeepGuard on).
- Set “Execute on this computer” to Always allow.
- In F-Secure, exclude:

- %LOCALAPPDATA%\Programs\Grok Bot
- %USERPROFILE%.grokbot

- Ask the bot to run a local command (e.g. hostname) → fails with unavailable / temporarily unreachable.
- Fully disable F-Secure, relaunch Grok Bot, retry the same command → succeeds.
- Re-enable F-Secure → local exec breaks again.

Operating System
Windows 10/11

Version Information
Grok Bot  0.47.0

Does this stop you from using Cursor
No - Cursor works, but with this issue

## @mohitjain 2026-09-10T09:11:48 [STAFF]

Hey @Jason_Chu,

From our side, F-Secure is delaying each command past the 10-second window the agent waits, not blocking the connection (with it on, your first response takes ~12s; off, ~1s). The folder exclusions don’t help because each command runs a fresh one-off PowerShell script from your temp folder (%LOCALAPPDATA%\Temp), which is outside what you excluded.

Could you run hostname from the bot after each of these, one at a time?

- Turn off only DeepGuard (leave Virus protection on) - does it work?
- DeepGuard back on, then turn off only real-time / virus protection - does it work?
- Everything back on, then allow Grok Bot.exe (from %LOCALAPPDATA%\Programs\Grok Bot) in F-Secure’s DeepGuard app permissions - does it work?
- If still failing, as a test only, exclude %LOCALAPPDATA%\Temp, try once, then remove it again.

Tell us which step worked plus your F-Secure product/version, and we’ll turn that into a proper allowlist. We’ve let the team know so command execution can be made more tolerant of security software that’s slow to inspect it.

## @Jason_Chu 2026-09-10T10:50:37

Thanks @mohitjain — we ran the tests.

Results:

- Turning off Behavior Detection (DeepGuard) alone → local exec works (~0.5s).
- Allowing only Grok Bot.exe with Behavior Detection ON → still fails (temporarily unreachable).
- Excluding %LOCALAPPDATA%\Temp with Behavior Detection ON → works (~0.5s). Excluding Grok Bot.exe is not needed.
- Narrowing the exclusion to a Grok subfolder under Temp → fails again. Only excluding the whole Temp folder works.

So the working workaround is excluding C:\Users\jason\AppData\Local\Temp while keeping Behavior Detection on. That matches your note about one-shot PowerShell under Temp.

I’d rather not leave all of Temp excluded long-term for security reasons. Happy to test a narrower allowlist or a build with a longer timeout when you have one.

F-Secure: Virus protection ON; Behavior Detection ON (with Temp excluded); Grok Bot 0.47.0; Windows 11.
