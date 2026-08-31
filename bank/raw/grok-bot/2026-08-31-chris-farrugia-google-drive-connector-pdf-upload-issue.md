---
id: 2026-08-31-chris-farrugia-google-drive-connector-pdf-upload-issue
kind: article
title: Google Drive connector PDF upload issue
source: "https://forum.cursor.com/t/google-drive-connector-pdf-upload-issue/169967"
author: Chris Farrugia
published: 2026-08-30
captured: 2026-08-31
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

Chris Farrugia (c17a): Google Drive connector create_file cannot reliably upload ~40–54KB PDFs as base64Content. One file landed 60 bytes short; others 8-byte junk or a few KB instead of ~46KB. Tiny test PDFs upload fine. Some attempts hit Auto-review 'An error occured while classifying this action. Please review manually.' Grok Bot 0.30.0 macOS. Request ID 237e57f2-5381-476f-9cbc-d3e67aed3f61. Staff Dean Rie (2026-08-30 11:05 UTC): known; Drive connector sends file contents as base64 inside the tool call; tens of KB unreliable on this path; Auto-review classify error is the same large tool-call symptom. Workarounds: send PDF as chat attachment then upload to Drive yourself; or upload via browser at drive.google.com (Google login once).
