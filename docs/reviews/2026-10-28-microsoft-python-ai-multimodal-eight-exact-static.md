# Microsoft Azure AI Python: eight changed-existing exact-version static reviews

**2026-10-28.** Source: `microsoft/skills` candidate `61fe0305ea70389ed8705eec6026a786f57865cf`. Registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` remains unchanged. This is static source inspection only, not a security scan, SDK execution, Azure operation, behavioral validation, or source admission.

## Macro-first source-family frontier

Candidate denominator **208** = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned. All 26 new candidates were already reviewed. Eight changed-existing Rust packages were previously completed. This tranche reviews **eight distinct Python Azure AI packages**, moving changed-existing full review **8/76 → 16/76**, with **60 remaining** (29 Python SDK, 30 Azure operations, one skill-creator). All four removed-path candidate decisions were previously completed. Registered July remains **186/186** at its original pin. No duplicate/mirror paths were counted here; these eight canonical package directories each contain one first-class front-mattered SKILL.md plus exactly two reference Markdown files.

All **24 exact-version package blobs** were inspected against the candidate tree, including each complete SKILL.md, capabilities reference, and non-hero scenario reference. Each package's Git tree SHA, three individual blob SHAs, purpose, trigger/nontrigger, source/license, dependencies, authority, privacy, controlled tags, score and decisive disposition are preserved in separate provenance and verification companions. The upstream MIT root license is recorded; transitive SDK/service terms were not independently audited. No local candidate corpus was vendored or installed.

## Individual dispositions

| Package | Score | State | Decisive finding |
|---|---:|---|---|
| `azure-ai-contentsafety-py` | 13/20 | REJECT unchanged | Sends content/images to external Azure analysis; creates/updates persistent moderation blocklists without action-specific approval |
| `azure-ai-contentunderstanding-py` | 11/20 | REJECT unchanged | Remote media analysis and custom analyzer create/delete are service-side and persistent effects without distinct authorization |
| `azure-ai-language-conversations-py` | 13/20 | REJECT unchanged | Example sends conversation text to remote Azure; inferred email intent is classification only, not an authorized send |
| `azure-ai-textanalytics-py` | 10/20 | REJECT unchanged | External NLP processing is invoked without explicit dataset/recipient/service-use authorization |
| `azure-ai-transcription-py` | 10/20 | REJECT unchanged | Batch audio URL submission, stream.send_audio_file and reference delete-transcription operations lack action-specific authorization |
| `azure-ai-translation-document-py` | 9/20 | REJECT unchanged | Translation jobs write translated documents to persistent target storage and can cancel jobs without owner/destination approval |
| `azure-ai-translation-text-py` | 12/20 | REJECT unchanged | Remote text translation and dictionary example requests have no per-dataset disclosure and cost approval boundary |
| `azure-ai-vision-imageanalysis-py` | 11/20 | REJECT unchanged | Image bytes or URLs are sent for remote analysis without scoped data transfer/recipient authority |

## Systemic findings and omissions

- **Authority hard fail, 8/8:** DefaultAzureCredential, environment-backed legacy keys, SDK capability, a configured endpoint, or a service subscription do not authorize transmitting actual content, incurring charges, creating/deleting analyzers or blocklists, writing translated documents, or deleting transcription jobs.
- **Privacy and retention:** Source material includes moderation text/images, invoices and multimodal media, conversational entities, PII and healthcare records, recordings/transcripts, translated documents, OCR, and people-detection outputs. Several examples print raw entities, transcripts, OCR, or source URLs. A secure external data-authorization, classification, minimization and retention boundary is missing.
- **Credential-bearing URL risk:** Document translation uses source/target/glossary SAS-bearing URLs and prints source-document URLs. Preserve the useful Blob translation mechanics without endorsing token-bearing URL disclosure.
- **Shared strength:** These packages consistently favor managed identity, constrain production credential chains, document synchronous/asynchronous client cleanup, and provide concrete SDK patterns. That does not close the missing authorization gates.
- **Duplication:** The capabilities and non-hero references frequently repeat manifest examples. They are package dependencies, not additional independent first-class skills. Their repetition does not supply missing action approval.
- **Distinctive extraction value:** severity/blocklist modeling; async multimodal analyzer polling; confidence-gated intent routing; PII redaction; audio batch/stream and cleanup; format-preserving document translation; language/dictionary operations; and OCR/object/people geometry.
- **Remaining frontier:** 29 changed-existing Python packages, 30 Azure operations packages, one skill-creator package. The source remains high-value reference material but is not eligible for candidate pin advancement without full current-version qualification and independent security/acceptance decisions.

No scanner, test, cloud call, translation, telemetry transmission, installer, or behavioral validation was run. Upstream source-owned examples remain reference evidence only. The repository remains entirely passive.
