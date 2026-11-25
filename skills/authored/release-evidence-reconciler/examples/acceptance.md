# Release Evidence Reconciler: synthetic falsification cases

Everything in this package is **fictional**. The included
`synthetic-release.json` references the byte string
`FICTIONAL_RELEASE_PAYLOAD_V1\\n` in
`examples/artifacts/fictional-installer.txt`. Despite its filename,
this is a harmless 29-byte text file. No installer is ever executed.

Expected SHA-256 of the literal bytes:
`7c6b04f68d62a909a01a535b6d5506f3834ae359d090eb88f534d94e033de292`.

## Planted release failures

The executable tests change one source link at a time:

- Correct tag and build source and exact-head required checks must match.
- Missing/failed/stale checks, or a different GitHub App claiming the
  required name, cannot silently qualify release CI.
- Distinct build and distribution checksum claims are a contradiction.
- Changing **actual local bytes** must be detected by computed SHA-256,
  even when the manifest still says they match.
- Provenance subject/source/repository mismatches are blockers. A text
  `reported_verified` and a fabricated receipt string are never
  authenticated by the offline script.
- Missing attestation or installer receipts are holds. A reported
  failed installation is a blocker; a reported passed installation
  is NOT an observed installed product.
- Multiple platforms/channels are independently reconciled. An
  unavailable channel cannot be silently omitted or accepted.
- JSON duplicate keys, nonfinite numbers, wrong checksums, file
  traversal, symlinks, unbounded inputs and oversized file bytes
  cannot evade source-bound constraints.
- CLI result codes distinguish a completed comparison from observed
  byte-chain parity, not a ship authorization.

## Limits on real security claims

This simple tool hashes files **already present** in an explicitly
authorized, stable local directory; it does not authenticate where
the file came from, validate digital signatures, inspect PE/MSIX/
DMG/container signatures, prove build reproducibility, attest the
running product or check deployment channel ownership.

Filesystem directory-write races are out of scope. For a higher threat
model, use a trusted isolated snapshot and platform-specific verified
artifact tools, then retain their actual independent receipts.

Independent consumer-host evidence is **NOT_RUN** until an authorized
host has actually performed the validation. No benchmark or
before/after release ROI is claimed by these synthetic cases.
