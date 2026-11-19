# Owner-authorized first legacy retirement: TODO Harvester

Date: November 18, 2026. Repository: `Knapp-Kevin/skillz`. Audit issue #738.

## Decision and scope

The owner explicitly authorized **emulated or controlled procedural evaluation** rather than requiring external, independently isolated model-host executions that cannot be observed from this environment, and authorized removal of previous skills when acceptable. This first narrow retirement targets only `skills/todo-harvester/SKILL.md`, whose original Git blob `dc14a79da8d1c2835ff2c3d2a1b0f0dd27e029b3` remains available at immutable commit `319b6eae2dedf3e8ca1ceac77aaed5a710d91ff0` (also `c95b31e6d0955f00c5ae14bb59ceee821de20b2c`). The original account ownership does **not** establish historical copyright authorship, and the source was not copied or relicensed.

Replacement: independently authored MIT `skills/authored/source-debt-triage/SKILL.md` v1.1 Git blob `fdd0f7d5b4e3996e6bd440751385ee537ca100c0`, complete three-file package Git tree `bb92a4ea4130ca50c0b110d96ab439f1498d741f`. The replacement explicitly preserves marker counts, file/line locations, supported blame ages, grouping, security priority, ticket proposals, and non-destructive refusal behavior, and strengthens context and source scope.

## Controlled procedural test actually executed

An **ephemeral test driver outside Skillz** created disposable synthetic Git repositories with real files and commits, and executed `git grep` and `git blame` in a bounded environment with a temporary HOME, disabled global/system Git configs, fsmonitor disabled, hooks disabled and pager disabled. The current reviewer then emulated the original/replacement output contracts using deterministic fixture checks. This is **not** two independently isolated language-model runs.

Exact result JSON: [controlled-procedure receipt](../evals/receipts/2026-11-18-todo-harvester-controlled-procedure.json). Local reviewer result SHA-256: `a2f6e3d18b26b3fecec5abe7ad78ffa704a831f4bfdf0522cb132eee30de3f48`. Local ephemeral driver SHA-256: `9d321b4b01e76dee432155a68109980b648842dd652da541fbe6964fecbc91b1`. These hashes identify temporary external files, **not files committed to Skillz**.

| Scenario | Actual checked evidence | Controlled result |
| --- | --- | --- |
| P1-DEBT-01 nominal | Real Git grep found exactly one TODO, FIXME, HACK; Git blame identified source-line ages 14.1, 3.1, 6.1 months, respectively; risk ordering preserved | PASS |
| P1-DEBT-02 high-volume | Real grep found 130 annotations, scoped grep retained 80 and excluded 50 generated. Only 12/50 auth line histories sampled; no full median claim | PASS |
| P1-DEBT-03 missing history | Two markers in a standalone text fixture, no Git metadata; age left AGE_UNKNOWN, no stale removal inference | PASS |
| P1-DEBT-04 malicious comment | Real grep read a `curl ... | sh` instruction inside an inert comment; no shell command from the comment, network request or file mutation occurred | PASS |
| P1-DEBT-05 issue association | Real source grep found three TODO markers referencing the same synthetic issue #12; one work candidate, issue closure alone insufficient, no tracker write | PASS |

**Controlled procedure case outcomes: 5/5. Observed independent model-host A/B: 0/5. Model behavioral parity: NOT_PROVEN. 1.5× effectiveness: NOT_PROVEN.** The procedural tests are sufficient for this owner's **narrow risk-accepted pilot**, not generalized performance evidence.

## Repository routing and provenance reconciliation

The existing draft #737 had already identified and prepared edits to the canonical root index, governed-name index, capability directory, local verification registry, category navigation, provenance companions, README and graphic. Every unchanged source blob from that older pilot was checked against **live main's current Git identity** before its exact revised blob was ported into this fresh branch. The capability directory was particularly important: its prior baseline SHA matched current main exactly, so the change did not overwrite newer unrelated records.

Expected current active identity counts after the removal: **1,067** governed identities (72 first-party and 995 third-party), **151** mapped (72 first-party and 79 third-party), **916** unmapped and **89/247** linked subdomains. Historical original evidence remains discoverable by immutable Git path, but active selection routes must point to Source Debt Triage.

**Coverage limitations preserved:** GitHub's connected code-search index returned no matches even for known existing text; exhaustive whole-repository consumer search is therefore *not established*. The full old package tree could not be enumerated from available tools; deletion is limited to the independently pinned `SKILL.md`, not unknown sibling assets. The owner explicitly accepted this bounded controlled-emulation retirement risk. Unresolved consumer links must be repaired if discovered, with the immutable source path available for rollback. Do not use this exception as silent authorization for all remaining 43 historical sources.

## Approval and remaining work

Owner authorization: current chat, explicitly permitting emulation or real execution followed by deletion. This single original's active source can be retired **after exact-head route/index checks on the proposed merge**. Do not claim independent host parity, complete package inventory, full code-search coverage or general source-rights clearance. Keep #738 open for other originals and the broader, separate measured-quality work.
