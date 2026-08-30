---
name: claude-pulse
description: >-
  Review the latest Claude updates from Anthropic's official release notes,
  blog posts, announcements, and relevant community discussion. Use when the
  user asks what's new with Claude, wants a Claude update digest, or needs a
  sourced read on recent Claude models, features, deprecations, bugs, and
  community reception.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Claude Pulse
  emoji: "📡"
  version: 1.2.0
---

# Claude Pulse

Produce a current, source-grounded digest of Claude developments using the external host agent's available browsing and retrieval capabilities.

## Repository boundary

This skill is passive knowledge and procedure only. It contains no fetcher, scheduler, executable helper, background process, or repository-owned monitoring mechanism. The external host agent performs any browsing, searching, filtering, and synthesis when the skill is intentionally invoked.

## Source hierarchy

Use four evidence layers and keep their authority distinct:

1. **Official Anthropic sources**
   - Claude Code CHANGELOG
   - Claude Code GitHub Releases
   - Claude Developer Platform release notes
   - Anthropic/Claude blog and announcements

2. **Model and feature announcements**
   - New model releases
   - Feature launches
   - API, pricing, capability, or availability changes
   - Deprecation and EOL notices

3. **Community commentary**
   - r/ClaudeAI
   - r/coding when Claude-relevant
   - r/LocalLLaMA when Claude-relevant
   - Other credible practitioner discussion when directly useful

4. **Synthesis**
   - What changed during the requested window
   - What materially affects current workflows
   - What the community is reporting
   - Notable bugs, workarounds, disagreements, and emerging patterns

Official sources establish product facts. Community commentary is reception and operational signal, not canonical truth.

## Host-agent procedure

1. Resolve the requested date window. If none is supplied, use the most recent seven days.
2. Check official Anthropic sources first and record publication or release dates.
3. Prioritize deprecations, EOL dates, breaking changes, pricing changes, and workflow-impacting changes before lower-impact news.
4. Search relevant community discussion for the same window.
5. Separate confirmed product facts from community claims, anecdotes, and speculation.
6. Cross-check material claims against primary sources when practical.
7. Note missing, inaccessible, or conflicting evidence rather than filling gaps by inference.
8. Synthesize the result into the output format below with links or citations supported by the host environment.

## Community-review guidance

When reviewing discussion:

- Prefer threads directly tied to a current release, feature, bug, or workflow.
- Distinguish repeated reports from one-off anecdotes.
- Treat scores, upvotes, and thread volume as attention signals only.
- Do not infer product quality from popularity.
- Surface useful workarounds, but label unofficial techniques clearly.
- Flag unresolved disagreements rather than manufacturing consensus.

Useful search patterns include:

- `Claude site:reddit.com/r/ClaudeAI`
- `Claude Code site:reddit.com/r/coding`
- `Claude site:reddit.com/r/LocalLLaMA`

Filter results to the requested time window whenever the host tools support it.

## Output format

```text
# Claude Pulse — [Date Range]

## Important Changes
- [Deprecation, EOL, breaking, pricing, or workflow-impacting change]

## Official Releases
### Claude Code
- [Release/date] — [key changes]

### Models & Platform
- [Announcement/date] — [key changes]

## Community Commentary
- [Thread/topic] — [what practitioners are reporting]

## Notable Patterns
- [Recurring theme, workaround, disagreement, or emerging workflow]

## Evidence Notes
- [Conflicts, inaccessible sources, unresolved claims, or confidence limits]

## Sources
- [Primary and community sources used]
```

## Canonical source locations

| Source | Location | Role |
|---|---|---|
| Claude Code CHANGELOG | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Primary |
| Claude Code Releases | https://github.com/anthropics/claude-code/releases | Primary |
| Claude Developer Platform release notes | https://platform.claude.com/docs/en/release-notes/overview.md | Primary |
| Anthropic / Claude blog | https://claude.com/blog | Primary |
| r/ClaudeAI | https://www.reddit.com/r/ClaudeAI/ | Community signal |
| r/coding | https://www.reddit.com/r/coding/ | Community signal |
| r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/ | Community signal |

## Authority and side effects

This skill is read-only. It may direct the host agent to retrieve public information and synthesize it, but it does not authorize posting, scheduling, repository mutation, account changes, or any other external side effect.

## Freshness rules

- Current product facts require current sources.
- Prefer primary sources for dates, version numbers, pricing, deprecations, and availability.
- State the evidence date when a claim may become stale quickly.
- Do not carry forward an old claim merely because it appeared in a prior digest.
