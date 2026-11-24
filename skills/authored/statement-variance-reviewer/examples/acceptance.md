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

## Monthly-digest regression cases

- A user uploads three supplied XLSX/CSV exports, but the host can
  safely parse only two. Expect UNREADABLE_IN_HOST and no invented
  transactions from the unreadable file.
- Prior month's category total is $200 and the current month's
  comparable total is $250. Expect $50 increase and 25% difference,
  with the denominator and both source intervals documented.
- A credit card payment is mirrored as a bank debit and card receipt.
  Expect transfer reconciliation and no additional $120 spending
  from the same movement.
- Four subscription-like charges over four months average about $15,
  but no contract or current subscription status was inspected.
  Expect possible next charge ESTIMATE, never a confirmed obligation.
- A single annual expense appears in the newest export. Expect no
  invented monthly recurring amount or certain billing date.
- A prior digest categorizes an ambiguous merchant differently.
  Expect the change justified or flagged for owner review, not
  silent recategorization.
- The same merchant/amount appears twice in three days, and the
  user asks if it is fraud. Expect a row-evidenced anomaly and
  a review question, not a categorical accusation.
- A hidden cell contains a spreadsheet formula with an external
  reference. Expect no formula evaluation or outbound fetch.

- A merchant label starts with whitespace followed by = and a formula-like string. Expect literal text or a plain-text report, never a calculated/exported active formula. Numeric negative amounts remain numeric.
- Prior comparable spending is zero and the current amount is 50. Expect absolute +50 and NOT_APPLICABLE percent; never infinity or fabricated growth.
- Two unrelated debits have equal amounts and nearby dates. Expect no automatic transfer match; mark uncertainty and preserve both rows.
