---
id: 2026-09-07-noname-grok-bot-stuck-on-reconnecting-malformed
kind: article
title: Grok Bot stuck on Reconnecting — malformed listAgents secretRequest.target
source: "https://forum.cursor.com/t/grok-bot-stuck-on-reconnecting-to-your-computer-fully-unusable-malformed-listagents-gateway-response/170736"
author: noname
published: 2026-09-06
captured: 2026-09-07
via: grok-bot/Field
lane: ai
status: raw
private: false
---

TITLE: Grok Bot stuck on “Reconnecting to your computer” — fully unusable — malformed listAgents gateway response
URL: https://forum.cursor.com/t/grok-bot-stuck-on-reconnecting-to-your-computer-fully-unusable-malformed-listagents-gateway-response/170736
CREATED: 2026-09-06T00:36:53.288Z
TAGS: grok-bot, networking

--- post #1 @noname 2026-09-06T00:36:53.351Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Grok Bot 0.43.0 on Ubuntu stuck “Reconnecting to your computer” — malformed listAgents gateway response Steps to Reproduce Grok Bot worked normally for about 30 minutes, then suddenly became permanently stuck on: Reconnecting to your computer… Retry does nothing. I have already: fully quit/restarted Grok Bot signed out and back in confirmed Privacy Mode/Data Sharing choice is explicitly saved tried Recover Computer verified normal internet connectivity verified no VPN/proxy is active killed all Grok Bot processes and relaunched removed the local gateway-descriptor.json and allowed Grok Bot to regenerate it The local daemon starts correctly, but Grok Bot consistently logs: node-agent-coordinator: agents roster seed skipped: SandGatewayMalformedReplyError: gateway listAgents reply is malformed: 1: pushMessageContent: message: message: secretRequest: target: required field This exact error returns even after deleting the local gateway descriptor and relaunching, which suggests the malformed listAgents response is being returned fresh from the Grok Bot gateway/backend. Could someone inspect my Grok Bot Agent Computer / gateway state from the backend and repair or reprovision it without deleting my existing Bots/files if possible? Please also check whether there is a malformed queued secretRequest missing its required target field in my account/computer state. Expected Behavior The application should work and not be stuck on reconnecting. Screenshots / Screen Recordings Screenshot from 2026-09-05 17-34-59.png 333×126 2.5 KB Operating System Linux Version Information Ubuntu 24.04 Grok Bot 0.43.0 no VPN no proxy cursor.com reachable over HTTPS local local-exec-daemon starts normally Additional Information I reproduced this on two separate accounts. A fresh account worked normally. Immediately after upgrading that account, Grok Bot became unable to reach its computer, exactly like my first upgraded account. I fully ruled out local networking: Ubuntu 24.04 VPN completely removed during test normal DNS https://api2.cursor.sh/ returns HTTP 200 Grok Bot local daemon starts Grok Bot consistently receives a malformed gateway response: SandGatewayMalformedReplyError: gateway listAgents reply is malformed: 3: pushMessageContent: message: message: secretRequest: target: required field Recover does not fix it. Please inspect the Agent Computer / gateway state for my upgraded accounts. This appears to be triggered by account upgrade/provisioning and likely requires backend repair. Does this stop you from using Cursor Yes - Cursor is unusable
