# Alpha Lock Criteria

Status: **NOT LOCKED**

Alpha is locked when `skillz` can reliably synthesize a fitted skill set for a user without confusing source reputation, availability, characterization, verification, or behavioral evidence.

## Required before alpha lock

- [x] Repository-link bootstrap entry contract exists.
- [x] User-facing library and engine machinery are structurally separate.
- [x] Approved indexed reference skills remain part of the usable library corpus.
- [x] Third-party provenance, source pins, and licensing rules exist.
- [x] Source role and source trust are separate registry concepts.
- [x] All non-Matt skill-bearing sources default to `unverified`.
- [x] Matt Pocock is explicitly the sole `trusted-baseline` source policy.
- [x] Characterization taxonomy exists.
- [x] Verification records bind tags/status to exact skill content fingerprints.
- [x] Offline drift detection can invalidate changed characterized skills.
- [ ] Bootstrap selection logic consumes verification status and characterization tags directly.
- [ ] Generated `INDEX.md` / `index.json` expose current verification status, tags, source role, and exact deduplicated counts.
- [ ] The generated index is refreshed and proven deterministic/idempotent against the current 12 vendored sources.
- [ ] Representative end-to-end bootstrap evals demonstrate reliable custom-set synthesis from accessible user evidence.
- [ ] At least one eval correctly reuses trusted/verified skills.
- [ ] At least one eval correctly rejects an unverified or stale skill from direct trusted selection.
- [ ] At least one eval correctly creates a new custom skill instead of forcing a poor existing match.
- [ ] Installation or portable handoff is demonstrated for the resulting fitted set.
- [ ] No selected trusted corpus item has unresolved dependency or license ambiguity.
- [ ] Documentation and generated counts agree with repository state.

## After alpha lock

Post-alpha work can focus primarily on enrichment rather than foundational semantics:

- characterize more of the existing corpus;
- verify more non-Matt skills;
- add behavioral validation evidence;
- add and retire sources;
- refine tags and matching weights;
- improve discovery and search;
- tune custom-skill synthesis from real use;
- expand host installation adapters.

Alpha lock is a capability threshold, not a declaration that the library is complete. A library that waits to become complete before shipping has discovered a very sophisticated way to never ship.
