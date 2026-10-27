# Microsoft Skills: candidate canonical denominator and ungoverned exposures

**Observed:** 2026-10-27. **Registered July pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`. **Candidate main:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Method:** full non-truncated upstream Git trees, existing registered crosswalk and review ledgers, exact manifest and package-tree SHA comparisons, and targeted static reading. No scripts, scanners, cloud operations or behavioral tests were run.

## Macro map and exact candidate denominator

| Partition | Exact count | Meaning |
|---|---:|---|
| July physical manifests | 192 | 186 governed canonical paths + 6 ungoverned physical paths |
| Governed carry-forwards | 106 | Exact package-tree identity retained |
| Governed changed-existing | 76 | Frozen screening is 76/76, **not** complete requalification |
| Governed removals | 4 | Absent at candidate; no successor equivalence established |
| Old ungoverned distinct packages | 5 | Six physical paths less one exact four-blob mirror |
| New physical additions | 24 | 21 first-class, three non-frontmattered App Onboard phase references |
| Candidate physical `SKILL.md` paths | 212 | Non-truncated upstream Git tree |
| Candidate structurally eligible packages | **208** | 212 physical less 3 non-first-class phase references less 1 exact-tree mirror |

Independent arithmetic: **106 carry-forward + 76 changed + 5 old ungoverned + 21 newly first-class = 208**. The latest source family therefore has **102 candidate packages requiring new current-standard exact-version qualification** (76 changed + 26 new/previously ungoverned), even though preliminary screening exists for many. Four removed governed identities require separate retirement/successor decisions. The registered July pin stays **186/186** current-standard and its historical evidence remains valid. No source-pin promotion is justified.

This is a **structural candidate denominator** based on physical frontmatter and exact package-tree identities, not proof of eligibility for unchanged use. The nested `slack-to-teams` is a separately frontmattered first-class skill with shared parent dependencies. The three `azure-app-onboard/{deploy,prepare,scaffold}/SKILL.md` files have no YAML frontmatter and explicitly route through the parent, so they are not independently eligible. Nested Foundry and AKS manifests with their own frontmatter remain separate packages. The two `applicationinsights-web-ts` exposure paths are byte-identical four-blob package trees and count once. The root and Azure-plugin `entra-agent-id` manifests and package trees differ, so they are **two distinct versioned exposures**, requiring disambiguated routing rather than silent aliasing.

## Six historically ungoverned July exposure paths

| Exposure | Exact structural disposition | Authority/privacy and qualification decision |
|---|---|---|
| `.github/plugins/azure-sdk-typescript/skills/applicationinsights-web-ts` | **EXACT MIRROR, exclude duplicate** | Same tree `cb03b364` as canonical `.github/skills/applicationinsights-web-ts`; browser telemetry consent still applies |
| `entra-app-registration` | **REJECT unchanged; extract** | Entra app, Graph permissions (including `Mail.Send`) and credential creation lack distinct tenant/owner authorization; 17 source-owned blobs, full review incomplete |
| `slack-to-teams` | **REFERENCE-ONLY pending full shared-package review** | Separate nested frontmatter and use-case boundary; parent-linked 100+ experts, cross-platform message/identity/file authority and tenant consent unresolved |
| `continual-learning` | **REJECT unchanged; extract** | Automatic hook install and global/local persistent learning capture lack explicit installation, privacy, retention and user authorization |
| `debugview` | **REJECT unchanged; extract** | Authenticode verification and bounded capture are useful, but kernel/boot/remote logging and driver installation lack scoped authority and sensitive-log controls |
| root `entra-agent-id` | **REJECT unchanged; extract** | Different four-blob beta-API package from seven-blob Azure plugin; identity creation, admin consent and deletion lack action-specific authorization |

These are **preliminary static authority dispositions**, not new `registry/verification` companions. Individual exact manifest SHA, package-tree SHA, dependencies, controlled tags, privacy and authority findings, honest unscored review state, and behavioral/security `not-run` are in [the structured ledger](../../registry/freshness/microsoft-skills-canonical-denominator-2026-10-27.json). Do not convert these into `verified` or `validated` without full structured package review and external evidence.

## Removed identities and systemic findings

The July `azure-servicebus-rust`, `azure-cost`, `azure-hosted-copilot-sdk`, and `azure-rbac` canonical paths are absent at the candidate revision. New cost-focused packages and similarly named SDK/identity skills are **not** proven exact successors; preserve old pin evidence and defer retirement decisions until semantic equivalence is assessed.

The risk clusters are identity/access grants and revocation, administrator diagnostics and secret-bearing logs, autonomous persistent memory hooks, telemetry consent, cross-platform message/data transfer, billable cloud changes, and large shared reference dependency trees. Reuse the useful signing, read-only, risk and consent patterns by adaptation; do not promote source-owned tools into `skillz` runtime.

## Lifecycle and next gate

PRs #412 and #413 remain draft admissions without complete pinned external security evidence or independent acceptance. PR #416 remains draft pending complete exact-final-package SkillSpector evidence and independent acceptance for 21 first-party changes; issue #415 cannot close before qualified merge. Issue #402 is an external security backfill. Issue #400 remains open for 102 candidate exact-version qualification units, four removal decisions, and source-pin/accounting decision. No newly discovered source was admitted this cycle.

**Next priority:** qualify the 26 newly eligible/previously ungoverned candidate packages at exact revision, deep-reviewing high-authority packages first, then reconcile the 76 changed packages to current-standard companion evidence and obtain external package-security results. Do not advance the source pin on structural accounting alone.
