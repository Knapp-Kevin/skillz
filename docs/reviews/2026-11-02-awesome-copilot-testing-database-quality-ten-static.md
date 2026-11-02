# Awesome Copilot testing and database-quality: ten exact-package static candidate reviews

**Date:** 2026-11-02. **Source:** `github/awesome-copilot` pinned at `f11a4e441c5ff061b4f8ae37952be8c602e4034e`. **Source role:** dynamic discovery only. **Root license:** MIT (pinned `LICENSE` blob `89bc5e962c9944cdb050887062afdaaf89be504a`), without relicensing dependencies or third-party code.

## Macro map and denominator

The pinned source has **432 raw SKILL.md paths**, 415 direct and 17 nested/internal. Prior to this tranche, **59** exact-path terminal candidate decisions existed (42 direct, 17 nested). Ten previously undecided direct-shape packages were selected by their testing, QA, SQL review and database-migration capability rather than publisher preference. Each was fetched at the exact pin, read in full, and verified as a **single-file Git package** by matching the independently recomputed Git tree SHA-1 of its sole `100644 SKILL.md` entry to the pinned package tree. All ten exact SKILL blobs matched their manifest entries. No required bundled references/scripts/assets were omitted; no upstream code executed.

**Tranche: 10 individual records, 2 REFERENCE-ONLY and 8 REJECT unchanged, scores 6–15/20.** All ten have individual rubric dimensions, exact identity, rights/dependency context, authority/privacy findings, controlled tags, rationale, and explicit `security_scan: not-run` and `behavioral_validation: not-run`. The [graded ledger](../../registry/discovery/github-awesome-copilot-testing-quality-ten-static-20261102.json) is the auditable source of individual judgments. None is a governed exact-version verification pair or admission.

## Systemic findings

1. **Execution/authority conflation.** `playwright-generate-test` directs test-file writes and execution without scoped approval. `pytest-coverage` prescribes unbounded repeated test changes until 100% line coverage. Neither respects a separate mutation/target boundary.
2. **Third-party remote egress.** `scoutqa-test` launches remote exploratory QA proactively and includes a plaintext credential-bearing follow-up example. It lacks a bounded authorization contract for the tested site, remote transmission, duration/cost and termination.
3. **Version-claim correctness.** `react19-test-patterns` claims StrictMode effects no longer receive the development double-invocation behavior and recommends a blanket spy-count rewrite. This is not a safe migration invariant. `csharp-mstest` retains useful patterns but mixes version-specific API claims that require actual target-version compilation.
4. **SQL correctness and tenant safety.** `sql-code-review` labels a MySQL-style `PREPARE` example as PostgreSQL/MySQL and proposes numeric security/performance scores without measured evidence. `postgresql-code-review` pairs a JSONB expression GIN index with an unrelated containment predicate and demonstrates RLS based on a mutable session setting without an authenticated identity-binding contract.
5. **Oracle migration authority.** Three related skills provide a coherent plan → scaffold → baseline test method. The scaffold/test steps assume rollback protects shared Oracle data, while lacking explicit isolated test DB and secret-store rules. The planning skill is useful as reference, but its hardcoded repository report path is not a general write authorization.
6. **Overlap and taxonomy.** SQL review and PostgreSQL review overlap, but remain distinct exact packages; Oracle planning, scaffolding and test creation are complementary stages. Existing controlled use-case tags are used without creating a database-specific domain. Narrow candidate capability paths are provisional and are not governed directory admission.

## Accounting and lifecycle

- Awesome Copilot terminal exact-path candidate decisions: **59 → 69 / 432**; direct **42 → 52 / 415**; nested **17 → 17 / 17**; remaining undecided direct **373 → 363**.
- Four-source path-matched terminal candidate decisions: **100 → 110 / 4,813 raw paths**. Other-source figures unchanged: j4flmao 41/645, OpenAI 169 plugin-family decisions not path-matched, AgentSkillExchange 0 path-matched.
- Governed exact-version review population **1,039**, registered source identities **25**, admitted denominator delta **0**, security scans **0**, behavioral validations **0**.
- Distinct eligible cross-source denominator remains **unknown**, because mirrors, rights and semantic overlaps are not fully reconciled.
- All public accounting surfaces must be updated together before merge: README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json. Source manifests, path-level progress and capability directory must distinguish source-vetted evidence from governed reviewed examples.
- No new runtime, CI, scripts, scanners, schedulers or other executable machinery. All review activity occurred in the external host.

## Next frontier

Continue source-neutral capability review of the remaining 363 Awesome Copilot direct paths, with priority to underrepresented non-engineering domains and cross-source overlap/rights checks. Separately, [draft #590](https://github.com/Knapp-Kevin/skillz/pull/590) remains a conflicting, broad capability-crosswalk lane requiring independent reconciliation. Do not merge it merely because this bounded source-vetting tranche completes.
