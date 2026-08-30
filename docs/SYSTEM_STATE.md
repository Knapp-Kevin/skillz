# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-31 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **Persisted third-party review companions** | 120 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
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
├── skills/                           43 first-party user-facing skill packages
│   ├── categories/                   human browse-by-purpose navigation
│   └── sources/                      12 intact exact-revision third-party corpora
├── .gitmodules                       exact source gitlink locations
├── engine/skills/                    passive repository-use/curation procedures
├── registry/
│   ├── sources.yaml                  19 unique source identities/roles/pins
│   ├── source-signals.yaml           volatile source-level context
│   ├── skills/                       mandatory per-skill provenance companions
│   ├── verification/                 exact-version semantic review companions
│   ├── local-verification.json       first-party structured reviews
│   ├── categories.yaml               canonical first-party category assignments
│   └── taxonomy.yaml                 controlled metadata vocabulary
└── docs/                             governance, provenance, curation, evidence, history
```

The canonical physical boundary is reflected in the live tree: user-facing first-party material is under `skills/`, intact pinned third-party corpora are under `skills/sources/<source-id>/`, and repository-use/curation instructions are under `engine/skills/` and excluded from user-facing counts.

There is no repository-owned runtime, root scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service.

Pinned third-party repositories may contain their own code or tooling. They remain intact reference sources and are not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party user-facing skills** have structured semantic review records and **43/43 first-party provenance companions** under `registry/skills/local-skills/` after the `automation-receipts` admission via issue #72.
- `automation-receipts` is classified under Agent Operations & Security in `registry/categories.yaml`; first-party category accounting therefore matches the 43-skill denominator.
- **12 pinned external corpora** provide the broad 500+ reference surface.
- **120 current exact-version third-party verification companion files** are persisted.
- `registry/sources.yaml` contains **19 unique source identities** after removing duplicate entries for `openclaw-agent-skills` and `archieindian-superpowers`. Source counts refer to unique IDs, not YAML row accidents.
- AWS Agent Toolkit has an established eligible denominator of **72** skills and a prior full-pass disposition of **70 verified / 2 rejected**; **20/72** currently have persisted exact-version provenance + verification companion pairs on `main`. The remaining 52 are evidence-reconciliation gaps, not unreviewed-by-definition skills.
- Historical source-level curation records document broader review work across multiple corpora; one-file companion reconciliation remains an explicit curation lane where needed.
- `engine/skills/` procedures do not count as user-facing inventory.

## Source lifecycle

The repository distinguishes:

**discovery surface → candidate issue/source → source-vetting → admitted corpus/reference/tracked source → individual exact-version review → user-fit decision**

Newly discovered third-party candidates use the issue-first intake workflow before admission. The candidate issue is the pre-admission evidence workspace; finalized provenance and verification companions are persisted only after an admission decision is justified.

Intentional discovery surfaces are documented in `docs/discovery-surfaces.md`. The connected Creator Technical Resource Catalog is discovery intelligence only; its rows, scores, verification labels, creator attributions, and recommendations are not `skillz` provenance or individual quality evidence.

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

## Current drift and reconciliation

The current first-party `skills/README.md` has been corrected to remove a stale claim that a repository-owned Node verification script enforces readiness. Completeness is instead checked by the external host agent against the passive review/provenance records.

The Tier-4 governance contract still names `INDEX.md` and `index.json` as passive catalog snapshots, but both files are currently absent from `main`. This is a live catalog-surface gap. Restore them as hand-maintained static snapshots only; do not reintroduce a generator, preflight, or executable refresh path.

## Current curation priority

1. Restore/reconcile `INDEX.md` and `index.json` as passive static catalog snapshots so Tier-4 governance matches the live tree.
2. Continue AWS Agent Toolkit current-standard companion reconciliation, preserving the prior 72/72 review evidence and re-reviewing only genuine evidence gaps.
3. Complete Microsoft Skills.
4. Complete Microsoft Azure Skills.
5. Continue remaining admitted creator/registered-source curation.
6. Continue governed discovery/source-vetting in parallel when evidence supports useful source candidates.
7. Keep README, governance, category navigation, source registry, catalog snapshots, and public counts aligned with material corpus changes.

The current living work surface is `CURATION_QUEUE.md` plus open provenance audit issue #66. Closed historical Wayfinder/issues/PRs remain evidence, not active execution plans.
