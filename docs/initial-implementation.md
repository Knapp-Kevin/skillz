# Initial Implementation Finish Line

The initial implementation of `skillz` is intentionally scoped around the **user and AI-agent experience**, not exhaustive library curation.

The product is ready for alpha lock when a person can arrive for the first time, hand the repository to an AI, receive a governed fitted skill set, install or hand it off correctly, and later return to review and refine that set without restarting from zero.

That promise is host-portable. A normal user/agent flow must not depend on a local clone, shell, Git executable, Node/Bun runtime, initialized submodules, or GitHub Actions. Those capabilities belong to maintainer-grade deterministic repository verification.

## What must work before alpha lock

### First visit

1. The human can understand what the repository does from the top of `README.md`.
2. An AI agent can jump directly to its operating instructions.
3. A constrained agent with repository read access can proceed through a connector/API/web path when local execution is unavailable.
4. The agent can inspect only legitimately available evidence and infer durable skill opportunities.
5. The agent can search the library using category and governed quality metadata, either through local tooling or direct registry/provenance/upstream inspection.
6. Where the host exposes exact content identity, the agent can compare a candidate's upstream Git blob/content SHA to its recorded fingerprint without local Git.
7. The agent can distinguish unchanged reuse, adaptation, composition, supplementation, custom creation, and no-skill outcomes.
8. Unverified material is design evidence by default, not silently trusted unchanged material.
9. Selected or created skills are evaluated appropriately.
10. The result ends in a concrete installation or portable-handoff state.

### Returning visit

1. The agent inventories the existing fitted set instead of rebuilding from zero.
2. It checks accessible fingerprints, freshness, quality state, overlap, gaps, and current user fit.
3. It preserves custom behavior that still works.
4. It makes the smallest justified change rather than maximizing novelty or skill count.
5. It can correctly conclude that no change is needed.
6. Materially changed skills are re-evaluated and installation/profile state is refreshed.

## Maintainer proof is separate from normal use

Repository-wide generated-catalog proof still requires a compatible maintainer environment because it validates all pinned corpora, generated counts, semantic invariants, and byte-identical regeneration together.

Failure to run that maintainer proof on one constrained host does not mean normal `skillz` use is broken. Likewise, a successful connector-native user flow does not replace the separate repository-wide preflight.

The connector-native portability smoke in [`evals/connector-native-smoke.md`](evals/connector-native-smoke.md) exists specifically to prove this boundary.

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

1. **eligible reuse or minimal adaptation**: an appropriate governed library skill is selected or minimally adapted because it actually fits;
2. **unsafe or unproven reuse refusal**: unverified or stale material is not treated as trusted unchanged material;
3. **custom creation**: a materially poor library fit causes creation rather than forced reuse;
4. **returning refinement**: an existing set receives only a justified change while valid custom behavior is preserved;
5. **returning no-op**: an existing set is correctly left unchanged when no material improvement is established.

These five decisions must be demonstrated with a **blind treatment/evaluator split**. Public treatment fixtures may contain only synthetic user context and neutral scenario identifiers. Expected decisions, candidate hints, and scenario-specific scoring criteria must remain outside the public repository and outside the treatment-agent context until that treatment output is frozen.

The evaluator-only rubric must be precommitted before treatment execution and fingerprint-bound to the exact public fixture. The repository provides `scripts/verify-alpha-evaluator-bundle.mjs` for that binding.

The original public v1 A1/A2/A3/R1/R2 fixture set cannot satisfy this proof requirement because its evaluator mappings were committed publicly and remain recoverable from Git history. It is retained only as historical evidence of the superseded design.

The exact live checklist is tracked in [Issue #15](https://github.com/Knapp-Kevin/skillz/issues/15) and [`docs/alpha-lock.md`](alpha-lock.md).
