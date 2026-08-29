# Share-Ready Semantic Adversarial Review

Date: 2026-08-29

Status: **PASS — no unresolved material repository-level ambiguity identified**

Confidence: **high, probabilistic**

## Evaluation boundary

`skillz` is a passive instruction/reference repository. This review evaluates the meaning, structure, consistency, provenance model, and likely interpretation of the current instructions and governance metadata.

It is not CI, a runtime test, a model benchmark, a behavioral success-rate study, or proof that arbitrary models will follow the instructions correctly.

The repository's responsibility is best effort: make the route explicit, preserve useful skill packages and components, provide trustworthy metadata/provenance, bound authority, and remove avoidable ambiguity.

Primary surfaces reviewed:

- `README.md`
- `AGENT_START_HERE.md`
- `BOOTSTRAP.md`
- `AGENTS.md`
- `engine/README.md`
- `engine/skills/skill-bootstrap/SKILL.md`
- repository-maintenance engine procedures
- `docs/skill-verification.md`
- `docs/evaluation-framework.md`
- `registry/verification/`
- `registry/local-verification.json`

## Cross-cutting findings

### 1. Normal user work versus repository maintenance

**Risk:** An agent sees repository-maintenance helpers and uses them while building the user's personal skill system.

**Result:** PASS after correction.

The front door and bootstrap identify one normal orchestrator and state that normal bootstrap must not modify `skillz` or depend on engine-maintenance machinery.

### 2. Passive engine versus active skill components

**Risk:** “Passive repository” is misread as “no user-facing skill may contain executable or structured supporting files.”

**Result:** PASS after correction.

The current contract distinguishes the two explicitly:

- the **engine/repository itself** has no runtime, CI, test harness, crawler, or required executable maintenance layer;
- an individual **user-facing skill package** may legitimately include its own scripts, references, templates, fixtures, JSON, examples, or other components when those are part of the skill's authored capability.

Those components are preserved and evaluated as part of the skill package. They are not deleted merely because they are executable or non-Markdown.

### 3. Capability-first discovery

**Risk:** The first superficially similar filename is selected before the user's actual need is understood.

**Result:** PASS.

The bootstrap requires durable-need discovery and capability definition before candidate search.

### 4. Source reputation shortcut

**Risk:** Official or popular upstream material is treated as blanket trusted inventory.

**Result:** PASS.

Tracked upstream repositories are reference/discovery surfaces. Individually governed exact-version records establish stronger skill-level eligibility.

### 5. Whole-skill-only thinking

**Risk:** The only choices appear to be whole-skill adoption or custom creation.

**Result:** PASS.

The bootstrap explicitly evaluates both whole-skill fit and reusable components, with composition/adaptation/supplementation paths.

### 6. Component reuse as a governance loophole

**Risk:** A useful component is borrowed while provenance, license, dependencies, rejection reason, authority, privacy, cost, or host constraints are ignored.

**Result:** PASS.

Component reuse remains governed by the constraints that materially apply to the component.

### 7. Endless evidence/search expansion

**Risk:** More context, more sources, and more skills are treated as inherently better.

**Result:** PASS.

The bootstrap stops evidence gathering and search when additional work is unlikely to change the next decision.

### 8. Host-format assumptions

**Risk:** One platform's file layout, command syntax, or writable filesystem is treated as universal.

**Result:** PASS.

The bootstrap binds to the actual host and supports direct write, API installation, UI upload, or portable handoff according to available capability and authority.

### 9. False proof language

**Risk:** Semantic review is converted into CI, runtime proof, model benchmarking, or success-rate commitments.

**Result:** PASS after correction.

Current quality documentation defines verification and validation as semantic/probabilistic review. Model capability is outside repository responsibility.

### 10. Returning-user churn

**Risk:** An existing fitted system is rebuilt because newer references exist.

**Result:** PASS.

The returning path preserves valid behavior, re-evaluates only affected capabilities, and explicitly allows `NO CHANGE NEEDED`.

## Representative semantic scenarios

### Scenario A — governed reference fits the requirement

A recurring user workflow has explicit safeguards and an exact-version governed reference appears relevant.

Expected route: define capability → inspect exact skill package and governance record → confirm actual fit → ADOPT only when the exact reviewed package, dependencies, authority, and host assumptions fit; otherwise ADAPT/COMPOSE/CREATE.

**Assessment:** PASS.

### Scenario B — useful skill with supporting script

A selected skill contains `SKILL.md` plus a TypeScript helper required to retrieve or process its source material.

Expected route: treat both files as the skill package → characterize the script's dependency/authority/host requirements → preserve it when adopting unchanged or deliberately adapt/replace it when necessary.

Incorrect route: delete the helper because “the repository is passive.”

**Assessment:** PASS after explicit boundary correction.

### Scenario C — useful component from an unsuitable whole skill

A candidate has a strong evidence gate but the whole package has unacceptable authority assumptions.

Expected route: exclude unchanged adoption → determine whether the evidence-gate mechanism can be independently expressed within provenance/license constraints → ADAPT/SUPPLEMENT only if safe and coherent.

**Assessment:** PASS.

### Scenario D — constrained host

The agent can read repository/upstream material but cannot write files or use a local shell.

Expected route: continue discovery/composition semantically → produce a complete portable package → report actual handoff state.

**Assessment:** PASS.

### Scenario E — returning user with one changed capability

Most of the fitted system still works; one handoff requirement changed.

Expected route: preserve the rest → re-evaluate only the affected capability → make the smallest justified change.

**Assessment:** PASS.

### Scenario F — no material improvement

Existing skills still fit and new references add no established value.

Expected route: stop and return `NO CHANGE NEEDED`.

**Assessment:** PASS.

## User-facing package integrity check

A closeout tree comparison confirmed that the final architecture cleanup did **not** remove supporting components from user-facing skills.

Only three local skill directories changed during the first-party hardening pass:

1. `agent-home-doctor`
2. `deck-outline`
3. `finance-review`

Each of those directories contained only `SKILL.md` both before and after the change. No supporting scripts, references, templates, fixtures, or other package components were removed.

All other user-facing skill directory trees remained unchanged during the closeout architecture cleanup. `claude-pulse`, including its bundled `scripts/pulse.ts`, remains intact.

## First-party corpus review

All 42 active local user-facing skills have structured records in `registry/local-verification.json` covering fingerprint, score, controlled tags, authority, portability, quality state, and material notes.

Three content-level findings were corrected before closeout:

1. `agent-home-doctor` had an overly broad approval interpretation for destructive cleanup;
2. `deck-outline` depended on a rejected third-party presentation skill;
3. `finance-review` depended on a rejected third-party spreadsheet skill.

These were instruction/dependency corrections only. No legitimate supporting package components were removed.

## Accepted limitations

- Models remain probabilistic and may ignore clear instructions.
- Exact upstream identity may not be establishable in every host; the bootstrap requires honest uncertainty and conservative handling in that case.
- Tracked upstream material is broader than individually governed inventory by design.
- `validation_status: not-run` on older review records means no separate scenario-level semantic validation was recorded. It is not an unfinished runtime or model benchmark requirement.

## Closeout judgment

The current architecture is coherent enough to remain in **governed curation mode**.

No unresolved material repository-level contradiction remains in the intended first-visit/returning-user route after the closeout corrections.

Future work is discretionary curation: discover useful skills/sources, evaluate them carefully, preserve their complete relevant packages, and admit only differentiated value. Core implementation should be revisited only when real use exposes an actual documentation or architecture defect.
