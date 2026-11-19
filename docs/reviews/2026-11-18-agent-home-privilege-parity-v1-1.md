# Agent workspace and privilege replacements: exact-package static review

Review date: 2026-11-18; audit issue #738.

## Functional comparison and provenance

Compared the retained historical procedures against independently
authored, currently revised replacements:

| Historical input | Comparator Git blob | Authored v1.1 target |
| --- | --- | --- |
| `skills/agent-home-doctor/SKILL.md` | `3415f1f4bb72afc44266706be649c3950f809337` | `agent-workspace-footprint-assessor` |
| `skills/permissions-review/SKILL.md` | `18f46840032829963715ec23894f7826dbbfcb77` | `privilege-exposure-mapper` |

The historical account and author marker do not establish original
copyright authorship or reuse permission. Comparison covers essential
functional outcomes, not copied wording or historically bundled
assets. Legacy files and their history remain unchanged. New
instruction and synthetic-case wording is independently authored.

## Identified loss and remediation

**Agent workspace audit:** v1.0 offered a safe footprint ledger, protected
object classes and a consent gate, but did not explicitly guarantee
diagnosis of broken configuration references, obsolete-layout
migration debris, retained backup recovery usefulness, or an
action-by-risk-tier operator plan. V1.1 defines six pathology classes
with evidence requirements and four risk tiers, including explicit
rollback, independent operation approval and post-operation readback.

**Privilege mapping:** v1.0 offered strong composite authority graphs
and rollback concepts but did not explicitly require full version-bound
MCP/connector inventory, hook and shell allowlist analysis, or the
Git execution configuration hazards that the predecessor covered.
V1.1 requires the source-bound inventory, classifies each tool and
hook, rejects permissive shell patterns, preserves unknown usage
status and provides a bounded least-privilege plan.

**Authority correction:** Workspace v1.0 already described actual
filesystem moves/deletes after separate authorization despite
registering `read-only`. V1.1 continues to default to
read-only inventory but its **maximum supported host operation is
mutating**, and both index and companion records are being updated to
reflect that. The permission mapper remains read-only. No static
skill may itself grant any mutation.

## Package identities

All packages have exactly three tracked files: SKILL.md, MIT LICENSE,
and `examples/synthetic-cases.md`.

| Package | SKILL blob | Cases blob | Complete Git tree |
| --- | --- | --- | --- |
| Workspace v1.0 (historical) | `d350c6e9f9bb396d7f5844109e5ee6c74d5b5a43` | `fb789a2c31a57e36157b28fe15147715accdcb72` | `e4846d301e09eb6851cc89325fc0528cccc29406` |
| Workspace v1.1 | `64e86c622b7242a6f0cd7f4489ce2525473fcfb2` | `00fed7d47f3afe47ad97918ba90c9f5f547f3eef` | `8437369eaa92cecd6ce036ce4733f8e132f8caee` |
| Privilege v1.0 (historical) | `7e1b0048bc244a4903ec2011b319e16317779970` | `917daec09ec5efa29f38216391380f241ce2b1c0` | `d4a6a4b07469ee6753fa7da0164db4c9a39787ec` |
| Privilege v1.1 | `2e07c2ff66fd6af2a55866d5b96c3bb877fb138f` | `b5cb507afd2abc803f67ec513d6e616faea92159` | `0bcb42382d152636c4b9f7c6c70367eb52633740` |

The unchanged MIT LICENSE Git blob is
`023abdb34298b27580d1d303084aca942050585e`.
Both historical package trees were independently reconstructed from
recorded blobs, reproducing the exact previous Git tree values.

## Static security and quality

Manual review of both complete revised packages, 16 new original
adversarial expected outcomes and the historical functional
requirements. No authorized user filesystem, MCP server, hook,
private settings, secret store or real remediation command was
accessed or executed. No external host behavior was observed.

Current ten-dimensional semantic rubric (trigger, procedure,
authority, failure, evidence, dependency, portability, usefulness,
adversarial, effectiveness):

| Package | Values | Score | State |
| --- | --- | --- | --- |
| Workspace v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | VERIFIED_STATIC |
| Privilege v1.1 | 2,2,2,2,2,2,1,2,2,1 | 18/20 | VERIFIED_STATIC |

Static review found no hard fail. Exact target paths, authorization,
private-data boundaries and record of failure remain explicit.
Portability depends on external host inspection/operation controls.
Effectiveness is only a source-design assessment, not a validated run.

## Remaining gates

No real host-agent acceptance, actual file mutation, shell-helper
escape test, connector enumeration, binary package security scan,
paired predecessor/replacement execution, or 1.5x quality measurement
was performed. Behavioral parity remains NOT_RUN; improvement >=1.5x
NOT_PROVEN. Do not retire the two historical entrypoints.

Confirm final exact-head index, companion values and merge receipt.
