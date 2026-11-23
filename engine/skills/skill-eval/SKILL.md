---
name: skill-eval
description: >-
  Perform a structured semantic evaluation of a first-party or third-party skill
  against the repository's current quality rubric, recording strengths,
  limitations, metadata, and a decisive disposition. Use for repository curation.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Eval
  emoji: "⚖️"
  version: 2.1.0
  repo-bound: true
---

# Skill Eval

**Repository-curation procedure only.**

`skillz` evaluates instruction artifacts semantically. This procedure does not benchmark multiple models, compare baseline/treatment token counts, or claim behavioral success rates.

## Procedure

1. Establish the exact artifact being reviewed:
   - source/repository;
   - canonical path;
   - revision or other exact identity when available;
   - complete package Git tree and SKILL.md blob fingerprints when establishable (do not confuse the two);
   - applicable license and attribution.
2. Read the complete skill package, including any skill-owned scripts, references, templates, examples, fixtures, or other components that materially affect behavior.
3. Identify the capability the skill claims to provide and its expected triggers/non-triggers.
4. Review against `docs/skill-verification.md`, including:
   - clarity and procedural completeness;
   - evidence discipline;
   - authority and side effects;
   - dependencies and host assumptions;
   - privacy/security implications;
   - portability;
   - failure handling;
   - provenance/licensing;
   - overlap and differentiated value.
5. Evaluate **the promised outcome, not only structural compliance**. Derive a clear pass condition from what a real consumer needs to accomplish. Read the candidate and its supporting files against a minimal discriminating scenario set:
   - **positive trigger:** a normal task where the intended usable output is observable;
   - **negative trigger:** a neighboring task it must not activate for;
   - **high-impact failure/adversary:** false authority, untrusted instruction, missing evidence, unsafe mutation, malformed input or source substitution relevant to its scope;
   - **capability boundary:** low-context/offline/missing-tool execution and a stronger host's legitimate equivalent method, where materially relevant;
   - **counterexample:** a superficially green checklist/output that still fails the actual consumer outcome.
   Choose cases based on material risk rather than mandating five arbitrary fixtures. Record exact input, expected distinction, applicable instruction, likely result and uncertainty. These are **static reviewer interpretations**, not evidence a model executed the cases.
6. Separate whole-skill quality from component value. A skill unsuitable for unchanged reuse may still contain a useful mechanism, provided its constraints and provenance follow that mechanism.
7. Assign a rubric score and decisive disposition using `docs/skill-verification.md`. `verified` requires an **exact-version complete-package** structured semantic review with no hard fail and the rubric thresholds met. A score cannot average away a known broken user outcome, unsupported completion claim, unsafe authority, unresolved required support file or unreviewed active dependency. `validated` additionally requires **actual representative external host-executed behavioral/adversarial evidence bound to that exact package**. Static cases, local deterministic scripts, plans, and recorded test counts alone never establish observed agent behavior. A single observed success also does not establish universal model reliability.
8. Keep **four distinct evidence layers**: (a) static package and instruction review, (b) deterministic local/unit/fixture checks if run, (c) external agent-host **observed behavior**, and (d) independent consumer/user **outcome acceptance** if available. Bind each to an exact source/package version, inputs and observed output or mark NOT_RUN. Distinguish checker pass from a user accomplishing the intended task. Record behavioral validation as `not-run` when no qualifying execution exists. Keep package-security state separate under `docs/security-scanning.md`; a semantic pass never implies a scanner pass or unchanged-use eligibility. A historical `incomplete` scan stays `incomplete` even if a complete direct content review succeeds.
9. Record material caveats, including missing evidence, honestly. Audit **false positives** (an irrelevant skill looks compatible by title/metadata, polished output lacks required effect) and **false negatives** (unfamiliar vocabulary, missing map slot, weaker model, unsupported host means a sound package is rejected). For every consequential failed case identify the **smallest actionable package correction** and a regression that would detect recurrence. Do not silently downgrade a requirement, add mandatory ceremonial stages or convert unknowns into a positive assumption.
10. Record the original `reviewed_at` and the separate latest exact-identity `checked_at`, together with `current-reviewed`, `needs-re-review`, `not-yet-reviewed`, or `source-unavailable` freshness. A changed material file requires an actual new review; never transfer the previous grade by filename or mutate its historical date.
11. Update the appropriate exact-version review/provenance records and controlled tags only when authorized. If a referenced directory is too large to inspect in full, list the bounded scope reviewed and do not imply all contents were read.

## Output

```text
Skill: <name>
Exact identity: <revision, SKILL.md blob, complete package tree, or not established>
Reviewed at: <date of actual semantic review>
Checked at: <latest exact-identity verification, if any>
Freshness: current-reviewed | needs-re-review | not-yet-reviewed | source-unavailable
Material references inspected: <exact files and any bounded directory scope>
Capability: <one sentence>
Rubric score: <score>
Quality state: verified | validated | unverified | stale | rejected | retired
Authority: <classification>
Portability: <classification>
Dependencies/license: <material notes>
Semantic scenarios: <positive / non-trigger / pressure findings; static interpretation only>
Behavioral validation: <not-run / exact external executed evidence reference>
Package security: <separate exact-package state/evidence or not-run>
Differentiated value: <what it adds or duplicates>
Component value: <useful mechanisms, if any>
Disposition: <adopt unchanged / adapt / compose / reference-only / reject / retire>
Static outcome test: <promised consumer result, likely outcome, failure counterexample>
Scenario coverage: <positive, non-trigger, high-risk, capability boundary; explicit omissions>
Deterministic local checks: <exact package/test reference, observed pass/fail or not-run>
Observed consumer acceptance: <reader/task evidence, limitations or not-run>
Remediation and discriminating regression: <material defect and exact necessary correction>
Material uncertainty: <only unresolved facts>
```

## Generated skill qualification

For any candidate produced with the optional
[builder](../../builder/README.md), evaluate the **actual authored
behavior**, not the fact that a blueprint compiled or a directory
exists. Inspect the full resulting package, source rights, supported
host and every mandatory output. Apply the independent
[builder acceptance gates](../../builder/acceptance.md): positive
trigger, non-trigger, incomplete dependency, adversarial scope and
false-green outcome. The builder's local structure pass is
`LOCAL_TEST` only for the compiler's mechanics, never an automatic
`verified`, `validated` or user-accepted label.

## Skill Pack evaluation boundary

For an optional [Skill Pack](../../packs/README.md), evaluate the
**complete capability-level outcome** separately from each subskill,
phase and reusable component. Confirm local dependency closure,
acyclic handoffs, unique ownership, required/optional semantics,
authority boundaries, user-private preference isolation and
cross-component regression coverage. A passed structural manifest
check is only a static graph observation. Individual module success
does not prove orchestration success; a pack-level verdict does not
automatically certify every separately reusable subskill.

Inspect post-execution feedback with the
[improvement-versus-preference decision tree]
(../../packs/feedback-decision-tree.md). Qualify an objective defect
before proposing a canonical change, retain current user preferences
outside published source, and split MIXED feedback into independent
authority/evidence receipts. Do not promote repeated AI self-review
into independent consumer evidence.

## Repeatable review of the newly corrected candidate

Apply the shared [engine refinement handoff](../../refinement/README.md)
so that each actionable finding has a source-bound reproduction,
protected success behavior, actual counterexample, honest evidence level
and ACCEPT / ITERATE / HOLD / REVERT / STOP_NO_CHANGE decision. The
handoff does **not** confer behavioral validation, installation authority
or source licensing rights; the independent evaluation rubric remains
unchanged.


For authorized refinement, evaluate the **original artifact**, identify
the material failure and produce a bounded correction. Then evaluate
the **new exact package**, not the old score or the edit description.
Challenge the original failure, a near-miss negative case, preservation
of a previously successful case and an unrelated higher-risk boundary.
Choose the next iteration because of an evidenced new defect, not to
satisfy a preordained number of passes.

Do not self-award Gold, `verified`, or `validated` because the loop
was followed. Record separately the source change, static reviewer
judgment, actual deterministic test, host-executed behavior, real
consumer acceptance and independent package security. When evidence
is missing, the proper decision may be HOLD or STOP_NO_CHANGE. The
evaluation system itself defines the quality bar independently of a
source package's own claimed standards.

The standalone `evidence-driven-refinement-loop` authored package
generalizes this approach to ordinary user artifacts, but these
engine instructions must remain sufficient without importing it.

## Regression and iterative quality rule

When an author requests refinement, don't respond with only a new checklist.
First point to a reproducible failure or material evidence gap, then revise
the relevant instructions, support assets or parser/test where authorized.
Check that the corrected case passes by static inspection (or mark real
execution NOT_RUN), and that already-supported positive, negative and
authority scenarios remain intact. Compare the **complete package tree**
before updating the exact-version verification record. Do not transplant a
previous revision's rubric or test counts to an untested current version.

A first-party skill may be self-contained with scripts and bounded synthetic
fixtures; the **passive Skillz engine** itself does not install, execute,
schedule, or require those supports. A deterministic parser test qualifies
that parser's mechanics but does not prove a host agent or human benefited.
Optional runtime/host tests can improve confidence where worth their cost
and when permitted, never as an invented universal quality prerequisite.

## Negative rules

- Do not make model competency, benchmark success rates, token deltas, or multi-model testing a repository quality requirement.
- Do not fabricate provenance, fingerprints, license terms, dependencies, or review evidence.
- Do not treat source popularity or official branding as proof of individual skill quality.
- Do not discard skill-owned supporting components merely because they are executable or non-Markdown; evaluate them as part of the skill package.
- Do not promote an artifact beyond the evidence actually reviewed.
- Do not call a static scenario review `validated`, or inherit security approval from semantic `verified`.
