# Dynamic discovery source-vetting: Agent Skill Exchange and j4flmao (2026-11-01)

**Decision:** TRACK both as **dynamic-discovery only** at exact observed pins. Neither source is admitted as a trusted skill corpus; no unchanged-use, installation, redistribution of upstream projects, behavioral, or security approval follows.

## Exact pinned evidence

| Source | Commit | Nontruncated Git tree | Raw SKILL.md paths | Direct-shape | Other-shape | Root terms |
|---|---|---:|---:|---:|---:|---|
| [Agent Skill Exchange](https://github.com/agentskillexchange/skills) | `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` | 6,652 entries | 3,200 | 3,196 | 4 | MIT root |
| [j4flmao/agent-skills](https://github.com/j4flmao/agent-skills) | `982203e52afe0b726a7847599a8bfb293890e0c5` | 6,145 entries | 645 | 424 | 221 | MIT root |

Each source-relative SKILL.md path has its exact Git blob SHA and containing package-tree SHA in `registry/discovery/leads/`. Shape classification is structural only. Both source trees were nontruncated. Neither count is a validated eligible or distinct skill denominator.

## Macro source review

**Agent Skill Exchange:** Root README currently advertises 3,195 published skills and 2,619 security-reviewed, while pinned tree contains 3,200 SKILL.md paths. Those are different populations; do not transfer publisher assertions into skillz verification. A sampled package (`skills/ab-test-agent-skills-mcp-changes-with-caliper/SKILL.md`) is a concise generated-looking *tool/workflow wrapper* pointing to `edonadei/caliper` as upstream. Its `verification: security_reviewed` front matter is **unverified external metadata**, not an independent skillz security scan. Every candidate needs original-source and rights checks; the root MIT license does not automatically relicense the linked upstream implementation. Source diversity is valuable for capability discovery, but synthetic/templated descriptions may be shallow and semantically duplicate original upstream skills.

**j4flmao:** The pinned root MIT license is present. A sampled `skills/ai/agentic-workflows/SKILL.md` has first-class front matter, clear trigger/non-trigger boundaries, explicit loop bounds, state-mutating approval checkpoints and an eval plan. It is useful source-level evidence but not blanket package qualification. The 221 non-direct-shape paths include nested skill packages and agent configuration paths; they require individual classification, not automatic exclusion. Bundled hooks and install instructions belong to the upstream repo; **do not execute, vendor or import them into skillz**.

## Decisions and constraints

- `agentskillexchange-skills`: **TRACK / dynamic-discovery**; original-source links and third-party claims are untrusted leads, not reviews. Per-package provenance/license and capability identity must be verified. No source admission.
- `j4flmao-agent-skills`: **TRACK / dynamic-discovery**; root MIT verified, package-local rights and authority still require individual review. No source admission.
- Both: no installation, runtime, scanner, CI, behavioral validation, source trust score, or automatic skill promotion.
- Existing two dynamic sources (GitHub Awesome Copilot 432 raw, OpenAI Plugins 536 raw) plus these two produce **4,813 raw SKILL.md paths**, **4,537 direct-shape candidates** and **276 other-shape paths**. Exact blob SHAs are distinct across these four snapshots, but this **does not rule out semantic mirrors or duplicate upstream mechanisms**.
- **4,813 is not the owner's 4,000+ eligible reviewed denominator.** It is a bounded raw discovery frontier; the final eligible distinct denominator remains unknown. Existing 995 governed third-party exact-version reviews are counted separately, not blindly added.
- Next: canonical per-package eligibility and upstream-source linkage, capability crosswalk, risk-based batches of 8–12 exact-version static decisions, and security/behavioral qualification as separate evidence.

Program: [#599](https://github.com/Knapp-Kevin/skillz/issues/599).
