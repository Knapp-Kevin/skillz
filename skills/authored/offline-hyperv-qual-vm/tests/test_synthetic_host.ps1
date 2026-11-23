#Requires -Version 5.1
# Synthetic PowerShell execution: entrypoint scripts run against fake module only.
# No actual Hyper-V VM, Windows guest, DPAPI user secret or owner path accessed.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$package = Split-Path -Parent $here
$moduleRoot = Join-Path $here 'fake'
$moduleFile = Join-Path $moduleRoot 'Hyper-V\Hyper-V.psm1'
$env:PSModulePath = $moduleRoot + [IO.Path]::PathSeparator + $env:PSModulePath
Import-Module -Name $moduleFile -Force -ErrorAction Stop
if ((Get-Module Hyper-V).Path -ne $moduleFile) {
    throw 'HOLD: synthetic module was not imported; refuse to test against native Hyper-V'
}
foreach ($command in @('Get-VM','Get-VMNetworkAdapter','Get-VMGpuPartitionAdapter','New-VM','Import-Clixml','Invoke-Command','Get-PSDrive')) {
    $resolved = Get-Command $command -ErrorAction Stop
    if ($resolved.CommandType -ne 'Function' -or $resolved.ModuleName -ne 'Hyper-V') {
        throw ('HOLD: command not bound to synthetic Hyper-V: ' + $command)
    }
}
$create = Join-Path $package 'scripts\New-OfflineQualVm.ps1'
$connect = Join-Path $package 'scripts\Connect-QualVm.ps1'
$passed = 0
function Check([bool]$condition, [string]$message) {
    if (-not $condition) { throw ('SYNTHETIC_TEST_FAILURE: ' + $message) }
}
function Assert-Hold([scriptblock]$action, [string]$pattern) {
    $threw = $false
    try { & $action | Out-Null }
    catch {
        $threw = $true
        if ($_.Exception.Message -notmatch $pattern) {
            throw ('Unexpected refusal class; expected ' + $pattern)
        }
    }
    if (-not $threw) { throw 'Expected HOLD did not occur' }
}
function Reset-Fake {
    $global:QualVmFake.Exists = $false
    $global:QualVmFake.VmState = 'Running'
    $global:QualVmFake.HostNic = $false
    $global:QualVmFake.GpuPartition = $false
    $global:QualVmFake.GuestNicUp = $false
    $global:QualVmFake.ImportCalls = 0
    $global:QualVmFake.DirectCalls = 0
    $global:QualVmFake.MutationCalls = 0
    $global:QualVmFake.EnterCalls = 0
}
$root = Join-Path $env:TEMP ('fictional-hyperv-' + [guid]::NewGuid().ToString('N'))
# Only temporary fictional fixture files are touched; no virtual disks or credentials.
New-Item -ItemType Directory -Path $root -ErrorAction Stop | Out-Null
$iso = Join-Path $root 'synthetic.iso'
Set-Content -LiteralPath $iso -Value 'not-a-real-operating-system' -Encoding Ascii
$credential = Join-Path $root 'synthetic.xml'
Set-Content -LiteralPath $credential -Value 'fake-document-no-real-secret' -Encoding Ascii
$validName = 'fictional-qual-vm'
try {
    Reset-Fake
    $plan = & $create -Name $validName -StorageRoot $root -IsoPath $iso
    Check ($plan.Status -eq 'PREFLIGHT_ONLY_NOT_CREATED') 'preflight status'
    Check (-not (Test-Path -LiteralPath (Join-Path $root $validName))) 'preflight must not create destination'
    Check ($global:QualVmFake.MutationCalls -eq 0) 'preflight must never call mutators'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    Assert-Hold { & $create -Name $validName -StorageRoot $root -IsoPath $iso } 'already exists'
    Check ($global:QualVmFake.MutationCalls -eq 0) 'existing VM must hold before changes'
    $passed++

    Reset-Fake
    $existing = Join-Path $root $validName
    New-Item -ItemType Directory -Path $existing | Out-Null
    Assert-Hold { & $create -Name $validName -StorageRoot $root -IsoPath $iso } 'destination already exists'
    Check ($global:QualVmFake.MutationCalls -eq 0) 'existing folder must not be overwritten'
    Remove-Item -LiteralPath $existing -ErrorAction Stop
    $passed++

    Reset-Fake
    Assert-Hold { & $create -Name $validName -StorageRoot 'Z:\fictional-private-vm' -IsoPath $iso } 'network-backed'
    Check ($global:QualVmFake.MutationCalls -eq 0) 'mapped VM root must hold'
    $passed++

    Reset-Fake
    # WhatIf/ShouldProcess prevents all operations, even with a commit switch.
    $null = & $create -Name $validName -StorageRoot $root -IsoPath $iso -Commit -WhatIf
    Check ($global:QualVmFake.MutationCalls -eq 0) 'WhatIf must never call mutators'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    $global:QualVmFake.HostNic = $true
    Assert-Hold { & $connect -Name $validName -CredentialPath $credential } 'host-side VM adapter present'
    Check ($global:QualVmFake.ImportCalls -eq 0) 'host NIC check must precede credential'
    Check ($global:QualVmFake.DirectCalls -eq 0) 'host NIC check must precede direct connection'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    $global:QualVmFake.GpuPartition = $true
    Assert-Hold { & $connect -Name $validName -CredentialPath $credential } 'GPU partition adapter present'
    Check ($global:QualVmFake.ImportCalls -eq 0) 'GPU check must precede credential'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    Assert-Hold { & $connect -Name $validName -CredentialPath (Join-Path $root 'missing-credential.xml') } 'exactly one private PowerShell Direct check failed'
    Check ($global:QualVmFake.ImportCalls -eq 0) 'missing file must never call importer'
    Check ($global:QualVmFake.DirectCalls -eq 0) 'missing credential must never attempt auth'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    Assert-Hold { & $connect -Name $validName -CredentialPath 'Z:\fictional.xml' } 'exactly one private PowerShell Direct check failed'
    Check ($global:QualVmFake.ImportCalls -eq 0) 'network-backed credential must hold'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    $global:QualVmFake.GuestNicUp = $true
    Assert-Hold { & $connect -Name $validName -CredentialPath $credential } 'exactly one private PowerShell Direct check failed'
    Check ($global:QualVmFake.ImportCalls -eq 1) 'guest check imports fictional credential exactly once'
    Check ($global:QualVmFake.DirectCalls -eq 1) 'guest Up refusal must not retry direct query'
    Check ($global:QualVmFake.EnterCalls -eq 0) 'guest Up refusal must not open session'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    $result = & $connect -Name $validName -CredentialPath $credential
    Check ($result.Status -eq 'HOST_ZERO_ADAPTERS_GUEST_NO_UP_ADAPTERS') 'mock guest safe status'
    Check ($result.OSOrProductQualificationComplete -eq $false) 'mock success must not claim product qualification'
    Check ($global:QualVmFake.ImportCalls -eq 1 -and $global:QualVmFake.DirectCalls -eq 1) 'only one synthetic check'
    Check ($global:QualVmFake.EnterCalls -eq 0) 'successful readiness does not start a session'
    $passed++

    Reset-Fake
    $global:QualVmFake.Exists = $true
    $global:QualVmFake.VmState = 'Off'
    Assert-Hold { & $connect -Name $validName -CredentialPath $credential } 'must be running'
    Check ($global:QualVmFake.ImportCalls -eq 0) 'off VM must not import secret'
    $passed++

    Check ($global:QualVmFake.MutationCalls -eq 0) 'fake host must never execute mutators'
    Write-Output ("SYNTHETIC_POWERSHELL_PASS: {0} mocked entrypoint cases; no real Hyper-V or guest" -f $passed)
} finally {
    if (Test-Path -LiteralPath $root) {
        Remove-Item -LiteralPath $root -Recurse -Force -ErrorAction Stop
    }
}
