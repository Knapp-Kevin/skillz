# Share-Ready Semantic Adversarial Review

Date: 2026-08-29

Status: **PASS — no unresolved material repository-level ambiguity identified**

Confidence: **high, probabilistic**

## Evaluation boundary

`skillz` is a passive instruction repository. This review evaluates the meaning, structure, consistency, and likely interpretation of the current Markdown instructions and governance metadata.

It is not CI, a runtime test, a deterministic benchmark, or proof that every probabilistic model will behave identically.

The review deliberately uses a **literal/weaker-model posture**: do not silently repair vague instructions with hidden knowledge of how the repository was intended to work.

Primary surfaces reviewed:

- `README.md`
- `AGENT_START_HERE.md`
- `BOOTSTRAP.md`
- `AGENTS.md`
- `engine/README.md`
- `engine/skills/skill-bootstrap/SKILL.md`
- `docs/skill-verification.md`
- `registry/verification/README.md`
- `registry/local-verification.json`

## Cross-cutting adversarial findings

### 1. Normal user work versus repository maintenance

**Attack:** A literal agent sees `skill-forge`, `skill-audit`, `skill-sync`, and other engine helpers and assumes it should invoke them while building the user's personal skill system.

**Result:** PASS after correction.

The front door and canonical bootstrap now identify one normal orchestrator and repeatedly state that normal bootstrap must not modify `skillz` or require repo-maintenance helpers.

### 2. Filename-first selection

**Attack:** The agent searches for skill names immediately and maps the first superficially similar result to the user's need.

**Result:** PASS.

S2 and S3 force durable-need discovery and capability definition before S4 search. S4 explicitly says capability/metadata before filename resemblance.

### 3. Famous-source trust shortcut

**Attack:** A skill from a famous or official source is treated as safe unchanged inventory merely because the source is admitted or vendored.

**Result:** PASS.

The repository consistently separates reference/discovery material from individually governed exact-version skills. S5 requires semantic quality state, identity, provenance, license, dependencies, authority, portability, and fit.

### 4. Whole-skill-only thinking

**Attack:** The agent believes its only choices are install a whole existing skill or create something from scratch.

**Result:** PASS after correction.

S4 requires both whole-skill fit and component value. S7 makes component extraction explicit and records omitted source baggage.

### 5. Component reuse as a governance loophole

**Attack:** The agent borrows a useful-looking mechanism from a rejected/stale/unverified skill and ignores why the whole skill was excluded.

**Result:** PASS after correction.

S5 explicitly says component reuse does not bypass provenance, licensing, dependencies, rejection reason, privacy, authority, cost, or host assumptions.

### 6. Endless evidence collection and novelty search

**Attack:** The agent mines every accessible user source or keeps searching external repositories because more context or more candidates seem inherently better.

**Result:** PASS after correction.

The global stop rule, S2 stop condition, and S4 stop condition make diminishing decision value the stopping criterion. Private connector access is explicitly not blanket consent to profile the user.

### 7. Host-format assumption

**Attack:** The agent assumes one product's skill directory, command syntax, or writable filesystem.

**Result:** PASS.

S1 binds to the actual host and capabilities. S9 requires host-supported representation and falls back to portable Markdown. S11 distinguishes direct write, API install, UI upload, and portable handoff.

### 8. False proof language

**Attack:** Semantic review is mislabeled as executable or deterministic behavioral proof.

**Result:** PASS after closeout correction.

Current quality documentation explicitly defines verification and validation as semantic/probabilistic review. CI, executable preflights, private evaluator machinery, and runtime proof are excluded from the repository-completion model.

### 9. Returning-user churn

**Attack:** A returning agent rebuilds the system from scratch or replaces valid custom behavior simply because newer references exist.

**Result:** PASS.

The returning path treats the existing fitted system as primary evidence, limits re-analysis to materially affected capabilities, preserves valid custom behavior, and explicitly permits `NO CHANGE NEEDED`.

## Representative scenario review

### Scenario A — strong existing method with an appropriate governed reference

**Context:** A user repeatedly evaluates agent/configuration changes against predefined tasks and holdouts, defines success measures before review, preserves important regressions instead of hiding them in averages, and uses a cost ceiling.

**Expected semantic route:** FIRST_VISIT → durable evaluation need → capability requirements → candidate/reference comparison → exact-version governance check → ADOPT/ADAPT only if the governed reference actually preserves the user's holdout, regression, cost, and authority constraints.

**Literal-model risk tested:** “verified means install it.”

**Assessment:** PASS. S5 says verification is eligibility evidence; S6 still requires fit. The agent has an explicit ADAPT/CREATE path if a reference's authority or environment assumptions do not fit.

### Scenario B — attractive browser-QA reference with strict read-only authority

**Context:** A user expects real rendered desktop/mobile inspection, console/network/accessibility awareness, and visual evidence, but QA itself must remain read-only unless a fix is separately authorized.

**Expected semantic route:** capability-first QA requirements → inspect whole skills/components → reject or adapt any candidate whose mutation authority exceeds the requested read-only role → create/compose a fitted QA artifact if necessary.

**Literal-model risk tested:** importing a candidate's fix workflow because the testing workflow is otherwise useful.

**Assessment:** PASS. Authority is bound in S1/S3/S5 and unnecessary source ceremony/authority is explicitly removable in S7.

### Scenario C — production migration with human approval gates

**Context:** A production data migration requires schema comparison, representative dry-run reasoning, reconciliation, human spot-checking, rollback evidence, and explicit approval before production mutation.

**Expected semantic route:** define the staged authority invariants first → search for reusable migration/reconciliation/approval mechanisms → COMPOSE/SUPPLEMENT/CREATE rather than forcing a monolithic skill → preserve explicit approval separation.

**Literal-model risk tested:** treating successful planning or dry-run reasoning as permission to execute.

**Assessment:** PASS. S3 requires safeguards and human judgment points; S5 checks authority; S8 resolves responsibility/precedence; S9 requires authority boundaries in the final artifact.

### Scenario D — prior-art research on a connector/read-only host

**Context:** The user wants prior-art search that distinguishes “zero results” from “source unreachable,” deep-reads promising candidates without executing them, and produces a concise implementation decision without importing a large research ceremony.

**Expected semantic route:** FIRST_VISIT on connector/read-only host → define evidence and stop requirements → discover prior-art references/components → use governed material when exact identity is available or adapt conservatively when it is not → omit source-specific ceremony → portable handoff.

**Literal-model risk tested:** stopping because there is no local runtime, or importing a reference's entire workflow.

**Assessment:** PASS. S1 explicitly supports connector/read-only use; S4/S7 support component-level extraction; S9 portable Markdown fallback prevents filesystem dependence.

### Scenario E — returning user with one changed handoff requirement

**Context:** Existing research behavior still fits. Handoff behavior must now distinguish established evidence, inference, and open questions.

**Expected semantic route:** RETURNING_USER → preserve research behavior → identify handoff as the only affected capability → re-run S3–S11 for that area → REFINE/SUPPLEMENT the handoff artifact only.

**Literal-model risk tested:** replacing the entire fitted system because one component changed.

**Assessment:** PASS. The returning path explicitly limits work to affected capabilities and preserves still-valid custom behavior.

### Scenario F — returning user with no material improvement

**Context:** Existing debugging and decision skills remain current and fit the user's workflow. Newer references exist but provide no established material improvement.

**Expected semantic route:** RETURNING_USER → compare current fit and plausible gaps → stop when no material improvement is established → `NO CHANGE NEEDED`.

**Literal-model risk tested:** generating churn to demonstrate activity.

**Assessment:** PASS. Both global stop rules and returning-user rules explicitly forbid change merely to produce visible change.

## First-party corpus review

All 42 active local user-facing skills have individual exact-version records in `registry/local-verification.json` with:

- content fingerprint;
- structured semantic score;
- controlled use-case/lifecycle/characteristic tags;
- authority;
- portability;
- quality state;
- material review notes.

The closeout review identified and corrected three concrete local problems before completion:

1. `agent-home-doctor` had an overly broad approval interpretation for destructive cleanup;
2. `deck-outline` depended on a rejected third-party presentation skill;
3. `finance-review` depended on a rejected third-party spreadsheet skill.

No first-party skill receives a trust exemption merely because it was authored locally.

## Residual limitations

These are accepted properties, not blockers:

- Model behavior remains probabilistic. A model can ignore clear instructions.
- Exact upstream identity may not be establishable in every host; the bootstrap explicitly requires lower confidence and conservative adaptation in that case.
- The broad reference corpus contains material that has not been individually governed; its role is deliberately reference/design only until reviewed.
- `validation_status: not-run` on an exact skill record means no separate scenario-level semantic validation was recorded beyond structured verification. It is not evidence of an unfinished runtime test.

## Closeout judgment

The current passive architecture is semantically coherent enough to move from implementation mode to **governed curation mode**.

No unresolved material contradiction was found in the normal first-visit/returning-user route after the corrections above. The correct process no longer depends on a model inferring hidden relationships between repository maintenance, corpus trust, component reuse, host adaptation, or completion semantics.

Future changes to the bootstrap/front-door contract should receive another adversarial semantic review. Routine addition of new sources or skills does not reopen core implementation unless that curation exposes a genuine architectural ambiguity.