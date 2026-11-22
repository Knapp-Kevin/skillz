# Evidence-Driven Refinement Loop

**Why:** A review can produce a list of suggestions without fixing anything.
Repeated unstructured improvements can also introduce regressions or simply
make an artifact look more polished while leaving its real user outcome broken.

**What:** This reusable skill turns observed failures into bounded,
source-backed corrections, confronts each correction with counterexamples,
protects previously working behavior, and stops when the evidence warrants it.

**How:** Read [SKILL.md](SKILL.md) in any supported agent/host and point it at
a real artifact, defect, improvement goal or authorized first version. Use
a concrete before/after result as the first refinement target.

## First useful result

For a README with a jargon-heavy opening, ask the agent to apply this skill
to the real README and project sources. The desired result is an improved
README that tells a newcomer why the project matters and how to begin, not
only a list of writing tips. The reviewer should challenge the new opening
with a first-time reader task, preserve verifiable technical details, and
report any unexecuted rendered/user checks.

For a CI policy, the first unit may instead be one actual
misclassified docs-only change, a correction to the classification rule,
and positive/mixed/protected-change counterexamples. The appropriate
verification is different; the fundamental outcome standard is not.

## Contents

- [The method](#the-method)
- [Evidence levels](#evidence-levels)
- [Examples and boundaries](#examples-and-boundaries)

## The method

**Observe → Explain → Change → Challenge → Decide.** Each cycle produces
an actual revised artifact when authorized, or a supported HOLD,
REVERT or STOP_NO_CHANGE disposition when not.

The full workflow, authority rules, portable evidence capsule and stop
conditions are in [SKILL.md](SKILL.md). No scripting, network access,
scheduled automation, parent Skillz repository or specific model is required.

## Canonical skill versus local preferences

A demonstrated general bug belongs in the **canonical improvement**
proposal lane. A user's preferred level of detail or output format
belongs in a **user-local preference** lane. Mixed feedback is separated.
A consuming host may, only with user consent and suitable private
storage, retain simple non-executable settings in an isolated file
outside the downloaded skill or Skillz repository. Preferences never
weaken verification, safety or authority requirements and do not
become public skill changes merely by repetition. The skill's bundled [`preferences/`](preferences/README.md)
component contains a [JSON Schema](preferences/schema.json) and
[anonymous example](preferences/example.json); actual user values go in
an opt-in `preferences.local.json` in a private user configuration area
or a strictly private single-user installation. The [skill](SKILL.md)
retains a read-only/no-storage fallback.

The canonical `SKILL.md` includes a concrete execution hook for the
bundled [routing rules](preferences/routing.md) and optional
[offline preference manager](preferences/manage.py). This supports
allowlisted, user-consented updates, removal, version checks and
private-state validation. See the [component instructions](preferences/README.md)
for supported hosts and a no-storage fallback. The optional
[regression tests](preferences/test_manage.py) are not mandatory for
normal skill execution.

## Evidence levels

Distinguish what was written, what was actually checked, what an agent
host did, and what a real user achieved. **Green tests are not the
same as verified user value.** Keep independent security and rights
requirements as hard constraints.

## Examples and boundaries

The [anonymous adversarial cases](examples/acceptance.md) illustrate
overfitting, false progress, correct no-change decisions, missing
authority and model/host limitations. They are designed cases, not
evidence of observed host behavior.

This method complements specialized failure investigation and trial
evaluation; it does not replace them or import their runtime dependencies.
A normal read-only review never authorizes a repository edit or release.

License: [MIT](LICENSE).
