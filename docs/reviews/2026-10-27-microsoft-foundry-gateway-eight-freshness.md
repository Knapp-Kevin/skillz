# Microsoft Skills: Foundry, model deployment and Azure AI eight-package freshness screening (2026-10-27)

**Result:** At exact upstream commit `1a63e5f771987a9a13e9f0571823dc1e80741583`, eight distinct changed-existing canonical packages received individual bounded exact-version static screening: **6 REJECT unchanged**, **2 REFERENCE-ONLY pending complete package and security qualification**. No source admission, scanner pass, behavioral validation or source-pin advance is claimed. The individual provenance, manifest and package-tree identities, dependencies, controlled tags, ten-dimension rubrics, authority/privacy decisions and explicit `not-run` states are in [the structured record](../../registry/freshness/microsoft-skills-foundry-gateway-eight-2026-10-27.json).

## Live denominator and macro map

- Repository starting `main`: `222859cf368fd7be87d4c3e8ec935ef5b05b5c0c`. Registered Microsoft pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` remains **186/186 current-standard at that exact pin**; 721 persisted third-party reviews, 44 first-party skills and 22 source identities are unchanged.
- The [frozen governed crosswalk](../../registry/freshness/microsoft-skills-governed-crosswalk-2026-10-10.json) partitions 186 canonical July packages into **106 exact-tree unchanged, 76 changed, four removed** at the frozen October revision. It is not the latest candidate denominator.
- Previous bounded changed-existing screening: **48/76**. This distinct tranche advances it to **56/76**, leaving **20**. Frozen raw additions are separately **22/22 classified** (19 frontmattered candidates, three non-frontmattered nested references), with two later Advisor additions. Four removed/renamed canonical paths still need decisions.
- This tranche comprises **six Foundry first-class identities** (one parent and five nested: finetuning, deploy-model, capacity, customize, preset) plus Azure AI and AI Gateway. The Foundry parent contains **220 Git blobs and five nested first-class `SKILL.md` files**; deploy-model contains 17 blobs including three nested first-class manifests. These are **eight canonical crosswalk identities, not eight independent copies of overlapping parent content**.
- The candidate source revision is the October 26 upstream head `1a63e5f771987a9a13e9f0571823dc1e80741583`. Comparison from frozen October `d5741a1e9325adead3a28d1d203bb69283907e06` shows **20 additional commits and 206 changed paths**, including a changed Foundry parent manifest and voice/managed-harness references. The parent **latest** tree is `2311f81bfa096aaefd50068b61443cb92ba70bfe`; do not reuse the frozen parent tree as current. All eight latest package trees were enumerated without truncation.
- Shared dependencies: Azure CLI/azd, Microsoft Foundry extension, Azure MCP, Python/PowerShell/Bash, quota/capacity APIs and cloud subscriptions. Shared risks: external installation, billable cloud resources, production routing/content-safety changes, subscription-key exposure, private training data, audio/document transmission, and overlapping nested workflows. Full transitive license and package-security review remain open.

## Individual dispositions

| Canonical identity | Latest manifest | Latest package tree | Files | Score /20 | Bounded disposition |
|---|---|---|---:|---:|---|
| `microsoft-foundry` | `14fd2bc5` | `2311f81b` | 220 | 11 | **REJECT UNCHANGED EXTRACT** |
| `microsoft-foundry-finetuning` | `428b2f36` | `91b3afac` | 34 | 11 | **REJECT UNCHANGED EXTRACT** |
| `microsoft-foundry-deploy-model` | `fd954ccf` | `5e60a085` | 17 | 15 | **REFERENCE ONLY PENDING FULL REVIEW** |
| `microsoft-foundry-deploy-model-capacity` | `46935315` | `547adfbf` | 5 | 11 | **REJECT UNCHANGED EXTRACT** |
| `microsoft-foundry-deploy-model-customize` | `eb488717` | `118035ed` | 4 | 15 | **REFERENCE ONLY PENDING FULL REVIEW** |
| `microsoft-foundry-deploy-model-preset` | `61fc18b2` | `643a38ce` | 4 | 11 | **REJECT UNCHANGED EXTRACT** |
| `azure-ai` | `6ba99c7a` | `34c27c07` | 16 | 12 | **REJECT UNCHANGED EXTRACT** |
| `azure-aigateway` | `2a02dbfc` | `8529348e` | 9 | 11 | **REJECT UNCHANGED EXTRACT** |

## Macro findings and omissions

1. **Installer authority hard fail:** The Foundry parent mandates running `check-and-setup-dependencies.sh` or `.ps1` before any sub-skill. Both source-owned scripts install the `microsoft.foundry` azd extension if absent. An automatic extension install is a real environment mutation; neither mandatory execution nor tool availability establishes user authorization. This is upstream package tooling, **not** repository-owned `skillz` runtime.
2. **A static code-injection boundary in a read-only skill:** The capacity helper `models/deploy-model/capacity/scripts/discover_and_rank.sh` interpolates `CAPACITY_JSON`, `PROJECTS_JSON`, `QUOTA_JSON`, `MIN_CAPACITY` and model inputs into a `python3 -c` program rather than passing them as data. Malformed or attacker-influenced content containing Python delimiters can alter constructed code. This is a **static risk finding**, not an executed exploit. The `capacity` manifest blob is unchanged from July, but its package tree changed, proving that manifest-only freshness is insufficient.
3. **Cost and deployment authority split:** `deploy-model` requires target-project confirmation and `customize` presents a full configuration summary. Preserve these good gates. The `preset` fast path nevertheless proceeds to project creation and billable model deployment without a standalone action-specific resource/spend authorization. The `customize` confirmation omits explicit cost/PTU and content-safety-policy implications; a troubleshooting delete example needs its own destructive-action gate.
4. **Training-data and deletion boundaries:** `finetuning` includes strong baseline, grader-calibration and checkpoint practices, but its quickstart uploads data, submits billable training and deploys without explicit data/cost authority. `cleanup.py --delete-files` can delete uploaded files; a CLI flag or optional dry-run is not independent authorization.
5. **Credential and privacy risks:** `azure-aigateway` retrieves APIM subscription keys and demonstrates backend/RBAC mutations and usage metrics without appropriate approval and minimization. `azure-ai` routes speech and search/document operations without an explicit sensitive-data transmission/disclosure gate. Cross-region capacity reporting also exposes project names and quota context.
6. **Source priority remains high, not automatically trusted:** Foundry has differentiated deployment/evaluation/agent-design mechanisms, but nested duplication, mandatory installation, sensitive-data paths and cloud costs justify deep review and selective extraction. No scores override the authority hard fail. The remaining 20 changed-existing packages and four removals are the next macro frontier; the latest eligible denominator is still unresolved.

## Evidence and non-execution

Inspected all eight current `SKILL.md` manifests, latest Git package-tree identities and file counts, the parent installer scripts, the capacity bash helper, preset/customize deployment references, fine-tuning quickstart and cleanup helper, and AI Gateway patterns/policies. Large packages (especially the 220-file Foundry parent) were **not fully semantically reviewed file by file**. Every candidate has its own truthful bounded screening record and `security_state: not-run`, `behavioral_validation: not-run`. The two reference-only candidates remain `unverified`; the six hard-fail candidates are rejected for unchanged use, while their extraction value is preserved.

No upstream scripts, cloud commands, training, deletion, scanner, CI or behavioral tests were executed. No new discovery source was admitted in this tranche. The repository remains entirely passive. PR #416, #412 and #413 remain blocked by external exact-package security/independent acceptance; issue #400 remains open for Microsoft freshness completion.
