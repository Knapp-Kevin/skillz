# Microsoft Azure Deploy and Foundry Finetuning: two exact-version static reviews

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`; registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. The complete **75 source files (75 distinct Git blobs, 320,665 bytes)** were fetched from the exact upstream revision and inspected as two independently front-mattered packages. No cloud deployment, training, script, scanner, security assessment or behavioral execution was performed.

## Macro map and accounting

Structural denominator **208 = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned**. All 26 new candidates are already fully statically reviewed. Changed-existing **69/76 → 71/76**; Azure operations **23/30 → 24/30**. Remaining five genuine gaps: `azure-diagnostics`, `azure-kubernetes` parent, `azure-prepare`, `azure-upgrade`, and `microsoft-foundry` root. Nested Kubernetes and Foundry children already independently reviewed remain distinct; shared source references are not counted as extra eligible packages.

| Package | Exact package tree | Source files | Score | Decision |
|---|---|---:|---:|---|
| `azure-deploy` | `782b021717e199423ed37720a6ba5436b2951aa7` | 41 | 12/20 | REJECT unchanged |
| `microsoft-foundry/finetuning` | `91b3afacfb2c855870109207d0b584e8e2993f8e` | 34 | 12/20 | REJECT unchanged |

## Package findings

**Azure Deploy:** The root requires a populated validation proof, a prepared plan, a pre-deploy checklist, and global `ask_user` confirmation for destructive, costly and security-sensitive actions. These are useful safeguards, but plan status and subscription/region selection are not a deployment-specific authorization grant. The root routes directly to `azd provision --no-prompt`, `azd up`, `azd deploy`, and Terraform apply. Source-owned CI examples include noninteractive deployment without guaranteed environment approval. SQL post-deployment scripts grant `db_datareader`, `db_datawriter` and `db_ddladmin` and apply EF migrations without a separate database owner, privilege, schema/data-migration and rollback approval. Terraform troubleshooting includes `destroy -auto-approve` examples, while global rules separately require confirmation. The full 41-file package therefore fails unchanged-use authorization coherence. Preserve the validation-proof chain, managed-identity recommendations, preflight checks, RBAC propagation checks, and endpoint verification as adaptation/checklist evidence.

**Foundry Finetuning:** The root's rules govern baseline evaluation, data validation, grader calibration, checkpoint choice and token-cost comparison, but not authorization to upload private training data, submit billable jobs, deploy endpoints, or delete resources. `scripts/submit_training.py`, `scripts/deploy_model.py`, and `scripts/cleanup.py` expose those operations directly. Quickstart and script examples accept `--api-key` CLI arguments, which can leak credentials via process lists or shell history. Dataset creation permits collection from production logs without data-owner/participant approval, minimization or retention boundaries; vision, medical/legal/resume and grader data raise additional transmission concerns. The manifest version is literally `0.0.0-placeholder`, so exact Git identity, not that version label, controls freshness. Preserve holdout evaluation, SFT/DPO/RFT selection, grader calibration, reward-hacking checks, checkpoint comparison and dataset validators as reference/adaptation evidence.

## Systemic synthesis and next gate

Both packages show **approval fragmentation across nested execution paths**. A parent validation chain or quality checklist cannot substitute for specific authority over paid cloud changes, persistent database roles, training data disclosure, model deployment and destructive cleanup. Secret-bearing CLI arguments are not an acceptable credential-handling default. The source-owned scripts, YAML pipeline examples and helpers remain intact upstream reference evidence; none becomes `skillz` runtime.

Two new individual provenance/verification companion pairs record complete package inventories, exact tree and manifest identities, source path freshness, controlled tags, ten-dimension scores, dependency/authority/privacy findings, and explicit security/behavioral `not-run`. No candidate security or behavioral validation, source admission or pin movement. Third-party verification **819 → 821**, total YAML **863 → 865** (44 first-party + 821 third-party). Registered July **186/186** and candidate structural denominator **208** unchanged. PRs #412/#413/#416 remain external security/acceptance holds. Issue #400 remains open until the five remaining reviews and source-pin decision.
