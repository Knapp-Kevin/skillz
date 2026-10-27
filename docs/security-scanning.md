# Skill package security scanning

## Purpose

`skillz` is **entirely passive**.

The repository has no scripts, tests, CI workflows, or other active machinery. An authorized external host can use its own tools to assess exact skill packages and record the resulting evidence here before admission or unchanged reuse.

Security scanning is a distinct evidence dimension. It does not replace provenance, licensing, semantic quality review, authority review, portability review, behavioral evidence, or user-fit judgment.

## Canonical scanner

The initial canonical scanner is [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector).

An authorized external host may invoke SkillSpector at the registered exact pin. This repository does not invoke or vendor its source.

| Attribute | Value |
|---|---|
| Tool | NVIDIA SkillSpector |
| Upstream release | `v2.12.0` |
| Exact commit | `c7958a3268d9498644b22edb75d0f051bbc8cbfc` |
| License | Apache-2.0 |
| Routine mode | static-only (`--no-llm`) |
| Default gate | fail on findings or incomplete/partial analysis |
| Network behavior | declared dependency coordinates may be queried against OSV.dev; external host operators must verify scanner egress and ensure that skill content is not disclosed without authority |

A future scanner update is a repository-maintenance decision. Do not silently follow an upstream branch or mutable tag.

## License boundary

SkillSpector is Apache-2.0. Apache-2.0 permits commercial and non-commercial use, modification, redistribution, and derivative works, and includes an express patent grant subject to its terms.

This repository keeps the integration boundary deliberately narrower:

- `skillz` remains MIT-licensed for its first-party material;
- SkillSpector source is not copied or relicensed here;
- an authorized external host installs the exact upstream revision outside this repository;
- references to NVIDIA and SkillSpector are descriptive attribution, not endorsement;
- if SkillSpector source is ever vendored, modified, or redistributed from this repository, the Apache-2.0 redistribution conditions and applicable upstream/third-party notices must be reviewed and satisfied at that time.

The upstream project itself installs additional third-party open-source dependencies. Their licenses remain their own; pinning SkillSpector does not relicense them under MIT.

## Security evidence state

Security state is separate from semantic verification state.

Allowed states:

- `not-run` — no qualifying exact-version security scan is recorded.
- `passed` — the exact package completed the required scanner gate with no active findings and complete coverage.
- `findings-reviewed` — findings existed, but each has a documented disposition and the maintainer explicitly accepted the residual risk for the exact package.
- `failed` — active findings block unchanged reuse.
- `incomplete` — the scanner did not establish complete coverage or execution; treat this as fail-closed.
- `stale` — the package identity changed after the recorded scan, or the evidence can no longer be bound to the exact candidate.

A semantic `verified` record does **not** imply `passed` security state.

## Eligibility rule

For a SkillSpector-compatible exact package, new unchanged admission or refresh eligibility requires:

1. truthful provenance and exact identity;
2. semantic state `verified` or `validated`;
3. security state `passed` or `findings-reviewed`;
4. acceptable license, dependencies, authority, privacy, portability, and user fit.

`not-run`, `failed`, `incomplete`, and `stale` do not satisfy unchanged-reuse eligibility.

Existing historical semantic reviews remain valid as semantic evidence. They do not inherit a security pass. Existing packages must be backfilled rather than ceremonially re-reviewed.

## Evidence record

Persisted security evidence belongs under `registry/security/` and must bind to the exact scanned package.

At minimum record:

- canonical skill/source identity;
- exact source revision and package path;
- package fingerprint when available;
- scanner name, release, and exact scanner commit;
- scan mode and relevant gate options;
- scan timestamp;
- coverage/completeness state;
- risk score/severity/recommendation;
- active finding identifiers and dispositions;
- final security state;
- evidence location or report digest;
- reviewer and rationale when using `findings-reviewed`.

Do not copy volatile scan output into semantic verification fields.

## External host assessment policy

The repository owns no CI workflow, runner, script, scheduled job or scanner process. An authorized external host may scan relevant pinned packages using its own environment and the exact registered scanner commit. Preserve the actual target package identity, revision, scan arguments, complete coverage proof, severity/findings, report digest and resulting disposition under `registry/security/`.

A qualifying static assessment uses no LLM credentials, fails closed on active findings or incomplete analysis, and does not disclose private content or credentials to third parties without explicit authority. Host-generated reports are evidence only; do not imply a scan ran unless the host actually executed it. Historical CI results may be retained as dated evidence of their scanned versions, not as a current repository automation requirement.

Optional LLM-backed analysis requires separate authorization for any external data transmission.

## Backfill

The current corpus predates this control. Backfill should prioritize:

1. first-party skills;
2. currently `verified` or `validated` third-party packages with executable components or consequential authority;
3. remaining unchanged-reuse candidates;
4. reference-only and rejected material only when a future decision makes the scan relevant.

Backfill changes security state only. It must not erase compatible provenance or semantic-review evidence.

## Failure handling

A scanner failure is evidence of uncertainty, not evidence of safety.

- scanner execution error -> `incomplete`;
- partial coverage -> `incomplete`;
- active unaccepted finding -> `failed`;
- package changed after scan -> `stale`;
- accepted false positive or bounded residual risk -> `findings-reviewed` with explicit rationale.

No average score, source reputation, or semantic-review score may override a fail-closed security state.
