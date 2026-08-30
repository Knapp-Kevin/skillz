# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-31 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 42 |
| **Persisted third-party review companions** | 120 |
| **Pinned external corpora** | 12 |
| **Registered sources** | 17 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

```text
skillz/
├── README.md
├── AGENT_START_HERE.md
├── BOOTSTRAP.md
├── AGENTS.md
├── CURATED.md
├── CURATION_QUEUE.md                 living curation evidence ledger
├── skills/                           first-party user-facing skill packages
│   ├── categories/                   human browse-by-purpose navigation
│   └── sources/                      12 intact exact-revision third-party corpora
├── .gitmodules                       exact source gitlink locations
├── engine/skills/                    passive repository-use/curation procedures
├── registry/
│   ├── sources.yaml                  source roles, paths, licenses, exact pins
│   ├── source-signals.yaml           volatile source-level context
│   ├── skills/                       mandatory per-skill provenance companions
│   ├── verification/                 exact-version semantic review companions
│   ├── local-verification.json       first-party structured reviews
│   └── taxonomy.yaml                 controlled metadata vocabulary
└── docs/                             governance, provenance, curation, evidence, history
```

The canonical physical boundary is now reflected in the live tree: user-facing first-party material is under `skills/`, intact pinned third-party corpora are under `skills/sources/<source-id>/`, and repository-use/curation instructions are under `engine/skills/` and excluded from user-facing counts.

There is no repository-owned runtime, root scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service.

Pinned third-party repositories may contain their own code or tooling. They remain intact reference sources and are not repository-owned execution machinery.

## Inventory boundaries

- 42 active first-party user-facing skills have individual structured semantic reviews.
- Under the mandatory provenance contract, those semantic reviews do not substitute for provenance companions. The active provenance audit recorded a 0/42 standalone first-party gap, reconciled 2026-08-30: **42/42 first-party provenance companions** now exist under `registry/skills/local-skills/`, authored from repository history and current review evidence, not inferred history.
- 12 pinned external corpora provide the broad 500+ reference surface.
- 120 current exact-version third-party verification companion files are persisted.
- AWS Agent Toolkit has an established eligible denominator of 72 skills and a prior full-pass disposition of 70 verified / 2 rejected; **20/72** currently have persisted exact-version provenance + verification companion pairs on `main`. The latest reconciliation is `finding-data-lake-assets`, bound to package tree SHA `e32f6445e9f80e2dca0bfe14ecf5e7ad53ac2721` at the registered AWS pin, with decisive current state `verified` at 17/20 and behavioral evidence `not-run`. The remaining companion closure is active evidence reconciliation work, not evidence that prior review disappeared.
- Historical source-level curation records document broader review work across multiple corpora; one-file companion reconciliation remains an explicit curation lane where needed.
- `engine/skills/` procedures do not count as user-facing inventory.
- 17 upstream sources are registered across pinned reference, tracked corpus, normative, and discovery roles.

## Source lifecycle

The repository distinguishes:

**discovery surface → candidate issue/source → source-vetting → admitted corpus/reference/tracked source → individual exact-version review → user-fit decision**

Newly discovered third-party candidates use the issue-first intake workflow before admission. The candidate issue is the pre-admission evidence workspace; finalized provenance and verification companions are persisted only after an admission decision is justified.

Intentional discovery surfaces are documented in `docs/discovery-surfaces.md`. The connected Creator Technical Resource Catalog is discovery intelligence only; its rows, scores, or verification labels are not `skillz` provenance or individual quality evidence.

Discovery does not grant trust, quality, redistribution authority, installation authority, or automatic admission. Source popularity, official branding, repository age, stars, forks, and activity are source context only and do not prove individual skill quality.

## Quality model

- Source identity and individual skill quality are separate.
- Every governed user-facing skill must have truthful provenance and applicable exact-version review evidence before the corpus can describe it as companion-complete.
- Pinned/tracked material is reference/design evidence unless an exact-version record establishes stronger eligibility.
- `verified` means structured semantic review passed for the exact bound material.
- `validated` means representative external scenario/adversarial evidence was also recorded.
- `unverified` and legacy `trusted-baseline` are not unchanged-reuse states.
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection.
- Fingerprints identify reviewed material. They are provenance/bookkeeping evidence, not executable proof.
- Static source completion requires an exact eligible denominator and a decisive current state for every in-scope skill.

Interpret candidates in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

The host agent may ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, use a CHECKLIST, keep behavior DYNAMIC, or make NO CHANGE.

## Responsibility boundary

`skillz` is responsible for the clarity and usefulness of its skills, procedures, source material, provenance, metadata, exact-version review evidence, safeguards, negative examples, and documentation.

The external host agent is responsible for active work such as browsing, discovery, evaluation, installation, file mutation, external actions, and any behavioral validation, subject to the user's authority and the host environment's capabilities.

Static corpus completion comes before broad behavioral validation. `skillz` owns no evaluator, benchmark, test harness, scenario runner, or behavioral-validation runtime. Later external behavioral evidence may be stored passively in the repository when it is useful.

## Current curation priority

1. Finish AWS Agent Toolkit current-standard companion reconciliation, preserving the prior 72/72 review evidence and re-reviewing only genuine evidence gaps.
2. First-party provenance reconciliation (42/42) is complete; remaining audit work is third-party companion closure (AWS and later sources).
3. Complete Microsoft Skills.
4. Complete Microsoft Azure Skills.
5. Continue remaining admitted creator/registered-source curation.
6. Continue governed discovery/source-vetting in parallel when evidence supports useful source candidates.
7. Keep README, governance, catalog snapshots, source registry, and public counts aligned with material corpus changes.

The current living work surface is `CURATION_QUEUE.md` plus open provenance audit issue #66. Closed historical Wayfinder/issues/PRs remain evidence, not active execution plans.
