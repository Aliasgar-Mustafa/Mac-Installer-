# Troubleshooting Guide - macOS Hackintosh Installation

Comprehensive troubleshooting guide for common issues during macOS installation on Windows.

## 🔴 Critical Issues

### Issue 1: Black Screen After USB Boot

**Symptoms**
- PC boots from USB but shows black screen
- No OpenCore menu appears
- Cursor may blink

**Solutions**

1. **Force Restart & Check BIOS**
   ```powershell
   # Hold power button for 10 seconds to force shutdown
   # Restart and press Delete/F2/F10 to enter BIOS
   ```

2. **Verify Boot Order**
   - In BIOS: Check Boot Order tab
   - USB should be FIRST device
   - Verify UEFI boot mode enabled
   - Disable CSM/Legacy if available

3. **Check BIOS Settings**
   ```
   - Secure Boot: DISABLED
   - XMP/DOCP: DISABLED (can cause issues)
   - UEFI: ENABLED
   - IOMMU/VT-d: ENABLED (optional)
   ```

4. **Reformat USB Drive**
   ```powershell
   # Using Rufus (graphical)
   # Select USB drive
   # Boot selection: Non bootable
   # Partition: GPT
   # File system: FAT32
   # Click Start
   
   # Or using PowerShell (advanced)
   Diskpart
   list disk
   select disk X (where X is USB disk number)
   clean
   create partition primary
   format fs=fat32 label=EFI quick
   ```

5. **Verify EFI Folder Copied**
   ```powershell
   # Check USB drive contains:
   E:\EFI\        (directory)
   E:\Boot\       (directory, if using recovery image)
   
   # If missing, copy from Desktop\EFI
   ```

6. **Update Motherboard BIOS**
   - Visit motherboard manufacturer website
   - Download latest BIOS version
   - Flash using BIOS update tool
   - This often fixes boot issues

---

### Issue 2: USB Drive Not Detected/Not Bootable

**Symptoms**
- USB not visible in boot menu
- BIOS doesn't recognize USB
- "No bootable device found" error

**Solutions**

1. **Try Different USB Ports**
   - Use USB 3.0 ports (blue colored)
   - Avoid USB 2.0 ports (black colored)
   - Avoid front panel USB headers
   - Try all rear USB ports one by one

2. **Try Different USB Drive**
   ```powershell
   # High-quality brands work best:
   # - SanDisk Extreme
   # - Kingston DataTraveler
   # - Samsung USB 3.1
   
   # Format new USB with Rufus:
   # 1. Insert new USB
   # 2. Open Rufus.exe
   # 3. Select new USB drive
   # 4. Boot selection: Non bootable
   # 5. Partition scheme: GPT
   # 6. File system: FAT32
   # 7. Click Start
   ```

3. **Enable USB in BIOS**
   - Restart → Enter BIOS
   - Find Integrated Peripherals or OnBoard Devices
   - Enable USB Controller/USB 3.0
   - Enable XHCI Hand-off (for USB 3.0)
   - Save and exit

4. **Update USB Chipset Drivers (Windows)**
   ```powershell
   # Open Device Manager
   # Find USB controllers
   # Right-click → Update driver
   # Search automatically for updated driver
   ```

5. **Test with Different Computer (if available)**
   - USB working on another computer?
   - If yes, format and try our process again
   - If no, USB drive is faulty

---

### Issue 3: Installation Stuck/Hangs

**Symptoms**
- Installation process stops at certain percentage
- Loading bar not advancing for >5 minutes
- "Still waiting for root device" message

**Solutions**

1. **Check Hardware Compatibility**
   - Visit: https://dortania.github.io/OpenCore-Install-Guide/macos-limits.html
   - Verify your CPU model is supported
   - Check GPU compatibility
   - Search your specific hardware on r/hackintosh

2. **Reset BIOS to Defaults**
   ```
   Restart → Enter BIOS
   Load Setup Defaults or Reset to Factory Settings
   Change only:
   - Secure Boot: Disabled
   - Boot Device: USB First
   Save and Exit
   ```

3. **Disable XMP/DOCP Profile**
   - BIOS → OC/Overclocking Settings
   - Find XMP (Intel) or DOCP (AMD)
   - Set to Disabled or Profile 1
   - This is common cause of hangs
   - Can re-enable after installation

4. **Use Different macOS Version**
   - Try older version (Monterey → Ventura → Sonoma → Sequoia)
   - Some hardware doesn't work on latest
   - Use OpenCore Simplify option to rebuild with different version

5. **Check USB Connection During Installation**
   - Don't move USB drive
   - Don't use USB hub
   - Ensure cable is firmly connected
   - Use powered USB port if available

6. **Force Restart and Try Again**
   ```powershell
   # Hold power button 10 seconds
   # Boot from USB again
   # Installation will resume where it left off
   ```

---

### Issue 4: "Waiting for root device" Error

**Symptoms**
- After OpenCore loads, shows "Waiting for root device"
- Hangs indefinitely
- Never reaches macOS installer

**Solutions**

1. **Missing SATA/NVMe Drivers**
   ```
   This happens when EFI doesn't have drivers for your storage
   Solution:
   1. Boot Windows
   2. Edit EFI/OC/config.plist with OCAT
   3. Verify SATA/NVMe drivers in UEFI/Drivers
   4. Try again
   ```

2. **Storage Device Not Detected in BIOS**
   - Restart → Enter BIOS
   - Check if storage drive appears in boot menu
   - Enable AHCI mode (in BIOS)
   - Update chipset drivers in Windows

3. **Rebuild EFI**
   - Run OpenCore Simplify again
   - Let it auto-detect and rebuild
   - Copy new EFI to USB
   - Try again

4. **Use Different Storage Device (if available)**
   - Try installing to different drive
   - Confirm macOS partition is detected

---

### Issue 5: Kernel Panic at Boot

**Symptoms**
- After OpenCore, system crashes with debug log
- Multiple lines of error text appear
- "Kernel panic" or "Panic CPU:0" message

**Solutions**

1. **Check Log for Specific Error**
   - Look at final lines of panic log
   - Search r/hackintosh for exact error message
   - Helps identify missing driver/kext

2. **Disable Problematic Kext**
   - Edit EFI/OC/config.plist with OCAT
   - Go to Kernel section
   - Find recently added kext
   - Set Enabled=False
   - Rebuild and try

3. **Reduce Kexts to Minimum**
   - Only keep essential kexts:
     - VirtualSMC.kext
     - SMCProcessor.kext
     - SMCSuperIO.kext
     - Lilu.kext
   - Remove others temporarily
   - Add back one at a time if needed

4. **Update/Rebuild EFI**
   - Run OpenCore Simplify option 3
   - Let it rebuild completely
   - Copy new EFI to USB
   - Try again

---

## 🟠 Medium Priority Issues

### Issue 6: Wi-Fi Not Working After Installation

**Symptoms**
- macOS boots successfully
- Wi-Fi menu shows "Not Available"
- Ethernet works fine

**Solutions**

1. **Immediate Workaround**
   ```
   Use Ethernet cable for internet during setup
   This allows software updates and app downloads
   ```

2. **Identify Your WiFi Card**
   - In Windows: Device Manager → Network Adapters
   - Note the exact WiFi card model
   - Examples: Intel AX200, Broadcom BCM94360, etc.

3. **Find Compatible Kext**
   - Visit: https://github.com/acidanthera/Lilu
   - Check Dortania guide for your WiFi card
   - Download appropriate kext
   - Search GitHub for "[Your Card] Hackintosh kext"

4. **Add WiFi Kext to EFI**
   ```
   1. In macOS, mount EFI partition (with OC Auxiliary Tools)
   2. Add WiFi kext to EFI/OC/Kexts
   3. Edit config.plist:
      - Add kext entry
      - Set Enabled=True
      - Set Load=True
   4. Restart macOS
   ```

5. **Check Community Resources**
   - Intel WiFi: https://github.com/OpenIntelWireless/itlwm
   - Broadcom: https://github.com/acidanthera/AirportBrcmFixup
   - Realtek: Check r/hackintosh for model-specific

---

### Issue 7: Audio Not Working

**Symptoms**
- Sound menu shows "No output devices"
- Audio slider disabled
- No sound from speakers/headphones

**Solutions**

1. **Identify Audio Codec**
   ```powershell
   # In Windows, run (as admin):
   wmic path win32_sounddevice get description
   
   # Look for: Realtek, ALC, Conexant, etc.
   # Examples: ALC892, ALC1220, Conexant CX20585
   ```

2. **Install Audio Kext**
   - Download AppleALC.kext from GitHub
   - Download Lilu.kext (dependency)
   - Add both to EFI/OC/Kexts
   - Edit config.plist to enable

3. **Determine Audio Layout ID**
   - Search: "[Your Codec] Hackintosh layout" on GitHub
   - Each audio codec has specific layout IDs
   - Add to config.plist: NVRAM > Add > csr-active-config
   - Format: 07080000 (example)

4. **Test Audio**
   - Restart macOS
   - System Settings > Sound
   - Should show "External Headphones" or "Internal Speakers"

---

### Issue 8: Ethernet Not Working

**Symptoms**
- Ethernet cable connected but not recognized
- No option to connect in System Settings
- "No ethernet available"

**Solutions**

1. **Identify Ethernet Card**
   ```powershell
   # In Windows Device Manager:
   # Network adapters → Find ethernet
   # Examples: Intel I219, Realtek RTL8111, etc.
   ```

2. **Get Correct Kext**
   - Intel: https://github.com/acidanthera/IntelMausi
   - Realtek: https://github.com/Realtek-OpenSource/RTL8111_Driver_linux
   - Apple: Usually built-in for supported models

3. **Install Ethernet Kext**
   - Download appropriate kext for your card
   - Add to EFI/OC/Kexts
   - Edit config.plist to enable
   - Restart macOS

4. **Manual Method (if kext unavailable)**
   ```
   1. Boot into macOS
   2. Connect USB ethernet adapter (usually works out of box)
   3. Download and install appropriate kext
   4. Restart with USB ethernet until native works
   ```

---

### Issue 9: GPU/Graphics Not Working

**Symptoms**
- Resolution stuck at 1024x768 or similar
- Very slow graphics performance
- "Unknown Display" in System Report

**Solutions**

1. **Check Supported GPUs**
   - Visit: https://dortania.github.io/GPU-Buyers-Guide/
   - NVIDIA: Older cards (before RTX) may have limited support
   - AMD: RX 5700 XT, RX 6000 series generally work well
   - Intel iGPU: Usually works, needs specific IGPU patch

2. **Install GPU Drivers (AMD)**
   ```
   For AMD GPUs:
   1. Download WebDriver or use native drivers
   2. May need IOPCI family patches
   3. Usually automatic in newer macOS
   ```

3. **Install GPU Drivers (Intel iGPU)**
   ```
   Requires:
   - Lilu.kext
   - WhateverGreen.kext
   - Specific IGPU patch in config.plist
   - Device-id may need spoofing
   ```

4. **For NVIDIA (Limited Support)**
   ```
   Older NVIDIA cards (GTX 900 series and older):
   - May require web driver
   - Generally not recommended for latest macOS
   - Consider AMD GPU upgrade
   ```

---

### Issue 10: Keyboard/Mouse Not Working at Boot

**Symptoms**
- USB keyboard/mouse not responding in OpenCore
- OpenCore menu not selectable
- Keyboard only works in macOS

**Solutions**

1. **Enable UEFI Keyboard Support in BIOS**
   ```
   BIOS → Integrated Peripherals
   Find: USB Keyboard Support or USB Legacy Support
   Set: Enabled
   ```

2. **Edit config.plist**
   ```
   In OCAT:
   1. Go to Misc section
   2. Find Boot section
   3. Set PickerMode: External (if available)
   4. Or use -v flag to disable GUI
   ```

3. **Try Different USB Ports**
   - Use rear USB ports (blue = USB 3.0)
   - Avoid USB-C or hub connections
   - Try all ports to find working one

4. **Workaround**
   ```
   If only macOS keyboard works:
   1. Use mouse/trackpad to select in OpenCore menu
   2. Or boot Windows first, then restart to OpenCore
   ```

---

## 🟡 Minor Issues

### Issue 11: Bluetooth Not Working

**Solution**: Similar to WiFi. Identify Bluetooth card model and find compatible kext. Install in EFI.

### Issue 12: USB Ports Not All Working

**Solution**: Use USBToolBox to map USB ports. Create USBMap.kext and add to EFI.

### Issue 13: Sleep/Wake Not Working

**Solution**: Disable sleep in System Preferences → Energy Saver, or fix in config.plist power management settings.

### Issue 14: Temperature Monitoring Not Working

**Solution**: Add monitoring kexts like SMCSuperIO.kext or similar for your chipset.

### Issue 15: Performance Issues/Lag

**Solution**: Check Activity Monitor for background processes. Disable unnecessary startup items. Verify XMP/DOCP is disabled in BIOS.

---

## 🟢 Recovery Procedures

### Emergency Boot Back to Windows

```powershell
# Method 1: Select from OpenCore menu
1. Restart computer
2. At OpenCore menu, use arrow keys to select Windows
3. Press Enter

# Method 2: Hold Option/Alt during boot (Mac method)
1. Restart
2. Immediately hold Option key
3. Select Windows drive

# Method 3: Change BIOS boot order
1. Restart, enter BIOS
2. Set Windows boot drive as first device
3. Save and exit
```

### Reset to Windows Only

```powershell
# IMPORTANT: This disables macOS boot!
# Only do this if you want to remove macOS option

# As Administrator:
bcdedit /set {bootmgr} path \Windows\System32\winload.efi

# Verify:
bcdedit /enum

# To re-enable macOS later:
bcdedit /set {bootmgr} path \efi\boot\bootx64.efi
```

### Restore from Backup

```powershell
# If system becomes unbootable:
# 1. Boot from Windows installation media
# 2. Use recovery options
# 3. Or restore from backup created before installation
```

---

## 📊 Diagnostic Commands

### Windows PowerShell (Admin)

```powershell
# Check disk space
Get-Volume | Select-Object DriveLetter, SizeRemaining, Size

# List USB drives
Get-Disk | Where {$_.BusType -eq 'USB'} | Select-Object

# Check boot config
bcdedit /enum

# Check system info
Get-ComputerInfo

# List network adapters
Get-NetAdapter

# Check Windows version
[Environment]::OSVersion.VersionString
```

### macOS Terminal

```bash
# List storage devices
diskutil list

# Check EFI partition
diskutil info /

# View system info
system_profiler SPHardwareDataType

# Check boot logs
log show --predicate 'eventMessage contains "boot"' --last 1h

# Check kernel panics
log show --predicate 'eventType == "logEvent" AND messageType == "Error"'

# List loaded kexts
kextstat | grep -i "your kext name"

# Check OpenCore version
/Volumes/EFI/EFI/OC/OpenCore.efi
```

---

## 📞 Getting Help

### Resources in Order of Priority

1. **Dortania OpenCore Guide**
   - https://dortania.github.io/OpenCore-Install-Guide/
   - Most comprehensive resource
   - Hardware-specific sections

2. **Reddit r/hackintosh**
   - https://www.reddit.com/r/hackintosh/
   - Active community, respond within hours
   - Search first - your issue likely solved

3. **GitHub Issues**
   - https://github.com/acidanthera/
   - Component-specific issues
   - Technical discussions

4. **InsanelyMac Forum**
   - https://www.insanelymac.com/
   - Long-running community
   - Detailed guides by hardware

### When Asking for Help, Provide

1. Exact error message or symptom
2. Your hardware (CPU, GPU, Motherboard model)
3. macOS version you're installing
4. What step you're stuck on
5. What you've already tried
6. System logs (if applicable)

---

## ⚡ Quick Reference Summary

| Issue | Quick Fix |
|-------|-----------|
| Black screen | Disable Secure Boot, verify boot order |
| USB not detected | Try different port, reformat USB |
| Installation stuck | Disable XMP, check hardware compatibility |
| No WiFi | Install WiFi kext, use Ethernet |
| No audio | Install AppleALC.kext + Lilu.kext |
| No ethernet | Install ethernet kext for your card |
| Bad graphics | Update BIOS, install GPU drivers |
| No USB keyboard | Enable USB legacy in BIOS |
| Can't boot | Select Windows from OpenCore menu |
| Want Windows only | bcdedit /set {bootmgr} path \Windows\System32\winload.efi |

---

**Remember**: Most issues are solvable with patience and research!
**Good luck! 🍎**
