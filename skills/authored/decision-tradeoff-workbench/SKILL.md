---
name: decision-tradeoff-workbench
description: >-
  Prepare defensible option comparisons and concise decision papers with criterion sensitivity, quantified uncertainty and explicit owner authority; use when choosing among real alternatives.
metadata:
  author: Skillz Maintainers
  category: Planning
  display-name: Decision Tradeoff Workbench
  version: 1.0.0
  license: MIT
---

# Decision Tradeoff Workbench

## Outcome and two modes
**Compare mode:** expose the actual tradeoffs between options.
**Decision-paper mode:** produce a concise executive artifact with a
recommendation, uncertainty and required owner decision. Use the same
evidence ledger but do not pretend the output formats are interchangeable.

## Input contract
Specify the decision owner, options, deadline or decision window,
hard constraints, stakeholder impacts, decision criteria and evidence
access. Distinguish user-confirmed criteria from proposed criteria.
Where weights matter, use the owner's weights or show unweighted
analysis plus a labeled illustrative sensitivity case.

## Decision protocol
1. Define the decision in a falsifiable sentence and distinguish
   mandatory feasibility gates from preference tradeoffs. An impossible
   option is not made viable by a high weighted score.
2. For each option/criterion pair record: value, unit, provenance,
   evidence date, uncertainty, missing information and whether the
   observation was independently checked. Do not fill empty cells by
   aesthetic preference.
3. Normalize only comparable units after explaining transformation
   assumptions; avoid false precision for qualitative effects.
4. Identify irreversible commitments, externalities, total lifetime cost,
   downside exposure and opportunities for small reversible experiments.
5. Perform at least two sensitivity checks, including an alternative
   weighting and one material unresolved assumption. Report whether
   the ordering changes; if evidence is insufficient, decline to rank.
6. Present the strongest valid argument for the runner-up or for
   deferring the decision. Distinguish analyst recommendation from
   owner acceptance.
7. For decision-paper mode compress to one screen without dropping
   material decision gates, evidence gaps or disconfirming observations.

## Outputs
Compare: `criterion | option | observation | unit | confidence |
source | risk`, explicit feasibility and sensitivity, conclusion.
Decision paper: context, choice required, viable alternatives,
tradeoffs and bounds, recommendation, downside, conditions for reversal,
decision owner/status. A memo is not a signed approval.

## Boundaries
Use authorized documents only. No vendor contact, payments, procurement,
account changes, binding decisions or automatic document writes without
appropriate separate approval. Do not interpret marketing copy as
independent performance evidence. Unverified inputs remain UNVERIFIED.

## Acceptance cases
See [independent cases](examples/acceptance.md).
