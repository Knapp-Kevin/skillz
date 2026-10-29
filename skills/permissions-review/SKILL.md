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

An on-demand inventory of the agent fleet's blast radius: every MCP server, allowlist entry, hook, and reachable credential, each judged against one question — when was this last needed? Permissions accumulate; they never expire on their own. This skill reports and recommends only; it never revokes, edits settings, or rotates credentials itself.

## Execution Flow

1. **Bind authorized scope first.** Identify which agent/workspace, configuration, logs and connected tools the operator has authorized this review to inspect. Do not broaden private-data access merely because a tool can reach it. Inventory connected MCP servers within that scope and enumerate their tool surfaces. Classify each server by the permission tiers in `docs/evaluation-framework.md`, using its highest-impact tool.
2. **Review permission settings.** When authorized and available, inspect the host's applicable permission settings and hooks; Claude Code `settings.json` and `settings.local.json` are examples, not mandatory dependencies. Flag broad patterns (wildcards, whole-command allowances) and hooks that execute with write or network access.
3. **Map reachable credentials without retrieving values.** Use authorized configuration metadata and documented credential references to identify which credential classes an agent may reach. Do not open secret stores, read token values, print credential-bearing URLs, or expand access to inspect a secret. Record what each credential class unlocks, never its value.
4. **Ask "when was this last needed?" per item.** Check only authorized transcripts, logs, or history where available; redact personal and credential-bearing content; where no evidence exists, mark last-use unknown — unknown is a finding, not a pass.
5. **Rank findings by risk.** Highest first: unused high-tier access (an idle `destructive` or `identity` capability), then broad allowlist patterns, then credentials with no identified consumer, then stale but low-tier items.
6. **Recommend tightenings.** For each finding, propose the specific change: the allowlist line to narrow, the server to disconnect, the credential to scope or remove. Never apply any of them — this is a report for a human to act on.

## Optional host-managed scheduling

- Default to a one-time scoped report. A periodic audit is a proposal, not authorization to create a schedule, repeatedly read private configurations, or post results.
- A recurring review may be created only by an authorized external host after separate explicit approval of cadence/timezone, exact future sources and access scope, delivery destination/recipients, retention, cost, and pause/revocation controls. Never persist credentials or include their values in scheduled output.
- If no approved host scheduler or future-access grant exists, provide a reusable manual review checklist and mark recurrence `not configured`.

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

- Strictly read-only for each approved review: never edit settings, disconnect servers, or retrieve credential values. Access to private config/log metadata requires an appropriate scope grant, and recurrence requires a separate authorization.
- Never record credential values in the report; record what each credential grants access to.
- "Last needed: unknown" items default to tightening candidates; the burden of proof is on keeping access, not removing it.
- Pair with mcp-vetting: vetting gates what gets connected, this review catches what should no longer be.
