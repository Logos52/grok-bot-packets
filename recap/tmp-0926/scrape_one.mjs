import { chromium } from 'playwright-core';
import fs from 'fs';

const VIDEO = process.argv[2];
const OUTDIR = process.argv[3];
if (!VIDEO || !OUTDIR) { console.error('usage: scrape_one.mjs VIDEO_ID OUTDIR'); process.exit(1); }
fs.mkdirSync(OUTDIR, { recursive: true });

const browser = await chromium.connectOverCDP('http://127.0.0.1:9234');
const context = browser.contexts()[0];
let page = context.pages().find(p => p.url().includes(VIDEO));
if (!page) page = await context.newPage();
if (!page.url().includes(VIDEO)) {
  console.log('goto', VIDEO);
  await page.goto(`https://www.youtube.com/watch?v=${VIDEO}`, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(4000);
} else {
  console.log('reuse tab', VIDEO);
}

for (const sel of [
  'button[aria-label*="Accept"]','button:has-text("Accept all")','button:has-text("Reject all")',
  'tp-yt-paper-button#dismiss-button',
]) {
  try { const el = page.locator(sel).first(); if (await el.isVisible({timeout:800})) await el.click({timeout:2000}); } catch {}
}

for (const sel of ['#description-inline-expander tp-yt-paper-button#expand','#expand','tp-yt-paper-button#expand']) {
  try { const el = page.locator(sel).first(); if (await el.isVisible({timeout:1200})) { await el.click(); await page.waitForTimeout(800);} } catch {}
}

let opened = false;
for (const sel of ['button[aria-label="Show transcript"]','button:has-text("Show transcript")','ytd-video-description-transcript-section-renderer button']) {
  try {
    const el = page.locator(sel).first();
    if (await el.isVisible({timeout:2000})) { await el.click({timeout:5000}); opened=true; console.log('clicked', sel); break; }
  } catch {}
}
console.log('opened', opened);
await page.waitForTimeout(2500);

try {
  await page.waitForSelector('transcript-segment-view-model', { timeout: 25000 });
} catch (e) {
  console.log('no segments', e.message);
  await page.screenshot({ path: `${OUTDIR}/debug.png` });
  fs.writeFileSync(`${OUTDIR}/page.html`, await page.content());
  process.exit(2);
}

let prev = 0;
for (let i = 0; i < 80; i++) {
  await page.evaluate(() => {
    const els = document.querySelectorAll('transcript-segment-view-model');
    const last = els[els.length - 1];
    if (last) last.scrollIntoView({ block: 'end' });
    const panel = document.querySelector('ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"]');
    if (panel) {
      for (const el of panel.querySelectorAll('*')) {
        if (el.scrollHeight > el.clientHeight + 50) el.scrollTop = el.scrollHeight;
      }
    }
  });
  await page.waitForTimeout(100);
  const n = await page.evaluate(() => document.querySelectorAll('transcript-segment-view-model').length);
  if (i > 10 && n === prev) break;
  prev = n;
}

const lines = await page.evaluate(() => [...document.querySelectorAll('transcript-segment-view-model')].map(s => ({
  t: s.querySelector('.ytwTranscriptSegmentViewModelTimestamp')?.textContent?.trim() || '',
  text: s.querySelector('.ytAttributedStringHost')?.textContent?.trim() || '',
})).filter(x => x.text));

fs.writeFileSync(`${OUTDIR}/transcript-lines.json`, JSON.stringify(lines, null, 2));
fs.writeFileSync(`${OUTDIR}/transcript.txt`, lines.map(l => `${l.t}\t${l.text}`).join('\n'));
fs.writeFileSync(`${OUTDIR}/transcript-plain.txt`, lines.map(l => l.text).join(' '));
const title = await page.title();
fs.writeFileSync(`${OUTDIR}/title.txt`, title);
const meta = await page.evaluate(() => ({
  desc: (document.querySelector('meta[name="description"]')?.content || '').slice(0, 800),
  date: document.querySelector('meta[itemprop="datePublished"]')?.content
    || document.querySelector('meta[itemprop="uploadDate"]')?.content || '',
  dur: document.querySelector('meta[itemprop="duration"]')?.content || '',
  channel: document.querySelector('link[itemprop="name"]')?.getAttribute('content')
    || document.querySelector('#channel-name a')?.textContent?.trim() || '',
}));
fs.writeFileSync(`${OUTDIR}/meta.json`, JSON.stringify(meta, null, 2));
const words = lines.map(l => l.text).join(' ').split(/\s+/).length;
console.log('OK', VIDEO, 'lines', lines.length, 'words', words, 'range', lines[0]?.t, '->', lines[lines.length-1]?.t);
console.log('title', title);
process.exit(0);
