# Curated Skill Shelf

This is the human-readable view of skills that have received individual curation review.

It complements the larger generated `INDEX.md`. A skill may appear here as:

- **vendored**: physically present in this repository through a pinned upstream source,
- **imported**: copied into this repository with its upstream obligations preserved,
- **external**: individually reviewed and worth using, but intentionally left at its upstream source until it can be brought in intact.

Every entry links to a companion provenance record under `registry/skills/`.

See [`docs/curation-policy.md`](docs/curation-policy.md) for the rules.

## Addy Osmani Agent Skills

Source: [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) · MIT · community-vetted · pinned at `f63ec56a3cc936408d792956ae583c3c96a825bd`

The full upstream source is vendored intact under `vendor/addyosmani-agent-skills`, preserving its 24 skills, shared references, tests, scripts, and license. The table below is the individually reviewed subset, not a blanket endorsement of all 24.

| Skill | Availability | Upstream last updated | Why it is here | Provenance |
|---|---|---:|---|---|
| [API and Interface Design](vendor/addyosmani-agent-skills/skills/api-and-interface-design/SKILL.md) | vendored | 2026-08-13 | Contract-first interfaces, boundary validation, idempotency safeguards | [record](registry/skills/addyosmani-agent-skills/api-and-interface-design.yaml) |
| [Browser Testing with DevTools](vendor/addyosmani-agent-skills/skills/browser-testing-with-devtools/SKILL.md) | vendored | 2026-06-11 | Browser verification with explicit isolated-profile security guidance | [record](registry/skills/addyosmani-agent-skills/browser-testing-with-devtools.yaml) |
| [Code Review and Quality](vendor/addyosmani-agent-skills/skills/code-review-and-quality/SKILL.md) | vendored, source-intact | 2026-08-07 | Strong review discipline with its shared upstream checklists preserved | [record](registry/skills/addyosmani-agent-skills/code-review-and-quality.yaml) |
| [Code Simplification](vendor/addyosmani-agent-skills/skills/code-simplification/SKILL.md) | vendored | 2026-03-31 | Behavior-preserving simplification, scope control, incremental verification | [record](registry/skills/addyosmani-agent-skills/code-simplification.yaml) |
| [Context Engineering](vendor/addyosmani-agent-skills/skills/context-engineering/SKILL.md) | vendored | 2026-03-31 | Selective context loading, trust levels, stale-context and ambiguity handling | [record](registry/skills/addyosmani-agent-skills/context-engineering.yaml) |
| [Debugging and Error Recovery](vendor/addyosmani-agent-skills/skills/debugging-and-error-recovery/SKILL.md) | vendored | 2026-07-22 | Systematic debugging with ecosystem-neutral command guidance | [record](registry/skills/addyosmani-agent-skills/debugging-and-error-recovery.yaml) |
| [Incremental Implementation](vendor/addyosmani-agent-skills/skills/incremental-implementation/SKILL.md) | vendored, source-intact | 2026-08-07 | Small-increment execution and verification boundaries | [record](registry/skills/addyosmani-agent-skills/incremental-implementation.yaml) |
| [Observability and Instrumentation](vendor/addyosmani-agent-skills/skills/observability-and-instrumentation/SKILL.md) | vendored, source-intact | 2026-08-07 | Production observability and instrumentation discipline | [record](registry/skills/addyosmani-agent-skills/observability-and-instrumentation.yaml) |
| [Test-Driven Development](vendor/addyosmani-agent-skills/skills/test-driven-development/SKILL.md) | vendored, source-intact | 2026-08-07 | Mature TDD flow with portability work and shared reference material | [record](registry/skills/addyosmani-agent-skills/test-driven-development.yaml) |
| [Spec-Driven Development](vendor/addyosmani-agent-skills/skills/spec-driven-development/SKILL.md) | vendored | 2026-08-14 | Structured spec workflow with multi-capability scope mapping | [record](registry/skills/addyosmani-agent-skills/spec-driven-development.yaml) |

## Matt Pocock Skills

Source: [`mattpocock/skills`](https://github.com/mattpocock/skills) · MIT · community-vetted · pinned in `vendor/mattpocock-skills`

| Skill | Availability | Upstream last updated | Why it is here | Provenance |
|---|---|---:|---|---|
| [Codebase Design](vendor/mattpocock-skills/skills/engineering/codebase-design/SKILL.md) | vendored | 2026-08-19 | Architecture vocabulary separated from workflow ceremony | [record](registry/skills/mattpocock-skills/codebase-design.yaml) |
| [Diagnosing Bugs](vendor/mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md) | vendored | 2026-08-19 | Tight evidence-before-hypothesis diagnostic loop | [record](registry/skills/mattpocock-skills/diagnosing-bugs.yaml) |
| [Research](vendor/mattpocock-skills/skills/engineering/research/SKILL.md) | vendored | 2026-08-19 | Independent structured evidence-gathering workflow | [record](registry/skills/mattpocock-skills/research.yaml) |

## What comes next

The next source waves should broaden the shelf rather than merely duplicate engineering patterns. Current targets include GitHub Awesome Copilot, OpenHands Extensions, Cline Skills, the Agent Skills specification/examples, Cloudflare Skills, and Google Agents CLI.

A source appearing on that target list does not mean all of its skills will be promoted. Individual skills still have to earn their shelf space.
