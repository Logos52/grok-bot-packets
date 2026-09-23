---
id: 2026-09-23-dnz-grok-bot-keeps-reconnecting-api2-cursor
kind: article
title: "Grok Bot keeps reconnecting: api2.cursor.sh → 100.60.17.13 presents Pearson cert (devapi.english.com)"
source: "https://forum.cursor.com/t/grok-bot-keeps-reconnecting-api2-cursor-sh-resolves-to-100-60-17-13-which-presents-a-certificate-for-devapi-english-com/172578"
author: dnz
published: 2026-09-22
captured: 2026-09-23
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot keeps reconnecting: api2.cursor.sh resolves to 100.60.17.13, which presents a certificate for devapi.english.com
URL: https://forum.cursor.com/t/grok-bot-keeps-reconnecting-api2-cursor-sh-resolves-to-100-60-17-13-which-presents-a-certificate-for-devapi-english-com/172578
Created: 2026-09-22T03:02:31.147Z

## @dnz — 2026-09-22T03:02:31.175Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Grok Bot stays on “Can’t reach your computer” and keeps reconnecting. Cursor’s updater says the certificate is invalid and the server may be pretending to be api2[.]cursor[.]sh. api2[.]cursor[.]sh CNAMEs to api2geo[.]cursor[.]sh, then api2direct[.]cursor[.]sh. Both 1.1.1.1 and 8.8.8.8 return 100.60.17.13 in that set. Connecting to 100.60.17.13 with that hostname presents a certificate for devapi[.]english[.]com (Pearson PLC / Sectigo), so TLS hostname verification fails. From the same network, 34.235.15.195 in the same DNS set presents the correct certificate (CN=api2[.]cursor[.]sh, issuer Amazon RSA 2048 M01). Mobile hotspot works because it gets a different address list. No local proxy or antivirus HTTPS scanning. Changing DNS to 1.1.1.1 and 8.8.8.8 does not remove 100.60.17.13. Steps to Reproduce On this office network, resolve api2direct[.]cursor[.]sh with 1.1.1.1 or 8.8.8.8. 100.60.17.13 is in the answer. Connect to 100.60.17.13 port 443 using the hostname api2[.]cursor[.]sh. TLS fails: certificate subject is devapi[.]english[.]com, not api2[.]cursor[.]sh. Open Grok Bot. It keeps reconnecting with “Can’t reach your computer”. Same account on a phone hotspot connects normally. Expected Behavior Every address published for api2[.]cursor[.]sh should present a certificate for that hostname. Grok Bot should connect without a certificate warning. Operating System MacOS Version Information Grok Bot 0.57.1 OS: macOS 27.0 (build 26A428), arm64, Apple M5 Electron: 42.1.0 Chrome: 148.0.7778.97 Node.js: 24.15.0 Does this stop you from using Cursor Sometimes - I can sometimes use Cursor

## @mohitjain (staff) — 2026-09-22T12:13:05.670Z
Hey @dnz , this isn’t on our side and your computer is healthy, so don’t Reset or Recover. 100.60.17.13 is a real api2 address and serves the correct api2.cursor.sh certificate when we test from outside. The Pearson cert you get means your network is delivering that address to the wrong server, which is why only the 100.x addresses fail and the hotspot works. To pin down where: run traceroute -n 100.60.17.13 and traceroute -n 34.235.15.195 from the office network. If they diverge, that’s your office or ISP redirecting the 100.x range. Ask your network team to check firewall, NAT, or routing rules covering 100.0.0.0/8 (often added by mistake near the 100.64.0.0/10 carrier-NAT range). The hotspot keeps you connected meanwhile.
