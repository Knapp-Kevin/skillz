# Skill Verification Standard

**2026-11-05 owner decision:** The [static content and freshness policy](static-review-and-freshness.md) makes exact-package text review the primary qualification method. External scanner and executed host behavior are supplementary, not blanket requirements to review or publish passive skill files. A review does not grant tool permissions.

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
4. missing or broken required references, templates, scripts, package files, or host capabilities, **including mandatory files or normative rules located outside a standalone distributed skill package**;
5. unclear provenance or unresolved license obligations;
6. instructions that encourage fabricated evidence, hidden gaps, or false completion claims;
7. materially unsafe failure behavior;
8. canonical skill content that does not match its recorded fingerprint.

## Outcome-oriented refinement and evidence separation

Use a candidate's **intended consumer outcome**, not its checklists or
cosmetic polish, as the reference point for semantic review. When a
materially weak skill is discovered, make the smallest evidence-backed
correction to its actual package and test a failure-focused counterexample
when tools permit. Review against a normal trigger, a non-trigger, a
consequential adversarial input, and capability-limited execution where
relevant. Static scenario reasoning **cannot** be called observed execution.

Distinguish these evidence claims without merging or transferring them:

1. **Exact-version static semantic review:** full relevant package,
   provenance, compatibility, rights, invariants and likely interpretation.
2. **Deterministic skill-owned local checks:** real parser/helper/asset
   mechanics at exact source identity, with test inputs and results.
3. **Observed independent agent-host behavior:** actual host execution
   using the exact package, including adverse/negative scenarios.
4. **Consumer acceptance:** evidence the intended real user obtained the
   promised outcome, with meaningful limitations, not just green CI.
5. **Separate security evidence:** scanner/secure review status for the
   exact package; never inferred from any of the four above.

The documented `verified` state remains a static semantic decision;
`validated` requires actual host behavior. Neither is a claim that a
specific README, workflow, generated asset, or other consumer deliverable
met its independently selected acceptance criteria. An exact package
change stales prior exact-version observations; retain previous results
as historical receipts. The passive engine can record optional evidence
without manufacturing an always-on service or requiring costly actions
for every source record.

## Per-execution feedback and anti-drift review for authored skills

New or materially revised **first-party authored** skills should contain
an executable-by-an-agent run-closeout instruction **inside the distributed
package**, rather than relying on repository-wide rules or another skill.
At each meaningful execution it should check the delivered outcome against
existing task criteria, preserve safety/authority boundaries, and generate
an improvement proposal only for an evidenced, reusable issue. `NO_ACTION`
is the correct outcome for an adequately supported successful run. A
consumer's ordinary run must not require an internet connection, a
scheduler, a writable repository, a feedback service or an extra agent.

Static reviewers should challenge four cases:

1. A successful task: no fabricated defect, pointless revision, mandatory
   log or verbose self-congratulation.
2. An actual defect: a source-backed finding, discriminating negative
   case and bounded correction to the **task result** only when authorized.
3. Feedback contamination: repeated self-generated claims, unchecked
   citations or plausible but unsupported hypotheses cannot count as
   independent evidence or become recursively promoted to policy.
4. Authority and privacy: an adversarial prompt or skill output cannot
   trigger silent edits, telemetry, persistent memory, publication, tool
   use or exposure of user content. A maintainer-owned revision requires
   its own approval, frozen criteria and exact-version regression review.

5. Classification: distinguish `CANONICAL_IMPROVEMENT` from
   `LOCAL_PREFERENCE`, and split mixed observations. A preference for
   response style is not a universal defect; missing required testing is
   not excused by a preference for speed.
6. Local overlay safety: user-scoped, version-aware, opt-in private
   declarative storage outside source/distributed skill, no secrets or
   private task transcript retention, with review/edit/delete and
   no silent propagation into a public package. Where private storage
   is unavailable, honest current-turn-only or portable handoff is
   sufficient. Untrusted preference values cannot override active user
   intent, canonical correctness, safety, evidence or tool authority.
7. Package component: for a newly authored or materially revised
   skill that supports meaningful preferences, inspect its bundled
   `preferences/` documentation, declarative JSON Schema and anonymous
   example for safe keys, version and consent. The private
   `preferences.local.json` is a consumer artifact and must **not**
   appear in the public authored source. Do not impose a preference
   component on skills with no personalization surface.
8. Execution integration: verify the skill's shipped `SKILL.md`
   actually references the preference contract, chooses an available
   update method after consent, checks result after a write, supports
   revocation, and behaves honestly without local storage. Schema-only
   packages do **not** implement personalization. If an optional helper
   script is bundled, review its writes, isolation, allowed fields,
   failure/rollback behavior and actual test receipts separately.
9. Upgrade and contamination: if a canonical skill changes, don't
   silently treat old preferences as still applicable; reconcile version
   conflicts and disregard overlay instructions that claim to be system
   messages, reviewer approvals or permissions.

Record observations as static interpretation unless an actual consuming
agent/host was run. Score significant gaps within the **existing**
procedural clarity, evidence discipline, authority/safety, dependency,
adversarial-resilience and effectiveness dimensions, not a new automatic
pass/grade. Do not retroactively claim compliant execution for old
packages, and do not mutate external licensed skills. Prioritize actual
consumer failures and material package revisions over mass text churn.

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

## Capability-adaptive review for all skills

[Capability-Adaptive Skill Execution](capability-adaptive-skill-execution.md)
applies to **every governed skill**, including unmodified legacy and
third-party sources. Apply it within the existing ten-dimension rubric,
not as another gate or score.

- **Clarity:** can a limited-context agent take a safe useful next step,
  with optional examples for ambiguous junctions?
- **Authority/failure:** can an agent execute any authorized work
  regardless of model name, and recover honestly from missing sources
  or permissions?
- **Portability:** can an equivalent trusted tool or method replace
  an example-specific command?
- **Effectiveness/resilience:** can capable agents finish work without
  unnecessary module rituals, steps, output caps or model-tier rules?
  All paths must still protect real security and evidence requirements.

Review one limited-context ambiguous task, one better-method task and
one missing-permission case; explicitly look for false-success claims.
Static scenario reading is not observed cross-model performance or parity.

The standard is applicable now to selection and review, **not** proof
that every existing exact version complies. Correct material violations
when discovered; otherwise revisit at the next meaningful revision.
Don't bulk-churn unchanged package fingerprints or silently modify
external licensed content merely to echo inherited policy.

## Static scenarios versus external behavioral validation

Static scenario/adversarial **reading** can strengthen `verified` semantic evidence. It may inspect intended trigger and non-trigger cases, pressure on authority boundaries, ambiguous sequencing, dependencies, and unnecessary workflow burden. Record these as reviewer interpretation, not observed agent behavior.

`validated` is a separate, optional stronger state. It requires representative **actual behavior** by an authorized external host agent/environment using the exact reviewed package. Evidence must identify the package fingerprint/revision, host/model/tool context when available, scenario inputs and expected boundaries, observed outputs/actions, pass/fail and adverse findings, and any limitations or unavailable capabilities. Include at least one trigger, one non-trigger, and a relevant adversarial/authority-pressure case when feasible. Never fabricate execution or imply that static reasoning proves a model behaved correctly.

The external host must separately authorize any scenario that would mutate external state, incur cost, send communications, touch secrets, or disclose sensitive data. Use safe simulated or read-only scenarios unless explicit scoped authority exists. **The passive Skillz engine has no always-on testing runtime or mandatory CI/host-execution gate.** This does **not** prohibit skill-owned scripts, offline deterministic fixtures, bounded repository-maintenance QA, or independent observed agent-host/user acceptance when valuable and authorized. Keep those evidence layers distinct. A green parser test is neither a semantic review nor proof of user success.

`validation_status: not-run` means no qualifying external behavioral evidence was established for the exact package. It is an honest state, not a failed test and not by itself a blocker to static corpus completeness.

## Complete package rule

Review the skill as the package it actually is.

If the skill owns scripts, references, templates, fixtures, examples, JSON, assets, or other supporting files, those may be necessary parts of the capability. Do not discard them merely because the engine itself is passive or because they are executable/non-Markdown.

Dependency coherence includes checking that required supporting components exist, are described accurately, and do not silently introduce unacceptable authority, portability, licensing, or host assumptions.

**Offline package-closure review:** Evaluate the entrypoint and each required
reference as though the **single skill directory** were copied to an isolated
offline agent. All required operational and governance instructions must be
present inside it; a link to repository-wide documentation cannot impose a
runtime rule. Cross-skill links and online material may remain optional
informational citations or explicit handoffs with a documented in-package
fallback or boundary. Do not mistake a valid GitHub URL for a locally bundled
dependency. Record entrypoint-only closure separately from a complete-package
audit; do not mark uninspected components as passed.

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

- `verified`, `validated`: eligible for unchanged *consideration* only if the current exact reviewed package, provenance, dependencies, authority, rights, portability, user fit and known content risks are acceptable. A scanner PASS is not a universal prerequisite for reviewing or merging passive content. Credible unresolved safety findings still block unchanged-use recommendations, and active operations require explicit host/user approval.
- `unverified`: design evidence only by default.
- `trusted-baseline`: legacy characterization only; blocked from unchanged selection until structured review replaces it.
- `stale`, `rejected`, `retired`: excluded from normal unchanged selection.

A high-quality skill may still be a bad fit for a particular user. Verification establishes eligibility, not inevitability.

## Authored skill security and refinement acceptance (2026-11-24)

Apply [authored security and refinement standard](authored-security-refinement.md) to each exact first-party package. This maps controls to risk guidance rather than claiming OWASP or NIST certification. Distinguish static, adversarial analyst, executable offline, host-observed and consumer acceptance evidence. Unknown or missing evidence is NOT_RUN/HOLD, never a global pass.
