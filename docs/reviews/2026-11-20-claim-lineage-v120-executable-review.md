# Claim Evidence Adjudicator v1.2: independent-root audit with real-source control

**Date:** 2026-11-20. **Issue:** #738. **Artifact scope:** original standalone six-file authored package, no historical source content imported.

## Source pins

- Entrypoint \`SKILL.md\`: \`112e125b44a3d117c570fc49c17cea6551714560\`.
- Complete v1.2 package tree: \`2a5cc6d1b2ab81960edcb13d32cc3d2cbe12a4c0\`.
- Original Python method: \`f778a602212e1c593179ffe8209bcaf0a9c28331\`.
- Original regression suite: \`bfb0279e3294b49ba97b4c2dea0591b88506e33e\`.
- Historical v1.1 package pin: \`4f1576d8c8170e1b14f97e761a2dcfd4a8bcd0c4\`; historic \`fact-check\` comparator: \`dc28e222ef448bed3d72193477fac2e7206f2ec9\`. Their retirement evidence is **not** replaced with new version claims.

## Real increment

Previously the skill instructed users to distinguish several articles from one original press release, but did not provide a method to trace derived-from relationships, group identical roots, or reject temporal and population mismatches. v1.2 adds an *optional*, original, offline Python standard-library tool for narrow deterministic lineage analysis over a bounded authorized JSON snapshot. It classifies original versus derivative, known versus unknown provenance, same versus differing origin contradictions, directly consulted primary source versus reported secondary source, and wrong-time/wrong-population evidence. It validates a DAG, refuses extra/malformed input and never executes retrieved strings.

In a **real public-source negative control**, the GitHub PR #817 REST view, GitHub PR web view and GitHub Issue API view of PR #817 all ultimately reflect one authoritative GitHub PR merge event. The PR's merge at 2026-11-20 19:57:51 UTC and resulting merge commit \`777e41bdcb29f14e0026dcee834033ec8e546a7c\` were separately verified through the GitHub connector. Their three source entries correctly produce **3 eligible citations, only 1 recorded direct-primary origin**. The web/API views are not independent corroboration.

## Executed verification

In local Python **3.13.5**, ran \`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v\`: **48/48 PASS**, zero errors. Locally executed script and test file Git blob identities matched uploaded GitHub blobs byte-for-byte. These are actual method tests, not only hypothetical scenario designs.

Cases include common roots, asserted separate independent primary roots, derivatives mentioning more than one unconsulted root, contested claims with shared or distinct declared roots, missing/inaccessible sources, unknown lineage, citations to unread documents, future publication and incomplete event-period coverage, population scope mismatch, malformed or circular provenance, duplicate JSON and IDs, nonfinite constants, embedded hostile directives remaining inert, oversize file rejection and stdout-only operation.

## Non-promotions, exact limits

**The tool is not a source authenticator.** A caller can falsely label sources independent, primary, consulted, dated and authorized. The result remains \`source_authenticity_verified: false\` and \`global_verdict: NOT_DETERMINED_BY_LINEAGE_AUDIT\`. A human/host must actually open approved source records and evaluate truth, denominator, authority and causal claims. Real GitHub event verification was performed separately, not by the bundled checker.

**No independent old/new agent-host A/B was performed. No 1.5x user-effectiveness uplift or actual claim-adjudication accuracy is proven.** Historical original authorship and licensing remain not established; no original source expression was incorporated. \`#738\` must remain open for remaining qualification.

**Static rubric:** prior v1.1 18/20 remains a historical opinion. This review confirms explicit original fallback, use bounds, evidence and negative tests, but does not claim a new independent numeric quality grade without a separate scored rubric.

Machine receipt: [2026-11-20-claim-lineage-v120-executable.json](../evals/receipts/2026-11-20-claim-lineage-v120-executable.json).
