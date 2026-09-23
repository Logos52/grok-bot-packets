import { chromium } from 'playwright-core';
import fs from 'fs';
const VIDEO = process.argv[2];
const OUTDIR = process.argv[3];
const browser = await chromium.connectOverCDP('http://127.0.0.1:9234');
const context = browser.contexts()[0];
const page = await context.newPage();
await page.goto(`https://www.youtube.com/watch?v=${VIDEO}`, { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(5000);
for (const sel of ['button[aria-label="Show transcript"]','button:has-text("Show transcript")']) {
  try {
    const el = page.locator(sel).first();
    if (await el.isVisible({ timeout: 3000 })) { await el.click(); console.log('clicked', sel); break; }
  } catch {}
}
// expand description then show transcript
try {
  const exp = page.locator('#expand, tp-yt-paper-button#expand').first();
  if (await exp.isVisible({ timeout: 2000 })) await exp.click();
} catch {}
await page.waitForTimeout(2000);
for (const sel of ['button[aria-label="Show transcript"]','button:has-text("Show transcript")']) {
  try {
    const el = page.locator(sel).first();
    if (await el.isVisible({ timeout: 2000 })) { await el.click(); console.log('clicked2', sel); break; }
  } catch {}
}
await page.waitForTimeout(6000);
// scroll new panel
for (let i=0;i<50;i++){
  await page.evaluate(() => {
    const els = document.querySelectorAll('transcript-segment-view-model, ytd-transcript-segment-renderer');
    const last = els[els.length-1];
    if (last) last.scrollIntoView();
  });
  await page.waitForTimeout(150);
}
const html = await page.content();
fs.writeFileSync(`${OUTDIR}/page.html`, html);
await page.screenshot({ path: `${OUTDIR}/debug.png` });
console.log('title', await page.title());
console.log('seg count', (html.match(/transcript-segment-view-model/g)||[]).length);
process.exit(0);
