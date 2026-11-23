# Synthetic acceptance and negative controls

**These are proposed host-test scenarios, not Windows test executions.**
The offline unit suite checks source-level invariants on the PowerShell
scripts. Operational acceptance requires an owner-authorized Windows
Hyper-V host using throwaway fictional names, no credentials logged and
a separate controlled VM as applicable.

| Case | Input/state | Required result |
| --- | --- | --- |
| First planning call | New name, approved ISO, existing storage root, no -Commit | PREFLIGHT_ONLY_NOT_CREATED; no VM or files created |
| Existing name | VM already exists at target name | HOLD before any mutation |
| Existing directory | New name but destination already exists | HOLD without overwrite |
| Missing or redirected ISO | Missing file, symbolic link, or wrong extension | HOLD before mutation |
| Successful approved shell | Owner-authorized commit and confirmed prompt | Gen 2, static memory, dynamic VHDX, DVD-first, zero NIC, auto checkpoints disabled, GSI enabled |
| Unexpected host adapter | Host has a NIC at connect time | HOLD *before* importing credential |
| GPU partition adapter | GPU partition present even after checkpoint restore | HOLD; never automatic removal |
| Missing credential file | User/owner has not enrolled private DPAPI | HOLD; do not ask for password |
| Credential from another user | Import-Clixml cannot decrypt or returns wrong type | HOLD after one attempt, no retry |
| Guest network Up | Get-NetAdapter reports Up | HOLD, do not open interactive session |
| Guest check fails | PowerShell Direct unavailable, OS not ready or guest command errors | HOLD without retry or credential print |
| Console access | Explicit owner console mode after zero NIC/GPU check | VMConnect only, manual password, no credential injection |
| Checkpoint reboot | Revert happened; adapters reappear at host | HOLD before further qualification |
| False-green suite | VM booted, no native tests executed | NOT_QUALIFIED |
| Partial disk creation | Failed provisioning midway | HOLD partial VM; no delete, overwrite or retry |
| Evaluation shutdown | Guest expires mid-run | Incomplete/failed tests, no license bypass |
| Delete request | Owner does not verify VM identity/size | No deletion authorized |
| Owner-approved retirement | Identity and disk impacts verified, evidence exported | Explicit, separately authorized Remove-VM and owned-folder removal only |

**Source-only coverage:** Tests in tests/test_source.py assert the invariants
are represented, reject selected unsafe edits, and inspect simulated
source-configuration facts. They cannot establish PowerShell syntax/runtime
or actual Hyper-V behavior on a Windows host. Host stages remain NOT_RUN.

## Synthetic PowerShell test lane (no Windows guest)

The Windows CI job uses the fake Hyper-V module in
[tests/fake/Hyper-V/Hyper-V.psm1](../tests/fake/Hyper-V/Hyper-V.psm1)
and invokes the original scripts through
[tests/test_synthetic_host.ps1](../tests/test_synthetic_host.ps1).
The harness explicitly validates its module binding before any script runs;
all hypervisor mutators are blocked. Its local files and fictional
credential stand-ins are ephemeral, not owner private data.

Passing this lane demonstrates selected *PowerShell source execution against
mocked host responses*, not live PowerShell Direct, actual credential
decryption, hardware isolation, a hypervisor, a valid Windows guest, a
checkpoint or a native test. Do not describe this as actual host acceptance.
