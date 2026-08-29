---
name: skills-pulse
description: >-
  Review the agent-skills ecosystem for promising new or changed sources and
  propose selective curation candidates. Use when the user explicitly asks for
  a skills scan, source refresh, or new-candidate review.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skills Pulse
  emoji: "🧭"
  version: 2.0.0
  repo-bound: true
---

# Skills Pulse

**On-demand curation procedure only.**

`skillz` does not monitor, crawl, schedule, or automatically ingest anything. When explicitly asked, the active host agent may inspect public sources using whatever legitimate web, GitHub, connector, or browsing capabilities it already has.

## Procedure

1. Read `registry/sources.yaml` and current governed records so already-known material is not rediscovered as new.
2. Inspect a small, relevant set of public sources for meaningful changes or differentiated skills.
3. Treat popularity, stars, installs, or official branding as discovery signals only.
4. For promising material, check:
   - source identity and maintainer provenance;
   - license/terms;
   - exact revision or content identity when establishable;
   - dependencies and bundled resources;
   - authority/side effects;
   - portability and host assumptions;
   - overlap with existing local or governed capabilities.
5. Prefer differentiated capability over generic best-practice duplication.
6. Propose only candidates worth individual semantic review.
7. Do not admit, install, copy, or modify anything merely because it was discovered.

## Output

For each candidate provide:

- source and exact revision/identity when available;
- what differentiated capability it adds;
- likely overlap/redundancy;
- license/dependency/authority concerns;
- recommendation: `SOURCE-VET`, `INDIVIDUAL-REVIEW`, `REFERENCE-ONLY`, or `IGNORE`.

If nothing materially useful is found, report that plainly. Curation does not need to manufacture work.

## Negative rules

- No scheduling or background monitoring is part of this repository.
- No repository-owned crawler or scan script is required or implied.
- Do not bulk-ingest repositories.
- Do not treat source-level trust as individual skill proof.
- Do not create a backlog merely to preserve activity.
