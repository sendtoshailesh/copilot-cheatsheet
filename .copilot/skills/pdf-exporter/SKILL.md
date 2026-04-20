---
name: pdf-exporter
description: 'Export HTML content to PDF using Puppeteer. Supports LinkedIn carousels (multi-page) and screenshots. Handles fonts, dark backgrounds, and retina rendering. USE FOR: generate PDF from HTML, export carousel to PDF, Puppeteer screenshot, HTML to PDF conversion.'
---

# PDF Exporter

Export carousel HTML to production-quality PDFs using Puppeteer.

## Prerequisites

```json
{ "dependencies": { "puppeteer": "^24.41.0" } }
```

## Capture Script

The workspace includes `capture-carousel.js` which:

1. Launches headless Puppeteer at 1080×1350px, 2x DPR
2. Opens the carousel HTML via `file://` protocol
3. Waits for Google Fonts (`document.fonts.ready` + 2s delay)
4. Hides instructions bar, removes body padding
5. Generates multi-page PDF with `printBackground: true`
6. Saves cover PNG screenshot

### Run

```bash
node capture-carousel.js
```

### Key Settings

| Setting | Value | Notes |
|---------|-------|-------|
| `TOTAL_SLIDES` | 14 | Must match actual slide count |
| `deviceScaleFactor` | 2 | Retina quality |
| `waitUntil` | `networkidle0` | All resources loaded |
| `printBackground` | `true` | Preserves dark backgrounds |

## Verification

After generating, verify:
- Page count: `mdls -name kMDItemNumberOfPages *.pdf`
- File size: should be 500KB–2MB for 14 slides
- Cover PNG: should be 1080×1350 visible content

## Troubleshooting

| Issue | Fix |
|-------|-----|
| White backgrounds | Add `printBackground: true` |
| Blurry text | Set `deviceScaleFactor: 2` |
| Wrong page count | Check print CSS `page-break-after: always` |
| Fonts missing | Add font wait + 2s delay |
