---
name: smallbiz-ops
description: >-
  Run the monthly upkeep sweep for the family business web presences — Hill
  House Transport, Neat & Clean, and Chesapeake Moms Club — checking content
  freshness, site uptime, listings drift across search results, and seasonal
  to-dos. Use when the user asks "run the business site check", "smallbiz
  ops sweep", "are the family sites healthy", or wants the monthly web
  presence review.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Small Biz Ops
  emoji: "🏪"
  version: 1.0.0
---

# Small Biz Ops

A monthly upkeep cadence for the family business web presences: Hill House Transport, Neat & Clean, and Chesapeake Moms Club. Each sweep answers four questions per site — is it up, is the content current, do the listings agree with the site, and what does the coming season require — and ends with a prioritized to-do list. The skill proposes edits; it never publishes anything.

## Execution Flow

1. **Uptime spot-check:** fetch each site's homepage with the web fetch tool. Record reachable/unreachable, obvious error pages, and anything visibly broken (missing images, placeholder text).
2. **Content freshness:** on each site, look for dated content — copyright year, "last updated" stamps, seasonal offers, event announcements. Flag anything expired (a spring promo in July) or stale (copyright two years back).
3. **Listings drift:** web-search each business name (plus locality where needed) and compare hours, phone number, and address across the top results — Google listing, directories, social pages — against what the site itself says. Every mismatch is a finding.
4. **Seasonal to-dos:** from the current date, derive what the next 4–6 weeks require — holiday hours, seasonal service messaging, annual renewals. July example: post any Independence Day closure; start drafting back-to-school messaging for Chesapeake Moms Club.
5. **Present** in the Output Format below. Every proposed edit is copy or a change description for the operator to apply — this skill has no publish step.

## Scheduling

- **Claude Code:** use `/schedule` to create a monthly routine (e.g. first Monday) whose instruction is "Run the smallbiz-ops skill and post the report."
- **Other agent platforms:** a monthly scheduled automation with the same instruction.

## Output Format

```
# Small Biz Ops — [Month Year]

## Site Status
| Site | Up? | Freshness | Listings | Notes |
|------|-----|-----------|----------|-------|
| Hill House Transport | [OK/DOWN] | [current / stale: what] | [consistent / drift: what] | [one line] |
| Neat & Clean | ... | ... | ... | ... |
| Chesapeake Moms Club | ... | ... | ... | ... |

## To-Dos (priority order)
1. [Site] — [action] — [why now] — [proposed copy or change, ready to apply]

## Seasonal Watch
- [Upcoming date/season] — [what to prepare]
```

## Notes

- Read-only: this skill checks and proposes. It never edits sites, updates listings, posts to social accounts, or contacts anyone; proposed copy is handed to the operator to publish.
- A site that fails to fetch once may be a transient blip — retry before reporting DOWN, and say which it was.
- Listings drift is the highest-value catch: wrong hours or phone in search results loses customers silently. Rank those to-dos first.
