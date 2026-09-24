import { chromium } from 'playwright-core';
import fs from 'fs';
const VIDEO = '6t5yF8ansoQ';
const OUTDIR = '/workspace/recap/tmp-0924-luca';
const CDP = process.env.CDP || 'http://127.0.0.1:9234';
const browser = await chromium.connectOverCDP(CDP);
const context = browser.contexts()[0];
// reuse existing YT tab if any
let page = context.pages().find(p => p.url().includes('6t5yF8ansoQ')) || await context.newPage();
if (!page.url().includes('6t5yF8ansoQ')) {
  await page.goto(`https://www.youtube.com/watch?v=${VIDEO}`, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(4000);
}
// ensure transcript open
for (const sel of ['button[aria-label="Show transcript"]','button:has-text("Show transcript")']) {
  try {
    const el = page.locator(sel).first();
    if (await el.isVisible({ timeout: 1500 })) { await el.click(); break; }
  } catch {}
}
await page.waitForTimeout(3000);
await page.waitForSelector('transcript-segment-view-model', { timeout: 20000 });
// scroll panel
for (let i=0;i<80;i++){
  await page.evaluate(() => {
    const els = document.querySelectorAll('transcript-segment-view-model');
    const last = els[els.length-1];
    if (last) last.scrollIntoView({block:'end'});
    // also try scrollable parent
    const panel = document.querySelector('ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"] #content')
      || document.querySelector('#panels') 
      || last?.closest('[style*="overflow"]');
    if (panel) panel.scrollTop = panel.scrollHeight;
  });
  await page.waitForTimeout(120);
}
const lines = await page.evaluate(() => {
  const segs = [...document.querySelectorAll('transcript-segment-view-model')];
  return segs.map(s => {
    const t = s.querySelector('.ytwTranscriptSegmentViewModelTimestamp')?.textContent?.trim() || '';
    const text = s.querySelector('.ytAttributedStringHost')?.textContent?.trim() || '';
    return { t, text };
  }).filter(x => x.text);
});
console.log('lines', lines.length, 'last', lines[lines.length-1]);
fs.writeFileSync(`${OUTDIR}/transcript-lines.json`, JSON.stringify(lines, null, 2));
fs.writeFileSync(`${OUTDIR}/transcript.txt`, lines.map(l => `${l.t}\t${l.text}`).join('\n'));
fs.writeFileSync(`${OUTDIR}/page2.html`, await page.content());
await page.screenshot({ path: `${OUTDIR}/debug2.png` });
process.exit(0);
