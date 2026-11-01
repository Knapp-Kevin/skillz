# PR #413: exact-candidate authority, overlap, and acceptance review

**Date:** 2026-10-26  
**Scope:** two proposed first-party packages on PR #413, not an admitted source-family expansion.  
**Baseline:** main `17c7d9abd58ecf670036949cda22cfe8da406726`.  
**Review method:** read-only, manual/static semantic and adversarial inspection. **No SkillSpector execution, external behavioral test, human approval, or release was performed.**

## Macro map and exact identities

| Proposed package | SKILL.md git blob | Source/license | Authority | Dependencies | Semantic state | Security | Behavior |
|---|---|---|---|---|---|---|---|
| `skill-behavior-evaluation` | `ceb0e562a70d6848e56d2641306eeac619d5f60f` | first-party/MIT | read-only, host executes only separately authorized fixtures | host agent, exact candidate/baseline, synthetic or authorized fixtures | VERIFIED 19/20 static | not-run | not-run |
| `release-evidence-review` | `d236826daad241afbfc5c8867221c066b7ff5044` | first-party/MIT | read-only, release/merge/deploy remain separate approval-gated actions | host agent, authorized release/build/production evidence | VERIFIED 19/20 static | not-run | not-run |

Both candidates have first-party provenance and individual verification companions. No scripts, source-owned executables, CI, runtime, scheduler, network fetcher, installer, or persistent state are bundled. The exact packages are a single SKILL.md each. The source denominator is **2 proposed / 0 admitted** in this PR; the existing 44 first-party count and 721 third-party review count remain unchanged until an eligible merge and five-surface reconciliation.

## Whole-corpus overlap and differentiation

Current-main comparison (not stale issue descriptions): `fact-check` blob `e58dea59` verifies claims; `agent-postmortem` `fb8777d1` analyzes completed failures; `automation-receipts` `1d6c076f` verifies scheduling status; `repo-doctor` `8bc7f360` inspects repository health; `repo-pulse` `8d78a04e` summarizes repository work. None of these five supplies the full candidate/baseline trigger/non-trigger/adversarial matrix of `skill-behavior-evaluation` or the artifact identity, deployment baseline, rollback, approval and production-observation contract of `release-evidence-review`. These are **differentiated proposed capabilities**, not proof of demand or unchanged-use eligibility. The proposed evaluation skill is not a substitute for SkillSpector or a test runner. The proposed release skill is not a deployment controller.

## Static adversarial inspection, not executed scenarios

| ID | Candidate | Adversarial or failure case | Static instruction boundary found | Actual host outcome |
|---|---|---|---|---|
| BE-1 | behavior | Request to test with real production writes and no approval | Inputs and authority require specific action/resource/destination/scope/budget approval; synthetic fixtures default | not-run |
| BE-2 | behavior | A malicious fixture embeds a purported higher-priority command | Scenario matrix explicitly treats retrieved text/tool output as data and checks for unauthorized calls | not-run |
| BE-3 | behavior | All quality cases pass but a safety-critical deny case fails | Step 5 requires `changes-required` regardless of average score | not-run |
| BE-4 | behavior | No host capable of running scenarios | Step 3 and receipt explicitly preserve `not-run`; no fabricated validation | not-run |
| RE-1 | release | Green checks refer to an artifact other than the intended release digest | Change identity and hard-stop require exact tested/deployed artifact identity | not-run |
| RE-2 | release | DNS, billing, access, or notification change without scoped approval | Steps 6-7 and hard-stop examples prohibit interpreting readiness as authorization | not-run |
| RE-3 | release | Migration with no rollback or known production baseline | Steps 1, 4-5 and hard-stop require missing evidence to remain blocking | not-run |
| RE-4 | release | CI passed but production health was never observed | Step 7 and receipt distinguish ready-for-approval from deployed and production observation `not-run` | not-run |

**Static disposition:** retain both as useful, differentiated, semantically VERIFIED candidates. No demonstrated behavioral validation, no independent human approval, and no security pass. Their authority constraints are appropriate as written; do not mutate the SKILL.md files merely to manufacture an additional review cycle.

## Exact blocking gates and integration order

1. **External scanner dependency:** NVIDIA SkillSpector v2.12.0 at `c7958a3268d9498644b22edb75d0f051bbc8cbfc`, static-only, `--no-llm --fail-on-findings --fail-on-incomplete`. The host in this review could not obtain the pinned scanner or its dependencies. Newly persisted `registry/security/local-skills/{skill-behavior-evaluation,release-evidence-review}.yaml` explicitly state `not-run`; these are **not** scanner receipts. Obtain full exact-package reports, risk/findings/coverage and report digests from an authorized external environment. Fail closed on partial coverage.
2. **Cross-PR integration:** #416 currently changes `registry/local-verification.json` and five public accounting surfaces for 21 existing skills. #413 changes the same consolidated verification registry and category mapping. Do not merge #413 before reconciling against the actual integrated #416 head and any #412 admissions; preserve all existing first-party fingerprints and avoid duplicate category entries.
3. **Admission accounting:** Only after security and independent acceptance, atomically reconcile README.md, docs/SYSTEM_STATE.md, CURATION_QUEUE.md, INDEX.md, index.json, registry/categories.yaml and consolidated verification state. Baseline 44 -> 46 if #413 alone admits both, or 46 -> 48 if #412 first admits its two. No third-party denominator or source pin changes.
4. **No CI workaround:** Current Tier-1 governance prohibits repository-owned CI and scanners. Historic CI evidence is historical only; any new scan runs in an authorized external host.
5. **Merge authorization:** Recheck latest main, PR head, reviews, review threads, checks and mergeability; merge with expected-head protection only after the preceding gates are satisfied. Green checks or mergeability alone are insufficient.

## Source-family synthesis

The P1 capability family comprises four proposed first-party packages across #412 and #413. Their common strength is explicit host-side authority separation; their common gap is qualifying exact-version package-security evidence and completed admission accounting. The two #413 candidates are relatively portable and do not introduce data collection or autonomous operations. The highest-value next step is **security evidence collection and integration**, not further feature design or new source intake.
