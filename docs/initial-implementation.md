# Initial Implementation Finish Line

The initial implementation of `skillz` is the **user + agent experience of building and refining a dependable fitted skill system**, not the accumulation of an arbitrary number of skills.

The repository is passive. A normal user hands the repository to an agent; the agent uses legitimately available context and capabilities to discover durable needs, compare reference material, select or synthesize the smallest coherent system, validate it honestly, and install or hand it off in the format supported by the active host.

## What the core experience must do

### First visit

1. Route directly into bootstrap instead of stopping at a repository summary.
2. Bind to the active environment, evidence scope, privacy boundaries, authority, and installation capability.
3. Infer durable user needs from minimum relevant evidence.
4. Translate those needs into capability requirements before searching by skill name.
5. Search the broad reference corpus and individually governed surface by capability/metadata.
6. Distinguish whole-skill fit from useful components/patterns.
7. Gate unchanged third-party reuse on current exact-version quality and operational fit.
8. Choose explicitly among reuse, adaptation, supplementation, composition, clean custom creation, checklist/helper, dynamic behavior, or no skill.
9. Compose the smallest coherent system without importing unnecessary reference ceremony.
10. Produce real artifacts for the active environment.
11. Adversarially test important custom/adapted behavior and report behavioral evidence honestly.
12. End in a concrete installation or portable-handoff state.

### Returning visit

1. Inventory the current fitted system rather than resetting it.
2. Preserve still-valid custom behavior.
3. Identify only material drift, gaps, conflicts, or changed needs.
4. Re-run capability definition/search/governance for affected capabilities.
5. Make the smallest justified change.
6. Correctly return `NO CHANGE NEEDED` when evidence does not justify modification.
7. Re-evaluate changed artifacts and refresh installation/handoff state.

## Reference corpus versus governed individual skills

The broad local/vendor/tracked corpus is useful discovery and design material. Physical presence or source reputation does not make every upstream skill trusted inventory.

An individually governed third-party skill has exact provenance, fingerprint, controlled metadata, dependency/authority/portability characterization, and a decisive structured review record.

Only exact `verified` or `validated` records are eligible for unchanged third-party consideration. Other material may still inform clean design or bounded adaptation under provenance/licensing and safety constraints.

## Maintainer proof is separate from normal use

Normal agent use must not require a local clone, shell, Git executable, Node/Bun runtime, initialized submodules, writable `skillz` checkout, or GitHub Actions.

Maintainer-grade repository proof does require a fully materialized checkout because it validates pinned source state, generated catalog semantics/counts, deterministic regeneration, audits, tests, and exact characterization fingerprints.

`node scripts/share-ready-preflight.ts` is the one-command deterministic closure gate before independent behavioral proof.

## Blind behavioral proof

Static contracts are necessary but insufficient. Completion requires isolated treatment runs proving that agents actually follow the intended process.

The original v1 fixture is invalid because evaluator keys were public. The v2 fixture is also invalid for blind closure because public Issue #15 later mapped its neutral IDs to expected decision classes.

The current active treatment fixture is:

`docs/evals/fixtures/share-ready-scenarios-v3.json`

Expected decisions, candidate hints, and scenario-specific scoring criteria must remain in a separately stored private evaluator bundle until each treatment response is frozen. `scripts/verify-alpha-evaluator-bundle.mjs` binds that private bundle to the exact public fixture.

The proof set must collectively demonstrate:

- appropriate governed whole-skill reuse when it truly fits;
- refusal of unsafe/unproven unchanged reuse;
- component extraction and composition without reference contamination;
- custom creation when reuse would distort the workflow;
- constrained connector/read-only success without local runtime;
- host-specific packaging/handoff honesty;
- returning-user minimal refinement;
- returning-user no-op;
- success by at least one materially weaker/cheaper model, not only a frontier model.

## Alpha versus share-ready

Alpha lock is the narrower internal capability threshold tracked in [`alpha-lock.md`](alpha-lock.md) and Issue #15.

Share-ready repository completion is stronger and is tracked by Issue #56. It additionally requires the intentionally governed corpus to be companion-complete and decisive, front-door documentation to agree with the engine, and no unresolved repeated failure attributable to repository ambiguity.

Once share-ready is green, adding more sources and skills is enrichment rather than unfinished core functionality.