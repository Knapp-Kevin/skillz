# Core Implementation Completion

Status: **CORE COMPLETE / CURATION MODE**

The core implementation of `skillz` is the **user + agent experience of building and refining a dependable fitted skill system**, not the accumulation of an arbitrary number of skills.

`skillz` is passive. It contains instructions, reference material, skill packages, and governance metadata. The active agent reads those materials and does the work with capabilities legitimately available in its host.

There is no repository-owned runtime to prove. Core completion is based on semantic coherence, governed curation, and best-effort adversarial review of the instructions.

## Core experience

### First visit

The canonical bootstrap makes it straightforward for an agent to:

1. route into bootstrap rather than stop at a repository summary;
2. bind to the active environment, evidence scope, privacy boundaries, authority, and installation capability;
3. infer durable user needs from minimum relevant evidence;
4. translate those needs into capability requirements before searching by skill name;
5. search local skills, governed external records, and tracked upstream references by capability/metadata;
6. distinguish whole-skill fit from useful components/patterns;
7. preserve and evaluate required skill-owned scripts, references, templates, fixtures, or other components when they are part of a selected skill package;
8. gate unchanged third-party reuse on exact-version quality and actual fit;
9. choose explicitly among reuse, adaptation, supplementation, composition, clean custom creation, checklist/helper, dynamic behavior, or no skill;
10. compose the smallest coherent system without importing unnecessary reference ceremony;
11. produce complete artifacts for the active environment when possible, otherwise a truthful portable handoff;
12. adversarially review important instructions and state uncertainty honestly.

### Returning visit

The returning path:

1. inventories the current fitted system rather than resetting it;
2. preserves still-valid custom behavior and required supporting components;
3. identifies only material drift, gaps, conflicts, or changed needs;
4. re-runs capability definition and comparison only where change is plausible;
5. makes the smallest justified change;
6. correctly returns `NO CHANGE NEEDED` when evidence does not justify modification.

## Reference corpus versus governed skills

Tracked upstream corpora are discovery and design material. Source reputation does not make every upstream skill trusted inventory.

An individually governed third-party skill has exact provenance, content identity, controlled metadata, dependency/component/authority/portability characterization, and a decisive structured semantic review record.

Only exact `verified` or `validated` records are eligible for unchanged third-party consideration. Other material may still inform clean design or bounded adaptation under provenance, licensing, safety, and rejection-reason constraints.

First-party skills are subject to the same basic quality discipline. Their individual reviews live in `registry/local-verification.json`.

## Evaluation model

The repository's evaluation surface is semantic and probabilistic.

Useful review asks:

- Is the intended route explicit?
- Are input, output, stop, and fallback conditions clear enough at each stage?
- Can a reader distinguish reference material from governed unchanged-reuse candidates?
- Are component extraction and composition understandable without importing another source's ceremony?
- Are authority, privacy, dependencies, and installation claims bounded truthfully?
- Are legitimate skill-owned supporting components preserved and characterized rather than confused with engine machinery?
- Can a returning agent preserve good behavior and decide not to change anything?
- Do any documents contradict the bootstrap or use obsolete terminology?

Representative scenarios and adversarial readings are best-effort review evidence. They are not benchmarks of model capability, success-rate commitments, or claims that arbitrary models will perform correctly.

See [`evals/share-ready-semantic-review.md`](evals/share-ready-semantic-review.md).

## Completion criteria

The repository is core-complete when:

- the canonical passive bootstrap path is explicit and ordered;
- normal user synthesis is unmistakably separated from repository maintenance;
- every intentionally governed skill has adequate provenance/metadata and a decisive semantic quality state;
- broad source material is clearly reference/design evidence unless individually governed;
- active first-party user-facing skills have individual review records;
- front-door and governance documentation agree on the same quality semantics;
- best-effort semantic/adversarial review finds no unresolved repository-level ambiguity likely to materially derail the intended process.

No CI, executable preflight, application test harness, hidden evaluator bundle, multi-model benchmark, weaker-model success target, or runtime proof is part of this definition.

## Responsibility boundary

The repository is responsible for giving an agent the best reasonable opportunity to succeed through clear instructions, useful skills, preserved skill components, trustworthy provenance, and honest metadata.

The capability or compliance of the model that later reads those materials is outside the repository's responsibility.

## Curation mode

After core completion, normal repository work is deliberately boring:

1. occasionally discover promising new skills or source repositories;
2. decide independently whether they add meaningful capability;
3. source-vet and establish provenance/license/dependencies;
4. individually score, tag, characterize, and disposition admitted skills;
5. retain weak or unsafe material only as clearly bounded reference/negative evidence when useful;
6. update the bootstrap only when real feedback reveals an actual instruction-design problem.

New sources make the ecosystem broader. They do not reopen the question of whether the core repository is complete.
