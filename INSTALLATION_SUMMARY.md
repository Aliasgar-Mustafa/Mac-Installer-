# macOS Hackintosh Installation - Complete Package

Welcome to the automated macOS Hackintosh Installation toolkit for Windows!

This package contains everything needed to automate the process of installing macOS on a Windows computer.

## 📦 What's Included

### Main Applications
1. **macOS-Installer.py** (Primary Tool)
   - Full-featured Python automation script
   - Interactive menu system
   - Automatic downloads and setup
   - System validation and logging
   - Troubleshooting guides

2. **Start-macOS-Installer.bat** (Windows Batch Launcher)
   - One-click launcher with admin privileges check
   - Easy for non-technical users
   - Validates Python installation

3. **macOS-Installer.ps1** (PowerShell Helper)
   - System information and diagnostics
   - USB drive detection
   - Boot configuration viewing
   - Disk space and connectivity checks

### Documentation
- **README.md** - Comprehensive installation guide
- **QUICK_REFERENCE.md** - Quick lookup table
- **INSTALLATION_SUMMARY.md** - This file
- **TROUBLESHOOTING_GUIDE.md** - Common issues and fixes

## 🎯 Installation Methods

### Method 1: Easiest (Batch File)
```
1. Right-click "Start-macOS-Installer.bat"
2. Select "Run as administrator"
3. Follow on-screen prompts
```

### Method 2: Command Prompt
```
1. Open Command Prompt as Administrator
2. Navigate to this folder
3. Type: python macOS-Installer.py
4. Follow the menu
```

### Method 3: PowerShell
```
1. Open PowerShell as Administrator
2. Navigate to this folder
3. Type: .\macOS-Installer.ps1
4. Select options from menu
```

### Method 4: Full Automation (Advanced)
```
1. Open Command Prompt as Administrator
2. Navigate to this folder
3. Type: python macOS-Installer.py --auto
4. Wait for completion (2-4 hours)
```

## 📋 Step-by-Step Process

### Phase 1: Preparation (5-10 minutes)
- [ ] Back up all important data
- [ ] Verify 150GB+ free disk space
- [ ] Check hardware compatibility on Dortania
- [ ] Prepare 16GB+ USB drive
- [ ] Document motherboard model for BIOS

### Phase 2: Automated Setup (30-45 minutes)
- [ ] Validate system requirements
- [ ] Install Python dependencies
- [ ] Download OpenCore Simplify
- [ ] Download tools and utilities
- [ ] Download macOS recovery image

### Phase 3: OpenCore Configuration (10-15 minutes)
- [ ] Run OpenCore Simplify
- [ ] Let it scan your hardware
- [ ] Select desired macOS version
- [ ] Allow EFI auto-generation

### Phase 4: USB Preparation (15-20 minutes)
- [ ] Format USB drive with Rufus
- [ ] Copy EFI folder to USB
- [ ] Copy recovery image files to USB
- [ ] Verify files are present

### Phase 5: Disk Setup (10 minutes)
- [ ] Create macOS partition in Windows
- [ ] Allocate 80-120GB space
- [ ] Format as exFAT
- [ ] Label as "macOS"

### Phase 6: BIOS Configuration (5 minutes)
- [ ] Restart computer
- [ ] Enter BIOS (Delete/F2/F10)
- [ ] Disable Secure Boot
- [ ] Set USB as first boot
- [ ] Save and exit

### Phase 7: Installation (60-90 minutes)
- [ ] Boot from USB
- [ ] Select macOS from OpenCore
- [ ] Wait for Recovery to load
- [ ] Format partition in Disk Utility
- [ ] Start macOS installation
- [ ] System reboots multiple times
- [ ] Complete setup wizard

### Phase 8: Post-Installation (15-20 minutes)
- [ ] Mount internal EFI partition
- [ ] Copy EFI from USB to internal drive
- [ ] Eject and unplug USB
- [ ] Boot back to Windows
- [ ] Configure dual-boot in BCD
- [ ] Test both systems

## ⚙️ System Requirements

### Minimum Hardware
- **Processor**: Intel Core i5 / AMD Ryzen 5 (or better)
- **RAM**: 4GB (8GB+ recommended)
- **Disk**: 150GB+ free space on Windows drive
- **USB**: 16GB+ USB 3.0 drive
- **GPU**: Dedicated or integrated (check compatibility)

### Software
- **Windows**: 10 or 11 (Home, Pro, Enterprise)
- **Python**: 3.8 or later
- **Administrator Access**: Required for installation

### Network
- **Internet**: 10GB+ bandwidth for downloads
- **Connection Stability**: Stable connection preferred for long downloads

## 🚀 Quick Commands Reference

```bash
# Validate system only (no downloads)
python macOS-Installer.py --validate

# Interactive menu (recommended for first-time)
python macOS-Installer.py

# Full automation (runs entire process)
python macOS-Installer.py --auto

# PowerShell system check
.\macOS-Installer.ps1

# Reset boot to Windows only (if needed)
bcdedit /set {bootmgr} path \Windows\System32\winload.efi
```

## 📊 Expected Download Sizes

| Item | Size | Time (Mbps) |
|------|------|------------|
| OpenCore Simplify | 50 MB | <1 min |
| USB Tools | 100 MB | <1 min |
| OC Auxiliary Tools | 80 MB | <1 min |
| OpenCore Package | 200 MB | 1 min |
| macOS Recovery Image | 10-15 GB | 10-30 min |
| **TOTAL** | **~11-15 GB** | **15-35 min** |

*Times based on 50 Mbps connection*

## 🎮 Menu Guide

### Main Menu Options

```
1. Validate System Requirements
   ↓ Checks admin, Python, disk space, internet

2. Download & Setup OpenCore Simplify
   ↓ Gets latest OpenCore tools

3. Run OpenCore Simplify
   ↓ Hardware scanning and EFI building
   ↓ Generates optimized EFI folder

4. Download USB Tools
   ↓ Gets USBToolBox for port mapping

5. Download Additional Tools
   ↓ OCAuxiliaryTools, OpenCore, Rufus

6. Download macOS Recovery Image
   ↓ ~11GB macOS installation files

7-12. Installation Guides
   ↓ Step-by-step instructions for manual phases

13. Troubleshooting Guide
   ↓ Common issues and solutions

14. View Installation Log
   ↓ Debug information and timestamps

15. Exit
```

## ⚠️ Critical Warnings

### Data Loss Risk
- ⚠️ Partitioning your disk can erase data
- **BACKUP EVERYTHING** before starting
- Use external drive or cloud storage

### Compatibility
- ⚠️ Not all hardware is supported
- Check Dortania compatibility list first
- Older Intel/AMD CPUs may not work

### Apple Licensing
- ⚠️ Hackintosh violates Apple's EULA
- Use for educational/development only
- Not for commercial purposes

### Stability
- ⚠️ macOS on non-Apple hardware is unsupported
- May have stability and performance issues
- Updates require manual EFI adjustments

## 🔧 Troubleshooting Quick Ref

| Problem | Quick Fix |
|---------|-----------|
| Python not found | Install from Microsoft Store |
| Admin privileges denied | Right-click → Run as Administrator |
| Black screen on boot | Force shutdown → Boot BIOS → Check settings |
| USB not detected | Try different port or USB drive |
| Installation hangs | Check hardware compatibility → Try different USB |
| Wi-Fi missing | Use Ethernet → Add WiFi kext to EFI |
| Can't access Windows | Hold Shift → Select Windows in boot menu |

## 📚 Additional Resources

### Official Documentation
- **Dortania OpenCore Guide**: https://dortania.github.io/OpenCore-Install-Guide/
- **OpenCore Documentation**: https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/Configuration.pdf
- **macOS Compatibility**: https://dortania.github.io/OpenCore-Install-Guide/macos-limits.html

### Community Support
- **Reddit**: https://www.reddit.com/r/hackintosh/
- **GitHub Issues**: https://github.com/acidanthera/OpenCorePkg/issues
- **InsanelyMac Forum**: https://www.insanelymac.com/

### Tools Used
- **OpenCore Simplify**: https://github.com/lzhoang2801/OpCore-Simplify
- **USBToolBox**: https://github.com/USBToolBox/tool
- **OC Auxiliary Tools**: https://github.com/ic005k/OCAuxiliaryTools
- **Rufus**: https://rufus.ie/

## 🔐 Security Notes

- This tool downloads files from GitHub
- Verify downloads against official repositories
- Run antivirus scan before executing
- Only run on personal/test computers
- Never use on production systems

## 📝 Logging and Debugging

All actions are logged automatically in `installation.log`:
- Timestamps for each step
- Download progress
- Error messages
- System information

View logs:
- In app: Select option 14 (View Installation Log)
- File: Check for `installation.log` in working directory

## ✅ Success Indicators

You'll know installation was successful when:
- ✓ macOS boots without intervention
- ✓ All system features work (graphics, audio, networking)
- ✓ OpenCore boot menu appears on every restart
- ✓ Both macOS and Windows can be selected from menu
- ✓ Windows still boots normally when selected

## 🎯 Next Steps After Installation

1. **Install Updates**
   - Check System Settings > Software Update
   - Install any available updates

2. **Configure macOS**
   - Customize settings and preferences
   - Install favorite applications

3. **Optimize Performance**
   - Fine-tune BIOS settings
   - Adjust power management

4. **Address Issues**
   - Check Dortania guide for your hardware
   - Add additional kexts if needed
   - Rebuild EFI if required

## 📞 Getting Help

If you encounter issues:
1. Check the Troubleshooting Guide (Option 13)
2. Review installation logs (Option 14)
3. Visit Dortania guide: dortania.github.io
4. Check r/hackintosh on Reddit
5. Search GitHub issues for similar problems

## 📄 File Structure After Setup

```
Desktop/
├── EFI/                    # OpenCore bootloader
│   ├── Boot/
│   └── OC/
├── OpenCore-Simplify/     # EFI builder tool
├── USBTools/              # USB utilities
│   ├── USBToolBox.exe
│   └── Kexts/
├── MacOSTools/            # Additional tools
│   ├── OCAuxiliaryTools/
│   ├── OpenCorePkg/
│   └── Rufus.exe
└── macOS_Recovery/        # Installation media
    └── com.apple.recovery.boot/

Downloads/
└── (Temporary download files - can be deleted)
```

## 🎓 Educational Value

This toolkit demonstrates:
- Automated system management with Python
- Disk partitioning and boot configuration
- BIOS and firmware interactions
- macOS installation process
- Open-source bootloader usage

## 📋 Checklist Before Starting

- [ ] Windows 10/11 installed and working
- [ ] Administrator access available
- [ ] 150GB+ free disk space
- [ ] External backup of data completed
- [ ] 16GB+ USB drive obtained
- [ ] Python 3.8+ installed or will install
- [ ] Internet connection available
- [ ] Hardware compatibility verified
- [ ] Motherboard manual available
- [ ] 3-4 hours time available

## 🚀 Ready to Begin?

### Start with one of these:
1. **Easy**: Double-click `Start-macOS-Installer.bat`
2. **Normal**: Run `python macOS-Installer.py`
3. **Fast**: Run `python macOS-Installer.py --auto`

---

**Need help?** See README.md for detailed instructions.
**Quick lookup?** See QUICK_REFERENCE.md for common tasks.
**Troubleshooting?** See TROUBLESHOOTING_GUIDE.md for solutions.

**Good luck with your Hackintosh! 🍎**
