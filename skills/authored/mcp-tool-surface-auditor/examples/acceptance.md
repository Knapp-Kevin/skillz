# MCP tool-discovery evidence boundary and synthetic tests

The [synthetic 18-to-12 fixture](synthetic-18-versus-12.json)
declares 18 backend tools, 18 MCP-listed tools, and 12
host-visible tools under a fictional, matched context and source.
The expected report contains exactly six
`mcp_list_to_host_visible / NOT_VISIBLE_DOWNSTREAM`
findings, with `host_or_server_fault_assigned:false`.

All examples are **invented**: no connection, plugin, host
registration, tool call, or credentials were inspected.

### Planted negative controls

The test suite exercises incomplete pagination, missing stages,
duplicate tool names, changed schemas and output schemas, stable
schema reordering, context and revision mismatches, stale capture
windows, unsupported modern cache hints, legacy compatibility,
public-cache advisories, JSON duplicate keys and nonfinite values,
symlinked files, input limits, and CLI exit behavior.

A static PASS proves only that the offline comparison behaved as
defined for supplied JSON. It cannot establish host conformance,
actual MCP transport behavior, causal responsibility for missing
tools, privacy safety of a real connection, or recovered user
outcomes. A later host-backed trial needs authorized, redacted,
version-matched observations from all three layers, separately
verified receipts and before/after evidence.

Protocol background (optional online reading only):
https://blog.modelcontextprotocol.io/posts/2026-07-28/
