# Operations replacement capability-regression remediation

Date: 2026-11-18. Issue #738.
Branch: `fix/738-operations-repo-parity`.

## Scope and rights

Independent functional-outcome comparison against retained historical
`skills/task-surface/SKILL.md` and `skills/repo-doctor/SKILL.md`,
plus the existing authored v1.0 content. Historic authorship and rights
remain unresolved: retained comparator skills are only evaluation
evidence. New v1.1 instructions and fixture cases are separately authored
and MIT-covered by their own existing LICENSE files. No original source
was deleted or copied as part of this remediation.

## Complete package identity (Git object identities)

All packages contain SKILL.md, LICENSE and examples/acceptance.md.
Tree IDs were computed using Git tree serialization of the exact recorded
blobs; the same algorithm reproduced both previously governed v1.0 trees.

| Skill | SKILL blob | Fixture blob | LICENSE blob | Complete package tree |
| --- | --- | --- | --- | --- |
| personal-operations-control-board v1.1 | `6ec82d3e34e2bd5adea16838d9ba49955106b893` | `1d909279525f353d7d5a9204207b3a1fcb4f6a14` | `023abdb34298b27580d1d303084aca942050585e` | `9ab584fac422cbaaea81d12fdc832945c9661bf4` |
| repository-delivery-assessor v1.1 | `8f142859fac2420657377453f5b531d80c31dbb4` | `2fd511c67a50f730adfd945353c332f6b1ee2189` | `023abdb34298b27580d1d303084aca942050585e` | `d77f373e2825c2eee23cfe60937afc83a547e778` |

## Outcome-level findings

**Coordination board:** v1.0 covered prioritization, inbox triage and
proposed task updates but did not provide an end-to-end option for
designing an authorized coordination workspace, specifying its rules,
preparing a complete create/establish operation, and verifying readback.
v1.1 restores this separately bounded mode; the pointer-to-canonical
design avoids duplicative sources of truth and introduces explicit
privacy/permission controls at each write.

**Repository delivery assessor:** v1.0 focused on roadmap and release
readiness but did not require a one-shot repository maintenance diagnostic
with TODO/FIXME baseline trend, README/license checks, dependency
staleness distinctions or executable repair guidance. v1.1 adds a
specific diagnostics matrix, evidence-completeness states, and a
repair ledger that distinguishes a safely proposed exact command from
an unverified or unsafe command.

## Static structured review

Reviewer: ChatGPT maintainer session, manual examination of the changed
SKILL.md packages, fixture cases and MIT license, plus direct functional
comparison with retained legacy sources. No executable test, scanner,
real account operation, host-agent challenge or behavioral pairwise run.

Scores use the ten dimensions of `docs/skill-verification.md`
(trigger/procedure/authority/failure/evidence/dependency/portability/
usefulness/adversarial/effectiveness design). No hard-fail finding
was identified at source level.

| Package | Dimensions (each out of 2) | Static score | Qualification |
| --- | --- | --- | --- |
| Coordination board v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | verified static, host not run |
| Repository assessor v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | verified static, host not run |

Portability remains constrained by actual host APIs and safe local
repository inspection; effectiveness is design-only. A submitted
workspace creation plan is not a created repo; a proposed repair
command is not a performed fix. A candidate tool command cannot be
constructed by directly running or interpolating untrusted issue text.

## Open acceptance obligations

- No actual external-host creation of a coordination repository was
  performed. All task-write, privacy and source readback cases remain
  synthetic acceptance specifications.
- No local git command or untrusted repository configuration was run.
- No observed paired comparison of legacy versus v1.1 was conducted.
- The 1.5x effectiveness target remains **NOT_PROVEN**, even though
  specific source-level functional omissions have been addressed.
- Validate exact-head index/companions and integration at merge time.
  Retain all historical comparator files and their source evidence.

Disposition: **SOURCE PACKAGE STATIC VERIFIED**, behavior **NOT_RUN**.
