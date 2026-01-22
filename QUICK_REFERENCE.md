# Quick Reference Guide - macOS Hackintosh Installation

## 📋 Pre-Installation Checklist

- [ ] Administrator access on Windows 10/11
- [ ] 150GB+ free disk space
- [ ] 16GB+ USB drive (preferably USB 3.0)
- [ ] External backup of important data
- [ ] Python 3.8+ installed
- [ ] Motherboard manual/documentation available
- [ ] Internet connection (10GB+ bandwidth)
- [ ] Verified hardware compatibility on Dortania

## 🚀 Quick Start Commands

```powershell
# Option 1: Run batch file (easiest)
Right-click Start-macOS-Installer.bat → Run as administrator

# Option 2: Run with Python
python macOS-Installer.py

# Option 3: Full automation (hands-off)
python macOS-Installer.py --auto

# Option 4: Validate only
python macOS-Installer.py --validate
```

## 🔑 Key Menu Options

| Option | Purpose |
|--------|---------|
| 1 | Check system requirements |
| 2 | Download OpenCore Simplify |
| 3 | Run hardware scan & build EFI |
| 4 | Download USB tools |
| 5 | Download OCAT, OpenCore, Rufus |
| 6 | Download macOS recovery image |
| 7 | USB formatting guide |
| 8 | Copy files to USB |
| 9 | Create macOS partition |
| 10 | BIOS configuration help |
| 11 | Installation procedure |
| 12 | Post-installation steps |
| 13 | Troubleshooting |
| 14 | View installation log |

## ⏱️ Estimated Timeline

| Phase | Time | Notes |
|-------|------|-------|
| System validation | 1 min | Automatic check |
| OpenCore Simplify | 10 min | Scanning & EFI build |
| Tool downloads | 5 min | Small utilities |
| macOS recovery | 20-30 min | Largest download |
| USB preparation | 10 min | Formatting & copying |
| Partitioning | 5 min | Disk management |
| BIOS setup | 5 min | Per motherboard |
| macOS install | 60-90 min | Multiple reboots |
| Post-install | 15 min | EFI mounting |
| **TOTAL** | **2-4 hours** | Mostly waiting |

## 🎯 Critical Steps

### 1. OpenCore Simplify Prompts
```
Skip update? → Type: N (get latest)
Skip future updates? → Type: Y (avoid nags)
Scan hardware? → Type: I (run scan)
List macOS? → Type: E (show versions)
Build EFI? → Type: 6 (generate EFI)
```

### 2. Rufus USB Settings
- **Device**: Your USB drive
- **Boot Selection**: Non bootable
- **Partition Scheme**: GPT
- **File System**: FAT32
- **Click**: Start

### 3. BIOS Settings (General)
- **Disable**: Secure Boot
- **Set First Boot Device**: USB drive
- **Enable**: XMP disabled (optional)
- **Save**: F10 > Yes

### 4. Disk Utility (macOS Recovery)
- **Select**: macOS partition (exFAT)
- **Erase**:
  - Name: macOS
  - Format: APFS
  - Scheme: GUID

### 5. Final Boot Configuration (Windows)
```powershell
# Run as Administrator
bcdedit /set {bootmgr} path \efi\boot\bootx64.efi
```

## 🗂️ File Locations

| File | Location | Purpose |
|------|----------|---------|
| EFI Folder | Desktop/EFI | OpenCore bootloader |
| OpenCore Simplify | Desktop/OpenCore-Simplify | Hardware scanning tool |
| USBToolBox | Desktop/USBTools/USBToolBox.exe | USB port mapping |
| OCAT | Desktop/MacOSTools/OCAuxiliaryTools | EFI editor |
| Rufus | Desktop/MacOSTools/Rufus.exe | USB formatter |
| Recovery Image | Desktop/macOS_Recovery | Installation files |

## ⚠️ Common Issues & Quick Fixes

### Black Screen
```
Force shutdown (10s) → Boot BIOS → Check boot order → Verify USB first
```

### USB Not Detected
```
Try different USB port → Try different USB drive → Reformat with Rufus
```

### Stuck Installation
```
Check compatibility → Disable XMP in BIOS → Try different USB → Check cables
```

### Wi-Fi Issues
```
Use Ethernet first → Add WiFi kext → Rebuild EFI → Try again
```

### Revert to Windows Only
```powershell
bcdedit /set {bootmgr} path \Windows\System32\winload.efi
```

## 📞 Support Resources

| Resource | URL |
|----------|-----|
| Dortania Guide | dortania.github.io/OpenCore-Install-Guide/ |
| Reddit Community | reddit.com/r/hackintosh |
| OpenCore Docs | github.com/acidanthera/OpenCorePkg |
| Hardware Limits | dortania.github.io/OpenCore-Install-Guide/macos-limits.html |
| SMBIOS Generator | github.com/corpnewt/GenSMBIOS |

## 🔐 Boot Menu Shortcuts

| Action | Key |
|--------|-----|
| Enter BIOS | Delete, F2, F10, F12 (motherboard dependent) |
| Select boot device | ESC or F12 during startup |
| Safe Mode Windows | Hold Shift during restart |
| macOS Recovery | Cmd + R after boot |
| Disk Utility | Tools > Disk Utility in Recovery |

## 💾 Data Backup Command

```powershell
# Backup important files before starting
robocopy C:\Users\alias\Documents D:\Backup /mir /z
```

## ✅ Validation Commands (Windows)

```powershell
# Check Python
python --version

# Check admin
net session

# Check disk space
Get-Volume

# Check free space on C:
$vol = Get-Volume -DriveLetter C
Write-Host "Free: $($vol.SizeRemaining / 1GB) GB"

# Check USB drives
Get-Disk | Where {$_.BusType -eq 'USB'}
```

## 🎮 Dual Boot Menu

After installation, reboot and you'll see OpenCore boot menu:
```
> macOS (default)
  Windows 11
  UEFI Shell
  Reset NVRAM
```

Use arrow keys to select, Enter to boot.

## 📊 Installation Phases

### Phase 1: Boot to USB (1-2 min)
```
Computer starts → OpenCore menu → Select macOS Base System
```

### Phase 2: macOS Recovery (5-10 min)
```
Loading Darwin → Recovery complete → Open Disk Utility
```

### Phase 3: Format & Install (30-45 min)
```
Erase partition → Start macOS Install → Initial setup
```

### Phase 4: Installation Reboots (30-45 min)
```
System Restart 1 → Continue install
System Restart 2 → Continue install
System Restart 3 → macOS boots
```

### Phase 5: Setup Wizard (5-10 min)
```
Language → Region → Wi-Fi → Apple ID (optional) → Complete
```

## 🔄 If Installation Fails

1. **Force shutdown** (hold power 10 seconds)
2. **Boot to Windows** (select from OpenCore menu)
3. **Reformat macOS** partition (Disk Management)
4. **Check logs** (Option 14 in menu)
5. **Consult Dortania** guide for your hardware
6. **Try again** with updated EFI if needed

## 📝 Important Notes

- ⏱️ **Plan 3-5 hours** for complete installation
- 🔌 **Don't unplug USB** during installation phases
- 🌐 **Need internet** for ~10GB of downloads
- 💾 **Backup first** - disk operations are destructive
- 🔐 **Secure Boot OFF** - required for OpenCore
- 📱 **Apple ID optional** - can setup later in System Settings

## 🎯 Next Steps After Installation

1. Mount internal EFI partition
2. Copy EFI from USB to internal drive
3. Install macOS updates (if any)
4. Install kexts for unsupported hardware
5. Fine-tune BIOS settings
6. Test Windows boot from dual-boot menu

---

**Ready to start? Run:** `Start-macOS-Installer.bat` as Administrator

**Have questions? See:** Full README.md in installation folder
