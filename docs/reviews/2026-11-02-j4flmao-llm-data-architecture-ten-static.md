# Pinned j4flmao LLM, data and architecture qualification (2026-11-02)

**Source:** [j4flmao/agent-skills](https://github.com/j4flmao/agent-skills/tree/982203e52afe0b726a7847599a8bfb293890e0c5) at `982203e52afe0b726a7847599a8bfb293890e0c5`. This is dynamic discovery, **not admitted**. Root MIT notice blob `0e8b6e6d8678128ebfcc28d7cad91fa9ed7f2354` applies to the source's own content, not separately licensed models, dependencies or datasets. [Ten individual 10-dimension records](../../registry/discovery/j4flmao-llm-data-architecture-ten-static-20261102.json).

## Macro frontier and dispositions

At the preceding checkpoint: **51/645** exact-path candidate decisions (20/424 direct, 31/221 other). This tranche inspects ten complete packages, including their pinned SKILL.md files and both bundled multi-agent references. All are independently front-mattered. Nine package trees contain one SKILL.md, one contains three package-owned Markdown files. **7 other-shape + 3 direct-shape** become **61/645** (23 direct, 38 other), leaving **584 raw** (401 direct, 183 other). Across four dynamic sources: **138 → 148/4,813 raw paths**. These are overlapping path populations, **not a deduplicated eligible-skill denominator**.

| Pinned package | Grade | Disposition | Decisive static finding |
|---|---:|---|---|
| `skills/ai/llm-engineering/kv-cache/SKILL.md` | 16/20 | REFERENCE-ONLY | Useful GQA-aware cache sizing, vLLM flags and evaluation checks, but sample launch and GPU allocation are not scoped to an authorized host, and V1/default assumptions require version verification. |
| `skills/ai/llm-engineering/model-quantization/SKILL.md` | 14/20 | REJECT | Concrete model conversion downloads datasets/models and writes persistent quantized weights without an action-specific authorization or dataset/model-rights gate; the suggested GGUF imatrix command assumes an optional file exists. Preserve method comparison and evaluation checklist. |
| `skills/ai/llm-engineering/rag-architecture/SKILL.md` | 11/20 | REJECT | Useful ANN/RRF concepts, but cross-encoder reranking sends retrieved private passages without an egress boundary; sample IVF training samples 200,000 vectors without guarding smaller corpora; repository-specific CI and chunking rules are not portable. |
| `skills/architecture/databases/postgresql-internals/SKILL.md` | 14/20 | REJECT | Read-only diagnostic queries are useful, but ALTER TABLE/autovacuum and performance changes appear as direct fixes without separate production target, lock, rollback and change-window authorization. Query excerpts can expose sensitive SQL. |
| `skills/architecture/databases/scaling-and-sharding/SKILL.md` | 14/20 | REJECT | Good vertical-before-sharding and bucket-routing advice, but executable CREATE TABLE/Citus distribution and resharding deletion steps lack action-specific database, traffic and destructive-state approval. Hash-ring sample has no explicit duplicate-node safeguards. |
| `skills/architecture/system-design/domain-driven-design/SKILL.md` | 18/20 | REFERENCE-ONLY | Strong bounded-context, aggregate and outbox modeling reference; TypeScript example is illustrative, not a complete transactional implementation, and event publishing/ERP mapping need data ownership and PII checks before use. |
| `skills/architecture/system-design/microservices-patterns/SKILL.md` | 13/20 | REJECT | The sample saga includes charge_payment and refund compensation with no payment-action authorization boundary; generic idempotency and logging do not confer consent. Compensation failures are not safely handled and exception logs can leak data. |
| `skills/ai/genai-vision/SKILL.md` | 11/20 | REJECT | Image code persists full prompts and generated files to disk without a scoped privacy/retention authorization; audio transcription and speech-to-image flow lack subject/voice-data consent and storage boundary. Model-card license checks are advisory only. |
| `skills/ai/llm-finetuning/SKILL.md` | 13/20 | REJECT | Training recipe writes adapter checkpoints and may ingest private licensed datasets without an action-specific training/compute and retention gate; data-cleaning advice is not authorization to use user documents or pay for GPU resources. |
| `skills/ai/multi-agent-systems/SKILL.md` | 12/20 | REJECT | LangGraph sample can resume a production deploy after state approval flag update without verifying actor, exact target, expiry or revision inside deploy_node; notification and durable checkpoints retain sensitive state by default. HITL reference is conceptual, not authorization. |

## Systemic findings

- Seven nested other-shape paths are independent front-mattered packages with their own exact tree/blob identity; three direct-shape AI packages are also distinct. Nine packages have only SKILL.md, while multi-agent-systems owns two references read in full.
- Hard fails cluster around production DDL and resharding, money-bearing saga compensation, persistent training/image artifacts, private RAG reranker egress, and multi-agent deploy approvals. Generic checks, flags, and HITL interrupts are not action-specific authorization.
- Strong prior art includes KV memory math, quantization evaluation gates, ANN+RRF retrieval, MVCC/WAL diagnostics, logical shard buckets, DDD invariants, and explicit orchestration state. Extract with authority/privacy repairs; no unchanged-use approval.
- The directory has no dedicated AI/ML training and model-serving domain. Nearest-fit subdomain placement is explicit and does not certify full coverage; do not invent a new domain solely to satisfy a tranche.
- No cross-source semantic equivalence established. Candidate 0-20 scores are not governed exact-version semantic review pairs, security qualification, or behavioral validation.

## Scope, rights and evidence

All ten pinned skill blobs, containing package-tree hashes, source identity, license, required dependencies, authority/privacy boundaries, trigger/non-trigger descriptions, individual dimension scores, exact rationale, and behavioral state are in the linked JSON. The multi-agent references were individually read and are **not separate SKILL.md identities**. No upstream package was copied into this repository. All security scans and representative behavioral tests are **not-run**; no governed review pair, admission or installed skill was created. A REFERENCE-ONLY decision preserves method value without unchanged-use approval. Rejected packages remain as negative/adaptation evidence, not deleted.

**Next frontier:** j4flmao other-shape `skills/backend/deno/oak/SKILL.md`; direct-shape cursor recomputed from pinned manifests and existing exact-path decisions. Review a coherent bounded tranche after reconciling any concurrent writer and source/license changes.
