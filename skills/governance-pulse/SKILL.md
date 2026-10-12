---
name: governance-pulse
description: >-
  Scan the AI governance landscape — EU AI Act milestones, NIST AI RMF
  updates, OWASP LLM/agentic security work, vendor transparency and policy
  announcements, and new governance/agent-security repos — and synthesize a
  digest. Use when the user asks "governance pulse", "AI regulation news",
  "what changed in AI governance", "EU AI Act update", or wants regulatory
  awareness feeding the operator's bound governance-product positioning.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Governance Pulse
  emoji: "⚖️"
  version: 1.1.0
---

# Governance Pulse

Topic pulse for AI governance: regulation, standards, security frameworks, and the emerging governance-tooling market. Directly feeds the operator's bound governance-product positioning (from operator profile or governance doc; generic market read when none is bound).

## Execution Flow

1. **Collect.** Read the bundled `sources.json` beside this SKILL.md as a source list. The authorized external host agent fetches or searches selected sources with capabilities it actually has, records source URLs and dates, and respects access and privacy boundaries. If browsing is unavailable, report the unverified gaps. This repository provides no runner, fetcher, scheduler, or automated collection process.

2. **Fill gaps.** Fetch the EU AI Act tracker (implementation deadlines are the hard dates), NIST AI RMF page, and OWASP GenAI project; run the searches for the week's regulatory news.
3. **Optional operator-workspace review (read-only).** Only when the user has authorized access to a separate governance-instrumented workspace, inspect available governance ledgers and locally recorded process-drift summaries there. These files are external workspace evidence, never required components of this skill package. If no such workspace is authorized and accessible, omit this section. Do not write to governance artifacts.
4. **Synthesize.** Deadlines and binding changes first; standards drafts; security-framework updates; competitive signals (new governance startups/repos — the bound product's market).

## Scheduling

- **Claude Code:** `/schedule` weekly; monthly is acceptable — regulation moves slower than models. Schedule only when the user explicitly authorizes it and the external host supports scheduling; this skill does not create a scheduled job.

## Output Format

```
# Governance Pulse — [range]
## Binding: deadlines & regulation in force
## Standards & frameworks (NIST, OWASP, ISO)
## Vendor policy & transparency moves
## Market: new governance/agent-security tooling
## Local process drift (when governance state is present; read-only)
## Notable patterns
## Sources
```

## Notes

- Distinguish in-force obligations from drafts and lobbying noise — label each item.
- Competitive findings here should become registry or BACKLOG entries, not action inside this skill.
