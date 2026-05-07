"""
GitHub Copilot CLI: Research vs Ask vs Plan Mode — Animated Comparison
Author: Shailesh | linkedin.com/in/shaileshmishra1

Usage:
    pip install manim
    manim -p --resolution 1080,1080 --fps 30 copilot_modes_animated.py CopilotModesComparison

Output: media/videos/copilot_modes_animated/1080p30/CopilotModesComparison.mp4
Upload to LinkedIn as a video post.
"""

from manim import *

config.background_color = "#0D1117"

BLUE = "#58A6FF"
GREEN = "#3FB950"
ORANGE = "#F78166"
CARD_BG = "#161B22"
BORDER = "#30363D"
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#C9D1D9"
TEXT_MUTED = "#8B949E"
ACCENT_PURPLE = "#A371F7"

MODES = [
    {
        "name": "/research",
        "emoji": "🔍",
        "color": BLUE,
        "tagline": "Explorer's Mind",
        "description": "Deep autonomous\ninvestigation",
        "uses": [
            "Understand unfamiliar code",
            "Explore architecture patterns",
            "Pre-coding investigation",
            "Comprehensive reports",
        ],
        "lifecycle": "DISCOVERY",
        "output": "report.md with citations",
        "edits_files": "❌ Never",
    },
    {
        "name": "Ask/Execute",
        "emoji": "💬",
        "color": GREEN,
        "tagline": "Builder's Mind",
        "description": "Interactive\niteration & edits",
        "uses": [
            "Quick bug fixes",
            "Write & edit code",
            "Run shell commands",
            "Iterative development",
        ],
        "lifecycle": "BUILD",
        "output": "Working code + file edits",
        "edits_files": "✅ Yes (with approval)",
    },
    {
        "name": "Plan Mode",
        "emoji": "🗺️",
        "color": ORANGE,
        "tagline": "Architect's Mind",
        "description": "Structure first,\ncode later",
        "uses": [
            "Complex multi-file tasks",
            "New feature design",
            "Refactoring strategy",
            "Architecture decisions",
        ],
        "lifecycle": "DESIGN",
        "output": "plan.md with checkboxes",
        "edits_files": "❌ Plans only",
    },
]


class CopilotModesComparison(Scene):
    def construct(self):
        self._scene_intro()
        self.wait(0.5)
        self._scene_three_cards()
        self.wait(0.8)
        self._scene_comparison_table()
        self.wait(0.8)
        self._scene_lifecycle()
        self.wait(0.8)
        self._scene_outro()
        self.wait(1.5)

    def _scene_intro(self):
        """Title slide with branding."""
        title = Text(
            "GitHub Copilot CLI",
            font_size=52,
            color=TEXT_PRIMARY,
            weight=BOLD,
        ).shift(UP * 1.2)

        subtitle = Text(
            "3 Ways to Think with AI",
            font_size=36,
            color=ACCENT_PURPLE,
        ).next_to(title, DOWN, buff=0.4)

        author = Text(
            "by Shailesh | linkedin.com/in/shaileshmishra1",
            font_size=20,
            color=TEXT_MUTED,
        ).to_edge(DOWN, buff=0.5)

        # Animated GitHub-style border
        border = RoundedRectangle(
            width=10, height=6, corner_radius=0.3,
            stroke_color=BORDER, stroke_width=1.5
        )

        self.play(Create(border), run_time=0.8)
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(author), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, subtitle, author, border)), run_time=0.6)

    def _build_mode_card(self, mode: dict, scale: float = 1.0) -> VGroup:
        """Build a single mode card."""
        color = mode["color"]

        bg = RoundedRectangle(
            width=3.4 * scale, height=5.0 * scale,
            corner_radius=0.2,
            fill_color=CARD_BG, fill_opacity=1,
            stroke_color=color, stroke_width=2,
        )

        # Header accent
        header_bar = Rectangle(
            width=3.4 * scale, height=0.08 * scale,
            fill_color=color, fill_opacity=1, stroke_width=0,
        ).align_to(bg, UP).shift(DOWN * 0.01)

        # Mode name
        name_text = Text(
            mode["name"], font_size=int(26 * scale),
            color=color, weight=BOLD,
        ).move_to(bg.get_top() + DOWN * 0.5 * scale)

        # Tagline
        tagline = Text(
            mode["tagline"], font_size=int(18 * scale),
            color=TEXT_SECONDARY,
        ).next_to(name_text, DOWN, buff=0.15 * scale)

        # Lifecycle badge
        badge_bg = RoundedRectangle(
            width=1.8 * scale, height=0.35 * scale,
            corner_radius=0.1,
            fill_color=color, fill_opacity=0.15,
            stroke_color=color, stroke_width=1,
        ).next_to(tagline, DOWN, buff=0.2 * scale)

        badge_text = Text(
            mode["lifecycle"], font_size=int(14 * scale),
            color=color, weight=BOLD,
        ).move_to(badge_bg)

        # Use cases
        bullets = VGroup()
        for use in mode["uses"][:3]:
            dot = Dot(radius=0.04 * scale, color=color)
            txt = Text(use, font_size=int(14 * scale), color=TEXT_SECONDARY)
            bullet = VGroup(dot, txt).arrange(RIGHT, buff=0.1 * scale)
            bullets.add(bullet)
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.12 * scale)
        bullets.next_to(badge_bg, DOWN, buff=0.25 * scale)

        # Edits files indicator
        edit_text = Text(
            f"Edits files: {mode['edits_files']}",
            font_size=int(12 * scale),
            color=TEXT_MUTED,
        ).align_to(bg, DOWN).shift(UP * 0.3 * scale)

        return VGroup(bg, header_bar, name_text, tagline, badge_bg, badge_text, bullets, edit_text)

    def _scene_three_cards(self):
        """Show 3 mode cards flying in."""
        cards = VGroup()
        for mode in MODES:
            card = self._build_mode_card(mode, scale=0.9)
            cards.add(card)

        cards.arrange(RIGHT, buff=0.3)
        cards.move_to(ORIGIN)

        # Fly cards in from bottom
        for card in cards:
            card.save_state()
            card.shift(DOWN * 6).set_opacity(0)

        self.play(
            *[
                card.animate.restore()
                for card in cards
            ],
            lag_ratio=0.2,
            run_time=1.8,
        )

        # Highlight each card
        for i, card in enumerate(cards):
            self.play(
                card.animate.scale(1.05),
                run_time=0.3,
            )
            self.play(
                card.animate.scale(1 / 1.05),
                run_time=0.3,
            )

        self.wait(2.0)
        self.play(FadeOut(cards), run_time=0.6)

    def _scene_comparison_table(self):
        """Animated comparison table."""
        header = Text(
            "Side-by-Side Comparison",
            font_size=32, color=TEXT_PRIMARY, weight=BOLD,
        ).to_edge(UP, buff=0.5)

        self.play(Write(header), run_time=0.6)

        table_data = [
            ["Can edit files?", "❌ Never", "✅ Yes", "❌ Plans only"],
            ["Asks questions?", "❌ Autonomous", "✅ Interactive", "✅ Up-front"],
            ["Output", "Report .md", "Code changes", "plan.md"],
            ["Speed", "Slow (thorough)", "Fast", "Medium"],
            ["Model", "Hardcoded", "Configurable", "Configurable"],
            ["Best for", "Investigation", "Quick tasks", "Complex features"],
        ]

        # Column headers
        col_headers = VGroup(
            Text("", font_size=16),
            Text("/research", font_size=18, color=BLUE, weight=BOLD),
            Text("Ask/Execute", font_size=18, color=GREEN, weight=BOLD),
            Text("Plan", font_size=18, color=ORANGE, weight=BOLD),
        ).arrange(RIGHT, buff=0.8).next_to(header, DOWN, buff=0.5)
        col_headers[0].set_width(2.0)

        self.play(FadeIn(col_headers), run_time=0.5)

        rows = VGroup()
        for row_data in table_data:
            cells = VGroup(
                Text(row_data[0], font_size=14, color=TEXT_MUTED).set_width(2.0),
                Text(row_data[1], font_size=14, color=BLUE),
                Text(row_data[2], font_size=14, color=GREEN),
                Text(row_data[3], font_size=14, color=ORANGE),
            ).arrange(RIGHT, buff=0.8)
            rows.add(cells)

        rows.arrange(DOWN, buff=0.25)
        rows.next_to(col_headers, DOWN, buff=0.4)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(2.5)
        self.play(FadeOut(VGroup(header, col_headers, rows)), run_time=0.6)

    def _scene_lifecycle(self):
        """Show DevOps lifecycle flow."""
        header = Text(
            "When to Use Each",
            font_size=32, color=TEXT_PRIMARY, weight=BOLD,
        ).to_edge(UP, buff=0.5)

        self.play(Write(header), run_time=0.6)

        # Create flow boxes
        phases = [
            ("DISCOVER", "/research", BLUE, "🔍"),
            ("DESIGN", "Plan Mode", ORANGE, "🗺️"),
            ("BUILD", "Ask/Execute", GREEN, "💬"),
            ("SHIP", "Ask + /review", GREEN, "🚀"),
        ]

        flow_group = VGroup()
        arrows = VGroup()

        for i, (phase, mode, color, emoji) in enumerate(phases):
            box = RoundedRectangle(
                width=2.2, height=1.6, corner_radius=0.15,
                fill_color=CARD_BG, fill_opacity=1,
                stroke_color=color, stroke_width=2,
            )
            phase_text = Text(phase, font_size=16, color=color, weight=BOLD)
            mode_text = Text(mode, font_size=13, color=TEXT_SECONDARY)
            label = VGroup(phase_text, mode_text).arrange(DOWN, buff=0.1)
            label.move_to(box)
            flow_group.add(VGroup(box, label))

        flow_group.arrange(RIGHT, buff=0.5)
        flow_group.move_to(ORIGIN)

        # Animate boxes appearing
        for i, box_group in enumerate(flow_group):
            box_group.save_state()
            box_group.set_opacity(0).shift(DOWN * 2)

        self.play(
            *[box_group.animate.restore() for box_group in flow_group],
            lag_ratio=0.25,
            run_time=2.0,
        )

        # Draw arrows between
        for i in range(len(flow_group) - 1):
            start = flow_group[i].get_right()
            end = flow_group[i + 1].get_left()
            arrow = Arrow(start, end, color=TEXT_MUTED, stroke_width=2, buff=0.1)
            self.play(Create(arrow), run_time=0.3)

        self.wait(2.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)

    def _scene_outro(self):
        """Outro with CTA."""
        main_text = Text(
            "Stop using just one mode.",
            font_size=36, color=TEXT_PRIMARY, weight=BOLD,
        ).shift(UP * 1.0)

        sub_text = Text(
            "Research → Plan → Build → Ship",
            font_size=28, color=ACCENT_PURPLE,
        ).next_to(main_text, DOWN, buff=0.4)

        author = VGroup(
            Text("Shailesh", font_size=24, color=TEXT_PRIMARY, weight=BOLD),
            Text("linkedin.com/in/shaileshmishra1", font_size=18, color=BLUE),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.8)

        # Color dots representing the three modes
        dots = VGroup(
            Dot(radius=0.12, color=BLUE),
            Dot(radius=0.12, color=GREEN),
            Dot(radius=0.12, color=ORANGE),
        ).arrange(RIGHT, buff=0.3).next_to(sub_text, DOWN, buff=0.5)

        self.play(Write(main_text), run_time=1.0)
        self.play(FadeIn(sub_text, shift=UP * 0.2), run_time=0.7)
        self.play(
            *[GrowFromCenter(dot) for dot in dots],
            lag_ratio=0.15,
            run_time=0.8,
        )
        self.play(FadeIn(author, shift=UP * 0.3), run_time=0.7)


class CopilotDecisionTree(Scene):
    """Bonus scene: Decision tree for choosing a mode."""

    def construct(self):
        title = Text(
            "Which Mode Should I Use?",
            font_size=36, color=TEXT_PRIMARY, weight=BOLD,
        ).to_edge(UP, buff=0.4)

        self.play(Write(title), run_time=0.8)

        # Decision nodes
        start = self._node("What do you need?", TEXT_MUTED, y=2.0)
        research = self._node("/research", BLUE, x=-3.5, y=0)
        ask = self._node("Ask/Execute", GREEN, x=0, y=0)
        plan = self._node("Plan Mode", ORANGE, x=3.5, y=0)

        # Labels
        lbl_r = Text("Understand deeply", font_size=14, color=BLUE).move_to([-2.5, 1.1, 0])
        lbl_a = Text("Build/fix now", font_size=14, color=GREEN).move_to([0, 1.1, 0])
        lbl_p = Text("Complex multi-step", font_size=14, color=ORANGE).move_to([2.5, 1.1, 0])

        # Outputs
        out_r = Text("→ Comprehensive report", font_size=13, color=TEXT_SECONDARY).next_to(research, DOWN, buff=0.3)
        out_a = Text("→ Working code", font_size=13, color=TEXT_SECONDARY).next_to(ask, DOWN, buff=0.3)
        out_p = Text("→ Structured plan.md", font_size=13, color=TEXT_SECONDARY).next_to(plan, DOWN, buff=0.3)

        self.play(FadeIn(start), run_time=0.5)

        # Draw arrows
        for target, label in [(research, lbl_r), (ask, lbl_a), (plan, lbl_p)]:
            arrow = Arrow(
                start.get_bottom(), target.get_top(),
                color=BORDER, stroke_width=1.5, buff=0.15,
            )
            self.play(Create(arrow), FadeIn(label), FadeIn(target), run_time=0.6)

        self.play(FadeIn(out_r), FadeIn(out_a), FadeIn(out_p), run_time=0.5)

        # Author footer
        author = Text(
            "Created by Shailesh | @shaileshmishra1",
            font_size=16, color=TEXT_MUTED,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(author), run_time=0.4)
        self.wait(2.5)

    def _node(self, text: str, color: str, x: float = 0, y: float = 0) -> VGroup:
        bg = RoundedRectangle(
            width=2.8, height=0.7, corner_radius=0.15,
            fill_color=CARD_BG, fill_opacity=1,
            stroke_color=color, stroke_width=1.5,
        )
        txt = Text(text, font_size=16, color=color, weight=BOLD)
        txt.move_to(bg)
        group = VGroup(bg, txt).move_to([x, y, 0])
        return group
