# Q10 supplement: Resemble Detect hosted API skill

**Date:** 2026-11-03 · **Q9 discovery:** #697 · **Q10 review:** #698 · **Status:** promising method, **reject unchanged**

## Result

The pinned [Resemble Detect](https://github.com/resemble-ai/detect-skill/blob/4d31eac1ff9aed33b9a0a192e64f7db57821dc9f/SKILL.md) skill scored **13/20** in static review. It teaches a genuinely useful distinction: **a model result is not a fact about a person or a recording**. When a detector has not completed a job, the agent should not guess. Once it has, an answer should identify the provider, actual status, label, confidence and limitations rather than present a verdict as proven authenticity.

**Do not run unchanged.** Its default API workflows can transfer private recordings, messages, ID documents and visitor metadata to a hosted service and can incur charges or install browser telemetry. The source never establishes a separate authorization gate for those actions.

## What is worth studying

- Keep `processing`, `failed`, `uncertain`, and `completed` results distinct. Do not substitute intuition for an observed API response.
- For text, `prediction=human, confidence=.97` means the detector is confident in its **human classification**, not 97% AI probability.
- Report the detector's conclusion as **probabilistic evidence, not proof** or an independent basis for disciplinary action.
- Require the source and version of the service, and distinguish optional model analysis from a truly verified media chain of custody.

## Hard holds

| Concern | Source behavior | Required before any direct use |
|---|---|---|
| Private-data transfer | `POST /detect`, `POST /text_detect`, and `POST /secure_uploads` send media/text to a vendor | Explicit per-action user permission, sensitivity and third-party rights assessment, retention agreement and documented destination |
| Costs and entitlements | Text requests bill per completed unit; managed investigations consume limited entitlements; visitor telemetry may be charged | Separate approval for billable work, capped budget and documented failure path |
| Site visitor monitoring | Creates integrations, modifies domain lists, inserts third-party script into shared page head | Site-owner authorization, privacy/legal and visitor disclosure assessment, staging test and rollback |
| Unsupported accuracy promises | Gives long-form >99% AI detection and <0.2% false positive claims plus several domain percentages without independent experiment citations in the skill | Reproduce or verify current model/version statistics; do not present numbers as universal guarantees |
| Untrusted results | Detect Agents include SSE events, research content and answer streams | Treat all data as data, never instructions for tool use, secrets, sends, uploads or policy changes |
| Retention assertion | Instructs `zero_retention_mode` but cannot verify vendor-side behavior or secondary logs | Confirm current service terms and actual data handling externally |

## Identity and rights

Pinned commit and root tree: `4d31eac1ff9aed33b9a0a192e64f7db57821dc9f`. Owned skill `SKILL.md` blob `039f7658a9aa1b3895696257c6b119eb9b6125e4` (781 lines). The repository has three blobs: skill, README and full Apache-2.0 license (`261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`). Complete source text, root license and README were inspected. The license of the skill does **not** grant rights to send media, identify website visitors or use vendor APIs without separate authority.

The exact [machine review](../../registry/discovery/q10-resemble-detect-hosted-static-20261103.json) gives all ten axes, static adversarial scenarios and copy conditions. This is **not** an API conformance test: no bearer token was used, no file uploaded, no request made, and no security scanner or behavioral test run.

**Disposition:** 13/20; promising completed-result method to study, but no unchanged-use recommendation, positive feature promotion, hosted-API clearance or runtime acceptance.

