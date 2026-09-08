---
id: 2026-09-08-human-111425250-grok-bot-calldynamictool-fails-missing-namespace
kind: article
title: "Grok Bot: CallDynamicTool fails Missing namespace/toolName — SendToAgent/Task broken"
source: "https://forum.cursor.com/t/grok-bot-calldynamictool-fails-missing-namespace-toolname-sendtoagent-task-broken/170869"
author: Human_111425250
published: 2026-09-07
captured: 2026-09-08
via: grokbot/Field
lane: ai
status: raw
private: false
---

# Grok Bot: CallDynamicTool fails Missing namespace/toolName — SendToAgent/Task broken
URL: https://forum.cursor.com/t/grok-bot-calldynamictool-fails-missing-namespace-toolname-sendtoagent-task-broken/170869
Created: 2026-09-07T09:18:46.610Z

## Post 1 @Human_111425250 (2026-09-07T09:18:46.686Z)
Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Since Sun 6 Sep 2026 ~21:45 Europe/London, one agent (Maturin / Desk) cannot invoke cursor-namespace tools via CallDynamicTool. Every call fails immediately with:

Tool execution error. Missing required fields: namespace, toolName. Re-issue the call with the tool’s identity set; arguments alone does not identify the tool.

This happens even when namespace and toolName ARE supplied (nested or flattened args).

Fails: SendToAgent (cannot message teammate agents), Task/browserUse/computerUse, CreateAgent/UpdateAgent; often SearchPlugins/WebSearch via the same path. SendFeedback also fails the same way.

Works: user↔agent chat (SendToUser); Shell/files/memory/routines on the agent computer; GetDynamicTools still lists the tools; user can chat teammates directly in the app; at least one inbound teammate→Maturin message arrived while outbound was already broken. box-doctor all pass. status.cursor.com showed Grok Bot operational / no matching open incident. Client restart and Reset Grok Bot’s Computer did not fix it.

Impact: multi-agent desk cannot coordinate specialists from the assembler bot.

Steps to Reproduce
Steps to Reproduce

Open Grok Bot; chat with an agent that uses teammates (SendToAgent) / Task workers.
Have the agent call CallDynamicTool for SendToAgent (or Task / CreateAgent) with namespace=“cursor” and toolName set.
Observe immediate failure: Missing required fields: namespace, toolName — even though those fields were provided.
Confirm GetDynamicTools still lists SendToAgent/Task; user chat still works.

Expected Behavior
CallDynamicTool should execute SendToAgent/Task/CreateAgent when namespace + toolName (+ args) are correctly supplied. Agent-to-agent messaging and background workers should work while user chat works.

Operating System
MacOS

Version Information
Version: 0.44.0

Release Track: stable

OS: darwin

Additional Information

First noticed during chartist-bot setup evening of 6 Sep; earlier that evening Task/browserUse had worked (TradingView check).
Overnight 30-min probes: often SearchPlugins OK / SendToAgent missing or call fails; never full recovery through morning 7 Sep (still broken after computer Reset ~09:42).
Mac client. Related weekend forum threads on Grok Bot send/reply failures; this case is specifically CallDynamicTool invoke / agent-to-agent outbound while chat remains healthy.

Does this stop you from using Cursor
No - Cursor works, but with this issue

## Post 5 @deanrie [CursorStaff] (2026-09-07T09:42:55.465Z)
Hey, thanks for the detailed report. With this description, it’s much clearer what’s going on.

This error is coming from the tool call itself, not from your computer or account. It means the request reached us without namespace and toolName as top-level fields next to arguments. On our side, we can see that the calls Maturin has been sending since Sunday evening don’t include those fields at the top level, they’re most likely ending up inside arguments. And once a few calls like that land in the conversation history, the bot starts repeating the same shape. Your computer is fine though, which is why Shell, files, and routines keep working, and why Reset Grok Bot’s Computer didn’t change anything. The chat history isn’t stored on the computer.

Two steps, in order:

In the chat with Maturin, send this message: “When you call CallDynamicTool, namespace and toolName must be top-level keys alongside arguments, never inside arguments. Send a one-line hello to one of your teammates now using that shape.”
If it still fails, right click Maturin in the sidebar → Duplicate. This creates a bot with the same setup but a clean chat. Ask the duplicate to message a teammate.

Let me know which step worked. If neither helps, send the exact JSON the bot shows for one failed call, plus the time in UTC, and I’ll dig deeper.

## Post 6 @Human_111425250 (2026-09-07T10:01:25.352Z)
Dean Rie:

When you call CallDynamicTool, namespace and toolName must be top-level keys alongside arguments, never inside arguments. Send a one-line hello to one of your teammates now using that shape.”

Outstanding! Step 1. solved the issue. No need for Step 2. Thank you for the super rapid response.
