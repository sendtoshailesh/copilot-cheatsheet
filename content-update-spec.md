# GitHub Copilot CLI Modes — Content Update Spec
# For updating: How-To-GitHub-Copilot-Better-Than-99-Carousel.html
# 
# Author: Shailesh | linkedin.com/in/shaileshmishra1
# Date: May 2026
# 
# This file documents new features to add to the existing "99%" content.
# Use with the content-creation pipeline: @content-pipeline

## Overview

The existing 14-slide carousel (last updated April 20, 2026) needs updating with
features released between April 20 - May 5, 2026 (v1.0.17 through v1.0.40).

## New Features to Add

### 🆕 Tip 13: /research — Deep Investigation Mode (v0.0.417 → v1.0.40)
- Most users just chat. Power users spawn multi-subagent research jobs
- Produces comprehensive Markdown reports with citations + Mermaid diagrams
- Export as HTML: /share html research
- Autonomous: never asks questions, makes assumptions, documents confidence
- Uses hardcoded model (not your /model selection)
- Read-only: never edits files
- Use BEFORE planning to gather intelligence
- Trigger: /research TOPIC
- Lifecycle phase: DISCOVERY

### 🆕 Tip 14: Plan → Autopilot Workflow (v0.0.387 → v1.0.40)
- Shift+Tab cycles: Ask/Execute → Plan → Autopilot
- Plan mode asks questions, creates structured plan.md
- --plan flag to start directly (v1.0.23)
- Approve plan → "Accept and build on autopilot"
- Autopilot: 5 message default limit (configurable with --max-autopilot-continues)
- Critic agent reviews plans using complementary model (v1.0.18, experimental)
- The "explore → plan → code → commit" workflow is officially recommended

### 🆕 Tip 15: Remote Sessions & /chronicle (v1.0.25 → v1.0.40)
- Start session in terminal, continue from GitHub.com or mobile
- --remote flag or /remote on
- /chronicle: standup summaries, tips, improvement suggestions from session history
- Now available to ALL users (no longer experimental)
- Background delegation with & prefix

## Updates to Existing Tips

### Update Tip 4 (Model Selection):
- ADD: `auto` model selection (v1.0.32) — Copilot picks best model for the task
- ADD: continueOnAutoMode config option

### Update Tip 6 (MCP Servers):
- ADD: `copilot mcp` command (v1.0.21) for CLI management
- ADD: MCP registry install with guided config (v1.0.25)
- ADD: client_credentials OAuth for headless/CI (v1.0.40)
- ADD: .mcp.json is now the sole config source (v1.0.12)

### Update Tip 7 (CLI):
- ADD: --plan, --autopilot, --mode flags (v1.0.23)
- ADD: /research command (v0.0.417)
- ADD: /rewind to any checkpoint (v1.0.13)
- ADD: /ask for quick off-record questions (v1.0.27)
- ADD: Location-based permission persistence (v1.0.37)
- ADD: Shell completion scripts: copilot completion bash|zsh|fish (v1.0.37)

### Update Tip 10 (Skills & Extensions):
- ADD: Built-in skills now ship with CLI (v1.0.17)
- ADD: Skills invokable as slash commands (v0.0.389)
- ADD: Skills available in ACP clients (v1.0.40)
- ADD: Custom agents can declare `skills` field (v1.0.22)

### Update Tip 11 (Governance):
- ADD: HTTP hook support (v1.0.35) — POST JSON to URLs
- ADD: preToolUse hooks can approve/deny programmatically
- ADD: Location-based permission persistence (v1.0.37)

## Version Bump
- Footer: "April 2026" → "May 2026"  
- Reference: "Based on the latest GitHub Changelog · May 2026"
- Note: v1.0.40 released May 1, 2026
- Slide count: 17 → 18 (cover + 16 tips + CTA)

## New Features Added (May 6 Update)

### ✅ Tip 16: Modes Mastery — Know When to Use Each Mode
- Added as Slide 17/18 (before CTA)
- Compares all 5 modes: Ask, Plan, Agent, Autopilot, Research
- Uses `.modes-grid` layout (3+2 cards) with per-mode color coding
- Key insight: Shift+Tab cycles Ask → Plan → Autopilot
- Addresses the gap: Agent mode was never compared with Ask and Plan modes
- Color: yellow (next in rotation after coral/Tip 15)
- All progress dots updated to 18 across all slides
- All slide counters updated to /18
- CTA updated: 15 → 16 tips, Tip 16 added to summary list

## Content-Creation Pipeline Command

To run this through the automated pipeline:
```
cd /Users/shaileshmishra/my-docs/my-proj/content-creation
@content-pipeline Update the "How to use GitHub Copilot better than 99%" content with new May 2026 features per the update spec
```

Or clone the repo first:
```
cd /Users/shaileshmishra/my-docs/my-proj
git clone https://github.com/sendtoshailesh/content-creation.git
cd content-creation
```
