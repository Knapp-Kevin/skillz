# Local Skill Library

This directory contains the locally maintained and directly imported portion of the `skillz` library.

## Counting rule

**Every user-facing skill directory under `skills/` counts as library inventory, but `skills/` is not the entire library.**

The complete usable library also includes approved, indexed third-party skill references from the source corpus under [`vendor/`](../vendor/). Those reference skills have always been part of the repository's searchable/comparable skill inventory and continue to count as available library skills.

Repository machinery is the exception. Bootstrap, authoring, evaluation, auditing, synchronization, ecosystem scanning, and source-vetting procedures live under [`engine/skills/`](../engine/skills/) and do **not** count toward the library total.

So when someone asks, "How many skills does this repository have?", report the indexed user-facing library corpus, not merely the number of directories directly under `skills/`.

## What belongs here

A skill belongs in this directory when it is locally maintained or intentionally imported as an independently installable or reusable capability for an AI agent or user workflow.

Examples include research, writing, debugging, planning, monitoring, review, operations, domain workflows, and other capabilities that remain useful even if the `skillz` repository itself did not exist.

A skill can still be used internally by `skillz` and remain here. The deciding question is not "does skillz use it?" The deciding question is:

> Would this capability make sense for a user to install independently of maintaining `skillz`?

If yes, it belongs in the user-facing library rather than the engine.

## Third-party skills

Third-party skills directly imported into this directory must preserve applicable upstream licensing and have provenance recorded under [`registry/skills/`](../registry/skills/).

Pinned repositories under [`vendor/`](../vendor/) provide the larger reference library. Their indexed skills count as available reference skills, while individual curation and validation status are tracked separately. Presence in an approved source does not mean every skill is individually endorsed.

The useful distinction is therefore:

- **local/imported library skills**: maintained directly under `skills/`;
- **indexed reference skills**: available through approved source corpora under `vendor/`;
- **curated skills**: individually reviewed and documented;
- **validated skills**: curated skills with additional behavioral evidence;
- **engine skills**: repository machinery under `engine/skills/`, excluded from library counts.
