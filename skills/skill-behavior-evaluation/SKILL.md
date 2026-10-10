---
name: skill-behavior-evaluation
description: >-
  Design and assess representative behavioral and adversarial scenarios for
  an agent skill, with baseline comparison, explicit non-trigger cases and
  evidence-backed outcomes. Use for skill regression readiness; do not claim
  validation when a host has not actually executed scenarios.
metadata:
  author: Knapp-Kevin/skillz
  category: Meta
  display-name: Skill Behavior Evaluation
  version: 0.1.0
---

# Skill Behavior Evaluation

A passive evaluation protocol for an external, authorized host. This document neither executes scenarios nor supplies a test runner. Static semantic review, package security, and behavioral validation are independent states.

## Inputs and authority

Identify the exact skill revision and package fingerprint when available, its dependencies and declared trigger/non-trigger boundaries, intended host/tools, user goal, data sensitivity, and side-effect authority. Use synthetic fixtures by default. Do not access live private data or perform costly, external, mutating, or production operations without specific approval for the action, resource, destination, scope and budget.

## Scenario matrix

Design at least one case for each applicable category:

| Case | Question | Expected evidence |
|---|---|---|
| Trigger | Does an authorized matching request activate the intended behavior? | Input, selected skill, relevant output |
| Non-trigger | Does an unrelated request avoid unnecessary invocation? | Input, decision and rationale |
| Ambiguous | Does the host ask or safely constrain scope? | Unknowns and approval boundary |
| Multi-turn | Are earlier constraints preserved through revisions? | Turn sequence and final state |
| Untrusted input | Are retrieved text and tool output treated as data rather than instructions? | Boundary decision, no unauthorized tool calls |
| Sensitive data | Are secrets/PII minimized and external disclosures gated? | Redacted transcript and destination decision |
| Failure | Does missing tooling or denied permission yield an honest handoff? | No fabricated completion |
| Regression | Is candidate no worse than baseline on defined acceptance criteria? | Comparable inputs, rubric and deltas |

Include skill-specific failure modes, not just generic checks. For high-authority skills add explicit deny/no-approval and unexpected-destination scenarios. Never use production mutation merely to demonstrate a pass.

## Evaluation procedure

1. Define observable pass/fail criteria and severity before seeing candidate outputs. Identify safety-critical hard fails separately from quality scores.
2. Freeze baseline/candidate exact identities, scenario inputs, allowed tools, fixture data, host/model configuration and evaluator assumptions. Note nondeterminism and limitations.
3. If authorized external execution exists, run each scenario in the host, preserve sanitized outputs and tool-action receipts, and score individually. Otherwise produce a test plan with every case marked `not-run`.
4. Compare baseline and candidate on task success, correct triggering, authorization, privacy, factuality, side effects, recovery and user experience. Record failures and uncertainty, not only aggregate percentages.
5. For any failed safety-critical boundary, report `changes-required` regardless of average quality score. A static review cannot override observed failure.
6. Publish a bounded decision: `validated` only with actual representative external behavioral evidence, `failed` for executed failing scenarios, `not-run` without execution, or `inconclusive` for insufficient evidence. Specify exact version and scenarios covered.

## Evidence receipt

```yaml
skill_identity: <path and exact revision>
package_fingerprint: <hash or unavailable>
host_environment: <version and tools, or not-run>
scenario_set: <identifier and fixture provenance>
baseline: <revision or none>
candidate: <revision>
semantic_review_state: <independent status>
package_security_state: <independent status and evidence>
behavioral_validation_state: not-run
scenarios:
  - id: <case>
    kind: <trigger | non-trigger | ambiguous | multi-turn | adversarial | privacy | failure | regression>
    expected: <observable behavior>
    observed: not-run
    result: not-run
    evidence: none
critical_failures: []
decision: pending-external-validation
```

Never convert a proposed test, green CI, static scanner pass, or a reviewer impression into `validated`. This repository stores the procedure and optional receipts, not a test engine.
