# Field 2026-09-03 candidates (compiler notes)

## KEEP
### education SETUP — anatoly314 / AnkiMCP
url: https://github.com/ankimcp/anki-mcp-server
who: Anatoly Tarnavsky (anatoly314); rosaunde on scheduling PR
date: push 2026-08-31 20:15 UTC (03:15 ICT 1 Sep) — v0.25.0 forgetCards/setDueDate
mechanism: tutor-loop, killed-claim, generated-input, teach-once
score: mech 5 + evid 4 = 9
notes: MCP exposes present_card/rate_card tutor session; addNotes can batch-write. Explicit note: forgetCards/setDueDate reschedule WITHOUT logging a review — rating Again to bury permanently skews ease. Distinct from bornayo7 (SRS host+review queue), overtonch (YT→lemma Make/Discard), sergiyclas (in-page prepare/commit), Segar (held-out QC).

### agentic FAILURE — digvijaysai_g
url: https://forum.cursor.com/t/grok-bot-0-30-0-unusable-for-4-days-cant-reach-computer-stuck-previous-image-webhook-routines-still-burn-usage/170315
date: 2026-09-02 08:36 UTC (15:36 ICT 2 Sep); deanrie 11:29 UTC
mechanism: killed-claim, persistent-computer, coverage-ceiling
score: 5+5=10
notes: ISP DNS fails *.cursorvm.com → UI says can't-reach / stuck previous image / Reset failed while box is healthy. Cloudflare 1.1.1.1 fixes. Webhooks still burn usage while unreachable and can't pause. Related jivn 170327 Jio/Airtel. ALERT candidate: set DNS before Reset.

### agentic FAILURE — o_Oaii
url: https://forum.cursor.com/t/grok-bot-routines-dont-auto-run-on-schedule/170358
date: 2026-09-02 15:15 UTC; Colin 16:22 UTC
mechanism: quiet-when-nothing, killed-claim
score: 5+5=10
notes: Colin: routines DID fire every slot but queued 10–37 min late; finished without chat message so looked like total misses. "Next run = Run now" = queued. Editing instructions / recreate does not fix.

### agentic FAILURE — im_grok
url: https://forum.cursor.com/t/grok-bot-0-30-0-windows-can-t-reach-computer-after-failed-reset-partial-state-bots-visible-vm-won-t-connect/170373
date: 2026-09-02 18:48 UTC
mechanism: killed-claim, persistent-computer
score: 4+4=8
notes: Reset hung on wiping → partial state → false first-run empty UI. Recover restored sidebar bots; computer still unreachable. DNS already public. Distinct from Emman Recover-minted-new-bot.

## BOUNCE highlights
- Android 170384 → Brief (tool announcement)
- Sep2 templates ×14 (library as group; Code Red human-gate one-liner only)
- SystemicVoid anki-api (stale Jul 24)
- Brain-Dump (Mar tutorial)
- ops blank/black/can't-reach cluster
- Sentry issueCreated 170337 (listener never fires — thin single report)
