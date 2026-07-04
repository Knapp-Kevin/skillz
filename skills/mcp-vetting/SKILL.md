---
name: mcp-vetting
description: >-
  Security review of an MCP server before it is connected: provenance, tool
  surface, data flow, injection exposure, and version pinning, ending in a
  permission-tier verdict and a recommended registry entry. Use when the user
  asks "vet this MCP server", "is this MCP safe to connect", "review this MCP
  before I add it", or before any new server enters the config.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: MCP Vetting
  emoji: "🛡️"
  version: 1.1.0
---

# MCP Vetting

Static security review of an MCP server before it earns a connection. An MCP server is the highest-trust dependency class we adopt — it sits inside the agent's tool loop with live credentials — so vetting happens on documentation and source, never by running the server. Output is a verdict with a permission tier and a recommended registry entry; connecting remains a separate human decision.

## Execution Flow

1. **Provenance.** Identify the maintainer and their organization, the repository's history and activity authenticity, license, and whether the server appears in an official registry listing. Unknown or pseudonymous maintainers cap the trust score per the evaluation framework's source-trust criterion.
2. **Tool-surface enumeration.** From the server's source or manifest, list every tool it exposes with its declared parameters. Classify each tool by the permission tiers in `docs/evaluation-framework.md` (`read-only` through `destructive`). The server's overall tier is its highest-impact tool.
3. **Data-flow review.** Determine what data leaves the machine and to which endpoints, where credentials live (env vars, config files, keychain) and how the server reads them, and what the server logs locally or remotely.
4. **Injection exposure.** Check whether tool output feeds model context unsanitized — fetched web content, third-party API responses, or file contents that an attacker could seed with instructions. Note any sanitization or provenance-marking the server performs.
5. **Version pinning and update channel.** Confirm a pinnable version exists (tag, hash, lockfile), identify the update mechanism, and flag auto-update behavior or install-time script execution.
6. Deliver the verdict in the Output Format below: connect / connect-with-restrictions / do-not-connect, the assigned permission tier, and a recommended `registry/candidates.yaml` entry (status, tier, rationale) for a human to record.

## Output Format

```
# MCP Vetting: <server-name>

Provenance: <maintainer / org / registry listing> — <trust assessment>

## Tool surface
| Tool | Purpose | Permission tier |
|------|---------|-----------------|

## Data flow
Outbound: <endpoints> | Credentials: <where/how> | Logging: <what/where>

## Injection exposure
<unsanitized paths found, or "none identified">

## Versioning
Pin: <tag/hash available?> | Update channel: <mechanism>

## Verdict
<connect | connect-with-restrictions | do-not-connect> at tier <tier>

## Recommended registry entry
status: <adopted | sandbox | quarantined | rejected>
permission_tier: <tier>
rationale: <one sentence>
```

## Negative rules

These override the checklist format. A vetting report that leaks what it vets has failed at its own job.

- **Never reproduce secret-shaped strings** from server configs, env examples, or docs (API keys, tokens, connection strings) — type + short prefix only; a credential visible in a candidate's repo is itself a security finding with a rotation recommendation.
- **Never fabricate a security posture.** If a dimension could not be checked (unreadable code, no advisories database, opaque distribution), the verdict line says `not established` for that dimension — an unchecked box is never a passed box.
- **Unknown stays unknown.** Missing evidence lowers the confidence stated with the verdict; it is never filled with assumptions about what "a typical server" does.

## Notes

- Never connect, install, or execute the server during vetting — static review of source and documentation only. A server that cannot be reviewed statically fails vetting by default.
- Any single tool at `identity`, `cost`, or `destructive` tier means the whole server carries that tier; tiers do not average.
- This skill recommends registry entries; it never writes to `registry/candidates.yaml` or the MCP config itself.
- Re-vet on major version changes: a vetted server is vetted at a pinned version, not forever.
