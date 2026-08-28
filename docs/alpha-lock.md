# Alpha Lock Criteria

Status: **NOT LOCKED**

Alpha is locked when `skillz` can reliably synthesize and later refine a fitted skill set for a user without confusing source reputation, availability, characterization, verification, behavioral evidence, or current user fit.

## Required before alpha lock

- [x] Repository-link first-visit bootstrap entry contract exists.
- [x] Returning-user review/refine entry contract exists.
- [x] Human browse-by-purpose category navigation exists for the local library.
- [x] Canonical machine-readable local category assignments exist.
- [x] User-facing library and engine machinery are structurally separate.
- [x] Approved indexed reference skills remain part of the usable library corpus.
- [x] Third-party provenance, source pins, and licensing rules exist.
- [x] Source role and individual skill quality are separate registry concepts.
- [x] A missing individual quality record defaults to unverified for normal selection.
- [x] Characterization taxonomy exists and covers engineering plus broader knowledge-work use cases.
- [x] Verification records bind tags/status to exact skill content fingerprints.
- [x] Offline drift detection can invalidate changed characterized skills.
- [x] Bootstrap has a deterministic selector that consumes verification status and characterization tags directly.
- [x] Default governed selection excludes unverified unchanged reuse and blocks stale/rejected/retired material; explicit unverified review is design-evidence only.
- [x] Recursive local-skill discovery is integrated into index, audit, risk-audit, and sync tooling before category folders become canonical skill paths.
- [x] Alpha preflight has an explicit vendored-source materialization gate that binds every vendored registry source to a clean initialized submodule at exactly the superproject gitlink SHA.
- [x] Alpha preflight requires every characterized skill path to be available after materialization rather than silently accepting missing verification targets.
- [x] Catalog proof rejects semantically incoherent schema-v2 output, including zero-skill vendored sources, source/count mismatch, impossible aggregate counts, duplicate source identities, and malformed catalog shapes.
- [x] The original public v1 behavioral fixture set is explicitly retired because its expected decisions and scoring keys were committed publicly and remain recoverable from Git history.
- [x] The rotated v2 public treatment fixture contains only synthetic user context, uses neutral scenario IDs, and mechanically forbids evaluator-only answer-key fields.
- [x] A private evaluator-bundle verifier binds frozen evaluator criteria to the exact public v2 fixture by set ID, SHA-256, and complete scenario coverage without committing the rubric.
- [ ] The exact vendored-source materialization gate has passed on the current commit in a fully materialized checkout.
- [ ] Generated `INDEX.md` / `index.json` have been refreshed from the current fully materialized corpora and expose verification status, tags, source role, human category, and exact counts.
- [ ] The refreshed generated index is proven semantically coherent and deterministic/idempotent against the current vendored sources.
- [ ] The private v2 evaluator bundle has been verified against the exact committed public fixture before treatment execution.
- [ ] Three isolated v2 first-visit runs collectively demonstrate eligible reuse/minimal adaptation, refusal of unsafe or unproven unchanged reuse, and custom creation when reuse would distort the workflow.
- [ ] Two isolated v2 returning-user runs collectively demonstrate minimal justified refinement and a correct no-change outcome.
- [ ] Every treatment run is completed before its matching private evaluator criteria are opened.
- [ ] Installation or portable handoff is demonstrated and truthfully reported for the resulting fitted set.
- [ ] Changed material is re-evaluated and installation/profile state is updated where required.
- [ ] No selected trusted corpus item has unresolved dependency or license ambiguity.
- [ ] Documentation and generated counts agree with repository state.

## Invalid evidence

The retired v1 scenario identifiers and their historical results, if any, cannot satisfy the behavioral alpha gate. Their evaluator mappings were public and therefore are not blind evidence.

A v2 run is also invalid if the treatment agent receives the private evaluator bundle, evaluator-only criteria, candidate hints, or prior scored treatment output before its own output is frozen.

## After alpha lock

Post-alpha work can focus primarily on enrichment rather than foundational semantics:

- characterize more of the existing corpus;
- verify more skills that require structured review;
- add behavioral validation evidence;
- add and retire sources;
- refine tags and matching weights;
- improve discovery and search;
- tune custom-skill synthesis from real use;
- expand returning-user refinement heuristics;
- expand host installation adapters.

Alpha lock is a capability threshold, not a declaration that the library is complete. A library that waits to become complete before shipping has discovered a very sophisticated way to never ship.
