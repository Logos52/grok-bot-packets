import { chromium } from 'playwright-core';
import fs from 'fs';

const VIDEO = 'JEUboZzZGM4';
const OUTDIR = '/workspace/recap/tmp-0929';
const CDP = process.env.CDP || 'http://127.0.0.1:9229';

const browser = await chromium.connectOverCDP(CDP);
const context = browser.contexts()[0] || await browser.newContext();
let page = context.pages().find(p => p.url().includes(VIDEO));
if (!page) {
  page = await context.newPage();
}
const url = `https://www.youtube.com/watch?v=${VIDEO}`;
console.log('goto', url, 'via', CDP);
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 120000 });
await page.waitForTimeout(5000);
console.log('title', await page.title());
console.log('url', page.url());

// Dismiss consent / overlays
for (const sel of [
  'button[aria-label*="Accept"]',
  'button:has-text("Accept all")',
  'button:has-text("Reject all")',
  'tp-yt-paper-button#dismiss-button',
  'button[aria-label="Close"]',
]) {
  try {
    const el = page.locator(sel).first();
    if (await el.isVisible({ timeout: 800 })) await el.click({ timeout: 2000 });
  } catch {}
}

async function openTranscript() {
  for (const sel of [
    '#description-inline-expander tp-yt-paper-button#expand',
    '#expand',
    'tp-yt-paper-button#expand',
  ]) {
    try {
      const el = page.locator(sel).first();
      if (await el.isVisible({ timeout: 1500 })) {
        await el.click({ timeout: 3000 });
        await page.waitForTimeout(1000);
      }
    } catch {}
  }
  for (const sel of [
    'button[aria-label="Show transcript"]',
    'ytd-video-description-transcript-section-renderer button',
    '#primary-button button',
    'button:has-text("Show transcript")',
    'yt-button-shape button:has-text("Show transcript")',
  ]) {
    try {
      const el = page.locator(sel).first();
      if (await el.isVisible({ timeout: 2500 })) {
        await el.click({ timeout: 5000 });
        console.log('clicked', sel);
        return true;
      }
    } catch {}
  }
  // Try menu ... → Show transcript
  try {
    const more = page.locator('button[aria-label="More actions"], #button-shape button[aria-label="More actions"]').first();
    if (await more.isVisible({ timeout: 2000 })) {
      await more.click();
      await page.waitForTimeout(800);
      const item = page.locator('tp-yt-paper-listbox ytd-menu-service-item-renderer, ytd-menu-service-item-renderer').filter({ hasText: 'transcript' }).first();
      if (await item.isVisible({ timeout: 2000 })) {
        await item.click();
        console.log('clicked menu transcript');
        return true;
      }
    }
  } catch (e) { console.log('menu path', e.message); }
  return false;
}

let opened = await openTranscript();
if (!opened) {
  try {
    await page.locator('#description-inline-expander').first().click({ timeout: 3000 });
    await page.waitForTimeout(1000);
    opened = await openTranscript();
  } catch {}
}
console.log('opened', opened);
await page.waitForTimeout(3000);

const panelSel = 'ytd-transcript-segment-renderer, transcript-segment-view-model, ytd-transcript-body-renderer';
try {
  await page.waitForSelector(panelSel, { timeout: 25000 });
} catch (e) {
  console.log('no panel', e.message);
  await page.screenshot({ path: `${OUTDIR}/debug.png`, fullPage: false });
  fs.writeFileSync(`${OUTDIR}/page.html`, await page.content());
  // dump buttons text
  const btns = await page.evaluate(() => [...document.querySelectorAll('button')].map(b => (b.getAttribute('aria-label')||b.innerText||'').slice(0,80)).filter(Boolean).slice(0,80));
  console.log('buttons sample', btns);
  process.exit(2);
}

for (let i = 0; i < 80; i++) {
  await page.evaluate(() => {
    const segs = document.querySelectorAll('ytd-transcript-segment-renderer, transcript-segment-view-model');
    const last = segs[segs.length - 1];
    if (last) last.scrollIntoView({ block: 'end' });
    const panel = document.querySelector('ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"] #content')
      || document.querySelector('ytd-transcript-renderer #segments-container')
      || document.querySelector('ytd-transcript-body-renderer');
    if (panel) panel.scrollTop = panel.scrollHeight;
  });
  await page.waitForTimeout(150);
}

const lines = await page.evaluate(() => {
  const segs = [...document.querySelectorAll('ytd-transcript-segment-renderer, transcript-segment-view-model')];
  return segs.map(s => {
    const t = s.querySelector('.segment-timestamp, div.segment-timestamp')?.textContent?.trim()
      || s.querySelector('[class*="timestamp"]')?.textContent?.trim()
      || '';
    let text = s.querySelector('.segment-text, yt-formatted-string.segment-text')?.textContent?.trim() || '';
    if (!text) {
      const raw = (s.innerText || '').trim();
      text = raw.replace(/^\d+:\d+\s*/, '').trim();
      // if timestamp not found separately, parse from raw
    }
    let ts = t;
    if (!ts) {
      const m = (s.innerText || '').match(/^(\d+:\d+(?::\d+)?)/);
      if (m) ts = m[1];
    }
    return { t: ts, text };
  }).filter(x => x.text);
});

console.log('lines', lines.length);
fs.writeFileSync(`${OUTDIR}/transcript-lines.json`, JSON.stringify(lines, null, 2));
fs.writeFileSync(`${OUTDIR}/transcript.txt`, lines.map(l => `${l.t}\t${l.text}`).join('\n'));
fs.writeFileSync(`${OUTDIR}/title.txt`, await page.title());
console.log('sample', lines.slice(0, 8));
console.log('tail', lines.slice(-3));
process.exit(0);
