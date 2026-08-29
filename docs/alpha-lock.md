# Alpha Lock Criteria

Status: **NOT LOCKED**

Alpha is the narrower internal capability milestone. Share-ready repository completion is the stronger gate tracked by Issue #56.

Alpha is locked when `skillz` can reliably synthesize and later refine a fitted skill system without confusing source reputation, reference availability, exact-version quality, behavioral evidence, current user fit, authority, or host capability.

## Structural capability already established

- [x] Repository-link first-visit bootstrap entry exists.
- [x] Returning-user refinement path exists and preserves valid custom behavior.
- [x] User-facing library and engine machinery are structurally separate.
- [x] `skill-bootstrap` is the single canonical normal user-flow orchestrator.
- [x] Normal bootstrap does not require maintainer-grade local runtime.
- [x] Connector/API/web and minimal read-only paths are supported.
- [x] Capability-first discovery, whole-skill comparison, component extraction, composition, custom creation, adversarial review, and host adaptation are explicit stages.
- [x] Normal bootstrap explicitly must not mutate the `skillz` repository.
- [x] Source role and individual skill quality are separate concepts.
- [x] Exact-version verification records bind status/tags to canonical skill fingerprints.
- [x] `verified` and `validated` are the only current unchanged-reuse quality states.
- [x] Missing/unverified/legacy-baseline material is design evidence rather than silent trusted reuse.
- [x] Stale/rejected/retired material is excluded from normal unchanged selection.
- [x] Component borrowing is explicitly subject to provenance, licensing, dependency, rejection-reason, authority, and host-fit checks.
- [x] Deterministic selector consumes governed status and controlled metadata.
- [x] Offline fingerprint-drift detection exists.
- [x] Vendored-source materialization and semantic catalog checks exist.
- [x] Connector-native exact-version smoke has succeeded without local Git/Node/submodules.
- [x] Share-ready governed-corpus verifier and one-command deterministic preflight exist.

## Behavioral-evidence integrity

Two earlier public treatment generations are invalid as blind closure evidence:

- **v1** exposed evaluator answer-key material directly in the public repository.
- **v2** used neutral IDs, but public Issue #15 later mapped those IDs to expected decision classes. That public mapping compromises blindness even though the fixture itself contained no evaluator fields.

The active public treatment set is now:

`docs/evals/fixtures/share-ready-scenarios-v3.json`

Its neutral IDs must never be publicly mapped to expected decisions or scenario-specific scoring criteria while the set is active.

The evaluator-only rubric must:

- remain outside the repository and treatment workspace;
- be frozen before treatment execution;
- bind to the exact public v3 fixture bytes by set ID and SHA-256;
- cover every scenario ID exactly once;
- contain expected decisions and `must_observe` / `must_not` criteria privately;
- be opened for a scenario only after that treatment output is frozen.

The repository verifier is `scripts/verify-alpha-evaluator-bundle.mjs`.

## Remaining alpha gate

- [ ] Run `node scripts/share-ready-preflight.ts` in a fully materialized checkout of the exact candidate commit and record PASS.
- [ ] Record exact regenerated schema-v2 catalog counts and byte-identical second-pass proof.
- [ ] Create/freeze a new private evaluator bundle for `share-ready-v3-2026-08-29` outside the repository.
- [ ] Verify that private bundle against the committed v3 fixture before treatment.
- [ ] Run every v3 scenario in a fresh isolated treatment context.
- [ ] Include both a strong model and at least one materially weaker/cheaper model across the proof set.
- [ ] Demonstrate connector/API/read-only completion without local runtime.
- [ ] Demonstrate whole-skill eligibility reasoning and refusal of unsafe/unproven unchanged reuse.
- [ ] Demonstrate component extraction/composition without importing unnecessary source ceremony.
- [ ] Demonstrate clean custom creation when corpus fit would distort the workflow.
- [ ] Demonstrate truthful host-specific packaging/install or portable handoff.
- [ ] Demonstrate returning-user minimal refinement.
- [ ] Demonstrate a correct `NO CHANGE NEEDED` outcome.
- [ ] No repeated failure remains attributable to repository ambiguity or broken/stale references.

## Invalid evidence

A run cannot satisfy alpha/share-ready behavioral proof if:

- its scenario ID has been publicly mapped to expected evaluator outcome;
- treatment received private criteria, candidate hints, prior scored output, or evaluator notes before freezing its response;
- the same context was used for treatment and evaluator material;
- behavioral validation, fingerprint proof, installation, or inaccessible evidence was fabricated;
- maintainer-preflight failure was hand-waved away as irrelevant.

Conversely, inability to run maintainer Node/Git tooling in a constrained host is not evidence that normal user bootstrap failed. Those are separate proof layers.

## After alpha lock

Post-alpha work may broaden sources, add individual reviews/behavioral evidence, improve ranking/taxonomy, and add host adapters. Those are enrichment once the core fitted-skill-system experience is proven.