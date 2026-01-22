# macOS Hackintosh Installer for Windows

A comprehensive terminal-based automation tool to guide and automate the installation of macOS on a Windows computer using OpenCore.

## ⚠️ DISCLAIMER

**This tool is for educational purposes only.** Installing macOS on non-Apple hardware may violate Apple's licensing terms. Ensure you understand the legal implications before proceeding.

## 📋 Requirements

### Hardware
- **CPU**: Intel or AMD processor (check Dortania compatibility list)
- **RAM**: Minimum 4GB (8GB+ recommended)
- **Disk Space**: 150GB+ free space
- **USB Drive**: 16GB+ (for installation media)
- **GPU**: Supported graphics card (NVIDIA, AMD, or iGPU)

### Software
- **Windows 10/11** with Administrator privileges
- **Python 3.8+** (install from Microsoft Store)
- **Internet Connection** (10GB+ bandwidth for downloads)

### Pre-Installation
- **Backup all data** to external drive or cloud
- **Disable Secure Boot** in BIOS (will be done during installation)
- **Check compatibility** at https://dortania.github.io/OpenCore-Install-Guide/

## 🚀 Quick Start

### Option 1: Automated Installation (Recommended)
```powershell
cd "C:\Users\User\Downloads\Mac Os"
python macOS-Installer.py --auto
```

### Option 2: Interactive Menu
```powershell
cd "C:\Users\User\Downloads\Mac Os"
python macOS-Installer.py
```

### Option 3: System Validation Only
```powershell
cd "C:\Users\User\Downloads\Mac Os"
python macOS-Installer.py --validate
```

### Option 4: Batch File (Easiest)
1. Right-click `Start-macOS-Installer.bat`
2. Select "Run as administrator"
3. Follow the on-screen prompts

## 📋 What This Tool Does

### Automated Steps
✅ Validates system requirements and administrator privileges
✅ Checks Python installation and dependencies
✅ Verifies disk space and internet connectivity
✅ Downloads all required tools and utilities
✅ Extracts and organizes files
✅ Downloads macOS recovery image (10-30 minutes)
✅ Generates activity logs for troubleshooting

### Manual Steps (User Guided)
📌 Running OpenCore Simplify for hardware scanning and EFI building
📌 USB drive formatting with Rufus
📌 Disk partitioning for macOS in Windows Disk Management
📌 BIOS configuration (Secure Boot disable, boot order)
📌 macOS installation from USB
📌 Post-installation EFI mounting and file copying

## 📥 Installation Steps

### Step 1: System Validation
```
python macOS-Installer.py
Select: 1 (Validate System Requirements)
```
Verifies:
- Administrator privileges
- Python 3.8+
- Windows 10/11
- Disk space (150GB+ free)
- Internet connectivity

### Step 2: Download OpenCore Simplify
```
Select: 2 (Download & Setup OpenCore Simplify)
```
This tool will:
- Scan your hardware automatically
- List compatible macOS versions
- Auto-select appropriate patches and drivers
- Build EFI folder with optimized configuration

### Step 3: Run OpenCore Simplify
```
Select: 3 (Run OpenCore Simplify)
```
Follow the prompts:
1. When prompted "Skip update?": Type **N** (get latest)
2. When prompted "Skip future updates?": Type **Y**
3. Type **I** to scan hardware
4. Type **E** to list supported macOS versions
5. Select desired macOS (e.g., **24** for Sequoia)
6. Wait for auto-selection (~5 minutes)
7. Type **6** to build EFI
8. Copy generated EFI folder to Desktop

### Step 4: Download Tools
```
Select: 4 (Download USB Tools)
Select: 5 (Download Additional Tools)
Select: 6 (Download macOS Recovery Image)
```
This downloads:
- USBToolBox for USB port mapping
- OC Auxiliary Tools for EFI editing
- Rufus for USB formatting
- OpenCore bootloader
- macOS recovery image (⏱️ ~20 minutes)

### Step 5: Prepare USB Drive
```
Select: 7 (USB Formatting Guide)
```
Using Rufus:
1. Insert 16GB+ USB drive
2. Select USB drive in Rufus
3. Set: Boot=Non-bootable, Partition=GPT, File System=FAT32
4. Click Start and confirm

### Step 6: Copy Files to USB
```
Select: 8 (Copy Files to USB)
```
Copy these to USB root:
- `Desktop/EFI` → `E:\EFI`
- `Desktop/macOS_Recovery/com.apple.recovery.boot` → `E:\com.apple.recovery.boot`

### Step 7: Partition macOS Drive
```
Select: 9 (Disk Partitioning Guide)
```
In Windows Disk Management:
1. Right-click C: → Shrink Volume
2. Shrink by 100GB (or desired size)
3. Right-click unallocated space → New Simple Volume
4. Format as exFAT, label "macOS"

### Step 8: Configure BIOS
```
Select: 10 (BIOS Configuration Guide)
```
During restart:
1. Press Delete/F2/F10 to enter BIOS
2. Find Boot/Security tab
3. **Disable Secure Boot**
4. Set USB as **first boot device**
5. Save and Exit (F10)

### Step 9: Install macOS
```
Select: 11 (macOS Installation Guide)
```
Boot process:
1. PC boots from USB to OpenCore
2. Select "macOS Base System"
3. Wait for Recovery to load (5-10 min)
4. Open Disk Utility
5. Erase "macOS" partition as APFS
6. Start macOS Installation
7. System restarts 3-4 times automatically
8. Complete setup wizard

### Step 10: Post-Installation
```
Select: 12 (Post-Installation Steps)
```
Final steps in macOS:
1. Open OC Auxiliary Tools
2. Go to Disk → Mount EFI
3. Copy Boot and OC folders from USB EFI to internal EFI
4. Boot to Windows
5. Open Command Prompt (Admin)
6. Run: `bcdedit /set {bootmgr} path \efi\boot\bootx64.efi`
7. Restart to see dual-boot menu

## 🛠️ Troubleshooting

### Black Screen After Boot
```
Select: 13 (Troubleshooting Guide)
Select: 1 (Black screen after boot)
```
Solutions:
- Force shutdown → Boot to BIOS
- Verify USB is first boot device
- Reformat macOS partition
- Disable Secure Boot in BIOS

### USB Not Detected
- Try different USB ports
- Use different USB drive (8GB+ minimum)
- Reformat with Rufus
- Check for cable issues

### Installation Stuck/Hangs
- Check hardware on Dortania.io
- Verify BIOS settings (XMP disabled, UEFI enabled)
- Try different USB drive
- Check for bad sectors: `chkdsk E: /F`

### Wi-Fi Not Working
- Use Ethernet temporarily
- Check WiFi kext compatibility
- Add WiFi kext before reinstalling

### Revert to Windows Only
```
1. Boot to Windows
2. Open Command Prompt (Admin)
3. Run: bcdedit /set {bootmgr} path \Windows\System32\winload.efi
4. Restart
```

## 📊 File Organization

After running this tool, your Desktop will contain:

```
Desktop/
├── EFI/                          # Main EFI bootloader
│   ├── Boot/
│   └── OC/
├── OpenCore-Simplify/           # Tool for scanning and EFI building
├── USBTools/
│   ├── USBToolBox.exe          # USB port mapping tool
│   └── Kexts/                   # USB drivers
├── MacOSTools/
│   ├── OCAuxiliaryTools/        # EFI editor GUI
│   ├── OpenCorePkg/             # OpenCore source
│   └── Rufus.exe               # USB formatter
└── macOS_Recovery/              # Recovery image files
    └── com.apple.recovery.boot/
```

## 📝 Installation Log

All actions are logged automatically. View logs:
```
Select: 14 (View Installation Log)
```

Logs help with troubleshooting if something goes wrong.

## 🔗 Useful Links

- **Dortania Guide**: https://dortania.github.io/OpenCore-Install-Guide/
- **OpenCore Documentation**: https://github.com/acidanthera/OpenCorePkg
- **Hardware Compatibility**: https://dortania.github.io/OpenCore-Install-Guide/macos-limits.html
- **Community Support**: https://www.reddit.com/r/hackintosh/
- **SMBIOS Generator**: https://github.com/corpnewt/GenSMBIOS

## ⚡ Advanced Options

### Command Line Arguments

```bash
# Full automation (non-interactive)
python macOS-Installer.py --auto

# Validate system only
python macOS-Installer.py --validate

# Show help
python macOS-Installer.py --help
```

### Troubleshooting Commands

```powershell
# Reset boot to Windows only
bcdedit /set {bootmgr} path \Windows\System32\winload.efi

# Check current boot config
bcdedit

# Check disk space
Get-Volume

# Check free disk space
(Get-Volume D:).SizeRemaining / 1GB
```

## 📌 Important Notes

1. **Backup Data**: Create full backup before modifying disk partitions
2. **Secure Boot**: Must be disabled in BIOS during installation
3. **BIOS Version**: Update motherboard BIOS to latest version first
4. **Hardware Compatibility**: Research on Dortania before starting
5. **Internet Required**: For downloading 10GB+ of files
6. **Time**: Total process takes 3-5 hours including downloads
7. **Patience**: Installation can take 1-2 hours with multiple restarts

## ❓ FAQ

**Q: Is this legal?**
A: Installing macOS on non-Apple hardware violates Apple's EULA. This tool is for educational purposes.

**Q: Which hardware is supported?**
A: Intel/AMD CPUs with compatible GPUs. Check Dortania's compatibility list.

**Q: How long does installation take?**
A: Downloads (20-30 min) + Partitioning (5 min) + Installation (1-2 hours) + Post-setup (15 min)

**Q: Can I dual-boot Windows and macOS?**
A: Yes, this tool sets up dual-boot with OpenCore menu.

**Q: What if something goes wrong?**
A: Use the Troubleshooting Guide or revert to Windows-only using provided commands.

**Q: Do I need an Apple ID?**
A: Not required during installation, but helpful for App Store access later.

**Q: Can I update macOS after installation?**
A: Yes, but requires EFI updates. Check Dortania guide for updates.

## 🐛 Bug Reports

If you encounter issues:
1. Check troubleshooting section (Option 13)
2. Review installation log (Option 14)
3. Visit https://dortania.github.io/OpenCore-Install-Guide/
4. Consult community at r/hackintosh

## 📄 License

This tool is provided as-is for educational purposes. Users assume all responsibility and risk.

---

**Made for enthusiasts. Use at your own risk. Happy Hackintoshing! 🍎**

