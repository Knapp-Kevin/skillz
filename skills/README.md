# Local Skill Library

This directory contains the locally maintained and directly imported portion of the `skillz` library.

## Browse by purpose

Start with [`categories/`](categories/) if you are browsing as a human.

- [Planning & Productivity](categories/planning-productivity/)
- [Writing & Communication](categories/writing-communication/)
- [Research & Analysis](categories/research-analysis/)
- [Software & Repositories](categories/software-repositories/)
- [Agent Operations & Security](categories/agent-operations-security/)
- [Monitoring & Intelligence](categories/monitoring-intelligence/)
- [Business & Career](categories/business-career/)

The category folders are currently a human navigation layer. Canonical skill directories remain directly under `skills/` while recursive discovery is integrated into index, audit, and synchronization tooling. Once that migration is verified, the category layout can become the canonical physical organization without breaking existing installs or links.

## Counting rule

**Every user-facing skill under `skills/` counts, but `skills/` is not the entire library.**

The complete usable library also includes approved indexed third-party skill references from pinned source corpora under [`vendor/`](../vendor/). Repository machinery under [`engine/skills/`](../engine/skills/) is the exception and does not count.

When someone asks how many skills the repository has, report the indexed user-facing corpus, not merely the number of directories here.

## What belongs here

A capability belongs here when it makes sense for a user to install or use independently of maintaining `skillz`, even if the repository also happens to use it internally.

Third-party skills directly imported here must preserve applicable licensing and provenance under [`../registry/skills/`](../registry/skills/).

## Availability is not verification

Pinned vendor sources are part of the larger library corpus, but their individual skills do not inherit quality merely from repository inclusion.

The useful distinctions are:

- **local/imported**: maintained directly under `skills/`;
- **indexed reference**: available through approved sources under `vendor/`;
- **characterized**: has source provenance plus controlled tags/fingerprint;
- **trusted-baseline**: exact characterized version is eligible under repository quality policy;
- **verified**: structured skill-quality rubric passed;
- **validated**: representative behavioral evidence also passed;
- **unverified**: available/design evidence, not trusted unchanged by default;
- **stale**: prior characterization no longer matches the current skill content;
- **engine**: repository machinery under `engine/skills/`, excluded from library counts.

See [`../docs/skill-verification.md`](../docs/skill-verification.md) and [`../registry/verification/README.md`](../registry/verification/README.md).
