# Skill Verification Standard

Source reputation and skill quality are separate facts.

A repository may be official, popular, or professionally maintained and still contain a skill that is narrow, stale, unsafe, poorly triggered, dependency-broken, or ineffective for our use. Availability alone never establishes trusted unchanged-selection eligibility.

Every characterized skill receives an exact-version quality state according to the repository's quality policy.

## Quality lifecycle

```text
discovered -> characterized -> unverified -> verified -> validated
reviewed -> rejected | retired
any assessed state -> stale
```

- `verified` means the exact fingerprint passed the structured quality gate below.
- `validated` additionally requires representative behavioral evidence.
- `unverified` remains useful as design/reference evidence while review is pending but is not silently trusted for unchanged installation.
- `trusted-baseline` is retained in the schema vocabulary only for historical compatibility. It is not eligible for current unchanged selection and must be replaced by an individual structured review before a skill can satisfy the repository's completion standard.

`verified` and `validated` are intentionally different. Static review can establish that a skill is coherent, bounded, useful, and fit for consideration. It cannot prove that the skill improves model behavior. Behavioral evidence is required for `validated`.

The current curation finish line is stricter than the historical characterization model: every ingested user-facing skill must receive an individual structured review. A passing skill becomes `verified`; a failing unchanged skill becomes `rejected` or another explicit excluded state. No current characterized skill should remain indefinitely `unverified` or rely on source reputation as a shortcut.

## Hard-fail conditions

A skill cannot be promoted to `verified` while any of these are unresolved:

1. hidden or unbounded authority escalation;
2. mutation or external side effects without a clear trigger/consent boundary;
3. prompt-injection-like instructions that try to override higher-priority policy or unrelated user intent;
4. missing or broken required references, scripts, templates, or host capabilities;
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
| Procedural clarity | Steps are executable, ordered, and not dependent on magical inference |
| Authority and safety | Mutations, cost, privacy, approvals, and side effects are bounded |
| Failure handling | Retries, abstention, escalation, and stop conditions are explicit where needed |
| Evidence discipline | Claims of correctness/completion are tied to observable evidence |
| Dependency coherence | Referenced files, tools, packages, and host features exist and are described |
| Portability honesty | Host/platform assumptions are explicit rather than masquerading as universal |
| Usefulness/differentiation | Adds durable capability or a meaningfully stronger method than obvious prompting |
| Adversarial resilience | Resists common shortcuts, looping, scope creep, confirmation bias, or unsafe execution |
| Effectiveness design | The workflow contains credible mechanisms likely to improve outcomes, even before local behavioral validation |

Promotion to `verified` requires:

- no hard fail;
- at least **15/20** overall;
- Trigger precision, Authority and safety, and Dependency coherence each score at least `1`;
- an exact content fingerprint;
- controlled characterization tags;
- reviewer notes explaining material limitations.

## Behavioral validation

`validated` requires representative eval evidence. At minimum:

1. a case where the skill should trigger;
2. a case where it should not trigger;
3. at least one pressure/adversarial case relevant to its likely failure mode;
4. a comparison against no-skill or prior-skill behavior when practical;
5. evidence that the skill improves the intended outcome without creating unacceptable regressions.

Upstream tests may contribute evidence, but they do not automatically become local validation. Record exactly what was run or inspected.

## Hash invalidation

Verification is attached to the exact canonical `SKILL.md` blob SHA. When that hash changes:

1. mark the existing assessment stale in operational use;
2. inspect the upstream delta and dependency changes;
3. refresh provenance dates/revisions;
4. re-run the structured rubric for material behavior changes when required;
5. re-run relevant behavioral validation when prior evidence could be invalidated;
6. update tags if scope, authority, portability, or behavior changed;
7. record the new fingerprint only after review.

No upstream source is auto-upgraded merely because a newer commit exists.

## Selection semantics

- `verified`, `validated`: eligible for unchanged selection if fingerprint, tags, and user fit match.
- `unverified`: design evidence only by default; verify before direct trusted installation.
- `trusted-baseline`: legacy characterization only; blocked from unchanged selection until structured review replaces it.
- `stale`, `rejected`, `retired`: excluded from normal selection.

A high-quality skill may still be a bad fit for a particular user. Verification establishes eligibility, not inevitability.
