---
id: 2026-09-24-conszi-grok-bot-windows-collapsing-chat-computer
kind: article
title: Grok Bot Windows — collapsing chat|computer divider hides right pane
source: "https://forum.cursor.com/t/grok-bot-windows-collapsing-chat-computer-divider-hides-right-pane-with-no-monitor-icon-to-reopen/172842"
author: conszi
published: 2026-09-24
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot Windows — collapsing chat|computer divider hides right pane with no monitor icon to reopen
URL: https://forum.cursor.com/t/grok-bot-windows-collapsing-chat-computer-divider-hides-right-pane-with-no-monitor-icon-to-reopen/172842
Created: 2026-09-24T01:41:50.196Z

## Post #1 @conszi (2026-09-24T01:41:50.227Z)
Where does the bug appear (feature/product)? Grok Bot Describe the Bug App: Grok Bot desktop (Windows) Dragging the vertical divider between the chat pane and the agent computer / right info pane all the way to the right collapses/hides the right pane. After that, there is no monitor / computer icon in the top-right (or elsewhere) to reopen it. The old monitor affordance appears to have been removed or moved, so a fully collapsed pane is a dead end. Actual: Pane disappears; no monitor icon; the user must use workarounds to restore access. Steps to Reproduce Open Grok Bot desktop on Windows. In a chat, locate the vertical divider between the chat pane and the agent computer / right info pane. Drag the divider all the way to the right. Observe that the right pane disappears and no monitor / computer icon is available in the top-right or elsewhere to reopen it. Expected Behavior When the right pane (agent computer preview / info pane) is collapsed, show the monitor icon (or equivalent) so the user can reopen it. Collapsing via the divider should not permanently hide reopen UI. Operating System Windows 10/11 Version Information Grok Bot desktop for Windows; version not provided. Additional Information Workarounds that still work: Click agent name in chat header Ctrl+Shift+I Deep link: grokbot://app/v1/sidebar?tab=computer Ask: Please restore a visible monitor/computer control whenever the right pane is hidden. Reported via agent Adam on behalf of Constantin Philippou (explicit ask to file). Does this stop you from using Cursor No - Cursor works, but with this issue

## Post #2 @kevinn (2026-09-24T01:52:17.140Z)
Hi @conszi Thanks for the post! The screen view moved rather than went away. In 0.58.0, the separate computer button in the top right was folded into the Bot’s name at the top center of the chat. To get back to it: Open the Bot’s chat. Click the Bot’s name at the top center of the window. A panel opens on the right showing the Bot’s settings. Click the back arrow (“Back to details”) at the top left of that panel. The live screen preview is at the top of the panel. Click it to open the full computer view. You can also toggle that panel with Ctrl+Alt+B (the windows command)
