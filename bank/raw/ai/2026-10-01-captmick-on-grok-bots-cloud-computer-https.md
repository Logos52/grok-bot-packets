---
id: 2026-10-01-captmick-on-grok-bots-cloud-computer-https
kind: article
title: On Grok Bot's cloud computer, HTTPS through SAND CONNECT fails on hostname but succeeds on public IP
source: "https://forum.cursor.com/t/on-grok-bot-s-cloud-computer-https-through-the-shared-sand-connect-proxy-127-0-0-1-8791-fastly-prod-xai-1-fails-when-connect-uses-my-public-hostname-but-succeeds-when-connect-uses-that-host-s-literal-public-ip/173542"
author: captMick
published: 2026-10-01
captured: 2026-10-01
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# On Grok Bot’s cloud computer, HTTPS through the shared SAND CONNECT proxy (127.0.0.1:8791, fastly-prod-xai-1) fails when CONNECT uses my public hostname, but succeeds when CONNECT uses that host’s literal public IP
url: https://forum.cursor.com/t/on-grok-bot-s-cloud-computer-https-through-the-shared-sand-connect-proxy-127-0-0-1-8791-fastly-prod-xai-1-fails-when-connect-uses-my-public-hostname-but-succeeds-when-connect-uses-that-host-s-literal-public-ip/173542
created: 2026-10-01T20:21:10.259Z  last: 2026-10-01T20:21:10.316Z  posts: 1  tags: ['mcp', 'grok-bot', 'networking']

## @captMick 2026-10-01T20:21:10.316Z
Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Product / platform

Product: Grok Bot
Platform: macOS desktop + Grok Bot cloud computer
Proxy: SAND HTTP CONNECT on 127.0.0.1:8791 (SAND_HTTP_PROXY_NAME=fastly-prod-xai-1)
Date: 2026-10-01 ~21:40–21:54 Europe/Zurich
Account email / Grok Bot version / request ID: (fill from About + Copy request ID)

Summary
Via shared SAND egress, HTTPS to my own public origin fails when CONNECT uses the hostname, but succeeds when CONNECT uses the literal public VIP for that same host. CONNECT returns 200, then TLS unexpected EOF. Origin is healthy (TLS + HTTP 401 by IP). Not Local Egress / not split-horizon private IP.

Steps to Reproduce

On Grok Bot cloud computer, confirm SAND proxy on loopback port 8791.
Pick a public hostname with one A to a public VIP (no AAAA, no hosts-file override). Labels: HOSTNAME and VIP.
With HTTPS_PROXY pointing at that loopback proxy, curl -vk --max-time 20 to https on HOSTNAME path /mcp
See CONNECT HOSTNAME port 443 → 200, then TLS EOF (OpenSSL unexpected eof while reading). VIP edge counters flat.
Same proxy: curl -vk to https on VIP path /mcp with Host header set to HOSTNAME → TLS OK + HTTP 401; counters move.
Optional: curl --resolve HOSTNAME:443:VIP still CONNECTs the hostname → same EOF.
Same proxy: HTTPS to well-known public sites succeeds.

Expected Behavior
Hostname CONNECT completes TLS for HOSTNAME and returns HTTP 401 without bearer, same as the VIP control. Hostname and IP CONNECT to the same public VIP behave the same. Packets hit the VIP after hostname CONNECT.

Actual behavior
Hostname CONNECT → 200 + TLS EOF; counters flat. VIP CONNECT → TLS OK + 401. --resolve does not help. Nonsense hostnames also get CONNECT 200 in my checks.

Operating System
MacOS

Version Information
grok bot 0.63.0

Additional Information
Impact
A custom MCP attach URL has to be a hostname; the connector fails_to_load even though the origin works over SAND-by-IP.

Additional ask
Please publish or privately share the current Grok Bot shared static egress source CIDRs (and update cadence), and clarify whether SAND CONNECT uses those ranges, Fastly edges, or both — so I can delimit firewall ACLs for this MCP/HTTPS host.

Notes
Real HOSTNAME / VIP / traces privately on request. Distinct from Local Egress private-IP rejection; this VIP is public and IP CONNECT works on shared SAND.

Does this stop you from using Cursor
No - Cursor works, but with this issue
