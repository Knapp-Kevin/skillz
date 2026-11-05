# Issue #402: three more historically incomplete Q8 packages, reviewed as passive source

**Review date: 2026-11-05.** Source: [exact-source machine ledger](../../registry/security/q8-three-incomplete-execution-and-rights-static-dispositions-20261105.json). This tranche is 3 **complete pinned packages**, six owned files, plus two root MIT license texts. All exact package-tree and SKILL.md Git object identities match the historical Q12 register. Selected packages still match the corresponding upstream default branch tree on the review date, even though the GitHub awesome-copilot repository head has advanced. No source script, mastering command, evaluator, HTTP request, outbound message, or behavioral host test was executed.

Historical NVIDIA SkillSpector verdicts remain **INCOMPLETE**, not upgraded to PASS. Static source review can determine that a script contains an overwriting action, or that a contract is self-contradictory; it cannot establish that code was safely executed or that an operator authorized a future operation.

## New source-review decisions

| Skill | Pinned complete package | Static score | Unchanged-use decision |
|---|---|---:|---|
| [Audio Mastering](https://github.com/FuDesign2008/open-music-skills/tree/95e66582a82579fa44dca55fff64b874de608a98/skills/audio-mastering) | `33e78f89415c2963d60e49b2ed921db5` | 10/20 | **HOLD** code execution: overwrite/verification correctness |
| [Verify Agent Action](https://github.com/github/awesome-copilot/tree/f11a4e441c5ff061b4f8ae37952be8c602e4034e/skills/verify-agent-action) | `23d23e397768e21750ad9bc3497d01eb32e15736` | 15/20 | **Reference-only**, evaluator run needs separate permission |
| [Shopify Review Triage](https://github.com/github/awesome-copilot/tree/f11a4e441c5ff061b4f8ae37952be8c602e4034e/skills/shopify-review-triage) | `478c553aa5e1983b5f629697235ba70811e2617d` | 16/20 | **Reference-only**, copied third-party rubric rights unresolved |

### Audio Mastering: meaningful output safety and verification defects

**Pinned SKILL.md:** `9570c7ef2689f32a88e844d6c1bb51d17b64b525`. Four exact owned files inspected: SKILL.md, both bundled Python scripts and one eval case; root MIT license `36f5a47244ee233936f9f1eb87b5bbd70fc81a71`. Scanner found genuine subprocess calls (LP3, AST4), but that alone is not malicious content. Its static-parse/reference limitations persist as historical scanner evidence.

The source repeatedly promises that originals will never be overwritten. But `scripts/master_twopass.py:31-32,49-52` takes a caller-supplied `--out` directory, then invokes FFmpeg with `-y`, automatically replacing a file at the output path. With `--out .`, or a symlink resolving back to the source, the output can target the input. This is a **high-severity data-preservation contract failure**, established from the code, not a reproduced incident. The default `mastered/` output reduces the ordinary-case risk, but is not an enforced prohibition.

A separate **high-severity verification defect** appears in `master_twopass.py:18-22,52-65`: the initial FFmpeg measurement's return code is not tested, and a failed second-pass render does not prevent the later verification loop from scanning any previous output with that filename. The final report accepts a LUFS-range check without also enforcing the promised true-peak ceiling, enabling misleading success. A reproducible test suite would need fail-on-error processing, isolated output paths, checksums and exact-output verification.

`scripts/rms_silence_check.py:25-43` divides minimum smoothed RMS by the maximum. Entirely silent audio has a zero denominator, producing invalid ratios rather than meaningful controlled silence evidence; the prompt-compliance threshold is also an unverified heuristic. Finally, the package's fixed EQ/lowpass recipe and streaming LUFS table are based on limited examples, not verified current standards for every provider.

**Positive design:** retaining original WAV files by default, measuring loudness before and after, and passing subprocess arguments as an array rather than shell interpolation. **Remediation:** reject output/source path and symlink identity collisions, require explicit overwrite permission, fail closed on subprocess exit failures, verify the exact freshly written output including true peak, guard zero RMS/empty files, and qualify provider-specific claims.

### Verify Agent Action: strong governance philosophy, inconsistent execution boundary

**Pinned SKILL.md:** `1a8d5dcb0d6accecaef12a806c3c89c689d507a3`. Single-file exact package, root GitHub, Inc. MIT notice `89bc5e962c9944cdb050887062afdaaf89be504a`. Historical scanner is `INCOMPLETE` on one reference flag with no content finding. Reading this source does not justify inventing a scanner security problem.

The source correctly demands `execution_authorized:false`, separate human/enforcement approval, exact action binding, replay protection, reviewer independence, contradiction preservation and monitoring freshness. This is useful as a read-only governance checklist.

**Material high-severity ambiguity:** Its opening safety boundary says never execute anything, but the first control instructs the reviewer to **re-run the declared deterministic evaluator**. An evaluator supplied by a project or untrusted packet could be an executable program, and this step provides neither a trusted-code constraint nor a separate isolated-fixture execution/permission gate. Static recomputation of an already-reviewed formula is different from running arbitrary evaluator source. The procedure must explicitly branch between those cases.

It also requests extensive original approval and monitoring packets without a redaction/minimization rule for credentials or tokens reproduced in the final review. No live nonce store, trusted time source or evaluator was available; therefore this review makes no statement about actual action authorization. **Remediation:** make the default review purely static, permit sandboxed known-evaluator execution only under an explicit independent authorization, and redact sensitive packet fields.

### Shopify Review Triage: privacy-aware, but copying rights are unresolved

**Pinned SKILL.md:** `18970ef465b48008b39cd39bdfcab9ecc120bf52`. Single file at the pinned complete tree; root GitHub, Inc. MIT notice `89bc5e962c9944cdb050887062afdaaf89be504a` read. No source code or network tools are required, and the scanner's historical `INCOMPLETE` state only reports one reference coverage limitation.

The source **explicitly says its keyword lists, priority rules and brief template are verbatim copies from an independently maintained public guide**. The package does not include that guide's license or express redistribution permission. The GitHub root MIT grant for authored source cannot automatically establish rights to a separately authored external work. **This is a genuine copying-rights hold**, even though the classification technique can be independently paraphrased and studied. We did not establish the original publisher's terms; no blanket copying clearance is granted.

The rubric's `checkout` and `error` triggers also produce P0 candidates when a review mentions those words positively or incidentally. To its credit, the source explicitly warns about that and requires a human before promoting a candidate to a verified defect.

**Positive design:** public-review-only input, refusal to accept private merchant or order data, no automatic fetch or reviewer reply, preservation of supplied source links, clear first-pass labeling, and no false claims of comprehensive coverage. **Remediation:** clarify source expression permissions or rewrite independently; keep human review and no-sending gates.

## Progress and next frontier

After this tranche the historically flagged Q8 featured set has **7/7 historically FAILED plus 9/33 historically INCOMPLETE** packages with direct, current pinned static content-risk reviews: **16/40**, leaving **24 historically INCOMPLETE packages** in this priority set. The historical scanner outcomes remain **10 PASS / 7 FAIL / 33 INCOMPLETE** among all 50 featured study references. These are two different evidence dimensions; no new scanner PASS, host execution acceptance, skill installation, or unchanged-use permission was created.

The [current README risk chart](../../docs/assets/q8-direct-static-risk-review-progress.svg) is regenerated from review ledgers rather than painted manually. No capability-domain or total skill admission has occurred, so unrelated capability charts remain unchanged. #402 stays open for the remaining 24 and the larger governed third-party corpus. Continue with still-unreviewed packages carrying real cloud, file, private-data, external payment or subprocess risks before low-consequence documents.
