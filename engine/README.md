# skillz Engine

This directory contains passive Markdown procedures that explain how to use or maintain `skillz`.

**Nothing under `engine/` counts as user-facing skill-library inventory.**

## Canonical normal user flow

For SINGLE_SKILL_BUILD, FIRST_VISIT and RETURNING_USER work, use:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md)

No other engine procedure is required for normal bootstrap.

A single-skill creation request follows the focused route inside this same
orchestrator. It does not require a whole fitted-system interview or call
repository-maintenance Forge.

## Optional deterministic builder

[Skill builder](builder/README.md) accepts an agent-authored original-content
blueprint and emits one standalone skill, an internally phased skill or a
[Skill Pack](packs/README.md). Its optional Python-standard-library compiler
has a read-only planning default, an explicit non-overwriting write mode
and truthful draft/evidence receipts. It **does not invent task instructions**,
authorize host actions, certify rights, install packages or qualify
consumer behavior. Any host without Python may follow the same template
contract manually; Bootstrap remains the one normal orchestrator.

The [optional design preflight](builder/design-contract.md) checks author-supplied
evidence IDs, task obligations, proposed adversarial probes and their
mapping to an original-content blueprint before invoking that same
compiler. No inference or actual task execution is claimed.

The [source-blind feedback boundary](refinement/feedback-boundary.md)
provides an optional enum-only offline guard against identity-bearing
consumer feedback becoming canonical instructions. It does not collect
telemetry, authenticate evidence or authorize a change.

## Required host compatibility guard

The builder and design gate enforce the same static package preflight
before any destination write. Authors identify the actual target surface
and capability constraints before drafting, pass explicit `--host` targets
or use the all-configured-profiles baseline when unknown, and resolve known
blockers before handoff. Existing or manually authored custom packages
can use `host_compat.py --package`; hosts without Python apply the same
rules manually. Package readiness does not prove native loading,
runtime functionality or user acceptance.

## Shared refinement mechanism

[Engine refinement handoff](refinement/README.md) is the common procedure
used by Bootstrap, Forge and Eval for outcome-based, evidence-labeled,
bounded refinement. It carries an optional fictional portable case
receipt, not background work or mandatory telemetry. **No additional
user-facing skill or runtime service is introduced.**

## Optional Skill Pack composition

The [Skill Pack architecture and manifest](packs/README.md) lets one
capability be a self-contained skill, an internally phased skill, or
a pack containing independently meaningful subskills, phases and
components. Its [feedback decision tree](packs/feedback-decision-tree.md)
separates canonical corrections from private, opt-in consumer preferences.
It reuses Bootstrap, Forge, Eval and the refinement handoff, **not** a
second engine, automatic updater, hosted runtime or new release cadence.

## Repository-maintenance procedures

Other procedures support occasional curation or maintenance, such as:

- `skill-forge`: create a new first-party skill in this repository when explicitly requested;
- `skill-audit`: semantically review repository clarity and metadata consistency;
- `skill-eval`: structure semantic evaluation evidence;
- `skill-sync`: describe an explicitly requested host-mediated export/copy;
- `skills-pulse`: perform an on-demand external skill discovery pass;
- `source-vetting`: assess an external source before admission.

They are instructions for the host agent, not executable services, scripts, CI gates, or a runtime.

## Critical boundary

During normal user work:

- do not write the user's custom skills into this repository by default;
- do not require shell, Git, Node/Bun, CI, submodules, or local scripts;
- do not invoke repository-maintenance procedures merely because they are visible;
- create/package artifacts for the user's actual host or provide a portable handoff.

## Quality boundary

The repository owns the quality of its instructions, metadata, provenance, and best-effort semantic review. It does not guarantee that any particular model is capable of following them.

See [`../docs/skill-verification.md`](../docs/skill-verification.md) and [`../docs/evals/share-ready-semantic-review.md`](../docs/evals/share-ready-semantic-review.md).
