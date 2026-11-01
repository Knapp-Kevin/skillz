# Security evidence registry

This directory stores persisted exact-version skill-package security evidence.

Security evidence is intentionally separate from provenance under `registry/skills/` and semantic quality evidence under `registry/verification/`.

**First-party per-skill lookup:** [`first-party-package-lookup.json`](first-party-package-lookup.json) provides a compact keyed pointer for all 44 first-party package names, the historically recorded baseline state and whether baseline/candidate scans match the package tree at the recorded source snapshot. For deeper evidence inspect [the baseline](first-party-baseline-2026-10-10.json) or [the separate candidate scans](first-party-candidate-2026-10-10.json). A historical pass transfers **only to an identical exact package tree**. Do not use 21 nonmatching candidate passes for unchanged current packages; do not turn this index into a fresh security certificate.

Each persisted record must bind to an exact package identity and follow `docs/security-scanning.md`. A semantic `verified` or `validated` state never implies a security pass.

Do not commit secrets, model credentials, unrestricted raw external content, or reports whose licensing/terms prohibit redistribution. Normalize evidence when necessary while preserving the scanner identity, exact scanner revision, target identity, completeness/coverage, findings, dispositions, and final security state.
