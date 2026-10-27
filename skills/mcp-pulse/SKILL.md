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
  version: 1.1.0
---

# MCP Pulse

Topic pulse for the Model Context Protocol — the portability layer this repo's own contract depends on (external services go through MCP so connectors swap per platform). Spec drift here ripples into every agent surface: Claude Code and the bound platform's MCP integration and adapters.

## Execution Flow

1. **Collect.** Use the authorized external host's retrieval capabilities:

   Read the bundled `sources.json` in this skill folder. Use authorized host browsing or connected search tools to inspect selected sources, keep source dates and URLs, and state which sources were unavailable. No repository-owned runner, script, or automatic collection process exists.

   The external host selects the available approved web/API capabilities; unavailable retrieval is reported as an evidence gap, not silently filled.

   **Resolve source-query windows.** `sources.json` is inert source configuration. For each `github_search[].q` containing `{SINCE}`, substitute a UTC `YYYY-MM-DD` date at the beginning of the requested report window before querying GitHub. If the user supplied no window, use the preceding seven days and label that default in the report. GitHub date-only `created:>` filters are approximate window boundaries, not proof of complete coverage. Never submit a literal `{SINCE}` placeholder, execute the source file, or imply an unexecuted search succeeded; record unavailable tools and incomplete results as evidence gaps.

2. **Fill gaps.** Fetch the spec changelog (the hard source — protocol changes are the deprecation-equivalent); run the searches, especially the security one — MCP server vulnerabilities are an active research area.
3. **Synthesize.** Spec/SDK changes first with migration impact; security advisories second; then notable new servers (filter: does it unlock a capability we lack, or duplicate a connected one?); registry/ecosystem news.

## Scheduling

- **Claude Code:** `/schedule` weekly — pairs with github-pulse (which sweeps MCP repos broadly; this pulse goes narrow and deep — cross-reference, don't duplicate). Scheduling is a separate host action requiring explicit user authorization; the repository never schedules runs.

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

- A server recommended for adoption needs a governed intake record and explicit permission-tier review. If the skillz intake registry is accessible in the authorized host, consult its current decisions; otherwise provide a proposed intake handoff rather than assuming the registry is bundled with this skill.
- Flag changes affecting the bound platform's MCP integration or the user's actual connector configuration, when the user has authorized access. Host-specific configuration is external to this skill package and may be unavailable.
