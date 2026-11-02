# asset-pipeline 2.0.0: complete pinned package static review

Source: j4flmao/agent-skills at 982203e52afe0b726a7847599a8bfb293890e0c5. Path: skills/game/game-engine/asset-pipeline/SKILL.md. Blob: 476bb7f2f40f1e4f43f0f4dd01c683e90cf66fd5. Package tree: b2f29cf45e43030504185bdff3b5be26a90ef2bf. MIT declared in skill frontmatter; external tools and dependency licenses remain separate.

Inspected SKILL.md and six bundled reference files: import-and-cook abc1620; asset-registry 2616c9f; hot-reload e846383; packing ea4325b; shader-pipeline ed574c2; streaming-throttle.

Trigger: asset-pipeline design and code guidance in a game engine. Nontrigger: authorization to modify deployed engines, publish packages, import untrusted data, or transmit private traces.

**Terminal source-vetting decision: REJECT unchanged.** AssetRegistry::Unload frees an asset on refcount zero without guaranteeing asynchronous reads, decode, GPU uploads, and in-flight GPU consumers have completed. Hot-reload retires GPU assets after a fixed frame count rather than confirmed completion. Packing treats CRC32 as an integrity gate for potentially untrusted mod packs, although CRC is not authenticity verification. No bounded decompression or archive path traversal controls are specified. Preserve deterministic cooking, content-addressed dependency closure and staged publishing, but require lifetime leases, authenticated provenance where relevant, bounded parsing and fence-gated reclamation.

Authority/privacy: require user approval before modifying asset storage, collecting diagnostics, publishing archives or exporting gameplay data. Treat imported and modded assets as untrusted inputs. No external tools were run.

Static complete-package inspection only. Behavioral validation NOT RUN; security scanning NOT RUN; numerical 20-point grade NOT ASSIGNED; governed semantic review NOT CREATED. No public count or denominator change until reconciliation.
