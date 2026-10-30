# Addy Osmani: second ten-package pinned authority macro review

**Review date:** 2026-10-30  
**Registered source:** https://github.com/addyosmani/agent-skills at `f63ec56a3cc936408d792956ae583c3c96a825bd` (MIT)  
**Canonical eligible denominator:** 24 first-class `skills/<name>/SKILL.md` packages; 24/24 existing exact-version companion pairs, zero static gaps. The pinned source is retained intact; this is a recheck of prior approvals, not a new admission or validation.

## Whole-frontier map and disjoint tranche

The preceding [ten-package high-authority review](2026-10-29-addyosmani-ten-authority-macro.md) covered CI/CD, Git, migration, shipping, security, browser tooling, observability, performance, source-driven development and routing, with two rejections corrected. This disjoint tranche examined ten further exact pinned packages: `api-and-interface-design`, `code-review-and-quality`, `debugging-and-error-recovery`, `documentation-and-adrs`, `frontend-ui-engineering`, `incremental-implementation`, `interview-me`, `planning-and-task-breakdown`, `spec-driven-development`, and `test-driven-development`. Four lower-authority packages remain outside these two deeper tranches: `code-simplification`, `context-engineering`, `doubt-driven-development`, and `idea-refine`.

All ten manifest blob identities were compared to the pinned upstream tree and their existing individual verification records. No alias, mirror, nested first-class manifest or duplicate exposure was found in this bounded source map. Shared dependencies are the intact source-level `references/` material, repository-specific test/build tools and optional external issue trackers; these are not repository-owned runtime. The common strengths are small verified changes, source validation, quality gates, human-readable planning and untrusted-data handling. The principal risk cluster is *turning engineering advice into unapproved durable writes or operational actions*.

## Two decisive corrections

| Skill | Exact SKILL.md Git blob | Before | After | Hard-fail reason |
|---|---|---|---|---|
| `debugging-and-error-recovery` | `03775802b244cddf2f58f6c54039f6e6ee8702f2` | VERIFIED semantic only 17/20 | **REJECT unchanged 14/20** | The non-reproducible incident path directs load/concurrency runs, added logging and persistent error alerts without authorization for production traffic, private logs/telemetry, notification recipients, retention or cost. Bisect and dependency-install steps also change local state without a bound workspace. |
| `incremental-implementation` | `6df12f9a878c80305c42bcdbe8a43a10d2e0c933` | VERIFIED semantic only 17/20 | **REJECT unchanged 15/20** | Its required slice loop commits every increment and its feature-flag guidance proposes merging incomplete work to main, without an explicit approval boundary for repository, branch, staging, commit or merge. |

Both retain exact-version provenance, individual rubric, controlled authority tags, dependencies and `validation_status: not-run`. Their unchanged upstream packages remain useful for **ADAPT / EXTRACT / CHECKLIST**. A host adaptation should make diagnosis read-only by default, bind any live environment/log access and notification recipients before monitoring changes, and separate implementation from approval to commit, push or merge.

## Eight reviewed without a changed disposition

- `api-and-interface-design`: VERIFIED 19/20; design examples, not an instruction to mutate live APIs.
- `code-review-and-quality`: VERIFIED 18/20; review/checklist guidance, not automatic merge authorization.
- `documentation-and-adrs`: VERIFIED 19/20; documentation templates; no external publication default.
- `frontend-ui-engineering`: VERIFIED 16/20; code-writing remains bounded by an actual implementation request.
- `interview-me`: REJECT 13/20 already; host-specific conversational process and optional file persistence.
- `planning-and-task-breakdown`: REJECT 14/20 already; rigid artifact conventions plus external-tracker item creation from project-agent rules. Existing rejection already prevents unchanged reuse.
- `spec-driven-development`: VERIFIED 17/20; spec and implementation sequencing, with explicit ask-first constraints for consequential project changes.
- `test-driven-development`: VERIFIED 18/20; test sizes describe resource models; actual external test execution remains subject to host authority. Browser output is treated as untrusted.

## Macro synthesis and accounting

The two newly corrected approvals show that **local engineering intent does not silently authorize persistent repository lifecycle actions or production diagnostics**. A branch commit, main merge, pager alert, live load reproduction or private-log read needs its own scoped authorization. This is distinct from a benign recommendation to test, write a plan or design a rollback.

**Tranche:** 10 inspected / 2 VERIFIED to REJECT unchanged / 8 retained. Combined two-tranche deep-review coverage is 20/24; four remain for later lower-risk recheck. Admitted denominator 24/24 to 24/24, zero static gaps; 44 first-party, 826 third-party semantic companions, 870 total unchanged. No source pin, package content, license, discovery admission, security status or behavioral validation changed. No scripts, tests, CI, scanners, monitors, schedulers or repository-owned execution surfaces added.

**Lifecycle:** The five existing draft PRs #412, #413, #489, #492 and #496 remain gated on their separate exact-package security and independent behavioral/adversarial acceptance. The 36 distinct changed first-party trees in the last three drafts cannot inherit historical matching-pass evidence. No ready authorized PR was left unmerged in this review.

**Next action:** Qualify the 36 exact final first-party package trees with pinned external SkillSpector v2.12.0 full reports/digests and independent host-executed adversarial evidence, then reconcile the shared first-party registry and merge qualified repairs.
