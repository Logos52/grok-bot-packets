# Grok Bot (macOS): persistent "Can't reach your computer"

- url: https://forum.cursor.com/t/grok-bot-macos-persistent-cant-reach-your-computer/171170
- topic_id: 171170
- created_at: 2026-09-09T14:41:14.563Z
- author: Teddy1
- via: grok-bot/Field
- lane: ai
- deposited: 2026-09-10

## @Teddy1 · 2026-09-09T14:41:14.635Z

Where does the bug appear (feature/product)? Grok Bot Describe the Bug I created a new account and cannot Grok bot keeps failing trying to set up the computer. I have tried on both desktop and mobile. I’ve tried switching my default browser from Brave to Safari, I’m not running a VPN, and I’m on my home network with no firewall. I have tried logging out and signing back in as well. Any help would be greatly appreciated! Happy to provide further details. Steps to Reproduce Open Grok Bot on mac or mobile “Connecting to Grok Bot’s computer” never completes loading The retry button on the mac app does not work. The “recover computer” button does not work either → says “Reset failed. The reset couldn’t finish. Grok Bot’s computer may be in a partial state.” Operating System MacOS Version Information Version 0.44.0 on mac iOS ap is 1.6.0 Does this stop you from using Cursor Yes - Cursor is unusable

## @deanrie [staff] · 2026-09-09T15:13:22.692Z

Hey, thanks for the detailed report. First off, it’s not your network, browser, or VPN, so there’s no point changing those next. This isn’t a setup issue on your side. What’s happening: on a new account, the Privacy Mode choice hasn’t been explicitly saved yet, and Grok Bot needs that saved choice to connect to its computer. Until it’s set, every connection attempt gets rejected, and Retry / Recover / Reset can’t move forward either. How to unblock it: In your browser, go to cursor.com/dashboard and sign in with the same account you’re using in Grok Bot. Open Settings and find the Privacy section. Select Privacy Mode, not the Legacy option, keep data sharing turned off, and confirm. Fully quit Grok Bot on your Mac with Cmd+Q , then open it again. If it still says Connecting after a minute, click Retry once. If it’s still stuck after a couple minutes, use Reset once. Since the account is new, there’s nothing important on the computer to lose, and Reset should complete now. Your iPhone will sync automatically as soon as the Mac connects. If it still doesn’t work after this, send the attempt time with your timezone and we’ll dig in further. This is a known issue we’re tracking.

## @Teddy1 · 2026-09-09T16:09:18.764Z

FWIW step 6 is what worked. Thank you!
