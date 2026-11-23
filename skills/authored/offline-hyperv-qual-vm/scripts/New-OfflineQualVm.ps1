#Requires -Version 5.1
#Requires -Modules Hyper-V
<#
.SYNOPSIS
  Creates a strictly offline Generation 2 qualification VM after explicit owner approval.
.DESCRIPTION
  Default invocation is a read-only preflight plan. -Commit creates new files
  and a NEW VM only after ShouldProcess confirmation. No OS, user, password,
  network adapter, driver, checkpoint, or guest command is installed/created.
  If provisioning fails, the partial VM/directory is a HOLD for manual review.
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-z][a-z0-9-]{2,60}$')]
    [string] $Name,
    [Parameter(Mandatory = $true)]
    [string] $StorageRoot,
    [Parameter(Mandatory = $true)]
    [string] $IsoPath,
    [ValidateRange(4294967296, 549755813888)]
    [UInt64] $StartupMemoryBytes = 8589934592,
    [ValidateRange(34359738368, 2199023255552)]
    [UInt64] $OsDiskBytes = 137438953472,
    [ValidateRange(8589934592, 2199023255552)]
    [UInt64] $DataDiskBytes = 85899345920,
    [switch] $Commit
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Assert-LocalPath([string]$Path) {
    # Refuse UNC, relative and redirected PSDrives BEFORE touching media bytes.
    if (-not [IO.Path]::IsPathRooted($Path) -or $Path -notmatch '^[a-zA-Z]:\\' -or
        $Path.StartsWith('\\')) {
        throw 'HOLD: only an absolute local drive path is permitted.'
    }
    $backingDrive = Get-PSDrive -Name $Path.Substring(0, 1) -ErrorAction Stop
    if ($backingDrive.Provider.Name -ne 'FileSystem' -or $backingDrive.DisplayRoot) {
        throw 'HOLD: mapped or network-backed storage is prohibited.'
    }
    $entry = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    $cursor = $entry
    while ($null -ne $cursor) {
        if ($cursor.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            throw 'HOLD: redirected file or ancestor is not permitted.'
        }
        $cursor = if ($cursor.PSIsContainer) { $cursor.Parent } else { $cursor.Directory }
    }
    return $entry
}
function Assert-RealDirectory([string]$Path, [string]$Label) {
    $entry = Assert-LocalPath $Path
    if (-not $entry.PSIsContainer) {
        throw "HOLD: $Label must be an existing directory."
    }
    return $entry.FullName
}
function Assert-RealIso([string]$Path) {
    $entry = Assert-LocalPath $Path
    if ($entry.PSIsContainer -or
        -not $entry.Extension.Equals('.iso', [StringComparison]::OrdinalIgnoreCase)) {
        throw 'HOLD: OS media must be an ordinary, authorized .iso file.'
    }
    return $entry.FullName
}
function Assert-NoNetwork([string]$VmName) {
    $adapters = @(Get-VMNetworkAdapter -VMName $VmName -ErrorAction Stop)
    if ($adapters.Count -ne 0) { throw 'HOLD: VM still has a host-side network adapter.' }
}

# Refuse invalid host conditions and existing VM names before any mutation.
$cmds = @('Get-VM','New-VM','New-VHD','Add-VMHardDiskDrive',
          'Add-VMDvdDrive','Set-VMFirmware','Set-VM',
          'Get-VMNetworkAdapter','Remove-VMNetworkAdapter',
          'Enable-VMIntegrationService','Get-VMDvdDrive')
foreach ($cmd in $cmds) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        throw 'HOLD: required Hyper-V cmdlet is unavailable.'
    }
}
$storage = Assert-RealDirectory $StorageRoot 'StorageRoot'
$media = Assert-RealIso $IsoPath
if (@(Get-VM -Name $Name -ErrorAction SilentlyContinue).Count -gt 0) {
    throw 'HOLD: a VM with this name already exists; never overwrite or adopt it.'
}
$vmDir = Join-Path $storage $Name
if (Test-Path -LiteralPath $vmDir) {
    throw 'HOLD: output destination already exists; never overwrite it.'
}
$osVhd = Join-Path $vmDir 'os.vhdx'
$dataVhd = Join-Path $vmDir 'data.vhdx'

$plan = [pscustomobject]@{
    Status = 'PREFLIGHT_ONLY_NOT_CREATED'
    Name = $Name
    VmDirectory = $vmDir
    OsDiskBytes = $OsDiskBytes
    DataDiskBytes = $DataDiskBytes
    MemoryBytes = $StartupMemoryBytes
    Generation = 2
    NetworkAdapters = 0
    SecureBoot = 'On'
    AutomaticCheckpoints = $false
    OSInstalled = $false
    CredentialCreated = $false
    ExternalConnectivity = 'NONE'
}
if (-not $Commit) {
    $plan
    return
}
if (-not $PSCmdlet.ShouldProcess($Name, 'Create new air-gapped qualification VM and two dynamic VHDX disks')) {
    return
}
# No rollback deletion is performed on a partial failure. That preserves evidence
# and prevents a tool from deleting something it did not fully create.
try {
    $vm = New-VM -Name $Name -Generation 2 -NoVHD -MemoryStartupBytes $StartupMemoryBytes -Path $vmDir -ErrorAction Stop
    # No switch is ever supplied. If this host inserts an adapter by default,
    # remove it immediately before starting or configuring the guest.
    Get-VMNetworkAdapter -VMName $Name -ErrorAction Stop | Remove-VMNetworkAdapter -ErrorAction Stop
    Assert-NoNetwork $Name
    New-VHD -Path $osVhd -SizeBytes $OsDiskBytes -Dynamic -ErrorAction Stop | Out-Null
    New-VHD -Path $dataVhd -SizeBytes $DataDiskBytes -Dynamic -ErrorAction Stop | Out-Null
    Add-VMHardDiskDrive -VMName $Name -Path $osVhd -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0 -ErrorAction Stop
    Add-VMHardDiskDrive -VMName $Name -Path $dataVhd -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 1 -ErrorAction Stop
    $dvd = Add-VMDvdDrive -VMName $Name -Path $media -ControllerNumber 0 -ControllerLocation 2 -Passthru -ErrorAction Stop
    Set-VMFirmware -VMName $Name -EnableSecureBoot On -FirstBootDevice $dvd -ErrorAction Stop
    Set-VM -VMName $Name -DynamicMemoryEnabled:$false -AutomaticCheckpointsEnabled:$false -AutomaticStartAction Nothing -ErrorAction Stop
    Enable-VMIntegrationService -VMName $Name -Name 'Guest Service Interface' -ErrorAction Stop
    Assert-NoNetwork $Name
    if ((Get-VM -Name $Name -ErrorAction Stop).State -ne 'Off') {
        throw 'HOLD: VM unexpectedly running. Do not continue.'
    }
    [pscustomobject]@{
        Status = 'CREATED_VM_SHELL_NO_OS_NO_CREDENTIAL'
        Name = $Name
        VmDirectory = $vmDir
        NetworkAdapters = 0
        NextAction = 'OWNER_INSTALL_OS_THEN_SAVE_CREDENTIAL_AND_FRESH_OS_CHECKPOINT'
        HostBehaviorVerified = $true
        GuestAirGapVerified = $false
        NativeQualificationComplete = $false
    }
} catch {
    # Do not echo paths or upstream exception details into shared logs.
    throw 'HOLD: provisioning incomplete. Do not boot. Inspect VM state and partial files locally; no automatic cleanup.'
}
