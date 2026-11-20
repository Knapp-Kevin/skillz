# Decision Tradeoff Workbench v1.2: executable scoring review

**Issue:** #738  
**Review date:** 2026-11-20  
**Scope:** original six-file portable package; optional Python 3.9+ stdlib scoring method.  
**Current entrypoint blob:** \`24c65454a57689bfbea24ef024591e202118b675\`  
**Current complete package tree:** \`a8cb0eac3a487bdc77064935b2f6c4f10fff215c\`

## Actual implementation

The v1.1 skill instructed a host to calculate weighted scores, reject hard-gate failures, handle unknown evidence and test sensitivities. It included no executable verification. This revision provides an original, offline JSON-to-JSON scorer in the package, with explicit input schema, unapproved-weight refusal, missing-cell coverage, exact decimal arithmetic, per-cell products, maximum possible totals, noncompensatory hard gates, tie handling and supplied illustrative weight scenarios. The skill remains useful without Python or with a stronger host analyzer. No external account, dependency, network, vendor login, source file mutation or repository write is used by the scorer.

## Executed result and exact source binding

Executed \`python3 -m unittest discover -s tests -v\` with Python 3.13.5: **25 run, 25 passed**. Git blob hash calculations of the *locally executed bytes* agree with uploaded GitHub blobs: script \`5a097723cf7e4335ac93364a761a08c5fb462cc6\`; tests \`020463fd7710dce36baf41c0c8de4c985f4d62ad\`. The exact inputs reproduce the prior fictional compare case: A=22, B=25, but B fails the noncompensatory security threshold and A is the conditional feasible leader.

Coverage also includes UNKNOWN-vs-zero, unapproved weights, incomplete and unknown-gate refusal, sensitivity flip, ties, invalid/duplicate JSON keys, unbounded input, missing source pointers, malformed scores, opaque untrusted text and stdout-only operation. See [machine-readable receipt](../evals/receipts/2026-11-20-decision-workbench-v120-executable-scoring.json).

## Source and authority safety

Only approved user-supplied weights can generate the base ranking. Every criterion must have a cell for every alternative, including explicit UNKNOWN. The tool does **not** verify source accuracy, permission, owner consent, normalized rubric, rating comparability, source freshness, real product feasibility or the correctness of a physical one-page brief. Source strings are not executed or echoed in output. It is deliberately an arithmetic checker, not a procurement or decision engine.

## Review and hard limits

**Maintainer current-package static assessment: 18/20.** The package is bounded, source-independent and portable; qualification remains limited because the 25 cases are author-operated method tests rather than an independently operated agent-host comparison, and no user outcome was inspected. Security of arbitrary supplied source references depends on the host performing redaction and scope authorization. The older v1.1 review remains historical rather than silently upgraded.

**Historical retirement pins are unchanged.** Existing old/new textual emulation is not converted to an externally validated A/B. For both historical \`compare\` and \`brief-writer\` predecessors: independent complete skill parity **NOT PROVEN**, outcome effectiveness ratio **NOT PROVEN**, original historical rights **NOT ESTABLISHED**. No user action, purchase or memory persistence authorized by a score.

Next evidence gate is an isolated host comparison plus independent source and user-decision outcome checks, not more self-graded rubric paperwork.
