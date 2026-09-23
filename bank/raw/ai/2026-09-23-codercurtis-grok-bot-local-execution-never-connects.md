---
id: 2026-09-23-codercurtis-grok-bot-local-execution-never-connects
kind: article
title: Grok Bot local execution never connects (ListMachines connected=false) while desktop chat works — Ubuntu 22.04 GLIBCXX
source: "https://forum.cursor.com/t/grok-bot-local-execution-never-connects-listmachines-connected-false-while-desktop-chat-works/172307"
author: codercurtis
published: 2026-09-18
captured: 2026-09-23
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot local execution never connects (ListMachines connected=false) while desktop chat works
URL: https://forum.cursor.com/t/grok-bot-local-execution-never-connects-listmachines-connected-false-while-desktop-chat-works/172307
Created: 2026-09-18T23:20:37.476Z

## @codercurtis — 2026-09-18T23:20:37.513Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug On Grok Bot desktop, chat from my registered computer works, but local command execution never becomes available. ListMachines reports connected: false for my computer. Any agent Shell call with that machineId fails immediately with: Your local machine isn’t connected right now (the Grok Bot desktop app must be open and online to run commands on it). The failure happens before any approval prompt. Local execution is set to Always allow . Under Settings → Computer → Computers, my computer only shows “this is the computer you are using now” with no online/offline status. There is no Network debugger row under Settings on this build. Steps to Reproduce Open Grok Bot desktop app on Linux; confirm you are chatting from that machine (message shows “Sent from machine …”). Settings → Local execution → set to Always allow . Settings → Computer → Computers: my computer is listed as “this is the computer you are using now.” In chat, ask the agent to run a simple local command (e.g. echo hello / hostname ) on this computer. Observe: agent reports my computer disconnected; command fails with the “local machine isn’t connected” error. No approval UI appears. Retried after: app update check (none available), privacy mode off, Cursor account sign-out/sign-in, full computer reboot, clean quit of Grok Bot (ensure process gone) and reopen, wait ~30s, retry. Same result every time. Expected Behavior With the desktop app open on the registered computer and Local execution enabled (Always allow), ListMachines should show my computer as connected, and agent local Shell commands should run (or at least reach the approval flow if set to Ask every time). Operating System Linux Version Information Version: 0.57.0 Built: 2026-09-18T16:32:48.691Z Release Track: stable OS: linux For AI issues: which model did you use? Grok Bot (in-app assistant / default model for this agent) For AI issues: add Request ID with privacy disabled Not available as a separate Request ID in the Grok Bot UI I can find. Conversation / agent id with privacy disabled: eacaeb79-da2e-445f-ae6b-243aa66f6b26 Additional Information Conversation / agent id: eacaeb79-da2e-445f-ae6b-243aa66f6b26 Does this stop you from using Cursor Yes - Cursor is unusable

## @Colin (staff) — 2026-09-19T15:42:54.807Z
Hey @codercurtis , thanks for the detailed report. What you’re describing matches something we’re already tracking on Linux: the small helper process that Grok Bot uses to run commands on your computer is failing to start, so your machine never shows up as connected even though chat works. Your settings are fine, and nothing about your account needs resetting. To confirm it’s the same thing, could you send two bits of info? Run this in a terminal and paste the output: tail -n 30 ~/.grokbot/local-exec-daemon.log (we’re looking for a line mentioning libstdc++ / GLIBCXX ) Your distro and version: cat /etc/os-release | head -n 3

## @codercurtis — 2026-09-19T16:27:59.402Z
Thanks Here’s the output of that command: Error: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.31' not found (required by /opt/Grok Bot/resources/app.asar.unpacked/dist/deps/tree-sitter/build/Release/tree_sitter_runtime_binding.node) at process.func [as dlopen] (node:electron/js2c/node_init:2:2625) at Module._extensions..node (node:internal/modules/cjs/loader:1998:18) at Object.func [as .node] (node:electron/js2c/node_init:2:2852) at Module.load (node:internal/modules/cjs/loader:1560:32) at Module._load (node:internal/modules/cjs/loader:1362:12) at c._load (node:electron/js2c/node_init:2:18095) at wrapModuleLoad (node:internal/modules/cjs/loader:262:19) at Module.require (node:internal/modules/cjs/loader:1583:12) at require (node:internal/modules/helpers:153:16) at load (/opt/Grok Bot/resources/app.asar/dist/deps/node-gyp-build/node-gyp-build.js:22:10) { code: 'ERR_DLOPEN_FAILED' } Node.js v24.15.0 My distro and version: PRETTY_NAME="Ubuntu 22.04.5 LTS" NAME="Ubuntu" VERSION_ID="22.04"

## @Colin (staff) — 2026-09-20T09:01:40.317Z
Hey @codercurtis , thanks, that log confirms it. The helper process that runs commands on your computer needs a newer C++ runtime library (libstdc++) than Ubuntu 22.04 ships, so it fails to start every time and your machine never shows up as connected. Chat keeps working because it doesn’t use that helper. Nothing in your settings or account is wrong. Two ways to get local execution going today: Option 1 (quick, keeps Ubuntu 22.04): upgrade just the libstdc++ library from Ubuntu’s official toolchain PPA. This is a system library change, so only do it if you’re comfortable with that. It’s backward compatible and doesn’t need a reboot. sudo add-apt-repository ppa:ubuntu-toolchain-r/test sudo apt update sudo apt install --only-upgrade libstdc++6 Then fully quit Grok Bot (make sure the process is gone) and reopen it. After about 30 seconds, ask the agent to run hostname on this computer. If it works, you’re set. If not, please send tail -n 20 ~/.grokbot/local-exec-daemon.log again. Option 2: upgrade to Ubuntu 24.04, which ships a new enough library. Grok Bot local execution works there without any extra steps.

## @system (staff) — 2026-09-22T09:01:59.332Z
This topic was automatically closed 2 days after the last reply. New replies are no longer allowed.
