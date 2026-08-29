# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-29 |
| **Milestone** | Core implementation complete |
| **State** | Governed curation mode |
| **Repository type** | Passive instruction/reference repository |
| **Evaluation model** | Semantic + adversarial probabilistic review |
| **CI requirement** | None |

## Current architecture

```text
skillz/
├── README.md                         human front door + passive boundary
├── AGENT_START_HERE.md               single agent routing entry
├── BOOTSTRAP.md                      human-readable first/returning workflow
├── AGENTS.md                         repository-wide agent contract
├── skills/                           local user-facing skills
│   └── categories/                   human browse-by-purpose navigation
├── engine/skills/
│   ├── skill-bootstrap/              canonical normal user-flow instructions
│   └── ...                           optional repository-maintenance helpers
├── vendor/                           third-party reference corpora
├── registry/
│   ├── sources.yaml                  source identity/role/license
│   ├── skills/                       third-party provenance companions
│   ├── verification/                 exact-version semantic quality records
│   ├── local-verification.json       first-party individual reviews
│   └── taxonomy.yaml                 controlled metadata vocabulary
├── docs/evals/                       semantic/adversarial review records
└── INDEX.md / index.json             browse/index snapshots
```

## Inventory boundaries

- **42 active local user-facing skills** are individually reviewed in `registry/local-verification.json`.
- **7 engine skills** are repository/bootstrap machinery and do not count as user-facing inventory.
- **17 registered sources** currently provide vendored, tracked, normative, or discovery material.
- The broader reference corpus remains **500+** skills/patterns. Exact breadth can change as curation evolves and is not a completion gate.

## Quality model

- Source identity and individual skill quality are separate concepts.
- Broad source material is reference/design evidence unless an individual skill has a governed exact-version record.
- `verified` means structured semantic review passed.
- `validated` means a verified exact version also received representative scenario/adversarial semantic review.
- `unverified` and legacy `trusted-baseline` are not unchanged-reuse states.
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection.
- Fingerprints identify which exact text was reviewed; they are bookkeeping, not executable proof.

## User experience state

### First visit

Implemented:

- immediate route from repository link into bootstrap;
- environment/authority binding;
- minimum-relevant-evidence need discovery;
- capability definition before skill-name search;
- whole-skill and component discovery;
- governed unchanged-reuse gate;
- ADOPT/ADAPT/SUPPLEMENT/COMPOSE/CREATE/no-skill decision vocabulary;
- component ledger and baggage removal;
- smallest-coherent-system composition;
- host-specific artifact/handoff adaptation;
- semantic adversarial review;
- explicit installation/handoff state.

### Returning user

Implemented:

- starts from the existing fitted system;
- preserves still-valid custom behavior;
- limits work to materially affected capabilities;
- prefers the smallest justified change;
- explicitly permits `NO CHANGE NEEDED`.

## Repository-maintenance boundary

Optional scripts and engine helpers may assist maintainers with indexing, metadata, source inspection, or file operations. They are not a runtime, not CI, and not evidence that the semantic instruction architecture is correct.

No user-flow or repository-completion criterion depends on executing them.

## Evaluation state

The current semantic adversarial review is recorded in:

`docs/evals/share-ready-semantic-review.md`

Result: **PASS — no unresolved material repository-level ambiguity identified after closeout corrections.**

The review specifically challenged:

- user work versus repository maintenance confusion;
- filename-first selection;
- famous-source trust shortcuts;
- whole-skill-only reasoning;
- component-governance loopholes;
- endless evidence/search expansion;
- host-format assumptions;
- false executable-proof language;
- returning-user churn;
- constrained read-only/connector use;
- minimal refinement and true no-op outcomes.

## Current mode

**CURATION MODE.**

Normal work from this point forward is:

1. discover promising sources or skills occasionally;
2. independently decide whether they add meaningful value;
3. establish provenance/license/dependencies;
4. score and characterize admitted skills;
5. assign a decisive semantic quality state;
6. retain unsuitable material only as clearly bounded reference/negative evidence when useful;
7. revisit core bootstrap instructions only when real feedback or repeated semantic review exposes an architectural ambiguity.

More skills broaden the ecosystem. They do not reopen core implementation.