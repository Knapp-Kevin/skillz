# Source Debt Triage: synthetic acceptance inputs

- `const fixmeCounter = 2;` appears in source. Expected: not a comment marker.
- `// FIXME: retries sometimes charge twice` appears in active billing.
  Expected: actionable high-risk candidate, no automatic code change.
- One hand-authored annotation appears in 300 generated bundle copies.
  Expected: exclude generated copies or document counting policy.
- A recent formatting pass changes blame on a very old annotation.
  Expected: age is uncertain, not incorrectly "new".
- An issue is closed but the code still has the bad behavior.
  Expected: do not mark OBSOLETE without evidence.
- Remote search returns the first 100 of 1,000 matches.
  Expected: explicitly partial coverage and no invented total.

Mark tests observed only when actually exercised by a host.
