---
id: 2026-09-03-chen-zhanfeng-grokbot-linux-execution-on-local-computer
kind: article
title: GrokBot Linux Execution on Local Computer not working
source: "https://forum.cursor.com/t/grokbot-linux-execution-on-local-computer-not-working/170157"
author: Chen_Zhanfeng
published: 2026-09-01
captured: 2026-09-03
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

# GrokBot Linux Execution on Local Computer not working
URL: https://forum.cursor.com/t/grokbot-linux-execution-on-local-computer-not-working/170157
Created: 2026-09-01T03:38:08.038Z

## Post 1 @Chen_Zhanfeng · 2026-09-01T03:38:08.096Z

Where does the bug appear (feature/product)? Grok Bot Describe the Bug Time: 2026-09-01 11:10 SGT / 03:10 UTC ListMachines: {“machines”: } now, after restart, after full GUI kill, and on a new agent (LocalExec probe 74a73a1f-2903-4839-97eb-84286a2361a4) This agent: Boss 186fb847-ca75-4e0a-ae8a-34fffd349bf9 Client: Linux, current computer name XPS-15, Execution = Always allow Box hostname cursor, kernel 6.12.94+, uid box Box exec-daemon: listening :1337, tracing off (hasTraceEndpoint: false, ghostMode: true), computerUseEnabled: true, workspace /workspace Box-doctor: 10/10 pass (unrelated to laptop local-exec) always allow already enabled Steps to Reproduce minimal session to produce this failure 74a73a1f-2903-4839-97eb-84286a2361a4 Screenshots / Screen Recordings Screenshot from 2026-09-01 11-35-15.png 1047×312 27 KB Operating System Linux Version Information GrokBot LInux 0.30.0 Does this stop you from using Cursor No - Cursor works, but with this issue

## Post 2 @Colin [staff] · 2026-09-01T05:46:50.863Z

Hey @Chen_Zhanfeng , thanks for the report! This is a known issue on Grok Bot 0.30.0 on Linux and a fix is already merged. It ships in the next desktop update, so local execution should start working once you update. If you want to try a workaround before the update: Make sure a system keyring is installed and unlocked (gnome-keyring on GNOME/Ubuntu, KWallet on KDE). The helper needs it to store its machine identity. Fully quit Grok Bot and check no leftover Grok Bot processes remain. Relaunch Grok Bot
