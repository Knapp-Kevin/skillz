# Persisted exact-version review accounting: candidate-shelf reconciliation

**Date:** 2026-10-30  
**Base:** `f1cbd73525bb61d5ff268604db5854ff6cf7262f`  
**Scope:** Static file-tree accounting only; no new review, source admission, security scan, behavioral validation, or repository-owned execution.

## Recomputed exact counts

An independent recursive Git tree read found **911** `registry/verification/**/*.yaml` files and exactly **911** `registry/skills/**/*.yaml` provenance companions. The verification total breaks down into:

| Shelf | Exact-version companions |
|---|---:|
| First-party `registry/verification/local-skills/` | 44 |
| Third-party registered/tracked source shelves excluding candidate-only subtrees | 746 |
| Microsoft candidate-only `microsoft-skills-candidate/` | 102 |
| Matt Pocock candidate-only `mattpocock-skills-candidate/` | 19 |
| **Persisted third-party total** | **867** |
| **All persisted verification companions** | **911** |

The public count of **848 third-party / 892 total** omitted the 19 existing Matt Pocock candidate-only exact-version records while including the 102 Microsoft candidate-only records. This was a count-definition inconsistency, not 19 new reviews. All 19 Matt candidate records are explicitly `source_role: unadmitted-upstream-freshness-candidate` at candidate revision `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa`; the registered pin remains `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.

## Interpretation and controls

**Persisted evidence is not admitted inventory.** The 121 candidate-only records count toward persisted exact-version review evidence, but do not increase the registered source-family denominators, source pins, eligible unchanged-use corpus, first-party skills, or source identities. A candidate `verified` semantic record is not a package-security pass or behavioral validation. No candidate pin was promoted.

Current source-family coverage, including David Ondrej 55/55, AWS 94/94, and Microsoft registered 186/186, is unchanged. Public snapshot counts are now **44 first-party / 867 third-party / 911 total**. Older dated tranche snapshots remain historical, while the live front-door counters and index summary use the recomputed values. The five public accounting surfaces were updated together.

**Lifecycle:** Seven open issues and five qualification-held draft PRs remain unchanged. No issue/PR was closed, merged, or opened by this accounting-only correction other than its own bounded PR. The 36 changed first-party repair trees still require external pinned SkillSpector v2.12.0 and independent adversarial evidence before merge.

**Next action:** Qualify the 36 first-party repair package trees in an authorized external host; reconcile shared registry and merge only qualified work.
