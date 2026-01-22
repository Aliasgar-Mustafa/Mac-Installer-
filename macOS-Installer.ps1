# macOS Hackintosh Installer - PowerShell Helper Script
# Run this with administrator privileges for full functionality

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('menu','auto','validate','help')]
    [string]$Mode = 'menu'
)

# Color definitions
$Colors = @{
    'Green' = [System.ConsoleColor]::Green
    'Red' = [System.ConsoleColor]::Red
    'Yellow' = [System.ConsoleColor]::Yellow
    'Cyan' = [System.ConsoleColor]::Cyan
    'White' = [System.ConsoleColor]::White
}

# Function to write colored output
function Write-ColorOutput {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Message,
        [Parameter(Mandatory=$false)]
        [System.ConsoleColor]$Color = 'White'
    )
    Write-Host $Message -ForegroundColor $Color
}

# Function to check admin privileges
function Test-AdminPrivileges {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Function to check Python installation
function Test-PythonInstallation {
    try {
        $pythonVersion = python --version 2>&1
        Write-ColorOutput "✓ Python detected: $pythonVersion" $Colors['Green']
        return $true
    }
    catch {
        Write-ColorOutput "✗ Python not found in PATH" $Colors['Red']
        return $false
    }
}

# Function to display system info
function Show-SystemInfo {
    Write-Host ""
    Write-ColorOutput "=== SYSTEM INFORMATION ===" $Colors['Cyan']
    Write-Host ""
    
    $osInfo = Get-CimInstance -ClassName Win32_OperatingSystem
    Write-Host "OS: $($osInfo.Caption)"
    Write-Host "Version: $($osInfo.Version)"
    Write-Host "Build: $($osInfo.BuildNumber)"
    Write-Host ""
    
    $cpu = Get-CimInstance -ClassName Win32_Processor | Select-Object -First 1
    Write-Host "CPU: $($cpu.Name)"
    Write-Host "Cores: $($cpu.NumberOfCores)"
    Write-Host ""
    
    $ram = Get-CimInstance -ClassName Win32_ComputerSystemProduct
    $totalRam = ([Math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB))
    Write-Host "RAM: ${totalRam}GB"
    Write-Host ""
    
    $drives = Get-Volume | Where-Object {$_.DriveLetter} | Select-Object DriveLetter, FileSystemLabel, SizeRemaining, Size
    Write-ColorOutput "DISK SPACE:" $Colors['Yellow']
    foreach ($drive in $drives) {
        $freeGB = [Math]::Round($drive.SizeRemaining / 1GB)
        $totalGB = [Math]::Round($drive.Size / 1GB)
        Write-Host "$($drive.DriveLetter): $freeGB GB free / $totalGB GB total"
    }
    Write-Host ""
}

# Function to check disk space
function Test-DiskSpace {
    Write-ColorOutput "=== CHECKING DISK SPACE ===" $Colors['Cyan']
    
    $cDrive = Get-Volume -DriveLetter C
    $freeSpace = [Math]::Round($cDrive.SizeRemaining / 1GB)
    
    Write-Host "Free space on C: $freeSpace GB"
    
    if ($freeSpace -lt 150) {
        Write-ColorOutput "⚠ WARNING: Less than 150GB free (recommended: 150GB+)" $Colors['Yellow']
        Write-Host ""
        return $false
    }
    else {
        Write-ColorOutput "✓ Sufficient disk space" $Colors['Green']
        Write-Host ""
        return $true
    }
}

# Function to check internet connectivity
function Test-InternetConnectivity {
    Write-ColorOutput "=== CHECKING INTERNET CONNECTIVITY ===" $Colors['Cyan']
    
    try {
        $testConnection = Test-NetConnection -ComputerName github.com -Port 443 -WarningAction SilentlyContinue
        if ($testConnection.TcpTestSucceeded) {
            Write-ColorOutput "✓ Internet connection verified" $Colors['Green']
            return $true
        }
        else {
            Write-ColorOutput "✗ Cannot connect to internet" $Colors['Red']
            return $false
        }
    }
    catch {
        Write-ColorOutput "⚠ Could not verify internet connection" $Colors['Yellow']
        return $false
    }
}

# Function to list USB drives
function Get-USBDrives {
    Write-ColorOutput "=== USB DRIVES DETECTED ===" $Colors['Cyan']
    Write-Host ""
    
    $usbDrives = Get-Disk | Where-Object {$_.BusType -eq 'USB'}
    
    if ($usbDrives) {
        $index = 1
        foreach ($drive in $usbDrives) {
            $volume = Get-Partition -DiskNumber $drive.Number -ErrorAction SilentlyContinue | 
                      Get-Volume -ErrorAction SilentlyContinue
            $sizeGB = [Math]::Round($drive.Size / 1GB)
            Write-Host "$index. Disk $($drive.Number) - $sizeGB GB"
            Write-Host "   Friendly Name: $($drive.FriendlyName)"
            Write-Host "   Serial: $($drive.SerialNumber)"
            Write-Host ""
            $index++
        }
        return $usbDrives.Count
    }
    else {
        Write-ColorOutput "✗ No USB drives detected" $Colors['Red']
        Write-Host ""
        return 0
    }
}

# Function to show boot configuration
function Show-BootConfiguration {
    Write-ColorOutput "=== CURRENT BOOT CONFIGURATION ===" $Colors['Cyan']
    Write-Host ""
    
    try {
        $bcdeditOutput = bcdedit /enum firmware 2>$null
        if ($bcdeditOutput) {
            Write-Host $bcdeditOutput
        }
        else {
            Write-Host "No UEFI entries found"
        }
    }
    catch {
        Write-ColorOutput "Could not read boot configuration" $Colors['Yellow']
    }
    Write-Host ""
}

# Function to start installation
function Start-Installation {
    param(
        [ValidateSet('auto','menu','validate')]
        [string]$InstallMode = 'menu'
    )
    
    $scriptPath = Get-Location
    $pythonScript = Join-Path $scriptPath "macOS-Installer.py"
    
    if (-not (Test-Path $pythonScript)) {
        Write-ColorOutput "✗ macOS-Installer.py not found in $scriptPath" $Colors['Red']
        return
    }
    
    Write-ColorOutput "Starting macOS Hackintosh Installer..." $Colors['Green']
    Write-Host ""
    
    if ($InstallMode -eq 'auto') {
        python $pythonScript --auto
    }
    elseif ($InstallMode -eq 'validate') {
        python $pythonScript --validate
    }
    else {
        python $pythonScript
    }
}

# Main menu
function Show-Menu {
    Clear-Host
    Write-ColorOutput "╔════════════════════════════════════════════════════════════╗" $Colors['Cyan']
    Write-ColorOutput "║   macOS Hackintosh Installer for Windows - PowerShell      ║" $Colors['Cyan']
    Write-ColorOutput "║                    Helper Script                          ║" $Colors['Cyan']
    Write-ColorOutput "╚════════════════════════════════════════════════════════════╝" $Colors['Cyan']
    Write-Host ""
    
    # Check prerequisites
    if (Test-AdminPrivileges) {
        Write-ColorOutput "✓ Administrator privileges" $Colors['Green']
    }
    else {
        Write-ColorOutput "✗ NOT running as Administrator" $Colors['Red']
    }
    
    if (Test-PythonInstallation) {
        # Already shows result
    }
    else {
        Write-ColorOutput "  → Install Python from Microsoft Store" $Colors['Yellow']
    }
    
    Write-Host ""
    Write-ColorOutput "SELECT AN OPTION:" $Colors['Yellow']
    Write-Host ""
    Write-Host "1. Show System Information"
    Write-Host "2. Check Disk Space"
    Write-Host "3. Check Internet Connectivity"
    Write-Host "4. List USB Drives"
    Write-Host "5. Show Boot Configuration"
    Write-Host "6. Start Installation (Interactive Menu)"
    Write-Host "7. Start Installation (Full Automation)"
    Write-Host "8. Validate System Only"
    Write-Host "9. System Health Check"
    Write-Host "0. Exit"
    Write-Host ""
    Write-Host -NoNewline "Enter choice (0-9): "
}

# Main loop
function Main {
    if (-not (Test-AdminPrivileges)) {
        Write-ColorOutput "ERROR: This script requires administrator privileges!" $Colors['Red']
        Write-ColorOutput "Please run PowerShell as Administrator" $Colors['Red']
        exit 1
    }
    
    if ($Mode -eq 'help') {
        Write-Host @"
macOS Hackintosh Installer - PowerShell Helper Script

USAGE:
  .\macOS-Installer.ps1 [Mode]

MODES:
  menu      - Interactive menu (default)
  auto      - Start full automation immediately
  validate  - Validate system requirements only
  help      - Show this help message

EXAMPLES:
  .\macOS-Installer.ps1
  .\macOS-Installer.ps1 auto
  .\macOS-Installer.ps1 validate

REQUIREMENTS:
  - Windows 10/11
  - Administrator privileges
  - Python 3.8+ installed
  - 150GB+ free disk space
  - USB drive 16GB+ (for installation)
"@
        exit 0
    }
    
    if ($Mode -eq 'auto') {
        Start-Installation -InstallMode 'auto'
        exit 0
    }
    
    if ($Mode -eq 'validate') {
        Start-Installation -InstallMode 'validate'
        exit 0
    }
    
    # Interactive menu mode
    while ($true) {
        Show-Menu
        $choice = Read-Host
        
        switch ($choice) {
            '1' {
                Show-SystemInfo
                Read-Host "Press Enter to continue"
            }
            '2' {
                Test-DiskSpace
                Read-Host "Press Enter to continue"
            }
            '3' {
                Test-InternetConnectivity
                Read-Host "Press Enter to continue"
            }
            '4' {
                Get-USBDrives
                Read-Host "Press Enter to continue"
            }
            '5' {
                Show-BootConfiguration
                Read-Host "Press Enter to continue"
            }
            '6' {
                Start-Installation -InstallMode 'menu'
                exit 0
            }
            '7' {
                $confirm = Read-Host "Start full automation? (Y/N)"
                if ($confirm -eq 'Y' -or $confirm -eq 'y') {
                    Start-Installation -InstallMode 'auto'
                    exit 0
                }
            }
            '8' {
                Start-Installation -InstallMode 'validate'
                exit 0
            }
            '9' {
                Clear-Host
                Write-ColorOutput "=== SYSTEM HEALTH CHECK ===" $Colors['Cyan']
                Write-Host ""
                Show-SystemInfo
                Test-DiskSpace | Out-Null
                Test-InternetConnectivity | Out-Null
                Get-USBDrives | Out-Null
                Read-Host "Press Enter to continue"
            }
            '0' {
                Write-ColorOutput "Exiting... Good luck with your macOS installation!" $Colors['Green']
                exit 0
            }
            default {
                Write-ColorOutput "Invalid choice. Please try again." $Colors['Red']
                Start-Sleep -Seconds 1
            }
        }
    }
}

# Run main function
Main
