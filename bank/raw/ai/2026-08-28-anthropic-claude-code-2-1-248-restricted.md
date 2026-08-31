---
id: 2026-08-28-anthropic-claude-code-2-1-248-restricted
kind: article
title: Claude Code 2.1.248 --restricted
source: "https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md"
author: Anthropic
published: 2026-08-28
captured: 2026-08-28
via: grok-bot/Brief
lane: ai
status: raw
private: false
---

# Claude Code CHANGELOG

## 2.1.248

- Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project and local settings files
- Added `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter: a per-agent prompt cache TTL used when no subagent TTL setting is configured
- Added `claude self-hosted-runner --client-label` (or `SELF_HOSTED_RUNNER_CLIENT_LABEL`) to override the label the runner registers with (default: hostname)
- Added server-managed settings diagnostics: a startup warning when the settings fail to load, and a `/doctor` and `/status` line explaining a load failure or why they weren't fetched
- Added a warning in `/web-setup` when the GitHub CLI token lacks the `workflow` scope
- Added `/usage-credits` for Enterprise organizations billed through AWS Marketplace, self-serve Enterprise, and Enterprise trials
- Added cross-session messaging (`SendMessage` / `ListAgents`) between sessions on the same machine on Bedrock, Vertex, and Foundry, and when telemetry is disabled
