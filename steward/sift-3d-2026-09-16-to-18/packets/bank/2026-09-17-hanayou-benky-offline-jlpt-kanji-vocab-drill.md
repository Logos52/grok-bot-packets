---
id: 2026-09-17-hanayou-benky-offline-jlpt-kanji-vocab-drill
kind: article
title: Benkyō — offline JLPT kanji/vocab drill PWA with working-set rotation
source: "https://github.com/Hanayou/benkyou"
author: Hanayou
published: 2026-09-16
captured: 2026-09-17
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# Benkyō — offline JLPT kanji/vocab drill PWA with working-set rotation

Source: https://github.com/Hanayou/benkyou
Author: Hanayou
Created: 2026-09-16
Pushed (window): 2026-09-16T08:06:30Z
Lane: learning / Field education hunt 2026-09-17
Via: grok-bot/Field

## Hunt blurb
Named offline JLPT N5–N1 kanji+vocab drill PWA. Six-direction quizzes, working set ~20 unfinished groups, locked per-list target rules, KanjiVG stroke drawer, IndexedDB progress + clipboard backup. Day-0 created 2026-09-16.

## README
# 勉強 Benkyō

A simple, fast JLPT kanji & vocabulary drill app — an installable offline PWA.
No accounts, no server: all progress lives on your device.

## What it does

- **10 lists**: N5→N1 Kanji and N5→N1 Vocabulary.
- **Classic drill loop**: each item ("group") is quizzed in 6 directions —
  kanji↔yomi, kanji↔English, yomi↔English — as 4-choice questions. Each correct
  answer scores a point for that direction; there is no penalty for mistakes.
  A direction maxes out after N correct answers (default 5, configurable).
- **Working set**: only the first ~20 unfinished groups rotate at once, so new
  material repeats frequently. Maxed-out groups retire and the next group is
  pulled in. When every group is maxed, the list is complete.
- **Locked rules per list**: the answers-per-direction setting is frozen into a
  list the moment you start it; only resetting that list picks up a new value.
- **Info drawer**: swipe up from the bottom of the quiz for stroke-order
  animations (KanjiVG), readings, meanings, example sentences, and related
  vocabulary for whatever you just answered. Stays out of the way otherwise.
- **Search tab**: search every list by kanji, kana, romaji, or English.
- **Settings**: auto-advance delay, rotation size, per-direction target,
  per-list reset, and clipboard backup/restore of all progress.

## Development

```bash
npm install
npm run data:fetch   # download source dictionaries into .data-cache/
npm run data:build   # build public/data/ (lists, stroke shards, examples)
npm run icons        # regenerate icons from KanjiVG strokes
npm run dev          # dev server
npm test             # quiz-engine unit tests
npm run build        # production build (dist/)
```

`public/data/` is committed, so clones can build without re-fetching sources.

## Deploying

Pushes to `main` deploy to GitHub Pages via `.github/workflows/deploy.yml`
(build with `BASE_PATH=/<repo-name>/`). Any static host works — set `BASE_PATH`
to the URL prefix the app is served under.

## Installing on iPhone

Open the deployed URL in Safari → Share → **Add to Home Screen**. The app
precaches everything (~6 MB) and works fully offline. Progress is stored in
IndexedDB; use Settings → Backup to copy it elsewhere.

## Data sources & licenses

App code is MIT. The bundled study data is built from:

| Source | Used for | License |
| --- | --- | --- |
| [KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) (via [kanji-data](https://github.com/davidluzgouveia/kanji-data)) | kanji readings/meanings, JLPT levels | CC BY-SA 4.0 (EDRDG) |
| [Jonathan Waller's JLPT lists](https://www.tanos.co.uk/jlpt/) (via [open-anki-jlpt-decks](https://github.com/jamsinclair/open-anki-jlpt-decks)) | vocabulary lists | CC BY |
| [KanjiVG](https://kanjivg.tagaini.net/) | stroke-order diagrams | CC BY-SA 3.0 |
| [Tanaka Corpus](https://www.edrdg.org/wiki/index.php/Tanaka_Corpus) | example sentences | CC BY |

JLPT level assignments are unofficial community estimates — the JLPT has not
published official lists since 2010.

## Recent commits.atom (truncated)
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" xml:lang="en-US">
  <id>tag:github.com,2008:/Hanayou/benkyou/commits/main</id>
  <link type="text/html" rel="alternate" href="https://github.com/Hanayou/benkyou/commits/main"/>
  <link type="application/atom+xml" rel="self" href="https://github.com/Hanayou/benkyou/commits/main.atom"/>
  <title>Recent Commits to benkyou:main</title>
  <updated>2026-09-16T08:06:29Z</updated>
  <entry>
    <id>tag:github.com,2008:Grit::Commit/3419342fdf47bd0659734dfe1bd5bcd7bf7904a9</id>
    <link type="text/html" rel="alternate" href="https://github.com/Hanayou/benkyou/commit/3419342fdf47bd0659734dfe1bd5bcd7bf7904a9"/>
    <title>
        Move quiz to top, make info drawer non-blocking
    </title>
    <updated>2026-09-16T08:06:29Z</updated>
    <media:thumbnail height="30" width="30" url="https://avatars.githubusercontent.com/u/33036922?s=30&amp;v=4"/>
    <author>
      <name>Hanayou</name>
      <uri>https://github.com/Hanayou</uri>
    </author>
    <content type="html">
      &lt;pre style=&#39;white-space:pre-wrap;width:81ex&#39;&gt;Move quiz to top, make info drawer non-blocking

The prompt and answer grid now sit at the top of the screen; the drawer
occupies the remaining space below as an in-flow panel instead of an
overlay, so it can stay open while answering — content still swaps at
the moment of each answer, and scroll resets to the top for new items.
Also harden setPointerCapture against invalid pointer ids.

Co-Authored-By: Claude Fable 5 &amp;lt;noreply@anthropic.com&amp;gt;&lt;/pre&gt;
    </content>
  </entry>
  <entry>
    <id>tag:github.com,2008:Grit::Commit/5142500941d99ad9a5ed8a837a23009332f7d667</id>
    <link type="text/html" rel="alternate" href="https://github.com/Hanayou/benkyou/commit/5142500941d99ad9a5ed8a837a23009332f7d667"/>
    <title>
        Initial release: 勉強 Benkyō JLPT drill PWA
    </title>
    <updated>2026-09-16T07:49:05Z</updated>
    <media:thumbnail height="30" width="30" url="https://avatars.githubusercontent.com/u/33036922?s=30&amp;v=4"/>
    <author>
      <name>Hanayou</name>
      <uri>https://github.com/Hanayou</uri>
    </author>
    <content type="html">
      &lt;pre style=&#39;white-space:pre-wrap;width:81ex&#39;&gt;Initial release: 勉強 Benkyō JLPT drill PWA

Offline-first JLPT study app (Preact + Vite + Dexie PWA):
- N5–N1 kanji and vocabulary lists with 6-direction 4-choice drills
- Working-set rotation (first 20 unfinished groups), points per direction,
  no wrong-answer penalty; per-list rules locked at start
- Bottom info drawer with KanjiVG stroke-order animation, Tanaka Corpus
  example sentences, and related vocabulary
- Search across all lists (kanji/kana/romaji/English)
- Settings with per-list reset and clipboard backup/restore
- Data pipeline building from KANJIDIC2, Tanos JLPT lists, KanjiVG, and
  the Tanaka Corpus into static JSON (committed under public/data)

Co-Authored-By: Claude Fable 5 &amp;lt;noreply@anthropic.com&amp;gt;&lt;/pre&gt;
    </content>
  </entry>
</feed>
