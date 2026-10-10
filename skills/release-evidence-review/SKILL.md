---
name: release-evidence-review
description: >-
  Assess software release or deployment readiness using test, provenance,
  environment, rollback, approval and post-release evidence. Use before
  proposing a promotion, merge, or production release; not as a deployment
  controller or substitute for repository-specific release governance.
metadata:
  author: Knapp-Kevin/skillz
  category: Development
  display-name: Release Evidence Review
  version: 0.1.0
---

# Release Evidence Review

A passive, evidence-first checklist. The host may inspect only authorized sources and must not merge, deploy, modify DNS, rotate credentials, spend money, notify users, or change infrastructure based solely on this skill.

## Release contract

Establish target revision/artifact digest, source repository, intended environment, release scope, rollback owner, decision maker, acceptance criteria, and applicable organizational gates. Identify whether the user requested analysis, a draft plan, or a specific authorized action. Readiness is not permission to execute.

## Evidence review

1. **Change identity.** Confirm exact commit, artifact digest, dependency lock state, changelog, migration inventory and diff against the current deployed baseline. Unknown production baseline is a blocker for claims of verified equivalence.
2. **Build and supply chain.** Check available build results, provenance attestations, dependency/license advisories, signatures where relevant, and artifact immutability. Distinguish absent evidence from a pass.
3. **Functional quality.** Map critical acceptance criteria to executed tests, failure results, browser/operator journeys, accessibility and integration evidence. Static checks alone do not prove behavior.
4. **Environment and data.** Identify configuration drift, feature flags, secrets handling, permissions, migrations, backup/recovery assumptions, production traffic impact, and irreversible operations. Never expose credential values in a report.
5. **Operations and recovery.** Specify health signals, monitoring ownership in the external host/environment, abort thresholds, rollback procedure, restoration evidence, and residual risk. Do not create repository-owned monitors or schedulers.
6. **Authority.** Require explicit approval tied to action, environment, target revision, destination, expected cost/impact, and communication recipients. A green check, mergeability flag, or parameter selection is not approval.
7. **Decision.** Choose `ready-for-approval`, `changes-required`, `blocked-external`, or `insufficient-evidence`. Even `ready-for-approval` is not `deployed`. Actual deployment and post-release verification must be recorded separately if externally executed.

## Hard-stop examples

- Tests pass but the deployment artifact differs from the tested artifact.
- Production migration has no reviewed backup or rollback strategy.
- A release needs DNS, security-control, identity or billing changes without scoped approval.
- A dependency advisory is unresolved and its impact has not been assessed.
- A deployment is reported successful based only on CI rather than observed production state.
- A customer notice is drafted but no recipient/sending authorization exists.

## Receipt

```yaml
revision: <commit>
artifact_digest: <digest or unknown>
target_environment: <name>
baseline: <revision or unknown>
evidence:
  build: <pass | fail | missing, with source>
  tests: <pass | fail | missing, with scope>
  security: <pass | fail | incomplete, with scope>
  provenance: <verified | unknown>
  migration_and_rollback: <reviewed | incomplete | not-applicable>
  production_observation: not-run
approval:
  action: <merge | deploy | communicate | other>
  resource: <target>
  destination: <environment or recipient>
  scope: <changes and impact>
  state: not-established
decision: insufficient-evidence
action_executed: false
```

Use only truthful states. If the host later performs an explicitly authorized action, record the actual result and evidence separately. This procedure is not an installer, CI workflow, release bot, or runtime.
