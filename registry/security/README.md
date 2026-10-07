# Security evidence registry

This directory stores persisted exact-version skill-package security evidence.

Security evidence is intentionally separate from provenance under `registry/skills/` and semantic quality evidence under `registry/verification/`.

Each persisted record must bind to an exact package identity and follow `docs/security-scanning.md`. A semantic `verified` or `validated` state never implies a security pass.

Do not commit secrets, model credentials, unrestricted raw external content, or reports whose licensing/terms prohibit redistribution. Normalize evidence when necessary while preserving the scanner identity, exact scanner revision, target identity, completeness/coverage, findings, dispositions, and final security state.
