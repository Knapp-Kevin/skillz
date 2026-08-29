# skillz Engine

This directory contains passive Markdown procedures that explain how to use or maintain `skillz`.

**Nothing under `engine/` counts as user-facing skill-library inventory.**

## Canonical normal user flow

For FIRST_VISIT and RETURNING_USER work, use:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md)

No other engine procedure is required for normal bootstrap.

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
