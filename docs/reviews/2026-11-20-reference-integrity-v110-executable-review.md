# Reference Integrity Auditor v1.1 executable graph audit

**Date:** 2026-11-20. **Issue:** #738. **Scope:** first-party standalone original package, bounded offline validation only.

## Actual engineering improvement

v1.0 described relationship provenance, permission-aware resolver status and downstream impact accurately, but its execution was entirely host prose. v1.1 includes an **optional original offline Python 3.9+ standard-library checker** that validates a bounded graph provided by an authorized source reader. It distinguishes confirmed broken links (explicit authorized provider absence) from unknown HTTP 404, permission denials, revision drift, missing renderer checks and unverified redirects.

The checker computes proposed rename/move/delete **direct and transitive reverse-graph impact**, including cycles; possible unresolved dependents are separate from confirmed dependency edges. Orphan candidates require explicitly complete source and visibility inventories and are always **within-scope candidates**, never deletion authority. Hidden source/target edges are excluded without disclosing IDs or counts, and out-of-scope target identities are never promoted to verified.

It rejects schema extras, duplicate JSON keys/identifiers, inconsistent absence/redirect proofs, unbounded input and symlinked input paths or parents. It has no crawler, network dependency, secret read, subprocess, automatic scheduled job, mutation or patch engine. The full standalone package contains its own governing contract and test fixture. Optional neighboring skills are not runtime prerequisites.

## Executed evidence and exact source

- Local **Python 3.13.5**: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`, **60 tests passed, 0 failures**.
- Exact locally executed script Git blob: `693e3fff1c8f6da8963b0dcb9dd0e76cce8d53e2`, executable test blob `78faf463668625639219ed6a9383e69c76112a74`. GitHub-uploaded blobs match byte-for-byte.
- Complete **seven-file** package Git tree: `5a2008481596cc9b89d441a50c8db2dc00234571` and SKILL.md blob `7ee18deb36d517b3c43b43cfdfbf47ae54efa327`.
- The public positive control was independently verified using GitHub's actual source tree at pinned commit `4ec0ac51cf1d53b012123a2c9314868a70b5bf2f`. Three SKILL.md local references resolved to actual blob-backed targets: LICENSE, reference contract and synthetic cases. The CLI returned three **recorded** `VERIFIED_CURRENT` statuses and one direct source dependent of the proposed contract rename. Because enumeration was deliberately partial, it reported orphan scope **UNDETERMINED**.
- All negative link, permission, stale, anchor, private-edge and transitive graph cases are **synthetic**, not observed defects on GitHub.

## Evidence and authority limits

The checker trusts only internally consistent **provided** evidence. It **does not authenticate** a provider, viewer identity or completeness. Its `target_evidence_authenticated: false` flag makes that explicit. The actual public Git source reading occurred separately through an authorized GitHub connector. No private source, user content, credential or deployment was touched. No files or links were modified by the Python method.

Historical static rubric **18/20** remains a prior assessment, not a new numerical benchmark. No independent original-versus-new skill host A/B, observed consumer acceptance or 1.5x outcome improvement was measured. These limitations remain **NOT_PROVEN**, and #738 should stay open. The root README does not need another transaction log.

Machine-readable execution receipt: [2026-11-20-reference-integrity-v110-graph-check.json](../evals/receipts/2026-11-20-reference-integrity-v110-graph-check.json).
