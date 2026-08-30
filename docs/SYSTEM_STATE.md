# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-29 |
| **Milestone** | Core implementation complete |
| **State** | Governed curation mode |
| **Repository type** | Passive instruction/reference repository |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 42 |
| **Persisted third-party review companions** | 102 |
| **Pinned external corpora** | 12 |
| **Registered sources** | 17 |
| **Evaluation model** | Best-effort semantic + adversarial review |
| **CI/runtime requirement** | None |

## Current architecture

```text
skillz/
├── README.md
├── AGENT_START_HERE.md
├── BOOTSTRAP.md
├── AGENTS.md
├── CURATED.md
├── CURATION_QUEUE.md                 living curation evidence ledger
├── skills/                           42 first-party user-facing skill packages
│   └── categories/                   human browse-by-purpose navigation
├── vendor/                           12 exact-revision external reference corpora
├── .gitmodules                       pins the external reference corpora
├── engine/skills/                    passive bootstrap/maintenance procedures
├── registry/
│   ├── sources.yaml                  source roles, paths, licenses, exact pins
│   ├── skills/                       governed third-party provenance
│   ├── verification/                 exact-version semantic quality records
│   ├── local-verification.json       first-party structured reviews
│   └── taxonomy.yaml                 controlled metadata vocabulary
└── docs/evals/                       semantic/adversarial review records
```

There is no repository CI workflow, root runtime, root `scripts/` execution layer, root `tests/` gate, `.agent/`, or `.qor/` runtime machinery.

The existence of pinned Git submodules does **not** make the engine active. They are static reference material at exact upstream revisions. Normal agent use does not require them to be materialized locally because the same registered sources may be read through repository/API/web capabilities.

## Inventory boundaries

- 42 active first-party user-facing skills have individual structured semantic reviews.
- 12 pinned external corpora restore the broad 500+ reference surface.
- 102 current exact-version third-party verification companion files are persisted.
- AWS Agent Toolkit has an established eligible denominator of 72 skills and a prior full-pass disposition of 70 verified / 2 rejected; 2/72 currently have persisted exact-version provenance + verification companion pairs on `main` (`aws-cdk` and `aws-cloudformation`). The remaining companion closure is an active reconciliation lane, not evidence that the other prior dispositions disappeared.
- Historical source-level curation records document at least 210 reviewed external entry points across nine corpora.
- The gap between historical source-level evidence and current one-file companions is an explicit reconciliation lane in `CURATION_QUEUE.md`.
- Engine procedures do not count as user-facing inventory.
- 17 upstream sources are registered across pinned reference, tracked corpus, normative, and discovery roles.

## Quality model

- Source identity and individual skill quality are separate.
- Pinned/tracked material is reference/design evidence unless an individual exact-version record establishes stronger eligibility.
- `verified` means structured semantic review passed.
- `validated` means representative scenario/adversarial semantic review was also recorded.
- `unverified` and legacy `trusted-baseline` are not unchanged-reuse states.
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection.
- Fingerprints identify which exact material was reviewed. They are bookkeeping/provenance evidence, not executable proof.
- Skill-owned scripts, references, templates, fixtures, examples, JSON, assets, or other components remain legitimate parts of a skill package.

## User-flow state

The canonical bootstrap provides:

- explicit route selection;
- environment/authority binding;
- minimum-relevant-evidence need discovery;
- capability definition before skill-name search;
- first-party, governed, pinned-reference, tracked, and live discovery surfaces;
- whole-skill and component discovery;
- exact-version unchanged-reuse gating;
- explicit reuse/adapt/supplement/compose/create/no-skill decisions;
- smallest-coherent-system composition;
- host-specific artifact/handoff adaptation;
- semantic adversarial review;
- returning-user minimal refinement and `NO CHANGE NEEDED`.

## Responsibility boundary

The repository is responsible for making its instructions, skill packages, metadata, provenance, and curation evidence as clear and useful as reasonably possible.

It is **not** responsible for proving that arbitrary models of different capability levels will follow those instructions successfully. Multi-model benchmarks, success-rate targets, CI, runtime tests, and executable proof are not completion requirements.

## Evaluation state

The current repository-level closeout review is recorded in `docs/evals/share-ready-semantic-review.md`.

Result: **PASS — no unresolved material core-architecture ambiguity identified after closeout corrections.**

Corpus enrichment remains ongoing by design. That is tracked separately in `CURATION_QUEUE.md`.

## Current mode

**CURATION MODE.**

Future work is optional and occasional:

1. reconcile prior review evidence where useful;
2. continue admitted-source evaluation;
3. discover promising sources or skills;
4. determine independently whether they add meaningful value;
5. establish provenance/license/dependencies/required components;
6. score and characterize selected skills;
7. assign a decisive semantic quality state;
8. preserve useful negative/adaptation evidence where appropriate;
9. revisit core bootstrap instructions only when real use exposes a genuine ambiguity.

There is no standing core implementation backlog. The living curation queue is the intended long-term work surface.
