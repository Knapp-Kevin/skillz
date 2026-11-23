"""Offline source/refusal tests. NOT PowerShell or Hyper-V execution.

The suite deliberately catches removal of safety preconditions using
synthetic source mutations. Windows host tests remain separately required.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
NEW = ROOT / "scripts" / "New-OfflineQualVm.ps1"
CONNECT = ROOT / "scripts" / "Connect-QualVm.ps1"
SKILL = ROOT / "SKILL.md"
CARD = ROOT / "examples" / "vm-card-template.md"
ACCEPT = ROOT / "examples" / "acceptance.md"


def source(path):
    return path.read_text(encoding="utf-8")


def required_features(creation, connection):
    """Return source-contract violations; does NOT execute these scripts."""
    problems = []
    required_new = [
        "#Requires -Modules Hyper-V",
        "SupportsShouldProcess = $true",
        "[switch] $Commit",
        "if (-not $Commit)",
        "if (-not $PSCmdlet.ShouldProcess(",
        "Get-VM -Name $Name",
        "if (Test-Path -LiteralPath $vmDir)",
        "New-VM -Name $Name -Generation 2 -NoVHD",
        "Get-VMNetworkAdapter -VMName $Name",
        "Remove-VMNetworkAdapter",
        "Assert-NoNetwork $Name",
        "New-VHD -Path $osVhd",
        "New-VHD -Path $dataVhd",
        "Add-VMHardDiskDrive",
        "Add-VMDvdDrive",
        "Set-VMFirmware -VMName $Name -EnableSecureBoot On -FirstBootDevice $dvd",
        "AutomaticCheckpointsEnabled:$false",
        "DynamicMemoryEnabled:$false",
        "AutomaticStartAction Nothing",
        "Enable-VMIntegrationService -VMName $Name -Name 'Guest Service Interface'",
        "partial files locally; no automatic cleanup",
    ]
    required_connect = [
        "#Requires -Modules Hyper-V",
        "Get-VMNetworkAdapter -VMName $Name",
        "Get-VMGpuPartitionAdapter -VMName $Name",
        "if ($hostAdapters.Count -gt 0)",
        "if ($gpuAdapters.Count -gt 0)",
        "Import-Clixml -LiteralPath",
        "if ($cred -isnot [System.Management.Automation.PSCredential])",
        "Invoke-Command -VMName $Name -Credential $cred",
        "Get-NetAdapter -IncludeHidden",
        "Where-Object { $_.Status -eq 'Up' }",
        "if ($guestUp.Count -gt 0)",
        "Enter-PSSession -VMName $Name -Credential $cred",
        "if ($OpenOwnerSession)",
        "if ($Console)",
        "vmconnect.exe localhost $Name",
        "Remove-Variable -Name cred",
        "No retry",
    ]
    for item in required_new:
        if item not in creation:
            problems.append("create lacks: " + item)
    for item in required_connect:
        if item.lower() not in connection.lower():
            problems.append("connect lacks: " + item)
    for unsafe in ("Add-VMNetworkAdapter", "Connect-VMNetworkAdapter",
                   "Start-VM ", "Remove-VM ", "Stop-VM ",
                   "Set-VMGpuPartitionAdapter", "Remove-VMGpuPartitionAdapter"):
        if unsafe.lower() in creation.lower() or unsafe.lower() in connection.lower():
            problems.append("unsafe operation in script: " + unsafe)
    if "Invoke-Expression" in creation or "Invoke-Expression" in connection:
        problems.append("unsafe expression execution")
    plan = creation.find("if (-not $Commit)")
    mutate = creation.find("New-VM -Name $Name")
    if plan < 0 or mutate < 0 or plan > mutate:
        problems.append("create operation before explicit commit")
    network = connection.find("Get-VMNetworkAdapter -VMName $Name")
    credential = connection.find("Import-Clixml")
    guest = connection.find("Invoke-Command -VMName $Name")
    if network < 0 or credential < 0 or guest < 0 or not (network < credential < guest):
        problems.append("connection attempts credential before isolation")
    if connection.count("Invoke-Command -VMName $Name") != 1:
        problems.append("repeated guest check")
    return problems


class OfflineContract(unittest.TestCase):
    def test_complete_contract_current_source(self):
        self.assertEqual(required_features(source(NEW), source(CONNECT)), [])

    def test_create_only_after_explicit_commit(self):
        self.assertLess(source(NEW).index("if (-not $Commit)"),
                        source(NEW).index("New-VM -Name $Name"))

    def test_creation_does_not_start_vm_or_attach_network(self):
        s = source(NEW)
        self.assertIn("New-VM -Name $Name -Generation 2 -NoVHD", s)
        self.assertNotIn("Add-VMNetworkAdapter", s)
        self.assertNotIn("Start-VM ", s)

    def test_no_password_prompt_or_private_path_written_by_creator(self):
        s = source(NEW)
        for forbidden in ("Get-Credential", "Export-Clixml",
                          "Set-LocalUser", "New-LocalUser", "net user"):
            self.assertNotIn(forbidden, s)

    def test_host_nic_zero_enforced_before_guest_execution(self):
        s = source(CONNECT)
        self.assertLess(s.index("Get-VMNetworkAdapter -VMName $Name"),
                        s.index("Import-Clixml"))
        self.assertLess(s.index("Get-VMGpuPartitionAdapter -VMName $Name"),
                        s.index("Import-Clixml"))

    def test_no_retry_loop_on_direct_credential(self):
        s = source(CONNECT)
        self.assertEqual(s.count("Invoke-Command -VMName $Name"), 1)
        self.assertNotIn("Get-Credential", s)

    def test_private_credential_not_redisplayed(self):
        s = source(CONNECT)
        for forbidden in ("Write-Host $cred", "Write-Output $cred",
                          "ConvertFrom-SecureString", "$cred.Password",
                          "Export-Clixml", "ConvertTo-Json $cred"):
            self.assertNotIn(forbidden, s)

    def test_no_vm_deletion_automatic_recovery(self):
        s = source(NEW) + source(CONNECT)
        self.assertNotRegex(s, r"(?m)^\s*(?:Remove-VM|Remove-Item|Stop-VM)\s")

    def test_guest_status_is_read_only(self):
        s = source(CONNECT)
        self.assertIn("Get-NetAdapter -IncludeHidden", s)
        self.assertNotIn("Disable-NetAdapter", s)
        self.assertNotIn("Enable-NetAdapter", s)

    def test_owner_interactive_session_opt_in_only(self):
        s = source(CONNECT)
        self.assertLess(s.index("if ($OpenOwnerSession)"), s.index("Enter-PSSession"))
        self.assertIn("vmconnect.exe localhost $Name", s)

    def test_creation_has_bounded_disks_and_memory(self):
        s = source(NEW)
        self.assertGreaterEqual(s.count("[ValidateRange("), 3)
        self.assertIn("New-VHD -Path $osVhd", s)
        self.assertIn("New-VHD -Path $dataVhd", s)

    def test_error_does_not_echo_guest_exception(self):
        s = source(CONNECT)
        self.assertNotIn("Write-Error $_", s)
        self.assertIn("HOLD: exactly one private PowerShell Direct check failed", s)

    def test_postcreation_network_recheck(self):
        self.assertGreaterEqual(source(NEW).count("Assert-NoNetwork $Name"), 2)

    def test_gpu_partition_is_inspected_not_modified(self):
        s = source(CONNECT)
        self.assertIn("Get-VMGpuPartitionAdapter", s)
        self.assertNotIn("Remove-VMGpuPartitionAdapter", s)

    def test_skill_explicit_anti_secret_boundary(self):
        s = source(SKILL).lower()
        for word in ("password", "private", "no retry",
                     "explicit owner", "offline", "not_run"):
            self.assertIn(word, s)

    def test_credential_card_has_no_actual_password(self):
        s = source(CARD)
        self.assertIn("NOT PASSWORD", s)
        self.assertIn("DO NOT COMMIT", s)
        self.assertNotIn("example@example", s)

    def test_fixture_is_labeled_synthetic(self):
        self.assertIn("NOT Windows test executions", source(ACCEPT))

    def test_supporting_files_exist(self):
        for p in (NEW, CONNECT, CARD, ACCEPT, ROOT / "LICENSE"):
            self.assertTrue(p.is_file(), str(p))

    def test_missing_shouldprocess_is_detected(self):
        mutated = source(NEW).replace("SupportsShouldProcess = $true", "SupportsShouldProcess = $false")
        self.assertTrue(required_features(mutated, source(CONNECT)))

    def test_missing_commit_gate_is_detected(self):
        mutated = source(NEW).replace("if (-not $Commit)", "if ($Commit)")
        self.assertTrue(required_features(mutated, source(CONNECT)))

    def test_missing_adapter_guard_is_detected(self):
        mutated = source(CONNECT).replace("if ($hostAdapters.Count -gt 0)", "if ($false)")
        self.assertTrue(required_features(source(NEW), mutated))

    def test_missing_guest_up_probe_is_detected(self):
        mutated = source(CONNECT).replace("if ($guestUp.Count -gt 0)", "if ($false)")
        self.assertTrue(required_features(source(NEW), mutated))

    def test_missing_gpu_guard_is_detected(self):
        mutated = source(CONNECT).replace("if ($gpuAdapters.Count -gt 0)", "if ($false)")
        self.assertTrue(required_features(source(NEW), mutated))

    def test_injected_network_attachment_is_detected(self):
        mutated = source(NEW) + "\nAdd-VMNetworkAdapter -VMName bad\n"
        self.assertTrue(required_features(mutated, source(CONNECT)))

    def test_injected_start_is_detected(self):
        mutated = source(NEW) + "\nStart-VM -Name bad\n"
        self.assertTrue(required_features(mutated, source(CONNECT)))

    def test_injected_guest_command_retry_is_detected(self):
        mutated = source(CONNECT) + "\n# Invoke-Command -VMName $Name -Credential $cred\n"
        self.assertTrue(required_features(source(NEW), mutated))

    def test_missing_secure_boot_detected(self):
        mutated = source(NEW).replace("EnableSecureBoot On", "EnableSecureBoot Off")
        self.assertTrue(required_features(mutated, source(CONNECT)))

    def test_missing_auto_checkpoint_disable_detected(self):
        mutated = source(NEW).replace("AutomaticCheckpointsEnabled:$false", "AutomaticCheckpointsEnabled:$true")
        self.assertTrue(required_features(mutated, source(CONNECT)))

    def test_deleted_guest_refusal_detected(self):
        mutated = source(CONNECT).replace("if ($guestUp.Count -gt 0)", "if ($false)")
        self.assertTrue(required_features(source(NEW), mutated))


if __name__ == "__main__":
    unittest.main(verbosity=2)
