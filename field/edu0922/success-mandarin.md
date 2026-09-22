# Success with Mandarin

Static website for Success with Mandarin, part of Kemix Academy. Run `node server.cjs`, then visit http://127.0.0.1:4178.
Public website: https://leonardywu.github.io/success-with-mandarin/

GitHub Pages publishes the `dist` directory automatically when changes are pushed to `main`. The repository is public. Local preview remains available through `node server.cjs`.

## Editing
- `dist/app.js`: per-person package prices, teaching hours, schedule options, WhatsApp number, vocabulary quiz.
- `dist/index.html`: page content, schedule, FAQ, social links.
- `dist/styles.css`: visual styles and responsive layout.
- `dist/assets`: supplied brand logos.

## Items to confirm before launch
- HSK prices updated from the owner's table on September 21, 2026. The unlabeled upper table is interpreted as Private 1-on-1; the lower table is Private Group for 2–4 people. All prices are per person.
- HSK 1: 36 hours, private 3,450,000 / group 1,925,000 IDR. HSK 2: 36 hours, private 4,025,000 / group 2,212,500. HSK 3: 48 hours, private 6,131,800 / group 3,265,900.
- HSK 4A and 4B: 24 hours each, private 3,450,000 / group 1,925,000 per part. HSK 5A and 5B: 48 hours each, private 7,665,900 / group 4,032,950 per part.
- Two weekly sessions of 1.5 hours or three weekly sessions of 1 hour; both total 3 hours/week. Estimated weeks exclude holidays/rescheduling. No unconfirmed bundle discounts are applied.
- TOCFL price and hours, platform, timezone, exact schedules, and package validity remain to be confirmed.
- Tutor profile and verified qualifications; no fabricated credentials or testimonials are displayed.
- Certificate issuer/requirements, payment, rescheduling and cancellation rules.
- Quiz is casual beginner vocabulary practice, not a formal HSK level assessment. Tutor review recommended before launch.

Website opens a prefilled WhatsApp draft; it does not send a message automatically. Quiz data stays in page memory and resets on reload. No signup or analytics tracking is included. Google Fonts requires internet; local font fallbacks are provided.

## Quiz levels
- Beginner: 10 everyday vocabulary questions, with pinyin.
- Advanced / HSK 5: 4 vocabulary-in-context questions and 6 sentence-completion questions; original items using classic HSK 5 vocabulary, with Indonesian explanations.
- Level selection before starting; retry the same level or select another after finishing. Scores and WhatsApp drafts include the selected level.
- Reference for curriculum review: Chinese Testing International's resource center, https://admin.chinesetest.cn/godownload.do (HSK 5 syllabus and 2015 vocabulary list). The quiz is an informal vocabulary exercise, not an official examination or a claim of full syllabus coverage.
- Verified both 10-question flows, mixed and perfect scores, retry, level-switch reset, WhatsApp level/score text, and mobile sentence wrapping.
