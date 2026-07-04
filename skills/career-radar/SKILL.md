---
name: career-radar
description: >-
  Run a periodic market scan for roles and rates matching the operator's
  bound professional profile — clustering postings by role type, noting
  demand signals, and comparing against the profile's positioning. Use
  when the user asks "run the career radar", "what's the market doing for
  my profile", "scan roles and rates", or wants a monthly read on demand
  for their skills.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Career Radar
  emoji: "🛰️"
  version: 1.1.0
---

# Career Radar

A periodic market scan that answers three questions for the operator's bound professional profile: what roles are being hired for, what they pay, and whether the market is moving toward or away from the profile's positioning. It builds on the career-ops/job-ranger work in this ecosystem — radar is the recurring wide scan; job-ranger handles evaluating specific openings. The skill observes only: it never applies to roles or contacts anyone.

## Execution Flow

1. **Bind the profile.** Read the profile from the operator's career notes, operator profile, or host memory — the bound source is authoritative over remembered assumptions. If none exists, elicit (role focus, seniority, remote/location, core terms) and offer to persist the answers as career notes for future runs. Always say which profile the scan ran against.
2. **Scan postings:** web-search 4–6 query variants around the profile's core terms (e.g., for a platform-engineering profile: "AI platform engineer remote", "agent infrastructure architect", "LLM platform engineering jobs") across job boards and company career pages surfaced in results. Collect titles, seniority, comp when listed, and posting dates.
3. **Scan rates:** web-search recent salary/rate surveys and comp threads for the role cluster. Prefer sources dated within 12 months; note the date on every figure.
4. **Cluster** the postings by role type (e.g. platform engineering, agent infrastructure, AI governance/safety, solutions architecture) with a rate range per cluster.
5. **Extract demand signals:** keywords repeating across postings, newly appearing titles, requirements shifting (e.g. eval harnesses, MCP, agent orchestration), and clusters growing or shrinking versus the previous scan if one exists in notes.
6. **Compare against positioning:** where the profile is ahead of demand, where it lags, and 2–3 concrete positioning suggestions (terms to adopt, artifacts to surface).
7. **Present** in the Output Format below, citing sources for every rate figure.

## Scheduling

- **Claude Code:** use `/schedule` to create a monthly routine whose instruction is "Run the career-radar skill against the bound profile and post the scan."
- **Other agent platforms:** a monthly scheduled automation with the same instruction.

## Output Format

```
# Career Radar — [Month Year] — profile: [profile]

## Role Clusters
| Cluster | Openings seen | Rate range | Sources |
|---------|---------------|------------|---------|
| [role type] | [n, over period] | [$X–$Y / $Z/hr] | [survey/board + date] |

## Demand Signals
- [Repeat keyword / new title / shifting requirement] — [evidence]

## Positioning
- Ahead: [where the profile already matches rising demand]
- Gap: [what postings ask for that the profile undersells]
- Suggestions: [2–3 concrete positioning moves]
```

## Notes

- Read-only: this skill scans and reports. It never applies to roles, submits forms, or contacts recruiters or companies.
- Rate figures are only as good as their sources — always cite and date them; if sources disagree, show the spread rather than averaging it away.
- Keep each scan's output in notes so the next run can report cluster growth and signal changes over time.
