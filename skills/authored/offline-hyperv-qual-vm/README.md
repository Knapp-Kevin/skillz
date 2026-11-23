# Offline Hyper-V Qualification VM

A standalone first-party MIT skill for an **owner-controlled, air-gapped
Windows qualification guest**, not a generic networked VM template.

- **New-OfflineQualVm.ps1**: read-only plan by default; explicit commit and
  PowerShell confirmation before creating a new Gen 2 shell, dynamic VHDX
  disks, approved DVD media and no network adapter.
- **Connect-QualVm.ps1**: refuses host networking/GPU partition devices, imports
  only an owner-created same-user Windows DPAPI credential, performs one
  PowerShell Direct guest check and refuses guest adapters reporting Up.
  Owner console mode never inserts a password.
- **VM card template**: private, reproducible stage, checkpoint, OS-license,
  credential-location and evidence lineage without secrets in the repository.
- **Adversarial source tests**: deterministic static mutation assertions
  that run without Windows, PowerShell, Hyper-V, VM provisioning or credentials.
- **Synthetic PowerShell harness**: a separate Windows CI job runs the real
  entrypoint scripts against an intentionally fake Hyper-V module. All VM
  mutation functions are stubs that throw. This tests selected preflight,
  network, GPU, missing-credential, single-attempt and guest-Up refusal
  paths without creating a VM, using a real password or touching a hypervisor.

**Important:** A fake Hyper-V module is **not** a working Windows
hypervisor. Static plus synthetic PowerShell checks do NOT test actual VM
creation, guest login, owner-specific DPAPI decryption, checkpoint restore,
native build, file copy or retirement. Actual Windows-host qualification,
source/behavior review and owner approval are required before operational use.

    python3 -B -m unittest discover -s tests -p 'test_*.py' -v

On Windows, separately, the fake-module harness runs with Windows
PowerShell 5.1 and MUST NOT be replaced by the real Hyper-V module:

    powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File tests/test_synthetic_host.ps1

Consult [the complete skill](SKILL.md), [fictional VM card](examples/vm-card-template.md)
and [acceptance scenarios](examples/acceptance.md).

Official factual API references (no source expression copied):
[New-VM](https://learn.microsoft.com/powershell/module/hyper-v/new-vm),
[Set-VMFirmware](https://learn.microsoft.com/powershell/module/hyper-v/set-vmfirmware),
[Integration Services](https://learn.microsoft.com/windows-server/virtualization/hyper-v/manage/manage-hyper-v-integration-services),
[PowerShell Direct](https://learn.microsoft.com/windows-server/virtualization/hyper-v/powershell-direct),
[Windows DPAPI Export-Clixml](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/export-clixml).
