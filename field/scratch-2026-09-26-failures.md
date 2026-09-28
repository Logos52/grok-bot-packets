# Field Grok Bot failure hunt · packet 2026-09-26 (Saturday Asia/Taipei cron)
Cutoff: after ~2026-09-24/25 UTC (post Fri packet KEEP TheAviv 172859 — **do not re-keep**). Forum via public topic JSON + `tag/grok-bot/l/latest.json` (+ page=1) + `search.json?q=Grok+Bot+after:2026-09-25` (+ `after:2026-09-24`) + keyword friction (stuck, reconnecting→**429**, routines, Always allow, Auto-review, local execution). Category `c/grok-bot/l/latest.json` and `c/grok-bot/33.json` → skip if 404. Public, no login. No Firecrawl. Scratch for packet compiler.

Already kept/seen (skipped / bounce only): Fri KEEP TheAviv 172859 (Always-allow = text instruction; broader Auto-review Rules + prune). Thu KEEP Chexander 172715; Thu KEEP GFP 171703. Overflow SEEN: Peacerk 172618, Sonya_Phillips 172774, Chris_Clarke 172797. Standing footer: Catty Kaspersky / Kin_Su DNS / Zscaler / server-routines / ENAMETOOLONG / F-Secure / Name>255 / Update-Computer auth / secure-card Saved≠env / Reconnecting=inactive / weekly usage silent / computer-view-OK=backend-unreachable / Slack /invite / GitHub issue-assigned / one-bot silent / iOS unexpected-error / multi-device account-stuck / first-init incomplete / Windows partial-state AV HTTPS / Update/Reset hung 43% / nhog don’t-Reset / **Route-through rejects RFC1918** / **Reset-fail/partial ≡ no access** / **Free-plan≡no-access** / **Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins**. Do not re-alert footer list (+ TheAviv 172859).

## KEEP candidates (1) — recommend for packet

### KEEP 1 — jsolly · Plugin "Connected" = first connector only; bindings may still need auth
- url: https://forum.cursor.com/t/grok-bot-cloudflare-plugin-shows-connected-while-one-of-its-connectors-bindings-still-needs-auth-ios-and-mac-disagree/173019
- date: OP 2026-09-25 21:56 UTC; Colin staff 2026-09-25 22:57 UTC
- tags: teach-once, plugins, mcp, coverage-ceiling
- score: **9** (portable 5 / evidence 4)
- packet one-liner: [agentic·teach-once·plugins·coverage-ceiling] score=9 | jsolly | Marketplace Cloudflare plugin (4 connectors · 9 skills) shows account/plugin **Connected** while `cloudflare-bindings` still needs auth; Mac says Connected with 2/2 tools; iOS disagrees. **Colin: plugin page shows one account row + one tool count for the whole plugin, both reflecting only its first connector** (docs, no sign-in) — so Connected ≠ every connector authenticated. Known issue, tracking. Workaround for now: open each connector / try a bindings tool and complete auth when prompted; don’t trust the green Connected alone on multi-connector plugins. Distinct from generic MCP OAuth failures — **Connected status is first-connector-scoped**. Alert: **no** (no this-week Settings/routine change for Wedge unless he installs Cloudflare plugin; teach lands in footer/packet).
- staff: Colin
- bank: raw/ai/2026-09-25-jsolly-grok-bot-cloudflare-plugin-connected-while.md

## OVERFLOW / watch (not packet KEEP)

### DXM888 / wjt 172957 (+ merged 172958) — stuck “Setting up Grok Bot's computer” Mac/iOS/Windows
- Colin 2026-09-25 05:18 UTC: aware; watch https://status.cursor.com/. Brand-new installs never connected. Reinforces standing can’t-reach / first-init / Reset family — **no new portable teach**. Bounce/reinforce. Alert: no.

### sd-tenbridge 172951 (+ merged Rick_Leffke 173018) — voice preference not persist (Android Sal; desktop Rex→Leona)
- Colin: known; mobile some bots don’t pick up saved voice/speed; mid-call changes last for that call; disk settings intact (desktop still correct). Soft voice UX ≈7. Alert: no.

### jsolly 172955 — delisted GitHub plugin 48677658 can’t uninstall; Connected with 0 tools after 401
- Same author / plugin-surface as 173019; empty PAT; can’t remove. Soft plugin-lifecycle watch — pair under Connected≠auth. Alert: no.

### tianmind 172989 — X assistant browser-automated posts froze account
- kevinn looking into. Not a this-week Wedge Settings action; do not roster X-posting bots. Bounce. Alert: no.

### doughy 171895 — update_state memory “brain docs snapshot cut short” (elevate watch)
- deanrie: known tracking; settings/file writes still work; Sep 17 routine outage was separate and fixed. Old thread, no new portable this-week teach. Bounce. Alert: no.

### Josiah_Fannon 173021 — Failed / “Not delivered yet” drafts undeletable (desktop)
- Feature request after computer-update interrupted sends. Soft UX. Alert: no.

### HorstHauser 172965 — three Surfaces rant; chiayu0816 172963 Cloud Agent timers bill — off Field path / Cloud Agents Brief bounce
### aptlabs 173020 — IDE agent switched to Grok against will — IDE not Grok Bot computer
### NeoLuca 173014 — Groups list serialize binary / CVP — Teams dashboard, Colin fix rolling; not Grok Bot Field
### jesse85 172902 — bigger plan / OpenAI-style reset FR — product request

## Standing kills reinforce (footer, not KEEP)
- Route-through rejects RFC1918 · Reset-fail/partial ≡ no access · Free-plan≡no-access (Peacerk/GFP) · Always-allow=text instruction prefer broader Auto-review Rules+prune; Ask-first wins (TheAviv) · Kaspersky/DNS/Zscaler/43% Transferring · Plugin Connected = first connector only (new, from 173019 KEEP)

FAILURE_COUNT=1
alert=no
