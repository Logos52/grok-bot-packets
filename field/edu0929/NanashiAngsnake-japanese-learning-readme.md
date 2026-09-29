# 日本語学習 — Japanese grammar SRS (full-stack)

A spaced-repetition web app for learning Japanese grammar: user accounts,
fill-in-the-blank (cloze) reviews with answer checking, progress tracking, and a
Stripe paywall.

> **Note** — this public repository is a **code & architecture showcase**. The
> grammar content dataset is proprietary and is **not** included here.

## Stack

**Next.js 16** (App Router) · **Prisma** + SQLite · **NextAuth** · **Tailwind CSS** · **Stripe**.

## Features

- 🔐 Accounts (sign-up / sign-in, `USER` / `ADMIN` roles) via NextAuth
- 🔁 SRS reviews with **SM-2** scheduling, presented as cloze exercises with input validation
- 💳 Pro subscription (Stripe Checkout + webhooks) — a batch of free points, the rest gated
- 📊 Progress dashboard, user profile, leaderboard, achievement badges
- 🛠️ Admin panel

## Getting started

```bash
npm install
cp .env.example .env        # fill in your own keys
npm run db:push
npm run db:seed
npm run dev
```

See [`DESIGN.md`](DESIGN.md) for the data model and the main design decisions.

---

> **License:** All rights reserved. This code is published as a portfolio, for viewing and evaluation only — reuse or redistribution is not permitted. See [LICENSE](LICENSE).
