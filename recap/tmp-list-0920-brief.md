# Recap daily noon 2026-09-20 — executor brief

You are running Recap's daily noon Asia/Taipei clock for Wedge. Do LIST + INGEST. Report only to parent Recap automation; do not message Wedge.

## Goal
1. LIST every pin for what's new since last pass (2026-09-19 ~04:00 UTC / noon Asia/Taipei yesterday).
2. INGEST any NEW long-form episodes published since that pass (newest first; if heavy, LIST + newest 1-2 and list deferred).
3. Write under /workspace/recap/. Update /workspace/recap-seen.json and rebuild /workspace/recap/latest.md (last 7 days packets, newest first).
4. If every pin is nothing-new AND no INGEST: write /workspace/recap/tmp-list-0920/quiet.json with {"quiet":true,"date":"2026-09-20"} — parent will stay silent.

## Pins only
- All-In: RSS https://allinchamathjason.libsyn.com/rss + YT https://www.youtube.com/@allin/videos
- Maxinomics: https://www.youtube.com/@Maxinomics/videos
- Justin Sung: https://www.youtube.com/@JustinSung/videos
- Elon sit-downs: sit-down interviews where Elon is guest (not wraps/clips/daily X)
- Fern English: https://www.youtube.com/@fern-tv/videos
- Moon English: https://www.youtube.com/@Moon-Real/videos
- Frontpage English: https://www.youtube.com/@frontpagechannel/videos
- Naval parked: only note if published (RSS https://naval.libsyn.com/rss)

Skip shorts, clip dumps, clones, German Fern, Arguments pins.

## Already ingested (do NOT re-ingest)
See /workspace/recap-seen.json. Latest per show:
- all-in: Bill Gurley Searching for Feynman 2026-09-19 https://www.youtube.com/watch?v=A4Q7zAayW20
- moon: Satisfying Collapse of Bullsh*t Consulting 2026-09-17 https://www.youtube.com/watch?v=NQmRUeEkpFk
- fern: El Mencho 2026-09-16 https://www.youtube.com/watch?v=d61n1isTfeo
- frontpage: Gig Economy 2026-09-17 https://www.youtube.com/watch?v=MPEEITJd19A
- justin-sung: 5 Thinking Habits 2026-08-28 https://www.youtube.com/watch?v=6Z3I-9HvBQA
- maxinomics: China Found Something Better Than Oil 2026-09-11 https://www.youtube.com/watch?v=BXLGV0Sj0n8
- elon: Economist 2026-07-23 + All-In Elon+Shotwell already done

Mirror LIST format: /workspace/recap/2026-09-19-list.md
Sources: /workspace/recap-sources.md

## Fetch
mkdir -p /workspace/recap/tmp-list-0920
Use yt-dlp / curl. Flat-playlist ends ~12-15. Duration: skip under ~10 min unless clearly long ep; skip All-In Summit intro-style short clips.
Elon: light check for NEW sit-downs since 09-19 only.

## INGEST if new long-form
First-party captions only:
  yt-dlp --skip-download --write-auto-sub --sub-lang en --sub-format vtt/srv3/json3
Never ASR, never third-party transcript sites, never Firecrawl, never recap from memory.
Before fetch: rg -F URL /workspace/bank/INDEX.md — use bank if present.
Packet: /workspace/recap/YYYY-MM-DD-<show-slug>.md
Content: takeaways/arguments/claims, timestamped (--:-- unless chapters), 3-6 quotes max 25 words.
After transcript: python3 /workspace/bank/scripts/bank.py --root /workspace/bank --text --lane LANE --kind podcast --via grok-bot/Recap --source URL --title TITLE --author AUTHOR --published DATE < body.txt
Lanes: ideas=All-In/Elon/Fern/Moon/Frontpage; money=Maxinomics; learning=Justin Sung.
Update recap-seen.json.

## LIST file
Write /workspace/recap/2026-09-20-list.md like yesterday's. Rebuild latest.md from packets last 7 days.

## Return
1. Per-pin one-liner (nothing-new OR title/URL/duration/published)
2. Paths of new INGEST packets + LIST path
3. QUIET true/false
4. Full chat-ready LIST (+ INGEST summaries) for WakeParent to Wedge
5. Deferred / failures
