import { chromium } from 'playwright-core';
import fs from 'fs';

const VIDEO = process.argv[2] || 'VF90rBzl26E';
const OUTDIR = process.argv[3] || '/workspace/recap/tmp-0923-hilton';
const CDP = process.env.CDP || 'http://127.0.0.1:9234';

const browser = await chromium.connectOverCDP(CDP);
const context = browser.contexts()[0] || await browser.newContext();
const page = context.pages().find(p => p.url().includes('youtube.com/watch')) || await context.newPage();

const url = `https://www.youtube.com/watch?v=${VIDEO}`;
console.log('goto', url);
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);

// Dismiss consent / overlays if present
for (const sel of [
  'button[aria-label*="Accept"]',
  'button[aria-label*="Reject"]',
  'button:has-text("Accept all")',
  'button:has-text("Reject all")',
  'tp-yt-paper-button#dismiss-button',
]) {
  try {
    const el = page.locator(sel).first();
    if (await el.isVisible({ timeout: 800 })) await el.click({ timeout: 2000 });
  } catch {}
}

// Expand description if needed, then open "...more" / Show transcript
async function openTranscript() {
  // Click "...more" in description
  for (const sel of [
    '#description-inline-expander tp-yt-paper-button#expand',
    '#expand',
    'tp-yt-paper-button#expand',
    'button[aria-label="Show transcript"]',
    'button:has-text("Show transcript")',
  ]) {
    try {
      const el = page.locator(sel).first();
      if (await el.isVisible({ timeout: 1500 })) {
        await el.click({ timeout: 3000 });
        await page.waitForTimeout(1000);
      }
    } catch {}
  }
  // Engagement panel button
  for (const sel of [
    'button[aria-label="Show transcript"]',
    'ytd-video-description-transcript-section-renderer button',
    '#primary-button button',
    'button:has-text("Show transcript")',
  ]) {
    try {
      const el = page.locator(sel).first();
      if (await el.isVisible({ timeout: 2000 })) {
        await el.click({ timeout: 5000 });
        console.log('clicked', sel);
        return true;
      }
    } catch {}
  }
  return false;
}

let opened = await openTranscript();
if (!opened) {
  // Try scrolling description into view / clicking description
  try {
    await page.locator('#description-inline-expander').first().click({ timeout: 3000 });
    await page.waitForTimeout(1000);
    opened = await openTranscript();
  } catch {}
}
console.log('opened', opened);

// Wait for transcript segments
await page.waitForTimeout(3000);
const panelSel = 'ytd-transcript-segment-renderer, ytd-transcript-body-renderer';
try {
  await page.waitForSelector(panelSel, { timeout: 20000 });
} catch (e) {
  console.log('no panel yet', e.message);
  // screenshot for debug
  await page.screenshot({ path: `${OUTDIR}/debug.png`, fullPage: false });
  fs.writeFileSync(`${OUTDIR}/page.html`, await page.content());
  console.log('title', await page.title());
  process.exit(2);
}

// Scroll transcript to load all
const body = page.locator('ytd-transcript-renderer, #segments-container').first();
for (let i = 0; i < 40; i++) {
  await page.evaluate(() => {
    const el = document.querySelector('ytd-transcript-renderer #segments-container') 
      || document.querySelector('ytd-transcript-body-renderer')
      || document.querySelector('ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"]');
    if (el) el.scrollTop = el.scrollHeight;
  });
  await page.waitForTimeout(200);
}

const lines = await page.evaluate(() => {
  const segs = [...document.querySelectorAll('ytd-transcript-segment-renderer')];
  return segs.map(s => {
    const t = s.querySelector('.segment-timestamp, div.segment-timestamp')?.textContent?.trim() || '';
    const text = s.querySelector('.segment-text, yt-formatted-string.segment-text')?.textContent?.trim() || s.innerText.replace(/^\d+:\d+\s*/,'').trim();
    return { t, text };
  }).filter(x => x.text);
});

console.log('lines', lines.length);
fs.writeFileSync(`${OUTDIR}/transcript-lines.json`, JSON.stringify(lines, null, 2));
const plain = lines.map(l => `${l.t}\t${l.text}`).join('\n');
fs.writeFileSync(`${OUTDIR}/transcript.txt`, plain);
fs.writeFileSync(`${OUTDIR}/title.txt`, await page.title());
console.log('sample', lines.slice(0, 5));
console.log('done');
// leave browser open
process.exit(0);
