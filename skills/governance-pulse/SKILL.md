---
name: governance-pulse
description: >-
  Scan the AI governance landscape — EU AI Act milestones, NIST AI RMF
  updates, OWASP LLM/agentic security work, vendor transparency and policy
  announcements, and new governance/agent-security repos — and synthesize a
  digest. Use when the user asks "governance pulse", "AI regulation news",
  "what changed in AI governance", "EU AI Act update", or wants regulatory
  awareness feeding Qortara/FailSafe/Qor-logic positioning.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Governance Pulse
  emoji: "⚖️"
  version: 1.0.0
---

# Governance Pulse

Topic pulse for AI governance: regulation, standards, security frameworks, and the emerging governance-tooling market. Directly feeds MythologIQ positioning (Qortara, FailSafe, Qor-logic, agent-governance-toolkit).

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/governance-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Fetch the EU AI Act tracker (implementation deadlines are the hard dates), NIST AI RMF page, and OWASP GenAI project; run the searches for the week's regulatory news.
3. **Optional local section (read-only).** When run inside the MythologIQ workspace, skim `docs/META_LEDGER.md` and shadow-genome growth across `.qor/`-instrumented repos and report process drift in one short section. Never write to governance artifacts from this skill.
4. **Synthesize.** Deadlines and binding changes first; standards drafts; security-framework updates; competitive signals (new governance startups/repos — these are Qortara's market).

## Scheduling

- **Claude Code:** `/schedule` weekly; monthly is acceptable — regulation moves slower than models.

## Output Format

```
# Governance Pulse — [range]
## Binding: deadlines & regulation in force
## Standards & frameworks (NIST, OWASP, ISO)
## Vendor policy & transparency moves
## Market: new governance/agent-security tooling
## Local process drift (when in MythologIQ workspace; read-only)
## Notable patterns
## Sources
```

## Notes

- Distinguish in-force obligations from drafts and lobbying noise — label each item.
- Competitive findings here should become registry or BACKLOG entries, not action inside this skill.
