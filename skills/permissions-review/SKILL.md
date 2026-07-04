---
name: permissions-review
description: >-
  Periodic audit of everything agents can touch — connected MCP servers and
  their tool surfaces, permission allowlists, hooks, and reachable
  credentials — producing a risk-ranked report with recommended tightenings.
  Use when the user asks "review agent permissions", "what can my agents
  touch", "audit the allowlists", or on the monthly security cadence.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Permissions Review
  emoji: "🔐"
  version: 1.0.0
---

# Permissions Review

A recurring inventory of the agent fleet's blast radius: every MCP server, allowlist entry, hook, and reachable credential, each judged against one question — when was this last needed? Permissions accumulate; they never expire on their own. This skill reports and recommends only; it never revokes, edits settings, or rotates credentials itself.

## Execution Flow

1. **Inventory connected MCP servers.** From the active MCP configuration, list each server and enumerate its tool surface. Classify each server by the permission tiers in `docs/evaluation-framework.md`, using its highest-impact tool.
2. **Review permission settings.** Read Claude Code `settings.json` and `settings.local.json` allowlists (Bash patterns, tool permissions) and configured hooks. Flag broad patterns (wildcards, whole-command allowances) and hooks that execute with write or network access.
3. **Map reachable credentials.** Identify credentials agents can reach: environment variables, credential files in readable paths, tokens embedded in MCP server configs. Record what each credential unlocks, not its value.
4. **Ask "when was this last needed?" per item.** Check transcripts, logs, or git history where available; where no evidence exists, mark last-use unknown — unknown is a finding, not a pass.
5. **Rank findings by risk.** Highest first: unused high-tier access (an idle `destructive` or `identity` capability), then broad allowlist patterns, then credentials with no identified consumer, then stale but low-tier items.
6. **Recommend tightenings.** For each finding, propose the specific change: the allowlist line to narrow, the server to disconnect, the credential to scope or remove. Never apply any of them — this is a report for a human to act on.

## Scheduling

- **Claude Code:** `/schedule` a monthly run — "Run the permissions-review skill and post the report." Run ad hoc after connecting any new MCP server or adding any allowlist entry.
- **Other agent platforms:** a monthly scheduled automation with the same one-line instruction.

## Output Format

```
# Permissions Review — <date>

## Inventory
| Item | Type | Tier | Last needed |
|------|------|------|-------------|
| <name> | <MCP server / allowlist / hook / credential> | <tier> | <date / unknown> |

## Findings (risk-ranked)
1. <finding> — risk: <why it matters> — evidence: <source>

## Recommended tightenings
- <exact change to make, e.g. narrow "Bash(*)" to "Bash(git *)">
```

## Notes

- Strictly read-only: this skill never edits settings files, disconnects servers, or touches credentials — report and recommend only.
- Never record credential values in the report; record what each credential grants access to.
- "Last needed: unknown" items default to tightening candidates; the burden of proof is on keeping access, not removing it.
- Pair with mcp-vetting: vetting gates what gets connected, this review catches what should no longer be.
