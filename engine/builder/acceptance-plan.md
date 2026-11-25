# Contract-derived acceptance plans

For a newly generated single, phased or pack skill, reuse its authored
[design dossier](design-contract.md), rather than inventing a second
contract. The optional generator reads the exact completed canonical draft
and compares every member to deterministic rendering of that dossier.
It then checks the selected assessed host and produces a private NOT_RUN plan.

    python3 -B engine/builder/acceptance_plan.py --design /private/design.json \
      --package /private/exact-skill-slug --host claude-apps

The package folder must have its canonical slug and contain every expected
file, with no added or changed members. This route covers builder-generated
original skills; manually authored or adapted packages use the
[manual native host protocol](host-acceptance.md) until a reviewed
contract for their actual source is available. Do not force them through
an unrelated blueprint.

The output binds the plan to the canonical file SHA-256 map, the dossier
digest and the selected host member transformation manifest. Every case
has an explicit expected contract and stage mapping. It preserves the
authored positive, near-non-trigger, missing-input, authority and false-green
probes and adds per-step/per-module output and missing-handoff cases.
Optional pack modules have separate fallback challenges. Host loading and
reset have their own cases. A plan is not a generated executable test suite:
concrete fictional/public fixtures and independent outcome oracles must
be authored and reviewed before any run. The deterministic output cannot
establish semantic coverage, authorization or execution.

## Handoff to native acceptance

1. Review each case against the actual skill and choose concrete safe input,
   independent observation and pass/fail criteria. Freeze the exact plan
   digest and fixture/oracle identities in private custody before running.
2. Obtain separate authorization for the actual native host and isolation.
   For a release, reconcile the exact source tree and selected archive's
   members/digests against this plan, then use the source-pinned manifest.
   If the package or adapter changed, regenerate and review the plan.
3. Observe each required case. Never derive a PASS from the plan, a missing
   dependency alone, a self-report or a green static check. Record failures,
   timeouts and unknowns separately. Keep evidence and raw prompts private.
4. Use the plan's receipt_stage_requirements as a **conjunctive** checklist:
   only claim a stage pass if every mapped case has independently supported
   successful observations. Missing or failed cases block that stage.
   The six-stage [host acceptance checker](host-acceptance.md) currently
   checks claims and archive identity, not this plan's detailed case ledger.
   Preserve that ledger for independent review; no automatic conversion
   or promotion is performed.

The CLI prints private design-derived text to stdout. Do not publish its
output, include it in a skill archive, or send it as anonymous feedback.
If Python is unavailable, perform the same bounded design-to-package review
manually and label the tool NOT_RUN.
