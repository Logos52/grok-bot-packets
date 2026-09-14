const puppeteer = require('puppeteer-core');
const fs = require('fs');

async function scrape(url, label) {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome-stable',
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--window-size=1400,900',
      '--lang=en-US'
    ]
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });
  await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36');
  await page.setExtraHTTPHeaders({ 'Accept-Language': 'en-US,en;q=0.9' });

  console.log(`[${label}] Navigating...`);
  await page.goto(url, { waitUntil: 'networkidle2', timeout: 90000 });
  await new Promise(r => setTimeout(r, 5000));

  // Try to dismiss consent if present
  try {
    const buttons = await page.$$('button');
    for (const b of buttons) {
      const t = await page.evaluate(el => el.textContent || '', b);
      if (/Accept all|I agree|Accept/i.test(t) && t.length < 40) {
        await b.click();
        await new Promise(r => setTimeout(r, 2000));
        break;
      }
    }
  } catch (e) {}

  // Wait for flight results / prices
  try {
    await page.waitForFunction(() => {
      const body = document.body.innerText;
      return /\$\d/.test(body) || /No flights|sold out|unavailable/i.test(body);
    }, { timeout: 45000 });
  } catch (e) {
    console.log(`[${label}] waitForFunction timeout`);
  }
  await new Promise(r => setTimeout(r, 3000));

  // Expand more flights if button exists
  try {
    const more = await page.$$('button');
    for (const b of more) {
      const t = await page.evaluate(el => (el.textContent || '').trim(), b);
      if (/View more flights|More flights|Show more/i.test(t)) {
        await b.click();
        await new Promise(r => setTimeout(r, 2500));
        break;
      }
    }
  } catch (e) {}

  const text = await page.evaluate(() => document.body.innerText);
  const html = await page.content();
  fs.writeFileSync(`/workspace/gf_${label}.txt`, text);
  fs.writeFileSync(`/workspace/gf_${label}.html`, html);
  await page.screenshot({ path: `/workspace/gf_${label}.png`, fullPage: true });

  // Extract structured-ish flight cards from text
  // Also try DOM extraction
  const cards = await page.evaluate(() => {
    const results = [];
    // Google Flights uses li elements with role or specific classes; try broad extraction
    const priceNodes = Array.from(document.querySelectorAll('[aria-label*="$"], [data-gs], span, div'))
      .filter(el => /^\$[\d,]+$/.test((el.textContent || '').trim()))
      .slice(0, 80);
    // Get nearby text from parent containers
    const seen = new Set();
    for (const p of priceNodes) {
      let container = p;
      for (let i = 0; i < 8; i++) {
        if (!container.parentElement) break;
        container = container.parentElement;
        const t = (container.innerText || '').trim();
        if (t.length > 40 && t.length < 800 && /\$/.test(t)) {
          const key = t.slice(0, 200);
          if (!seen.has(key)) {
            seen.add(key);
            results.push(t.replace(/\n+/g, ' | ').slice(0, 500));
          }
          break;
        }
      }
    }
    return results.slice(0, 40);
  });

  fs.writeFileSync(`/workspace/gf_${label}_cards.json`, JSON.stringify(cards, null, 2));
  console.log(`[${label}] cards: ${cards.length}`);
  console.log(`[${label}] text length: ${text.length}`);
  // Print Asiana-related lines
  const lines = text.split('\n').map(l => l.trim()).filter(Boolean);
  const asianaIdx = [];
  lines.forEach((l, i) => {
    if (/Asiana|OZ\b|ICN|Incheon|\$\d/.test(l)) asianaIdx.push(i);
  });
  // Dump a window around interesting lines
  const interesting = new Set();
  asianaIdx.forEach(i => {
    for (let j = Math.max(0, i - 3); j <= Math.min(lines.length - 1, i + 3); j++) interesting.add(j);
  });
  console.log(`--- ${label} interesting lines ---`);
  [...interesting].sort((a,b)=>a-b).slice(0, 120).forEach(i => console.log(`${i}: ${lines[i]}`));

  await browser.close();
  return { cards, textLen: text.length };
}

(async () => {
  const wed = 'https://www.google.com/travel/flights?hl=en&curr=USD&q=Flights%20to%20JFK%20from%20HAN%20on%202026-09-23%20oneway%201%20adult';
  const thu = 'https://www.google.com/travel/flights?hl=en&curr=USD&q=Flights%20to%20JFK%20from%20HAN%20on%202026-09-24%20oneway%201%20adult';
  await scrape(wed, 'wed23');
  await scrape(thu, 'thu24');
  console.log('DONE');
})().catch(e => { console.error(e); process.exit(1); });
