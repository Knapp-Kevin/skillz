# Vercel Agent Skills: exact-pin optimize authority macro review (2026-10-29)

## Live scope and denominator

Registered source `vercel-labs/agent-skills`, MIT source context, exact pinned gitlink `f8a72b9603728bb92a217a879b7e62e43ad76c81`. The upstream pinned tree contains exactly nine first-class `skills/*/SKILL.md` entry points. All nine already have matching individual provenance and exact-version semantic companions; **9/9 current-standard complete, zero genuine static gaps, zero new source exposure or denominator delta**. This review read the nine pinned manifests and existing dispositions, plus `vercel-optimize`'s bundled data-collection and Observability Plus guidance and collector. Existing `deploy-to-vercel` correction is retained, not double-counted.

| Package | Exact pinned SKILL.md blob | Current static disposition |
|---|---|---|
| composition-patterns | d07025bf943345bc1cf15eb923594f889ff881f0 | VERIFIED semantic only |
| deploy-to-vercel | a0251ce89a7636230be9c5b989a81e1a54a52a96 | REJECT unchanged (prior authority review) |
| react-best-practices | 237988de4a66dd8a71d30a2c24ebe1a86b58d04e | VERIFIED semantic only |
| react-native-skills | 73401865dd7440a43c5243b107a3763e0d2f4aae | VERIFIED semantic only |
| react-view-transitions | dcecd8e3f356c73f340676cfcefb33539435e987 | VERIFIED semantic only |
| vercel-cli-with-tokens | 814423d0c40f56853e0f4f2f64d03a02266dadf4 | REJECT unchanged (secret handling) |
| vercel-optimize | c8a6d6d7075b2cc3f7921da89de86e6926f78985 | **REJECT unchanged (this review)** |
| web-design-guidelines | ceae92ab319216a68274168fba9b63b998b65997 | REJECT unchanged (unpinned remote rules) |
| writing-guidelines | 63facf310252a990d154bed12b3dcdd295ba771a | REJECT unchanged (unpinned remote rules) |

## Macro findings

The nine-package family clusters into four capability lanes: React/Native design references (four verified), deployment and account operations (deploy rejected), credential-bearing Vercel CLI operations (rejected), and remote guideline retrieval (two rejected). The optimization workflow is the remaining high-authority outlier. Shared upstream tooling is source-owned, **not repository-owned runtime**. There is no demonstrated alias, symlink, or duplicate first-class exposure in the pinned nine-entry denominator. No new admission or discovery decision was made. Semantic review and security/behavioral execution remain separate.

The family offers strong differentiated methods in deterministic metric gates, version-aware citations, candidate-bounded source inspection, React performance patterns and precise deployment state detection. Recurring weaknesses are action authorization, private account data minimization, credential exposure and mutable external instructions. Do not generalize the rejection to the four lower-authority reference packages without individual evidence.

## Deep review: vercel-optimize

- **Exact identity:** pinned manifest `skills/vercel-optimize/SKILL.md` blob `c8a6d6d7075b2cc3f7921da89de86e6926f78985`; the existing provenance and verification companions match. Bundled `scripts/collect-signals.mjs`, `references/data-collection.md`, `references/observability-plus.md`, libraries, tests and rules are source-owned package dependencies. Vercel CLI v53+, authenticated Vercel account, Node 20+ and optionally Observability Plus are operational dependencies. Portability remains low.
- **Authorization hard fail:** the `not_linked` and project/scope recovery instructions tell the host to execute `vercel link --yes` once a project/team is identified. This writes persistent worktree/project linkage without a separate action-specific authorization gate. Confirming the project identity or team is parameter resolution, not authorization to link it.
- **Private data scope:** the source-owned collector obtains account plan, contract, usage/billing and route metrics for the linked account. It checks identity/scope technically but does not require approval for the exact private billing/usage fields to read or retain. Raw account/project signals are written into a newly created temp run directory with no explicit data minimization, retention or disposal boundary. Authentication is not authorization to collect or retain everything accessible.
- **Internal sequencing defect:** the SKILL.md says not to inspect source until `signals.json` exists, but its pipeline runs `scan-codebase.mjs` before `merge-signals.mjs` creates `signals.json`. This weakens its claimed candidate-bound inspection discipline; it is not proof of an executed disclosure.
- **Existing safeguards retained as prior art:** scope matching, Observability Plus blocker prompts, opt-in degraded audits, bounded candidate gates, citation/version checks, report sanitizers, non-echoing token guidance and recommendation verification. Those do not repair the separate missing action-authorization boundaries.

**Decision:** REJECT unchanged, static rubric **15/20** (trigger 2, procedure 2, authority 0, failure 1, evidence 2, dependencies 2, portability 1, usefulness 2, adversarial resilience 1, effectiveness 2). Appropriate host outcomes are ADAPT, EXTRACT or CHECKLIST. Require approval for exact project/account, private billing/usage/metric fields, retention/deletion, and persistent linkage before any active operation. In a read-only audit, report the link requirement instead of silently linking. Treat private raw signals as protected evidence and minimize/dispose under the approved retention policy.

## Accounting and lifecycle

Vercel **5 VERIFIED / 4 REJECT → 4 VERIFIED / 5 REJECT**, denominator **9/9 → 9/9**, static gaps **0 → 0**. Existing package trees, upstream pin, other eight dispositions, controlled tags, published **44 first-party / 826 third-party reviews / 870 total** and discovery/source-vetting state remain unchanged. Only the target provenance and verification companions, this review and five public accounting surfaces are updated. `validation_status: not-run` remains truthful. **No pinned SkillSpector scan or executed adversarial validation was performed.** Existing first-party repair drafts #489/#492/#496 and admission drafts #412/#413 are disjoint and remain qualification holds; this review neither approves nor merges them.
