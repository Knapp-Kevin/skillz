#Requires -Version 5.1
#Requires -Modules Hyper-V
<#
.SYNOPSIS
  Verify air-gapped Hyper-V guest readiness before owner-authorized access.
.DESCRIPTION
  PowerShell Direct is the default: reads owner-created DPAPI Export-Clixml
  PSCredential under its SAME Windows account/machine. Tries authentication
  ONCE, checks guest adapters are not Up, then reports readiness.
  -OpenOwnerSession explicitly opens a session after verification.
  -Console does not load or forward a password; owner signs in manually.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-z][a-z0-9-]{2,60}$')]
    [string] $Name,
    [Parameter(Mandatory = $true, ParameterSetName = 'Direct')]
    [string] $CredentialPath,
    [Parameter(ParameterSetName = 'Direct')]
    [switch] $OpenOwnerSession,
    [Parameter(Mandatory = $true, ParameterSetName = 'Console')]
    [switch] $Console
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

foreach ($cmd in @('Get-VM','Get-VMNetworkAdapter','Get-VMGpuPartitionAdapter')) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        throw 'HOLD: required Hyper-V inspection command unavailable.'
    }
}
$vm = Get-VM -Name $Name -ErrorAction Stop
if ($null -eq $vm) { throw 'HOLD: requested VM does not exist.' }
$hostAdapters = @(Get-VMNetworkAdapter -VMName $Name -ErrorAction Stop)
if ($hostAdapters.Count -gt 0) {
    throw 'HOLD: host-side VM adapter present; air gap not qualified.'
}
$gpuAdapters = @(Get-VMGpuPartitionAdapter -VMName $Name -ErrorAction Stop)
if ($gpuAdapters.Count -gt 0) {
    throw 'HOLD: GPU partition adapter present; console and snapshot behavior must be reviewed by owner.'
}
if ($Console) {
    if (-not (Get-Command vmconnect.exe -ErrorAction SilentlyContinue)) {
        throw 'HOLD: VMConnect unavailable.'
    }
    # Console login remains owner-operated; no credential is supplied.
    & vmconnect.exe localhost $Name
    return
}
if ($vm.State -ne 'Running') {
    throw 'HOLD: VM must be running for a PowerShell Direct guest check.'
}

# Credential contents must never appear in stdout, exceptions, public logs,
# VM card or output artifact. Refuse filesystem redirection on input.
$cred = $null
try {
    if (-not [IO.Path]::IsPathRooted($CredentialPath) -or
        $CredentialPath -notmatch '^[a-zA-Z]:\\' -or
        $CredentialPath.StartsWith('\\')) {
        throw 'HOLD: credential path must be an absolute local drive path.'
    }
    $backingDrive = Get-PSDrive -Name $CredentialPath.Substring(0, 1) -ErrorAction Stop
    if ($backingDrive.Provider.Name -ne 'FileSystem' -or $backingDrive.DisplayRoot) {
        throw 'HOLD: mapped or network-backed credential path is prohibited.'
    }
    $item = Get-Item -LiteralPath $CredentialPath -Force -ErrorAction Stop
    if ($item -is [IO.DirectoryInfo] -or
        ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -or
        $item.Length -gt 1048576) {
        throw 'HOLD: credential path is unsafe or oversized.'
    }
    $dir = $item.Directory
    while ($null -ne $dir) {
        if ($dir.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            throw 'HOLD: credential ancestor is redirected.'
        }
        $dir = $dir.Parent
    }
    # Same-user/same-machine DPAPI storage. No retries, prompting, resetting
    # Windows credentials, or offline account tampering by this agent.
    $cred = Import-Clixml -LiteralPath $item.FullName -ErrorAction Stop
    if ($cred -isnot [System.Management.Automation.PSCredential]) {
        throw 'HOLD: credential file is not a PSCredential.'
    }
    # Probe the guest once, without printing machine, login or adapter names.
    $guestUp = @(Invoke-Command -VMName $Name -Credential $cred -ErrorAction Stop -ScriptBlock {
        @(
            Get-NetAdapter -IncludeHidden -ErrorAction Stop |
                Where-Object { $_.Status -eq 'Up' } |
                Select-Object -ExpandProperty Name
        )
    })
    if ($guestUp.Count -gt 0) {
        throw 'HOLD: guest reports an Up network adapter. Disconnect and investigate with owner.'
    }
    [pscustomobject]@{
        Status = 'HOST_ZERO_ADAPTERS_GUEST_NO_UP_ADAPTERS'
        CredentialLoadedFromDPAPI = $true
        HostIsolationVerifiedNow = $true
        GuestUpAdapterCount = 0
        FreshOSCheckpointVerified = $false
        OSOrProductQualificationComplete = $false
    }
    if ($OpenOwnerSession) {
        # Explicit owner-held access approval must precede this switch.
        # Not an authority grant for mutating guest state.
        Enter-PSSession -VMName $Name -Credential $cred -ErrorAction Stop
    }
} catch {
    # Only safe generic errors are surfaced; never expose password/username,
    # credential path or hypervisor/guest exception payloads in public logs.
    throw 'HOLD: exactly one private PowerShell Direct check failed or the guest is not isolated. No retry; owner intervention required.'
} finally {
    Remove-Variable -Name cred -ErrorAction SilentlyContinue
}
