# Q8 batch 2: eleven more reference-only candidates in still-unfeatured domains

**Date:** 2026-11-03 · **Route:** explicit `REPOSITORY_MAINTENANCE` · **Tracking:** #588, #599, #624 · Follows [batch 1](2026-11-03-q8-reference-only-qualification-batch1.md)

## Why this batch

After batch 1, **16 domains** still had nothing on the featured shelf. We took the strongest reference-only candidates there (17/20 in earlier static sweeps), one or two per domain. We skipped candidates that take real-world actions on their own, such as placing phone calls to businesses. The method was the same as batch 1:

- exact pinned tree re-derived (**11 of 11 matched**);
- every file read;
- the 10-part, 20-point rubric with written reasons;
- a pinned static security scan;
- the decisive claims checked against the source lines.

## Results

| Candidate | Domain | Earlier | Now | Decision |
|---|---|---:|---:|---|
| Build Evidence Map | Research | 17 | **18** | **Valuable Reference** |
| Singapore SSP Navigator | Law | 17 | **17** | **Valuable Reference** |
| Radiology Reproducibility | Research | 17 | **16** | **Valuable Reference** |
| Submission Auditor | Education | 17 | **16** | **Valuable Reference** |
| Read Ledger | Memory / context | 17 | **15** | **Valuable Reference** |
| GTM Deal Pulse | Sales | 17 | **15** | **Valuable Reference** |
| RTOS Fundamentals | Robotics / IoT | 17 | 14 | Keep in research |
| scRNA-seq QC | Science | 17 | 11 | Keep in research |
| PaperPilot CSV Preflight | Analytics | 17 | 11 | Keep in research |
| Novel Text Rewrite Lint | Fiction | 17 | 10 | **Reject unchanged** |
| Management Hiring | Career | 17 | 7 | **Reject unchanged** |

The shelf grows from **27 methods / 17 domains to 33 / 22**. Unchanged-use approvals stay at **0**.

## What each new method teaches, and its main limit

- **Build Evidence Map.** Draw a contested decision as a map. Every piece of evidence points to an exact source passage and is labeled for, against, qualifying or missing. A checker refuses broken maps. *Limit:* “valid” means well-formed, not true, and hand-written verification entries slip through.
- **Radiology Reproducibility.** Give each result its own reproducibility level and fix the acceptance margin before rerunning. Keep failed runs, and never patch quietly. *Limit:* reruns could execute untrusted code on patient data, and some labels are undefined.
- **Read Ledger.** Log exactly which text spans were reviewed in which version of a source, so edits reopen old reviews. *Limit:* its install step clones an unpinned outside repository.
- **Submission Auditor.** Turn a teacher’s rules into a checklist where every check traces to something students were told. Cite where each finding is, and compare verdicts across the class. It never grades or sends anything. *Limit:* student work goes to the model with weak privacy handling.
- **Singapore SSP Navigator.** Collect a system’s classification facts, pick one base security plan by rule, add the overlays, and escalate combinations with no published template. *Limit:* it is a dated July 2026 snapshot and is not legal advice.
- **GTM Deal Pulse.** Score a deal only from tagged, dated evidence, and refuse to give a score when too few signals are known. *Limit:* one of its rules contradicts itself, and it needs a profile file that is not shipped.

## Why five did not make it

- **RTOS Fundamentals:** accurate but mostly textbook scheduling theory.
- **scRNA-seq QC:** its runner script is outside the package and starts a local server without asking.
- **PaperPilot CSV Preflight:** a generic CSV linter. Its tests check install text the skill does not contain, and it promotes a paid upload service.
- **Novel Text Rewrite Lint (rejected):** a manual for a tool that is not in the package.
- **Management Hiring (rejected):**
  - It would steer an agent toward employment actions with no legal or human review: marking candidates “no reapplication”, asking salary expectations at the first screen, culture-fit judgments and pay set by score.
  - Its own scoring scales contradict each other.

## Security scan (static, not a clearance)

- **Passed:** Read Ledger (1).
- **Failed:** Singapore SSP Navigator (1). This is a false positive on “skipping Level 2 needs no approval, but record the reasoning”.
- **Incomplete:** the other 9, mostly because they reference files outside the package.
- Behavioral tests: **not run**.

## Evidence

- [Batch 2 individual records](../../registry/discovery/q8-reference-only-qualification-batch2-20261103.json)
- [Current shelf](../../registry/consumer-positive-references-q8-20261103.json)
- [Pipeline ledger](../../registry/qualification-pipeline-20261103.json)

## Next

The qualification queue is now **1,534**. Domains still without a featured method:

- Visual design
- Fiction
- Audio
- Video
- Analytics
- Time / productivity
- Business
- Career
- Science
- Robotics / IoT
- ML accelerators

Several of these have strong candidates that carry paid-API or vendor-license issues, such as the Adobe and Boltz plugins. Those need rights-focused review rather than score-ranked selection.
