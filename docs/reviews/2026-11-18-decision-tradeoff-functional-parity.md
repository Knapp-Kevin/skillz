# Decision Tradeoff Workbench: source-level functional parity review

Reviewed: 2026-11-18. Issue #738. Branch `fix/738-decision-parity`.

## Comparator boundaries

Historical references:
- `skills/brief-writer/SKILL.md`, blob `bdc5411eec2eb268955c677f0b0c7c6bdba171e3`
- `skills/compare/SKILL.md`, blob `37b5d493dfa87ff1ce20e7b44d7d095e2eeed700`

These historical source texts have unresolved original authorship/rights
and remain in the corpus. Their outcomes were used as comparison evidence;
the authored source and synthetic cases are independently expressed.
Historic account ownership is not proof of original authorship.

## Pinning

| Version | SKILL blob | Cases blob | License blob | Complete package tree |
| --- | --- | --- | --- | --- |
| v1.0 historical | `671d0bdd130414c8a71c86059e21489123f08c4d` | `fd31eb5d09c39b8696772a19a86ddd44a24c02e3` | `023abdb34298b27580d1d303084aca942050585e` | `45b00d78352674b6e705704deb96af114ba4c830` |
| v1.1 proposed | `923d03cc92ab15f953528bd9ce5232bafda8a4e8` | `a05d7cd93429257ccf268e136894da0cf58dc945` | `023abdb34298b27580d1d303084aca942050585e` | `3f2e3af52d6a10faccb6a25dc1f2fa97e18e8650` |

Git tree construction independently reproduced the governed v1.0
three-file tree exactly, then computed the new tree from new blobs.

## Functional crosswalk

| Essential outcome | Prior v1.0 condition | v1.1 source remediation |
| --- | --- | --- |
| Freeze criteria before evidence-gathering | Proposed vs confirmed distinguished; no explicit phase gate | Requires confirmation first where decision-critical; otherwise provisional |
| Per-cell source and date | Present but broad output schema | Detailed dated matrix, source type, unit, uncertainty, coverage |
| Weighted evaluation | Sensitivity but no required transparent cell products | Explicit scoring rules, weight x cell score and missing-coverage treatment |
| Strong runner-up argument | Present | Preserved and anchored to evidence and threshold |
| One-page decision brief | One screen, not a hard one-page scope requirement | Bounded one-page deliverable, SCOPE_TOO_BROAD and split procedure |
| 2–4 genuine options, cost, risk, reversibility | Only general alternatives/tradeoffs | Explicit option and reversibility contract |
| Unknown cost/date/owner | Input contract generally bounded | Explicit unknowns, no invented owner acceptance |
| Hard gates, normalization, sensitivity | Strong | Retained |
| No unauthorized acquisition or action | Present | Retained |

## Complete-package static review

Reviewed actual changed `SKILL.md`, synthetic test specification and
existing MIT LICENSE. No script/tool dependency was introduced.
Reviewer: ChatGPT maintainer session, source-content inspection and
adversarial scenario reasoning.

Rubric dimensions (trigger, procedure, authority, failure handling,
evidence, dependencies, portability, usefulness, adversarial design,
effectiveness design): **2,2,2,2,2,2,1,2,2,1 = 18/20**. The portability
point is limited by host source/tool availability and the ability to
verify a physically rendered page. Effectiveness remains design-only.
No material static hard-fail was identified.

## Unproven results

- No agent-host paired run occurred against the original comparators.
- No final page rendered or measured.
- No external pricing, benchmarks, vendors, accounts or costs were queried.
- Original comparator rights remain unresolved; no source retirement.
- **Behavioral parity NOT_RUN; 1.5x improvement NOT_PROVEN.**
- Full exact-head index/companion consistency still requires check
  after source integration.

Disposition: `verified-static` for exact proposed v1.1 complete
package; not behaviorally validated.
