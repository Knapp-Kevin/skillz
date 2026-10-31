# Microsoft Skills / Azure Skills exact-tree mirror reconciliation (2026-10-30)

## Scope and authority

Current main at start: `1ab1c2511a8d29f304a59c7657b41d137418a9eb`. The current README and Tier-1 governance control; Wayfinder #35, queue #27, structure #41, and PR #42 are historical destination/structure evidence. All seven open issues and five open draft PRs were inspected before selecting this disjoint third-party registry lane. Drafts #489/#492/#496 change first-party skills and shared local registry, and #412/#413 propose new first-party admissions; none touches these Microsoft/Azure mirror companions. No draft met its exact-version external security and behavioral qualification gates. No repository-owned runtime, scripts, scanner, tests, CI, scheduler or generator were added.

## Whole-family macro map

The registered Microsoft Skills pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` has 186/186 current-standard companions. Azure Skills pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4` has 34/34. Exactly **33** Azure package names have a Microsoft Skills companion with identical recorded Git tree and SKILL.md blob identities; **33/33** have the same decisive semantic disposition and explicit `not-run` behavioral state. The remaining Azure-only `entra-app-registration` has its own rejected exact-version review. Source-family static gaps are zero; cross-source exposure is not a new review identity or license grant.

Three identical-package pairs nevertheless assigned different scores and materially different authority characterization. The Microsoft Skills records reviewed the complete bundled references and described more consequential behavior; the Azure records emphasized the top-level guide. We reconciled the Azure mirrors to the fuller exact-tree evidence, without pretending to rerun execution or altering either pinned upstream package.

| Identical package | Microsoft score | Azure before → after | Final disposition | Material evidence previously underrepresented in Azure |
|---|---:|---:|---|---|
| `appinsights-instrumentation` | 12/20 | 13 → 12 | REJECT unchanged | Production telemetry/resource mutations, Log Analytics primary shared-key retrieval and credential custody |
| `azure-ai` | 10/20 | 13 → 10 | REJECT unchanged | Persistent Azure AI Search index/document writes, external AI/audio/document transmission, cost and retention |
| `azure-aigateway` | 8/20 | 13 → 8 | REJECT unchanged | APIM identity/RBAC, routing and security-control mutation, `az apim subscription keys list` credential output, live traffic |

## Authority, privacy, freshness and dependencies

- All three remain **REJECT unchanged**. Access to Azure services, resource identifiers and an authenticated CLI are not permission to mutate identity/access, persistent cloud state, production traffic, telemetry or security controls, or disclose credentials and private content.
- The credential-output issue in `azure-aigateway` is an additional concrete secret-handling defect, not merely an insufficiently specific cloud-operation approval. Do not print subscription keys or copy credential-bearing commands into conversation.
- Useful methods remain ADAPT/EXTRACT/CHECKLIST prior art: OpenTelemetry/instrumentation topology, Azure AI service selection and managed-identity guidance, and AI gateway policy/caching/rate-control patterns. Preserve all bundled upstream references, scripts, package identities, source-specific license/terms, revisions and dependencies intact.
- Both source pins and all six recorded package fingerprints remain unchanged. All three Azure companions now record the full-package score, richer authority/dependency rationale and `last_checked_at` / `last_verified_at` 2026-10-30. These are static evidence-reconciliation dates, not scanner or behavioral run dates.
- The index.json current counts also retained an obsolete Cloudflare 8 VERIFIED / 5 REJECT split after the merged 13-package recheck; corrected to 6 VERIFIED / 7 REJECT without changing the 13/13 denominator. The source registry's Dan Dewhurst rationale was separately stale: it claimed all 23 VERIFIED despite the existing 21 VERIFIED / 2 REJECT decision. It now agrees with the current ledger and source-specific security/behavioral caveat.

## Accounting and disposition

**Azure 34/34 → 34/34, Microsoft 186/186 → 186/186; zero new identities, zero source-family gaps, denominator delta 0.** Exactly three Azure provenance and three verification records refreshed; one source registry rationale corrected. Public totals remain **44 first-party / 867 third-party / 911 total persisted review/provenance pairs**. All five public accounting surfaces were reconciled in this tranche. No source pin promotion, package-security scan, behavioral validation, license change, upstream modification or executable machinery was introduced.

**Lifecycle:** Existing issues +0 opened / -0 closed; five pre-existing draft PRs remain held for explicit external exact-package security and independent executed adversarial acceptance. Next priority: qualify the 36 final changed first-party package trees in #489/#492/#496 and reconcile their shared local verification registry before merging eligible repairs.
