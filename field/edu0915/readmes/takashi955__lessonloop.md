# LessonLoop — native iOS prototype

SwiftUI app for turning language-course material into daily practice. iOS 17+, iPhone and iPad. No third-party dependencies, API keys or backend required.

## Open and run

1. Open `LessonLoop.xcodeproj` in Xcode.
2. Choose the `LessonLoop` scheme and an iPhone simulator.
3. Run. The app opens with two Japanese sample lessons and French meanings.

To run on a physical iPhone, choose your signing team in the target’s Signing & Capabilities settings and select your device. The example bundle identifier can be changed when connecting your own repository and signing setup.

## Try this

- Practice → Start practice → recall → reveal → rate.
- To clarify → すみません → add meaning/context → confirm.
- My items → edit an item → change its personal note → check that other items stay unchanged. Undo is available per item.
- Add material → Photo library / Camera → real on-device OCR → choose targets → add meanings → confirm → save.
- Paste `expression | reading | meaning` for structured text import. Unpaired lines never become guessed translations.
- Say it aloud → reveal → listen → record → play back. Recording is temporary and discarded when moving on.
- Prepare for an exam → set date and covered lessons → practise without changing daily review dates.

## What is real

Native navigation, local JSON persistence, saved source photos, Apple Vision OCR, item-level revisions, duplicate protection within lessons, due-date scheduling, exam scoping, speech synthesis, microphone recording and playback.

## What is deliberately not connected

AI document interpretation, translation, automatic scope detection, calendar/exam parsing, handwriting grading, pronunciation scoring, cloud sync and production spaced-repetition scheduling. These need a separate implementation. The scheduler uses 10 minutes / 1 day / 3 days and one in-session retry, not FSRS.

The initial examples are prepared from the conversation and include illustrative translations; they are not live extraction results. The separate HEIC homework image was not interpreted. No personal source photos are bundled in the project.

OCR is text recognition only. It does not distinguish teacher answers from student handwriting, or instructions from learning targets. Photo candidates start unselected. Missing meanings and unconfirmed items stay out of practice. Source text is preserved separately from corrections. Photos are downsampled to at most 2600 pixels before recognition and storage. Unsupported OCR languages produce a visible warning; audio depends on available system voices.

Course files are stored in the app’s Documents/ LessonLoop directory. No account, analytics or external AI requests are included. Source photos remain on device and recordings are temporary. Standard device backups may include Documents data. Deleting the app deletes its local data unless restored from backup.

## Architecture

- Models.swift: stable IDs, learning items, source material, revisions, parser.
- CourseStore.swift: atomic local storage, safe updates, imports and scheduling.
- PracticeViews.swift: practice sessions and exam mode.
- LibraryViews.swift: lessons, item editing, provenance and settings.
- ImportView.swift / PhotoTextReader.swift: photo capture, OCR and reviewed import.
- PracticeAudio.swift: native playback and temporary recording.

## Verification

The XCTest target covers unpaired text, confirmation requirements, edit isolation, persistence, exam scheduling and duplicate-safe imports. Run Product → Test in Xcode.

Verified on 13 September 2026 with Xcode 26.6: simulator build succeeded; all five tests passed on iPhone 16 Pro / iOS 18.6. The native home screen, reveal-answer action, recall rating and advancement to the next item were checked in the running simulator. Physical-device camera/microphone and OCR on your actual handouts have not yet been runtime-validated.

Apple references: [Vision text recognition](https://developer.apple.com/documentation/vision/vnrecognizetextrequest), [PhotosPickerItem](https://developer.apple.com/documentation/photosui/photospickeritem).
