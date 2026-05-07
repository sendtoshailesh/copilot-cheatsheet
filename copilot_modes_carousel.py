"""
GitHub Copilot CLI: Research vs Ask vs Plan Mode — LinkedIn PDF Carousel
Author: Shailesh | linkedin.com/in/shaileshmishra1

Usage:
    pip install Pillow
    python copilot_modes_carousel.py

Output: copilot_modes_comparison_carousel.pdf (10 slides, 1080x1080 each)
Upload to LinkedIn as Document post.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

W, H = 1080, 1080
BG_COLOR = (13, 17, 23)        # #0D1117 - GitHub Dark
CARD_BG = (22, 27, 34)         # #161B22
BORDER_COLOR = (48, 54, 61)    # #30363D
TEXT_PRIMARY = (255, 255, 255)  # White
TEXT_SECONDARY = (201, 209, 217)  # #C9D1D9
TEXT_MUTED = (139, 148, 158)   # #8B949E

BLUE = (88, 166, 255)          # #58A6FF - Research
GREEN = (63, 185, 80)          # #3FB950 - Ask/Execute
ORANGE = (247, 129, 102)       # #F78166 - Plan
PURPLE = (163, 113, 247)       # #A371F7 - Accent

AUTHOR = "Shailesh"
LINKEDIN = "linkedin.com/in/shaileshmishra1"

# ─── FONT LOADING ─────────────────────────────────────────────────────────────

def load_fonts():
    """Try to load system fonts, fall back to default."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    
    font_file = None
    for fp in font_paths:
        if os.path.exists(fp):
            font_file = fp
            break
    
    if font_file:
        return {
            "hero": ImageFont.truetype(font_file, 64),
            "title": ImageFont.truetype(font_file, 48),
            "subtitle": ImageFont.truetype(font_file, 36),
            "body": ImageFont.truetype(font_file, 28),
            "small": ImageFont.truetype(font_file, 22),
            "tiny": ImageFont.truetype(font_file, 18),
            "badge": ImageFont.truetype(font_file, 20),
        }
    else:
        default = ImageFont.load_default()
        return {k: default for k in ["hero", "title", "subtitle", "body", "small", "tiny", "badge"]}


FONTS = load_fonts()

# ─── DRAWING HELPERS ──────────────────────────────────────────────────────────

def new_slide():
    """Create a blank slide with background."""
    img = Image.new("RGB", (W, H), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    return img, draw


def draw_header_footer(draw, slide_num, total=10):
    """Draw consistent header and footer branding."""
    # Top accent line
    draw.rectangle([(0, 0), (W, 4)], fill=PURPLE)
    
    # Footer
    draw.rectangle([(0, H - 60), (W, H)], fill=(10, 13, 18))
    draw.text((30, H - 45), f"Created by {AUTHOR}", font=FONTS["tiny"], fill=TEXT_MUTED)
    draw.text((W - 30, H - 45), f"{slide_num}/{total}", font=FONTS["tiny"], fill=TEXT_MUTED, anchor="ra")
    draw.text((W // 2, H - 45), LINKEDIN, font=FONTS["tiny"], fill=BLUE, anchor="ma")


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=2):
    """Draw a rounded rectangle."""
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_accent_bar(draw, y, color, width_pct=0.3):
    """Draw a horizontal accent bar."""
    bar_w = int(W * width_pct)
    x_start = (W - bar_w) // 2
    draw.rounded_rectangle(
        [(x_start, y), (x_start + bar_w, y + 4)],
        radius=2, fill=color
    )


# ─── SLIDE GENERATORS ─────────────────────────────────────────────────────────

def slide_cover():
    """Slide 1: Cover."""
    img, draw = new_slide()
    
    # Large centered content
    draw.text((W // 2, 200), "GitHub Copilot CLI", font=FONTS["title"], fill=TEXT_PRIMARY, anchor="mm")
    
    # Three colored dots
    dot_y = 300
    for i, (color, label) in enumerate([
        (BLUE, "/research"), (GREEN, "Ask/Execute"), (ORANGE, "Plan")
    ]):
        x = W // 2 + (i - 1) * 200
        draw.ellipse([(x - 15, dot_y - 15), (x + 15, dot_y + 15)], fill=color)
        draw.text((x, dot_y + 40), label, font=FONTS["small"], fill=color, anchor="mm")
    
    # Main title
    draw.text((W // 2, 480), "3 Modes.", font=FONTS["hero"], fill=TEXT_PRIMARY, anchor="mm")
    draw.text((W // 2, 560), "3 Ways to Think.", font=FONTS["hero"], fill=PURPLE, anchor="mm")
    draw.text((W // 2, 650), "1 Powerful Workflow.", font=FONTS["subtitle"], fill=TEXT_SECONDARY, anchor="mm")
    
    # Subtitle
    draw.text((W // 2, 780), "Most developers only use one.", font=FONTS["body"], fill=TEXT_MUTED, anchor="mm")
    draw.text((W // 2, 830), "Here's how to use all three.", font=FONTS["body"], fill=TEXT_SECONDARY, anchor="mm")
    
    # Author
    draw.text((W // 2, 950), f"by {AUTHOR}", font=FONTS["subtitle"], fill=TEXT_PRIMARY, anchor="mm")
    draw.text((W // 2, 1000), LINKEDIN, font=FONTS["small"], fill=BLUE, anchor="mm")
    
    draw_header_footer(draw, 1)
    return img


def slide_problem():
    """Slide 2: The Problem."""
    img, draw = new_slide()
    draw_header_footer(draw, 2)
    
    draw.text((W // 2, 120), "The Problem", font=FONTS["title"], fill=TEXT_PRIMARY, anchor="mm")
    draw_accent_bar(draw, 160, PURPLE)
    
    # Problem statement card
    draw_rounded_rect(draw, [80, 220, W - 80, 520], radius=16, fill=CARD_BG, outline=BORDER_COLOR)
    draw.text((W // 2, 300), "90% of Copilot CLI users", font=FONTS["body"], fill=TEXT_SECONDARY, anchor="mm")
    draw.text((W // 2, 350), "only use the default mode.", font=FONTS["body"], fill=TEXT_SECONDARY, anchor="mm")
    draw.text((W // 2, 430), "They're missing 66% of", font=FONTS["subtitle"], fill=TEXT_PRIMARY, anchor="mm")
    draw.text((W // 2, 480), "Copilot's thinking power.", font=FONTS["subtitle"], fill=ORANGE, anchor="mm")
    
    # Three mode indicators
    modes_y = 620
    for i, (emoji, name, color, desc) in enumerate([
        ("🔍", "/research", BLUE, "Deep investigation"),
        ("💬", "Ask/Execute", GREEN, "Interactive coding"),
        ("🗺️", "Plan Mode", ORANGE, "Structured planning"),
    ]):
        y = modes_y + i * 100
        draw_rounded_rect(draw, [120, y, W - 120, y + 80], radius=12, fill=CARD_BG, outline=color)
        draw.text((180, y + 40), name, font=FONTS["body"], fill=color, anchor="lm")
        draw.text((W - 160, y + 40), desc, font=FONTS["small"], fill=TEXT_SECONDARY, anchor="rm")
    
    return img


def slide_mode(mode_data, slide_num):
    """Generate a slide for a specific mode."""
    img, draw = new_slide()
    draw_header_footer(draw, slide_num)
    
    color = mode_data["color"]
    
    # Mode badge
    draw.text((W // 2, 100), mode_data["lifecycle"], font=FONTS["badge"], fill=color, anchor="mm")
    draw_accent_bar(draw, 125, color, 0.15)
    
    # Mode name
    draw.text((W // 2, 200), mode_data["name"], font=FONTS["title"], fill=color, anchor="mm")
    draw.text((W // 2, 260), mode_data["tagline"], font=FONTS["subtitle"], fill=TEXT_PRIMARY, anchor="mm")
    
    # Main card
    draw_rounded_rect(draw, [80, 320, W - 80, 900], radius=16, fill=CARD_BG, outline=color)
    
    # Description
    draw.text((W // 2, 370), mode_data["description"].replace("\n", " "), 
              font=FONTS["body"], fill=TEXT_SECONDARY, anchor="mm")
    
    # Divider
    draw.line([(160, 420), (W - 160, 420)], fill=color, width=1)
    
    # Use cases
    y = 470
    for use in mode_data["uses"]:
        draw.ellipse([(150, y + 8), (162, y + 20)], fill=color)
        draw.text((180, y + 2), use, font=FONTS["body"], fill=TEXT_PRIMARY)
        y += 55
    
    # Output section
    draw.line([(160, y + 20), (W - 160, y + 20)], fill=BORDER_COLOR, width=1)
    draw.text((150, y + 50), "Output:", font=FONTS["small"], fill=TEXT_MUTED)
    draw.text((280, y + 50), mode_data["output"], font=FONTS["small"], fill=color)
    
    # Edits files
    draw.text((150, y + 95), "Edits files:", font=FONTS["small"], fill=TEXT_MUTED)
    draw.text((320, y + 95), mode_data["edits_files"], font=FONTS["small"], fill=TEXT_PRIMARY)
    
    # Activation
    activations = {
        "/research": "Trigger: /research TOPIC",
        "Ask/Execute": "Trigger: Default mode (just run copilot)",
        "Plan Mode": "Trigger: Shift+Tab or /plan or --plan",
    }
    draw.text((W // 2, 940), activations[mode_data["name"]], 
              font=FONTS["small"], fill=TEXT_MUTED, anchor="mm")
    
    return img


def slide_comparison():
    """Slide 6: Comparison Matrix."""
    img, draw = new_slide()
    draw_header_footer(draw, 6)
    
    draw.text((W // 2, 80), "Quick Comparison", font=FONTS["title"], fill=TEXT_PRIMARY, anchor="mm")
    draw_accent_bar(draw, 115, PURPLE)
    
    # Table
    headers = ["", "/research", "Ask/Execute", "Plan Mode"]
    rows = [
        ["Edits files?", "❌ Never", "✅ Yes", "❌ No"],
        ["Asks questions?", "❌ Never", "✅ Yes", "✅ Up-front"],
        ["Output", "Report .md", "Code edits", "plan.md"],
        ["Speed", "Slow", "Fast", "Medium"],
        ["Model", "Hardcoded", "Your choice", "Your choice"],
        ["Data sources", "Code+Web+GH", "Local code", "Local code"],
        ["Best for", "Investigate", "Quick tasks", "Design"],
    ]
    
    # Header row
    col_w = (W - 160) // 4
    start_x = 80
    header_y = 170
    
    colors = [TEXT_MUTED, BLUE, GREEN, ORANGE]
    for i, (header, color) in enumerate(zip(headers, colors)):
        x = start_x + i * col_w + col_w // 2
        draw.text((x, header_y), header, font=FONTS["small"], fill=color, anchor="mm")
    
    # Separator
    draw.line([(100, header_y + 25), (W - 100, header_y + 25)], fill=BORDER_COLOR, width=1)
    
    # Data rows
    for row_idx, row in enumerate(rows):
        y = header_y + 60 + row_idx * 85
        
        # Alternating row background
        if row_idx % 2 == 0:
            draw.rounded_rectangle(
                [(90, y - 20), (W - 90, y + 50)],
                radius=8, fill=(18, 22, 28)
            )
        
        for col_idx, (cell, color) in enumerate(zip(row, colors)):
            x = start_x + col_idx * col_w + col_w // 2
            font = FONTS["tiny"] if col_idx == 0 else FONTS["small"]
            draw.text((x, y + 15), cell, font=font, fill=color, anchor="mm")
    
    return img


def slide_lifecycle():
    """Slide 7: DevOps Lifecycle Mapping."""
    img, draw = new_slide()
    draw_header_footer(draw, 7)
    
    draw.text((W // 2, 80), "Dev Lifecycle Mapping", font=FONTS["title"], fill=TEXT_PRIMARY, anchor="mm")
    draw_accent_bar(draw, 115, PURPLE)
    
    # Flow diagram (horizontal)
    phases = [
        ("DISCOVER", "/research", BLUE),
        ("DESIGN", "Plan Mode", ORANGE),
        ("BUILD", "Ask/Execute", GREEN),
        ("SHIP", "Ask + /review", GREEN),
    ]
    
    box_w = 200
    box_h = 140
    start_x = 80
    gap = (W - 2 * start_x - 4 * box_w) // 3
    y_center = 350
    
    for i, (phase, mode, color) in enumerate(phases):
        x = start_x + i * (box_w + gap)
        
        # Box
        draw_rounded_rect(
            draw, [x, y_center - box_h // 2, x + box_w, y_center + box_h // 2],
            radius=12, fill=CARD_BG, outline=color, width=2
        )
        
        # Phase name
        draw.text((x + box_w // 2, y_center - 20), phase, 
                  font=FONTS["small"], fill=color, anchor="mm")
        # Mode name
        draw.text((x + box_w // 2, y_center + 20), mode,
                  font=FONTS["tiny"], fill=TEXT_SECONDARY, anchor="mm")
        
        # Arrow
        if i < len(phases) - 1:
            arrow_x = x + box_w + 5
            arrow_end = arrow_x + gap - 10
            draw.line([(arrow_x, y_center), (arrow_end, y_center)], fill=TEXT_MUTED, width=2)
            # Arrowhead
            draw.polygon([(arrow_end, y_center - 6), (arrow_end + 10, y_center), 
                         (arrow_end, y_center + 6)], fill=TEXT_MUTED)
    
    # Description below
    desc_y = 500
    draw_rounded_rect(draw, [80, desc_y, W - 80, desc_y + 320], radius=16, fill=CARD_BG, outline=BORDER_COLOR)
    
    flow_text = [
        ("🔍 Research first:", "Understand the problem landscape", BLUE),
        ("🗺️ Plan next:", "Break into structured steps", ORANGE),
        ("💬 Build then:", "Implement with interactive edits", GREEN),
        ("🚀 Ship finally:", "Review, fix CI, merge", GREEN),
    ]
    
    for i, (label, desc, color) in enumerate(flow_text):
        y = desc_y + 40 + i * 70
        draw.text((140, y), label, font=FONTS["body"], fill=color)
        draw.text((140, y + 32), desc, font=FONTS["small"], fill=TEXT_SECONDARY)
    
    return img


def slide_decision_tree():
    """Slide 8: Decision Tree."""
    img, draw = new_slide()
    draw_header_footer(draw, 8)
    
    draw.text((W // 2, 80), "Which Mode Do I Use?", font=FONTS["title"], fill=TEXT_PRIMARY, anchor="mm")
    draw_accent_bar(draw, 115, PURPLE)
    
    # Start node
    draw_rounded_rect(draw, [340, 170, 740, 230], radius=12, fill=CARD_BG, outline=PURPLE)
    draw.text((W // 2, 200), "What do you need?", font=FONTS["body"], fill=PURPLE, anchor="mm")
    
    # Three branches
    branches = [
        (180, "Understand deeply", "/research", "→ Get a comprehensive\n   report with citations", BLUE),
        (540, "Build/fix something", "Ask/Execute", "→ Interactive coding\n   with real-time edits", GREEN),
        (900, "Plan something complex", "Plan Mode", "→ Structured plan.md\n   before any code", ORANGE),
    ]
    
    for x, question, mode, result, color in branches:
        # Connector line
        draw.line([(W // 2, 230), (x, 310)], fill=TEXT_MUTED, width=1)
        
        # Question
        draw_rounded_rect(draw, [x - 140, 310, x + 140, 380], radius=10, fill=CARD_BG, outline=color)
        draw.text((x, 345), question, font=FONTS["small"], fill=color, anchor="mm")
        
        # Arrow down
        draw.line([(x, 380), (x, 420)], fill=color, width=2)
        
        # Mode box
        draw_rounded_rect(draw, [x - 120, 420, x + 120, 480], radius=10, fill=color + (40,), outline=color)
        draw.text((x, 450), mode, font=FONTS["body"], fill=color, anchor="mm")
        
        # Result
        for j, line in enumerate(result.split("\n")):
            draw.text((x, 510 + j * 28), line, font=FONTS["small"], fill=TEXT_SECONDARY, anchor="mm")
    
    # Pro tip at bottom
    draw_rounded_rect(draw, [100, 700, W - 100, 830], radius=12, fill=(30, 20, 10), outline=ORANGE)
    draw.text((W // 2, 730), "💡 Pro Tip: Not sure? Start with the full workflow:", 
              font=FONTS["small"], fill=ORANGE, anchor="mm")
    draw.text((W // 2, 780), "/research → /plan → implement → ship",
              font=FONTS["body"], fill=TEXT_PRIMARY, anchor="mm")
    
    return img


def slide_power_workflow():
    """Slide 9: Power user workflow."""
    img, draw = new_slide()
    draw_header_footer(draw, 9)
    
    draw.text((W // 2, 80), "The Power Workflow", font=FONTS["title"], fill=TEXT_PRIMARY, anchor="mm")
    draw.text((W // 2, 130), "What 99% of users don't do", font=FONTS["small"], fill=TEXT_MUTED, anchor="mm")
    draw_accent_bar(draw, 160, PURPLE)
    
    steps = [
        ("1", "/research How is auth implemented?", BLUE, "Deep dive report"),
        ("2", "/plan Implement password reset", ORANGE, "Structured plan.md"),
        ("3", "Review plan → Approve", PURPLE, "Ctrl+Y to edit plan"),
        ("4", "Accept & build on Autopilot", GREEN, "Hands-free execution"),
        ("5", "Run tests → Fix → Commit", GREEN, "Ship with confidence"),
    ]
    
    y_start = 220
    for i, (num, command, color, note) in enumerate(steps):
        y = y_start + i * 130
        
        # Step number circle
        draw.ellipse([(100, y + 10), (140, y + 50)], fill=color)
        draw.text((120, y + 30), num, font=FONTS["body"], fill=BG_COLOR, anchor="mm")
        
        # Command card
        draw_rounded_rect(draw, [170, y, W - 120, y + 65], radius=10, fill=CARD_BG, outline=color)
        draw.text((200, y + 18), command, font=FONTS["small"], fill=TEXT_PRIMARY)
        draw.text((200, y + 44), note, font=FONTS["tiny"], fill=TEXT_MUTED)
        
        # Connector
        if i < len(steps) - 1:
            draw.line([(120, y + 50), (120, y + 130 + 10)], fill=BORDER_COLOR, width=1)
    
    return img


def slide_cta():
    """Slide 10: CTA."""
    img, draw = new_slide()
    draw_header_footer(draw, 10)
    
    # Main CTA
    draw.text((W // 2, 250), "Start Using", font=FONTS["title"], fill=TEXT_SECONDARY, anchor="mm")
    draw.text((W // 2, 320), "All Three Modes", font=FONTS["hero"], fill=TEXT_PRIMARY, anchor="mm")
    draw.text((W // 2, 400), "Today.", font=FONTS["hero"], fill=PURPLE, anchor="mm")
    
    # Quick reference
    draw_rounded_rect(draw, [150, 480, W - 150, 700], radius=16, fill=CARD_BG, outline=BORDER_COLOR)
    
    commands = [
        ("copilot", "→ Ask/Execute (default)", GREEN),
        ("/research TOPIC", "→ Deep investigation", BLUE),
        ("Shift+Tab", "→ Plan mode", ORANGE),
        ("--autopilot", "→ Hands-free execution", PURPLE),
    ]
    
    for i, (cmd, desc, color) in enumerate(commands):
        y = 510 + i * 45
        draw.text((200, y), cmd, font=FONTS["small"], fill=color)
        draw.text((550, y), desc, font=FONTS["small"], fill=TEXT_SECONDARY)
    
    # Author
    draw.text((W // 2, 780), f"Follow {AUTHOR} for more", font=FONTS["subtitle"], fill=TEXT_PRIMARY, anchor="mm")
    draw.text((W // 2, 840), LINKEDIN, font=FONTS["body"], fill=BLUE, anchor="mm")
    
    # Hashtags
    draw.text((W // 2, 930), "#GitHubCopilot  #CopilotCLI  #DevTools  #AI", 
              font=FONTS["tiny"], fill=TEXT_MUTED, anchor="mm")
    
    return img


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("🎨 Generating GitHub Copilot Modes Comparison Carousel...")
    print(f"   Author: {AUTHOR} | {LINKEDIN}")
    print(f"   Dimensions: {W}×{H} px per slide")
    print()
    
    slides = [
        ("Cover", slide_cover()),
        ("Problem", slide_problem()),
        ("Research Mode", slide_mode(MODES[0], 3)),
        ("Ask/Execute Mode", slide_mode(MODES[1], 4)),
        ("Plan Mode", slide_mode(MODES[2], 5)),
        ("Comparison", slide_comparison()),
        ("Lifecycle", slide_lifecycle()),
        ("Decision Tree", slide_decision_tree()),
        ("Power Workflow", slide_power_workflow()),
        ("CTA", slide_cta()),
    ]
    
    # Save individual PNGs
    os.makedirs("carousel_slides", exist_ok=True)
    for i, (name, img) in enumerate(slides):
        filepath = f"carousel_slides/slide_{i+1:02d}_{name.lower().replace(' ', '_')}.png"
        img.save(filepath, "PNG")
        print(f"   ✅ Slide {i+1}/10: {name} → {filepath}")
    
    # Save as multi-page PDF
    pdf_path = "copilot_modes_comparison_carousel.pdf"
    slides[0][1].save(
        pdf_path,
        save_all=True,
        append_images=[s[1] for s in slides[1:]],
        resolution=72,
    )
    print(f"\n   📄 PDF Carousel: {pdf_path}")
    print(f"   📁 Individual PNGs: carousel_slides/")
    print(f"\n🚀 Upload to LinkedIn:")
    print(f"   Share → + → Document → Select {pdf_path}")
    print(f"   Use 10 slides to maximize swipe engagement!")


if __name__ == "__main__":
    main()
