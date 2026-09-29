---
id: 2026-09-28-wgg-mohitjain-grok-bot-chat-image-file-attachments
kind: article
title: "Grok Bot: chat image/file attachments fail while text OK — computer dead; Recover not Reset (mohitjain)"
source: "https://forum.cursor.com/t/grok-bot-chat-image-file-attachments-fail-to-send-3-pcs-since-2026-09-26-text-ok/173187"
author: WGG; mohitjain
published: 2026-09-28
captured: 2026-09-28
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot: chat image/file attachments fail to send (3 PCs, since 2026-09-26; text OK)
- id: 173187
- url: https://forum.cursor.com/t/grok-bot-chat-image-file-attachments-fail-to-send-3-pcs-since-2026-09-26-text-ok/173187
- created: 2026-09-28T06:14:30Z (UTC)
- last: 2026-09-28T08:50:45Z
- tags: [{'id': 272, 'name': 'chat', 'slug': 'chat'}, {'id': 416, 'name': 'grok-bot', 'slug': 'grok-bot'}]
- posts: 5
- staff: ['mohitjain', 'system']

## #1 WGG · 2026-09-28T06:14:30Z
Summary Grok Bot cannot send pasted/dragged images or file attachments in chat. Plain text works. Reading images via a full local desktop path still works, so this is not a vision/OCR failure. The chat attachment upload channel is broken. What happens Pasting, dragging, or attaching images/files in the chat composer fails to send UI shows: “Will send after reconnecting” or “Unable to send your message. Please check the network connection and try again.” Plain-text messages still send normally Asking the bot to read an image by full local path still works Scope Same account, at least 3 PCs, same failure (not a single-machine config issue) “Update Grok Bot’s Computer” did not fix it Timeline (Asia/Shanghai) Last successful chat-attachment write on disk: ~2026-09-26 16:22 No new chat attachments after that User clearly reported the issue starting ~2026-09-27 (“cannot read images / attachments will not send”) Environment App: Grok Bot 0.61.0 on Windows 10 signedIn=true, crashSeen=false Sidebar status: Backup not ready egressTunnelEnabled=false (egress tunnel; unrelated to chat attachment upload; toggling it does not fix this) Already tried (no fix) Full quit and relaunch of Grok Bot System proxy enabled (127.0.0.1:7897) DNS set to 1.1.1.1 / 8.8.8.8 and flushdns Update Grok Bot’s Computer Reproduced drag/upload failure on three PCs Conclusion / Ask This looks like an app/account-side shared chat-attachment upload failure. Please restore paste/drag/file attachment upload in chat, and tell us ETA or any temporary workaround. Evidence (optional) Desktop evidence image: C:\Users\Administrator\Desktop\grok_upload_fail_evidence.png (Please attach via the form Upload / + button.)

## #4 system [STAFF] · 2026-09-28T06:14:43Z

## #5 system [STAFF] · 2026-09-28T06:14:47Z
Hi, Thanks for posting on the Cursor forum! To help ensure most of our users can participate in discussions, this forum is currently English only. If you’d like, you can edit your post to translate it into English. Once it meets our guidelines, it will be automatically relisted. Thanks for understanding! Note: This is an automated detection system and sometimes makes mistakes. If your post is already in English, feel free to ignore this message, or just make a small edit and it will be reviewed again.

## #9 mohitjain [STAFF] · 2026-09-28T08:50:29Z

## #10 mohitjain [STAFF] · 2026-09-28T08:50:45Z
Hey @WGG , Here’s what’s happening: plain text goes straight to our servers, but pasted or dragged images and files upload to your Grok Bot computer first. Your computer stopped responding around Sep 26 (about 16:24 your time), so attachments get stuck on “Will send after reconnecting” while text keeps working. That same state is why Update stalls at “Backup not ready.” I’ve rebuilt your Grok Bot computer from your last saved snapshot on our side. Please fully quit Grok Bot (not just close the window), reopen it, wait for it to reconnect, then try pasting or dragging an image again. A couple of things to know: Anything changed on the computer after around Sep 26 16:22 may not carry over, and any apps or packages you installed there will need reinstalling. Your bots and chats are kept. If you ever hit this again, use Recover (Settings → Updates), not Reset - Reset can drop recent bots and files. If attachments still fail after a full quit and reopen, reply here and I’ll take another look.
