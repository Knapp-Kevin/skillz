# Alpha Lock Criteria

Status: **NOT LOCKED**

Alpha is locked when `skillz` can reliably synthesize and later refine a fitted skill set for a user without confusing source reputation, availability, characterization, verification, behavioral evidence, or current user fit.

## Required before alpha lock

- [x] Repository-link first-visit bootstrap entry contract exists.
- [x] Returning-user review/refine entry contract exists.
- [x] Human browse-by-purpose category navigation exists for the local library.
- [x] User-facing library and engine machinery are structurally separate.
- [x] Approved indexed reference skills remain part of the usable library corpus.
- [x] Third-party provenance, source pins, and licensing rules exist.
- [x] Source role and source trust are separate registry concepts.
- [x] Source-level quality defaults are explicit and machine-readable.
- [x] Characterization taxonomy exists and covers engineering plus broader knowledge-work use cases.
- [x] Verification records bind tags/status to exact skill content fingerprints.
- [x] Offline drift detection can invalidate changed characterized skills.
- [ ] Bootstrap selection logic consumes verification status and characterization tags directly.
- [ ] Generated `INDEX.md` / `index.json` expose current verification status, tags, source role, human category, and exact deduplicated counts.
- [ ] The generated index is refreshed and proven deterministic/idempotent against the current vendored sources.
- [ ] Recursive local-skill discovery is integrated into index, audit, risk-audit, and sync tooling before category folders become canonical skill paths.
- [ ] Representative end-to-end first-visit bootstrap evals demonstrate reliable custom-set synthesis from accessible user evidence.
- [ ] At least one eval correctly reuses a trusted/verified skill.
- [ ] At least one eval correctly rejects an unverified or stale skill from direct trusted selection.
- [ ] At least one eval correctly creates a new custom skill instead of forcing a poor existing match.
- [ ] Installation or portable handoff is demonstrated for the resulting fitted set.
- [ ] A returning-user eval inventories an existing fitted set, detects meaningful drift or a genuine gap, makes the smallest justified change, and preserves still-valid custom behavior.
- [ ] A returning-user eval can correctly conclude that no change is needed.
- [ ] No selected trusted corpus item has unresolved dependency or license ambiguity.
- [ ] Documentation and generated counts agree with repository state.

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
