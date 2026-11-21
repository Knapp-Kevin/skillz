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
  version: 2.1.0
  repo-bound: true
---

# Skills Pulse

**On-demand curation procedure only.**

`skillz` does not monitor, crawl, schedule, or automatically ingest anything. When explicitly asked, the active host agent may inspect public sources using whatever legitimate web, GitHub, connector, or browsing capabilities it already has.

## Procedure

1. Read `registry/sources.yaml`, the capability directory, and current governed/discovery records so already-known material is not rediscovered as new. Treat all dated snapshot counts as provenance observations, never as the corpus size.
2. Derive the requested **capability coverage and time window** before selecting public source lanes. Inspect all relevant accessible governed and indexed discovery families, plus current public sources when material. Use a bounded shortlist for an ordinary question, but **do not impose a fixed tiny source cap** on an explicitly broad sweep. Follow all relevant pages/chunks/cursors of a selected source; record inaccessible/partial families. A source pin and its observed latest change are separate facts.
3. Search by intended task and mechanism, plus alternate language and neighboring domains. Check possible retrieval false positives from schema field names or shared folder names, and false negatives from unmapped taxonomy slots. Treat popularity, stars, installs or official branding as discovery leads only.
4. For promising material, check:
   - source identity and maintainer provenance;
   - license/terms;
   - exact revision or content identity when establishable;
   - dependencies and bundled resources;
   - authority/side effects;
   - portability and host assumptions;
   - overlap with existing local or governed capabilities.
5. Prefer evidence-backed differentiated capability over generic best-practice duplication. Compare complete package scope, exact source identity, existing mechanisms and observed limitations before collapsing same-name records or claiming novelty. A source-level change does not establish an individual skill's behavior or eligibility.
6. Propose only candidates worth individual semantic review, recording `FOUND`, `PACKAGE_READ`, `REVIEWED`, or `NOT_INSPECTED` separately and stating what must be verified next. Where a known authored skill is stronger, identify a concrete refinement mechanism rather than producing another duplicate. A promising unreviewed file is not installed or endorsed.
7. Do not admit, install, copy, or modify anything merely because it was discovered.

## Discovery quality controls

Before asserting "nothing relevant" or "new capability", make a brief
coverage record: query/capability synonyms, source families and revision
pins, paginated parts attempted, candidate matches, full packages
actually read, and unresolved rights, access or review status. A missing
map entry, empty first page, stale snapshot, search result matching a
serialized metadata key, or a same-name package from another publisher
does not prove absence, relevance, or equivalence.

For material decisions, test one intentionally irrelevant term
(**precision probe**) and one credible alternative synonym/mechanism
(**recall probe**). These are observations about available search,
not synthetic claims about end-user usage. Record skipped probes with
a reason when the request is a narrow exact-identity lookup.

Do not scan every source by reflex. Stop when additional coverage is
unlikely to change a bounded decision; continue more broadly when the
user explicitly requests comprehensive discovery or a gap decision
would otherwise be premature. Never convert a partial search into an
exhaustive claim.

## Output

For each candidate provide:

- source and exact revision/identity when available, including checked-at date;
- what differentiated capability it adds;
- likely overlap/redundancy;
- license/dependency/authority concerns, package-read versus lead-only status, and unsearched source limits;
- recommendation: `SOURCE-VET`, `INDIVIDUAL-REVIEW`, `REFERENCE-ONLY`, or `IGNORE`.

If nothing materially useful is found, report that plainly. Curation does not need to manufacture work.

## Negative rules

- No scheduling or background monitoring is part of this repository.
- No repository-owned crawler or scan script is required or implied.
- Do not bulk-ingest repositories.
- Do not treat source-level trust as individual skill proof.
- Do not create a backlog merely to preserve activity.
