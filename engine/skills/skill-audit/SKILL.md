---
name: skill-audit
description: >-
  Review skillz repository skills and companion metadata for structural,
  safety, provenance, and consistency problems using the host agent's own
  inspection capabilities. Use when curating or auditing this repository.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Audit
  emoji: "🔍"
  version: 2.0.0
  repo-bound: true
---

# Skill Audit

This is a passive instruction set for an external agent reviewing `skillz`. It executes nothing and depends on no repository-owned script, test runner, CI job, or runtime.

## Purpose

Determine whether a skill and its companion records are coherent, useful, appropriately scoped, and honestly represented.

## Review each skill

Check the following from the files and evidence you can legitimately inspect:

1. **Identity**
   - `SKILL.md` has a clear name and trigger-bearing description.
   - The skill describes a reusable method rather than a one-off fact or preference.
   - Scope is narrow enough to be coherent and broad enough to be worth preserving.

2. **Trigger quality**
   - State when to use the skill.
   - State meaningful non-triggers where over-activation would be harmful.
   - Avoid host-specific trigger assumptions unless the skill is intentionally host-specific.

3. **Procedure quality**
   - Steps are ordered and decision points are explicit.
   - Required evidence is distinguished from inference.
   - Missing information has a conservative fallback.
   - The procedure does not rely on a repository-owned executable helper.

4. **Authority and safety**
   - Read-only analysis is distinguished from mutation or external side effects.
   - Recommendations are not treated as authorization.
   - Sensitive data is minimized.
   - The skill does not fabricate unavailable evidence or claim completion it cannot establish.

5. **Portability**
   - Host-specific tools are treated as capabilities of the external agent, not dependencies of `skillz` itself.
   - When a capability is unavailable, the skill gives a reasonable fallback or truthfully reports the limitation.

6. **Provenance and licensing**
   - Third-party material has a source, canonical path, license, pinned revision, and relationship recorded where applicable.
   - Exact-version conclusions are bound to the recorded fingerprint.
   - A source's reputation never substitutes for individual skill review.

7. **Companion metadata**
   - Provenance and verification companions agree on skill identity and source.
   - Tags describe actual behavior and authority.
   - Freshness dates and source signals are evidence-based.
   - `verified`, `validated`, `rejected`, `stale`, and other states match the evidence rather than aspiration.

8. **Redundancy and fit**
   - Compare against nearby corpus skills before creating another implementation.
   - Prefer adaptation, extraction, supplementation, or composition when that preserves the better workflow.
   - Keep a distinct skill when merging would blur responsibilities or authority.

## Semantic risk review

Explicitly look for:

- unsupported certainty;
- missing negative rules;
- mutation without an approval boundary;
- unnecessary private-data access;
- hidden external-service assumptions;
- excessive ceremony;
- source-specific terminology copied without need;
- instructions that imply `skillz` itself executes, schedules, monitors, installs, or validates anything.

## Result

For each reviewed skill, return one decisive state:

- **PASS**: no material correction required;
- **REVISE**: useful skill with a specific correctable defect;
- **ADAPT**: reference is useful but should not be reused unchanged;
- **MERGE/COMPOSE**: overlap is better handled with an existing skill relationship;
- **REJECT**: unsuitable for normal unchanged reuse;
- **RETIRE**: previously useful material should no longer be selected.

Record the evidence and make the smallest justified static repository change. Do not create executable validation machinery to prove the audit. The external reviewing agent is responsible for performing the review.
