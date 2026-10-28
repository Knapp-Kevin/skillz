# Microsoft Kusto candidate tranche: exact-version static rejection

**Date:** 2026-10-27. **Upstream exact revision:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Registered pin remains:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`. **Scope:** three previously ungoverned/new first-class packages, each independently reviewed as a complete source-owned package. No upstream code was executed.

## Frontier and accounting

The source's **208** structurally eligible candidates partition into **106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned**. The 76 changed packages were previously screened, not promoted. This tranche gives **3/26 new candidates** decisive current-standard static **REJECT unchanged** records, leaving **23** new candidates without decisive full-package semantic review. The remaining current-version semantic frontier is **76 changed + 23 new = 99**. Four removed historical paths still lack proven successors. The registered July source stays **186/186** at its own pin; there is **no source admission or pin movement**.

The exact candidate-version provenance and semantic rejection companions are under `registry/skills/microsoft-skills-candidate/` and `registry/verification/microsoft-skills-candidate/`. They do **not** assert that candidate packages have been vendored, scanned, behaviorally validated or approved for unchanged use. The physical verification shelf was independently enumerated at current main: **724 third-party YAML companions before this tranche** (not the stale 721 displayed publicly); three new records make **727**. The 44 first-party local companions are excluded from that count.

## Individual dispositions

| Exact first-class package | Tree SHA prefix | Score | Decision |
|---|---|---:|---|
| `azure-kusto-graph` | `9d9ea93a` | 14/20 | **REJECT unchanged; EXTRACT** edges-first KQL graph, shortest paths and explicit persistent-model approval. Security/authentication telemetry reads and output disclosure lack scoped authorization. |
| `azure-kusto-irql-graph` | `0a36fe4d` | 15/20 | **REJECT unchanged; EXTRACT** schema-aware `Lift_To_Graph` mapping and function preflight. The high rubric score cannot override the privacy/authority hard fail for security, identity, email and process data. |
| `azure-kusto-irql` | `916cc9b4` | 13/20 | **REJECT unchanged; EXTRACT** composable IRQL selectors. The declared `Get_Event_Authentication_All` schema includes `PasswordHash`; no blanket retrieval or disclosure authority exists. |

## Complete-package and macro findings

The three packages contain **4 + 4 + 3 = 11** source-owned blobs. All manifests and bundled references were inspected at the exact upstream revision. The Kusto Explorer launch reference is a **shared identical blob** across all three packages (`b972a03ee9b88dd4a41226837ee43e96de6c4d9e`), so it was read once and its identical exposure was reconciled across all three. It correctly requires consent before saving files or launching Windows executables and avoids here-string injection. This **does not** authorize a different action, namely reading or disclosing private security telemetry. IRQL Graph additionally bundles persistent `.create-or-alter function` definitions and uses external icon URLs; its top-level deployment confirmation does not resolve data access scope. IRQL's auth selector exposes a password-hash field, making output minimization particularly important.

**Useful shared pattern:** first-class graph operators, function-existence preflight, query/schema preservation, optional user-consented local export. **Recurring defect:** read-only access to security logs is treated as implicitly permissible. A host must establish tenant/workspace scope, data-owner authorization, minimum fields, retention and recipient/disclosure scope separately from persistent function or local file approvals.

All three semantic states are `rejected`; external security and behavioral states are `not-run`. No SkillSpector pass, test, cloud query or execution evidence is claimed. No repository-owned runtime, CI, scanner, scripts or scheduler was added.

## Lifecycle

PR #416 remains draft pending exact-final-package external security receipts and independent acceptance for 21 first-party repairs. Draft admissions #412 and #413 remain blocked on their own qualification gates. Issues #400, #402 and #415 remain open; this tranche advances #400 but does not resolve its source-pin or removed-path decisions. Next highest priority is the remaining **23 new/previously ungoverned candidate packages**, grouped by shared dependencies and authority risk.
