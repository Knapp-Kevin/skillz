# Issue #402: six repaired pulse packages, source-level security preflight

Date: 2026-11-04. Existing PR: #673. Scope: precisely the six historically nonpassing **previous source versions** in the 2026-11-03 external SkillSpector scan. This report describes current changed instructions as read from GitHub, not executable scanner output.

## Concrete remediation

- `hf-pulse`, `inference-pulse`, `kimi-pulse`: replace ambiguous wording with explicit permission required before changing sources, accounts, recipients or recurring access.
- `github-pulse`: public research no longer reads a private candidate registry.
- `governance-pulse`: public governance news no longer triggers local governance-file inspection; local comparison uses a supplied redacted summary.
- `mcp-pulse`: public protocol news no longer opens local MCP configuration or private candidate registries; optional local relevance depends on supplied redacted evidence.

## Exact new candidate identities

| Skill | SKILL.md Git blob SHA | Previously reported scanner state |
|---|---|---|
| hf-pulse | `149e577a9f72895b09aea43d607203d731db1bce` | failed |
| inference-pulse | `d76c0cc56bc90e7c88c2c63564ae9f24a77cca6c` | failed |
| kimi-pulse | `6625f147011dfd38ed2b9881eda2d5ea62e2ece4` | failed |
| github-pulse | `9c345c88cef5f4f97235facb6d3d7414ab820f1a` | incomplete |
| governance-pulse | `4eb7b63979fb29d997ef3ad6a10e9248e7c573ce` | incomplete |
| mcp-pulse | `33070cbc43c1bf05feeeb4e9bdd1c1d0ac04247a` | incomplete |

The previous states were measured on **older Git package trees**, not on these source blobs. These six changed packages have **not** been rescanned; do not interpret the table as six passes.

## Bounded preflight actually executed

For each of the six current exact SKILL.md blobs, fetched the companion `sources.json` and individual verification YAML from the PR branch. Checked nine properties: (1) individual fingerprint matches current source; (2) `sources.json` parses as JSON; (3) instructions describe a one-time run; (4) recurring runs need separate authorization; (5) retrieved material is untrusted; (6) targeted private local paths are absent; (7) old ambiguous `extend the scope` phrase is absent; (8) inaccessible sources are reported as gaps; (9) no repository-owned runner is claimed. **All 54/54 bounded textual/identity checks passed** on source readback.

These are simple string/JSON/static identity checks. They do not execute the skill, prove a model will obey it, inspect dependency vulnerabilities, or establish full package-tree scanner coverage. The package's `sources.json` itself was parsed, not independently security audited against every possible URL/query.

## Acceptance remains blocked

1. Export **each complete final package tree** from the pinned #673 head and record the Git package-tree SHA, file inventory and complete coverage.
2. Run NVIDIA SkillSpector at repository-registered `v2.12.0`, commit `c7958a3268d9498644b22edb75d0f051bbc8cbfc`, with `--no-llm --fail-on-findings --fail-on-incomplete --format json` in a trusted, authorized external host. Retain timestamps, report digests and finding dispositions. Any finding or incomplete coverage remains fail-closed pending an explicit maintainer decision.
3. Independently test trigger/non-trigger and adversarial host behavior with synthetic source pages, malicious retrieved instructions, unauthorized recurring delivery, missing private scope and restricted credentials. Capture actual action/response observations, not a static guess.
4. Requalify semantic grades for these new fingerprints. Reconcile the shared 44-skill registry and other open repair branches against the merge target; obtain owner/reviewer acceptance before merging.
5. Keep issue #402 and issue #415 open until the merged source and relevant security-backfill acceptance conditions actually hold.

**Environment limitation observed:** This ChatGPT container does not have SkillSpector installed, and DNS lookup for `github.com` and `pypi.org` failed. An independent trusted scanner host is required. No CI, repository-owned scanner, user private data, or external account access was used.

## Follow-up authority hardening and final source readback

A complete text review exposed three residual conflicts even after the original six-source remediation: GitHub Pulse still proposed direct local candidate-registry reading during public discovery; Inference Pulse suggested looking up host memory and profiles without prior source approval; Governance Pulse implied operator-profile discovery for public news. All three were corrected to use only already authorized or explicitly supplied user context, with a public-only fallback. A final source readback verified the six current fingerprints in the table above match their individual verification files and the provenance records. The same bounded nine checks were repeated against each revised exact source and bundled JSON: **54/54 passed**. This supersedes the earlier six source fingerprints where changed; the historical previous scanner states remain historical. The current six source versions still have **no qualifying new SkillSpector scan and no observed external-host behavioral acceptance**.
