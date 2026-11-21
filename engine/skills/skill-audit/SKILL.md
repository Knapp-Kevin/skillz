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
  version: 2.1.0
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
5. Look for stale paths, deleted folders, obsolete runtime/CI/test language, contradictory counts, or old terminology that could mislead an agent. **Cross-check current canonical maintainer invariants against the actual tree**, especially first-party creation under `skills/authored/<slug>/`, engine instructions under `engine/skills/`, paired local provenance and verification companions, and a downloadable package's offline closure. A valid reference must not point to a removed or absent skill path.
6. Read important changed instructions adversarially for likely overreach, ambiguity, false certainty, needless ceremony, and **false completion**. Probe at least the failure mode being repaired and an adjacent negative case. Determine whether a smaller/weaker host can follow a safe fallback, a stronger host may use an equivalent method, and an executable skill's claimed output could be an attractive but unusable artifact. Static interpretation must not be reported as observed behavior.
7. Correct material findings directly when authorized. Amend the normative engine source itself when it causes repeated wrong decisions, not merely a sidecar checklist. Check that analogous instructions in Forge, Eval, Bootstrap, Pulse and current templates still agree; don't bulk-copy generic prose across unrelated packages.
8. Report the exact files reviewed, material corrections actually made, evidence for those corrections, and any unresolved findings or unavailable references. If no material findings remain, report `PASS` explicitly as a bounded **static semantic review judgment**, never as a scanner or observed host-behavior pass.

## High-impact drift probes

- **Authoring destination:** `docs/skill-template.md` and Skill Forge
  must agree on the complete new authored destination. Any `skills/<name>/`
  default for first-party creation is a material FAIL, not harmless history.
- **Discovery quality:** Bootstrap and Pulse must reject a filename, JSON
  metadata key, first page or unmapped capability slot as evidence of
  positive fit, duplicate mechanism or exhaustive absence. Scoped
  partial searches must disclose limits.
- **Evaluation depth:** Eval must distinguish exact-version static
  source review, deterministic check execution, observed agent-host
  behavior, external consumer outcome and independent package security.
  A high checklist score cannot override a known failed consumer task.
- **Portable package:** a standalone authored skill cannot require
  another parent-repository file at runtime. Skill-owned support files
  may include executable helpers when justified, but the skill must
  still respect authority and honest testing evidence.
- **Evidence freshness:** changed package support files invalidate
  exact-version conclusions until actually rechecked. Review dates
  and prior tests are preserved as history, not automatically carried.
- **Repository README:** root public documentation must not become
  a PR diary; maintenance receipts belong in appropriate records.

These are discriminating **static semantic checks**, not a claim that
another model or a consumer executed them. Report each actual failure
with exact source and actionable correction. Do not invent an always-on
audit service, CI requirement or a universal test runner.

## Negative rules

- Do not introduce CI, executable tests, scripts, preflights, or runtime proof as repository-completion requirements.
- Do not claim the repository can guarantee that an arbitrary model will follow instructions correctly.
- Do not make this maintenance procedure a prerequisite for normal first-visit or returning-user bootstrap.
- Do not treat source reputation or repository authorship as proof of individual skill quality.
