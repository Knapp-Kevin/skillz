# Provenance: Microsoft Skills `finetuning`

- Source family: `microsoft-skills`
- Source repository: `https://github.com/microsoft/skills`
- Source class: official Microsoft
- License: MIT
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Canonical package path: `.github/plugins/azure-skills/skills/microsoft-foundry/finetuning`
- Canonical `SKILL.md`: `.github/plugins/azure-skills/skills/microsoft-foundry/finetuning/SKILL.md`
- Package tree: `f4fce572b9e1db4e7880315bf39045d03f42a0fd`
- `SKILL.md` blob: `68ad2dc82e4e38b5bdc07170ae1a2aa477b0a277`
- Freshness evidence: `981d9b71d0187be796b03c2f4d69cccca80c0e42` synchronized this exact `SKILL.md` on 2026-05-25T12:08:54Z
- Behavioral validation: `not-run`

## Package identity and boundary

`finetuning` is an independently front-mattered first-class nested skill under the canonical `microsoft-foundry` package and therefore contributes its own eligible denominator unit. The package includes the root `SKILL.md`, twelve topical references, five workflow guides, fine-tuning data validators, and operational Python helpers for training submission/monitoring, grader calibration, checkpoint analysis, model deployment, evaluation, synthetic-data generation, quality scoring, and cleanup. Those upstream scripts remain source evidence only; they are not repository-owned `skillz` runtime.

## Purpose and dependencies

The skill covers SFT, DPO, and RFT fine-tuning on Microsoft Foundry, including dataset preparation and validation, grader design/calibration, training job submission and monitoring, checkpoint selection, deployment, evaluation, synthetic/distillation data generation, large-file upload, and cleanup. Operational use depends on Python, Azure/Foundry identities and endpoints, OpenAI/Azure APIs, model deployments, training/evaluation datasets, and Azure management-plane access for deployment paths.

## Authority and portability

Authority profile: **mutating + external-side-effect**. Bundled workflows and scripts can upload training data, submit paid training jobs, deploy models, invoke external model/evaluation services, and delete files/deployments. The package does not impose a mandatory action-specific authorization checkpoint immediately before those consequential operations.

Portability: **low** unchanged because operational behavior is tightly coupled to Microsoft Foundry/Azure APIs and resource lifecycle. Its dataset-quality, grader-calibration, checkpoint-selection, baseline-first, reward-hacking, and training-curve guidance remain useful adaptation/reference evidence.

## Secret and sensitive-data context

Fine-tuning and evaluation can transmit and persist user/application datasets, prompts, model outputs, audio/image/document-derived material, and explicitly PII-dense training content. The package lacks a universal disclosure/minimization boundary before upload, training, synthetic-data generation, evaluation, or persistence. Any adaptation must use approved credential paths, avoid exposing tokens/keys or credential-bearing URLs, and require explicit data authority plus minimization/redaction before external transmission.