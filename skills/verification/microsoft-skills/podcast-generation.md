# Verification: Microsoft Skills `podcast-generation`

- Source family: `microsoft-skills`
- Canonical path: `.github/skills/podcast-generation`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `a1aeeb2e902d732035066ed9f7be20cf120ce53c`
- `SKILL.md` blob: `7f2e72053b725adf289d5438138ddcee55e47012`
- Static disposition: **rejected unchanged**
- Score: **13/20**
- Behavioral validation: **not-run**
- Controlled tags: `implementation`, `cloud`, `communication`, `tool-assisted`, `production-oriented`, `mutating`, `external-side-effect`

## Structured semantic review

### Useful material to preserve

The package gives a coherent end-to-end reference for Azure OpenAI Realtime audio generation: WebSocket endpoint construction, streaming audio/transcript event handling, PCM-to-WAV conversion, browser playback, and a concrete FastAPI/React integration shape. The bundled conversion helper is small and deterministic, and the references make the data flow and persistence model easy to inspect.

Preserve the Realtime event loop, explicit audio-format assumptions, deterministic PCM/WAV conversion, separation between backend generation and frontend playback, and the general full-stack integration pattern as adaptation/reference evidence.

### Authority and sensitive-data hard fail

Unchanged adoption fails the current authority standard. The procedure tells the host to send arbitrary source content, including bookmark/tag/application content, to an external Azure OpenAI Realtime service without a mandatory disclosure-authorization and minimization checkpoint immediately before transmission. The reference implementation also writes generated transcripts and base64 audio into persistent database state without a mandatory action-specific authorization boundary before that mutation.

The environment example uses a placeholder API key rather than a literal credential, which is good, but the package does not state that real credentials must remain in secure external configuration and must not be pasted into conversational context. A safe adaptation should use identity-based or secure secret injection where available, minimize content before external transmission, require explicit authority for private/sensitive source disclosure, and separately authorize persistence of generated audio/transcripts.

### Trigger and non-trigger boundary

Use the mechanisms when implementing text-to-audio or narrated-content features against an already authorized Realtime deployment. Do not use unchanged for private-document narration, user-message/audio processing, persistent storage of generated media, or other sensitive-content workflows unless disclosure and persistence authority are explicitly established. Do not treat the example database schema or API layout as a required architecture.

## Portability

Medium. The PCM/WAV and event-handling concepts are portable, but the package is specifically shaped around Azure OpenAI Realtime, Python/FastAPI, React, WebSockets, and a database-backed application. The useful mechanisms extract cleanly even though unchanged operational adoption does not.

## Validation note

This review inspected the exact registered-pin four-file package but did not call Azure OpenAI, transmit content, write database records, or run the bundled script. No representative external behavioral or adversarial evidence was produced, so behavioral validation remains `not-run`.
