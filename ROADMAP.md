# Roadmap

`skillz` is a passive AI-skill reference and instruction repository whose core job is to help an existing agent build and refine the smallest useful fitted skill system for its user.

## Current milestone: governed curation mode

Status: **CORE IMPLEMENTATION COMPLETE**

The core architecture is now stable enough that routine work is curation rather than continued product construction.

### Ongoing curation

- discover promising first-party, official, and community skill sources;
- independently decide whether each source or skill adds meaningful value;
- preserve source, author, license, path, exact revision/identity, and material dependencies;
- assign controlled metadata, authority, portability, and semantic quality state;
- verify individual skills before unchanged trusted reuse;
- reject, retire, or retain only as bounded reference/negative evidence when appropriate;
- refresh review when material content changes.

### Selection quality

- refine taxonomy only when real curation or user feedback exposes a useful distinction;
- improve duplicate/overlap reasoning when the corpus actually creates ambiguity;
- preserve capability-first search and user-fit-before-reuse;
- improve composition/adaptation guidance only when real examples justify it.

### Returning-user refinement

- preserve smallest-change behavior;
- keep `NO CHANGE NEEDED` as a first-class successful outcome;
- improve drift/overlap guidance only when recurring semantic review or user feedback reveals a gap.

### Host portability

- add or document host-specific packaging only when a real host surface requires it;
- keep portable semantic skill identity separate from host packaging;
- never make one product's installation model universal.

### Human library experience

- evolve category navigation as the corpus grows;
- improve browsing and explanation where it reduces user burden;
- keep the README human-first and the AI entry route unmistakable;
- keep provenance and quality state understandable without requiring users to understand repository internals.

## Evaluation posture

Repository evaluation is semantic and probabilistic. Review the Markdown instructions for clarity, authority, fit, contradiction, likely weaker-model interpretation, and adversarial failure modes.

There is intentionally no CI or executable completion gate. Optional maintenance scripts may assist with bookkeeping, but they are not proof of repository correctness.

See `docs/evals/share-ready-semantic-review.md`.

## Durable design rules

1. **Compare before creation. User-fit before reuse.**
2. **Smallest useful set over maximum skill count.**
3. **Availability is not verification.**
4. **Exact-version identity matters for reviewed third-party material.**
5. **Attribution travels with third-party material.**
6. **Engine machinery does not count as user-facing library inventory.**
7. **Broad source material is reference/discovery unless individually governed.**
8. **Installation or a precise portable handoff is part of the user result.**
9. **Returning users are refined, not reset.**
10. **No-change is a valid outcome.**
11. **Semantic review is honest about probabilistic model behavior.**
12. **No CI/runtime proof layer should be introduced for repository completion.**

## Historical work

Older alpha/Qor plans, executable proof experiments, gate artifacts, and evaluation harnesses are historical context only. They do not define current architecture or completion criteria.