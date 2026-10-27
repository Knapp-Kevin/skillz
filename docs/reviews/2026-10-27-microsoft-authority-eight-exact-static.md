# Microsoft authority/privacy: eight complete-package static reviews

**Date:** 2026-10-27. **Candidate revision:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Registered pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` (unchanged). **Method:** reviewed all **52 package blobs** across eight distinct candidate package trees, plus three shared upstream continual-learning hook files. Source-owned scripts were inspected as reference evidence, **not executed**. No scanner, Azure/Windows operations, package install, security approval or behavioral validation occurred.

## Exact candidate results

| Candidate | Full package tree | Files | Score | Static disposition |
|---|---|---:|---:|---|
| `aks-network-capture` | `bd71608b467949a7b33fcebbecccd56ebc4002ff` | 13 | 13/20 | **REJECT unchanged** |
| `azure-search-nav` | `8c7c7f9e294b3117fa320527ced55fe22ac17362` | 4 | 11/20 | **REJECT unchanged** |
| `azure-local-multi-rack` | `6f0c6e65c070ac687c140a434472a722a2062698` | 9 | 14/20 | **REJECT unchanged** |
| `azure-local` | `0fe5c431fd9766e39c086bd2ea6583a7579f1105` | 10 | 15/20 | **REJECT unchanged** |
| `discover-azure-skills` | `baf3348531f80582ceb1445357250af80a1aa8c5` | 4 | 12/20 | **REJECT unchanged** |
| `continual-learning` | `0c2b5645bbb3fe92e02f2c7b1d11fb51da02eeac` | 1 | 10/20 | **REJECT unchanged** |
| `debugview` | `1a9e965776b48abb8e0934c27cf9f5f100fc2d95` | 7 | 12/20 | **REJECT unchanged** |
| `entra-agent-id-root` | `3ea709c1b312d75518093040b47faa2f7e23a238` | 4 | 11/20 | **REJECT unchanged** |

Each candidate has its own exact-version provenance and verification companion, original manifest identity, all bundled-file paths, controlled tags, rubric, authority/privacy/dependency findings, and `security: not-run`, `behavioral: not-run`. `entra-agent-id-root` is deliberately distinguished from a different same-name plugin exposure. `continual-learning` has one in-package blob but three separately inspected shared source-owned hook files. No candidate was admitted or declared safe for unchanged selection.

## Macro synthesis

**Hard authority boundaries:** `aks-network-capture` has a good explicit capture-approval reference and separate debug-container gate, but its Bash/PowerShell selectors default to **all Linux nodes**, and full-packet capture can disclose credentials and PII. `azure-search-nav` posts an ARM-audience bearer token to a fixed `azurefd.net` semantic-search endpoint without a qualified audience/origin trust boundary. `azure-local-multi-rack` recommends `az extension add --yes --upgrade` and initial billable NFC/Cluster Manager creation without distinct approval for installation and resource/cost effects. Standard `azure-local` contains useful scoped-change safety rules, but initial Arc/instance creation does not establish a separate owner/budget authorization boundary. These are **static findings**, not executed exploits.

**Identity, persistent observation and host effects:** `entra-agent-id-root` provides Graph beta identity/permission provisioning and destructive cleanup without scoped tenant-owner consent. `continual-learning` installs silent session hooks; the shared upstream `learn.sh` creates global/local SQLite stores and records tool outcomes without opt-in or data-retention authority. `debugview` has sound Authenticode and bounded-capture safeguards, but can load a kernel driver, enable persistent boot logging, connect remotely and capture sensitive output without action-specific approval. These are **upstream-owned** assets, not repository runtime.

**Governed discovery omission:** `discover-azure-skills` discovers from moving `main` and offers Copilot/Claude/`npx skills` install commands without exact-version source vetting or security qualification. It does not itself auto-install, so this is a quality/trust-gate rejection, not an observed executed side effect.

**Differentiated reusable patterns:** Preserve target-bound capture approval and run-ID cleanup; exact portal resource-type mapping; standard-vs-multi-rack routing and fabric blast-radius planning; bounded diagnostic capture and Authenticode verification; preview Agent ID BlueprintPrincipal dependency/WIF guidance; and two-tier memory scoping only with explicit consent and retention. These are adaptation/extraction/checklist references, not unchanged approvals. Recurrent omission: permission/capability checks and parameter confirmation are mistaken for authorization of infrastructure, sensitive-data, identity, persistent observation, or money-bearing actions.

## Source-family and lifecycle accounting

Latest candidate structural denominator **208** = 106 unchanged exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned. Before this tranche **11/26** new candidates had full static reviews (4 semantic VERIFIED only, 7 REJECT unchanged). Eight distinct genuine gaps were closed as **REJECT unchanged**, yielding **19/26** fully reviewed (4 VERIFIED semantic only, **15 REJECT unchanged**); **7 new + 76 changed = 83** still require full candidate-version qualification. Four removed-path successor/retirement decisions remain open. The registered July source stays **186/186** at its unchanged pin.

Independent live-tree count before mutation: **779 verification YAML** (44 first-party + 735 third-party); eight new candidate companions make **787 total / 743 third-party**. The five public accounting surfaces are reconciled in this same tranche. Source admissions 0; source-pin movement 0; package security and behavioral validation not-run.

PRs #412, #413 and #416 remain draft with their own external exact-package security and independent acceptance blockers. Issues #400, #402 and #415 remain open. This review is not permission to execute any upstream scripts or install plugins.
