---
name: mcp-pulse
description: >-
  Scan the Model Context Protocol ecosystem — spec and SDK releases,
  registry news, notable new servers, and MCP security advisories — and
  synthesize a digest. Use when the user asks "mcp pulse", "what's new
  with MCP", "new MCP servers worth using", "MCP spec changes", or wants
  protocol-level awareness for agent integration work.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: MCP Pulse
  emoji: "🔌"
  version: 1.0.0
---

# MCP Pulse

Topic pulse for the Model Context Protocol — the portability layer this repo's own contract depends on (external services go through MCP so connectors swap per platform). Spec drift here ripples into every agent surface: Claude Code, COREFORGE Synapse, Qortara adapters.

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/mcp-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Fetch the spec changelog (the hard source — protocol changes are the deprecation-equivalent); run the searches, especially the security one — MCP server vulnerabilities are an active research area.
3. **Synthesize.** Spec/SDK changes first with migration impact; security advisories second; then notable new servers (filter: does it unlock a capability we lack, or duplicate a connected one?); registry/ecosystem news.

## Scheduling

- **Claude Code:** `/schedule` weekly — pairs with github-pulse (which sweeps MCP repos broadly; this pulse goes narrow and deep — cross-reference, don't duplicate).

## Output Format

```
# MCP Pulse — [range]
## Spec & SDK changes (migration impact stated)
## Security advisories
## Notable new servers (capability-gap filter applied)
## Registry & ecosystem
## Notable patterns
## Sources
```

## Notes

- Server finds that merit adoption go through the intake registry (`registry/candidates.yaml`) with a permission tier — an MCP server is the highest-trust dependency class there is.
- Flag anything affecting COREFORGE's Synapse MCP integration or the vendored plugins' `.mcp.json` configs.
