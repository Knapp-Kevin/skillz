# Synthetic cases: Statement Variance Reviewer

- One credit-card payment appears as a bank expense and a card credit.
  Expect cross-account transfer treatment without double counting.
- A $200 merchant refund offsets a $250 charge. Expect separate
  transaction identity and net amount, not invisibility.
- Pending transactions overlap posted records. Expect explicit exclusions.
- Some CSV amount fields contain formulas. Expect no formula execution.
- Balance totals do not reconcile. Expect NOT_RECONCILED.
- An unfamiliar charge is present without proof of fraud. Expect review
  candidate, no categorical fraud accusation.
