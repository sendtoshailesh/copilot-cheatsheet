---
name: copilot-feature-tracker
description: "Track GitHub Copilot feature releases from official sources (Changelog, Blog, Docs, VS Code Updates). Fetch, categorize, and compare against existing content to identify coverage gaps. USE FOR: monitor copilot features, find new releases, gap analysis, feature inventory updates, content freshness checks."
---

# Copilot Feature Tracker

Monitor GitHub Copilot feature releases and identify coverage gaps in existing content.

## Overview

This skill fetches new feature announcements from GitHub's official channels, categorizes them using a standardized taxonomy, and compares against a feature inventory to find what existing content is missing. It outputs structured data consumed by the `content-enhancer` agent.

## Source Priority

| Priority | Source | URL | Signal |
|----------|--------|-----|--------|
| 1 | GitHub Changelog | `https://github.blog/changelog/` | Definitive release announcements |
| 2 | GitHub Blog | `https://github.blog/category/product/copilot/` | Deep dives, GA announcements |
| 3 | GitHub Docs | `https://docs.github.com/en/copilot` | Feature documentation |
| 4 | VS Code Updates | `https://code.visualstudio.com/updates` | Editor integration features |
| 5 | Copilot CLI Releases | `https://github.com/github/copilot-cli/releases` | CLI version changelogs |

## Feature Taxonomy

Categorize every feature into exactly one primary category:

| Category | Slug | Covers |
|----------|------|--------|
| Modes | `modes` | Ask, Plan, Agent, Autopilot, Research, mode switching |
| CLI | `cli` | Terminal commands, flags, shell integration, completion |
| MCP | `mcp` | Model Context Protocol servers, registry, config, OAuth |
| Models | `models` | Model selection, auto routing, new model availability |
| Skills | `skills` | Built-in skills, custom skills, extensions, ACP |
| Governance | `governance` | Permissions, hooks, policies, audit, enterprise controls |
| Code Review | `code-review` | PR review, security scanning, auto-fix suggestions |
| Cloud Agent | `cloud-agent` | GitHub-hosted agent, issue assignment, cloud execution |
| IDE | `ide` | Editor integration, inline completions, chat panel |
| Instructions | `instructions` | Custom instructions, prompt files, agent definitions |
| Remote | `remote` | Remote sessions, cross-device, background delegation |

## Workflow

### 1. Fetch Recent Features

```
Input:  { since: "2026-05-01" }
Action: Fetch each source URL, extract entries dated after `since`
Output: Raw feature list with title, date, source URL, excerpt
```

For each source:
- **Changelog**: Look for entries containing "Copilot" in title or body
- **Blog**: Look for posts in the Copilot category
- **Docs**: Check the "What's new" section for recent additions
- **VS Code Updates**: Search for "Copilot" mentions in release notes

### 2. Categorize Features

For each raw feature:
1. Assign a primary `category` from the taxonomy above
2. Extract a short `name` (e.g., "Auto model selection")
3. Extract `version` if mentioned (e.g., "v1.0.32")
4. Rate `significance`: `major` (new capability), `minor` (enhancement), `patch` (fix/tweak)
5. Extract the best documentation URL

### 3. Compare Against Inventory

1. Read `feature-inventory.md` from the workspace root
2. For each new feature, check if it is already listed in the inventory
3. If listed: check if the `covered-in` column includes the target content file
4. If not listed: mark as a gap

### 4. Classify Gaps

For each gap, recommend an action:

| Significance | Recommendation |
|-------------|---------------|
| `major` + new category | New tip/slide needed |
| `major` + existing category | Update existing tip with prominent mention |
| `minor` + existing category | Add as bullet point to existing tip |
| `patch` | Log in inventory, no content change needed |

### 5. Output

```json
{
  "checked_date": "2026-05-06",
  "sources_checked": ["changelog", "blog", "docs", "vscode-updates"],
  "new_features": [
    {
      "name": "Auto model selection",
      "date": "2026-04-28",
      "version": "v1.0.32",
      "category": "models",
      "significance": "major",
      "source_url": "https://github.blog/changelog/...",
      "docs_url": "https://docs.github.com/en/copilot/...",
      "description": "Copilot automatically selects the best model for each task"
    }
  ],
  "gaps": [
    {
      "feature": "Auto model selection",
      "target_content": "How-To-GitHub-Copilot-Better-Than-99-Carousel.html",
      "action": "update_existing",
      "target_tip": "Tip 04 (Model Selection)",
      "suggested_text": "ADD bullet: `auto` mode — Copilot picks the best model per task"
    }
  ],
  "summary": {
    "total_new_features": 8,
    "gaps_found": 5,
    "new_tips_recommended": 1,
    "existing_updates_recommended": 3,
    "minor_additions": 1
  }
}
```

## Verified Source URLs (May 2026)

These URLs have been confirmed live and are the primary monitoring targets:

```
https://github.blog/changelog/
https://github.blog/category/product/copilot/
https://docs.github.com/en/copilot
https://docs.github.com/en/copilot/about-github-copilot/whats-new-in-copilot
https://code.visualstudio.com/updates
https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli
https://docs.github.com/en/copilot/concepts/mcp-management
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent
```

## Edge Cases

- **Feature spans multiple categories**: Use the primary category; note secondary in the description
- **Feature is a rename/rebrand**: Update the existing inventory entry name, do not create a duplicate
- **Source is unavailable**: Skip that source, note the failure, proceed with remaining sources
- **Feature is experimental/beta**: Include in inventory with a `(beta)` suffix; recommend content inclusion only after GA
- **Duplicate across sources**: Deduplicate by feature name; prefer Changelog as the canonical source
