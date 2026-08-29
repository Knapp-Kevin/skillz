# Skill Verification Standard

Source reputation and skill quality are separate facts.

A repository may be official, popular, or professionally maintained and still contain a skill that is narrow, stale, unsafe, poorly triggered, dependency-broken, or ineffective for our use. Availability alone never establishes trusted unchanged-selection eligibility.

`skillz` is a passive instruction repository. Its quality surface is therefore the **meaning and likely interpretation of its text**, not a runtime owned by this repository. Verification and validation are semantic, reviewer-driven, and probabilistic.

## Quality lifecycle

```text
discovered -> characterized -> unverified -> verified -> validated
reviewed -> rejected | retired
any assessed state -> stale
```

- `verified` means the exact fingerprint passed the structured semantic quality gate below.
- `validated` means a verified exact version also received representative scenario/adversarial semantic review and remained coherent under those readings.
- `unverified` remains useful as design/reference evidence while review is pending but is not silently trusted for unchanged installation.
- `trusted-baseline` is retained only for historical compatibility. It is not eligible for current unchanged selection.
- `stale` means the reviewed content or material evidence changed enough that the previous judgment should not be silently inherited.
- `rejected` and `retired` are excluded from normal unchanged selection.

Neither `verified` nor `validated` is a mathematical guarantee that every model will behave identically. Models are probabilistic. The purpose of the review is to make the instruction set clear, bounded, useful, and difficult to misread, especially by a literal or weaker model.

## What is not required

Repository quality does **not** depend on:

- CI;
- an application runtime;
- a Python/Node test harness;
- executable preflight gates;
- hidden evaluator bundles;
- deterministic model-behavior claims.

Optional maintainer utilities may help with indexing or bookkeeping, but they are conveniences rather than evidence that the instructions are semantically correct.

## Hard-fail conditions

A skill cannot be promoted to `verified` while any of these are unresolved:

1. hidden or unbounded authority escalation;
2. mutation or external side effects without a clear trigger/consent boundary;
3. prompt-injection-like instructions that try to override higher-priority policy or unrelated user intent;
4. missing or broken required references, templates, or host capabilities;
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
| Dependency coherence | Referenced files, tools, packages, and host features are accurately described |
| Portability honesty | Host/platform assumptions are explicit rather than masquerading as universal |
| Usefulness/differentiation | Adds durable capability or a meaningfully stronger method than obvious prompting |
| Adversarial resilience | Resists shortcuts, looping, scope creep, confirmation bias, or unsafe interpretation |
| Effectiveness design | Contains credible mechanisms likely to improve outcomes |

Promotion to `verified` requires:

- no hard fail;
- at least **15/20** overall;
- Trigger precision, Authority and safety, and Dependency coherence each score at least `1`;
- an exact content fingerprint;
- controlled characterization tags;
- reviewer notes explaining material limitations.

## Semantic validation

`validated` is optional stronger evidence. It means the exact verified text was reviewed against representative situations rather than only rubric dimensions in isolation.

A useful semantic validation set includes:

1. a situation where the skill should trigger;
2. a situation where it should not trigger;
3. a pressure/adversarial situation targeting its most likely failure mode;
4. a literal or weaker-model reading looking for ambiguous sequencing, authority, or completion claims;
5. a check that the instruction does not create a worse or more burdensome workflow than the problem requires.

The reviewer records what was examined, the likely interpretation, any ambiguity found, and the resulting revision or disposition. The result remains probabilistic evidence about instruction quality, not executable proof.

`validation_status: not-run` simply means no separate scenario/adversarial semantic review was recorded beyond the structured verification. It is not a runtime failure and is not, by itself, a repository-completion blocker.

## Fingerprint invalidation

Verification is attached to the exact canonical `SKILL.md` blob SHA. When that content changes materially:

1. inspect the delta and dependency changes;
2. refresh provenance dates/revisions where applicable;
3. refresh the structured semantic rubric for material behavior changes;
4. repeat relevant semantic scenario review when prior validation could be invalidated;
5. update tags if scope, authority, portability, or behavior changed;
6. record the new fingerprint only after review.

No upstream source is auto-upgraded merely because a newer commit exists.

## Selection semantics

- `verified`, `validated`: eligible for unchanged consideration if fingerprint, provenance, dependencies, authority, portability, and user fit match.
- `unverified`: design evidence only by default.
- `trusted-baseline`: legacy characterization only; blocked from unchanged selection until structured review replaces it.
- `stale`, `rejected`, `retired`: excluded from normal unchanged selection.

A high-quality skill may still be a bad fit for a particular user. Verification establishes eligibility, not inevitability.