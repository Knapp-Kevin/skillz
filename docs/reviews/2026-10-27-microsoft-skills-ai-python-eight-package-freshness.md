# Microsoft Skills freshness: eight Azure AI Python candidate packages (2026-10-27)

**Decision:** **8/8 REJECT unchanged at the latest observed upstream revision**. All eight remain useful **EXTRACT/ADAPT/REFERENCE** prior art. This is a bounded freshness review for [issue #400](https://github.com/Knapp-Kevin/skillz/issues/400), **not** a source-pin advancement, a current registered-pin companion replacement, a package-security pass, or behavioral validation. No third-party code, package, credential, cloud request, or sample was executed.

## Live source-family macro map and exact identity

- `skillz` starting main: `66825507835978801d4cf31c733d1b0f831e79fe`; 44 first-party, 22 registered sources, 721 persisted third-party exact-version companions. All admitted families explicitly marked complete have zero **registered-pin static** gaps.
- Registered Microsoft pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` with **186/186** governed static reviews. The previously established **complete** 2026-10-10 candidate tree `d5741a1e9325adead3a28d1d203bb69283907e06` partitioned those 186 as **106 exact-subtree carry-forwards, 76 changed, 4 removed**, with **22 newly observed raw SKILL.md paths** requiring eligibility/alias review.
- Latest upstream Microsoft HEAD read on October 27: `1a63e5f771987a9a13e9f0571823dc1e80741583`. Registered-pin-to-latest comparison: **138 commits ahead**, **300 returned changed paths**, hence **CAPPED** and *not* a complete latest candidate denominator. Separately, the **October 10 candidate-to-latest** compare reports **20 commits and 206 changed files**; none are inside the eight selected package subtrees. Their **complete package tree SHA-1s from the previously verified untruncated October 10 tree therefore carry forward** to this exact latest head. All eight SKILL.md blobs were independently read at latest HEAD and match that earlier candidate tree evidence. This does **not** imply that the other 178 packages are unchanged.
- Scope selected: eight `azure-sdk-python` AI language, media and translation packages, all eight from the **76 changed existing** bucket at October 10. Each has a canonical first-class `SKILL.md`, two declared Markdown reference files, and an individual source-tree identity; the two declared references were fetched/read for each. Root Microsoft MIT license text read at latest head, blob `79656060de00aa4659ad2c276d5be8830664d544`; each manifest declares MIT. SDK dependencies are not locked and their independent redistribution terms are not audited.
- Shared authority/privacy clusters: billable Azure API calls; off-device document, image, text, audio and conversation processing; consent/regulated-data boundaries; legacy environment-backed API keys; service-side remote URL retrieval; local/remote writes and deletes; unredacted output/logging; SAS-bearing URLs. Shared positive controls: preference for Entra/managed identity, constrained production credential chains in most manifests, context-managed client cleanup, explicit SDK examples and references.
- Controlled taxonomy from `registry/taxonomy.yaml` applied per record. Structured rubric uses ten dimensions at 0–2 each from `docs/skill-verification.md`. **Authority/safety=0 and hard-fail for all eight**, independent of total score. None may be promoted to `verified` unchanged. Every actual behavioral and pinned package-security state remains `not-run`.

## Individual exact-version candidate decisions

| Canonical package | Exact SKILL.md blob SHA-1 | Exact package tree SHA-1 | Static rubric | Decision |
|---|---|---|---:|---|
| `azure-ai-contentsafety-py` | `9caadcc9ee73fa54a2336d6ab117a1e2690e530f` | `63dca1fa9603fd7514ce7c586bb1cf1a51ad3761` | **13/20** | **REJECT unchanged** |
| `azure-ai-contentunderstanding-py` | `5b59e23e547de5392ef1c98a3b4bb7ab91b34738` | `bdc77f05d3f0f8fceb5c6160d84a7c8814906e6b` | **12/20** | **REJECT unchanged** |
| `azure-ai-language-conversations-py` | `2d678f3181212c68164e8e0becd844c889079982` | `065885039d26abe547d0059e2248cb2da1097717` | **12/20** | **REJECT unchanged** |
| `azure-ai-textanalytics-py` | `3f7ec0d3239a968bb2acb0bec5fa6956894365cd` | `375453ad9ff4f6867adf6623a1b567bfe0c60bfb` | **12/20** | **REJECT unchanged** |
| `azure-ai-transcription-py` | `e27cf1800cec405570f25dbed2b8f9de014192de` | `c21d6071b1414199c46f08dcf3a1a0632843d00d` | **11/20** | **REJECT unchanged** |
| `azure-ai-translation-document-py` | `64da88e8a88f1ff64c38261c0ca0df09544f3b70` | `e548c746ec02f0ec9d2acb4adf18334d6ca0edf3` | **13/20** | **REJECT unchanged** |
| `azure-ai-translation-text-py` | `e8ed670c9d5e23a5a08bee0684c7ea18f64fa809` | `1d0affb190094b511470c1f6b9622044d5c3c25f` | **13/20** | **REJECT unchanged** |
| `azure-ai-vision-imageanalysis-py` | `adaaf3c05668d618d8c5a932e37ac78053a255c7` | `bc979291b13c4a0b5c3133fb8a12ae94a7a55883` | **12/20** | **REJECT unchanged** |

### 1. `azure-ai-contentsafety-py`

- **Purpose / differentiator:** Severity classification, category coverage, credential-chain preference, context-managed client lifecycle.
- **Dependency / portability:** `pip install azure-ai-contentsafety` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`529c17761535106b3a6faa9b8c363d7d2237509f`) and `references/non-hero-scenarios.md` (`3d08cd4522ed615eb3953c1bc05c803ce7dcc42f`).
- **Decisive authority/privacy failure:** Unapproved external transmission of text/images and image URLs; create/update blocklists without distinct persistent-write approval; advice to log moderation results without minimization or retention rules.
- **Static score:** 13/20; ten dimensions in rubric order: `1,2,0,1,1,2,1,2,1,2`. Prior registered-pin score: 13/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** EXTRACT severity decision logic; ADAPT only with consented content scope, remote-fetch boundaries, blocklist write approval and redacted logs.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 2. `azure-ai-contentunderstanding-py`

- **Purpose / differentiator:** Multimodal analyzer selection, long-running poller handling, sync/async lifecycle, extraction schemas.
- **Dependency / portability:** `pip install azure-ai-contentunderstanding` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`d03bbc131c15cd4c863b8e2ee7aec0d3f4fc821b`) and `references/non-hero-scenarios.md` (`754b45efbb519353e109c82813e7dd010a2e71a7`).
- **Decisive authority/privacy failure:** Cloud analysis of potentially sensitive documents/audio/video/frames and external URLs without disclosure consent; extracted transcripts/invoice fields printed; custom analyzer creation and deletion lack operation-specific authorization.
- **Static score:** 12/20; ten dimensions in rubric order: `1,2,0,1,1,2,1,2,0,2`. Prior registered-pin score: 11/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** EXTRACT typed extraction/LRO method; require approved data class, region, retention, safe output and separate analyzer lifecycle permits.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 3. `azure-ai-language-conversations-py`

- **Purpose / differentiator:** Structured CLU intent/entity payloads, service logging disabled in examples, retries and context-managed clients. Earlier unclosed Markdown code fence appears repaired.
- **Dependency / portability:** `pip install azure-ai-language-conversations` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`abaae4b5497f1da0eb43979216606736c5fa20fe`) and `references/non-hero-scenarios.md` (`fded76ab3ee4ed889affefda31a3e6e507b1ec55`).
- **Decisive authority/privacy failure:** Arbitrary conversation content transmitted to Azure without participant/privacy authorization; recommends latest SDK without reproducible version pin; entity text can be printed in supporting examples.
- **Static score:** 12/20; ten dimensions in rubric order: `1,2,0,1,1,1,1,2,1,2`. Prior registered-pin score: 11/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** ADAPT with data classification, participant consent, output minimization, fixed SDK constraints and non-trigger boundaries.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 4. `azure-ai-textanalytics-py`

- **Purpose / differentiator:** Sentiment, entities, PII detection, healthcare entities and batch error handling with Entra-first auth.
- **Dependency / portability:** `pip install azure-ai-textanalytics` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`19ce159a085f49df02218d03f9b3229dce172761`) and `references/non-hero-scenarios.md` (`461cb890d8482c2f81f34e956c989d7601117fb7`).
- **Decisive authority/privacy failure:** Explicit raw SSN/email sample prints detected PII after redaction; healthcare example sends patient/medication text to Azure and prints extracted entities; no consent, output-redaction or retention gate.
- **Static score:** 12/20; ten dimensions in rubric order: `1,2,0,1,1,2,1,2,0,2`. Prior registered-pin score: 12/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** REFERENCE/EXTRACT API patterns; require regulated-data authority, consent, redaction before output, bounded retention and approved endpoint.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 5. `azure-ai-transcription-py`

- **Purpose / differentiator:** Batch/streaming speech-to-text, timestamps, diarization, retry/backpressure and client cleanup; now describes optional token credentials.
- **Dependency / portability:** `pip install azure-ai-transcription` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`9f35147fd7a79ac43546f128bc79207719bd606c`) and `references/non-hero-scenarios.md` (`5fec3267ca85205468c6d0e8c5f413c490db0a7e`).
- **Decisive authority/privacy failure:** Audio/meeting content uploaded without recording or participant-consent gate; remote cost-bearing transcription jobs; prints speech content; supporting reference deletes completed transcriptions without explicit lifecycle approval.
- **Static score:** 11/20; ten dimensions in rubric order: `1,2,0,1,1,1,1,2,0,2`. Prior registered-pin score: 11/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** EXTRACT timing/diarization procedure; require participant consent, recording-law review, scoped job/budget approval, redacted transcript handling and deletion permit.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 6. `azure-ai-translation-document-py`

- **Purpose / differentiator:** Format-preserving batch/single translation, LRO/error handling, least-privilege SAS guidance, sync/async credential lifecycle.
- **Dependency / portability:** `pip install azure-ai-translation-document` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`d0ead4f44fb47932672a1ac538e618a0900158c4`) and `references/non-hero-scenarios.md` (`15eb6947c060176985d407d2424c93bc9faae6e2`).
- **Decisive authority/privacy failure:** SAS-bearing source/target/glossary URLs and source-document URLs printed in status; remote translation creates persistent output and incurs costs; cancellation and local writes lack scoped authorization.
- **Static score:** 13/20; ten dimensions in rubric order: `1,2,0,1,1,2,1,2,1,2`. Prior registered-pin score: 13/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** ADAPT with secure non-chat SAS handling, source/target ownership verification, approved document classification, cost caps and explicit write/cancel permissions.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 7. `azure-ai-translation-text-py`

- **Purpose / differentiator:** Translation, transliteration, dictionary, source-language and output options; Entra/custom-subdomain vs legacy key nuance.
- **Dependency / portability:** `pip install azure-ai-translation-text` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`379de29cdee61e59a7ea9beec64aefd03216ec35`) and `references/non-hero-scenarios.md` (`8bc5844dd6aa1b4dee6da1074a8d8b2267d64510`).
- **Decisive authority/privacy failure:** Unapproved transfer of potentially private text to Azure and billable batch operations; no explicit data sensitivity, disclosure or budget gate; unpinned package install.
- **Static score:** 13/20; ten dimensions in rubric order: `1,2,0,1,1,2,1,2,1,2`. Prior registered-pin score: 13/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** EXTRACT language/dictionary patterns; ADAPT with user-approved data scope, provider/region disclosure and budget threshold.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

### 8. `azure-ai-vision-imageanalysis-py`

- **Purpose / differentiator:** Image caption/OCR/people/object detection and cost-aware feature selection with context-managed credentials.
- **Dependency / portability:** `pip install azure-ai-vision-imageanalysis` (unpinned), Azure SDK auth/core, authorized Azure endpoint and paid cloud service; medium portability. Two declared references inspected: `references/capabilities.md` (`b24da438beec64aefd03216ec35f8478e757472`) and `references/non-hero-scenarios.md` (`fe519431024080a6cfe80daaebf4b6459c81c53d`).
- **Decisive authority/privacy failure:** Unapproved upload or remote URL processing of potentially personal images; OCR outputs and people detections printed without privacy/retention gates; no cost authorization.
- **Static score:** 12/20; ten dimensions in rubric order: `1,2,0,1,1,2,1,2,0,2`. Prior registered-pin score: 12/20. A changed manifest is not presumed improved merely because it has new references or revised credential guidance.
- **User-fit / salvage:** EXTRACT feature-selection and OCR method; require image owner consent, external processing approval, output redaction and budget bounds.
- **State:** candidate `rejected-unchanged`; **no** source-pin advancement or unchanged admission. Pinned package-security **not-run**; behavioral/adversarial host execution **not-run**.

## Macro findings, omissions and remaining frontier

1. **Credential hygiene is not consent.** Even strong DefaultAzureCredential, environment-variable, and context-manager instructions do not authorize off-device processing of personal, confidential, regulated or billable workloads. This is the repeated hard fail across eight apparently polished official SDK procedures.
2. **Privacy and state effects hide in examples and references.** Unredacted PII/entity/transcript/OCR output, SAS-bearing URLs, remote blocklist/analyzer/job writes and deletes, and unapproved Azure analysis costs remain. A host must independently gate these actions and outputs, not infer permission from a method signature.
3. **Actual progress:** Eight of the **76 October 10 changed governed Microsoft package identities** now have individual candidate-version static rejection decisions. The remaining **68 of that frozen changed set** are not completed by this tranche; four removals and 22 raw additions still require decisive treatment. The latest October 27 candidate eligible denominator remains **unresolved** because the full latest recursive tree has not been obtained. The 106 October 10 carry-forwards cannot be silently generalized to the newer head.
4. **No inflation:** Current registered Microsoft pin stays 186/186, source count 22, third-party persisted review count 721, first-party count 44. The five public accounting surfaces need **no count adjustment** for candidate-only research. No current `registry/verification/microsoft-skills/` companions were overwritten.
5. **Discovery lane:** Three public surfaces were searched during this run (recent GitHub SKILL.md repositories, skills.sh directory coverage, and Hugging Face agent-skills coverage). Results surfaced already known collections, general tutorials and security commentary, but **no distinct newly qualified first-class candidate** was established from those searches. No issue or source registration was created from weak discovery evidence.

**Next action:** Obtain an **uncapped complete latest** upstream tree and re-partition the 186 governed identities, alias/nested exposures and new raw manifests. Continue a distinct high-authority changed-package tranche, with exact package scans only in an authorized external host. PRs #412/#413/#416 remain draft/blocked on complete security evidence and independent acceptance; this document does not change their readiness.

**Machine-readable evidence:** [eight individual candidate records](../registry/freshness/microsoft-skills-ai-python-candidate-2026-10-27.json). These are *pre-pin freshness review records*, not canonical admitted-source verification companions.
