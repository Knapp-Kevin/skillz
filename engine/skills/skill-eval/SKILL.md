---
name: skill-eval
description: >-
  Guides an external agent through representative behavioral evaluation of a
  skill after static review is complete. Use when a consequential or high-use
  skill needs evidence that it improves intended outcomes, when the user asks
  whether a skill actually helps, or when a verified exact version is being
  considered for validated status.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Eval
  emoji: "⚖️"
  version: 1.2.0
---

# Skill Eval

This is a passive evaluation procedure for the **external host agent** using `skillz`.

`skillz` does not run evaluations, spawn agents, execute tests, collect metrics, or change status automatically. The host agent may perform behavioral evaluation with capabilities legitimately available in its own environment and then store the resulting evidence in the repository.

Behavioral validation comes **after decisive static corpus review**, not before it. Use this skill selectively for consequential or high-use skills whose exact version already has a current verification companion. The governing standard is [`docs/skill-verification.md`](../../../docs/skill-verification.md).

## Inputs

Before evaluating, read:

1. the candidate skill itself;
2. its provenance companion under `registry/skills/<source-id>/<skill-name>.yaml`, when applicable;
3. its exact-version quality record under `registry/verification/<source-id>/<skill-name>.yaml`;
4. relevant dependencies, shared references, authority assumptions, and host requirements;
5. the intended user outcome that would make behavioral evidence useful.

Do not use source popularity, repository age, stars, or official branding as behavioral evidence.

## Evaluation procedure

1. **Confirm the exact version.** Behavioral evidence applies only to the content identity recorded in the verification companion. If the content no longer matches, stop and treat the prior evidence as stale rather than evaluating a moving target.
2. **State the claim under test.** Describe the behavior or outcome the skill is expected to improve. Keep the claim narrow enough to observe.
3. **Predefine representative cases.** At minimum include:
   - one case where the skill should trigger;
   - one case where it should not trigger;
   - one pressure or adversarial case relevant to the skill's likely failure mode.
4. **Predefine success checks.** Write observable checks before seeing results. Prefer exact properties, grounded rubric rows, authority-boundary checks, or other evidence the host can actually establish. Do not invent criteria after seeing the outputs.
5. **Establish a comparison when practical.** Compare the skill-assisted behavior with no-skill or prior-skill behavior using equivalent task framing and equivalent available context. If the host cannot isolate contexts or hold conditions reasonably constant, record that limitation explicitly.
6. **Run only through the external host.** Any model calls, subagents, browser use, code execution, tests, or other active operations occur through the host environment, not through repository machinery. Follow the host's approval, privacy, cost, and side-effect boundaries.
7. **Record observed evidence.** Capture only facts actually observed: case, expected behavior, observed behavior, relevant failures, limitations, and material cost/latency data when the host exposes it. Unavailable metrics remain unavailable.
8. **Assess regressions as well as gains.** A skill that improves one case while creating unacceptable safety, authority, reliability, or non-trigger regressions should not be promoted to `validated`.
9. **Record the result passively.** Update the exact-version verification companion with the behavioral-evidence state and concise evidence/limitations appropriate to the current schema. `validated` is appropriate only when the evidence meets the behavioral-validation contract in `docs/skill-verification.md`.

## Evidence shape

Use a compact record such as:

```text
Skill: <source-id>/<skill-name>
Exact content identity: <fingerprint/revision>
Claim under test: <narrow behavioral claim>

Cases:
- Trigger case: <task> -> <observed result against predefined check>
- Non-trigger case: <task> -> <observed result against predefined check>
- Pressure case: <task> -> <observed result against predefined check>

Comparison:
- Baseline/prior behavior: <observed evidence or not established>
- Skill-assisted behavior: <observed evidence>
- Material regressions: <none observed / details>

Limitations:
- <isolation, host capability, missing metric, sample-size, or other constraint>

Disposition:
- behavioral evidence supports validated status / does not yet support validated status
```

This is an evidence shape, not a required generated report format.

## Negative rules

- **Never fabricate a run, score, token count, latency, success rate, or comparison.** If the host did not expose or execute it, record `not established` or `not run`.
- **Never treat static verification as behavioral proof.** `verified` and `validated` answer different questions.
- **Never treat upstream tests as if they were local behavioral validation.** They may be relevant evidence, but record what they actually establish.
- **Never promote based on source reputation.** Popularity and provenance are separate from effectiveness.
- **Never require repository-owned scripts, CI, test runners, evaluators, fixtures, schedulers, or generators.** The repository stores guidance and evidence only.
- **Never weaken host safety or approval boundaries to make an evaluation easier to run.**
- **Never silently reuse behavioral evidence after the exact canonical content changes.** Reassess applicability first.

## Completion conditions

An evaluation pass is complete when:

- the exact skill version under evaluation is established;
- trigger, non-trigger, and relevant pressure cases were considered;
- success checks were defined before observing outcomes;
- comparison evidence was gathered when practical, or its absence was recorded;
- observed gains and regressions were both assessed;
- limitations are explicit;
- the repository records only evidence the external host actually established;
- any `validated` disposition satisfies the current behavioral-validation requirements in `docs/skill-verification.md`.
