# Field Grok Bot failure hunt · packet 18 · 2026-08-31
Cutoff: after ~2026-08-29 13:39 UTC (Ber77 last keep). Forum JSON + latest HTML. X skipped. No packet file. field-seen.json untouched.

Forum grok-bot tag latest actually listed (created after cutoff, newest first):
170018 jsolly Fastmail Save silent no-op · 169982 zayadur credit drain · 170010 rseromenho setup · 170006 Jerell partial reset · 170000 j0hns reconnect-after-update · 169991 Olivier Zoom localhost OAuth · 169981 Mao Wang endless setup · 169973 Netanel VM down · 169971 Drive Docs in-place write (FR) · 169970 ravi 72h unreachable · 169967 c17a Drive PDF create_file · 169966 Glenn blank/WARP · 169965 Kingsley custom MCP · 169955 moves prompt-injection FR · 169940 Biniam (yesterday bounce) · 169939 David (yesterday bounce) · 169938 per-bot usage FR · 169934 Peter per-bot connectors FR · 169930 Mike8 (yesterday bounce) · 169926 znuttyone per-agent usage FR · 169924 Russ (yesterday bounce) · 169920 JR White won’t open.

## Candidates

### KEEP 1 — Chris Farrugia / c17a · Drive create_file truncates real PDFs
- url: https://forum.cursor.com/t/google-drive-connector-pdf-upload-issue/169967
- date: 2026-08-30 10:35 UTC (17:35 ICT 30 Aug)
- tags: coverage-ceiling, killed-claim
- portable 5 / evidence 5 / combined 10
- ran: Drive connector `create_file` with ~40–54KB PDFs as `base64Content` (tiny test PDFs OK). Grok Bot 0.30.0 macOS. Request ID 237e57f2-5381-476f-9cbc-d3e67aed3f61.
- failed: payload truncated/corrupted (60 bytes short, 8-byte junk, or a few KB vs ~46KB). Some attempts Auto-review “An error occured while classifying this action. Please review manually.”
- killed claim: Drive `create_file` uploads a real PDF intact.
- staff: Dean Rie 2026-08-30 11:05 UTC — known; contents sent as base64 *inside the tool call*; tens of KB unreliable on this path; Auto-review classify error is the same large-call symptom. Workaround: chat attachment then human upload, or box browser at drive.google.com (Google login once).
- distinct from 169971 (Drive metadata vs Docs/Sheets body — staff says use the other connectors). This is a payload-size ceiling on the tool that *does* exist.
- alert-line: no (connector payload, not a this-week first-party computer rule / roster tool add-remove).

### KEEP 2 — John Solly / jsolly · Fastmail Filters Save is a silent no-op on box Chrome
- url: https://forum.cursor.com/t/grok-bot-fastmail-filters-rules-save-is-a-silent-no-op-chrome-on-the-box/170018
- date: 2026-08-30 23:25 UTC (06:25 ICT 31 Aug)
- tags: gui-as-api, killed-claim, coverage-ceiling
- portable 5 / evidence 4 / combined 9
- ran: Grok Bot computer, desktop Chrome 151, Fastmail Settings → Filters & Rules and Sieve editor. Twice 2026-08-30 (~5:00 AM ET and ~7:10 PM ET). Linux box. Existing three rules still listed (reads work). Mail helper still search/trash/archive.
- failed: Save does nothing (no toast, no error). Chrome “Your unsaved changes will be discarded.” Reload: new rule/Sieve gone. GTK Open File for Import: Open/Enter/double-click are no-ops (only Escape closes); drag-and-drop did not attach.
- killed claim: clicking Save (or Import) in box Chrome persists mailbox rules.
- staff: none
- distinct from yesterday’s jsolly Always-allow `[3397 chars omitted]` (same person, different mechanism: GUI write ≠ persist vs approval Details truncated).
- alert-line: no (Fastmail-specific + GTK chooser ceiling; not a this-week computer rule Wedge would change).

### KEEP 3 — Olivier GUILLOUX · Zoom catalog plugin OAuth hardcodes localhost
- url: https://forum.cursor.com/t/grok-bot-zoom-plugin-oauth-hardcodes-http-localhost-8787-callback-zoom-rejects-hostname-localhost-error-4700/169991
- date: 2026-08-30 15:45 UTC (22:45 ICT 30 Aug)
- tags: coverage-ceiling, killed-claim
- portable 4 / evidence 5 / combined 9
- ran: catalog Zoom plugin connect from Grok Bot desktop macOS. Zoom General OAuth app. Live probes: `localhost` → 4700; `127.0.0.1` and `https://www.cursor.com/agents/mcp/oauth/callback` → login HTML.
- failed: redirect_uri always `http://localhost:8787/callback`. Zoom rejects hostname localhost (4700); Marketplace will not allowlist localhost. No in-app redirect parameter. Plugin stays needsAuth / 0 tools. Recreating the Zoom app does not help.
- killed claim: catalog Zoom plugin will complete OAuth from Grok Bot the way Cursor Agents docs say (HTTPS agents callback).
- staff: Dean Rie 2026-08-30 17:23 UTC — diagnosed correctly; redirect not configurable; no user workaround; tracking switch to 127.0.0.1.
- distinct from Shopticon Gmail OAuth (Google-blocked vs Zoom localhost-hostname policy; staff: no Cursor-path workaround here).
- alert-line: no (not adding Zoom this week).

### KEEP 4 — zayadur · Grok Bot drains Cursor credit pool with no Cloud Agents
- url: https://forum.cursor.com/t/grok-bot-draining-cursor-credit-pool/169982
- date: 2026-08-30 13:01 UTC (20:01 ICT 30 Aug)
- tags: killed-claim, coverage-ceiling
- portable 4 / evidence 4 / combined 8
- ran: long-horizon Bot on laptop + Grok Bot computer, 0.30.0 macOS. Stop bot → drain stops. Conversation 73684ad6-85e5-4e10-8fd3-f1fe1620c41a. 99% of his Cursor chats/agents are Grok 4.6 Extra High Fast — not the models on the meter.
- failed: Spending shows `claude-opus-5-thinking-low` and `cursor-grok-4.6-high-fast` while Bot runs. No Cloud Agents spawned (David Stredansky asked; OP no). icetique: 52M Claude Opus tokens at 38% Grok Bot weekly + Grok High-Fast. geerzo: same.
- killed claim: dedicated Grok Bot weekly pool means Cursor Models / Other Models meters stay still (and “sand-* under Other Models is display-only”).
- staff: none on *this* thread. Earlier deanrie (169796/169658, before cutoff) said included weekly is separate, overflow → On-Demand, dashboard does not split; mohitjain (169581) said sand-* won’t block Claude. This thread is the post-cutoff named counter-example with stop-bot = stop-drain.
- alert-line: no (billing/meter, not a this-week computer rule).

## Bounce siblings (one line each)
- Ricardo Seromenho 170010 couldn’t finish setup / Can’t reach computer, Grok Bot 0.18.0 Linux (install sibling) https://forum.cursor.com/t/grok-bot-couldnt-finish-setup/170010
- Jerell 170006 Reset failed “partial state”; reopen → Reconnecting / Couldn’t Reach; wants data-preserving backend recovery (reconnect sibling) https://forum.cursor.com/t/grok-bot-computer-stuck-in-partial-state-reset-failed-existing-cloud-computer-unreachable/170006
- John Smith / j0hns 170000 reconnect after update; Recover+Reset fail; staff Dean: Recover/Reset need a live session (often lost after password change); sign-out/in fixed it — Settings had shown `Cursor #user_01…` not the named account (reconnect sibling + session note) https://forum.cursor.com/t/unable-to-reconnect-to-my-grok-bots-computer-after-attempted-update/170000
- ravi kumar 169970 Can’t reach 72h; staff Colin: DNS, try 1.1.1.1/hotspot; OP: still black icon after 1.1.1.1 + office/home/mobile (DNS/black-screen sibling) https://forum.cursor.com/t/cant-reach-your-computer-from-last-72-hours/169970
- Mao Wang 169981 endless “Setting up your Grok Bot”; staff Dean: free Cursor plan never mints the computer; spinner instead of access message is a known wrong UI (install/entitlement sibling — not a this-week Wedge rule) https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981
- Netanel 169973 “VMs down”; staff Colin: his computer unreachable ~30 min then recovered (down sibling) https://forum.cursor.com/t/grok-bot-is-down/169973
- Glenn / glenn0 169966 blank after setup; Windows same account OK; OP: Cloudflare WARP on Mac; staff: WARP intercepts, split-tunnel/exclude (network sibling, new staff cause) https://forum.cursor.com/t/blank-screen-after-opening-grok-bot/169966
- Kingsley Felix 169965 no Windows settings form for custom MCP; staff Colin: tell the bot in chat, public HTTPS/SSE, not localhost; OP already working (Udbhav 168350 sibling) https://forum.cursor.com/t/grokbot-custom-connectors/169965
- GrokUser841719 169971 Drive MCP should write Doc body / Sheet cells; staff Colin: use Docs + Sheets connectors, same Google account, same file ID (FR, not a killed tool — staff says the write tools live next door) https://forum.cursor.com/t/grok-bot-drive-mcp-should-write-google-docs-body-and-sheet-cells-not-only-file-metadata/169971
- JR White 169920 Grok bot won’t open, images only, no repro text (install sibling; 2026-08-29 14:27 UTC, just after cutoff) https://forum.cursor.com/t/grok-bot-wont-open/169920
- Peter Sullivan 169934 connectors per-bot not account-wide (FR) https://forum.cursor.com/t/connectors-on-a-per-bot-basis-rather-then-universal-account/169934
- znuttyone 169926 + GrokUser841719 169938 per-agent usage meter (FR; 169938 merged into 169926) https://forum.cursor.com/t/per-agent-grok-bot-usage-who-worked-tokens-cache-and-cost-vs-the-weekly-pool/169926
- moves 169955 prompt-injection / per-bot isolation (FR, not a run failure) https://forum.cursor.com/t/grokbot-security-isolation-prompt-injection-protection/169955
- Mille / Mille_C 169879 spinning-while-idle (created 2026-08-29 02:52 UTC, *before* cutoff; Colin: known status-indicator bug — opposite of quiet-when-nothing)
- Yesterday bounce still live / bumped: Biniam 169940, Russ 169924, Mike8 169930, David Stredansky 169939, jsolly Always-allow 169902, Robert Moran 169868, Maxwell 169896, plus black-screen cluster 169833/169856/169852/169848 etc.

## Fetch failures
- `https://forum.cursor.com/search?q=Grok%20Bot%20order%3Alatest` HTML is JS-empty; used `/tag/grok-bot/l/latest.json` + `/latest.json` + per-topic `.json` (public, no login).
- WebFetch of 169982.json timed out once; curl/python recovered full thread.
- X hunt skipped (down). HN/Reddit: no new *named* Grok Bot killed-claim after Aug 29 (Peter Yang X-connector chatter is older; OpenClaw 403 is not Grok Bot).
- Did not sign in. Discourse latest + tag JSON + topic JSON were public.

## Bank deposits
- KEEP: `raw/grok-bot/2026-08-31-chris-farrugia-google-drive-connector-pdf-upload-issue.md` ← 169967
- KEEP: `raw/grok-bot/2026-08-31-john-solly-grok-bot-fastmail-filters-rules-save.md` ← 170018
- KEEP: `raw/grok-bot/2026-08-31-olivier-guilloux-grok-bot-zoom-plugin-oauth-hardcodes.md` ← 169991
- KEEP: `raw/grok-bot/2026-08-31-zayadur-grok-bot-draining-cursor-credit-pool.md` ← 169982
- bounce staff-rule: `raw/grok-bot/2026-08-31-mao-wang-grok-bot-0-30-0-stuck.md` ← 169981
- bounce staff-rule: `raw/grok-bot/2026-08-31-john-smith-unable-to-reconnect-to-my-grok.md` ← 170000
- bounce staff-rule: `raw/grok-bot/2026-08-31-glenn-blank-screen-after-opening-grok-bot.md` ← 169966
- INDEX grok-bot lane now 12 (was 5). URLs were absent from INDEX before deposit.

Packet recommendation: if cap 2, take c17a + jsolly (strongest new mechanisms). If cap 3, add Olivier (distinct OAuth from Shopticon). zayadur is real but billing-meter, weaker portable gate. No alert-line. No packet file written. field-seen.json not edited.
