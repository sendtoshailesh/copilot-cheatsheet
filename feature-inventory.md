# Feature Inventory — GitHub Copilot Content

Last checked: 2026-05-06
Last updated: 2026-05-06

## Taxonomy

| Category | Slug |
|----------|------|
| Modes | `modes` |
| CLI | `cli` |
| MCP | `mcp` |
| Models | `models` |
| Skills | `skills` |
| Governance | `governance` |
| Code Review | `code-review` |
| Cloud Agent | `cloud-agent` |
| IDE | `ide` |
| Instructions | `instructions` |
| Remote | `remote` |

## Feature Registry

| Feature | Category | Version | Date | Covered In |
|---------|----------|---------|------|-----------|
| Agent Mode — autonomous multi-file editing | `modes` | GA | 2025 | Carousel Tip 01 |
| Cloud Agent — assign issues to Copilot | `cloud-agent` | GA | 2025 | Carousel Tip 02 |
| Custom Instructions — `.github/copilot-instructions.md` | `instructions` | GA | 2025 | Carousel Tip 03 |
| Model Selection — choose specific models | `models` | GA | 2025 | Carousel Tip 04 |
| `auto` model routing — Copilot picks best model | `models` | v1.0.32 | 2026-04 | Carousel Tip 04 |
| `continueOnAutoMode` config | `models` | v1.0.32 | 2026-04 | Carousel Tip 04 |
| Prompt Files — `.github/prompts/*.prompt.md` | `instructions` | GA | 2025 | Carousel Tip 05 |
| MCP Servers — Model Context Protocol | `mcp` | GA | 2025 | Carousel Tip 06 |
| `copilot mcp` CLI command | `mcp` | v1.0.21 | 2026-04 | Carousel Tip 06 |
| MCP registry install with guided config | `mcp` | v1.0.25 | 2026-04 | Carousel Tip 06 |
| `client_credentials` OAuth for MCP (headless/CI) | `mcp` | v1.0.40 | 2026-05 | Carousel Tip 06 |
| `.mcp.json` as sole config source | `mcp` | v1.0.12 | 2026-03 | Carousel Tip 06 |
| Copilot CLI — terminal AI | `cli` | GA | 2025 | Carousel Tip 07 |
| `--plan` flag | `cli` | v1.0.23 | 2026-04 | Carousel Tip 07, Tip 14 |
| `--autopilot` flag | `cli` | v1.0.23 | 2026-04 | Carousel Tip 07, Tip 14 |
| `--mode` flag | `cli` | v1.0.23 | 2026-04 | Carousel Tip 07 |
| `/research` command | `cli` | v0.0.417 | 2026-03 | Carousel Tip 07, Tip 13 |
| `/rewind` to any checkpoint | `cli` | v1.0.13 | 2026-03 | Carousel Tip 07 |
| `/ask` for off-record questions | `cli` | v1.0.27 | 2026-04 | Carousel Tip 07, Tip 16 |
| Location-based permission persistence | `governance` | v1.0.37 | 2026-04 | Carousel Tip 07, Tip 11 |
| Shell completion scripts | `cli` | v1.0.37 | 2026-04 | Carousel Tip 07 |
| @workspace & Slash Commands | `ide` | GA | 2025 | Carousel Tip 08 |
| PR Code Review — auto-review | `code-review` | GA | 2025 | Carousel Tip 09 |
| Skills & Extensions | `skills` | GA | 2025 | Carousel Tip 10 |
| Built-in skills ship with CLI | `skills` | v1.0.17 | 2026-04 | Carousel Tip 10 |
| Skills invokable as slash commands | `skills` | v0.0.389 | 2026-03 | Carousel Tip 10 |
| Skills available in ACP clients | `skills` | v1.0.40 | 2026-05 | Carousel Tip 10 |
| Custom agents can declare `skills` field | `skills` | v1.0.22 | 2026-04 | Carousel Tip 10 |
| Enterprise Governance — policies & hooks | `governance` | GA | 2025 | Carousel Tip 11 |
| HTTP hook support | `governance` | v1.0.35 | 2026-04 | Carousel Tip 11 |
| `preToolUse` hooks for programmatic approval | `governance` | v1.0.35 | 2026-04 | Carousel Tip 11 |
| Repo = Brain — structure guides Copilot | `instructions` | — | — | Carousel Tip 12 |
| /research — deep investigation mode | `modes` | v0.0.417 | 2026-03 | Carousel Tip 13 |
| Multi-subagent research with Markdown+Mermaid | `modes` | v0.0.417 | 2026-03 | Carousel Tip 13 |
| `/share html research` export | `modes` | v1.0.40 | 2026-05 | Carousel Tip 13 |
| Plan mode — structured plan.md with critic agent | `modes` | v0.0.387 | 2026-03 | Carousel Tip 14 |
| Autopilot — post-approval autonomous execution | `modes` | v1.0.23 | 2026-04 | Carousel Tip 14 |
| Shift+Tab mode cycling (Ask → Plan → Autopilot) | `modes` | v1.0.23 | 2026-04 | Carousel Tip 14, Tip 16 |
| Critic agent for plan review | `modes` | v1.0.18 | 2026-04 | Carousel Tip 14, Tip 16 |
| `--max-autopilot-continues` config | `modes` | v1.0.23 | 2026-04 | Carousel Tip 14 |
| Remote Sessions — cross-device continuity | `remote` | v1.0.25 | 2026-04 | Carousel Tip 15 |
| `--remote` flag and `/remote on` | `remote` | v1.0.25 | 2026-04 | Carousel Tip 15 |
| `/chronicle` — standup summaries | `remote` | v1.0.25 | 2026-04 | Carousel Tip 15 |
| Background delegation with `&` prefix | `remote` | v1.0.25 | 2026-04 | Carousel Tip 15 |
| Modes Mastery — 5-mode comparison strategy | `modes` | — | 2026-05 | Carousel Tip 16 |
| Ask mode — quick off-record Q&A | `modes` | v1.0.27 | 2026-04 | Carousel Tip 16 |
| GPT-5.5 GA | `models` | — | 2026-04-24 | Carousel Tip 04 |
| Usage-based billing (June 1) | `models` | — | 2026-05-06 | Carousel Tip 04 |
| Browser tab sharing with agents | `ide` | VS Code 1.119 | 2026-05-06 | Carousel Tip 01 |
| OpenTelemetry tracing for agent sessions | `governance` | VS Code 1.119 | 2026-05-06 | Carousel Tip 01, Tip 11 |
| Inline agent mode for JetBrains (preview) | `ide` | — | 2026-04-24 | Carousel Tip 01 |
| Cloud agent merge conflicts in 3 clicks | `cloud-agent` | — | 2026-04-13 | Carousel Tip 02 |
| Cloud agent 20% faster with Actions custom images | `cloud-agent` | — | 2026-04-27 | Carousel Tip 02 |
| View/manage agent sessions from Issues & Projects | `cloud-agent` | — | 2026-04-23 | Carousel Tip 02 |
| Secret scanning via GitHub MCP Server GA | `mcp` | — | 2026-05-05 | Carousel Tip 06 |
| Dependency scanning via MCP Server (preview) | `mcp` | — | 2026-05-05 | Carousel Tip 06 |
| Manage agent skills with GitHub CLI | `skills` | — | 2026-04-16 | Carousel Tip 10 |
| Code review consuming Actions minutes (June 1) | `code-review` | — | 2026-04-27 | Carousel Tip 09 |
| Agent sandbox allowNetwork mode | `governance` | VS Code 1.119 | 2026-05-06 | Carousel Tip 11 |
| Data residency US+EU with FedRAMP-authorized models | `governance` | — | 2026-04-13 | Carousel Tip 11 |
| MCP registry-based allowlists per org | `governance` | — | 2026-04-16 | Carousel Tip 11 |

## Content Files Tracked

| Content | File | Tips | Last Updated |
|---------|------|------|-------------|
| "How to use GitHub Copilot better than 99%" Carousel | `How-To-GitHub-Copilot-Better-Than-99-Carousel.html` | 16 (18 slides) | 2026-05-06 |
