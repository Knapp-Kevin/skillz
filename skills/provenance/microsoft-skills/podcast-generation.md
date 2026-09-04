# Provenance: Microsoft Skills `podcast-generation`

- Source family: `microsoft-skills`
- Canonical source: `microsoft/skills`
- Canonical path: `.github/skills/podcast-generation`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `a1aeeb2e902d732035066ed9f7be20cf120ce53c`
- `SKILL.md` blob: `7f2e72053b725adf289d5438138ddcee55e47012`
- Package contents: 4 files: `SKILL.md`, `references/architecture.md`, `references/code-examples.md`, and `scripts/pcm_to_wav.py`.
- Bundled reference identities: `references/architecture.md` blob `28e572aa1bc1b7189efdfe88fc5c8ee963c09494`; `references/code-examples.md` blob `18bbdc306505cdb9a9afe1deec121d3da8ab45e4`.
- Bundled script identity: `scripts/pcm_to_wav.py` blob `6f296aa89974d462d7def65daba5b91915947ec2`.
- Skill-path freshness evidence: `a2003b6b95ead129e53dd5377a2229682ff75b1b` (2026-01-28), the latest commit returned for `podcast-generation` that materially standardized the skill before the registered pin.
- License/terms: MIT, inherited from the registered Microsoft Skills source repository.

## Purpose and source context

`podcast-generation` is a full-stack implementation reference for turning text or application content into narrated audio with Azure OpenAI Realtime API. It covers prompt construction, WebSocket streaming, PCM-to-WAV conversion, transcript collection, browser playback, and a reference persistence/API shape using React, FastAPI, and a database-backed `AudioNarrative` model.

The package is preserved intact at the registered pin as third-party reference evidence. Its bundled Python conversion script and code examples are upstream package material, not repository-owned runtime.

## Dependencies and authority profile

The package assumes an Azure OpenAI Realtime deployment, an API endpoint and API key supplied through environment configuration, the OpenAI Python client, a Python/FastAPI backend, a React frontend, and database access for the full reference architecture. The local PCM-to-WAV conversion helper is deterministic and does not itself require external access.

The generation workflow sends source content to an external Azure OpenAI service and the reference implementation persists generated transcript/audio data to a database. Those operations can disclose private document/bookmark/application content and mutate persistent state. Unchanged use therefore requires explicit disclosure authority, data minimization, and action-specific authorization appropriate to the external generation and persistence actions. Credentials should remain in secure external configuration and must not be solicited or echoed into conversational context.
