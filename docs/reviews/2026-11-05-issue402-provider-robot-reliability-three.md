# #402: Adobe, Rerun URDF and MATLAB reliability source-risk reviews

**Date:** 2026-11-05. **Method:** direct passive reading of three complete pinned packages, nine owned source files and controlling available license texts, without executing scripts, accessing accounts, sending private files or invoking vendor tools. Detailed original Git trees, SHA-1 blobs, prior scanner report SHA-256 receipts, scores and findings are retained in the [machine ledger](../../registry/security/q8-three-incomplete-provider-robot-reliability-static-dispositions-20261105.json). Previous SkillSpector **INCOMPLETE** states remain unchanged.

| Exact pinned method | Static score | Disposition |
|---|---:|---|
| [Adobe Create Mockups](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/adobe/skills/adobe-create-mockups) | **12/20** | Reference-only: cloud upload, credits, board-sharing consent and source rights remain |
| [Rerun URDF](https://github.com/rerun-io/rerun/tree/6f39b09211b869d6e262083cfddefa392244088d/skills/rerun-urdf) | **14/20** | Pinned reference only: robot joint-validation defects; newer upstream version not reviewed |
| [MATLAB Analyze Reliability](https://github.com/matlab/matlab-agentic-toolkit/tree/032b4b605999b1f4adecaac1efa1c9faad41adf6/skills-catalog/ai-and-statistics/matlab-analyze-reliability) | **13/20** | Reference-only: censored-data fit defect, runtime and restrictive licensing |

## Adobe Create Mockups

**Pin:** package tree `ee836ce313ba56f96118c9400b07c75486be75d9`, main SKILL blob `2459e742e4e7e0c34140035f14b8d17dda9ad98c`. Inspected `SKILL.md`, agent YAML and both Adobe SVG assets, plus the external-to-package `.codex-plugin/plugin.json` manifest. It claims `license: Apache-2.0` in frontmatter, but the pinned package has no accompanying controlling license text and the Adobe-branded SVGs require separate mark consideration. No copying permission was inferred.

**HIGH:** `SKILL.md:348–408` **always** creates a Firefly Board, adds images, and requests a shareable link after the user asked for mockups. Pilot approval for image generation is not independent consent for persistent board creation and potential link sharing. The skill does avoid changing access permissions explicitly, but that does not authorize the extra workflow.

**HIGH:** `SKILL.md:8–41,80–97,273–314` sends user-uploaded design assets to a signed-in Adobe Firefly service and generates potentially billable images without a separate disclosure/checkpoint for private-brand egress, retention or credit budget. Do not assume authorization from a passive image attachment.

**MEDIUM:** Source distribution rights are unresolved at this pin. The plugin manifest names Adobe Inc. but does not grant unrestricted use of protected code or Adobe logos. In addition, the "never show prompts" directive must not supersede a user's explicit request to review the prompts.

**Useful controls:** image pilot signoff before bulk generation, preservation of source logo through reference-image input, refusal to invent IDs and transparent failure reporting. **Next acceptance:** explicit provider/budget/asset-use approval, separately optional board creation/sharing, source/mark rights clarification and observed scoped host behavior.

## Rerun URDF

**Reviewed historical pin:** package tree `d975189711aed05aadcbc93426906631df481b7e`; SKILL `b5a634f97b0dd20a0bb92a6fe294635cebc219c3`; helper `4c911ffb21ed1b001a5a01009cfec8654194707a`. Read dual upstream root Apache-2.0 and MIT notices; no code copied or run.

**HIGH:** The helper `scripts/check_joint_mapping.py:115–124,153–165` sets `--slack=2.0` by default in the *input unit*. Without `--degrees`, this allows **two radians** of joint-limit overshoot before treating a candidate as unacceptable. The diagnostic can misleadingly call a severe mismatch a tolerated fit and recommend clamping.

**MEDIUM:** `SKILL.md:110–126` warns never to presume URDF joint order equals the source column order; helper lines 129–141 **do** default to that order when `--joints` is absent. Matching counts are not proof of matching identities. There are also no explicit rejects for nonfinite values, unlimited joint limits or negative slack.

**MEDIUM:** `allowed-tools`, package installation examples, `uv run` and S3 `dataset.register_asset` illustrate capability but do not grant installation, file, network, or remote-storage authority. The method visualizes robots; no robot-actuation claim was made.

**Positive:** meticulous guidance for frame consistency, ambiguous joint states, disconnected transform roots and stream identity. **Next acceptance:** finite/positive unit-aware tolerance, explicit source-to-URDF mapping and robust malformed-input diagnostics, tested with permitted synthetic data.

**FRESHNESS HOLD:** The current upstream head `6f0057649fdcdec6b1101e2590dc7280a31f75d1` has package tree `081a3c5f4ab3d5211f1761d8332e705945b5bc26`, **different** from the reviewed pin. Its SKILL blob changed to `85c46e2c7fb546bf0bd34c1c7269e41bd5cc8feb`; helper script blob is unchanged. This is an actual update-available/re-review trigger. **Do not transfer the pinned 14/20 score to the new upstream text.**

## MATLAB Analyze Reliability

**Pin:** package tree `c2476dd8fcc5144429d69a477f41ec0d91d76f25`; SKILL `ed98b6f3ce8ea52e8d3d6b3c19d515e88b3350ed`, manifest and distribution-method reference inspected. Root `LICENSE.md` SHA `7f17a1e8690cca1da0ec834b4e45a86126cdebde` read. Package tree unchanged at observed latest upstream head.

**HIGH:** Although the skill correctly explains `Censoring=cens` for a right-censored lifetime fit, its AIC distribution-comparison example (`SKILL.md:65–144`) fits multiple models **without censoring**. Applied to censored records, the recipe treats censored units as failures, potentially biasing Weibull/lognormal/exponential comparisons and B10/MTTF conclusions. Require `Censoring` consistently for every candidate.

**MEDIUM:** K-S and chi-square tests are presented as formal goodness-of-fit tests on distributions just fitted from the same uncensored sample, without a parameter-estimation p-value calibration caveat. A non-rejection does not certify the model.

**MEDIUM:** The MathWorks root license is *not* unrestricted BSD-3-Clause: condition 3 restricts use of the work and derivatives solely in connection with MathWorks products/services. The SKILL/manifest also link to separate PMRL terms, not reconciled here. `evaluate_matlab_code` requires explicit tool execution authority and the declared MATLAB R2026a+/Statistics Toolbox dependencies. No live toolbox, validation dataset or engineering acceptance was tested.

**Useful controls:** version/toolbox declaration, survival upper-tail calculation and the explicit warning against uncensored GOF tests on censored data. **Next acceptance:** repair censored model-comparison recipes, verify technical procedures on representative authorized data, and resolve source terms before copying or operational use.

## Counts, permissions and next step

This tranche advances **direct reviewed pinned historical flagged Q8 sources to 21/40: 7/7 historical FAILED plus 14/33 historical INCOMPLETE**, leaving **19** incomplete pinned Q8 methods for their first direct source-risk review. The separate **newer Rerun source** also needs re-review and is **not** claimed current. Q8 scanner history remains **10 PASS / 7 FAIL / 33 INCOMPLETE**. No newly installed source, test-host pass, new hosted scanner, source copying, data upload, paid vendor job, or unchanged-use permission was claimed. The [generated README SVG](../../docs/assets/q8-direct-static-risk-review-progress.svg) counts these exact pinned reviews, not approvals or full corpus freshness. The capability-domain chart remains unchanged because no skills were admitted or mapped.
