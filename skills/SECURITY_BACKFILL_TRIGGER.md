# SkillSpector first-party backfill trigger

Maintenance-only trigger for issue #402.

This file exists only on the backfill branch so the changed-package workflow expands the scan to the complete first-party `skills/` surface while excluding pinned third-party corpora under `skills/sources/`.

Do not merge this trigger file into `main`.
