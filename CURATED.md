# Characterized Skill Shelf

This is the human-readable view of third-party skills that have received individual characterization. It is **not** a blanket endorsement list.

The larger generated `INDEX.md` represents the available indexed library. This shelf adds provenance, exact-version quality state, tags, and freshness for a smaller reviewed subset.

Status meanings:

- **TRUSTED BASELINE**: Matt Pocock quality policy applies to this exact fingerprint; local behavioral validation is not implied.
- **VERIFIED**: structured skillz verification rubric passed for this exact fingerprint; behavioral validation is still separate.
- **UNVERIFIED**: characterized and useful as design evidence, but not yet eligible for silent trusted unchanged selection.
- **VALIDATED**: representative behavioral evidence also passed.
- **STALE**: the skill changed after assessment and must be re-reviewed.

See [`docs/curation-policy.md`](docs/curation-policy.md), [`docs/skill-verification.md`](docs/skill-verification.md), [`registry/taxonomy.yaml`](registry/taxonomy.yaml), and [`registry/verification/`](registry/verification/).

## Structured-verified sample

These non-Matt skills passed the structured quality gate. None currently claims local behavioral validation.

| Skill | Source | Status | Upstream updated | Key characterization | Provenance | Verification |
|---|---|---|---:|---|---|---|
| [Review Team](vendor/cline-skills/skills/review-team/SKILL.md) | Cline, Apache-2.0 | **VERIFIED** | 2026-05-17 | code-review, orchestration, evidence-first, human-review, mutating, medium portability | [record](registry/skills/cline-skills/review-team.yaml) | [record](registry/verification/cline-skills/review-team.yaml) |
| [Agents SDK](vendor/cloudflare-skills/skills/agents-sdk/SKILL.md) | Cloudflare, Apache-2.0 | **VERIFIED** | 2026-04-15 | agent-development, retrieval-first, retrieval-map, mutating, medium portability | [record](registry/skills/cloudflare-skills/agents-sdk.yaml) | [record](registry/verification/cloudflare-skills/agents-sdk.yaml) |
| [Google Agents CLI Eval](vendor/google-agents-cli/skills/google-agents-cli-eval/SKILL.md) | Google, Apache-2.0 | **VERIFIED** | 2026-08-28 | evaluation, metric-driven, holdout-aware, cost-bounded, external-side-effect, low portability | [record](registry/skills/google-agents-cli/google-agents-cli-eval.yaml) | [record](registry/verification/google-agents-cli/google-agents-cli-eval.yaml) |

## Matt Pocock trusted baseline sample

Source: [`mattpocock/skills`](https://github.com/mattpocock/skills), MIT, pinned at `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.

Matt Pocock is the sole source-level trusted-quality exception. The entries below are individually fingerprinted and characterized. Other Matt skills inherit source-quality confidence but are not yet fully characterized/tagged until they receive individual records.

| Skill | Status | Upstream updated | Key characterization | Provenance | Verification |
|---|---|---:|---|---|---|
| [Codebase Design](vendor/mattpocock-skills/skills/engineering/codebase-design/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | architecture, planning/design, modularity, maintainability, high portability | [record](registry/skills/mattpocock-skills/codebase-design.yaml) | [record](registry/verification/mattpocock-skills/codebase-design.yaml) |
| [Code Review](vendor/mattpocock-skills/skills/engineering/code-review/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | code-review, evaluation, spec-driven, orchestration, read-only | [record](registry/skills/mattpocock-skills/code-review.yaml) | [record](registry/verification/mattpocock-skills/code-review.yaml) |
| [Diagnosing Bugs](vendor/mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | debugging, hypothesis-driven, evidence-first, iterative, high portability | [record](registry/skills/mattpocock-skills/diagnosing-bugs.yaml) | [record](registry/verification/mattpocock-skills/diagnosing-bugs.yaml) |
| [Domain Modeling](vendor/mattpocock-skills/skills/engineering/domain-modeling/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | domain-modeling, architecture, planning, traceable, mutating | [record](registry/skills/mattpocock-skills/domain-modeling.yaml) | [record](registry/verification/mattpocock-skills/domain-modeling.yaml) |
| [Prototype](vendor/mattpocock-skills/skills/engineering/prototype/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | prototyping, UX, hypothesis-driven, visual-verification, mutating | [record](registry/skills/mattpocock-skills/prototype.yaml) | [record](registry/verification/mattpocock-skills/prototype.yaml) |
| [Research](vendor/mattpocock-skills/skills/engineering/research/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | research, source-driven, evidence-first, synthesis, high portability | [record](registry/skills/mattpocock-skills/research.yaml) | [record](registry/verification/mattpocock-skills/research.yaml) |
| [Handoff](vendor/mattpocock-skills/skills/productivity/handoff/SKILL.md) | **TRUSTED BASELINE** | 2026-08-15 | handoff, context-management, safety-bounded, high portability | [record](registry/skills/mattpocock-skills/handoff.yaml) | [record](registry/verification/mattpocock-skills/handoff.yaml) |
| [Writing for Agents](vendor/mattpocock-skills/skills/productivity/writing-for-agents/SKILL.md) | **TRUSTED BASELINE** | 2026-08-19 | skill-authoring, agent-development, progressive-disclosure, context-efficient | [record](registry/skills/mattpocock-skills/writing-for-agents.yaml) | [record](registry/verification/mattpocock-skills/writing-for-agents.yaml) |

## Addy Osmani characterized, not yet verified

Source: [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills), MIT, pinned at `f63ec56a3cc936408d792956ae583c3c96a825bd`.

These ten skills were previously source-reviewed. Under the stricter policy they are explicitly **UNVERIFIED** until they pass the new rubric. Their exact fingerprints and tags are recorded now, so future verification is version-specific rather than ceremonial.

| Skill | Status | Upstream updated | Key characterization | Provenance | Verification |
|---|---|---:|---|---|---|
| [API and Interface Design](vendor/addyosmani-agent-skills/skills/api-and-interface-design/SKILL.md) | **UNVERIFIED** | 2026-08-13 | api-design, contract-first, compatibility-aware | [record](registry/skills/addyosmani-agent-skills/api-and-interface-design.yaml) | [record](registry/verification/addyosmani-agent-skills/api-and-interface-design.yaml) |
| [Browser Testing with DevTools](vendor/addyosmani-agent-skills/skills/browser-testing-with-devtools/SKILL.md) | **UNVERIFIED** | 2026-06-11 | browser-testing, visual-verification, external-side-effect | [record](registry/skills/addyosmani-agent-skills/browser-testing-with-devtools.yaml) | [record](registry/verification/addyosmani-agent-skills/browser-testing-with-devtools.yaml) |
| [Code Review and Quality](vendor/addyosmani-agent-skills/skills/code-review-and-quality/SKILL.md) | **UNVERIFIED** | 2026-08-07 | code-review, evidence-first, risk-aware | [record](registry/skills/addyosmani-agent-skills/code-review-and-quality.yaml) | [record](registry/verification/addyosmani-agent-skills/code-review-and-quality.yaml) |
| [Code Simplification](vendor/addyosmani-agent-skills/skills/code-simplification/SKILL.md) | **UNVERIFIED** | 2026-03-31 | refactoring, behavior-preserving, incremental | [record](registry/skills/addyosmani-agent-skills/code-simplification.yaml) | [record](registry/verification/addyosmani-agent-skills/code-simplification.yaml) |
| [Context Engineering](vendor/addyosmani-agent-skills/skills/context-engineering/SKILL.md) | **UNVERIFIED** | 2026-03-31 | context-management, context-efficient, evidence-first | [record](registry/skills/addyosmani-agent-skills/context-engineering.yaml) | [record](registry/verification/addyosmani-agent-skills/context-engineering.yaml) |
| [Debugging and Error Recovery](vendor/addyosmani-agent-skills/skills/debugging-and-error-recovery/SKILL.md) | **UNVERIFIED** | 2026-07-22 | debugging, hypothesis-driven, iterative | [record](registry/skills/addyosmani-agent-skills/debugging-and-error-recovery.yaml) | [record](registry/verification/addyosmani-agent-skills/debugging-and-error-recovery.yaml) |
| [Incremental Implementation](vendor/addyosmani-agent-skills/skills/incremental-implementation/SKILL.md) | **UNVERIFIED** | 2026-08-07 | implementation, incremental, test-gated | [record](registry/skills/addyosmani-agent-skills/incremental-implementation.yaml) | [record](registry/verification/addyosmani-agent-skills/incremental-implementation.yaml) |
| [Observability and Instrumentation](vendor/addyosmani-agent-skills/skills/observability-and-instrumentation/SKILL.md) | **UNVERIFIED** | 2026-08-07 | observability, instrumentation, production-oriented | [record](registry/skills/addyosmani-agent-skills/observability-and-instrumentation.yaml) | [record](registry/verification/addyosmani-agent-skills/observability-and-instrumentation.yaml) |
| [Spec-Driven Development](vendor/addyosmani-agent-skills/skills/spec-driven-development/SKILL.md) | **UNVERIFIED** | 2026-08-14 | planning/implementation, spec-driven, traceable | [record](registry/skills/addyosmani-agent-skills/spec-driven-development.yaml) | [record](registry/verification/addyosmani-agent-skills/spec-driven-development.yaml) |
| [Test-Driven Development](vendor/addyosmani-agent-skills/skills/test-driven-development/SKILL.md) | **UNVERIFIED** | 2026-08-07 | testing, test-driven, iterative | [record](registry/skills/addyosmani-agent-skills/test-driven-development.yaml) | [record](registry/verification/addyosmani-agent-skills/test-driven-development.yaml) |

## Registered source expansion

The source registry currently contains 14 sources. OpenHands Extensions, Cline Skills, Cloudflare Skills, and Google Agents CLI are pinned vendored corpora. The Agent Skills repository is tracked as a normative specification. GitHub Awesome Copilot is tracked as a dynamic-discovery source rather than vendored wholesale.

Source inclusion never grants non-Matt skills blanket verification.
