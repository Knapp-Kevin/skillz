# Vercel Agent Skills: pinned deploy authority reclassification (2026-10-29)

## Scope and exact identity

- Registered source: `vercel-labs/agent-skills`, MIT, pin `f8a72b9603728bb92a217a879b7e62e43ad76c81`.
- Current pinned family: 9/9 current-standard companion pairs, denominator unchanged, no new admission.
- Deep-review target: `skills/deploy-to-vercel/SKILL.md`, exact upstream Git blob `a0251ce89a7636230be9c5b989a81e1a54a52a96`, same blob as existing verification.
- This is an exact-version static semantic correction. No skill source, pinned gitlink, package dependency, scanner evidence or behavioral result changed.

## Macro map and disposition

All nine pinned Vercel manifest entry points and their nine existing provenance/verification identities were screened. The family contains (a) a deployment/account mutation lane, (b) an observability/optimization lane with account-scope and linking dependencies, and (c) reference-only React/UI/writing guidance. There is no newly discovered package denominator or duplicate exposure path in this bounded review.

Before correction the individual semantic states were six verified and three rejected unchanged. The deployment procedure is the high-authority outlier. After reclassification: **5 VERIFIED semantic only, 4 REJECT unchanged, 0 current-standard companion gaps**. The other eight exact-version decisions are retained; this screening is not a claim of fresh deep review or behavioral acceptance for them. `vercel-optimize` has a separate project-linking prerequisite that merits attention during a future focused authority audit; this record does not assert a new finding or change its existing status.

## Authority hard fail

The exact `deploy-to-vercel` manifest contains useful preview-first routing, team discovery, safe unlinked-state checks and an explicit ask before git push. Those safeguards do not authorize its distinct side effects:

1. On an unlinked project it says team selection is sufficient, then runs `vercel link --repo` or `vercel link` without separate approval for persistent account/repository linkage or potential new project creation.
2. The no-CLI branch globally installs the Vercel CLI and links a project as ordinary follow-on work, not an independently authorized host mutation.
3. The no-auth fallback packages and uploads local source to a deployment service, potentially disclosing private project content, without a separately scoped disclosure decision.
4. The git branch stages all files via `git add .` and pushes. The ask is generic and does not identify staged content, branch, visibility or the fact that a production branch can trigger production deployment despite the stated preview default.

A request to deploy a preview does not silently authorize every associated installation, account link, upload, repository push or production side effect. Choosing a team or confirming parameters is not action authorization. Under the current authority hard-fail rule, the unchanged package must be **REJECTED** for unchanged reuse even though the existing historical rubric score is 17/20. This is not a newly executed attack or security-scan finding.

## Salvage and host fit

**ADAPT/EXTRACT/CHECKLIST:** preserve the state-detection sequence, preview/production distinction, project/team scope resolution, branch-aware deployment method, and explicit result reporting. Before each consequential operation, require an external host to obtain action-specific authority for exact destination/project, persistent linking/creation, installation, source disclosure, staged files/branch, preview versus production, cost and any retained claim URL. Default to proposal-only when those bounds are missing; use a secure external credential path.

No repository-owned scanner, script, runtime, test, scheduler or generator is added. The pinned upstream package remains intact as reference evidence.

## Evidence and accounting

- Provenance: `registry/skills/vercel-agent-skills/deploy-to-vercel.yaml` reclassified to `rejected-unchanged`.
- Verification: `registry/verification/vercel-agent-skills/deploy-to-vercel.yaml` reclassified to `rejected`, retained exact blob, historical score 17/20, `validation_status: not-run`.
- Public accounting: README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json agree on 9/9, 5 verified / 4 rejected. Total inventory remains 44 first-party, 826 third-party companions, 870 total verification records.
- Package security: no new SkillSpector run; behavioral/adversarial execution: not-run.
- This is a bounded semantic safety correction, not source pin promotion or new-skill admission.
