---
name: content-researcher
description: 'Research and compile verified URLs, resources, and reference material from GitHub Docs, GitHub Blog, GitHub Changelog, and other official sources for content creation. USE FOR: find GitHub docs URLs, research copilot features, compile resource links, verify documentation URLs, gather source material for content.'
---

# Content Researcher

Research, verify, and compile official GitHub documentation URLs for carousel and content creation.

## Overview

This skill finds and validates live URLs from GitHub's documentation ecosystem. It outputs structured resource data consumed by the `linkedin-carousel-generator` skill.

## URL Source Priority

1. **GitHub Docs**: `docs.github.com/en/copilot/...`
2. **GitHub Blog**: `github.blog/...`
3. **GitHub Changelog**: `github.com/changelog/...`
4. **GitHub Features**: `github.com/features/copilot`
5. **GitHub Repos**: `github.com/github/...`

## Verified URLs (April 2026)

```
https://docs.github.com/en/copilot
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-a-pr
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/add-skills
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings
https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review
https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli
https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli
https://docs.github.com/en/copilot/concepts/billing/copilot-requests
https://docs.github.com/en/copilot/concepts/mcp-management
https://github.com/github/github-mcp-server
https://github.com/features/copilot
https://github.blog/category/product/copilot/
```

## Output Format

```json
[
  {
    "topic": "Agent Mode",
    "urls": [
      { "title": "Copilot Docs", "url": "https://...", "verified": true }
    ]
  }
]
```

## Workflow

1. Receive topic list from orchestrator
2. For each topic, search official docs
3. Fetch each URL to confirm HTTP 200
4. Output structured resource map
5. Flag any 404s or moved pages
