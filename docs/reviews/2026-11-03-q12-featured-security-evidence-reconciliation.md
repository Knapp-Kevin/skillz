# Q12: Reconcile featured-method security receipts without relaxing the gates

**Source snapshot:** Q8 draft `d3aaaa29f84b81e1905b295adb3657348551b9d8`, exact source pins and report SHA-256s · **Date:** 2026-11-03 · **Status:** Security evidence index only, **not a scanner rerun**.

## Why this matters

The pinned Q8 catalog has **50** proposed Valuable References. For the original **20** inherited from Q7, the `security_scan` field still says `not-run` even though [the exact-tree external-host scan receipts](https://github.com/Knapp-Kevin/skillz/blob/d3aaaa29f84b81e1905b295adb3657348551b9d8/registry/security/external-host-skillspector-featured-20261103.json) exist and are pinned. A reader opening one of those catalog entries receives stale security information. The [Q8 machine pipeline](https://github.com/Knapp-Kevin/skillz/blob/d3aaaa29f84b81e1905b295adb3657348551b9d8/registry/qualification-pipeline-20261103.json) has the correct combined total, but offers no easy per-method cross-ledger answer.

We did not rewrite Q8's source catalog or original historical records. Instead, the [50-record security reconciliation](../../registry/security/q12-featured-security-evidence-reconciliation-20261103.json) joins **each exact consumer ID, source repository, source commit and package-tree SHA** to one authoritative report. The [CSV](../data/q12-featured-security-evidence-matrix.csv) can be opened in any spreadsheet without redrawing a chart.

| Exact-source subset | Passed | Failed | Incomplete | Total |
|---|---:|---:|---:|---:|
| 20 Q7 external-host reports | 5 | 3 | 12 | 20 |
| 30 Q8 new selected methods | 5 | 4 | 21 | 30 |
| **All Q8 proposed references** | **10** | **7** | **33** | **50** |

**Zero** are approved for unchanged use. Passing one static gate does not authorize installation, paid model calls, secret access, email reads, shell execution, or robotic hardware.

## Seven failed cases: what needs adjudication

| Featured method | Domain | Static findings | Provenance |
|---|---|---|---|
| Audio Performance Debug | testing | MP2 MEDIUM | Q7_EXTERNAL_HOST_RECEIPT |
| scenario-storyboards | illustration | P9 MEDIUM | Q7_EXTERNAL_HOST_RECEIPT |
| scenario-identity-library | illustration | P9 MEDIUM | Q7_EXTERNAL_HOST_RECEIPT |
| Singapore SSP Navigator | law | EA2 MEDIUM | Q8_BATCH_2_PINNED_REVIEW |
| Geospatial and Cartographic Visualization | analytics | AR2 HIGH | Q8_BATCH_3_PINNED_REVIEW |
| Dynamo Interconnect Check | ml-accelerators | MP3 HIGH, AS3 MEDIUM, LP3 MEDIUM, AST4 MEDIUM | Q8_BATCH_3_PINNED_REVIEW |
| Cross-border Unit Economics | business | P2 HIGH | Q8_BATCH_4_PINNED_REVIEW |

The failed state is retained for **all seven**. Existing host false-positive proposals for the FFT term `pad input` and two padded Markdown rows are **plausible**, and two examples were independently checked against upstream pinned source text. However, they remain **unaccepted** findings. Removing a textual scanner alert would not fix the other holds: audio SIMD code safety, Scenario API permissions and media rights, privileged GPU/Dynamo commands, unresolved licenses, dated Singapore legal advice, or undefined financial-method dependencies.

A security pass is just one checkpoint. For example, a candidate that includes a static-gate pass may still clone an unpinned repository, access private files, depend on an unreviewed MCP server, or require paid hosted services. Do not turn a green scanner row into a consumer recommendation.

**New Q8 source pin:** Boltz Protein Design was added for a **generic cost-scoping idea** only. The original skill can contact paid services, transmit inputs and requests permission bypass; the exact scanner state is **incomplete**. This catalog reference is **not** permission to run the source or reproduce its scientific procedure. No unsafe experimental instructions are included here.

**New Q8 study-only references:** Room Acoustics (REW), Rerun URDF Ingestion, Nav2 Navigation Debugging, and MATLAB Reliability Analysis add **two static passes and two incomplete scans**. Their source methods may involve paid proprietary tools, ROS hardware, web access or licensed MATLAB, so no execution authority or unchanged-use approval is implied.

## The 33 incomplete scans

Across incomplete reports, the ledgers contain **167** `reference_missing` occurrences, **5** `obfuscated_instruction_text` occurrences and **8** `static_parse_limit` occurrences, plus **1** `analyzer_runtime_error` occurrence. These are **occurrences, not distinct packages**; some packages generate multiple reasons. A missing reference may mean a true unbundled sibling dependency, a named runtime output, a user local file, or a path outside the reviewed package. It cannot be automatically marked harmless.

Prioritize exact file/path classification per candidate and maintain separate gates:

1. **Licensing or sensitive-data/authority holds:** resolve controlling license text, privacy and expense boundaries; never accept an incomplete scanner as proof of safety.
2. **Technical coverage failures:** classify every missing reference by *required bundled file*, *optional sibling*, *runtime output*, or *external user input*. Re-scan actual package boundaries in an authorized isolated host when appropriate.
3. **Potential false positives:** record source lines and bounded counterexamples; only an authorized maintainer may accept a finding disposition. Keep the original scanner result immutable.
4. **Passing scans:** run representative/adversarial behavior tests where authorized. Do not label source-level quality or real-world correctness as proven by a scanner.

## Maintainer and integration requirements

This matrix was generated from six immutable source ledgers and the Q8 catalog and pipeline, each pinned by Git blob SHA in its JSON header. It checks unique consumer IDs, matching exact upstream commit/tree, per-report SHA-256 format, and totals `5+5=10`, `3+4=7`, `12+21=33`. It intentionally **does not** claim to have rerun SkillSpector, executed third-party code, copied upstream proprietary material, or approved false positives.

Preserve as a dated, source-pinned derived security evidence view. Its Q8 source is an unmerged draft; do not replace live README/graphics counters, rewrite Q7 historical scan fields, or present scanner results for a changed package tree without a new exact-tree scan. The Q11 visual/CSV and generator have been archived separately because their source reports an earlier 45-method Q8 proposal. On a new Q8 branch head, recompute the exact join first. Use the pinned [Q8 #693](https://github.com/Knapp-Kevin/skillz/pull/693) source snapshot for resolving historical records; Q11 #699 was closed without merge after byte-identical archival consolidation. Recompute this derived join when Q8's accepted final tree differs from the pinned source.


## 2026-11-04 acceptance audit

Verified 50 unique IDs and security statuses from the machine JSON: 10 passed, 7 failed, 33 incomplete. Fetched all seven source ledgers at pinned Q8 head `d3aaaa29f84b81e1905b295adb3657348551b9d8` and matched every declared Git blob SHA (7/7). The 50-row CSV includes a header plus 50 entries; the Q11 chart/CSV/generator are archived as a separate historical 45-reference snapshot, not live data. This is read-only evidence validation and does not execute SkillSpector or test candidate agents. No unchanged use is approved.
