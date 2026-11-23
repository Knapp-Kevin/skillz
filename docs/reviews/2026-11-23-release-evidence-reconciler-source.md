# Release Evidence Reconciler 0.1.0: initial evidence boundary

**Date:** 2026-11-23. **Issue:** #882. **Status:** original source candidate.
**Package:** eight original MIT files at
`skills/authored/release-evidence-reconciler`.

## Differentiator

CI Guard qualifies required verification placement but does not authenticate
what an end user downloaded. PR Integration Surgeon handles issue/PR merge
cutover but does not inspect distributed artifacts. Repository Delivery
Assessor gives broader health status rather than examining an actual
source → tested build → artifact digest → distribution → installation
chain. This new skill checks that chain using **actual locally hashed
artifact bytes**, separating confirmed local content from
self-reported metadata and external signature verification.

## Original implementation

Optional `scripts/reconcile.py` is Python 3.9+ stdlib, read-only and
offline; bounded to one MiB manifest, 32 channels, <=128 MiB local
files, no path traversal/symlinks and on Linux O_NOFOLLOW for leaf.
An example harmless 29-byte ASCII payload has SHA-256
`7c6b04f68d62a909a01a535b6d5506f3834ae359d090eb88f534d94e033de292`.
Its release, CI run, signature and installer data are fictional.
The suite has 55 synthetic planted methods, including explicit expected-channel coverage and deliberate
local-byte tampering, mismatched build/tag/check/app/attestation
subject/install digest and missing release channels.

The maximal label is `LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS`.
It neither validates an external signature nor authenticates the
download origin, checks actually executed, installed functionality,
SLSA build provenance, or a delivery acceptance decision.

## Remaining evidence

Exact-head GitHub-hosted tests **PASS 55/55** on [Actions #45123071252](https://github.com/Knapp-Kevin/skillz/actions/runs/45123071252); authored source/provenance [Actions #45123071291](https://github.com/Knapp-Kevin/skillz/actions/runs/45123071291) PASS 11/11. Both Socket Security checks SUCCESS; no independent agent trial,
real repository or market study, security attestation, package
installation, customer benefit or measured release ROI claimed.

Factual external references: https://slsa.dev/spec/v1.0/provenance
and https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
Neither external source is imported or executed.
