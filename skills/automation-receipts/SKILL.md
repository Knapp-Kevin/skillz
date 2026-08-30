---
name: automation-receipts
description: Verify claims that scheduled or automated work actually ran, before representing it as running, paused, completed, or scheduled. Use whenever an agent, report, or operator statement asserts automation status and the truth of that claim matters. Not for creating schedules or monitoring systems.
metadata:
  author: frostwulf.zo.computer
---

# Automation Receipts

A status claim about automation ("it ran", "it's scheduled", "the heartbeat is active") is a factual assertion about durable state, not a summary of intent. Verify it against receipts before repeating it.

## The receipt contract

A claim that automated work is running, paused, completed, or scheduled is **substantiated** only when all applicable receipts exist and agree:

| Receipt | What it establishes |
|---|---|
| Automation identity | rule/service/cron/automation id and its persistence surface (where the config lives) |
| Schedule | next fire time for scheduled work, or the recurrence expression |
| Log path | where run output is written |
| Last run | timestamp of the most recent execution |
| Exit status | success/failure of the most recent execution |
| Evidence artifact | path to the durable output the run claims to have produced |

A receipt is durable only if it lives outside the session that produced the claim. A statement in chat, in the agent's own context, or in an unmerged buffer is not a receipt.

## Procedure

1. **Restate the claim precisely.** Which automation, which status, asserted by whom, asserted when.
2. **Resolve the persistence surface.** Find where the schedule and its state actually persist (crontab, scheduler DB, service config, platform automation record). If you cannot locate it, the claim is unsubstantiated; say so and stop.
3. **Read the receipts.** Last-run timestamp, exit status, and the evidence artifact the run should have written. Open the artifact; confirm it exists and its content matches what the claim says the run did.
4. **Cross-check coherence.** Last run before the claim was made; next fire time consistent with the schedule; exit status consistent with the claimed outcome (a "completed" claim with a failure exit is contradicted, not substantiated).
5. **Report the verdict with the receipts named.** Cite the id, the log path, the timestamps. Never report a verdict without the receipts that produced it.

## Verdicts

- **Substantiated** — all applicable receipts exist and agree with the claim.
- **Unsubstantiated** — any applicable receipt is missing or unreadable. The honest report is "unsubstantiated", not a softened version of the claim.
- **Contradicted** — receipts exist and disagree (timestamps in the future, failed exits behind "completed" claims, artifact absent). Report the contradiction explicitly.

## Anti-fabrication rules

- Never infer a run happened from the schedule alone. A schedule is intent; a log entry is execution.
- Never describe an automation as durable because it "should have" fired, was configured earlier, or worked last time you checked.
- Missing log, missing artifact, or missing state each independently downgrade the claim to unsubstantiated.
- If the persistence surface is unreachable right now, report "unverified, surface unreachable" rather than passing the claim through.

## Boundaries

- This skill verifies claims; it does not create, edit, or delete schedules, and does not restart anything.
- It is agnostic to the scheduler: the same receipt contract applies to cron, launchd, platform automation registries, and supervised services.
- Status-only. Performance, correctness, and value of the work are out of scope here.
