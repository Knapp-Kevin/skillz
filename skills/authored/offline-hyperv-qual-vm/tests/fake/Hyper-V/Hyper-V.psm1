# Synthetic Hyper-V module used only by the Windows CI test process.
# NEVER delegates to the native Hyper-V cmdlets or creates guest resources.
# All mutating cmdlets throw, including if the script under test regresses.
$global:QualVmFake = [pscustomobject]@{
    Exists = $false
    VmState = 'Running'
    HostNic = $false
    GpuPartition = $false
    GuestNicUp = $false
    ImportCalls = 0
    DirectCalls = 0
    MutationCalls = 0
    EnterCalls = 0
}
function Get-VM {
    [CmdletBinding()]
    param([string]$Name)
    if ($global:QualVmFake.Exists) {
        [pscustomobject]@{ Name = $Name; State = $global:QualVmFake.VmState }
    }
}
function Get-VMNetworkAdapter {
    [CmdletBinding()]
    param([string]$VMName)
    if ($global:QualVmFake.HostNic) { [pscustomobject]@{ Name='synthetic-nic' } }
}
function Get-VMGpuPartitionAdapter {
    [CmdletBinding()]
    param([string]$VMName)
    if ($global:QualVmFake.GpuPartition) { [pscustomobject]@{ Name='synthetic-gpu' } }
}
function Get-PSDrive {
    [CmdletBinding()]
    param([string]$Name)
    if ($Name -eq 'Z') {
        [pscustomobject]@{
            Name = 'Z'
            Provider = [pscustomobject]@{Name='FileSystem'}
            DisplayRoot = '\\synthetic-server\fake-share'
        }
        return
    }
    Microsoft.PowerShell.Management\Get-PSDrive -Name $Name -ErrorAction Stop
}
function Import-Clixml {
    [CmdletBinding()]
    param([string]$LiteralPath)
    $global:QualVmFake.ImportCalls += 1
    $secure = ConvertTo-SecureString -String 'fictional-fixture-only' -AsPlainText -Force
    [System.Management.Automation.PSCredential]::new('fictional-guest', $secure)
}
function Invoke-Command {
    [CmdletBinding()]
    param([string]$VMName, [System.Management.Automation.PSCredential]$Credential,
          [scriptblock]$ScriptBlock)
    $global:QualVmFake.DirectCalls += 1
    if ($global:QualVmFake.GuestNicUp) { 'fictional-up-adapter' }
}
function Enter-PSSession {
    [CmdletBinding()]
    param([string]$VMName, [System.Management.Automation.PSCredential]$Credential)
    $global:QualVmFake.EnterCalls += 1
    throw 'No real guest interactive session is permitted in this synthetic harness.'
}
function Block-HostMutation {
    $global:QualVmFake.MutationCalls += 1
    throw 'SYNTHETIC_HOST_MUTATION_FORBIDDEN'
}
function New-VM { [CmdletBinding()] param([string]$Name) Block-HostMutation }
function New-VHD { [CmdletBinding()] param([string]$Path) Block-HostMutation }
function Add-VMHardDiskDrive { [CmdletBinding()] param([string]$VMName) Block-HostMutation }
function Add-VMDvdDrive { [CmdletBinding()] param([string]$VMName) Block-HostMutation }
function Set-VMFirmware { [CmdletBinding()] param([string]$VMName) Block-HostMutation }
function Set-VM { [CmdletBinding()] param([string]$VMName) Block-HostMutation }
function Remove-VMNetworkAdapter { [CmdletBinding()] param([Parameter(ValueFromPipeline=$true)]$InputObject) process { Block-HostMutation } }
function Enable-VMIntegrationService { [CmdletBinding()] param([string]$VMName) Block-HostMutation }
function Get-VMDvdDrive { [CmdletBinding()] param([string]$VMName) }
Export-ModuleMember -Function Get-VM,Get-VMNetworkAdapter,Get-VMGpuPartitionAdapter,Get-PSDrive,Import-Clixml,Invoke-Command,Enter-PSSession,New-VM,New-VHD,Add-VMHardDiskDrive,Add-VMDvdDrive,Set-VMFirmware,Set-VM,Remove-VMNetworkAdapter,Enable-VMIntegrationService,Get-VMDvdDrive
