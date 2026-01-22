# macOS Hackintosh Installer - Complete Package

## 📦 Package Contents

This folder contains a complete, production-ready terminal-based automation tool for installing macOS on Windows computers.

## 📋 Files Included

### 🔴 MAIN EXECUTABLE FILES

#### 1. **macOS-Installer.py** (RECOMMENDED)
   - **Type**: Python 3 Application
   - **Purpose**: Primary installation automation tool
   - **Features**:
     - Full interactive menu system
     - Automatic downloads from GitHub
     - System validation and compatibility checking
     - Installation progress logging
     - Guided installation steps
     - Built-in troubleshooting
   - **Usage**:
     ```
     python macOS-Installer.py
     python macOS-Installer.py --auto
     python macOS-Installer.py --validate
     ```
   - **Requirements**: Python 3.8+, Administrator access

#### 2. **Start-macOS-Installer.bat** (EASIEST FOR BEGINNERS)
   - **Type**: Windows Batch Script
   - **Purpose**: One-click launcher for macOS-Installer.py
   - **Features**:
     - Automatic admin privilege elevation
     - Python availability check
     - Error handling and reporting
   - **Usage**: 
     - Right-click → "Run as administrator"
     - Or double-click (will prompt for admin)
   - **Best for**: Non-technical users

#### 3. **macOS-Installer.ps1** (ADVANCED/DIAGNOSTIC)
   - **Type**: PowerShell Script
   - **Purpose**: System diagnostic and helper tool
   - **Features**:
     - System information display
     - Disk space analysis
     - USB drive detection
     - Internet connectivity check
     - Boot configuration viewing
     - Hardware assessment
   - **Usage**:
     ```
     .\macOS-Installer.ps1
     .\macOS-Installer.ps1 -Mode auto
     .\macOS-Installer.ps1 -Mode validate
     ```
   - **Requirements**: PowerShell 5.0+, Administrator access

---

### 📚 DOCUMENTATION FILES

#### 4. **README.md** (COMPREHENSIVE GUIDE)
   - Complete installation walkthrough
   - Step-by-step instructions for each phase
   - Hardware requirements and compatibility
   - Advanced options and customization
   - FAQ section
   - Troubleshooting overview
   - **Reading time**: 30-45 minutes
   - **When to use**: First-time installation setup

#### 5. **QUICK_REFERENCE.md** (QUICK LOOKUP)
   - Condensed checklists and tables
   - Menu options at a glance
   - Critical steps summary
   - Timeline and file locations
   - Common issues quick fixes
   - Command reference
   - Boot menu shortcuts
   - **Reading time**: 5-10 minutes
   - **When to use**: During installation for quick lookups

#### 6. **INSTALLATION_SUMMARY.md** (OVERVIEW)
   - Installation overview and methods
   - Phase-by-phase breakdown
   - System requirements summary
   - Expected file sizes and times
   - Success indicators
   - Pre-installation checklist
   - Getting started guide
   - **Reading time**: 15-20 minutes
   - **When to use**: Before starting, to understand process

#### 7. **TROUBLESHOOTING_GUIDE.md** (PROBLEM SOLVING)
   - 15+ common issues with solutions
   - Detailed diagnostic steps
   - Recovery procedures
   - Emergency boot options
   - Useful commands for Windows and macOS
   - When to ask for help
   - Resource links
   - **Reading time**: 20-30 minutes
   - **When to use**: When encountering problems

#### 8. **FILE_MANIFEST.md** (THIS FILE)
   - Complete list of all files
   - Description of each file
   - Quick start guide
   - Installation method comparison
   - File structure after installation
   - What each documentation file covers

---

## 🚀 QUICK START

### Choose Your Installation Method:

#### Method A: Absolutely Easiest (Batch File)
```
1. Right-click "Start-macOS-Installer.bat"
2. Select "Run as administrator"
3. Wait 2-4 hours
4. Done!
```

#### Method B: Interactive Menu (Recommended)
```
1. Open Command Prompt as Administrator
2. cd to this folder
3. python macOS-Installer.py
4. Select options 1-12 in order
5. Done!
```

#### Method C: Full Automation (Hands-off)
```
1. Open Command Prompt as Administrator
2. cd to this folder
3. python macOS-Installer.py --auto
4. Come back in 4 hours
5. Installation complete!
```

#### Method D: Validation Only (Pre-flight Check)
```
1. Open Command Prompt as Administrator
2. cd to this folder
3. python macOS-Installer.py --validate
4. Fix any issues indicated
5. Then try one of the other methods
```

---

## 📊 File Dependency Chart

```
Start-macOS-Installer.bat
    ↓ (launches)
macOS-Installer.py
    ├─ Requires: Python 3.8+
    ├─ Downloads: Tools from GitHub
    ├─ Creates: Desktop/EFI, Desktop/USBTools, etc.
    └─ Logs: installation.log

macOS-Installer.ps1
    ├─ Diagnoses: System configuration
    ├─ Checks: Disk, Internet, USB devices
    └─ Can launch: macOS-Installer.py

Documentation Files (Read-Only Reference)
    ├─ README.md (complete guide)
    ├─ QUICK_REFERENCE.md (lookup tables)
    ├─ INSTALLATION_SUMMARY.md (overview)
    └─ TROUBLESHOOTING_GUIDE.md (problem solving)
```

---

## 💾 File Storage & Organization

### Original Files (In Installation Folder)
```
C:\Users\alias\Downloads\Mac Os\
├── macOS-Installer.py               (Main tool - 45 KB)
├── Start-macOS-Installer.bat        (Launcher - 2 KB)
├── macOS-Installer.ps1              (Diagnostic - 12 KB)
├── README.md                        (Documentation - 18 KB)
├── QUICK_REFERENCE.md               (Quick guide - 8 KB)
├── INSTALLATION_SUMMARY.md          (Overview - 15 KB)
├── TROUBLESHOOTING_GUIDE.md         (Solutions - 22 KB)
└── FILE_MANIFEST.md                 (This file - 8 KB)

Total original files: ~130 KB (very small!)
```

### Generated Files (Created During Installation)
```
Desktop\
├── EFI\                             (Generated by OpenCore Simplify)
│   ├── Boot\
│   └── OC\
├── OpenCore-Simplify\               (Downloaded)
├── USBTools\                        (Downloaded & extracted)
├── MacOSTools\                      (Downloaded & extracted)
└── macOS_Recovery\                  (Downloaded - largest)

Downloads\
└── (Temporary download cache - can be deleted after)

installation.log                     (Created by macOS-Installer.py)
```

---

## 📈 System Requirements Verification

Before running, verify:
- [ ] Windows 10 or 11
- [ ] Administrator access
- [ ] Python 3.8+ installed
- [ ] 150 GB+ free disk space
- [ ] 16 GB+ USB drive
- [ ] Internet connection (10GB+ bandwidth)
- [ ] Hardware compatible (check Dortania)

### Check Your System:
```powershell
# Run as Administrator
python macOS-Installer.py --validate
```

---

## ⏱️ Estimated Timeline

| Phase | Time | Method |
|-------|------|--------|
| Validation | 1 min | Automatic |
| OpenCore Setup | 10 min | Automatic |
| Tool Downloads | 5 min | Automatic |
| Recovery Download | 20-30 min | Automatic |
| USB Preparation | 10 min | Manual guide |
| Disk Partition | 10 min | Manual guide |
| BIOS Config | 5 min | Manual guide |
| Installation | 60-90 min | Semi-automatic |
| Post-Setup | 15 min | Manual guide |
| **TOTAL** | **2-4 hours** | Mixed |

---

## 📞 Help & Support

### For General Questions
→ Read **README.md** (comprehensive guide)

### For Quick Reference During Installation
→ Check **QUICK_REFERENCE.md** (tables & checklists)

### For Understanding the Process
→ Review **INSTALLATION_SUMMARY.md** (overview)

### For Solving Problems
→ Consult **TROUBLESHOOTING_GUIDE.md** (solutions)

### For Online Resources
Visit:
- Dortania OpenCore Guide: https://dortania.github.io/OpenCore-Install-Guide/
- Reddit r/hackintosh: https://www.reddit.com/r/hackintosh/
- GitHub Issues: https://github.com/acidanthera/OpenCorePkg/issues

---

## 🎯 Feature Comparison

### macOS-Installer.py
```
✓ Full automation
✓ Interactive menus
✓ Guided installation
✓ Logging and debugging
✓ Troubleshooting built-in
✓ Multiple languages support
✓ Configuration validation
```

### Start-macOS-Installer.bat
```
✓ One-click launch
✓ Admin privilege check
✓ Python verification
✓ Error reporting
- Less features than .py
- Windows-only
```

### macOS-Installer.ps1
```
✓ System diagnostics
✓ Hardware detection
✓ Boot configuration
✓ No installation needed
- Diagnostic only
- Can launch main tool
```

---

## 🔒 Security & Safety

### What This Tool Does
- ✓ Downloads open-source tools from GitHub
- ✓ Validates system compatibility
- ✓ Creates partition for macOS
- ✓ Modifies boot configuration
- ✓ Logs all activities

### What This Tool Does NOT Do
- ✗ Delete your Windows installation
- ✗ Encrypt or lock your system
- ✗ Send data to external servers
- ✗ Modify system registry (beyond boot config)
- ✗ Run suspicious code

### Safety Recommendations
1. Backup all important data first
2. Test on non-production system if possible
3. Verify downloads match official GitHub
4. Keep antivirus active during downloads
5. Use trusted USB drive
6. Don't modify Python script unless you know Python

---

## ✅ Installation Checklist

### Before Starting
- [ ] Read README.md entirely
- [ ] Verify all system requirements
- [ ] Run: `python macOS-Installer.py --validate`
- [ ] Fix any reported issues
- [ ] Backup important data
- [ ] Have 2-4 hours available
- [ ] Motherboard manual nearby
- [ ] USB drive ready

### During Installation
- [ ] Don't unplug USB during process
- [ ] Keep internet connected
- [ ] Allow multiple computer restarts
- [ ] Don't force shutdown unless instructed
- [ ] Check QUICK_REFERENCE.md for prompts
- [ ] Take notes of any errors

### After Installation
- [ ] Test both macOS and Windows boot
- [ ] Install any pending updates
- [ ] Configure basic settings
- [ ] Check Troubleshooting Guide if issues
- [ ] Keep EFI backup safe

---

## 🆘 Emergency Procedures

### If Installation Fails
```
1. Force restart (hold power 10 sec)
2. Boot to Windows
3. Run: python macOS-Installer.py
4. Review installation.log
5. Check TROUBLESHOOTING_GUIDE.md
6. Consult r/hackintosh with details
```

### If Can't Boot to Windows
```
1. Restart computer
2. At OpenCore menu, select Windows
3. If that doesn't work:
   - Insert Windows installation media
   - Boot from media
   - Use recovery partition
```

### Emergency Reset to Windows Only
```powershell
# Run in Command Prompt (Admin):
bcdedit /set {bootmgr} path \Windows\System32\winload.efi
# Restart computer
# Windows will be only boot option
```

---

## 📝 Documentation Reading Guide

### Recommended Reading Order

**1st Time Users:**
1. This file (FILE_MANIFEST.md) - 10 min
2. INSTALLATION_SUMMARY.md - 20 min
3. QUICK_REFERENCE.md - 10 min
4. README.md - 30-40 min
5. Start installation using one of the methods above

**If You Encounter Issues:**
1. Check QUICK_REFERENCE.md (issue table)
2. Consult TROUBLESHOOTING_GUIDE.md (detailed solutions)
3. Search r/hackintosh with exact error
4. Check installation.log for details

**Advanced Users:**
- Can skip to specific sections of README.md
- Use QUICK_REFERENCE.md as primary guide
- Refer to TROUBLESHOOTING_GUIDE.md for specific issues

---

## 🎓 What You'll Learn

By following this guide, you'll understand:
- How OpenCore bootloader works
- macOS installation process on non-Apple hardware
- Disk partitioning and boot management
- BIOS/UEFI configuration
- Linux/Unix command line basics
- Hackintosh hardware compatibility
- Troubleshooting complex system issues

---

## 📋 List of Files Summary

| File | Type | Size | Purpose |
|------|------|------|---------|
| macOS-Installer.py | Python | 45 KB | Main automation tool |
| Start-macOS-Installer.bat | Batch | 2 KB | Easy launcher |
| macOS-Installer.ps1 | PowerShell | 12 KB | Diagnostic tool |
| README.md | Markdown | 18 KB | Complete guide |
| QUICK_REFERENCE.md | Markdown | 8 KB | Quick lookup |
| INSTALLATION_SUMMARY.md | Markdown | 15 KB | Overview |
| TROUBLESHOOTING_GUIDE.md | Markdown | 22 KB | Problem solving |
| FILE_MANIFEST.md | Markdown | 8 KB | This file |
| **TOTAL** | | **~130 KB** | **Complete package** |

---

## 🚀 Next Steps

1. **Verify Compatibility**
   - Check hardware on Dortania
   - Run: `python macOS-Installer.py --validate`

2. **Read Documentation**
   - Start with README.md
   - Keep QUICK_REFERENCE.md handy

3. **Backup Your Data**
   - External drive or cloud
   - Essential before partitioning

4. **Start Installation**
   - Choose your method (see Quick Start above)
   - Follow the guides
   - Be patient during installation

5. **Troubleshoot if Needed**
   - Consult TROUBLESHOOTING_GUIDE.md
   - Check r/hackintosh
   - Review installation.log

---

## 📞 Final Notes

- **This is educational content** - use responsibly
- **Requires administrator access** - secure your system
- **Can modify boot configuration** - backup first
- **Takes 2-4 hours** - plan your time
- **May void warranties** - read hardware manuals
- **Community support available** - you're not alone!

---

**Ready to install macOS? Start here:**

```bash
# Option 1: Easiest
Double-click: Start-macOS-Installer.bat

# Option 2: Interactive
python macOS-Installer.py

# Option 3: Full automation
python macOS-Installer.py --auto

# Option 4: Validate first
python macOS-Installer.py --validate
```

**Good luck! 🍎**
