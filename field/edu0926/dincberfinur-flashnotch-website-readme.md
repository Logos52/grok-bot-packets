# FlashNotch website

The landing page (`index.html`) and privacy policy (`privacy.html`) for FlashNotch, served by
GitHub Pages at https://dincberfinur.github.io/flashnotch-website/. Plain static files: no build step.

## Preview locally

```bash
python3 -m http.server 8123
# then open http://127.0.0.1:8123/
```

## Publish

Commit and push `main`. GitHub Pages redeploys within a minute or two.

Publish before you submit the app for review: the App Store listing's marketing, support and
privacy links point here, and the app's About tab links to `#support`.

## The launch switch

At the top of the script in `index.html`:

```js
const LAUNCH = {
  live: false,   // false: "Coming soon" + "Email me at launch"; true: Mac App Store badge
  appStoreUrl: "https://apps.apple.com/app/flashnotch/id6778994529",
  price: "$4.99",
  contactEmail: "support@minutebank.app"
};
```

Set `live: true` the day FlashNotch is on sale, then push. The contact address also appears in
the Support section, the footer and `privacy.html`; change all four together.

## Images

`images/*.webp` are exported from the app's screenshot studio (real captures of the app, fed by
a demo collection):

```bash
cd ../flashNotch/fastlane/screenshot-studio
node render.mjs --web ../../../flashnotch-website/images
```

`og-image.png` (1200×630) is the link-preview image; `favicon.png` and `apple-touch-icon.png`
come from the app icon.
