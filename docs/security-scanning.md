# Skill package security scanning

## Purpose

`skillz` is **runtime-passive and maintenance-active**.

Normal consumers do not need a local shell, Python, CI, Git, or any repository-owned service to use this repository as a knowledge resource. Repository maintainers may, however, use bounded automation to establish security evidence about exact skill packages before those packages are admitted, refreshed, or represented as eligible for unchanged reuse.

Security scanning is a distinct evidence dimension. It does not replace provenance, licensing, semantic quality review, authority review, portability review, behavioral evidence, or user-fit judgment.

## Canonical scanner

The initial canonical scanner is [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector).

The repository invokes SkillSpector as an **external maintenance dependency** and does not vendor its source.

| Attribute | Value |
|---|---|
| Tool | NVIDIA SkillSpector |
| Upstream release | `v2.12.0` |
| Exact commit | `c7958a3268d9498644b22edb75d0f051bbc8cbfc` |
| License | Apache-2.0 |
| Routine mode | static-only (`--no-llm`) |
| Default gate | fail on findings or incomplete/partial analysis |
| Network behavior | declared dependency coordinates may be queried against OSV.dev; skill file contents are not sent by the static-only CI gate |

A future scanner update is a repository-maintenance decision. Do not silently follow an upstream branch or mutable tag.

## License boundary

SkillSpector is Apache-2.0. Apache-2.0 permits commercial and non-commercial use, modification, redistribution, and derivative works, and includes an express patent grant subject to its terms.

This repository keeps the integration boundary deliberately narrower:

- `skillz` remains MIT-licensed for its first-party material;
- SkillSpector source is not copied or relicensed here;
- CI installs the exact upstream revision as an external dependency;
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

## CI policy

`.github/workflows/skillspector.yml` is a **maintenance gate**, not repository runtime.

For pull requests it scans changed skill packages. For source-level changes that cannot be mapped to one package, it expands conservatively to the affected skill family. A manual full scan is available through `workflow_dispatch`.

Routine CI:

- runs static-only;
- uses no LLM credentials;
- does not schedule recurring full-corpus scans;
- fails on active findings;
- fails on incomplete analysis;
- fails closed whenever the pinned scanner reports partial or incomplete coverage;
- installs SkillSpector from the exact pinned commit.

LLM-backed SkillSpector analysis may be used manually as supplemental evidence when justified. It is not required for ordinary CI and must not silently transmit repository content to an external model provider.

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
