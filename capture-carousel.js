const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const SLIDE_W = 1080;
const SLIDE_H = 1350;
const TOTAL_SLIDES = 14;
const DPR = 2; // retina

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none']
    });

    const page = await browser.newPage();
    await page.setViewport({ width: SLIDE_W, height: SLIDE_H, deviceScaleFactor: DPR });

    const htmlPath = path.resolve(__dirname, 'How-To-GitHub-Copilot-Better-Than-99-Carousel.html');
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0', timeout: 30000 });

    // Wait for fonts to load
    await page.evaluateHandle('document.fonts.ready');
    await new Promise(r => setTimeout(r, 2000));

    // Extra settling time for fonts and layout
    await new Promise(r => setTimeout(r, 500));

    // Hide the instructions bar and remove body padding/gap for PDF
    await page.evaluate(() => {
        const instr = document.querySelector('.instructions');
        if (instr) instr.style.display = 'none';
        document.body.style.padding = '0';
        document.body.style.gap = '0';
        document.body.style.margin = '0';
    });
    await new Promise(r => setTimeout(r, 500));

    // Count slides
    const slideCount = await page.evaluate(() => document.querySelectorAll('.slide').length);
    console.log(`Found ${slideCount} slides`);

    if (slideCount !== TOTAL_SLIDES) {
        console.warn(`⚠️  Expected ${TOTAL_SLIDES} slides, found ${slideCount}`);
    }

    // Generate PDF directly from the HTML page
    const pdfPath = path.resolve(__dirname, 'How-To-GitHub-Copilot-Better-Than-99-Carousel.pdf');
    await page.pdf({
        path: pdfPath,
        width: `${SLIDE_W}px`,
        height: `${SLIDE_H}px`,
        printBackground: true,
        margin: { top: 0, right: 0, bottom: 0, left: 0 },
        preferCSSPageSize: false
    });

    const pdfSize = (fs.statSync(pdfPath).size / 1024).toFixed(1);
    console.log(`\n✅ PDF saved: ${pdfPath}`);
    console.log(`   ${slideCount} pages, ${SLIDE_W}×${SLIDE_H}px, ${pdfSize} KB`);

    // Also save individual slide PNGs for preview (optional)
    // Re-get positions after layout change
    const slideOffsets = await page.evaluate(() => {
        const slides = document.querySelectorAll('.slide');
        return Array.from(slides).map(s => {
            const rect = s.getBoundingClientRect();
            return { top: rect.top + window.scrollY, height: rect.height };
        });
    });

    // Save just the cover slide as a preview PNG
    const coverPath = path.resolve(__dirname, 'How-To-GitHub-Copilot-Better-Than-99-Carousel-Cover.png');
    await page.screenshot({
        path: coverPath,
        type: 'png',
        clip: {
            x: 0,
            y: slideOffsets[0].top,
            width: SLIDE_W,
            height: SLIDE_H
        },
        omitBackground: false
    });
    console.log(`✅ Cover preview: ${coverPath}`);

    await browser.close();
    console.log('\n🎉 Done! Upload the PDF as a LinkedIn document post.');
})();
