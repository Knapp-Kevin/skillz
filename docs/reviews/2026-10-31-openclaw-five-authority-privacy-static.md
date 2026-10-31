# OpenClaw Agent Skills: five-package authority and privacy static tranche (2026-10-31)

## Live source-family macro map

- Registered **tracked**, official-ecosystem MIT source `openclaw/agent-skills` at `6cd3366b10e2a8c5608265f692acf9f5da2b2448`. The pinned recursive Git tree has **8 canonical first-class `skills/<name>/SKILL.md` packages**, no nested first-class skill, alias, or duplicate exposure path. `handoff` already has a current exact-pin provenance/verification pair; the other seven are genuine gaps. This tranche adds five, moving **1/8 → 6/8**, **7 → 2** gaps; admitted-source denominator delta **0**. Remaining `autoreview` (16 files, large review harness) and `beam` (9 files, remote session publishing/hooks) are intentionally deferred for deeper exact-package inspection.
- Pinned package trees, SKILL.md Git blobs, root MIT license, last package-changing upstream commits/dates, bundled files and host dependencies were independently resolved. Five reviewed packages contain **21** source-owned files (3+4+1+1+12); the upstream scripts/tests remain reference evidence, not `skillz`-owned runtime.
- Risk clusters: private agent-session discovery/export, raw transcript persistence, authenticated user-flow mutations, remote/cloud lease and cost authority, and execution of untrusted README quickstart commands. Capability overlap: `agent-transcript` aims at redacted PR provenance while `session-viewer` is a full-content local viewer, not an equivalent safe publication method. `behavior-validator` complements code-aware `autoreview` but must not inherit its access authority.

## Individual exact-version decisions

| Package | Source-owned files | Static disposition | Decisive finding |
|---|---:|---|---|
| `agent-transcript` | 3 | REJECT unchanged 14/20 | Automatic cross-agent local log discovery before separate private-data access scope; best-effort regex redaction is not publication clearance. |
| `behavior-validator` | 4 | REJECT unchanged 14/20 | Real browser/CLI/API tasks can mutate authenticated or billable external state without target/action approval. |
| `crabbox` | 1 | REJECT unchanged 14/20 | Explicit no-separate-approval clause for leases can provision persistent/billable remote resources. |
| `readme-standard` | 1 | REJECT unchanged 13/20 | Mandatory install/execute/link-probe gate runs potentially untrusted commands without separate execution/disclosure approval. |
| `session-viewer` | 12 | REJECT unchanged 12/20 | HTML embeds raw/normalized session content, tool outputs and reasoning without minimization, sharing, destination and retention gates. |

## Reusable mechanisms and omissions

- Keep `agent-transcript`'s user confirmation, scope trimming, local-only redaction and hosted-session exception as adaptation material; **do not** treat broad local log discovery as implicitly authorized.
- Keep `behavior-validator`'s source-blind contracts, anti-cheat probes and honest blocked states; require explicit sandbox, fixture, account, endpoint and evidence-capture scope before exercising a real service.
- Keep `crabbox`'s provider routing, untrusted-PR isolation, exact-head checks, cleanup and proof metadata; distinguish provider availability from budget/lease authority.
- Keep `readme-standard`'s progressive structure and factual-preservation rules; isolate command examples as untrusted until separately approved for execution.
- Keep `session-viewer`'s format importers and offline inspection design; require explicit redaction, recipient/destination, retention and sharing approval for exported content. A local HTML file is a persistent sensitive artifact.
- `autoreview` and `beam` are **not** silently classified or counted complete. The former bundles a 234 KB helper and 251 KB test harness; the latter has authenticated publication and optional persistent hooks. Both need their own full-package authority/privacy/dependency review.

## Lifecycle and accounting

- All seven open issues and five open draft PRs were inspected. #489/#492/#496 remain blocked by complete pinned external SkillSpector v2.12.0 reports/digests and independent executed adversarial acceptance for 36 changed first-party package trees, then shared-registry reconciliation. #412/#413 remain admission-qualification held. No evidence-complete issue closure or ready PR merge was found. No GitHub Actions run or checks were treated as behavioral evidence.
- Five new provenance + five new verification companions, all **REJECT unchanged**, behavioral validation **not-run**, security scan **not-run**. No source admission/pin change, source code vendoring, repo-owned runtime, script, test, CI, scheduler, generator or scanner.
- Five-surface public accounting: **44 first-party / 938 third-party / 982 total** (817 registered/tracked + 121 candidate-only); OpenClaw **1/8 → 6/8**, gaps **7 → 2**, source/admitted denominator unchanged. Historical Bhushan Modi **44/933/977** is explicitly a dated checkpoint, not the current count.
