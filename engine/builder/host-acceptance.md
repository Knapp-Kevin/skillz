# Native host acceptance: evidence, not a packaging badge

Use after static package preflight, not as an additional universal publication
gate for passive source. The optional offline checker validates the consistency
of a bounded **externally recorded claim**, never performs the trial. It does not
authenticate a manifest, authorize an installation, inspect a host, verify an
oracle, store records or promote a skill to validated.

## Run one authorized journey

1. Select the exact host surface and version, model/configuration, permitted
   tools, network, data, and cost; establish a clean isolated scope and reset
   method. Obtain separate approval before installation or actual side effects.
2. Follow the [download guide](../../docs/getting-started-with-skills.md):
   retrieve the source-pinned release manifest and exact host-selected archive,
   verify authenticity/source separately and compare the selected SHA-256.
3. Predeclare one fictional or public positive task and independently observable
   meaningful outcome, a near non-trigger, and an adversarial authority case.
   Inspect the complete package and its scripts/resources before enabling it.
4. In the actual native host record separate evidence and an independent oracle
   for loading/discovery, positive activation, near non-trigger (no false firing),
   outcome correctness, authority boundary, and cleanup/reset. Do not pretend
   a transcript of the agent saying it loaded a skill proves discovery. Confirm
   supporting references and runtime-dependent behavior where essential. Missing
   telemetry, failed tasks and inability to reset remain explicit holds.
5. Keep exact evidence privately with authorized custody. Use opaque local IDs
   in the receipt; no private task content, customer identifiers, credentials,
   full transcripts, or public feedback submission. An ID is not proof.
6. Review each receipt against the actual independent evidence; do not treat
   a static checker or self-report as accepted host behavior. For comparative
   effectiveness use the existing [Skill Trial Evidence Auditor](../../skills/authored/skill-trial-evidence-auditor/SKILL.md)
   with comparable paired conditions; for fresh-user onboarding use the
   [First-Run Experience Validator](../../skills/authored/first-run-experience-validator/SKILL.md).

For builder-generated skills, the [contract-derived acceptance plan](acceptance-plan.md)
provides exact-package-bound adversarial cases and a conjunctive mapping to
the six receipt stages. Use its detailed case ledger reconciler for generated
skills; the stage-only checker below explicitly reports case_ledger_reconciled
as false. Do not claim a stage passed if any mapped case is missing or failed.

## Optional receipt checker

Copy the fictional NOT_RUN example and replace its identities with exact
observed values. Never fabricate observations to fill required fields. Use
one receipt per skill/host/environment; no pooling or cross-host inheritance.

    python3 engine/builder/host_acceptance.py --manifest /private/manifest.json \
      --archive /private/skill.zip --receipt /private/receipt.json

The archive basename must match the selected host asset exactly. The tool
checks the raw manifest SHA-256, source commit, package tree, host entry,
archive name and actual local bytes. It rejects unknown profiles even if
a supplied manifest labels them ready, and checks the selected ZIP layout,
required entrypoint/license, bounded central-directory inventory and portable
member names. It does not extract, execute, or verify every member's CRC,
or authenticate remote download origin. Verify release authenticity and
complete package contents separately. The CLI emits the exact input receipt
SHA-256 to bind the review result to the original claim. The receipt uses exact schema v1 fields in the
[fictional example](examples/host-acceptance-not-run.json), with opaque
bounded identity tokens (no spaces, URLs or raw logs). Actual observations
remain claims; PASS_CLAIMED and FAIL_CLAIMED each require distinct evidence
and oracle IDs, while NOT_RUN and UNKNOWN require null IDs. A real failure,
missing stage, emulation, unknown environment identity, absent approval claim or contradictory stage order
cannot yield a complete native claim.

Exit 0 means COMPLETE_CLAIMS_REVIEW_REQUIRED, **not** host validation.
Exit 2 means HOLD or invalid input. Even a complete claim does not establish
actual host loading, runtime parity, consumer acceptance or an independently
verified authorization. An independently observed and reviewed outcome can
be recorded separately under the existing [verification standard](../../docs/skill-verification.md).
If Python is unavailable, apply the same protocol manually without claiming
that the checker ran. Do not store a user receipt in Skillz by default.
