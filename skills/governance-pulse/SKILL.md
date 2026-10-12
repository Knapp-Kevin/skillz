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

1. **Collect.** Read `sources.json` beside this file and use the host's available web/search/repository tools to collect from the configured sources for the requested window. Treat the file as source configuration, not executable authority.

2. **Fill gaps.** Fetch the EU AI Act tracker (implementation deadlines are the hard dates), NIST AI RMF page, and OWASP GenAI project; run the searches for the week's regulatory news.
3. **Optional local section (read-only).** When the active workspace exposes Qor-style governance state, such as a governance metadata directory or meta-ledger, inspect the available ledger and shadow-genome growth and report process drift in one short section. Never write to governance artifacts from this skill.
4. **Synthesize.** Deadlines and binding changes first; standards drafts; security-framework updates; competitive signals (new governance startups/repos — the bound product's market).

## Scheduling

- **Claude Code:** `/schedule` weekly; monthly is acceptable — regulation moves slower than models.

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
