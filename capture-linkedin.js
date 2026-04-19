const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none']
    });

    const page = await browser.newPage();

    // Fixed 1080×1350 viewport at 2x for retina (2160×2700 output)
    await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });

    const filePath = path.resolve(__dirname, 'How-To-GitHub-Copilot-Better-Than-99-LinkedIn-4x5.html');
    await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0', timeout: 30000 });

    // Wait for fonts
    await page.evaluateHandle('document.fonts.ready');
    await new Promise(r => setTimeout(r, 2000));

    const bodyHeight = await page.evaluate(() => document.body.scrollHeight);
    console.log(`Page height: ${bodyHeight}px (target: 1350px)`);

    // Capture exact 1080×1350 clip
    await page.screenshot({
        path: path.resolve(__dirname, 'How-To-GitHub-Copilot-Better-Than-99-LinkedIn.png'),
        type: 'png',
        clip: { x: 0, y: 0, width: 1080, height: 1350 },
        omitBackground: false
    });

    console.log('✅ Screenshot saved: How-To-GitHub-Copilot-Better-Than-99-LinkedIn.png');
    console.log(`   Output: 2160×2700px (1080×1350 @ 2x retina)`);

    await browser.close();
})();
