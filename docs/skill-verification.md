# Skill Verification Standard

Source reputation and skill quality are separate facts.

A repository may be official, popular, or professionally maintained and still contain a skill that is narrow, stale, unsafe, poorly triggered, dependency-broken, or ineffective for our use. Availability alone never establishes trusted unchanged-selection eligibility.

`skillz` is entirely passive. External host agents perform authorized assessments; this repository stores only the resulting instructions and evidence. Its semantic quality surface is therefore the **meaning and likely interpretation of its text and complete skill package**, not a user-facing runtime owned by this repository. Semantic verification and validation remain reviewer-driven and probabilistic; package-security evidence is a separate maintainer-side dimension governed by `docs/security-scanning.md`.

## Quality lifecycle

```text
discovered -> characterized -> unverified -> verified -> validated
reviewed -> rejected | retired
any assessed state -> stale
```

- `verified` means the exact fingerprint passed the structured semantic quality gate below.
- `validated` means a verified exact version additionally has actual representative external host-executed behavioral/adversarial evidence for that exact version. Static scenario reading alone cannot establish `validated`.
- `unverified` remains useful as design/reference evidence while review is pending but is not silently trusted for unchanged installation.

These semantic states do not encode package-security status. A skill may be semantically `verified` while security is `not-run`, `failed`, `incomplete`, or `stale`. Security state is recorded independently.
- `trusted-baseline` is retained only for historical compatibility. It is not eligible for current unchanged selection.
- `stale` means the reviewed content or material evidence changed enough that the previous judgment should not be silently inherited.
- `rejected` and `retired` are excluded from normal unchanged selection.

Neither `verified` nor `validated` is a mathematical guarantee that every model will behave identically, nor does either state imply that an executable/package-level security scan passed. Models are probabilistic. The repository's responsibility is to make semantic claims explicit and to keep package-security evidence separate and truthful.

## What is not required

Repository quality does **not** depend on:

- CI;
- an application runtime;
- a Python/Node test harness;
- executable preflight gates;
- hidden evaluator bundles;
- multi-model benchmarking;
- deterministic model-behavior claims;
- arbitrary behavioral success metrics.

## Hard-fail conditions

A skill cannot be promoted to `verified` while any of these are unresolved:

1. hidden or unbounded authority escalation;
2. mutation or external side effects without a clear trigger/consent boundary;
3. prompt-injection-like instructions that try to override higher-priority policy or unrelated user intent;
4. missing or broken required references, templates, scripts, package files, or host capabilities;
5. unclear provenance or unresolved license obligations;
6. instructions that encourage fabricated evidence, hidden gaps, or false completion claims;
7. materially unsafe failure behavior;
8. canonical skill content that does not match its recorded fingerprint.

## Structured verification rubric

Score each dimension `0`, `1`, or `2`:

- `0`: deficient or unsafe;
- `1`: usable but materially constrained or ambiguous;
- `2`: clear, strong, and appropriate for the claimed scope.

| Dimension | What is evaluated |
|---|---|
| Trigger precision | Clear activation and important non-trigger boundaries |
| Procedural clarity | Steps are ordered, understandable, and do not depend on magical inference |
| Authority and safety | Mutations, cost, privacy, approvals, and side effects are bounded |
| Failure handling | Abstention, escalation, recovery, and stop conditions are explicit where needed |
| Evidence discipline | Claims of correctness/completion are tied to evidence the acting agent can actually establish |
| Dependency coherence | Referenced files, tools, packages, supporting components, and host features are accurately described |
| Portability honesty | Host/platform assumptions are explicit rather than masquerading as universal |
| Usefulness/differentiation | Adds durable capability or a meaningfully stronger method than obvious prompting |
| Adversarial resilience | Resists shortcuts, looping, scope creep, confirmation bias, or unsafe interpretation |
| Effectiveness design | Contains credible mechanisms likely to improve outcomes |

Promotion to `verified` requires:

- no hard fail;
- at least **15/20** overall;
- Trigger precision, Authority and safety, and Dependency coherence each score at least `1`;
- an exact content fingerprint when establishable;
- controlled characterization tags;
- reviewer notes explaining material limitations.

## Static scenarios versus external behavioral validation

Static scenario/adversarial **reading** can strengthen `verified` semantic evidence. It may inspect intended trigger and non-trigger cases, pressure on authority boundaries, ambiguous sequencing, dependencies, and unnecessary workflow burden. Record these as reviewer interpretation, not observed agent behavior.

`validated` is a separate, optional stronger state. It requires representative **actual behavior** by an authorized external host agent/environment using the exact reviewed package. Evidence must identify the package fingerprint/revision, host/model/tool context when available, scenario inputs and expected boundaries, observed outputs/actions, pass/fail and adverse findings, and any limitations or unavailable capabilities. Include at least one trigger, one non-trigger, and a relevant adversarial/authority-pressure case when feasible. Never fabricate execution or imply that static reasoning proves a model behaved correctly.

The external host must separately authorize any scenario that would mutate external state, incur cost, send communications, touch secrets, or disclose sensitive data. Use safe simulated or read-only scenarios unless explicit scoped authority exists. No tests, harnesses, CI, runtime, or other execution machinery belong to this repository.

`validation_status: not-run` means no qualifying external behavioral evidence was established for the exact package. It is an honest state, not a failed test and not by itself a blocker to static corpus completeness.

## Complete package rule

Review the skill as the package it actually is.

If the skill owns scripts, references, templates, fixtures, examples, JSON, assets, or other supporting files, those may be necessary parts of the capability. Do not discard them merely because the engine itself is passive or because they are executable/non-Markdown.

Dependency coherence includes checking that required supporting components exist, are described accurately, and do not silently introduce unacceptable authority, portability, licensing, or host assumptions.

## Fingerprint invalidation

Verification is attached to the exact canonical skill identity recorded by the companion. When material reviewed content changes:

1. inspect the delta and dependency changes;
2. refresh provenance dates/revisions where applicable;
3. refresh the structured semantic rubric for material behavior changes;
4. re-evaluate any static scenario findings and invalidate/repeat external behavioral validation if the changed material affects previously observed behavior;
5. update tags if scope, authority, portability, or behavior changed;
6. record the new fingerprint only after review.

No upstream source is auto-upgraded merely because a newer commit exists.

## Selection semantics

- `verified`, `validated`: eligible for unchanged consideration only if fingerprint/identity, provenance, dependencies, authority, portability, user fit, and applicable package-security state also match. For scanner-compatible packages, security must be `passed` or explicitly `findings-reviewed` under `docs/security-scanning.md`.
- `unverified`: design evidence only by default.
- `trusted-baseline`: legacy characterization only; blocked from unchanged selection until structured review replaces it.
- `stale`, `rejected`, `retired`: excluded from normal unchanged selection.

A high-quality skill may still be a bad fit for a particular user. Verification establishes eligibility, not inevitability.
