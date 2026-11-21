# Evidence-Driven Refinement Loop v0.3.1: adversarial source review

**Date:** 2026-11-21  
**Target:** `skills/authored/evidence-driven-refinement-loop/` on draft PR #826  
**Current reviewed SKILL.md Git blob:** `d921b7fd317a04ac9327bb874e23eb678a75182f`  
**Complete package tree:** `a98510befd694a2509cfb469cf3829646bef0405`  
**Evidence:** exact-source review plus later successful GitHub Actions regression tests (see executed-evidence addendum). No independent consuming-agent acceptance or hosted security scan has been performed.

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
- **38** optional Python preference-manager tests passed on both Python 3.11 and 3.13 in Actions run 44943402910.
- **22** engine source-contract tests passed on both Python 3.11 and 3.13 in Actions run 44943402910.
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

## Executed-evidence addendum (2026-11-21)

The previously NOT_RUN mechanics suites were subsequently executed on the
public GitHub Actions runners, without using an external scanner or a
consuming-agent host:

- [Workflow run 44943402910](https://github.com/Knapp-Kevin/skillz/actions/runs/44943402910)
  at commit `15e1217d5fc8337afc24ba051b63853bd76ff0c1`.
- Python 3.11: preference-manager tests **38/38 PASS**; engine contract
  tests **22/22 PASS**.
- Python 3.13: preference-manager tests **38/38 PASS**; engine contract
  tests **22/22 PASS**.
- A bounded POSIX `flock` mutation lock now serializes **cooperating**
  managers at the same private root. Contention is refused without
  clobbering state. This does not protect against hostile same-UID
  processes or distributed/multi-host races.
- Two isolated private configuration roots now have an executable test:
  different preferences persist without cross-over; clearing one root
  does not erase the other. Both roots run under the **same POSIX user**
  in CI, so this is a logical isolation test, not a true multi-user
  host tenancy or authorization test.
- The duplicate regression workflow created during development was
  removed. The retained `.github/workflows/skill-preference-qa.yml`
  tests two Python versions on relevant changes.

The full package tree now contains ten files at
`a98510befd694a2509cfb469cf3829646bef0405`; its `SKILL.md`
identity remains `d921b7fd317a04ac9327bb874e23eb678a75182f`.
The pass is deterministic local-mechanics evidence, **not** proof that
actual agents classify preferences reliably, user-specific storage is
correctly provisioned by every host, or users achieve improved outcomes.
`validation_status` therefore remains `not-run` for consuming-agent
behavior.
