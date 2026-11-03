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
  version: 1.1.1
---

# Governance Pulse

Topic pulse for AI governance: regulation, standards, security frameworks, and the emerging governance-tooling market. Directly feeds the operator's bound governance-product positioning (from operator profile or governance doc; generic market read when none is bound).

## Execution Flow

1. **Collect (external host only).** Read the `sources.json` file beside this skill. For the requested time window (default: last 30 days), use the host's normal browser, search, or connected read-only tools to inspect the listed public pages, GitHub repositories and searches. Substitute the window start date for `{SINCE}` in search templates. Treat Reddit and other community discussions as leads to verify, not authoritative evidence. Record source links and publication dates; report inaccessible sources as gaps, never as checked. The repository supplies references only: **there is no skillz runner, script, crawler, or background job to invoke.** Do not upload private context or credentials to these sources.

2. **Fill gaps.** Fetch the EU AI Act tracker (implementation deadlines are the hard dates), NIST AI RMF page, and OWASP GenAI project; run the searches for the week's regulatory news.
3. **Optional local section (read-only).** When run inside a workspace carrying Qor-style governance state (a `.qor/` directory or `docs/META_LEDGER.md`), skim `docs/META_LEDGER.md` and shadow-genome growth across `.qor/`-instrumented repos and report process drift in one short section. Never write to governance artifacts from this skill.
4. **Synthesize.** Deadlines and binding changes first; standards drafts; security-framework updates; competitive signals (new governance startups/repos — the bound product's market).

## Scheduling

- **Optional cadence:** Weekly or monthly, only if the user explicitly authorizes a recurring task. Scheduling belongs to the external host; this repository schedules nothing.

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
