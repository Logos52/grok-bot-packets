const puppeteer = require('puppeteer-core');

const urls = process.argv.slice(2);
if (!urls.length) {
  console.error('Usage: node scrape.js <url> [url...]');
  process.exit(1);
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome',
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--window-size=1400,900',
      '--lang=en-US',
    ],
  });

  for (const url of urls) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 900 });
    await page.setUserAgent(
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    );
    console.log('\n========== URL ==========');
    console.log(url);
    console.log('=========================\n');

    try {
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 90000 });
      // Wait for flight results
      await page.waitForSelector('li, [role="listitem"], .pIav2d, .Rk10dc', { timeout: 45000 }).catch(() => {});
      await new Promise(r => setTimeout(r, 8000));

      // Try to dismiss cookie banners
      try {
        const buttons = await page.$$('button');
        for (const b of buttons) {
          const t = await page.evaluate(el => el.textContent || '', b);
          if (/Accept all|I agree|Reject all|Got it/i.test(t)) {
            await b.click().catch(() => {});
            await new Promise(r => setTimeout(r, 1000));
            break;
          }
        }
      } catch (_) {}

      await new Promise(r => setTimeout(r, 3000));

      // Screenshot for debugging
      const safe = url.includes('EWR') ? 'ewr' : url.includes('2026-09-24') ? 'jfk24' : 'jfk23';
      await page.screenshot({ path: `/workspace/flight-scrape/${safe}.png`, fullPage: false });

      // Extract text content of results area
      const data = await page.evaluate(() => {
        const bodyText = document.body.innerText || '';
        // Collect list items that look like flights
        const items = [];
        const candidates = document.querySelectorAll('li, [role="listitem"], .pIav2d');
        candidates.forEach((el, idx) => {
          const t = (el.innerText || '').trim();
          if (t.length > 40 && t.length < 2000 && (/\$|USD|hr|stop|Nonstop|Asiana|Qatar|Korean|United|Delta|ANA|JAL|EVA|Cathay|Emirates|Turkish|Vietnam|China|Singapore|Air Canada|American/i.test(t))) {
            items.push(t.replace(/\n+/g, ' | ').slice(0, 800));
          }
        });
        // Also get top of page for price summary
        return {
          title: document.title,
          items: items.slice(0, 40),
          bodySnippet: bodyText.slice(0, 12000),
        };
      });

      console.log('TITLE:', data.title);
      console.log('\n--- FLIGHT ITEMS ---');
      data.items.forEach((it, i) => console.log(`\n[${i}]\n${it}`));
      console.log('\n--- BODY SNIPPET ---');
      console.log(data.bodySnippet);
    } catch (e) {
      console.error('ERROR for', url, e.message);
      await page.screenshot({ path: `/workspace/flight-scrape/error.png` }).catch(() => {});
    }
    await page.close();
  }

  await browser.close();
})();
