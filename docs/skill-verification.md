# Skill Verification Standard

Source reputation and individual skill quality are separate facts.

`skillz` does not run a verifier. This document tells an **external reviewing agent** how to assess a skill and how to record that assessment passively in `registry/verification/`.

A repository may be official, popular, or professionally maintained and still contain a skill that is narrow, stale, unsafe, poorly triggered, dependency-broken, or ineffective for a particular use. Availability alone never establishes unchanged-reuse eligibility.

## Quality lifecycle

```text
discovered -> characterized -> unverified -> verified -> validated
reviewed -> rejected | retired
any assessed state -> stale
```

- `verified` means an external reviewing agent found that this exact version satisfies the structured static-review standard below.
- `validated` additionally means representative behavioral evidence has been recorded.
- `unverified` remains useful as design/reference evidence while review is pending, but is not trusted for unchanged reuse by default.
- `rejected` means the exact version should not be reused unchanged under the current policy. Useful patterns may still be extracted or adapted where licensing and safety permit.
- `retired` means the prior record is intentionally no longer active for normal selection.
- `stale` means previously recorded evidence no longer establishes the current content state.
- `trusted-baseline` may appear in historical records but does not satisfy the current completion standard without individual review.

Static review can establish that a skill is coherent, bounded, useful, attributable, and eligible for consideration. It cannot prove that the skill improves model behavior. Behavioral evidence is required for `validated`.

## Passive verification invariant

Verification is evidence, not a repository process.

- The external agent reads the skill and relevant companion/source material.
- The external agent applies the rubric.
- The repository stores the resulting status, evidence, tags, limitations, and exact content identity.
- No script, test runner, CI workflow, runtime, preflight command, or background service is required or implied.
- If the external agent cannot establish an exact fact, it records the limitation instead of inferring success.

## Hard-fail conditions

A skill cannot be recorded as `verified` while any of these are unresolved:

1. hidden or unbounded authority escalation;
2. mutation or external side effects without a clear trigger/consent boundary;
3. instructions that attempt to override higher-priority policy or unrelated user intent;
4. missing, broken, or undisclosed required references, templates, assets, code, packages, tools, or host capabilities;
5. unclear provenance or unresolved license obligations;
6. instructions that encourage fabricated evidence, hidden gaps, or false completion claims;
7. materially unsafe failure behavior;
8. inability to establish the exact canonical content identity that the assessment is meant to describe.

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
| Failure handling | Abstention, escalation, retries, and stop conditions are explicit where needed |
| Evidence discipline | Claims of correctness/completion are tied to observable evidence |
| Dependency coherence | Referenced files, tools, packages, assets, and host features are present or honestly described |
| Portability honesty | Host/platform assumptions are explicit rather than presented as universal |
| Usefulness/differentiation | Adds durable capability or a meaningfully stronger method than obvious prompting |
| Adversarial resilience | Resists shortcuts, looping, scope creep, confirmation bias, or unsafe execution |
| Effectiveness design | Contains credible mechanisms likely to improve outcomes before behavioral validation |

Recording `verified` requires:

- no hard fail;
- at least **15/20** overall;
- Trigger precision, Authority and safety, and Dependency coherence each score at least `1`;
- an exact content identity for the reviewed version when establishable from the source host;
- controlled characterization tags;
- reviewer notes describing material limitations and assumptions.

The score is evidence for the decision, not an automatic machine promotion rule.

## Behavioral validation

`validated` requires representative external evaluation evidence. At minimum, the recorded evidence should cover:

1. a case where the skill should trigger;
2. a case where it should not trigger;
3. at least one pressure/adversarial case relevant to its likely failure mode;
4. comparison against no-skill or prior-skill behavior when practical;
5. evidence that the skill improves the intended outcome without unacceptable regressions.

Behavioral evaluation happens in the external agent/host environment. The repository stores only the instructions and resulting evidence.

Upstream tests may inform review, but they do not automatically become local behavioral validation. Record exactly what evidence was inspected or produced.

## Content-change invalidation

Verification applies only to the exact content version described by its companion record.

When the canonical skill content changes, an external reviewing agent should:

1. treat the prior exact-version assessment as stale for unchanged reuse;
2. inspect the upstream delta and dependency changes;
3. update provenance revision/date evidence;
4. apply the structured rubric again when behavior or material assumptions changed;
5. revisit behavioral evidence when prior evidence may no longer describe the new version;
6. update tags if scope, authority, portability, or behavior changed;
7. record the new content identity only after review.

No upstream source or individual skill is automatically promoted because a newer commit exists.

## Selection semantics

- `verified`, `validated`: eligible for unchanged consideration when exact content identity and user fit match.
- `unverified`: design/reference evidence by default; review before trusted unchanged reuse.
- `trusted-baseline`: historical characterization only; not sufficient for current static completion.
- `stale`, `rejected`, `retired`: excluded from normal unchanged selection.

A high-quality skill may still be a bad fit for a particular user. Verification establishes eligibility for consideration, not inevitability of reuse.
