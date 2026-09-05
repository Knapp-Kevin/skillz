# Verification: Microsoft Skills `finetuning`

- Source family: `microsoft-skills`
- Canonical path: `.github/plugins/azure-skills/skills/microsoft-foundry/finetuning`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `f4fce572b9e1db4e7880315bf39045d03f42a0fd`
- `SKILL.md` blob: `68ad2dc82e4e38b5bdc07170ae1a2aa477b0a277`
- Static disposition: **rejected unchanged**
- Score: **12/20**
- Behavioral validation: **not-run**
- Controlled tags: `cloud`, `deployment`, `operations`, `production-oriented`, `risk-aware`, `mutating`, `external-side-effect`, `low`

## Structured semantic review

### Useful material to preserve

The package has strong fine-tuning methodology prior art: baseline-before-training discipline, explicit SFT/DPO/RFT selection, dataset validation and format guidance, grader calibration with target base-model failure rates, reward-hacking checks, checkpoint evaluation instead of final-checkpoint assumption, token-cost measurement alongside accuracy, training-curve diagnosis, iterative dataset improvement, and deployment/evaluation separation. The independently front-mattered nested skill has genuine value as adaptation/reference material even though unchanged execution is unsafe under current governance.

### Authority hard fail

Unchanged adoption fails the current authority standard. Its normal workflows and bundled scripts submit paid fine-tuning jobs, upload training files, deploy models through Azure management APIs, invoke model/evaluation services, generate synthetic training data, and delete files/deployments. The procedure provides commands and parameters but does not require a mandatory action-specific authorization checkpoint immediately before each consequential resource, cost, upload, deployment, or destructive lifecycle operation. A request to fine-tune a model is not blanket authorization for every subsequent upload, paid job, deployment, or cleanup action.

### Secret and sensitive-data discipline

The package operates directly on training/evaluation datasets and explicitly discusses PII-dense training content. Synthetic-data generation, external evaluation, upload, training, and deployment workflows can transmit or persist user/application content in external Foundry/Azure services. There is no universal prerequisite for approved-data classification, disclosure authority, minimization, or redaction before those operations. Any adaptation must keep credentials out of conversational/log output and introduce explicit data-authority gates before external transmission or persistence.

### Trigger and non-trigger boundary

Use as reference for choosing SFT/DPO/RFT, preparing and validating datasets, calibrating graders, diagnosing training curves, selecting checkpoints, evaluating fine-tuned models, and designing safe fine-tuning workflows. Do not use unchanged as authorization to upload data, incur training/evaluation cost, deploy models, invoke external services, or delete remote resources.

## Portability

Low unchanged portability because execution is coupled to Foundry/Azure APIs, identities, deployment semantics, and model-training services. The methodological pieces around dataset quality, grader calibration, reward hacking, baseline comparison, checkpoint selection, and training diagnostics generalize well.

## Validation note

This review inspected the exact registered-pin `SKILL.md` and canonical package tree statically, including the package's references, workflow inventory, validators, and operational script surface. No training job, upload, deployment, evaluation, model invocation, synthetic-data generation, resource deletion, or credential-bearing operation was executed. No representative external behavioral/adversarial evidence exists, so behavioral validation remains `not-run`.