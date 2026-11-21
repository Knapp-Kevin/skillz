# Evidence-Driven Refinement Loop v0.3.1: adversarial source review

**Date:** 2026-11-21  
**Target:** `skills/authored/evidence-driven-refinement-loop/` on draft PR #826  
**Current reviewed SKILL.md Git blob:** `d921b7fd317a04ac9327bb874e23eb678a75182f`  
**Complete package tree:** `f57d732c4fe16f8d41c149c478f57966acba6b0b`  
**Evidence limit:** exact-source readback and adversarial static inspection. **No Python suite, independent consuming agent, user acceptance, or hosted security test executed.**

## Review method

Compare the installed skill's actual `SKILL.md`, bundled router, schema,
example, Python preference manager, existing tests, and package references.
Look for an untrusted local file changing canonical policy; writes without
user approval; incorrect privacy claims; lost or blocked preference revocation;
invalid commands escaping the CLI dispatcher; unsafe file metadata races;
and false claims of persistence or host behavior.

The core skill is an instructional artifact, not a sandbox or identity provider.
An on-disk `preferences.local.json` stores **only user-approved, allowlisted
data**, outside public/source/distributed files; it cannot authorize arbitrary
commands or modify `SKILL.md`. The host must supply actual authorization and
user-specific storage. A Python `--approved` flag is not proof of consent.

## Reproducible code-level findings and corrective changes

| Priority | Source finding | Correction | Evidence status |
| --- | --- | --- | --- |
| P1 | `execute()` previously relied on argparse for allowed actions; a direct caller with an unknown action could fall through into remove/delete logic without its mutation gate | Explicit allowlist and refusal **before** any storage access; planted regression `test_unknown_direct_action_cannot_mutate_without_approval` | Exact source changed; Python test NOT_RUN |
| P1 | A stale version or malformed JSON blocked `clear`, preventing the user from revoking their own preference data | Approved `clear` bypasses skill/schema/JSON parsing, but still checks real private file ownership, mode and non-symlink type; deletion must be confirmed | Exact source changed; stale/corrupt/schema-unavailable regression methods added, NOT_RUN |
| P1 | `SAVED` was reported immediately after atomic rename with no stored-state readback | Reopen, permission-check, deserialize and compare the actual stored document; fsync file and containing directory; refuse a success claim if verification fails | Exact source changed; planted readback/fdatasync regressions added, NOT_RUN |
| P1 | `lstat()` checked one pathname before opening another, allowing a different opened regular file's permissions to escape verification | `fstat()` checks the **opened** descriptor owner/type/mode/size before reading | Exact source changed; mocked descriptor-swap regression NOT_RUN |
| P2 | A private directory under a world/group-writable, non-sticky ancestor could be replaced by another OS identity while the program resolves paths | Require absolute root and no symlink/replaceable path ancestors; retain 0700 private directory requirement; document trust limit | Exact source changed; three negative ancestry tests NOT_RUN |
| Not a defect | First-pass review incorrectly reported missing JSON Schema `required`/`additionalProperties` guards | Second read showed these guards already present; no code change or fabricated regression credited | Verified existing schema Git blob unchanged |

## Threat boundaries that remain

- **Same-UID processes:** permissions such as 0700 and `O_NOFOLLOW`
  cannot isolate a user from another hostile process that holds the same OS
  identity. This helper is **not** a hostile-process sandbox.
- **Concurrent writers:** the read/modify/write cycle has **no
  cross-process transaction lock**; independent authorized writers can
  race and overwrite one another's otherwise valid changes. Host must
  serialize writes or provide a lock-backed user-private store.
- **Consent provenance:** `--approved` enforces a deliberate invocation
  convention but can be supplied by a caller; only the consuming host/user
  can establish actual action-specific consent.
- **Portability:** the helper fails closed without POSIX ownership/mode
  checks. Windows/non-filesystem hosts require a trusted native adapter
  or a current-interaction-only fallback.
- **Version reconciliation:** upgrading a canonical skill does not
  automatically approve converting old preferences. Invalid or obsolete
  entries remain held, except that a user-approved full deletion is
  independently supported.
- **Crash/partial writes:** a failed directory sync or verification may
  occur *after* a file was replaced. Report partial uncertainty; inspect
  the actual file. A failed method is not proof of rollback.
- **Host compliance:** source instructions and static helpers do not
  establish that a deployed AI agent will classify feedback correctly,
  always apply overlays, or preserve multi-user isolation.

These are limits on the claim, not permission to ignore them. Publication
of stronger isolation/persistence guarantees needs actual host tests and
a defined attacker model.

## Current static qualification

- Independently reconstructed **10-file** Git tree matches the registry
  pin `f57d732c4fe16f8d41c149c478f57966acba6b0b`.
- `SKILL.md` blob matches `d921b7fd317a04ac9327bb874e23eb678a75182f`;
  the version and example refer to `0.3.1`.
- Local Markdown references resolve, including the embedded preference
  router, schema and manager.
- Source-order assertions confirmed early unknown-action refusal and
  consented clear **before** skill version/schema reads, post-write
  readback checks, descriptor checks, and directory-owner checks.
- The schema already requires `key`, `value`, `source` and rejects
  additional preference fields. Do not record that as a repaired defect.
- **30** optional Python preference-manager test methods are committed,
  including planted adverse cases; **NOT_RUN**.
- **22** optional engine source-contract methods are committed; **NOT_RUN**.
- No independent host observation, privacy penetration test, consumer
  acceptance, or quantitative effectiveness improvement is claimed.

## Required next proof

Execute both optional suites against the **exact branch** in an approved
isolated POSIX environment; investigate every failure, then pin new source
after remediation. Follow with a two-profile consuming-agent test
demonstrating preference isolation, override refusal, revocation and
same-canonical-skill stability. Test concurrent writers or require a
host-provided serialized store before promising concurrency safety.
Retain PR #826 as draft until the maintainer can substantiate acceptance.
