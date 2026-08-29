# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-29 |
| **Milestone** | Core implementation complete |
| **State** | Governed curation mode |
| **Repository type** | Passive Markdown instruction/reference repository |
| **Evaluation model** | Best-effort semantic + adversarial review |
| **CI/runtime requirement** | None |

## Current architecture

```text
skillz/
├── README.md
├── AGENT_START_HERE.md
├── BOOTSTRAP.md
├── AGENTS.md
├── skills/                           first-party user-facing skills
│   └── categories/                   human browse-by-purpose navigation
├── engine/skills/                    passive bootstrap/maintenance procedures
├── registry/
│   ├── sources.yaml                  tracked upstream sources
│   ├── skills/                       governed third-party provenance
│   ├── verification/                 exact-version semantic quality records
│   ├── local-verification.json       first-party structured reviews
│   └── taxonomy.yaml                 controlled metadata vocabulary
└── docs/evals/                       semantic/adversarial review records
```

There is no `vendor/`, `.gitmodules`, `scripts/`, `tests/`, `.agent/`, `.qor/`, or CI workflow in the current architecture.

## Inventory boundaries

- 42 active local user-facing skills have individual structured reviews.
- Engine procedures do not count as user-facing inventory.
- 17 upstream sources are currently registered as tracked, normative, or discovery references.
- External source breadth is reference context, not a completion metric.

## Quality model

- Source identity and individual skill quality are separate.
- Tracked upstream material is reference/design evidence unless an individual exact-version record says otherwise.
- `verified` means structured semantic review passed.
- `validated` means representative scenario/adversarial semantic review was also recorded.
- `unverified` and legacy `trusted-baseline` are not unchanged-reuse states.
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection.
- Fingerprints identify which exact text was reviewed. They are bookkeeping, not executable proof.

## User-flow state

The canonical bootstrap now provides:

- explicit route selection;
- environment/authority binding;
- minimum-relevant-evidence need discovery;
- capability definition before skill-name search;
- whole-skill and component discovery;
- exact-version reuse gating;
- explicit reuse/adapt/supplement/compose/create/no-skill decisions;
- smallest-coherent-system composition;
- host-specific artifact/handoff adaptation;
- semantic adversarial review;
- returning-user minimal refinement and `NO CHANGE NEEDED`.

## Responsibility boundary

The repository is responsible for making its instructions, metadata, provenance, and curation evidence as clear and useful as reasonably possible.

It is **not** responsible for proving that arbitrary models of different capability levels will follow those instructions successfully. Multi-model benchmarks, success-rate targets, CI, runtime tests, and executable proof are not completion requirements.

## Evaluation state

The current closeout adversarial review is recorded in `docs/evals/share-ready-semantic-review.md`.

Result: **PASS — no unresolved material repository-level ambiguity identified after closeout corrections.**

## Current mode

**CURATION MODE.**

Future work is optional and occasional:

1. discover promising sources or skills when useful;
2. determine independently whether they add meaningful value;
3. establish provenance/license/dependencies;
4. score and characterize selected skills;
5. assign a decisive semantic quality state;
6. preserve useful negative/adaptation evidence where appropriate;
7. revisit core bootstrap instructions only when real use exposes a genuine ambiguity.

There is no standing implementation backlog.
