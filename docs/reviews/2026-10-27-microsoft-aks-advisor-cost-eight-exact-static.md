# Microsoft AKS, Advisor and Cost: eight exact-package static reviews

**Date:** 2026-10-27. **Exact candidate revision:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Registered July pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` (unchanged). **Method:** inspected all **44 source-owned package blobs** across eight distinct first-class packages, including bundled references. No upstream code, Azure calls, security scanner or behavioral tests were executed.

## Frontier and dispositions

The latest Microsoft source has **208 structurally eligible** candidates: **106** exact-tree carry-forwards, **76** changed-existing packages, **26** new/previously ungoverned. The previous new-candidate frontier was **3/26** fully reviewed (Kusto). This tranche adds **8/26**, yielding **11/26** fully statically reviewed, **15** new still needing full review, and **76 + 15 = 91** candidate-version packages still requiring full exact-version qualification. The registered July **186/186** denominator and source pin remain unchanged; four removed historical paths still require successor/retirement decisions.

| Candidate | Full-package Git tree | Files | Rubric | Static decision |
|---|---|---:|---:|---|
| `aks-gpu-inference` | `5b797fd877111afa34a811ffe4545de4789e7964` | 5 | 17/20 | **VERIFIED static; security pending** |
| `aks-known-issues` | `0642cbfede48e571a698325dccdf9c29ac6650e8` | 2 | 18/20 | **VERIFIED static; security pending** |
| `azure-advisor-actionability` | `339baea1441cc468bdcf620ad90d43944544e701` | 1 | 17/20 | **VERIFIED static; security pending** |
| `azure-advisor` | `cf9561057dc322d3be42b4a2f78a91adb8eaef6c` | 1 | 14/20 | **REJECT unchanged** |
| `cost-analysis` | `e2bcd6ba7f86f01f7c2ed74a3b7ef22d290ed3fd` | 13 | 16/20 | **VERIFIED static; security pending** |
| `cost-estimation` | `a21080854fecab8e15014121bcfd328bf4cbe5df` | 8 | 14/20 | **REJECT unchanged** |
| `cost-governance` | `dd006778491a957cd453b02ca0dcda6fb06f337b` | 5 | 15/20 | **REJECT unchanged** |
| `cost-optimization` | `a016fbc32a0961b6c18041298d0df37048d0afa3` | 9 | 14/20 | **REJECT unchanged** |

## Macro findings

**Strongest read-only designs:** `aks-known-issues` requires every signature qualifier and explicitly labels proposed fixes approval-required; `aks-gpu-inference` binds host capabilities, cluster/pod context, and diagnostic uncertainty. `azure-advisor-actionability` preserves source attribution and refuses invented remediation. `cost-analysis` provides currency separation, bounded cost queries, and explicit add-on/tier-change approval. These four passed semantic static review only, not package security or behavioral validation.

**Action-authorization failures:** `azure-advisor` offers only generic confirmation before persistent recommendation-state updates. `cost-governance` confirms budget configuration inputs but lacks a separate explicit authorization of budget creation and future recipient notifications. Both fail unchanged use despite useful read-only procedures.

**Sensitive-data and artifact failures:** `cost-estimation` directs returning a short-lived negotiated-pricesheet ZIP URL, contradicting its own fallback instruction not to expose that URL. `cost-optimization` instructs writing raw billing-query JSON and a report via `create_file` without artifact storage, retention or recipient authorization. Preserve public pricing/forecast logic, evidence-backed optimization and owner checks as extraction prior art, not unchanged operational authority.

**Shared dependencies and overlap:** Four Cost packages depend on Azure Resource Manager MCP Cost Management and related Resource Graph/Advisor surfaces; their workflows are complementary (actual spend, forecast/pricing, budgets/policy, optimization/commitments), not duplicate packages. The two Advisor packages separate listing/state changes from remediation generation. The AKS GPU and known-issue packages are distinct symptom-specific diagnostics. Host tools and source-owned references remain upstream/external, not `skillz` runtime. Financial data, resource IDs, recipient emails and operational telemetry require scoped access and disclosure authority.

**Evidence:** Every candidate has a distinct exact-version provenance companion under `registry/skills/microsoft-skills-candidate/` and verification companion under `registry/verification/microsoft-skills-candidate/`, with Git package-tree and manifest SHAs, individual rubric, controlled tags, dependency/authority/privacy findings, and `validation_status: not-run`, `package_security_status: not-run`. No package was admitted or approved for unchanged selection. New companion count is eight; the independently established previous third-party verification count was **727**, making **735** after this tranche.

## Lifecycle

PRs #412, #413 and #416 remain draft with independent external package-security and acceptance gates. Issue #400 remains open for 15 new and 76 changed current-version qualifications, four removed-path decisions and the eventual source-pin decision. Issues #402 and #415 remain blocked by external security evidence and #416 qualification respectively. No repository-owned runtime, CI, scanner, scheduler, scripts or tests are added.
