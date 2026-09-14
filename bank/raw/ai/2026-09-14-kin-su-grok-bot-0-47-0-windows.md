---
id: 2026-09-14-kin-su-grok-bot-0-47-0-windows
kind: article
title: Grok Bot 0.47.0 Windows — Agent Computer DNS SERVFAIL / ENOTFOUND; please rebuild or reattach on backend
source: "https://forum.cursor.com/t/grok-bot-0-47-0-windows-agent-computer-dns-servfail-enotfound-please-rebuild-or-reattach-on-backend/171482"
author: Kin_Su
published: 2026-09-13
captured: 2026-09-14
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot 0.47.0 Windows — Agent Computer DNS SERVFAIL / ENOTFOUND; please rebuild or reattach on backend
URL: https://forum.cursor.com/t/grok-bot-0-47-0-windows-agent-computer-dns-servfail-enotfound-please-rebuild-or-reattach-on-backend/171482
created: 2026-09-13T09:04:12.283Z

## @Kin_Su · 2026-09-13T09:04:12.314Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Please recover/rebuild the Agent Computer on the backend. Do not ask me to Reset. Settings Update is greyed out because the published hostname does not resolve. Recover is not offered. I have not clicked Reset. Where does the bug appear: Grok Bot Product: Grok Bot desktop 0.47.0 (sand 0.47.0, Electron 42.1.0) OS: Windows 11 10.0.26200, timezone America/Los_Angeles Cursor account: kinsuxq at gmail.com Auth: google-oauth2 user_01KWKMCMJ2PE502VRMVZHEVHWY Observed: 2026-09-13 01:22-01:47 PDT UI: signed in as Kin Su; “Grok Bot is having trouble connecting”; then “Reconnecting to your computer”; “No saved Bots yet” Network Debugger: Computer TLS, Computer health, Computer events all fail in 2-3ms Tested endpoint: bf655cc460505d8952aa-pod-cvymjpbe6vf53ffq743i7lagxi-1340 us8 cursorvm com Error: ENOTFOUND / router DNS Server failed (RT-AC1900P 192.168.50.1) Control: test123 us8 cursorvm com and other names under us8 cursorvm com resolve and return HTTP 404 Server awselb/2.0. Only this pod hostname is broken. Local current computer name: Kin-P1. No VPN. WinHTTP direct. No TLS inspection (Amazon / Lets Encrypt certs). Please reattach or recreate DNS for this Agent Computer and preserve existing Bots (Chief of Staff, EAD, Kin X1C, TAD-SYS, APM-SYS, etc.). Steps to Reproduce login Operating System Windows 10/11 Version Information 0.47.0 IDE Does this stop you from using Cursor No - Cursor works, but with this issue

## @Colin · 2026-09-13T10:01:35.935Z
Hey @Kin_Su , thanks for the detailed report! Nothing changed on our end: your VM’s hostname resolves normally from outside your network, to the same six addresses as test123.us8.cursorvm.com . There’s no per-computer DNS record to rebuild; everything under us8.cursorvm.com is served by a single wildcard record, so a rebuilt computer would just hit the same SERVFAIL on your router. So the lookup is failing somewhere between your PC and your router (or your ISP’s resolver). Could you try these in order? In PowerShell, run: nslookup bf655cc460505d8952aa-pod-cvymjpbe6vf53ffq743i7lagxi-1340.us8.cursorvm.com 8.8.8.8 You should get six addresses. Then run the same command against 192.168.50.1 to confirm the router still returns “Server failed”. Bypass the router’s DNS: Windows Settings > Network & internet > your connection > Edit (next to “DNS server assignment”) > Manual > toggle IPv4 on > Preferred: 1.1.1.1, Alternate: 8.8.8.8 > Save. Then run ipconfig /flushdns . Fully quit Grok Bot from the system tray (right-click > Quit), relaunch, and wait a minute or two. If that doesn’t help, it’s worth updating the DNS settings at the router level, and checking whether the router has malicious-site blocking (long hostnames can sometimes trigger it) or DNS filtering enabled!
