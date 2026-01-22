@echo off
REM macOS Hackintosh Installer for Windows - Batch Wrapper
REM This script launches the Python installer with administrator privileges

setlocal enabledelayedexpansion

REM Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo.
    echo [ERROR] This script requires Administrator privileges!
    echo.
    echo Please right-click this file and select "Run as administrator"
    echo.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo.
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.8+ from https://www.microsoft.com/store/apps/9NRWMJP3717K
    echo.
    pause
    exit /b 1
)

REM Get script directory
set "SCRIPT_DIR=%~dp0"

REM Check if macOS-Installer.py exists
if not exist "%SCRIPT_DIR%macOS-Installer.py" (
    echo.
    echo [ERROR] macOS-Installer.py not found in %SCRIPT_DIR%
    echo.
    pause
    exit /b 1
)

REM Launch Python installer
echo.
echo [INFO] Starting macOS Hackintosh Installer...
echo.

if "%1"=="--auto" (
    python "%SCRIPT_DIR%macOS-Installer.py" --auto
) else if "%1"=="--validate" (
    python "%SCRIPT_DIR%macOS-Installer.py" --validate
) else (
    python "%SCRIPT_DIR%macOS-Installer.py"
)

pause
