# Microsoft AKS / Azure readiness / Entra: three complete-package static rejections

**Date:** 2026-10-27. **Candidate revision:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Registered July pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` (unchanged). **Method:** exact non-truncated upstream Git tree and static reading of all **53 bundled blobs** across three first-class packages (20 + 16 + 17; 292,259 source bytes). No source-owned commands, cloud operations, external security scanner or behavioral tests executed.

## Seven-candidate macro map before tranche

The seven remaining new/previously ungoverned packages contain **249 physical package blobs** (about 2.09 MB), not seven uniform review units. The package/authority split is: `aks-troubleshooting` (20, live AKS reads and privileged diagnostics); `azure-app-onboard-prereq` (16, local sessions and CLI setup); `entra-app-registration` (17, tenant identity/permissions); `azure-app-onboard` (68, nested phase references and destructive session cleanup); `azure-kubernetes-app-deploy` (42, deployment manifests and CI templates); `foundry-iq` (85, ~1.28 MB of Python helpers and cloud/knowledge-base effects); `slack-to-teams` (one local manifest plus the parent Teams developer's 100+ shared expert references). These are **distinct** package trees, not duplicate exposures. The four deferred packages need deep review of shared or unusually large dependencies rather than a superficial quota pass.

## Exact dispositions

| Candidate | Manifest blob | Complete package tree | Files | Score | Decision |
|---|---|---|---:|---:|---|
| `aks-troubleshooting` | `b6d2a1e2f762ce0e5f3fb6b2f3551fc44a7e7e3e` | `bbed91bfbf8c43aab4bd5f0272b71ce713eb5f33` | 20 | 15/20 | **REJECT unchanged** |
| `azure-app-onboard-prereq` | `5897a8937a5180e91990f069ff301ae8ac4df036` | `da6314ba04834970836b18ea0b39bf6a20cfde13` | 16 | 14/20 | **REJECT unchanged** |
| `entra-app-registration` | `f7f472ade6f8ce489f3efae8bb8533dd0be6b3f0` | `051071c18ecb38347076f857819987e3ec37685e` | 17 | 12/20 | **REJECT unchanged** |

All three have individual exact-version provenance and verification companions, complete relative-file inventories, individual ten-axis rubrics, controlled tags, dependencies, authority/privacy findings and explicit `security: not-run` and `behavioral: not-run` states. They are unadmitted candidate-version evidence, not new trusted skills.

## Macro synthesis and preserved value

**AKS troubleshooting:** strong evidence-first 2–4 hypothesis convergence, target/context matching, denial reporting, bounded/redacted log projection, and explicit approval for the fallback privileged debug pod. However, the *existing* Inspektor Gadget route uses `kubectl gadget run` after a permission check for `create pods/portforward`, without an action-specific owner approval for those effects. The `aks-preview` operation command can auto-install an extension; `az aks get-credentials` writes kubeconfig without an explicit configuration-write gate. Authorization is not the same as RBAC or shell availability. Preserve the read-only diagnostic map and evidence discipline, not unchanged execution authority.

**App Onboard prereq:** valuable static-first prohibition on ordinary install/build/test, exact-command consent for optional validation, separate remediation approval, explicit readiness gates and cloud-SDK migration stop. But `references/session-protocol.md` orders automatic deletion of session folders older than seven days, and calls a CLI extension check/install tool without a separate install approval. Mandatory local state and tenant/user identity collection precede read-only assessment; no complete retention/redaction authority accompanies those artifacts. Preserve the build consent and deterministic verdict model; reject unchanged lifecycle authority.

**Entra app registration:** useful managed-identity and certificate preference, least privilege, PKCE and consent distinctions. The root skill and bundled CLI/OAuth references instruct app creation, Graph permissions, admin consent and credential resets without scoped tenant-owner authorization. `az ad app credential reset` returns a password value; the first-registration guide models copying a secret and links `jwt.ms` for token inspection without a secure external disclosure boundary. Example strings are illustrative, **not observed live secrets**. Preserve the authentication design guidance, not the unchanged mutating procedure.

**Systemic pattern:** capability, RBAC, question intent and parameter confirmation are repeatedly substituted for authorization to install, mutate identity, alter host configuration or delete persistent artifacts. Strong local approval sub-gates do not automatically authorize adjacent side effects. No new taxonomy values are needed.

## Atomic accounting and lifecycle

The candidate structural denominator remains **208** = 106 unchanged carry-forwards + 76 changed-existing + 26 new/previously ungoverned. Three distinct new candidates move **19/26 → 22/26** full exact-version static reviews (**4 semantic VERIFIED only / 18 REJECT unchanged**). The remaining full-review frontier moves **83 → 80** (4 new + 76 changed). Four removed-path successor/retirement decisions remain unresolved. Registered July stays **186/186**, no source pin or admission changed.

Live main before mutation had **787 verification YAML records = 44 first-party + 743 third-party**; three companions bring the intended new tree to **790 total = 44 + 746**. All five public accounting surfaces are updated in this tranche. No package-security pass, behavioral validation or source-pin promotion is claimed.

PRs #412 and #413 remain draft for exact-final security/independent admission; PR #416 remains draft and not merge-ready for 21 first-party security and independent acceptance gates. Issues #400, #402 and #415 remain open for their respective unresolved acceptance criteria. No candidate discovery or source admission occurred in this bounded source-family cycle.
