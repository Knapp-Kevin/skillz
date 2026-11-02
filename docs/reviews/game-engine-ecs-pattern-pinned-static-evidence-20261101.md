# ecs-pattern 2.0.0: complete pinned package static review

Source: j4flmao/agent-skills at 982203e52afe0b726a7847599a8bfb293890e0c5. Path: skills/game/game-engine/ecs-pattern/SKILL.md. Blob: ad5163695819ca68c1af519e2469345226e4e4a6. Package tree: 0604d31dbdb21aff02c79322105a03ef3a3bf8fc. MIT declared in skill frontmatter; external tools and dependency licenses remain separate.

Inspected SKILL.md and six bundled reference files: archetype-storage-deep-dive; system-scheduling-pipelines; unity-dots-in-practice; bevy-ecs-patterns; entt-and-flecs 8cf92b3; ecs-netcode a8849b9.

Trigger: ecs-pattern design and code guidance in a game engine. Nontrigger: authorization to modify deployed engines, publish packages, import untrusted data, or transmit private traces.

**Terminal source-vetting decision: REJECT unchanged.** The main sparse-set removal example indexes entities[idx] after popping the last element, which is out of bounds when removing the last item. It omits capacity and presence checks. The example World::spawn assumes archetypes[0] exists although the vector starts empty. The generation counter example increments the stored generation but returns the previous generation, so its newly created entity fails its own isValid check. The EnTT reference contains an undefined identifier enny instead of enemy. Bevy examples combine APIs from incompatible versions and require version pinning. Preserve read/write-set scheduling, deferred structural mutations, generational IDs and benchmark-first adoption after correcting code and version drift.

Authority/privacy: require user approval before modifying asset storage, collecting diagnostics, publishing archives or exporting gameplay data. Treat imported and modded assets as untrusted inputs. No external tools were run.

Static complete-package inspection only. Behavioral validation NOT RUN; security scanning NOT RUN; numerical 20-point grade NOT ASSIGNED; governed semantic review NOT CREATED. No public count or denominator change until reconciliation.
