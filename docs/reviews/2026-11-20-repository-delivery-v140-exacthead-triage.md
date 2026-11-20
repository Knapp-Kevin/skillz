# Repository Delivery Assessor v1.4: executable source-bound portfolio triage

**Issue:** #738. **Date:** 2026-11-20. **Scope:** original independently authored nine-file standalone package.

## Exact identities and origin

- New \`SKILL.md\` Git blob: \`5e940e687efdfd835528911523c831bcd9ebb1de\`.
- New complete nine-file package Git tree: \`f423b0c8765a2da62f949b0b571f9c40f7eaf569\`.
- Executed Python implementation Git blob: \`95ea924c4690ea497823ded58e2e8c71539b6c50\`.
- Executed Python test-suite Git blob: \`0a8652b2f8c727ddcdc69beaafb01e7ae8dbad66\`.
- Previous v1.3 complete package: \`58662de287377f9b479d80cfa92e454413f9dc0e\`. Historical retirement of \`repo-doctor\` and \`repo-pulse\` is unchanged. No rights-unknown original text or source code copied.

## Actual functional increment

The v1.3 skill instructed an agent to distinguish genuine review obligations from ordinary open PRs and to avoid counting stale or skipped checks as current green. v1.4 adds a portable, offline, read-only Python 3.9+ tool that **executes** this classification over a user-authorized, supplied, bounded GitHub snapshot. It requires an explicit repository allowlist, operator, PR head SHA, per-PR check SHA, known review requests, required-check provenance flags and complete-enumeration flags.

The method produces *Needs You*, per-repository/pr notes, explicitly quiet repositories, coverage gaps, and required-check confidence without inventing an owner action. A verified empty required-check set is **NO_REQUIRED_CHECKS_DEFINED**, not a green-CI claim. Passing exact-head checks never infer merge authorization, deployment or user outcome. Off-allowlist repositories and malformed/untrusted input are rejected; the tool does not call GitHub, fetch private data, run shell based on comments, change a branch, or schedule work. The skill's original components and full diagnostic/reporting methods are preserved. CI Guard remains an **optional** external specialist, never a required dependency for downloaded standalone use.

## Executed qualification

Ran \`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q\` with Python 3.13.5: **39 tests passed, 0 failed**. The locally executed script and tests match the uploaded GitHub Git blob SHA-1s byte-for-byte.

A *real public GitHub source check* independently inspected [Skillz PR #816](https://github.com/Knapp-Kevin/skillz/pull/816) with a historical snapshot at 2026-11-20 19:20:45 UTC. PR #816 was created 19:20:25 UTC and merged 19:21:00 UTC. Before merger, there were **zero review requests** and two successful Socket Security check runs completed 19:20:33 and 19:20:36 UTC on the exact PR head. The packaged input intentionally marks branch-protection required checks, full PR listing, last-push freshness and local worktree as *unverified*. The actual checker correctly reported **Needs You = []**, preserved two head-check successes, left gate state **REQUIRED_SET_NOT_VERIFIED**, and did not invent deployment or user outcome verification. This is independent public-source grounding for the test inputs, **not** an independent skill-host performance test.

Regression coverage further checks exact-head failures and timeouts, pending/skipped/neutral/stale/duplicate checks, verified-empty required checks, review request and draft conditions, no cross-tenant scope, incomplete PR enumeration, quiet/unknown/future timestamps, unsupported fields, invalid SHA/UTC, duplicate IDs and stdout-only operation.

## Static risk and evidence classification

Maintainer static assessment **18/20**: original high-value functional behavior now includes executable source-agnostic checking; evidence truth still depends on host-authorized API responses, policy interpretation, review semantics, environment access and release outcomes. The local tests establish a bounded method's behavior, not end-to-end repository delivery quality.

No old-versus-new independent agent-host A/B, no actual user-visible repair, no audited production rollout, no complete CI gates, and **no measurable 1.5x overall skill-effectiveness improvement**. All remain **NOT_PROVEN**. The historical source rights remain **NOT_ESTABLISHED**. Previous v1.3 retirement-phase identities are preserved, with the new method tracked separately in the 44-entry ledgers.

Machine receipt: [2026-11-20-repo-delivery-v140-verified-triage.json](../evals/receipts/2026-11-20-repo-delivery-v140-verified-triage.json).
