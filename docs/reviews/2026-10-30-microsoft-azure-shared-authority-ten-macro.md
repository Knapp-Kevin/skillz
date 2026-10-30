# Microsoft Azure shared exact-package authority macro review

**Date:** 2026-10-30  
**Scope:** registered pinned `microsoft-skills` (`32cad4ee689c95c309e61aeefcbc6af356f1e6a7`) and `microsoft-azure-skills` (`8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`).  
**Architecture:** passive static evidence only; no source package, pin, repository-owned runtime, security scanner, or external behavioral action changed.

## Macro map and duplicate accounting

The Azure Skills source has **34/34** current-standard individual reviews. A high-authority tranche inspected seven previously VERIFIED packages and three previously REJECTED control packages, rather than creating new review identities or assuming all of a creator's skills are safe. The Microsoft Skills source has **186/186** current-standard reviews. The two corrected packages are byte-identical across both registered exposures (same exact package-tree and SKILL.md blob), so each family retains its own exact-version companion while the substantive risk analysis is shared. The two mirrored records must never diverge in unchanged-use eligibility.

| Azure skill | Previous state | Current state | Primary finding |
|---|---|---|---|
| `azure-enterprise-infra-planner` | VERIFIED 18/20 | **REJECT unchanged 15/20** | Private subscription insights and retained JSON precede affirmative read/retention authorization |
| `microsoft-foundry-deploy-model` (root) | VERIFIED 17/20 | **REJECT unchanged 14/20** | Project/region input confirmation is not a final cost-bearing deployment authorization |
| `airunway-aks-setup` | VERIFIED 17/20 | Preserved | Explicit confirmation before controller/provider/model installation |
| `azure-cloud-migrate` | VERIFIED 17/20 | Preserved | Separate source tree and user choice before deployment handoff |
| `azure-rbac` | VERIFIED 17/20 | Preserved | Generates least-privilege commands rather than executing assignments |
| `microsoft-foundry-deploy-model-capacity` | VERIFIED 17/20 | Preserved | Read-only capacity/quota discovery; no deployment action |
| `microsoft-foundry-deploy-model-customize` | VERIFIED 17/20 | Preserved | Full configuration confirmation at Phase 12 before creation |
| `microsoft-foundry-deploy-model-preset` | REJECT 12/20 | Preserved | Direct deployment and optional project creation without final authorization |
| `azure-deploy` | REJECT 15/20 | Preserved | SQL identity grants and EF schema migrations lack separate post-deploy approval |
| `azure-validate` | REJECT 16/20 | Preserved | Validation escalates to workspace repair and mandatory deployment handoff |

## Decisive evidence

**Enterprise planner:** The unchanged SKILL.md blob is `a261c21ed056be1958902cf23f6ae4879001b404`; package tree `620e71b64d369c1ea3aa5c8f4feee7793841e7a5`. `references/workflow.md` makes Phase 1 mandatory. `references/phases/1-extract-insights.md` reuses a preexisting `.azure/insights.json` without freshness/scope validation; if the user does not answer its scope prompt, the default subscription is used. It invokes `insights_get` through a general-purpose subagent and persists the returned JSON. The later resource/plan approvals and exceptionally strong Phase 7 risk-acknowledgment gate are valuable, but do **not** authorize earlier private cloud reads, subagent disclosure, or persistent retention. An explicit affirmative account/subscription/field/time/retention gate is required; silence must not authorize reads. No literal credential exposure was established.

**Foundry deploy-model root:** The unchanged SKILL.md blob is `322b342762abbcd86eb90a92b2c4cb7dccd6aac6`; package tree `6ea62f4fb44575d28a3324b4c1eada0e0a3f6be9`. Root confirmation offers `Yes, deploy here` during project selection, before final model, quota, SKU, capacity, cost and potential project-creation decisions. Its default simple-request path delegates to `preset`, which explicitly says `Deploy immediately`, may create a new project, and uses 50% of available capacity without a final action-specific confirmation. A target-selection prompt is not a deployment/cost approval, and the separately safer `customize` Phase 12 cannot lend its gate to the `preset` path. Require a post-configuration, exact-target, resource, cost and external-write authorization before any delegated creation. The root retains differentiated routing, live quota checks and user-facing target visibility for ADAPT/EXTRACT/CHECKLIST.

## Macro findings

The recurring defect is **authorization being inferred from workflow progression or a selection prompt**. Strong downstream safeguards do not retroactively authorize private reads, retained telemetry or earlier subagent transmissions. Nor can a parent procedure inherit a safe sibling's confirmation gate when it routes to an unsafe child. Mirror exposure is a review/accounting relationship, not an extra eligible package or a new source admission.

## Accounting and lifecycle

- Azure Skills: **34/34 → 34/34**, static gaps **0**, VERIFIED **7 → 5**, REJECT **27 → 29**.
- Microsoft Skills: **186/186 → 186/186**, static gaps **0**; two identical-package mirrored dispositions corrected.
- **Eight** exact-version provenance/verification companions refreshed, **two** distinct package-tree decisions corrected, **four** source-exposure dispositions changed.
- Admitted denominator **+0**, new reviews **+0**, first-party **44**, third-party **848**, total verification **892**. Source pins, licenses, package fingerprints and dependency descriptions unchanged.
- `validation_status: not-run` remains truthful; no SkillSpector or adversarial pass was performed. Both rejected packages retain adaptation/checklist value.
- Existing draft first-party repairs #489/#492/#496 and admissions #412/#413 remain independent external security/behavioral qualification holds, not mergeable on green Socket checks alone.
- Passive hygiene: repaired three incorrect `docs/docs/reviews/` relative links in `docs/SYSTEM_STATE.md`, identified in a targeted navigation audit.

**Next action:** obtain complete pinned SkillSpector v2.12.0 exact-package reports and independent host-executed adversarial acceptance for the 36 changed first-party repair package trees; reconcile the shared first-party registry before merging any qualified draft.
