# Copilot Cheatsheet — Workspace Instructions

## Branding

| Field | Value |
|-------|-------|
| Author | Shailesh Mishra |
| LinkedIn | https://www.linkedin.com/in/shaileshmishra1/ |
| Twitter | @sendtoshailesh |
| Instagram | @sendtoshailesh |
| Cheatsheet URL | https://sendtoshailesh.github.io/copilot-cheatsheet/How-To-GitHub-Copilot-Better-Than-99.html |
| GitHub Pages | https://sendtoshailesh.github.io/copilot-cheatsheet/ |
| Repo | sendtoshailesh/copilot-cheatsheet |

## Carousel Conventions

- **Format**: 1080×1350px, 4:5 portrait, GitHub dark theme
- **Slide count**: 14 (cover + 12 tips + CTA)
- **No QR codes** — use plain-text hyperlinks only
- **Branding footer** on every slide with author name + social links
- **Content density**: fill 85-90% of vertical space per tip slide
- **PDF export**: `node capture-carousel.js` (Puppeteer, 2x DPR)

## Design System

- Font: Inter (Google Fonts)
- Background: #0d1117 (GitHub dark)
- Accent colors rotate per tip: blue → green → orange → purple → cyan → pink → coral → yellow → red → teal → orange → blue

## File Naming

- Carousel HTML: `How-To-GitHub-Copilot-Better-Than-99-Carousel.html`
- Carousel PDF: `How-To-GitHub-Copilot-Better-Than-99-Carousel.pdf`
- Cover PNG: `How-To-GitHub-Copilot-Better-Than-99-Carousel-Cover.png`
- LinkedIn post: `linkedin-post-carousel.txt`
- Capture script: `capture-carousel.js`

## Pipeline

1. Research URLs → `content-researcher` skill
2. Generate HTML → `linkedin-carousel-generator` skill
3. Export PDF → `pdf-exporter` skill (runs `capture-carousel.js`)
4. Draft post → `social-post-drafter` skill
5. Push to GitHub Pages → `git add . && git commit && git push`
