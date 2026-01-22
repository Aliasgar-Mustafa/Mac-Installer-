#!/usr/bin/env python3
"""
macOS Hackintosh Installation Automation Tool for Windows
Automates the process of installing macOS on Windows via OpenCore
"""

import os
import sys
import subprocess
import shutil
import json
import requests
import zipfile
import time
from pathlib import Path
from datetime import datetime
import ctypes
import platform
import re

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class MacOSInstaller:
    def __init__(self):
        self.desktop_path = Path.home() / "Desktop"
        self.downloads_path = Path.home() / "Downloads"
        self.app_data = {
            'opcore_url': 'https://github.com/lzhoang2801/OpCore-Simplify/archive/refs/heads/main.zip',
            'usbtoolbox_url': 'https://github.com/USBToolBox/tool/releases/download/v1.2.0/USBToolBox.exe',
            'usbtoolbox_kext_url': 'https://github.com/USBToolBox/kext/archive/refs/heads/master.zip',
            'ocat_url': 'https://github.com/ic005k/OCAuxiliaryTools/releases/download/latest/OCAT-Windows.zip',
            'opencore_url': 'https://github.com/acidanthera/OpenCorePkg/releases/download/latest/OpenCorePkg.zip',
            'rufus_url': 'https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5.exe',
        }
        self.installation_log = []

    def log(self, message, level="INFO"):
        """Log messages with timestamps"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.installation_log.append(log_entry)
        print(log_entry)

    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, text):
        """Print formatted header"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}{Colors.ENDC}\n")

    def print_success(self, text):
        """Print success message"""
        print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

    def print_error(self, text):
        """Print error message"""
        print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

    def print_warning(self, text):
        """Print warning message"""
        print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")

    def print_info(self, text):
        """Print info message"""
        print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

    def is_admin(self):
        """Check if running with administrator privileges"""
        try:
            return ctypes.windll.shell.IsUserAnAdmin()
        except:
            return False

    def validate_system(self):
        """Validate system requirements"""
        self.print_header("SYSTEM VALIDATION")
        
        validation_passed = True

        # Check admin privileges
        if not self.is_admin():
            self.print_error("Administrator privileges required!")
            self.print_info("Please run this script as Administrator")
            return False
        self.print_success("Administrator privileges verified")

        # Check OS
        if platform.system() != "Windows":
            self.print_error(f"Windows required. Current OS: {platform.system()}")
            return False
        self.print_success(f"OS: {platform.system()} {platform.release()}")

        # Check Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        if sys.version_info < (3, 8):
            self.print_error(f"Python 3.8+ required. Current: {python_version}")
            return False
        self.print_success(f"Python {python_version} verified")

        # Check disk space
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (1024**3)
        if free_gb < 150:
            self.print_warning(f"Low disk space: {free_gb}GB free (recommended: 150GB+)")
        else:
            self.print_success(f"Disk space: {free_gb}GB available")

        # Check internet connectivity
        if not self.check_internet():
            self.print_warning("Internet connectivity may be unstable")
        else:
            self.print_success("Internet connectivity verified")

        return True

    def check_internet(self):
        """Check internet connectivity"""
        try:
            requests.head("https://github.com", timeout=3)
            return True
        except:
            return False

    def install_dependencies(self):
        """Install required Python packages"""
        self.print_header("INSTALLING DEPENDENCIES")
        
        try:
            import requests
            self.print_success("requests library already installed")
        except ImportError:
            self.print_info("Installing requests library...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
            self.print_success("requests library installed")

    def download_file(self, url, destination, filename=None):
        """Download file from URL with progress"""
        if filename is None:
            filename = url.split('/')[-1]
        
        full_path = Path(destination) / filename
        full_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            self.print_info(f"Downloading {filename}...")
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(full_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size:
                            progress = (downloaded / total_size) * 100
                            print(f"\rProgress: {progress:.1f}%", end='')
            
            print()  # New line after progress
            self.print_success(f"Downloaded: {filename}")
            return full_path
        except Exception as e:
            self.print_error(f"Failed to download {filename}: {str(e)}")
            return None

    def extract_zip(self, zip_path, extract_to):
        """Extract ZIP file"""
        try:
            self.print_info(f"Extracting {zip_path.name}...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            self.print_success(f"Extracted to {extract_to}")
            return True
        except Exception as e:
            self.print_error(f"Failed to extract: {str(e)}")
            return False

    def download_opcore_simplify(self):
        """Download and extract OpenCore Simplify"""
        self.print_header("DOWNLOADING OPENCORE SIMPLIFY")
        
        extract_path = self.desktop_path / "OpenCore-Simplify"
        
        if extract_path.exists():
            self.print_warning(f"OpenCore-Simplify already exists at {extract_path}")
            choice = input("Overwrite? (Y/N): ").upper()
            if choice != 'Y':
                self.print_info("Skipping OpenCore Simplify download")
                return extract_path

        zip_path = self.download_file(
            self.app_data['opcore_url'],
            self.downloads_path,
            "OpCore-Simplify.zip"
        )
        
        if zip_path and self.extract_zip(zip_path, extract_path):
            return extract_path
        return None

    def run_opcore_simplify(self, opcore_path):
        """Guide user through OpenCore Simplify process"""
        self.print_header("RUNNING OPENCORE SIMPLIFY")
        
        bat_file = list(opcore_path.rglob("OpCore-Simplify.bat"))
        if not bat_file:
            self.print_error("OpCore-Simplify.bat not found")
            return False

        bat_path = bat_file[0].parent
        self.print_info(f"Opening command prompt in {bat_path}")
        self.print_info("Follow the on-screen prompts:")
        self.print_info("1. When prompted 'Skip update?': Type N, press Enter")
        self.print_info("2. When prompted 'Skip future updates?': Type Y, press Enter")
        self.print_info("3. Type I to scan hardware")
        self.print_info("4. Type E to list supported macOS versions")
        self.print_info("5. Select your desired macOS version (e.g., 24 for Sequoia)")
        self.print_info("6. Type 6 to build EFI")
        self.print_info("7. Wait for completion and copy EFI folder to Desktop")

        input("\nPress Enter when ready to launch OpenCore Simplify...")
        
        try:
            subprocess.Popen(f'start cmd /k "cd /d {bat_path} && OpCore-Simplify.bat"', shell=True)
            self.print_info("OpenCore Simplify launched. Wait for completion...")
            input("Press Enter after OpenCore Simplify completes and EFI is generated...")
            return True
        except Exception as e:
            self.print_error(f"Failed to launch: {str(e)}")
            return False

    def download_usb_tools(self):
        """Download USBToolBox and Kexts"""
        self.print_header("DOWNLOADING USB TOOLS")
        
        usb_folder = self.desktop_path / "USBTools"
        usb_folder.mkdir(exist_ok=True)

        # Download USBToolBox.exe
        self.download_file(
            self.app_data['usbtoolbox_url'],
            usb_folder,
            "USBToolBox.exe"
        )

        # Download USBToolBox kexts
        kext_zip = self.download_file(
            self.app_data['usbtoolbox_kext_url'],
            usb_folder,
            "USBToolBox-Kexts.zip"
        )

        if kext_zip:
            self.extract_zip(kext_zip, usb_folder / "Kexts")

        return usb_folder

    def download_additional_tools(self):
        """Download OCAuxiliaryTools, OpenCorePkg, and Rufus"""
        self.print_header("DOWNLOADING ADDITIONAL TOOLS")
        
        tools_folder = self.desktop_path / "MacOSTools"
        tools_folder.mkdir(exist_ok=True)

        # OCAuxiliaryTools
        ocat_zip = self.download_file(
            self.app_data['ocat_url'],
            tools_folder,
            "OCAT.zip"
        )
        if ocat_zip:
            self.extract_zip(ocat_zip, tools_folder / "OCAuxiliaryTools")

        # OpenCorePkg
        opencore_zip = self.download_file(
            self.app_data['opencore_url'],
            tools_folder,
            "OpenCorePkg.zip"
        )
        if opencore_zip:
            self.extract_zip(opencore_zip, tools_folder / "OpenCorePkg")

        # Rufus
        self.download_file(
            self.app_data['rufus_url'],
            tools_folder,
            "Rufus.exe"
        )

        return tools_folder

    def download_macrecovery(self, macos_version="sequoia"):
        """Download macOS recovery image"""
        self.print_header("DOWNLOADING MACOS RECOVERY IMAGE")
        
        recovery_folder = self.desktop_path / "macOS_Recovery"
        recovery_folder.mkdir(exist_ok=True)

        macos_versions = {
            'sequoia': ('Mac-7BA5B2DFE22DDD8C', '00000000000KXPG00'),
            'sonoma': ('Mac-937A206F2EE63C01', '00000000000LYNZA00'),
            'ventura': ('Mac-FFE5EF870D7BA81A', '00000000000TYFG0'),
            'monterey': ('Mac-94245B3640C91DA7', '00000000000GMT0A00'),
        }

        if macos_version.lower() not in macos_versions:
            self.print_error(f"Unknown macOS version: {macos_version}")
            return None

        board_id, mlb = macos_versions[macos_version.lower()]
        
        macrecovery_script = list((self.desktop_path / "MacOSTools" / "OpenCorePkg").rglob("macrecovery.py"))
        
        if not macrecovery_script:
            self.print_error("macrecovery.py not found. Download OpenCorePkg first.")
            return None

        script_path = macrecovery_script[0].parent
        
        self.print_info(f"Downloading {macos_version.capitalize()} recovery image...")
        self.print_info("This may take 10-30 minutes depending on internet speed...")
        
        cmd = f'python "{macrecovery_script[0]}" -b {board_id} -m {mlb} download'
        
        try:
            subprocess.run(cmd, shell=True, cwd=str(script_path), check=True)
            self.print_success("Recovery image downloaded")
            return script_path / "com.apple.recovery.boot"
        except Exception as e:
            self.print_error(f"Failed to download recovery image: {str(e)}")
            return None

    def format_usb_guide(self):
        """Guide user through USB formatting"""
        self.print_header("USB FORMATTING GUIDE")
        
        self.print_warning("IMPORTANT: All data on the USB drive will be erased!")
        input("Insert USB drive and press Enter to continue...")
        
        self.print_info("Instructions:")
        self.print_info("1. Open Rufus.exe from Desktop/MacOSTools")
        self.print_info("2. Select your USB drive from the dropdown")
        self.print_info("3. Set these options:")
        self.print_info("   - Boot selection: Non bootable")
        self.print_info("   - Partition scheme: GPT")
        self.print_info("   - File system: FAT32")
        self.print_info("4. Click 'Start' and confirm")
        self.print_info("5. Wait for completion")
        
        input("Press Enter after USB formatting is complete...")
        return True

    def copy_files_to_usb(self):
        """Guide copying files to USB"""
        self.print_header("COPYING FILES TO USB")
        
        self.print_info("You will now copy files to the USB drive")
        self.print_info("1. Open File Explorer")
        self.print_info("2. Navigate to Desktop/EFI folder")
        self.print_info("3. Copy the entire EFI folder to USB root (e.g., E:\\EFI)")
        self.print_info("4. Navigate to macOS_Recovery folder (if you downloaded recovery image)")
        self.print_info("5. Copy contents to USB root next to EFI folder")
        
        input("Press Enter after files are copied to USB...")
        return True

    def partition_disk_guide(self):
        """Guide user through disk partitioning"""
        self.print_header("DISK PARTITIONING GUIDE")
        
        self.print_warning("WARNING: Backup all important data first!")
        self.print_info("You will create a new partition for macOS")
        self.print_info("\nSteps:")
        self.print_info("1. Right-click Start Menu > Disk Management")
        self.print_info("2. Right-click C: drive > Shrink Volume")
        self.print_info("3. Enter size in MB (e.g., 100000 for 100GB)")
        self.print_info("4. Right-click unallocated space > New Simple Volume")
        self.print_info("5. Click 'Next'")
        self.print_info("6. Assign drive letter (e.g., D:) > Next")
        self.print_info("7. Format as exFAT, label 'macOS'")
        self.print_info("8. Click 'Next' > 'Finish'")
        
        input("Press Enter after partition is created...")
        return True

    def bios_configuration_guide(self):
        """Guide BIOS configuration"""
        self.print_header("BIOS CONFIGURATION GUIDE")
        
        self.print_warning("IMPORTANT: BIOS settings vary by motherboard")
        self.print_info("General Steps:")
        self.print_info("1. Restart your PC")
        self.print_info("2. Enter BIOS (Press Delete/F2/F10 during boot - check your motherboard manual)")
        self.print_info("3. Navigate to Boot or Security tab")
        self.print_info("4. DISABLE Secure Boot")
        self.print_info("5. Set USB as first boot device in Boot Order")
        self.print_info("6. Save and Exit (usually F10 then Yes)")
        self.print_info("7. Insert USB drive and restart")
        
        input("Press Enter after BIOS is configured and USB is inserted...")
        return True

    def installation_guide(self):
        """Guide macOS installation process"""
        self.print_header("MACOS INSTALLATION GUIDE")
        
        self.print_info("Your system will now boot from USB")
        self.print_info("\nDuring Installation:")
        self.print_info("1. Select 'macOS Base System' or 'Installer' from OpenCore menu")
        self.print_info("2. Wait for macOS Recovery to load (5-10 minutes)")
        self.print_info("3. Open Disk Utility")
        self.print_info("4. Select the 'macOS' partition (exFAT)")
        self.print_info("5. Click 'Erase'")
        self.print_info("6. Set:")
        self.print_info("   - Name: macOS")
        self.print_info("   - Format: APFS")
        self.print_info("   - Scheme: GUID Partition Map")
        self.print_info("7. Click 'Erase'")
        self.print_info("8. Close Disk Utility")
        self.print_info("9. Select 'Install macOS' (or 'Reinstall macOS')")
        self.print_info("10. Continue > Agree to terms")
        self.print_info("11. Select the formatted 'macOS' partition")
        self.print_info("12. Click 'Install'")
        self.print_info("13. System will restart multiple times (3-4 phases)")
        self.print_info("14. Complete setup wizard (language, region, Wi-Fi, Apple ID)")
        
        input("Press Enter to start installation...")
        return True

    def post_installation_guide(self):
        """Guide post-installation steps"""
        self.print_header("POST-INSTALLATION STEPS")
        
        self.print_info("After macOS boots successfully:")
        self.print_info("\n1. MOUNT EFI PARTITION:")
        self.print_info("   - Open OC Auxiliary Tools (macOS version)")
        self.print_info("   - Go to Disk > Mount EFI")
        self.print_info("   - Select internal drive's EFI partition")
        self.print_info("   - Mount it (will appear in Finder)")
        self.print_info("\n2. COPY EFI FILES:")
        self.print_info("   - From USB EFI, copy 'Boot' and 'OC' folders")
        self.print_info("   - Paste into mounted internal EFI partition")
        self.print_info("\n3. EJECT USB:")
        self.print_info("   - Eject USB from Finder")
        self.print_info("   - Unplug USB drive")
        self.print_info("\n4. BOOT CONFIGURATION:")
        self.print_info("   - Boot back to Windows")
        self.print_info("   - Open Command Prompt (Admin)")
        self.print_info("   - Run: bcdedit /set {bootmgr} path \\efi\\boot\\bootx64.efi")
        self.print_info("   - Restart")
        self.print_info("   - You'll now see OpenCore boot menu on every restart")
        
        input("Press Enter after post-installation is complete...")
        return True

    def troubleshooting_guide(self):
        """Troubleshooting guide"""
        self.print_header("TROUBLESHOOTING GUIDE")
        
        issues = {
            '1': {
                'issue': 'Black screen after boot',
                'steps': [
                    'Force shutdown (hold power button 10 seconds)',
                    'Boot to BIOS (press Delete/F2/F10)',
                    'Verify USB is first boot device',
                    'Reformat macOS partition in Disk Utility',
                    'Re-enable Secure Boot in BIOS',
                ]
            },
            '2': {
                'issue': 'USB not detected',
                'steps': [
                    'Try different USB ports',
                    'Use a different USB drive (8GB+)',
                    'Reformat USB with Rufus',
                    'Check cable connection',
                ]
            },
            '3': {
                'issue': 'Installation stuck/hangs',
                'steps': [
                    'Check hardware compatibility on Dortania.io',
                    'Verify BIOS settings (Secure Boot off, XMP disabled)',
                    'Check for USB port issues',
                    'Try different USB drive',
                ]
            },
            '4': {
                'issue': 'Wi-Fi not working',
                'steps': [
                    'Use Ethernet cable temporarily',
                    'Check Dortania guide for WiFi kext compatibility',
                    'Add WiFi kext to EFI/OC/Kexts before reinstalling',
                ]
            },
            '5': {
                'issue': 'Revert to Windows only',
                'steps': [
                    'Boot to Windows',
                    'Open Command Prompt (Admin)',
                    'Run: bcdedit /set {bootmgr} path \\Windows\\System32\\winload.efi',
                    'Restart',
                ]
            },
        }
        
        print("\nSelect an issue:")
        for key, value in issues.items():
            print(f"{key}. {value['issue']}")
        print("0. Go back")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice in issues:
            issue_data = issues[choice]
            self.print_header(f"Resolving: {issue_data['issue']}")
            for i, step in enumerate(issue_data['steps'], 1):
                print(f"{i}. {step}")
        
        return True

    def show_main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header("MACOS HACKINTOSH INSTALLER FOR WINDOWS")
        
        print("Select an option:\n")
        print("1. Validate System Requirements")
        print("2. Download & Setup OpenCore Simplify")
        print("3. Run OpenCore Simplify (Hardware Scanning & EFI Build)")
        print("4. Download USB Tools (USBToolBox & Kexts)")
        print("5. Download Additional Tools (OCAT, OpenCorePkg, Rufus)")
        print("6. Download macOS Recovery Image")
        print("7. USB Formatting Guide")
        print("8. Copy Files to USB")
        print("9. Disk Partitioning Guide")
        print("10. BIOS Configuration Guide")
        print("11. macOS Installation Guide")
        print("12. Post-Installation Steps")
        print("13. Troubleshooting Guide")
        print("14. View Installation Log")
        print("15. Exit")
        print()

    def show_installation_log(self):
        """Display installation log"""
        self.print_header("INSTALLATION LOG")
        if self.installation_log:
            for entry in self.installation_log:
                print(entry)
        else:
            print("No log entries yet")
        input("\nPress Enter to continue...")

    def run_full_automation(self):
        """Run full automation workflow"""
        self.print_header("FULL AUTOMATION WORKFLOW")
        
        print("This will execute all automated steps in sequence")
        print("Manual steps (BIOS, USB formatting, installation) will require your input\n")
        
        confirm = input("Continue with full automation? (Y/N): ").upper()
        if confirm != 'Y':
            return

        # 1. Validate system
        if not self.validate_system():
            return

        input("Press Enter to continue...")

        # 2. Install dependencies
        self.install_dependencies()

        # 3. Download and setup OpenCore Simplify
        opcore_path = self.download_opcore_simplify()
        if not opcore_path:
            self.print_error("Failed to setup OpenCore Simplify")
            return

        # 4. Run OpenCore Simplify
        if not self.run_opcore_simplify(opcore_path):
            self.print_error("Failed to run OpenCore Simplify")
            return

        # 5. Download USB tools
        self.download_usb_tools()

        # 6. Download additional tools
        self.download_additional_tools()

        # 7. Download macOS recovery
        macos_ver = input("\nEnter macOS version (sequoia/sonoma/ventura/monterey) [default: sequoia]: ").lower().strip()
        if not macos_ver:
            macos_ver = "sequoia"
        
        self.download_macrecovery(macos_ver)

        # 8-11. Manual guides
        self.format_usb_guide()
        self.copy_files_to_usb()
        self.partition_disk_guide()
        self.bios_configuration_guide()
        self.installation_guide()
        self.post_installation_guide()

        self.print_success("AUTOMATION WORKFLOW COMPLETE!")
        self.print_info("Check your Desktop for all tools and files")

    def main(self):
        """Main application loop"""
        try:
            # Check for command line arguments
            if len(sys.argv) > 1:
                if sys.argv[1] == '--auto':
                    self.run_full_automation()
                    return
                elif sys.argv[1] == '--validate':
                    self.validate_system()
                    return
                elif sys.argv[1] == '--help':
                    print("Usage: python macOS-Installer.py [--auto|--validate|--help]")
                    print("  --auto     : Run full automation workflow")
                    print("  --validate : Check system requirements only")
                    print("  --help     : Show this help message")
                    return

            # Interactive menu
            while True:
                self.show_main_menu()
                choice = input("Enter choice (1-15): ").strip()

                if choice == '1':
                    self.validate_system()
                    input("\nPress Enter to continue...")

                elif choice == '2':
                    self.install_dependencies()
                    self.download_opcore_simplify()
                    input("\nPress Enter to continue...")

                elif choice == '3':
                    opcore_path = self.desktop_path / "OpenCore-Simplify"
                    if opcore_path.exists():
                        self.run_opcore_simplify(opcore_path)
                    else:
                        self.print_error("OpenCore-Simplify not found. Download it first (Option 2)")
                    input("\nPress Enter to continue...")

                elif choice == '4':
                    self.download_usb_tools()
                    input("\nPress Enter to continue...")

                elif choice == '5':
                    self.download_additional_tools()
                    input("\nPress Enter to continue...")

                elif choice == '6':
                    macos_ver = input("Enter macOS version (sequoia/sonoma/ventura/monterey) [default: sequoia]: ").lower().strip()
                    if not macos_ver:
                        macos_ver = "sequoia"
                    self.download_macrecovery(macos_ver)
                    input("\nPress Enter to continue...")

                elif choice == '7':
                    self.format_usb_guide()
                    input("\nPress Enter to continue...")

                elif choice == '8':
                    self.copy_files_to_usb()
                    input("\nPress Enter to continue...")

                elif choice == '9':
                    self.partition_disk_guide()
                    input("\nPress Enter to continue...")

                elif choice == '10':
                    self.bios_configuration_guide()
                    input("\nPress Enter to continue...")

                elif choice == '11':
                    self.installation_guide()
                    input("\nPress Enter to continue...")

                elif choice == '12':
                    self.post_installation_guide()
                    input("\nPress Enter to continue...")

                elif choice == '13':
                    self.troubleshooting_guide()
                    input("\nPress Enter to continue...")

                elif choice == '14':
                    self.show_installation_log()

                elif choice == '15':
                    self.print_success("Exiting... Good luck with your macOS installation!")
                    break

                else:
                    self.print_error("Invalid choice. Please try again.")
                    input("Press Enter to continue...")

        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Installation interrupted by user{Colors.ENDC}")
            sys.exit(0)
        except Exception as e:
            self.print_error(f"An error occurred: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    installer = MacOSInstaller()
    installer.main()
