---
name: skills-pulse
description: >-
  Scan the agent-skills ecosystem for new and updated skills across the
  vendored official and community-vetted reference sources plus tracked
  marketplaces, then propose intake candidates for the registry. Use when
  the user asks "skills pulse", "any new agent skills", "scan the skill
  watchlist", "update the skill registry", or on a weekly intake schedule.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skills Pulse
  emoji: "🧭"
  version: 1.2.0
---

# Skills Pulse

Weekly intake scan of the agent-skills ecosystem. Finds what is new, filters it against what we already have, and proposes registry candidates. It does **not** install anything.

## What This Does

1. **Reference-source scan** (script): commits and releases on vendored official, community-vetted, and tracked skill repos, flagging pinned submodules with upstream activity.
2. **Marketplace sweep** (web search): new/trending skills on directories that have no API.
3. **Redundancy filter** (model): drop anything already covered by Qor-logic, host built-ins, vendored references, or this repo's roadmap.
4. **Candidate proposals** (model): ready-to-paste YAML entries for `registry/candidates.yaml`, scored per the evaluation framework.

Presence in the watchlist is a discovery signal. It is not an adoption decision.

## Execution Flow

1. **Run the scan script** from this skill's directory (either runtime works; set `GITHUB_TOKEN` to avoid rate limits):

   ```
   node scripts/scout.ts
   bun run scripts/scout.ts --since 30d
   ```

2. **Sweep the no-API marketplaces** with web search, filtered to the window:
   - `new agent skills site:skills.sh`
   - `Claude skills site:mcpmarket.com`
   - `site:awesomeclaude.ai skills`
   - `agent skills site:agentskills.io OR site:skills-directory.com`
   - `Claude Code skills` on Hacker News / Reddit for notable community launches

3. **Filter for redundancy**. For each find, check in order:
   1. `registry/candidates.yaml`: already decided?
   2. `INDEX.md`: already local or vendored?
   3. `registry/sources.yaml`: is the source already classified?
   4. the bound gated/SDLC registry, if the operator has one: lifecycle-governed territory?
   5. host built-ins (`/code-review`, `/security-review`, `/verify`, or equivalents)
   6. this repo's ROADMAP: planned first-party?

   Reject or track redundant candidates with a `covered_by` note rather than creating competing process authority.

4. **Submodule freshness.** Report per vendored source:
   - source class (`official` or `community-vetted`)
   - current pinned SHA
   - latest upstream SHA or release where detectable
   - refresh-needed verdict
   - likely delta classification: docs-only / skill-content / tooling / security / license-provenance

   Refreshing follows `docs/vendor-freshness.md`: one source at a time, review before commit, then re-index in the same commit. Never blanket-update all submodules just because several moved upstream.

5. **Treat community-vetted sources as comparative evidence.** A change in a community source does not inherit trust from its previous pin. If behavior changes materially, determine whether any adopted/adapted local skill or candidate needs re-evaluation.

6. **Propose candidates.** For each genuinely new, non-redundant find, draft a registry entry with id, name, source, category, status, permission tier, and rationale. Default to `track` unless there is a concrete recurring workflow and enough evidence to justify sandboxing.

7. **Do not install or mutate intake state automatically.** Present the proposals first. A separate authorized action may apply registry changes, vendor pins, or local adaptations.

### If no JS runtime is available

Fetch the watchlist repositories' releases/commits pages directly and do the marketplace sweep via web search. Read `registry/sources.yaml` to preserve source classification. The rest of the flow is unchanged.

## Scheduling

- **Claude Code:** `/schedule` weekly.
- **Other agent platforms:** scheduled automation whose instruction is "Run the skills-pulse skill and present the intake digest."

## Output Format

```
# Skills Pulse — [Date Range]

## Watchlist activity
- [repo] ([source class]): [n commits / release vX.Y] — [what changed, one line]

## Submodule freshness
| Source | Class | Pinned | Upstream | Refresh? | Likely delta |
|--------|-------|--------|----------|----------|--------------|

## New candidates (non-redundant)
### [skill name] — [source]
[what it does, one line]
Proposed registry entry:
```yaml
- id: ...
  status: track
  ...
```

## Filtered out (redundant)
- [name] — covered by [existing capability]
```

## Notes

- Discovery signals such as stars and installs are not quality signals.
- Official source means first-party authority for that platform, not automatic permission for high-impact actions.
- Community-vetted means intentionally centralized for comparison/adaptation value, not blanket endorsement.
- Anything touching browser sessions, payments, identity, or credentials is proposed as `quarantined` regardless of appeal.
- This skill is read-only toward adoption: it proposes registry/source updates and refreshes; a human or explicitly authorized follow-up applies them.
