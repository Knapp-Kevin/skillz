# Google Agents CLI: evaluation and workflow delegated-authority recheck

**Date:** 2026-10-30  
**Registered source:** `google/agents-cli` (Apache-2.0), `ef7808f33fc3038112b69d4ad488ce33b72699b1`  
**Scope:** all seven first-class pinned `skills/google-agents-cli-*/SKILL.md` identities, with deeper exact-package review of evaluation and orchestration.  
**Evidence type:** structured static semantic inspection only. No scanner execution, cloud command, model call, credential access, or behavioral validation.

## Macro frontier and exact identities

The pinned `skills/` tree contains seven distinct first-class packages, no extra aliases or mirror exposures. All seven existing provenance and verification companions already exist; there are **zero genuine static gaps**. The seven package Git tree identities at the registered pin are:

| Package | Exact package tree SHA | Decision after this review |
|---|---|---|
| `google-agents-cli-adk-code` | `21e3b4e1aa24f83dc050f62d8531ec2b005f8f49` | VERIFIED semantic only 17/20, retained |
| `google-agents-cli-deploy` | `b9d8f9bdb59456602db30ca8113d1d20a69ad3d2` | REJECT unchanged 15/20, retained |
| `google-agents-cli-eval` | `18d16f199fc2347f10c718abd017b19a770feaf7` | **REJECT unchanged 14/20**, previously VERIFIED 18/20 |
| `google-agents-cli-observability` | `dead3654a52ea09a02811e77c1d5dc456631fd65` | REJECT unchanged 14/20, retained |
| `google-agents-cli-publish` | `af513ee4f7ac0cb04ef22c03a0dc5a0200ce409d` | REJECT unchanged 14/20, retained |
| `google-agents-cli-scaffold` | `6611c3f0f57d51905c33a3ab19ae4a174e7c576e` | VERIFIED semantic only 19/20, retained |
| `google-agents-cli-workflow` | `b2617019f14333bc8997375e73043ab78e0b4d23` | **REJECT unchanged 14/20**, previously VERIFIED 19/20 |

All eleven bundled reference Markdown files for the two escalated packages were inspected at the pin (six eval, five workflow). Their `SKILL.md` blobs are `2ce4c881733de6cc75dce97bb7e3c4391df69c75` and `b33bd1202885bbdaf17b5c50df0660ae01452b3a` respectively. Package references are source-owned material, not repository-owned runtime. License, source revision, physical gitlinks, and package identities are unchanged.

## Decisive exact-version findings

### `google-agents-cli-eval`: VERIFIED 18/20 → REJECT unchanged 14/20

**Trigger/use:** agent evaluation, dataset construction, failure analysis, comparison and optimization; not deployment or scaffolding. **Dependencies:** Google agents-cli/ADK, project eval config, local agent server, Gemini/Vertex-backed model judges, optional managed evaluation service, six bundled references. **Portability:** low. **Authority:** local artifact writes and code edits, model inference and potentially cloud-side dataset/trace disclosure, money-bearing calls.

The governing procedure says `eval run` is **always run**, defaults to agent execution and grading, and requires 5–10+ repeated iterations. The bundled `metrics-guide.md` states that the scaffolded default `custom_response_quality` is an LLM judge using `genai.Client()` with Gemini API key or ADC. `user-simulation.md` confirms that scenario synthesis sends agent tools/instructions to the Vertex evaluation service and uses an LLM-backed simulator. `advanced-commands.md` provides managed `eval submit` which hands datasets and metrics to a cloud service, and `metrics-guide.md` documents remote code uploads for `CodeExecutionMetric`. The procedure gives a useful explicit opt-in for expensive GEPA optimization, but **does not separately authorize the default model calls, bounded cost/iteration budget, disclosure of private evaluation prompts/traces, remote endpoint/provider, or managed upload**. Dataset selection and a generic request to evaluate are not approval to transmit arbitrary private data or spend unbounded inference budget. No actual disclosure is alleged.

**Rubric (ten 0–2 dimensions):** trigger 2, clarity 2, authority 0, failure 2, evidence 1, dependencies 2, portability 1, differentiation 2, adversarial 0, effectiveness 2 = **14/20**. Retain metric selection, holdouts, failure-to-fix mapping, trajectory distinctions, local-vs-remote metric explanations, and cost-conscious optimization guidance for **ADAPT/EXTRACT/CHECKLIST**. Behavioral validation: **not-run**.

### `google-agents-cli-workflow`: VERIFIED 19/20 → REJECT unchanged 14/20

**Trigger/use:** whole-agent lifecycle from requirements to scaffolding, implementation, evaluation, deployment, publication and observability. **Dependencies:** agents-cli, related ADK/scaffold/eval/deploy/publish/observability procedures, five bundled references, optional sample recipes, Terraform/Google Cloud tooling. **Portability:** low. **Authority:** local project and instruction writes, remote model evaluation, infrastructure provisioning, persistent deployment, publication and telemetry.

Phase 0's user-approved specification and Phase 5's explicit approval before `agents-cli deploy` are useful but **not sufficient for separate effects**. Phase 3 says to follow a recipe's `Makefile` including `make setup-infra` and `make data-ingestion` when adapted, without a distinct infrastructure, private-data or cost authorization. Phase 4 makes `agents-cli eval run` mandatory, inheriting the evaluation disclosure/cost failure above. Phase 6/7 delegate to `publish` and `observability`, both already **REJECT unchanged** for independent registry mutations and default full-content telemetry. `references/internals.md` maps `infra single-project` to Terraform apply and `deploy` to cloud/k8s operations. A broad approved design/spec is not permission for these separately consequential effects. The explicit deploy approval does not repair the earlier provisioning and evaluation paths.

**Rubric:** trigger 2, clarity 2, authority 0, failure 2, evidence 1, dependencies 2, portability 1, differentiation 2, adversarial 0, effectiveness 2 = **14/20**. Retain phased design, preservation discipline, scoped scaffolding, specification approval, recipe discovery and debugging methods for **ADAPT/EXTRACT/CHECKLIST**. Behavioral validation: **not-run**.

## Family synthesis and omissions

The seven-package family has a useful modular lifecycle and deep source references. The recurring defect is **authority inheritance across phase boundaries**: approval of a specification or a deployment command is treated as permission for independent provisioning, external evaluation, publication and telemetry. A second pattern is **private dataset/trace egress hidden inside apparently local evaluation**. The two newly rejected parents are not rescued by individually useful child instructions; conversely, their rejection does not invalidate the two retained narrower semantic references.

No newly eligible packages, denominator changes, missing provenance companions, duplicate exposures, taxonomy additions, or new source candidates were established. The other five individual dispositions remain unchanged; the `adk-code` and `scaffold` retained approvals are **semantic only**, not package-security or behavioral approvals. All seven are `validation_status: not-run`.

**Accounting:** Google Agents CLI **7/7 → 7/7**, VERIFIED **4 → 2**, REJECT unchanged **3 → 5**, gaps **0 → 0**, admitted denominator delta **0**. Persisted inventory remains **44 first-party / 867 third-party / 911 total verification records**. README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json were reconciled together. No source pin, upstream package, third-party license, security report, workflow, scanner, script or autonomous service changed.

**Lifecycle:** The existing five draft PRs #412/#413/#489/#492/#496 are independently held; the three repair drafts still require full exact-final-tree pinned SkillSpector v2.12.0 reports and independent executed adversarial acceptance for 36 changed first-party trees, followed by shared-registry reconciliation. No previously open PR was qualified for merge and no bounded issue was qualified for closure in this review.
