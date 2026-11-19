# Final two replacement source comparisons: schedule receipts and fact checking

Date: 2026-11-18. Governed functional audit issue #738.
This is a manual **source-level** review, not agent-host behavioral
acceptance or a license adjudication.

## Historical references and rights

- `skills/automation-receipts/SKILL.md` Git blob
  `94fb288d7d6a3ea6982f22bd8bb9ef77b9de7add`
- `skills/fact-check/SKILL.md` Git blob
  `d83c43282d525682f3e13b8296111d7fe7de46f0`

Historical account ownership/author strings do not establish who
created the expression or convey an unrestricted right to license
it as new work. Original historical files and all their evidence
remain unchanged. New scheduled-auditor instructions and cases
were drafted independently from functional requirements.

## Scheduled Work Proof Auditor v1.1: changed

The v1.0 replacement already distinguished configuration, trigger,
execution, artifact existence/correctness and recipient delivery
more carefully than its predecessor. A residual source-level
loss was the predecessor's explicit durable receipt inventory
including the persistence location, last run, exit status, next
fire eligibility and **durable log path/equivalent** when claimed
automation status mattered. It also needed a more explicit
PAUSED-versus-RUNNING distinction.

V1.1 adds a job-specific durable receipt contract and precise
stage/overall statuses, accepting equally durable scheduler
run-record APIs instead of mandating invented filesystem paths.
Prior successful execution does not prove ongoing scheduling or
current run state. Inaccessible logs remain UNKNOWN; no private
account or scheduler access expansion is authorized. The skill
remains read-only and does not create, restart or edit a task.

Old v1.0 complete package Git tree was independently
reconstructed exactly from its historical blob identifiers.

| Version | SKILL blob | Cases blob | Complete tree |
| --- | --- | --- | --- |
| Scheduled Work v1.0 | `eccc5704701e8bba391bece41da7d74bba156403` | `c3895f7b4554544fc70f2be0b7add1cf99b8a91a` | `951eb6f5d91f1e035ffeb4835255864d595eee61` |
| Scheduled Work v1.1 | `22fe02a8dc2b021c4badaeb1028f3e492ad8e12b` | `a6198bd9faafaefc8f0de9a93f7027275a427852` | `bd9254ce997d807b1bfe91c820b820fd51ae9cfc` |

The three-file package retains MIT LICENSE blob
`023abdb34298b27580d1d303084aca942050585e`.

Manual structured rubric in canonical ten-dimension order:
`2,2,2,2,2,2,1,2,2,1` = **18/20**, with no
source-level hard-fail identified. Nine new synthetic expected
outcomes were examined, not executed. Portability depends
on supported scheduler read interfaces.

## Claim Evidence Adjudicator v1.0: reviewed unchanged

The original fact-check skill requires independently
testable component claims, primary evidence and date lineage,
including `unverifiable` and context-dependent verdicts,
explicit contradictions, source dependencies, and deciding
evidence that could change the overall conclusion.

The current independently authored
`skills/authored/claim-evidence-adjudicator/SKILL.md`
already requires those functional results through its typed
component-claim ledger, primary/secondary source provenance,
load-bearing attempted falsification, CONTEXT_MISSING,
CONFLICTED and UNRESOLVED states, causal alternatives,
overall decision confidence and explicit disconfirming evidence.
It also adds better date and evidence-source independence
checks. **No confirmed material source-level omission was
found to justify another textual rewrite in this pass.**
This is a judgment about specified behavior, not an observed
equivalence test.

Exact unchanged package artifacts:
- SKILL blob `63864e5ed30deee2be15c3044ddb87fd641145a0`
- Fixture blob `705d7f7fd0d02d60fddf0b23df9811663d8ac7dc`
- LICENSE blob `023abdb34298b27580d1d303084aca942050585e`
- Complete Git tree `f4fbdc7847e5e045b7ba298e84f31013b2d4fef7`,
  independently reconstructed from those blobs.

Existing 18/20 complete-package static review remains exact
and current. No new version or safety status is granted by this
audit; actual source and host behavior is still NOT_RUN.

## Remaining external qualification

No real automation log, scheduler, account, job delivery
or fact-check web-source research was executed. No current
host-agent paired scenarios established 100% behavioral parity
or the >=1.5x user-requested quality target. The legacy
44-to-21 crosswalk and retirement conditions under #738 remain
open. No historic source deletion is authorized.
