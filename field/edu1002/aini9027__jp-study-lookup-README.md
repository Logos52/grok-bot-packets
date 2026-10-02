# JP Study Lookup

A Chrome extension for studying Japanese. Highlight Japanese text on any web page, or in a PDF (even a scanned one), and a popup shows what you need to learn it, not just a translation.

## What the popup shows

- **Words:** reading, meanings, part of speech, JLPT level and a "common" tag. Conjugated forms are traced back to the dictionary form (食べました → 食べる).
- **Kanji:** every kanji in the selection with meanings, on and kun readings, stroke count and JLPT level.
- **Sentences:** an English translation plus a word-by-word breakdown, each word in dictionary form with its reading and meaning.
- **ひらがな button:** converts the selection to hiragana (kanji become their readings, katakana words stay as they are). Works offline.

Press Esc or click elsewhere to close the popup.

## Install

The extension isn't on the Chrome Web Store yet, so it's installed by hand. It takes about a minute.

1. Go to the [Releases page](https://github.com/aini9027/jp-study-lookup/releases) and download the latest `jp-study-lookup-vX.Y.Z.zip` (under "Assets").
2. Unzip it into a folder you'll keep, for example `Documents\jp-study-lookup`. Chrome loads the extension from this folder, so don't delete it afterwards.
3. Open `chrome://extensions` in Chrome.
4. Turn on **Developer mode** (top right).
5. Click **Load unpacked** and pick the unzipped folder (the one that contains `manifest.json`).
6. Reload any open tabs, then highlight some Japanese.

Chrome may show a reminder about developer-mode extensions when it starts. That's normal for extensions installed this way.

The first lookup after starting Chrome takes a few seconds while the Japanese dictionary loads. After that it's fast.

### Updating

Download the new zip from Releases, replace the contents of your folder with it, then press the reload icon on the extension's card in `chrome://extensions`.

## PDFs

Chrome's built-in PDF viewer blocks extensions, so PDFs open in the extension's own viewer (based on Mozilla's PDF.js) instead, where highlighting works as usual.

- **Online PDFs** open in it automatically.
- **Any other PDF:** click the extension's toolbar button (check the puzzle-piece menu) while the PDF is open, or right-click a link and pick "Open PDF in JP Study viewer".
- **PDFs on your computer:** click the toolbar button on any page to open an empty viewer, then drag the PDF in or use its Open file button. If you turn on **Allow access to file URLs** for the extension (Details on its card in `chrome://extensions`), PDFs from your computer open in the viewer automatically.

### Scanned PDFs (OCR)

Scanned PDFs are pictures of pages, so there's no text to highlight. When the viewer shows a page like that, an **OCR** button appears in its toolbar:

1. Pick the text direction next to it: 横書き (horizontal) or 縦書き (vertical).
2. Click **OCR**. The current page is read in a few seconds, and other pages are read as you scroll to them.
3. Highlight the text on the scan as usual.

Text recognition (Tesseract) runs on your computer; nothing is uploaded. It works best on clean printed text. Blurry photos, handwriting, tiny text and furigana come out worse, and a misread kanji means the lookup shows the wrong word.

## Privacy

The extension has no account, no analytics and no server of its own. When you highlight Japanese text, that text is sent to:

- [Jisho.org](https://jisho.org) for word entries
- [kanjiapi.dev](https://kanjiapi.dev) for kanji details
- Google Translate for the sentence translation

Nothing else is sent anywhere. The hiragana conversion, PDF viewer and OCR all run locally.

**Why it asks for access to all sites:** the popup has to work on whatever page you're reading, and the PDF viewer has to download PDFs from whatever site they're on.

## Known limitations

- Word lookups and translations need an internet connection.
- Jisho's API and the Google Translate endpoint used here are unofficial and could stop working or rate-limit.
- Rare names and unusual kanji readings can get the wrong reading.
- PDFs behind a login may not load in the viewer.
- The extension doesn't run on `chrome://` pages or the Chrome Web Store.

## Credits

Word data comes from [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) (via Jisho) and kanji data from [KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) (via kanjiapi.dev), property of the [Electronic Dictionary Research and Development Group](https://www.edrdg.org/), used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).

Built with [kuromoji.js](https://github.com/takuyaa/kuromoji.js), [PDF.js](https://github.com/mozilla/pdf.js) and [tesseract.js](https://github.com/naptha/tesseract.js). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for versions and licenses.

## Contributing

Bug reports and ideas are welcome in [Issues](https://github.com/aini9027/jp-study-lookup/issues). If something looks up wrong, include the exact text you highlighted.

To work on the code, see [docs/DEV_NOTES.md](docs/DEV_NOTES.md). It's plain JavaScript with no build step: load the folder with "Load unpacked" and reload the extension after each change.

## License

MIT, see [LICENSE](LICENSE). Bundled third-party components keep their own licenses, listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
