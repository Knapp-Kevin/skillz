---
name: skills-pulse
description: >-
  Review the agent-skills ecosystem for relevant new or changed sources and
  candidates using the external host agent's research capabilities, then record
  only evidence-backed intake recommendations. Use for a limited discovery pass
  when corpus curation needs fresh source context or the user explicitly asks
  what new skill material is worth considering.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skills Pulse
  emoji: "🧭"
  version: 2.0.0
---

# Skills Pulse

This is a passive discovery instruction set. `skillz` does not monitor repositories, schedule scans, make network requests, or run a scout process. Any discovery occurs only when an external agent is actively asked to perform it.

Discovery supports curation. It does not replace curation.

## Procedure

1. Establish the requested discovery window and scope.
2. Inspect already registered sources before searching for more.
3. Prefer changes or candidates that materially fill a known corpus gap.
4. Use the host agent's available web, GitHub, connector, or repository-reading capabilities to inspect source activity and candidate material.
5. For each find, establish source identity, license, current revision/freshness, intended use, and whether the material is actually a skill rather than surrounding repository tooling.
6. Check redundancy against existing user-facing skills and already reviewed source material.
7. Treat source popularity, stars, forks, installs, mentions, and activity as contextual signals only.
8. Propose a source or skill for intake only when it provides material reference value.
9. Do not automatically add, pin, install, or modify anything merely because it was discovered.

## Existing-source freshness

When reviewing a registered pinned source, compare the recorded pin with current upstream information if the host can establish it.

Classify meaningful changes as appropriate, for example:

- documentation only;
- skill content;
- shared reference/dependency change;
- security-sensitive change;
- license/provenance change.

Upstream movement is evidence, not an automatic upgrade. Re-review material changes before updating a pin or prior skill conclusions.

## Candidate triage

For each candidate answer:

- What concrete capability or pattern does it add?
- Is that capability already represented?
- Is the source authoritative, community-maintained, aggregated, or otherwise contextual?
- What license applies?
- Does the skill depend on shared files, tools, scripts, assets, services, or host assumptions?
- Is the material useful for unchanged reuse, adaptation, extraction, composition, or reference only?
- What evidence would justify spending curation effort on it now?

Default to **defer** when the corpus already has a higher-priority incomplete source.

## Output

Return a compact intake report containing:

- source/candidate;
- why it may matter;
- evidence inspected;
- license/source role;
- redundancy finding;
- freshness/activity context;
- recommendation: `REVIEW`, `TRACK`, `DEFER`, or `REJECT`;
- confidence and missing evidence.

Do not create a large speculative backlog from weak signals.

## Boundaries

- Discovery is read-only unless the user separately authorizes repository changes.
- No scheduled behavior exists inside `skillz`.
- No repository-owned network client or executable helper is required.
- Source reputation never substitutes for individual skill quality.
- Existing corpus curation remains the priority unless discovery exposes a concrete material gap.
