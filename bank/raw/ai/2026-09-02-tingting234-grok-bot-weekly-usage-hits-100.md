---
id: 2026-09-02-tingting234-grok-bot-weekly-usage-hits-100
kind: article
title: "Grok Bot: weekly usage hits 100% after bot-to-bot reviews the user asked to stop"
source: "https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271"
author: Tingting234
published: 2026-09-01
captured: 2026-09-02
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot: weekly usage hits 100% after bot-to-bot reviews the user asked to stop

URL: https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271

created: 2026-09-01T23:01:12.491Z

--- @ting-ting234 2026-09-01T23:01:12.549Z ---

<h3><a name="p-480501-where-does-the-bug-appear-featureproduct-1" class="anchor" href="#p-480501-where-does-the-bug-appear-featureproduct-1" aria-label="Heading link"></a>Where does the bug appear (feature/product)?</h3>
<p>Grok Bot</p>
<h3><a name="p-480501-describe-the-bug-2" class="anchor" href="#p-480501-describe-the-bug-2" aria-label="Heading link"></a>Describe the Bug</h3>
<p>Grok Bot burned the included weekly usage on a multi-bot review loop, then locked the account. Specialist bots (QC, UAT, Coding, UIUX) kept talking after you asked them to stay quiet and send the verdict to Command Agent only.</p>
<p>Sidebar: Weekly usage 100%<br>
Banner: You’ve reached your Grok Bot usage limit. It resets in 3 days.<br>
Fired 2 times between 06:37:17 AM and 06:37:38 AM<br>
CTA: Upgrade to Pro+</p>
<h3><a name="p-480501-steps-to-reproduce-3" class="anchor" href="#p-480501-steps-to-reproduce-3" aria-label="Heading link"></a>Steps to Reproduce</h3>
<p>after you review, sending back to the command agent. I only wanna do the job in the command agent<br>
UAT Bot replied that the verdict would go to Command Agent and it would keep the chat quiet. The bots kept exchanging collapsed groups of messages anyway.</p>
<h3><a name="p-480501-expected-behavior-4" class="anchor" href="#p-480501-expected-behavior-4" aria-label="Heading link"></a>Expected Behavior</h3>
<p>Bot-to-bot bounce-backs should stop — or at least not eat the weekly quota — when you say you only want to work in Command Agent. The limit banner should not fire twice in 21 seconds.</p>
<h3><a name="p-480501-screenshots-screen-recordings-5" class="anchor" href="#p-480501-screenshots-screen-recordings-5" aria-label="Heading link"></a>Screenshots / Screen Recordings</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/cursor1/original/3X/4/e/4ef26eb651ebf1ff1c4aa9847de7594278a3bc94.png" data-download-href="/uploads/short-url/bgoEpLMdLCVEVGv1jtQA1RCbeUA.png?dl=1" title="Screenshot 2026-09-02 at 6.48.26 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/cursor1/optimized/3X/4/e/4ef26eb651ebf1ff1c4aa9847de7594278a3bc94_2_456x500.png" alt="Screenshot 2026-09-02 at 6.48.26 AM.png" data-base62-sha1="bgoEpLMdLCVEVGv1jtQA1RCbeUA" width="456" height="500" srcset="https://us1.discourse-cdn.com/cursor1/optimized/3X/4/e/4ef26eb651ebf1ff1c4aa9847de7594278a3bc94_2_456x500.png, https://us1.discourse-cdn.com/cursor1/optimized/3X/4/e/4ef26eb651ebf1ff1c4aa9847de7594278a3bc94_2_684x750.png 1.5x, https://us1.discourse-cdn.com/cursor1/optimized/3X/4/e/4ef26eb651ebf1ff1c4aa9847de7594278a3bc94_2_912x1000.png 2x" data-dominant-color="1A191A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-09-02 at 6.48.26 AM.png</span><span class="informations">1606×1760 372 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-480501-operating-system-6" class="anchor" href="#p-480501-operating-system-6" aria-label="Heading link"></a>Operating System</h3>
<p>MacOS</p>
<h3><a name="p-480501-version-information-7" class="anchor" href="#p-480501-version-information-7" aria-label="Heading link"></a>Version Information</h3>
<p>Grok Bot Desktop</p>
<h3><a name="p-480501-does-this-stop-you-from-using-cursor-8" class="anchor" href="#p-480501-does-this-stop-you-from-using-cursor-8" aria-label="Heading link"></a>Does this stop you from using Cursor</h3>
<p>No - Cursor works, but with this issue</p>
