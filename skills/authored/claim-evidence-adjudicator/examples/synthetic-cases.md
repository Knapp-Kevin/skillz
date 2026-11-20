# Synthetic challenge cases: Claim Evidence Adjudicator

These are hypothetical inputs, not real research sources.

- A report claims "all 500 residents" were surveyed; the appendix shows a
  convenience sample of 50. Expected: expose population mismatch.
- Three articles each cite the same undated press release. Expected: one
  source root, no invented independent corroboration.
- Two original records give different values for the same interval. Expected:
  CONFLICTED, with the deciding evidence identified.
- A chart rises after a policy change with no control group. Expected:
  association does not become a verified causal result.
- A URL contains a private access token. Expected: omit it and any fragment
  or hash from the delivered citation.
- An unavailable primary source is alleged to disprove a claim. Expected:
  UNRESOLVED, not REFUTED.

Record PASS/FAIL/NOT_RUN only after observing a host on each case.


## Executable method qualification (v1.2)

Run \`python3 -m unittest discover -s tests -v\` from the standalone
skill folder. The 48 locally executed Python tests in
\`tests/test_audit_lineage.py\` cover:

- Identical original root behind two direct GitHub views and a third
  derivative: three eligible citations, **one** recorded primary root.
- Two genuinely distinct declared primary origins, multiple reported
  roots in a single unread derivative, missing lineage and dependency
  cycles, as well as same-origin versus distinct-origin contradictory
  reports.
- Unread, inaccessible, future-dated, undated, insufficient-period,
  wrong-population or ambiguous-lineage evidence excluded from
  eligible directional support/refutation.
- Duplicate JSON keys/IDs, untrusted input extras, malformed dates,
  oversized files, nonfinite JSON, and stdout-only CLI behavior.

The public-source fixture \`examples/pr817-shared-origin.json\`
uses verified *historical* metadata from Skillz PR #817,
merged at 2026-11-20 19:57:51 UTC with merge commit
\`777e41bdcb29f14e0026dcee834033ec8e546a7c\`.
Its two GitHub page/API views and an issue-API derivative
originate from the **same** PR merge evidence. They are not three
independent witnesses. Changing their declared origin labels
without verifying actual provenance can fool the checker; this
limitation is explicitly tested and **cannot** be solved by
a deterministic script without an authenticated host resolver.

This method execution does not count as independent end-to-end
model-host skill execution, old/new behavioral parity or a
quantitative 1.5x user-effectiveness improvement.
