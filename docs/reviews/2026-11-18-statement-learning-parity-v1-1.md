# Statement and learning replacement: functional-source review

Date: 2026-11-18. Governing issue: #738.
Reviewer: ChatGPT maintainer session.

## Historical comparator references and rights

Compared `skills/finance-review/SKILL.md`
(blob `86bdf2f9d6ebca2932612212882f6a915709203d`) and
`skills/learning-plan/SKILL.md`
(blob `7941b70fc971bf7c16c1201b7c8876f35db4ab29`)
to their newly authored versions. Historical account control
does not prove original author rights. The original artifacts
remain unchanged, and new text and cases were drafted
independently from functional output requirements.

## Function-level findings

**Statement variance reviewer:** the v1.0 replacement already
improved row lineage, credit/debit reconciliation, safe parsing,
category correctness and transfer/refund handling. However, it
restricted future-obligation reporting to explicit known records
and no longer guaranteed a monthly money digest with a clearly
labeled speculative recurring-charge forecast. V1.1 adds an
explicit files-and-coverage summary, before/after category table,
row-grounded anomalies and two different future sections:
confirmed dated obligations versus historical-pattern estimates.
It never infers active subscriptions or financial authorization
from a recurring-looking row.

**Learning evidence progression:** v1.0 improved prerequisite
graphs and applied practice, but the exact weekly plan with
source sections, allocated hours and self-gradeable checkpoints
was less specified. The recovery instruction did not explicitly
distinguish a shortfall requiring less optional work, calendar
disruption requiring a shifted timeline and an infeasible goal
requiring rescoping. V1.1 restores distinct week-by-week
deliverables, SOURCE_NOT_VERIFIED limits, and compress/shift/
rescope decision criteria without automatic enrollment, memory
writes or reminders.

## Exact three-file Git identity

All packages contain SKILL.md, LICENSE and examples/acceptance.md.
The current MIT LICENSE blob is
`023abdb34298b27580d1d303084aca942050585e`.

| Package | SKILL blob | Fixture blob | Complete tree |
| --- | --- | --- | --- |
| Statement v1.0 | `5ab4cc773e90213e2d769142ea0b4741f657ca5e` | `9eb417edf7c01a930578ec45881bb2f78a65dc72` | `08ecf062b07b632d5d5eef1cefa61abb658d5f48` |
| Statement v1.1 | `94f76bdb554fc3f3ee2b51d072ba7de067f518bd` | `c3d612d5c4d423dbbd838396b58bdd2f6f82c877` | `21118d6dda9fe0f07a9e96e361f3cd38f15cb82f` |
| Learning v1.0 | `0207ac7d4c8844f4922067cf49495437e1bea10a` | `1894f292564631f166e10e739d11d0caef59a25e` | `18052a4b7e0f574ff8530450367adab79ed0d9c6` |
| Learning v1.1 | `fcde18a06e403a24501bbe4fe804ef7f54e4a081` | `15b116ec558d7044e459a7dc172f86a62a592e0a` | `ca43eef9f7eb1b4ba5c4acef3c6c023d275037c1` |

Both historical Git trees were independently reproduced exactly
from the recorded component blobs.

## Static source review

Manually examined both revised complete packages and 16 new
synthetic scenario expectations, plus the previous source
requirements. No financial statement, spreadsheet file, live
bank system, learning web/course site, account or scheduler
was opened or changed.

Ten scores in order (trigger, procedure, authority, failure,
evidence, dependency, portability, differentiated usefulness,
adversarial resilience, effectiveness design):

| Exact package | Vector | Score | Disposition |
| --- | --- | --- | --- |
| Statement v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | VERIFIED_STATIC |
| Learning v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | VERIFIED_STATIC |

No source-level hard-fail found. The revised instructions
continue to be read-only; no account connection, financial
action, private-data export, reminders, enrollment or persistent
write is authorized. Portability is constrained by host data
parsers and actual source access. Actual effectiveness remains
unmeasured.

## Outstanding acceptance

- Numeric examples are expected outputs, not observed host-agent
  calculations or controlled predecessor comparisons.
- No real CSV/XLSX parser, balances or bank exports were assessed.
- No lesson source was independently fetched or checked live.
- No paired external-host scenarios ran. Legacy functional parity
  is NOT_RUN; 1.5x improvement NOT_PROVEN.
- Do not retire historical source packages; recheck exact-head
  index, companion records and GitHub merge state.
