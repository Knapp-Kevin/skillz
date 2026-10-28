# Microsoft Skills: four removed-path successor and retirement decisions

**Observed:** 2026-10-27. **Scope:** candidate-revision source identity reconciliation for issue #400, not unchanged-use admission. Registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; candidate `61fe0305ea70389ed8705eec6026a786f57865cf`. Microsoft root and old skill frontmatter declare MIT. This is a **four-path lifecycle tranche**, not four new exact-version skill reviews.

## Macro map and decision rule

The already established structural candidate denominator remains **208 = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned**, after excluding three non-first-class phase references and one exact package mirror from 212 physical manifests. The 76 changed-existing packages were screened, not fully requalified. The new/ungoverned full-static frontier remains **24/26** (4 semantic VERIFIED only, 20 REJECT unchanged), leaving **2 new + 76 changed = 78** full current-version reviews. This tranche resolves the *separate* four removed July-governed path identities. It does not change the candidate denominator.

For each removed path, the exact July `SKILL.md` was read, its Git blob identity recorded, and the same path was checked absent at the candidate revision. Relevant candidate plugin directories and possible nearby manifests were inspected. **No exact package-tree identity or one-to-one successor is established.** A similar topic, name, API or split feature is not a verified successor. Therefore the candidate path is classified **RETIRE_REMOVED_PATH**, without retiring the still-registered July package or transferring its review to any candidate. This is a candidate source-reconciliation decision, not a change to `registry/verification` semantic status.

## Four exact decisions

| July-governed package | Old manifest blob | Candidate outcome | Related material, not an automatic alias |
| --- | --- | --- | --- |
| `azure-servicebus-rust` | `365a93a6c3f94310d78791a73e9a3b2891775861` | **RETIRE path, no proven successor** | Azure SDK Rust directory has eight other skills but no Service Bus Rust. `azure-messaging` is troubleshooting, not a Rust send/receive client. |
| `azure-cost` | `8755e1c4db79a8e1bc44d6d1cdd1d3c55e5976e4` | **RETIRE umbrella path, split capability without alias** | `cost-analysis`, `cost-estimation`, `cost-governance`, `cost-optimization` divide the older umbrella's routes. Each has independent exact identity and review. |
| `azure-hosted-copilot-sdk` | `64b239df00aa320b64a9009c1875b303a87080b1` | **RETIRE path, no proven successor** | General `copilot-sdk` plus `azure-prepare` and `azure-deploy` do not inherit the old Azure-specific mandatory router's scope. |
| `azure-rbac` | `02ac75d2ba22b4d7aa1e74469b01575281f05ddc` | **RETIRE path, no proven successor** | Entra app registration and Azure resource lookup are different from Azure role-definition/role-assignment generation. |

The structured [four-path crosswalk](../../registry/freshness/microsoft-skills-removed-path-decisions-2026-10-27.json) preserves the exact old and related candidate manifest blob SHAs, old declared versions, authority implications and rationales.

## Systemic findings and preservation

- **Identity drift:** upstream has removed a pre-production Rust SDK skill, split a broad cost umbrella into specialist skills, and removed two Azure-specific routing/authorization surfaces. These are source-shape changes, not evidence that prior reviews are invalid at their original pin.
- **Authority boundaries:** Service Bus message settlement, private billing data, production deployment, credentials and Azure RBAC grants require action-specific authority. No related candidate inherits approval from a retired path or from another package's static review.
- **No silent migration:** old package paths remain valid evidence at the July pin. Do not delete historical companions, rename them to new packages, relabel them `retired` at the registered pin, or move the source pin merely because the candidate lacks them.
- **Capability mapping:** the cost split is a discovery/routing lead only. Each specialist package's individual semantic/security decision controls unchanged use; `copilot-sdk`, `azure-messaging`, Entra and Azure lookup likewise remain independent.
- **Limit:** this was an exact-manifest and targeted tree comparison, not complete package-tree semantic review of the possible replacements. No scanner, behavioral trial, Azure operation, install or external data transmission was performed.

## Accounting and lifecycle

**Removed candidate path decisions: 0/4 decided → 4/4 decided, 0 pending.** Registered July **186/186** and pin unchanged. Candidate structural denominator **208**, unchanged. New full-static **24/26**, unchanged. Remaining full current-version reviews **78**, unchanged. Third-party verification companions **748**, unchanged. **Admissions 0, semantic verification records 0, security passes 0, behavioral validations 0.**

This resolves only the removed-path successor/retirement subtask of [#400](https://github.com/Knapp-Kevin/skillz/issues/400). Keep #400 open for 78 full candidate-version reviews, qualifying external package-security evidence, and a source-pin decision. #402 and #415 retain independent security/first-party repair requirements. Draft PRs #412, #413 and #416 remain blocked on their exact-package security and independent acceptance gates. No repository-owned runtime or execution machinery is added.

**Next priority:** complete the two new candidate full-package reviews (Foundry IQ and Slack-to-Teams), then macro-tranche the 76 changed-existing packages.
