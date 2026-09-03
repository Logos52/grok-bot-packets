# Field Grok Bot failure hunt · packet 2026-09-03
Cutoff: after ~2026-09-01 00:00 UTC. Forum tag JSON (`/tag/grok-bot/l/latest.json` pages 0–2). Public, no login. X skipped. No packet file. field-seen.json untouched.

Already kept (skipped): Tingting234 170271, Emman Recover 170231, Axel 170265, jsolly 170255.
Already bounced Sep1–2 ops/white-dot cluster (skipped): 170208, 170214, 170221, 170235, 170239, 170241/242, 170247, 170248, 170251, 170256, 170258, 170270 (+170319 black-dot sibling).

## KEEP candidates (3)

### KEEP 1 — digvijaysai_g · computer unreachable but webhook/routines still burn; pause path needs the box
- url: https://forum.cursor.com/t/grok-bot-0-30-0-unusable-for-4-days-cant-reach-computer-stuck-previous-image-webhook-routines-still-burn-usage/170315
- date: 2026-09-02 08:36 UTC (15:36 ICT 2 Sep)
- tags: coverage-ceiling, killed-claim, quiet-when-nothing
- score: 8 (portable 4 / evidence 4)
- packet one-liner: [agentic·coverage-ceiling·killed-claim·quiet-when-nothing] score=8 | digvijaysai_g | Grok Bot 0.30.0 macOS. Shared Agent Computer unreachable 4+ days (“previous image” / Reset partial). **Webhook/routine jobs kept firing** while interactive use was dead. Could not pause routines: Routine controls appear to need the computer online; messaging the bot stuck on “waiting for the bot and computer to come online.” Later self-diagnosed ISP DNS (Reliant Geo Infocom India) blocking `*.cursorvm.com`; Cloudflare 1.1.1.1 restored reachability — staff deanrie confirmed the DNS pattern and clearer-error feedback. Usage billed while “unreachable” → hi@cursor.com. Killed: when the computer is down, scheduled/webhook routines stop — or there is an offline path to pause them all. Distinct from Tingting234 170271 (inter-bot chat burns weekly while user said stop) and kenners22 169841 (routine ok, no bubble) — here **background runs continue past an unreachable box with no offline kill switch**. Alert: no (DNS staff-rule + billing email; not a this-week roster paste).
- staff: system auto-unlisted as billing → deanrie re-listed; DNS diagnosis affirmed; usage check via email.
- bank: raw/grok-bot/2026-09-03-digvijaysai-g-grok-bot-isp-dns-blocks-cursorvm.md

### KEEP 2 — o_Oaii · scheduled routines queue late + finish with no chat bubble
- url: https://forum.cursor.com/t/grok-bot-routines-dont-auto-run-on-schedule/170358
- date: 2026-09-02 15:15 UTC (22:15 ICT 2 Sep)
- tags: quiet-when-nothing, killed-claim
- score: 9 (portable 5 / evidence 5)
- packet one-liner: [agentic·quiet-when-nothing·killed-claim] score=9 | o_Oaii | Multi-routine bot (created Windows, watched iOS). Scheduled slots looked like misses (no notification; “Next run” = “Run now”). Delete/recreate + Active toggle did not help. Control routine on another bot (file-write, not chat) looked healthy. Staff Colin: every slot *did* fire but sat in a **queue 10–37 min**; when runs executed they **finished without posting a chat message**. Instruction edits and creation platform ruled out. Killed: scheduled routine starts on time *and* leaves a visible chat bubble. Distinct from kenners22 169841 (status=ok, on-time fire, no bubble) — here staff names the **queue delay** (“Run now” = queued) *plus* silent finish. Alert: no.
- staff: Colin 2026-09-02 16:22 UTC — both issues known/tracked; chat message still the reliable on-demand check-in.
- bank: raw/grok-bot/2026-09-03-o-oaii-grok-bot-routines-do-not-auto.md

### KEEP 3 — im_grok · Reset partial state → first-run empty UI; Recover restores bots but VM still unreachable
- url: https://forum.cursor.com/t/grok-bot-0-30-0-windows-can-t-reach-computer-after-failed-reset-partial-state-bots-visible-vm-won-t-connect/170373
- date: 2026-09-02 18:48 UTC (01:48 ICT 3 Sep)
- tags: persistent-computer, killed-claim
- score: 8 (portable 4 / evidence 5)
- packet one-liner: [agentic·persistent-computer·killed-claim] score=8 | im_grok | Grok Bot 0.30.0 Windows 11. Computer froze → Reset stuck on “Wiping your data” → “Reset failed… may be in a **partial state**.” App then showed first-run “Create your first Bot” with no chats. Sign-out/in + **Recover** brought sidebar bots back (LIFE BOT, God View, Chase, Morgan, Rex, …) but still “Couldn’t Reach Grok Bot’s Computer — Your Bots, files, and logins are safe.” Retry no-op; did not Reset again. DNS/HTTPS to `*.cursorvm.com` OK (curl 404 awselb); generic firewall/Zscaler banner looks false. Staff kevinn investigating. Killed: Recover after a failed Reset reconnects the existing VM (not sidebar-only restore while the computer stays unreachable / first-run flash). Distinct from Emman 170231 (Recover **minted a new** bot; originals gone) and Jerell 170006 (partial reset, wants backend recovery) — here **Recover restores the roster but not the VM link**, with a false empty first-run surface mid-failure. Alert: no (don’t-Reset warning sibling; not a this-week routine change).
- staff: kevinn 2026-09-02 ~20:57 UTC — investigating internally.
- bank: raw/grok-bot/2026-09-03-im-grok-grok-bot-reset-partial-state-bots.md

## BOUNCE

### Named / adjacent (not kept this pass)
- Chen_Zhanfeng 170157 Linux Always-allow + ListMachines=[] — known 0.30.0; fix merged; keyring workaround (Jake_Sun 169877 sibling; demoted so packet can take the three directed keeps) https://forum.cursor.com/t/grokbot-linux-execution-on-local-computer-not-working/170157
- directs1357-lang 170337 Sentry issueCreated never triggers; lastRunAt empty (sibling of insoo970923 168421) https://forum.cursor.com/t/grok-bot-sentry-issuecreated-routine-never-triggers-despite-new-sentry-issue/170337
- PEI_NAN_JIANG 170281 fresh-profile Can’t reach — staff: app ignores system proxy; needs VPN TUN; OP fixed (Glenn WARP network sibling) https://forum.cursor.com/t/grok-bot-windows-fresh-profile-setup-fails-with-can-t-reach-your-computer-after-backend-fix/170281
- Ben_McBride 170331 iOS Can’t reach CoS; Recover not offered — staff force-quit (ops) https://forum.cursor.com/t/grok-bot-ios-can-t-reach-chief-of-staff-s-screen-recover-not-offered/170331
- tangjun 170283 weekly usage 4%→0% early (anecdote) https://forum.cursor.com/t/grok-bot-reset-usage-early/170283

### Sep 2–3 ops / white-dot / can’t-reach cluster (group bounce)
- Aydin_Mirzaee 170383 blank screen
- Dan_Baker 170356 black screen (staff backend tweak)
- David12 170360 reconnecting (staff: healthy now)
- Korbi 170342 infinite white circle iOS+macOS (staff tweak → working)
- art049 170328 “Bot failed to respond” every message (staff: box healthy)
- jivn 170327 first-setup Mac/Windows Jio+Airtel (staff → DNS 170320)
- xprayag 170320 can’t-reach Reset requested (staff DNS IPv4+IPv6 → fixed)
- Scott_Kim 170317 stuck starting since Aug 28 iPhone (staff backend tweak)
- Edwin_Cunanan 170294 black spinner Windows (staff: Zscaler)
- RuggeroCipriani 170319 black dot white screen (staff backend tweak)

### FR / announce / off-hunt
- kevinn 170384 Android live (announce)
- Bello 170359 Plaid connector FR
- Elisha_Cohen 170305 Chrome extension FR
- Bram_Vaessen 170216 minimize-to-tray FR
- amitmirgal 170300 orgbots pack directory (library)
- 170186 San Salvador meetup

### Already-kept / already-bounced (window)
- Tingting234 170271 · Emman 170231 · Axel 170265 · jsolly 170255
- Sep1 ops cluster 170208/214/221/235/239/241–242/247/248/251/256/258/270

## Fetch failures
- `/c/grok-bot/l/latest.json` → 404; `/c/grok-bot/33/l/latest.json` → 404
- `/tags/grok-bot/l/latest.json` → 301; JSON works at `/tag/grok-bot/l/latest.json` (+ page=1, page=2)
- Topic IDs 170241 / 170256 from yesterday bounce list → 404 (deleted/unpublished)
- Public topic JSON often omits `raw`; used cooked HTML strip (no login)
- X / Slack / Gmail not used

## Bank deposits
- KEEP: `raw/grok-bot/2026-09-03-digvijaysai-g-grok-bot-isp-dns-blocks-cursorvm.md` ← 170315
- KEEP: `raw/grok-bot/2026-09-03-o-oaii-grok-bot-routines-do-not-auto.md` ← 170358
- KEEP: `raw/grok-bot/2026-09-03-im-grok-grok-bot-reset-partial-state-bots.md` ← 170373
- Also on disk from earlier pass (now bounce): Chen_Zhanfeng 170157

## Packet recommendation
Keep count: **3** — digvijaysai_g 170315, o_Oaii 170358, im_grok 170373. No alert-line. No packet file written. field-seen.json not edited.
