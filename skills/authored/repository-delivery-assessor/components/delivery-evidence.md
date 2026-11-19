# Component: delivery evidence validation

**Select when:** An issue/PR/report claims "fixed", "merged", "released",
"deployed", "working", "accepted", or an agent offers its own success claim.
Useful for issue closeout and project status; it is not a general internet
fact checker (use `claim-evidence-adjudicator` for that).

Evidence ladder, **not** automatic promotion:

1. Proposed patch or statement only.
2. Committed source at exact SHA and repository.
3. Test execution with command/environment/results tied to that SHA.
4. Exact-head CI and required review on a compatible ref.
5. Merge receipt and resulting target-branch SHA.
6. Reproducible package or signed artifact identity, if required.
7. Deployment record binding artifact to environment and rollout.
8. Operational/user-observed acceptance against the original objective.

For each claim record `claim | supported highest stage | source ID |
revision/time/environment | independently observed or self-report |
contradictions | limitations | next required proof`.
Never infer stage 6 from merge, stage 7 from a tag, or stage 8 from
deployment. A passing test only shows the asserted test ran in the
asserted environment. A failed or inaccessible evidence source is
UNKNOWN, not a fabricated PASS or a proven FAIL.

Separate self-authored agent statements from actual tool receipts and
independent user/host confirmation. Status can be PROPOSED, IMPLEMENTED,
TESTED, REVIEWED, MERGED, PUBLISHED, DEPLOYED, OUTCOME_OBSERVED, or
UNVERIFIED; stages with no applicable artifact must be marked
NOT_APPLICABLE, not invented. Preserve accepted governance and owner review.
