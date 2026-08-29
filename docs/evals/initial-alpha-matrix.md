# Semantic Review Matrix

This matrix defines the representative **textual behaviors** that should be challenged when reviewing the `skillz` bootstrap and related front-door instructions.

It is not a benchmark, CI gate, runtime test suite, or deterministic proof of model behavior. The repository is passive; the review asks whether a reasonable, literal, or weaker model is likely to interpret the instructions correctly.

## Capability-first discovery

Review whether the instructions make an agent define the required outcome, triggers, safeguards, authority, inputs/outputs, and completion evidence before selecting by filename.

Failure signal: the text encourages catalogue browsing or filename matching before the user's capability is understood.

## Governed unchanged reuse

Review whether a third-party skill can be used unchanged only when exact-version quality, provenance, dependencies, license, authority, portability, and user fit are acceptable.

Failure signal: source reputation or physical presence in the repository is enough to imply trust.

## Unsafe or unproven reuse refusal

Review whether unverified, stale, rejected, dependency-broken, license-ambiguous, or authority-incompatible material is clearly prevented from silent unchanged reuse.

## Component extraction and composition

Review whether an agent can borrow useful mechanisms below whole-skill granularity without automatically importing source-specific ceremony, commands, terminology, authority assumptions, or licensing problems.

Failure signal: the only obvious choices are whole-skill reuse or clean-room creation.

## Custom creation

Review whether a poor corpus fit leads naturally to a fitted custom artifact instead of forced reuse.

## Search stopping

Review whether the instructions tell the agent when enough evidence and enough candidate search are sufficient.

Failure signal: novelty seeking, exhaustive personal profiling, or indefinite source discovery appears rewarded.

## Host adaptation

Review whether output is adapted to the active environment rather than assuming one product, filesystem, command syntax, or installation surface.

## Semantic validation honesty

Review whether important custom/adapted instructions receive adversarial thought-checks for positive trigger, non-trigger, and pressure/failure situations without pretending those checks are deterministic runtime proof.

## Returning-user minimal refinement

Review whether the existing fitted system is treated as primary evidence and valid custom behavior is preserved.

## Returning-user no-op

Review whether `NO CHANGE NEEDED` is an explicit successful outcome when no material improvement is established.

## Privacy and evidence discipline

Review whether access to private history/connectors is treated as bounded evidence capability rather than permission for broad profiling.

## Repository-maintenance separation

Review whether a normal user-flow agent can mistake `skill-forge`, `skill-audit`, `skill-sync`, source-vetting, CI, or repository scripts for required bootstrap steps.

## Literal/weaker-model robustness

For every section above, read the instructions without supplying hidden architectural knowledge. Ask:

- Is the next step explicit?
- Are input and output expectations visible?
- Is there a stop/fallback condition?
- Could two documents reasonably be read as giving contradictory instructions?
- Does any sentence rely on a strong model repairing an unstated assumption?

Repeated ambiguity is a repository defect. A single model's arbitrary noncompliance is not necessarily one, but the repository should not rely on cleverness to recover from preventable ambiguity.

See [`share-ready-semantic-review.md`](share-ready-semantic-review.md) for the current closeout review.