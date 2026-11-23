---
name: release-evidence-reconciler
description: >-
  Reconcile claimed source, tested HEAD, build result, distributed artifact
  bytes, reported provenance, and installed-product evidence without
  confusing passing CI with a verified usable release.
metadata:
  author: Skillz Maintainers
  category: Software Engineering & Supply Chain
  display-name: Release Evidence Reconciler
  version: 0.1.0
  license: MIT
---

# Release Evidence Reconciler

## Purpose and activation

Use when a release seems successful but someone asks **what was actually
shipped**, whether the downloaded installer corresponds to tested source,
whether a published package differs from its build, or why a release
appears green while the installed product fails.

This is distinct from CI Guard (check selection/assurance), Repository
Delivery Assessor (repository health), and PR Integration Surgeon
(unmerged dependency and review recovery). This package is standalone;
no sibling Skillz dependency, external service, or account is required.

**Completion criteria:** independently establish the intended source and tag,
required exact-HEAD tests, built output, authentic distribution origin and
downloaded bytes, trusted attestation verification, and real platform
installation/first-run outcomes. None of these implies the others.

## Evidence chain and authority

1. **Release identity:** bind repository, source commit, release tag
   and independently verified tag target. A version string or README
   badge is not source identity.
2. **CI qualification:** record the specific build run and effective
   required check names **and GitHub App identities**, their conclusions
   and exact checked commit. A green workflow label alone does not
   qualify the intended artifact.
3. **Build and production bytes:** record stable artifact/channel IDs,
   platform and architecture, build digest, distributor's published
   digest and the actual bytes *downloaded or otherwise independently
   obtained through an authorized trusted route*. Same filename is not
   identical bytes. A published checksum is itself a claim until its
   origin is authenticated.
4. **Provenance/attestation:** use an actual trusted verifier (e.g.,
   appropriate GitHub CLI attestation verification) on exact artifact
   bytes and establish the signer, subject digest, repository, source
   and builder identity. A claimed `reported_verified` field or
   certificate screenshot is **not cryptographic verification**.
5. **Installed outcome:** distinguish an installer existing, extracting,
   launching, functioning, and meeting acceptance. Require a bounded,
   isolated test on the actual artifact for each supported platform.
   Never run an untrusted installer in this passive audit.
6. **Distribution reconciliation:** for each relevant release channel,
   compare exactly the bytes published and those tested. Multiple
   channels/platforms need separate evidence. If listing completeness
   or download origin is unknown, report that limit.

A failure or missing receipt at any link prevents declaring the full
release accepted. A local checksum match is not provenance authenticity
or proof the software works.

## Optional offline measured-byte auditor

A Python 3.9+ standard-library, **read-only** tool is included, using a
versioned JSON release-claim manifest and a locally authorized, bounded
artifact directory. It measures SHA-256 of the actual file bytes, then
compares their digest with claimed build, published, provenance and
installation digests:

```sh
python3 scripts/reconcile.py \
  --manifest examples/synthetic-release.json \
  --artifact-root examples/artifacts \
  --require-local-match
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The fictional example is merely **29 ASCII bytes** named
`fictional-installer.bin`; it is not an executable installer. The
manifest's `schema_version: 1` requires `source`, `build` and
`channels`. Required checks are identified by `name + app`; all
checks and build source are matched to the exact declared source SHA.
For each channel, an item declares platform/architecture, file name
under the supplied root, build and published SHA-256 digests, a
reported external provenance verification record and a reported
installation result. See the complete fictional JSON for the exact
bounded input contract.

**Results:**

- `BLOCKED_CONTRADICTORY_EVIDENCE`: local bytes contradict declared
  checksum, or a source, tag, check, attestation, installation or
  channel claim is materially inconsistent or reports failure.
- `HOLD_INCOMPLETE_EVIDENCE`: essential receipts, successful checks,
  verification assertions, complete file inventory or actual local
  artifact bytes are absent/unsafe. A missing file cannot be called a
  valid release.
- `LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS`: all supplied
  claims agree, and the checker really hashed the local bytes. **This
  is not a secure, proven, authorized or successfully installed
  release.** Attestation, source, publication and installer receipts
  remain *untrusted caller assertions*.
- `RELEASE_HOLD`: malformed JSON, invalid digest, unsafe path, bad
  schema or other failed input bound. Repair input rather than
  bypassing the check.

By default the CLI exits 0 after emitting a bounded report, even if
mismatches exist; optional `--require-local-match` exits 3 unless
all the supplied stages structurally agree and local bytes match.
Malformed input exits 2. **A CLI exit 0 never authorizes release.**

The auditor rejects ambiguous `../` paths, symlinked artifact parents,
symlinked manifest/roots and nonregular files. On supported systems it
uses `O_NOFOLLOW` for the actual file open, limits a manifest to 1 MiB,
each artifact to 128 MiB, and at most 32 channels. It never executes
an installer, unpacks untrusted archives, runs source scripts, contacts
GitHub, fetches keys or installs dependencies. For larger artifacts,
use a separately authorized, appropriate trusted verifier; do not
weaken bounds. **Concurrent directory writers can race filesystem
inspection:** the host must provide an isolated stable snapshot for
security-relevant reliance. This tool is not a sandbox.

## Verification and decision report

Include a concise chain ledger: *expected source → observed exact-head
checks → build run/artifact → published channel/download origin →
locally computed digest → trusted attestation verifier receipt →
isolated installation/acceptance → actual user outcome*. Record which
links are independently verified versus alleged, source/as-of,
revision-bound proof references, actual platform and actor who can
resolve each gap.

Report **NO_GO / EVIDENCE_HOLD / ELIGIBLE_FOR_INDEPENDENT_RELEASE_SIGNOFF**
only after authority and trusted evidence are verified outside the
offline planner. Do **not** label its local-match status GO, approved
to ship, secure, signed, reproducible or working. A signed checksum
does not prove the software installs correctly, and passing a build
does not prove the installer contains the intended change.

Before a material release, independently use current official
release provenance guidance. Relevant factual references include
[SLSA provenance](https://slsa.dev/spec/v1.0/provenance)
and [GitHub artifact attestation verification](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations).
Their documentation is **not** bundled source, and this skill
does not import their code or forge their verifier receipts.

## Adversarial qualification and multi-turn use

[The bundled scenarios](examples/acceptance.md) contain planted
digest tampering, stale/failed CI, tag drift, wrong signer subject,
missing receipts, platform gaps, symlink attempts, and false
completion. They are entirely synthetic tests, not observed release
or consuming-agent results. Keep the same target release, protected
quality gates and unresolved channel obligations across follow-ups.
Never turn an open PR, authored test pass, or simulated demonstration
into a claim of a published functional product.

## Multi-turn continuity when the work is not one-shot

Treat follow-up messages as continuation of the active task unless the user explicitly changes its objective. Before the next substantive action, recover from available conversation or authorized artifacts: **objective, confirmed decisions, completed and uncompleted work, protected checks, blockers, and next acceptance step**. Do not invent unavailable history or claim persistent storage. Reconcile new instructions with this state; current user direction may change scope, but never silently remove safety, approval, source integrity or verification gates. Execute the next concrete step rather than repeatedly restating a plan. For longer work, provide a compact progress/handoff note showing what is done, what remains, and what evidence supports completion. Do not equate a drafted artifact, open PR, proposed test or green isolated check with the user's actual finished outcome. No autonomous follow-up, session creation or background execution is implied.

## Optional, anonymized-content skill feedback

If this skill reveals a reproducible defect, unclear instruction, safety gap, or useful improvement, the working agent may **optionally** prepare feedback at https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml. Feedback is **not required** to use or complete this skill. Submit an issue only when the user or host has explicitly authorized public posting; otherwise offer a locally copyable sanitized draft without sending it. Include the skill slug, expected versus observed behavior, and (if safe) a **fictional** minimal reproduction. Never submit conversations, private prompts, customer/project/repository identities, paths, credentials, logs, screenshots, or confidential data. If details cannot be safely generalized, do not post. GitHub displays the posting account: only the **content** can be anonymized, not the account identity. No telemetry, automatic reporting, or background network activity.
