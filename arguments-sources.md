# Arguments sources — ingest only
# Clock: Mon/Wed/Fri 12:00 Asia/Taipei · CRON_TZ=Asia/Taipei 0 12 * * 1,3,5
# First-party fetches only · no Firecrawl · no ASR on the box · no third-party transcript sites
# Public only. Weekly included usage only. Never write vault, tan, tsumugu, or GitHub.

## Products
# INGEST (Triggernometry, a16z) — per new qualifying episode. Takeaways, arguments (claim → support → what is rejected), listed facts. Timestamped. 3–6 verbatim quotes ≤25 words. One paragraph at the end. Footer: url, length, text source (captions | official transcript | NOTES-ONLY).
# ASMON (Asmongold talk VODs only) — arguments plus one-sentence takeaway. No wiki-grade analysis. No full ingest dump. No listed-facts block, no quote block, no closing paragraph unless a single takeaway sentence. Footer still: url, length, text source. Skip highlight clips.

## Pinned (fetch these — do not add more)
- TRIGGERnometry · https://www.youtube.com/@Triggerpod
  Full INGEST. Do not thin unless Wedge says so.
- a16z · https://www.youtube.com/@a16z
  Scope: The a16z Show / AI episodes. Skip promo shorts, news recaps, and non-AI/non-show filler.
  Full INGEST. Do not thin unless Wedge says so.
- Asmongold talks · https://www.youtube.com/@asmontv
  Talk/argument VODs only. Skip highlight dumps, highlight clips, competitions, and clip compilations.
  If a video is not him making or testing an argument, skip it.
  Product: arguments + one-sentence takeaway only (not full INGEST).

## Not Arguments — Recap owns these
- All-In
- Naval
- Maxinomics
- Justin Sung

## Text source order
1. First-party YouTube captions (manual or auto, from YouTube itself)
2. The show's own transcript (official page / description / site)
3. Show notes, marked NOTES-ONLY

Never ASR on the box. Never Firecrawl. Never third-party transcript sites (DownSub, youtubetranscript, etc.).

## Files
- /workspace/arguments/YYYY-MM-DD-<slug>.md
- /workspace/arguments/latest.md (last 7 days of packets)
- /workspace/arguments-seen.json
- /workspace/arguments-sources.md (this file)

## Cadence
Live: Mon/Wed/Fri 12:00 noon Asia/Taipei · schedule CRON_TZ=Asia/Taipei 0 12 * * 1,3,5
Usage hygiene: Asmongold volume will kill the quota if every clip is ingested. Thin packets still cost caption fetches; skip highlight clips. Not daily.
