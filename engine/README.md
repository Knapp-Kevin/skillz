# Passive Repository-Curation Instructions

Nothing under `engine/` is an execution engine.

This directory contains **passive Agent Skills-format instructions** that teach an external AI agent how to curate, bootstrap from, evaluate, transfer, research, and maintain the `skillz` repository.

The directory name is retained for repository continuity, but it must not be interpreted as a runtime, service, process, framework, or executable subsystem.

**Nothing under `engine/` counts as user-facing skill-library inventory.**

## Maintenance instruction skills

- `skill-bootstrap`: identify durable user workflows and build the smallest fitted skill set;
- `skill-forge`: author or adapt static skill artifacts;
- `skill-eval`: guide external behavioral evaluation and evidence recording;
- `skill-audit`: guide structural, semantic, provenance, and safety review;
- `skill-sync`: guide external host transfer/installation when authorized;
- `skills-pulse`: guide limited external discovery of relevant source changes/candidates;
- `source-vetting`: guide source and candidate trust/provenance review.

These files execute nothing. Any GitHub access, web research, file editing, behavioral evaluation, installation, scheduling, or other action is performed by the external host agent using its own capabilities.

## Boundary test

A skill belongs under `engine/skills/` when its primary purpose is telling an external agent how to curate or use the `skillz` repository itself.

A skill belongs under [`../skills/`](../skills/) when it represents a reusable user-facing capability that makes sense independently of maintaining this repository.

## Passive invariant

Current files under `engine/` must not require or reference repository-owned scripts, CI, test runners, schedulers, monitors, installers, runtimes, generators, or preflight commands.

If such a reference is found, treat it as stale architecture and rewrite the instruction so the external agent performs the reasoning/action directly through its host.
