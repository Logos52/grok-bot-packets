# Watch checklist (Cloudflare-first)

## Hosting
| Property | Host | Audience |
|----------|------|----------|
| tsumugu.cc | Cloudflare | CF Web Analytics (RUM) |
| tsumugu-ed.com | Cloudflare | CF Web Analytics (RUM) |
| logos52.github.io | GitHub Pages | Reach + Actions only |

## A. REACH
1–4 CF URLs + logos52.github.io + Actions latest. Note cf-cache-status on CF hosts.
Do NOT treat tsumugu.cc/dict|/browse|/c|/w 404 as failures until federation is live.

## B. AUDIENCE (PRIMARY)
Token: `/workspace/secrets/cf-analytics-readonly` (Bearer). Account Analytics / Web Analytics read.
Zones: tsumugu-ed.com, tsumugu.cc. Cache zone IDs in watch-state.json.
If MISSING: `AUDIENCE: MISSING CF analytics token — skip`

## C. SEARCH (optional)
`/workspace/secrets/gsc-readonly.json` — omit or MISSING line if absent.

## State
`/workspace/watch-state.json`
