# Skill package security scanning

**OPTIONAL evidence, 2026-11-05:** [Current static-review policy](static-review-and-freshness.md) governs qualification of passive source files. A paid/external scanner and agent-host behavior tests are **not** required to review static content or merge qualified source repairs. This document preserves the optional scanner contract and historical receipts; it does not promote any previously `not-run`, `incomplete` or `failed` scan to PASS. Investigate credible known findings before recommending unchanged adoption.

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

For passive source publication and content review, require inspected exact package instructions/references, a decisive static quality/authority assessment, rights and source identity. An external scanner is optional, not a gate to merge these files.

For unchanged-use recommendations, require `verified` or `validated` on the **current** package, no known unresolved high-risk content findings, valid rights, compatible dependencies, privacy/authority limits and host fit. An optional scanner may add confidence, but `not-run` or `incomplete` alone is not proof the text is unsafe and is not a blanket publication blocker. Any `failed` scan with a credible unresolved finding must still be investigated, fixed or held before suggesting unchanged use. Never reuse a PASS from another tree or imply a reviewer witnessed host behavior.

Current content changes require re-review; previous semantic and scanner results remain historical at their original fingerprints.

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

## Package boundaries and incomplete engine references

Do not treat a repository-relative reference as if it were automatically bundled or scanned inside an engine skill. The [51-package first-party matrix](../registry/security/first-party-51-exact-package-security-coverage-20261104.json) reports **five engine procedures with incomplete historical scans**; the [exact reference-closure manifest](../registry/security/engine-five-reference-closure-20261104.json) pins **21 existing repository objects** at the reported missing-reference lines. Existing at the repository root **does not mean inspected** in an individual one-file engine package.

When an external scanner reports `reference_missing`, `referenced_uninspected` or `static_parse_limit`:

1. Identify the original complete package Git tree and the scanner's exact line, reference, analyzer and coverage exception.
2. Resolve a repo-root target only at an exact pinned revision. Distinguish actual files, directories, and instructional placeholders. Never follow a referenced path into an unapproved private host directory or remote account.
3. Determine whether the registered scanner's supported transitive/dependency mode can inspect all required references without changing the package being asserted. Record every target identity and observed coverage; do not equate a separately materialized closure bundle's tree with the original package's tree.
4. Reproduce parser/analysis limits on the same exact source before changing instructions or considering an updated scanner. A newer upstream fix is a hypothesis until it reproduces; changes to the canonical scanner version require owner-reviewed governance.
5. Retain `incomplete` until a real authorized rerun passes both findings and completeness gates, with a report digest, exact root/closure identities, reviewed exceptions and independent behavioral acceptance where required.

For `engine/skills/skill-eval`, the historical pinned tool reported `static_patterns_tool_misuse` / `static_parse_limit` with **zero fully inspected files**. Reference existence alone cannot clear that failure. Do not change meaningful source instructions merely to silence a parser. The repo still owns no scanner runtime or CI.

Optional LLM-backed analysis requires separate authorization for any external data transmission.

## Backfill

Optional supplementary scanning, when risk or availability warrants, may prioritize:

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

No score or source reputation dismisses a credible unresolved security finding. When a scan is attempted, its incomplete/failed outcome is preserved honestly, without rewriting an exact-version static content-review outcome.
