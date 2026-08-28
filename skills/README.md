# Skill Library

This directory is the actual `skillz` library.

## Counting rule

**Every skill directory under `skills/` is library inventory.**

If someone asks, "How many skills does this repository have?", this is the primary first-party/imported count that should be reported.

Repository machinery does not live here. Bootstrap, authoring, evaluation, auditing, synchronization, ecosystem scanning, and source-vetting procedures live under [`engine/skills/`](../engine/skills/) and do not count toward the library total.

## What belongs here

A skill belongs in this directory when it is useful as an independently installable or reusable capability for an AI agent or user workflow.

Examples include research, writing, debugging, planning, monitoring, review, operations, domain workflows, and other capabilities that remain useful even if the `skillz` repository itself did not exist.

A skill can still be used internally by `skillz` and remain here. The deciding question is not "does skillz use it?" The deciding question is:

> Would this capability make sense for a user to install independently of maintaining `skillz`?

If yes, it belongs in the library.

## Third-party skills

Third-party skills imported into this directory must preserve applicable upstream licensing and have provenance recorded under [`registry/skills/`](../registry/skills/).

Pinned repositories under [`vendor/`](../vendor/) are reference/source corpora. Their contents do not count as library inventory until a skill is deliberately promoted or imported into the library according to the curation policy.
