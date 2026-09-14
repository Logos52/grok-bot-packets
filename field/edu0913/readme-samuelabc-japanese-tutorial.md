# 日本語の冒険 — Japanese Adventure

A Japanese learning site for Mandarin speakers — from fundamentals to travel phrases.

Built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build).

**Live site:** [https://japanese-tutorial.pages.dev](https://japanese-tutorial.pages.dev)

## Prerequisites

- **Node.js 22** — use [nvm](https://github.com/nvm-sh/nvm) to manage versions:

  ```sh
  nvm install 22
  nvm use 22
  ```

- **npm** (comes with Node)

## Local Development

```sh
# Install dependencies
npm install

# Start the dev server at localhost:4321
npm run dev
```

## Project Structure

```
src/
├── components/       # React & Astro components (KnowledgeCheck, ProgressTracker, etc.)
├── content/
│   └── docs/         # Lesson content in .mdx files
│       ├── 01-introduction/
│       ├── 02-hiragana/
│       ├── 03-katakana/
│       ├── 04-kanji/
│       ├── 05-grammar/
│       └── 06-travel/
├── styles/
│   └── custom.css    # Custom styles (kana-table, comparison-table, etc.)
└── content.config.ts
astro.config.mjs      # Starlight config & sidebar order
```

## Commands

| Command           | Action                                       |
| :---------------- | :------------------------------------------- |
| `npm install`     | Install dependencies                         |
| `npm run dev`     | Start dev server at `localhost:4321`         |
| `npm run build`   | Build production site to `./dist/`           |
| `npm run preview` | Preview the build locally before deploying   |

## Deploy

The site is deployed to **Cloudflare Pages** as a static site.

### Quick Deploy (Manual)

```sh
# 1. Build the site
npm run build

# 2. Deploy to Cloudflare Pages
npx wrangler pages deploy dist --project-name japanese-tutorial
```

On first run, `wrangler` will open a browser for Cloudflare authentication. After that, credentials are cached locally.

### Setting Up Cloudflare Pages from Scratch

If you're setting up the project on a new Cloudflare account:

1. **Install Wrangler** (Cloudflare CLI):

   ```sh
   npm install -g wrangler
   ```

2. **Authenticate** with your Cloudflare account:

   ```sh
   wrangler login
   ```

3. **Create the Pages project** (first deploy creates it automatically):

   ```sh
   npm run build
   wrangler pages deploy dist --project-name japanese-tutorial
   ```

4. Your site will be live at `https://japanese-tutorial.pages.dev`.

### Custom Domain (Optional)

To use a custom domain:

1. Go to the [Cloudflare Dashboard](https://dash.cloudflare.com) → **Workers & Pages** → **japanese-tutorial** → **Custom domains**
2. Click **Set up a custom domain** and follow the prompts
3. If your domain is already on Cloudflare, DNS records are configured automatically

### Git-Connected Deploys (Optional)

To auto-deploy on every push to `main`:

1. Go to the [Cloudflare Dashboard](https://dash.cloudflare.com) → **Workers & Pages** → **japanese-tutorial** → **Settings** → **Builds & deployments**
2. Connect the GitHub repo: [`samuelabc/japanese-tutorial`](https://github.com/samuelabc/japanese-tutorial)
3. Set these build settings:
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
   - **Node.js version:** Add environment variable `NODE_VERSION` = `22`
4. Every push to `main` will now trigger a deploy. Pull requests get preview URLs automatically.

### Environment Variables Reference

| Variable       | Where                | Value | Purpose                     |
| :------------- | :------------------- | :---- | :-------------------------- |
| `NODE_VERSION` | Cloudflare dashboard | `22`  | Ensures correct Node version during CI builds |

### Troubleshooting

- **Build fails on Cloudflare?** — Make sure `NODE_VERSION` is set to `22` in the Cloudflare Pages environment variables.
- **`wrangler` not found?** — Install globally with `npm install -g wrangler`, or use `npx wrangler` instead.
- **Authentication expired?** — Run `wrangler login` again to re-authenticate.

## Contributing

1. Lesson content lives in `src/content/docs/**/*.mdx`
2. Sidebar order is configured in `astro.config.mjs`
3. Use Starlight aside syntax for callout types: `:::note[Memory Trick]`, `:::tip[Mandarin Bridge]`, `:::caution[False Friend]`, `:::note[Deep Dive]`, `:::tip[Culture]`
4. Furigana uses inline `<ruby>` tags
5. Tables use CSS classes like `kana-table` and `comparison-table` from `src/styles/custom.css`

## License

This project is open source. See the [GitHub repo](https://github.com/samuelabc/japanese-tutorial) for details.
