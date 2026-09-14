---
id: 2026-09-14-alessio-palumbo-japartner-local-first-ja-tutor-goal
kind: article
title: Japartner — local-first JA tutor; goal-deadline roadmaps; gap-capture human-gate
source: "https://github.com/alessio-palumbo/japartner"
author: alessio-palumbo
published: 2026-09-13
captured: 2026-09-14
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# Japartner (alessio-palumbo/japartner)

Source: https://github.com/alessio-palumbo/japartner
Author: alessio-palumbo
Published: created 2026-09-13; same-day roadmap/mission/practice commits through ~20:01Z (public repo stamp ~23:46Z).

## Field summary (portable gates)
- **tutor-loop**: local-first Japanese tutor (Go/Wails + Ollama + whisper.cpp + VOICEVOX) plans daily practice around a goal and deadline; mission briefs with partner role, warm-up, phrase kit, success criteria.
- **human-gate**: Capture after real-world gaps — generate editable expression drafts; approve only useful ones; PDF/CSV import requires review before queue.
- **teach-once / quiet-when-nothing**: Today never needs an LLM request to open; Ollama prepares brief once on Start with local fallback; selection does not contact Ollama.
- **generated-input**: bounded daily lesson (due reviews, new/weak expressions, conversation targets, captured gaps); roadmap lessons evenly spaced; learner-confirmed mission success (not automated proficiency).
- Distinct from nihongo-tutor (Telegram FSRS+Sudachi i+1): this is desktop spoken practice with gap-capture → approve and goal-deadline roadmaps.

## README (excerpt)
# Japartner

Japartner is a local-first personal Japanese tutor built with Go, Wails, React, Ollama, whisper.cpp, VOICEVOX, and SQLite. It plans daily practice around a goal and deadline, tracks reusable expressions, turns real-world speaking gaps into study material, and runs targeted spoken conversations.

## Run

```sh
wails dev
```

Build a production app:

```sh
wails build
```

The built app is written to `build/bin/japartner.app`.

Run backend regressions with `go test ./...`, frontend transcript tests with `npm --prefix frontend test`, and the production frontend check with `npm --prefix frontend run build`.

## Releases

Push a version tag such as `v0.1.0` to build macOS, Windows, and Linux archives and publish a GitHub release. The macOS job signs, notarizes, and staples the app before publishing it.

Configure these GitHub Actions repository secrets for macOS releases:

- `MACOS_CERTIFICATE_BASE64`: exported Developer ID Application certificate (`.p12`) encoded as base64
- `MACOS_CERTIFICATE_PASSWORD`: password used when exporting the certificate
- `APPLE_ID`: Apple ID used for notarization
- `APPLE_TEAM_ID`: Apple developer team ID
- `APPLE_APP_SPECIFIC_PASSWORD`: app-specific password for notarization

The signing script can also be run locally with those notarization variables and an optional `MACOS_SIGNING_IDENTITY`.

## Using the App

- Set the active goal, exact deadline, focus areas, and practice frequency on **Today** (default: three days per week). Save to generate a short Ollama summary and weekly themes with scheduled lessons; a local roadmap is used if Ollama is unavailable or returns invalid content.
- Today assembles a bounded local lesson: up to 6 due reviews, 3 new expressions, 2 weak expressions, 3 conversation targets, and 2 captured gaps. A started roadmap lesson keeps its non-empty exercise list until completed, including across dates and restarts. Without a roadmap, a non-empty plan stays fixed for the local date.
- Only the current scheduled roadmap lesson can start. Start selects its local exercises and prepares a saved 5–10 minute activity brief: a concrete mission, partner role, warm-up, steps, 4–6 useful phrases, two examples to adapt, and success criteria. Ollama prepares the brief once on Start, with a local fallback; Today never needs an LLM request to open. Resume and Repeat preserve the brief across dates and restarts.
- Finish the reviews and conversation, then confirm whether you achieved the mission outcomes (with help if needed). Completing the lesson records pointers and activates the next scheduled lesson. Mission success is learner-confirmed, not an automated proficiency assessment. Completed lessons can be repeated without losing their original completion. Goal/cadence changes require finishing an in-progress lesson and preserve completed lessons.
- Review, new-learning, and weak-practice cards complete with Hard, Good, or Easy. Again means failed recall: the card remains unfinished and moves behind other cards for an in-lesson retry (its spaced-review retry is also scheduled in ten minutes). Use Reveal, the speaker button, Previous/Next, arrow keys, or touch swipes. Completed sections can be dismissed. Overall review, conversation, and vocabulary progress appears at the bottom of Today.
- Review due expressions by recalling the Japanese first, revealing the answer, then choosing Again, Hard, Good, or Easy.
- Use **Practice** for the guided activity. The tutor opens with an in-character question, follows the mission, and introduces a small complication. Try optional review expressions where they fit naturally; unrelated ones need not be used. The topic phrase kit is separate from review targets and does not silently add generated vocabulary to the library. Listen to phrases/examples using their audio buttons.
- Open **Mission & phrase kit** during Practice for support. **Help me** simplifies the task and offers an example; **Make it harder** introduces a small constraint or asks for a reason. Support actions stay in the same activity and are not recorded as learner replies. Local fallback activities rotate between opinion exchanges, role-plays, storytelling, and problem-solving. Existing started roadmaps receive a local brief safely when loaded.
- Choose **Need a hint?** only when you want to reveal a possible reply.
- End a conversation to record which target expressions you produced. Active conversation turns survive across app restarts.
- Use **Expressions** to add expressions manually, auto-fill their kana reading and meaning, and inspect their current learning status.
- Use **Capture** after a teacher lesson, meetup, or real-world conversation. Describe what you could not say, generate editable expression drafts, and approve only the useful ones.
- In **Capture**, choose a teacher PDF or vocabulary CSV. PDFs are read with built-in OCR when needed; CSV rows are imported directly. Review or remove every suggestion before adding it to the practice queue. Source files remain in their original location and are not copied into Japartner's data.
- Click `Explain` on an assistant reply to open a modal with a kana reading, translation, vocabulary, and grammar details. Useful words can be saved explicitly for later review.
- Use `How to say` mode when you want a natural Japanese phrase for an English idea.
- Use `Correction` mode when you want your Japanese sentence corrected.
- Press `Cmd+Enter` or `Ctrl+Enter` to send. Plain `Enter` stays available for Japanese IME selection and line breaks.
- Service readiness is shown as compact dots in the header. Click them for details and refresh controls.
- Model and speech configuration are kept in the collapsible **Settings** drawer.

Goals, expressions, gaps, sessions, attempts, and conversation turns are stored locally in `learning.sqlite` in the application's user configuration directory.

Daily plans store only selected IDs and completion alongside that existing learning state. Selection does not contact Ollama. New learning prioritizes captured/imported material, weakness uses the last three review ratings and latest evaluation among the last 20 completed conversations, and conversation/gap relevance uses simple matching against the active goal and focus areas. Missing lexical matches fall back to useful study items; this is not semantic topic classification. Without an active goal, review and learning still work, but targeted conversations are not planned.

Roadmaps add one metadata table referencing the existing goal and daily-plan snapshots. Practice dates are evenly spaced in seven-day blocks from the save date, not specific weekdays. Target dates are bounded to the next year. Weekly themes cycle for longer goals; the full curriculum is not generated upfront. Lesson pointers reuse local completion and the existing conversation evaluation, rather than requiring another model request. Skipped dates leave the current lesson available; subsequent lessons still follow their sc
