# Alpha Milestone

Status: **COMPLETE / HISTORICAL**

The alpha milestone established the basic shape of `skillz`: a passive repository that an existing agent can read to build or refine a fitted skill system for its user.

It is not an executable release gate. There is no application runtime, CI requirement, preflight command, or deterministic model-behavior proof attached to this milestone.

## What alpha established

- repository-link first-visit bootstrap entry exists;
- returning-user refinement starts from the fitted system and preserves valid custom behavior;
- user-facing library material is separated from repository-maintenance engine material;
- `skill-bootstrap` is the single canonical normal user-flow orchestrator;
- connector/API/web and minimal read-only hosts are legitimate normal-use paths;
- capability-first discovery, whole-skill comparison, component extraction, composition, custom creation, adversarial review, and host adaptation are explicit;
- normal bootstrap must not mutate the `skillz` repository;
- source reputation and individual skill quality are separate concepts;
- exact-version review records bind quality/tags to the text that was actually inspected;
- broad unreviewed source material is reference/design evidence rather than silent trusted reuse;
- returning-user review can correctly conclude `NO CHANGE NEEDED`.

## Evaluation boundary

The repository is evaluated semantically. Reviewers inspect whether the instructions are clear, bounded, internally consistent, and likely to guide an agent correctly.

Representative scenario and adversarial review should challenge:

- trigger and non-trigger interpretation;
- privacy/evidence scope;
- capability-first versus filename-first discovery;
- unchanged reuse versus adaptation/custom creation;
- component reuse without importing source-specific baggage;
- authority and approval boundaries;
- host-specific packaging/handoff;
- returning-user minimal change and no-op behavior;
- false claims of evidence or completion.

A literal/weaker-model reading is especially valuable because ambiguity that only a frontier model can repair is an instruction-design defect.

The current repository-level semantic review is recorded in [`evals/share-ready-semantic-review.md`](evals/share-ready-semantic-review.md).

## After alpha

The stronger core-completion definition is documented in [`initial-implementation.md`](initial-implementation.md). Once that boundary is satisfied, routine work moves to curation: discover, evaluate, characterize, and selectively admit more skills without treating the repository as perpetually unfinished.