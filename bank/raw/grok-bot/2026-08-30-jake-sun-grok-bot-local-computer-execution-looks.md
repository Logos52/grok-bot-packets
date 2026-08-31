---
id: 2026-08-30-jake-sun-grok-bot-local-computer-execution-looks
kind: article
title: Grok Bot local-computer execution looks connected in Settings but is not actually usable for file I/O
source: "https://forum.cursor.com/t/grok-bot-local-computer-execution-looks-connected-in-settings-but-is-not-actually-usable-for-file-i-o/169877"
author: Jake Sun
published: 2026-08-29
captured: 2026-08-30
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

Jake Sun: Grok Bot local-computer execution looks connected in Settings but is not actually usable for file I/O.

MacBook-Air-M2.local; Settings → Computer shows Current computer = Mac, Execution = Always allow, Computers lists the Mac. ListMachines flaky (connected true / empty / Unknown machineId). First turn often "No registered machines were available when this turn started" even when ListMachines already returned connected. Shell sometimes works for exactly one command then fails disconnected. CopyFromBox never succeeded even in the window where Shell just worked. Deep link settings id=local-execution jumps to General instead of Computer.

Staff (Dean Rie): matches tracked local-computer channel bug. When a command or file copy hits a timeout, the machine is temporarily removed from the agent's machine list for about a minute. That explains Settings connected + one Shell ok + next disconnected + CopyFromBox fail. "No registered machines when turn started" is expected — machine set fixed at turn start; send a new message after reconnect. Deeplink to General is the same empty-roster case. Workaround: wait ~1 minute after disconnected; if stuck, Cmd+Q, pkill -f local-exec-daemon, reopen. Improvements coming in a later desktop release (user on 0.29.0).

Portable: Settings "connected" ≠ usable channel. One successful Shell does not prove CopyFromBox. Timeout quietly drops the machine from the roster.
