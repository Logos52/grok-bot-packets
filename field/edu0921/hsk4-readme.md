# HSK Flashcards (HSK1‑HSK4)
A lightweight offline web‑based flashcard application for learning Chinese HSK 1‑4 vocabulary.
All 1200 words covering HSK1, HSK2, HSK3 and HSK4 are built‑in. No server required, works fully in‑browser.

> Developed by [DecentCoders](https://github.com/DecentCoders)

## ✨ Features
- 1200 vocabulary entries: Chinese characters, Pinyin, English meaning
- Shuffle / randomize word order for practice
- Click‑to‑flip flashcard design
- Keyboard shortcuts:
  - `Space` — flip current card
  - `←` / `→` — navigate previous / next word
- Full word‑list view to browse all vocabulary
- Chinese characters rendered with **Noto Serif SC** (font style close to official HSK exam papers)
- Mobile‑friendly responsive layout, works on phones, tablets and desktop
- 100% static HTML, run locally or deploy to any static hosting service

## 📦 Word Source
- HSK‑4 vocabulary from MandarinBean original list (600 words)
- Supplemented with HSK1 + HSK2 + HSK3 vocabulary (additional 600 words)
> Note: This is for personal study purposes. Please respect the original vocabulary content copyright.

## 🚀 Quick Start
### Run locally
1. Clone repository
```bash
git clone https://github.com/DecentCoders/Hsk4.git
cd Hsk4
2. Open `index.html` directly with any modern web browser (Chrome, Firefox, Edge).

> 
> No npm install / backend needed. Fully client‑side.

### Deploy online

You can deploy this static site on:

- Cloudflare Pages
- Vercel
- Netlify

> 
> ⚠️ Notice: GitHub Pages Terms of Service discourages putting advertisement‑funded commercial sites on github.io.
> If you plan to add advertisements for monetization, please use custom domain with other static hosting providers.

## 📝 Customization

1. **Add / modify words**
Edit the `WORDS` JavaScript array inside `index.html`.
Each word entry format:

```
{ no: 1, zh: "爱情", pinyin: "àiqíng", en: "Love" }
```

2. **Adjust fonts & styling**
CSS is embedded in the HTML file. Main Chinese characters use `Noto Serif SC` (simulates HSK exam paper serif font).
Pinyin and English definitions use `Noto Sans SC` for readability.
3. **Monetization note**
Technically you can insert ad network HTML snippets into this page.
Important prerequisites if you want to place ads:

- Use custom domain & non‑GitHub‑Pages hosting
- Add a privacy policy page for ad‑tracking compliance
- Ensure you hold proper usage rights for vocabulary datasets for commercial usage
- Place ads only at top / footer; hide ads on mobile devices, avoid overlapping flashcard interactive elements.

Alternative low‑risk option: add GitHub Sponsors / Buy‑me‑a‑coffee donation button.

## ⌨️ Keyboard Shortcuts

表格

| Key | Action |
| --- | --- |
| Space | Flip flashcard |
| Arrow Left | Previous card |
| Arrow Right | Next card |

## 📄 License

> 
> Fill your actual license, for example MIT:

```
MIT License

Copyright (c) 2026 DecentCoders

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🤝 Contributing

Contributions are welcome:

- Fix typos in vocabulary words / pinyin / translations
- Improve CSS styling & mobile responsiveness
- Add new features

1. Fork this repo
2. Create your feature branch
3. Commit your changes
4. Open Pull Request

## 📫 Issues

Found wrong vocabulary entry, pinyin mistake or UI bug? Open a GitHub Issue.
