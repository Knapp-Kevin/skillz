# Skillz repair branch consolidation: #673 + #686 into canonical #703

2026-11-04. This is a Git-object-verified preservation migration, **not** a security scanner run, behavioral validation, or unchanged-use approval.

## Source branch identities

- Pulse/removed-runner/privacy repairs: PR #673, head `1aa39ce7b63dfe047b6eb28b27dac4912f54ea89`, 16 distinct skill packages, 54 changed paths.
- Knowledge/credential-fragment/privacy repairs: PR #686, head `3d03c396d11645767c8e3a58b7113f8fec506ae2`, 5 distinct skill packages, 20 changed paths.
- Governance/recurrence/privacy repairs: PR #703, prior head `913b8e123faefd60f31737b2b8bc324b39d070be`, 13 distinct skill packages, 54 changed paths.

## Preservation and merge method

- The three PR changed-path sets intersect **only** at `registry/local-verification.json`, so no skill source, individual provenance, verification YAML or review file is overwritten by another PR.
- All **53 unique changed Git blobs from #673** and **19 unique changed Git blobs from #686** were copied by their exact Git blob SHA into #703's tree. The original #703 path set remained intact.
- The sole shared 44-row registry was reconciled by skill identity: 16 rows from #673 and 5 from #686 replace the old values in #703, preserving all 13 #703 changed rows and the other 10 unaffected first-party records. Every replaced source SHA was checked against its source PR's current SKILL.md blob.
- The consolidation commit has all three former PR heads in its parent ancestry, preserving Git history and source provenance. No source branch is force-pushed or deleted.
- After integration, live GitHub Git trees and exact changed-path blob identities must be compared to the source PR heads; do not mark a superseded PR closed unless the full readback passes and its review/issue handoff is recorded.

## Security gate remains unchanged

- This migration brings **34** proposed current first-party package repairs into one draft, with **14** historical exact-tree pinned NVIDIA SkillSpector static PASS receipts and **20** remaining exact-tree scans.
- No scanner ran in the migration. **Zero** actual agent-host behavioral validations and **zero** unchanged-use approvals remain. Do not merge the canonical draft onto main before qualified scanner/host acceptance and owner review.
- Security issue #402 and dependent issues #415, #491, #478, #481, #483, #495 remain open until accepted fixes are merged; the related parent corpus programs remain open.

## Acceptance checks

1. Verify 53/53 unique #673 and 19/19 unique #686 source-branch Git blob SHAs inside the new #703 tree.
2. Verify 44/44 merged `registry/local-verification.json` rows equal their corresponding changed package's source and individual verification blob; no accidental source downgrade.
3. Verify 34/34 actual Git skill package directory tree SHAs match the canonical issue #402 security frontier after the manifest is updated to the new canonical PR head.
4. Check every README, security chart, PR description and issue report for whether a reference is historical or currently active. Preserve all old PR URLs as provenance.
