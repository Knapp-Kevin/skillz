# Microsoft Rust SDK: eight changed-existing exact-version static reviews

**2026-10-28.** Upstream `microsoft/skills` candidate `61fe0305ea70389ed8705eec6026a786f57865cf`; registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. **Eight REJECT unchanged; zero admissions; security and behavioral validation not-run.**

## Macro-first denominator and identity

The full 76 changed-existing canonical frontier partitions into **37 azure-sdk-python, 30 azure-skills, 8 azure-sdk-rust and 1 skill-creator**. Previous 76/76 screening is not full requalification. The 26 new/previously ungoverned packages already have complete static reviews; 106 exact-tree carry-forwards retain prior evidence. Four removed paths have separate retirement decisions. The candidate structural denominator is **208 = 106 + 76 + 26**; registered July remains **186/186**. This tranche completes **8/76**, leaving **68** changed-existing full reviews.

All eight Rust candidates are distinct single-file first-class front-mattered packages. The candidate Git tree was traversed to verify each package tree SHA and each subtree contains only `SKILL.md`. All eight exact manifests were fetched and read in full, Git blob SHA matched prior screening evidence, and registered July provenance/verification was preserved. Upstream root MIT LICENSE blob `79656060de00aa4659ad2c276d5be8830664d544` agrees with manifest MIT terms. External crate and service terms, Rust compile/runtime behavior, and security were not independently validated.

## Individual decisions

| Package | Candidate tree SHA prefix | Score | Decisive unchanged-use defect |
|---|---|---:|---|
| `azure-cosmos-rust` | `ed1e2001dc9d` | 11/20 | Document create/replace/patch/delete lacks explicit account, database, container, item, recovery and cost authorization. |
| `azure-eventhub-rust` | `e7f76b175974` | 10/20 | Billable event sends and partition consumption lack destination, payload and owner approval. |
| `azure-identity-rust` | `2a047dcea30a` | 11/20 | Successful login and RBAC do not authorize fetching and printing Key Vault secrets. |
| `azure-keyvault-certificates-rust` | `0df025484a28` | 11/20 | Certificate creation, signing, property changes and deletion lack vault, certificate, owner and change-window approval. |
| `azure-keyvault-keys-rust` | `14b39462ab54` | 8/20 | Unapproved key lifecycle changes; a four-byte DEK from random::<u32>() is cryptographically unsuitable. |
| `azure-keyvault-secrets-rust` | `8549b0a1e53f` | 10/20 | Secret set/delete and disclosure lack vault, name and owner-specific approval. |
| `azure-storage-blob-rust` | `1d22a03690fb` | 11/20 | Blob/container mutations lack object, classification, retention and cost approval. |
| `azure-storage-queue-rust` | `a72fa4d7cea8` | 10/20 | Message sends/deletes lack queue/message approval and processing-completion gate. |

Each candidate has individual exact-version provenance and verification companions, complete one-file inventory, tree/blob identity, controlled tags, dependencies, purpose/nontrigger, rubric, authority/privacy finding, rationale, and explicit `not-run` security/behavioral states.

## Systemic synthesis

- **Authority:** 8/8 fail unchanged-use authorization for money-bearing writes, credential reads, cryptographic/identity operations, sensitive disclosure or destructive actions. RBAC and parameters are not action approval.
- **Privacy:** Event Hubs, queues, blobs and Key Vault examples print or transfer potentially private payloads, documents or secrets without recipient/retention boundaries.
- **Cryptographic hard fail:** `azure-keyvault-keys-rust` uses a four-byte `u32` data-encryption key with at most 32-bit entropy. Version-aware wrapping remains useful only after correcting key generation and authority.
- **Differentiated prior art:** official Rust crate names, managed versus developer credentials, partition keys, pagination, pop receipts, RBAC scoping, version-aware key operations and storage error handling.
- **Remaining 68:** 37 Python SDK, 30 Azure operations and 1 skill-creator changed-existing packages need full exact-version review. Earlier manifest/selected-reference screening is not complete-package qualification.

No Cargo commands, source-owned scripts, Azure operations, scanners or behavioral tests were executed. No repository-owned runtime, CI, scripts or scheduler was introduced. The registered pin, admissions and external acceptance/security gates remain unchanged. PRs #412/#413/#416 and issues #402/#415 retain independent blockers.
