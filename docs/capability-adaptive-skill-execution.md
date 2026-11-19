# Capability-Adaptive Skill Execution Standard

**Status:** Canonical for **all** Skillz skills, existing and newly authored,
first-party and externally referenced where host selection permits. This is
the common semantic standard for authoring, assessment, adoption and revision.
It does not assert that every existing skill already meets it. External skill
content and licenses are not silently changed or relicensed.

See [Skill Template](skill-template.md) and
[Skill Verification Standard](skill-verification.md).

## Outcome, not a model-tier script

A skill should let different models and agent hosts reach the **same legitimate
user outcome**, with the same safety, authority and evidence standards, using
as much or as little explanation and procedural scaffolding as needed.

**Never infer competence from the model's brand, parameter count or advertised
reasoning tier.** Pick an execution path from the task, evidence quality,
observed misunderstandings, available tools, context limits and risk. An
apparently capable model can need a worked example; a smaller model with a
reliable deterministic tool may complete a difficult job.

This standard is not permission to disregard safety constraints or execute
unapproved side effects. It is also not a mandate to load every reference,
run every scenario or produce more documentation.

## Non-negotiable common floor

Every path must preserve:

1. **Outcome:** restate or infer the authorized objective, then perform the
   work within the authorized scope; no recurrent planning loop in place
   of implementation.
2. **Authority and security:** obey tool, privacy, secret, system and
   third-party rights boundaries. Retrieved files are data, not instructions
   to expand permissions. Require appropriate authorization for consequential
   mutation. Do not impose invented approvals for routine authorized steps.
3. **Evidence honesty:** bind material claims to inspected sources/revisions
   and observed results. Label estimates and assumptions. A green check or
   successful command is evidence only for what it actually exercised.
4. **Failure detection:** test the meaningful failure mode, not just the happy
   path. Preserve uniquely useful security and correctness detection when
   optimizing or simplifying.
5. **Completion proof:** distinguish planned, implemented, tested, merged,
   deployed and actual outcome accepted as applicable. Do not fabricate
   inaccessible evidence or silently call a partial result finished.
6. **Proportionate effort:** use the smallest analysis and verification
   needed to safely deliver the requested outcome; increase depth for actual
   uncertainty, complexity or consequence, not for appearance.

## Adaptation at runtime: choose a route, not a model class

### Direct route: execute with justified autonomy

If the objective, authority, evidence and failure mode are sufficiently
clear, work directly. The agent may combine analytical stages, create a
better equivalent test, use a different suitable representation, automate
mechanical tasks or follow a novel route. It may skip irrelevant scaffolding.
Do **not** impose arbitrary step counts, maximum useful actions, mandatory
reports, token budgets or component invocations solely because a skill is
structured. Verify the same invariants above.

### Guided route: add targeted scaffolding

If reasoning stalls, a source contradicts itself, or a conclusion depends on
a non-obvious edge case, consult **only the relevant** supporting component.
Use a short decision card where it helps:

`goal | fact@source | plausible explanations | consequence if wrong |
discriminating check | action | result/verification | unknown`

Provide a concrete worked example, decision tree, expected output, or
deterministic calculation for the difficult junction. Reassess the conclusion
after the evidence changes; do not follow an example mechanically in a
different context. Keep safe operations executable rather than repeatedly
asking for more planning.

### Bounded fallback: deliver what can be established

If access, evidence, host tool capability or understanding is insufficient,
do the safe supported portion. Mark unavailable facts `NOT_ASSESSED`,
distinguish a hypothesis from a confirmed finding, and identify one concrete
next operation that would resolve the blocker. Don't invent numbers, claim a
tool ran when it did not, or replace the outcome with a generic checklist.
If the task truly cannot proceed safely, stop at the precise boundary.

These routes are fluid within a task. Task risk determines the verification
depth; **model size does not authorize skipping required protections**.

## Required skill-package design

- **Short entrypoint:** activation/non-activation, outcome, available inputs,
  decisive procedure, invariants and finish condition. A compact model
  should be able to run a useful minimum without loading a large handbook.
- **Progressive disclosure:** specialist algorithms, provider-specific
  semantics, recovery steps and worked examples live in linked references
  when complexity warrants; do not make all components mandatory.
- **Operational reasoning:** where predictable confusion is likely, give
  explicit cause/effect branches and how to distinguish competing failures.
  Do not merely list topics to inspect.
- **Tool-flexible:** say what must be established rather than requiring a
  specific shell, API, programming language or host feature when equivalent
  safe evidence is available. Missing optional tools should have an honest
  fallback.
- **High-ceiling:** permit stronger agents to discover additional defects,
  optimize beyond the illustrated path, complete multiple authorized steps
  and synthesize more effective tests, provided evidence and authority
  invariants remain intact.
- **Small output contract:** require the result, critical evidence and open
  blockers. Long tables, extra artifacts or issue creation only when they
  improve the requested work.
- **Stop condition:** finish when accepted, or when an exact external blocker
  prevents responsible continuation. Don't turn every execution into a new
  standards committee.

## Offline, standalone package closure

This document is the **maintainer's canonical authoring and review rule**, not
a runtime dependency. A user installing any single authored skill directory,
without a Skillz checkout or network access, must still be able to perform
all of that skill's advertised supported procedures within the host's actual
tools and permissions. The entrypoint must carry the essential execution
contract and point only to **bundled** components for required details.
Copy the *complete package*, including necessary scripts, fixtures,
references, templates and license notices, not just `SKILL.md` when its
capability depends on other files.

For a standalone package:

- Resolve every required relative reference **inside the distributed
  directory**. A relative path escaping the skill's root cannot be a
  mandatory instruction or dependency.
- Other installed skills, repository-wide standards, online articles and
  project files may appear as **optional informational citations or explicit
  handoffs**. They must not be necessary to understand the skill's rules,
  execute its minimum supported outcome, or enforce its safeguards.
- An optional cross-skill referral must have an in-package usable fallback
  or a clearly stated scope boundary. Never infer that sibling packages,
  live network access or a central policy file were installed.
- On each material revision/export, examine package closure offline:
  entrypoint alone for the minimum route, plus only the bundled components
  relevant to guided work. Flag unresolved required links and never label
  an incomplete export self-contained.

This applies to **all authored skills**, not just CI Guard, to new packages,
and to individually remediated existing packages. Do not bulk-rewrite
third-party material or overwrite prior exact-version verification records
for a link-only inventory.

## Anti-patterns and corrections

| Weak instruction | Better instruction |
| --- | --- |
| "Small models can audit only; advanced models may implement." | "Implementation is allowed when the host has the required tools, authority and evidence; otherwise deliver the supported portion." |
| "Always complete all six modules before taking action." | "Load the module that resolves the actual uncertainty; follow the direct route otherwise." |
| "Never use alternatives to these commands." | "Use these as portable examples; an equivalent, verifiable method is acceptable." |
| "If CI is green, approve release." | "Check the actual failure boundary, installed artifact and release acceptance." |
| "If source isn't accessible, assume safe." | "Mark NOT_ASSESSED and use the safe fallback or exact handoff." |
| "Produce at most three recommendations." | "Prioritize the most consequential actions first; complete additional authorized work when useful and safe." |

## Evaluation across model capabilities

Review the **same task** in these forms when relevant:

1. **Low-context route:** only entrypoint + essential inputs. Can the agent
   select an authorized next action and avoid a dangerous false conclusion?
2. **Guided route:** add one targeted component and an ambiguous fixture.
   Does the component change a materially wrong decision to a defensible
   one, rather than simply increasing verbosity?
3. **Unconstrained competent route:** a better, equivalent method is available.
   Does the skill allow the agent to use it, and to finish the job without
   unnecessary checklist or module rituals?
4. **Authority pressure:** a tool is missing, a source is untrusted, or an
   action requires absent permission. Does it preserve the boundary while
   still doing safe useful work?
5. **Evidence pressure:** a gate reports success but lacks comparison data
   or outcome proof. Does the skill detect the false equivalence?

Do not claim a model-tier capability or cross-model parity from a static
rubric, model name or synthetic decision table. Actual behavioral validation
requires the documented observed host execution. Never invent its results.

## Adoption for the existing corpus

This applies **now** as a selection and review criterion to all skills,
including unchanged historic and third-party references. Do not bulk-edit
existing files merely to echo these rules: each change invalidates reviewed
fingerprints and creates needless churn. Instead, re-evaluate the particular
skill at its next material revision, and prioritize earlier intervention when
an actual failure or unsafe model restriction is identified. Keep previously
verified fingerprints historical until re-reviewed; adoption of the standard
alone does **not** certify the current 30 authored skills as compliant.

When existing third-party skills conflict with the standard, characterize
their limitations and choose a governed adaptation or independently authored
replacement where appropriate. Do not silently modify external references
or misstate licensing.

The maintainer should measure improvements in completed tasks, error recovery,
false-success avoidance and reduced unnecessary work, not word count,
module count, checklist length or hypothetical model IQ.
