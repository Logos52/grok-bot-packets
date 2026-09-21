---
id: 2026-09-20-bigbojangles-deanrie-copyfrombox-read-local-exec-root-profile
kind: article
title: CopyFromBox/Read local-exec root — profile-only; Shell OK (BigBojangles)
source: "https://forum.cursor.com/t/copyfrombox-and-read-refuse-paths-outside-user-profile-after-0-57-1-outside-the-allowed-local-exec-root/172349"
author: BigBojangles / deanrie
published: 2026-09-19
captured: 2026-09-20
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# CopyFromBox and Read refuse paths outside user profile after 0.57.1 (outside the allowed local-exec root)
url: https://forum.cursor.com/t/copyfrombox-and-read-refuse-paths-outside-user-profile-after-0-57-1-outside-the-allowed-local-exec-root/172349
created: 2026-09-19T14:05:56.839Z

## @BigBojangles (2026-09-19T14:05:56.869Z)
Where does the bug appear (feature/product)? Grok Bot Describe the Bug CopyFromBox and Read refuse any path outside the user profile with the error “outside the allowed local-exec root.” I first noticed this on 0.53.0 and it is still present after updating to 0.57.1. Before that update I could copy files straight to a project folder on another drive. Shell still reads and writes those same paths fine, so this is not a broken disk. CopyFromBox and Read are affected. Shell and tools scoped to the user profile still work. Workaround: CopyFromBox into the home directory first, then move the file with Shell. Steps to Reproduce On Windows Grok Bot with a registered PC Create or use any folder on a non-system drive (for example D:\ or E:) or otherwise outside the user profile Attempt to Read a file in that folder with the Read tool Attempt to CopyFromBox a file into that folder Both return “outside the allowed local-exec root” Confirm Shell can read and write the same path Confirm CopyFromBox into the user profile or home directory still works Expected Behavior Read and CopyFromBox should reach folders outside the user profile the same way Shell does, as they did before the mid-September client updates. Operating System Windows 10/11 Version Information Grok Bot 0.57.1 (Windows desktop) Additional Information I reviewed the desktop-stable changelog entries from Sep 5 to 19. The only changelog entry that seems related is 0.53.0 Dynamic tool catalog support on stable. Does this stop you from using Cursor No - Cursor works, but with this issue

## @deanrie (2026-09-19T15:32:42.428Z)
Hey, thanks for the detailed report. What you’re seeing is how the local machine connection works right now, not a bad drive or something misconfigured on your side. On the registered machine, the Read and CopyFromBox tools plus CopyToBox are limited to your user profile folder C:\Users\<you> , while Shell isn’t. That’s why Shell can read and write to paths on D:\ or G:\ , but the file tools reject them. A junction or symlink inside your profile that points to another drive is also rejected because the check uses the real path. Your workaround is correct. Have the bot do CopyFromBox into the home folder, then move the file with Shell . Or read and copy files on other drives directly via Shell , for example Get-Content or Copy-Item in PowerShell. I passed this to the team. The direction is either file tools should reach the same locations as Shell , or the bot should know about this limitation ahead of time and pick Shell instead of failing. I’ll post here when there’s an update.
