# Initial Implementation Finish Line

The initial implementation of `skillz` is intentionally scoped around the **user and AI-agent experience**, not exhaustive library curation.

The product is ready for alpha lock when a person can arrive for the first time, hand the repository to an AI, receive a governed fitted skill set, install or hand it off correctly, and later return to review and refine that set without restarting from zero.

## What must work before alpha lock

### First visit

1. The human can understand what the repository does from the top of `README.md`.
2. An AI agent can jump directly to its operating instructions.
3. The agent can inspect only legitimately available evidence and infer durable skill opportunities.
4. The agent can search the indexed library using category and governed quality metadata.
5. The agent can distinguish unchanged reuse, adaptation, composition, supplementation, custom creation, and no-skill outcomes.
6. Unverified material is design evidence by default, not silently trusted unchanged material.
7. Selected or created skills are evaluated appropriately.
8. The result ends in a concrete installation or portable-handoff state.

### Returning visit

1. The agent inventories the existing fitted set instead of rebuilding from zero.
2. It checks accessible fingerprints, freshness, quality state, overlap, gaps, and current user fit.
3. It preserves custom behavior that still works.
4. It makes the smallest justified change rather than maximizing novelty or skill count.
5. It can correctly conclude that no change is needed.
6. Materially changed skills are re-evaluated and installation/profile state is refreshed.

## What is not required before alpha lock

The following remain important, but they are post-alpha enrichment:

- exhaustive characterization of the indexed corpus;
- verification of every third-party skill;
- adding every promising source repository;
- large-scale behavioral benchmarking of the full library;
- perfect taxonomy or ranking weights;
- every possible host installation adapter.

Curation continues after alpha. It should not indefinitely postpone proving the core experience.

## Proof requirement

Alpha lock requires representative evidence for five decisions:

1. **eligible reuse**: an appropriate governed library skill is selected unchanged;
2. **unsafe or unproven reuse refusal**: unverified or stale material is not treated as trusted unchanged material;
3. **custom creation**: a materially poor library fit causes creation rather than forced reuse;
4. **returning refinement**: an existing set receives only a justified change while valid custom behavior is preserved;
5. **returning no-op**: an existing set is correctly left unchanged when no material improvement is established.

The exact live checklist is tracked in [Issue #15](https://github.com/Knapp-Kevin/skillz/issues/15) and [`docs/alpha-lock.md`](alpha-lock.md).
