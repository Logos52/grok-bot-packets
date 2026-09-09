---
id: 2026-09-09-wes-anderson-grok-bot-box-secrets-wiped-overnight
kind: article
title: "Grok Bot box secrets wiped overnight (Shopify Client ID/secret)"
source: "https://forum.cursor.com/t/grok-bot-box-secrets-wiped-overnight-shopify-client-id-secret/171029"
author: Wes_Anderson
published: 2026-09-08
captured: 2026-09-09
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot box secrets wiped overnight (Shopify Client ID/secret)
URL: https://forum.cursor.com/t/grok-bot-box-secrets-wiped-overnight-shopify-client-id-secret/171029
Created: 2026-09-08T11:49:34.383Z

## Wes_Anderson — 2026-09-08T11:49:34.440Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug II asked my Grok Bot(Coach) to explain the problem we ran into trying a workaround since we do not have a Plugin for Shopify.(Wes) Coach: Twice in a row, stored Shopify app credentials disappeared from my Grok Bot computer’s secrets store overnight. I did not click Update Grok Bot’s Computer or Reset. Setup Custom Shopify app using client_credentials (Client ID + Client secret) Stored via Grok Bot’s secure secret input (not pasted in chat) A daily 5:00 AM CT routine reads those secrets, mints a ~24h Admin API token, and saves the token in an agent folder What happened Sep 7, ~3:24 AM CT: secrets store was empty. The existing Admin token file was still there and API calls still worked until that token expired later that day. I re-entered Client ID and secret. Refresh succeeded. Sep 8, 5:12 AM CT: secrets store empty again (zero secrets). Token file still present. A one-order read still returned HTTP 200, but the token was about to expire. I re-entered both credentials again and the refresh succeeded. What I did not do Did not run Update Grok Bot’s Computer or Reset Auto-update when idle is off Did not rotate the Shopify client secret Ask Is box-secrets expected to persist across overnight computer sync/refresh? If something clears that file without Update/Reset, can it be fixed so API credentials survive until the user removes them? Steps to Reproduce Coach: In Grok Bot, store two secrets with the secure secret input (not chat): SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET. Confirm a routine can read them from the box secrets store and mint a Shopify Admin API token. Save that token in an agent folder (not in the secrets file). Leave Grok Bot running overnight. Do not click Update Grok Bot’s Computer or Reset. Do not remove the secrets. Next morning, check the box secrets store. Expected: both secrets are still there. Actual (Sep 7 ~3:24 AM CT and Sep 8, 5:12 AM CT): secrets store is empty. The separate Admin token file is still present until that token expires. I can’t force it on demand. It has happened two nights in a row after secrets were stored this way. Expected Behavior Coach: Secrets stored with Grok Bot’s secure secret input should stay on the computer until I remove them or rotate them. An overnight run, and not clicking Update or Reset, should not empty that store. A scheduled job that reads those secrets the next morning should still find them. Operating System Windows 10/11 Version Information Grok Bot 0.43.0 For AI issues: which model did you use? Grok Bot Additional Information Additional context Happened two nights in a row (Sep 7 and Sep 8, US Central). Secrets were entered with Grok Bot’s secure secret input, not pasted in chat. Next morning the secrets store was empty. A short-lived API token saved in a separate agent file was still there and still worked until it expired (~24 hours). I did not click Update Grok Bot’s Computer or Reset. Auto-update when idle is off. I did not rotate the app credentials in Shopify. After I re-entered the same two secrets via the secure input, the morning refresh succeeded immediately both times. Impact: any job that needs those stored credentials fails until they are entered again. The leftover token only covers the gap until it expires. Does this stop you from using Cursor Yes - Cursor is unusable

## Colin — 2026-09-08T12:59:08.780Z
Hey @Wes_Anderson , thanks for the report! You did nothing wrong here, and this isn’t caused by Update or Reset. We were able to confirm what happened: right now, whenever the Grok Bot desktop app reconnects to your Grok Bot computer (for example after your PC sleeps or the connection drops overnight), it re-syncs its own list of secrets to the computer, and that sync currently overwrites anything that was saved through the in-chat secure input. That matches your logs exactly (both wipes happened in the evening, right when the app reconnected). We’re tracking this and I’ve added your report.

## Wes_Anderson — 2026-09-08T14:21:12.461Z
Yes that was it. I closed the Grok Bot Desktop app then reopened it. Credentials were okay before that and wiped after that. Fingers crossed on the Shopify Connector approach whenever Cursor can build it. Thanks! Wes
