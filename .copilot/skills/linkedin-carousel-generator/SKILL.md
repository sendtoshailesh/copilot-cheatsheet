---
name: linkedin-carousel-generator
description: 'Generate LinkedIn carousel HTML files from natural language prompts. Creates 1080x1350px dark-themed slides with visual components, examples, inline links, branding footer, and print CSS for PDF export. USE FOR: create LinkedIn carousel, generate carousel HTML, build slide deck, create content slides.'
---

# LinkedIn Carousel Generator

Generate production-ready LinkedIn carousel HTML from content briefs.

## Design System

### Dimensions & Layout
- **Slide**: 1080×1350px (4:5 portrait)
- **Padding**: 52px top, 64px sides, 72px bottom
- **DPR**: 2x retina for PDF export

### Color Palette (GitHub Dark Theme)
```css
--bg: #0d1117;  --surface: #161b22;  --inset: #010409;
--border: #30363d;  --fg: #e6edf3;  --muted: #8b949e;
--blue: #58a6ff;  --green: #3fb950;  --purple: #bc8cff;
--orange: #d29922;  --red: #f85149;  --pink: #f778ba;
--cyan: #76e3ea;  --coral: #ea6045;  --yellow: #e3b341;  --teal: #39d353;
```

### Typography
- **Font**: Inter (Google Fonts)
- **h1**: 52-54px, weight 900
- **h2**: 36px, weight 800
- **Body**: 16-18px
- **Code**: SFMono-Regular, 14-15px

## Slide Structure (14 slides)

1. **Cover**: Gradient headline, author name, cover pill
2. **Tips 01-12**: Each fully consolidated on one page:
   - Top bar (brand + tip number + slide counter)
   - Emoji badge + category tag
   - Title (h2) + expanded description (2-3 sentences)
   - Visual component (terminal / code / flow diagram / comparison)
   - 4-5 bullet points
   - Example box with pro tip or sample code
   - Inline doc links (text only, no QR codes)
   - Branding footer
   - 14 progress dots
3. **CTA**: Headline, cheatsheet link, engagement prompts, connect links

## Visual Components

- `.terminal` — CLI examples with syntax highlighting
- `.mono-box` — File paths, config snippets
- `.visual-flow` — Horizontal step diagrams with arrows
- `.visual-compare` — Side-by-side comparison boxes
- `.example-box` — Pro tips, sample code, checklists

## Branding Footer (every slide)

```html
<div class="branding-footer">
  <span class="author">Shailesh Mishra</span>
  <div class="socials">
    <a href="https://www.linkedin.com/in/shaileshmishra1/">🔗 LinkedIn</a>
    <a href="https://twitter.com/sendtoshailesh">𝕏 @sendtoshailesh</a>
    <a href="https://instagram.com/sendtoshailesh">📷 @sendtoshailesh</a>
  </div>
</div>
```

## Content Density Target

Fill 85-90% of the 1350px vertical space. Each tip slide should include:
1. Title + tag + badge (compact header)
2. Description (2-3 sentences)
3. One visual component (make it substantial)
4. 4-5 bullet points with actionable detail
5. One example/pro-tip box
6. 2-3 inline doc links
7. Branding footer

## Color Rotation

Each tip gets a unique accent: blue → green → orange → purple → cyan → pink → coral → yellow → red → teal → orange → blue

## No QR Codes

Use plain-text hyperlinks only. All links are clickable in the HTML and visible in the PDF.
