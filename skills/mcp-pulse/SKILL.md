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
  version: 1.1.1
---

# MCP Pulse

Topic pulse for the Model Context Protocol — the portability layer this repo's own contract depends on (external services go through MCP so connectors swap per platform). Spec drift here ripples into every agent surface: Claude Code and the bound platform's MCP integration and adapters.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check the listed public pages, upstream repos and queries. Substitute the window start date for `{SINCE}` search templates. Cite URLs and publication dates; treat community posts as unverified leads, and report inaccessible or rate-limited sources as gaps. Never expose user context, credentials, secrets or private project text through search queries or other outbound requests. If the host cannot fetch current sources, report an evidence-limited result, not fabricated freshness. **There is no skillz runner, crawler, script, scheduler or background worker.**

2. **Fill gaps.** Fetch the spec changelog (the hard source — protocol changes are the deprecation-equivalent); run the searches, especially the security one — MCP server vulnerabilities are an active research area.
3. **Synthesize.** Spec/SDK changes first with migration impact; security advisories second; then notable new servers (filter: does it unlock a capability we lack, or duplicate a connected one?); registry/ecosystem news.

## Scheduling

- **Optional cadence:** Weekly, only when the user has explicitly authorized this recurring digest. Any scheduling belongs to the external host. One-off research does not authorize repeated checks or outbound notifications.

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
- Flag anything affecting the bound platform's MCP integration or locally configured MCP servers (`.mcp.json` and equivalents).
