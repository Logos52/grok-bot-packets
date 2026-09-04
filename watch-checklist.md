# Watch checklist (Cloudflare-first)

## Hosting
| Property | Host | Audience |
|----------|------|----------|
| tsumugu.cc | Cloudflare | CF Web Analytics (RUM) |
| tsumugu-ed.com | Cloudflare | CF Web Analytics (RUM) |
| logos52.github.io | GitHub Pages | Reach + Actions only |

## A. REACH
1–4 CF URLs + logos52.github.io. Note cf-cache-status on CF hosts.
Do NOT treat tsumugu.cc/dict|/browse|/c|/w 404 as failures until federation is live.

## B. AUDIENCE (PRIMARY)
Token: `/workspace/secrets/cf-analytics-readonly` (Bearer). Account Analytics / Web Analytics read.
Zones: tsumugu-ed.com, tsumugu.cc. Cache zone IDs in watch-state.json.
If MISSING: `AUDIENCE: MISSING CF analytics token — skip`

## C. SEARCH (optional)
`/workspace/secrets/gsc-readonly.json` — omit or MISSING line if absent.

## D. CI (Logos52 primary Actions)
Token: `/workspace/secrets/github-readonly` (Bearer). Report only — never re-run, cancel, or write Actions.
Primary repos (default branch latest run, or latest overall if clearer):
- Logos52/tsumugu-core-dev
- Logos52/tsumugu-core
- Logos52/tsumugu
- Logos52/tsumugu-ed
- Logos52/tsumugu-wiki
- Logos52/logos52.github.io
- Logos52/grok-bot-packets
Skip archives unless added: wnab-dev-archive, wnab-fork-archive, notes, CulturePals, Norman-Sicily, etc.
Green = one CI line. Failures = alert with repo, workflow name, conclusion, html_url, age.
Exception-only after a clean CI baseline; first pass that finds a red (e.g. tsumugu-core-dev) must surface it.
in_progress = OK (note, not red). Rate-limit = ERROR not fake green.

## State
`/workspace/watch-state.json`
