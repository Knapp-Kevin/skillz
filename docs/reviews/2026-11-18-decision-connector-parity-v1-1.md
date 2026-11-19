# Decision logging and connector vetting: independent source review

Date: 2026-11-18; governed audit issue #738.

## Origin and functional comparison

Historical references:
- `skills/decision-log/SKILL.md`: `53b82e2a4838cdba57ee2e4c9158d6d2b4150c6b`
- `skills/mcp-vetting/SKILL.md`: `37a13d7296c7d3d87dc360988bc6aca1f873c4db`

Account control and author labels do not establish human
authorship, permission to reproduce historic expression, or
ownership of external assets. The new text and synthetic fixtures
are independently authored to preserve *function*, not copied
historical wording. The old files remain preserved.

The first authored decision-record version provided reasoned
decisions and an optional approved write but omitted an explicit
append-only log guarantee and the old due-date views. V1.1 now
requires record-specific approval and readback, historical
supersession without editing, overdue/upcoming 30-day/event-dependent
views, and never inventing missing decision dates. **Maximum host
authority: mutating** for separately approved append/create operations;
default mode read-only.

The first authored connector risk review provided stronger chained
tool-effect and enforcement analysis but insufficiently required
original license/rightsholder terms and independent security and
host-behavior gates. V1.1 distinguishes static source inspection,
complete-package security qualification and actual host acceptance
as separate evidence levels; requires exact version and license
grounds; preserves the prohibition on connecting or running the MCP
server merely to perform vetting.

## Exact complete-package source identities

Both historical three-file Git trees were independently reconstructed
using their component Git blob IDs and reproduced their recorded
values. Each v1.1 package has SKILL.md, LICENSE and
`examples/synthetic-cases.md`.

| Package | SKILL blob | Cases blob | Complete tree |
| --- | --- | --- | --- |
| Decision v1.0 | `ef0ae9791df3cbf69b0f9445807240188a17f130` | `9625f2d64d335e6e1f24af8349012d9d4b678732` | `992a7db63ea585fc939802dfac1f3cd76abe98a3` |
| Decision v1.1 | `d9005c5c1b3fbed122a52d106104dbee02b5a165` | `5648bdf6b784c34e4dc695af7a571a09a485b504` | `56b32d80412fbae75f05914e992156f081d8ce05` |
| Connector v1.0 | `53dcb0926ba29048e8ef42c5aa1f24ebdf180de6` | `66587b79f2c2cf597ce1ec0246ddc7f625d9b0f9` | `12809e8090eac17a1092fc18f687fd8f957d7fc3` |
| Connector v1.1 | `8a926f202b9fa94e06ca29a7b86826445d1a08ab` | `2ca929e523a2b9b29e85479d73408378e379b03c` | `864c622d0276f4efbe47d5b5ba21b23efbebbf29` |

Unchanged independently authored MIT license Git blob:
`023abdb34298b27580d1d303084aca942050585e`.

## Structured quality assessment

Manual inspection of both revised complete three-file packages and
16 original new synthetic cases, plus the two historic functional
comparators. No external MCP tool, account, scheduler, real decision
file or sensitive data was opened, altered or executed.

Ten rubric dimensions in order (trigger, procedure, authority,
failure handling, evidence, dependency, portability, usefulness,
adversarial design, effectiveness design):

| Package | Vector | Score | Result |
| --- | --- | --- | --- |
| Decision Record Steward v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | VERIFIED_STATIC |
| Connector Capability Risk Review v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | VERIFIED_STATIC |

No static hard fail identified in the exact review. Portability is
limited by whether host read/write or package inspection tools are
actually available. Effectiveness remains design-only. Source
reviews do not establish real legal clearance, authenticated origin
of historical documents, behavioral parity or product safety.

## Open quality gates

- No actual append/readback or due-date audit on a real log.
- No host MCP identity isolation, injection probe, security scanner
  or exact-package runtime acceptance.
- No paired legacy/replacement host execution or measured >=1.5x gain.
- No retirement or deletion of historical entrypoints.
- Recheck exact-head companion/index coherence and actual merge result.

Disposition: SOURCE_STATIC_VERIFIED 18/20; BEHAVIOR_NOT_RUN,
SUPERIORITY_NOT_PROVEN.
