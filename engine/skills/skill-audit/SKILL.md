---
name: skill-audit
description: >-
  Review the skillz repository's own instruction clarity, metadata consistency,
  passive-resource boundary, source/provenance records, and stale references.
  Use only for repository-maintenance review of skillz itself.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Audit
  emoji: "🔍"
  version: 2.0.0
  repo-bound: true
---

# Skill Audit

**Repository-maintenance procedure only.**

`skillz` is passive. This procedure tells the host agent how to inspect the repository semantically. It does not execute a test suite, prove model behavior, or require a runtime.

## Review flow

1. Confirm the task is `REPOSITORY_MAINTENANCE`.
2. Inspect the current front-door contract: `README.md`, `AGENT_START_HERE.md`, `BOOTSTRAP.md`, `AGENTS.md`, and `engine/skills/skill-bootstrap/SKILL.md`.
3. Check that all current instructions agree on:
   - passive repository identity;
   - one canonical normal-user orchestrator;
   - user work versus repository-maintenance boundaries;
   - current quality-state semantics;
   - capability-first discovery and component reasoning;
   - truthful host adaptation and handoff.
4. Inspect affected local skills and governed third-party records for complete provenance, metadata, authority, portability, licensing/dependency context, score, and decisive disposition.
5. Look for stale paths, deleted folders, obsolete runtime/CI/test language, contradictory counts, or old terminology that could mislead an agent.
6. Read important changed instructions adversarially for likely overreach, ambiguity, false certainty, or needless ceremony.
7. Correct material findings directly when authorized.
8. Report only unresolved material findings. If none remain, report `PASS` as a semantic review judgment.

## Negative rules

- Do not introduce CI, executable tests, scripts, preflights, or runtime proof as repository-completion requirements.
- Do not claim the repository can guarantee that an arbitrary model will follow instructions correctly.
- Do not make this maintenance procedure a prerequisite for normal first-visit or returning-user bootstrap.
- Do not treat source reputation or repository authorship as proof of individual skill quality.
