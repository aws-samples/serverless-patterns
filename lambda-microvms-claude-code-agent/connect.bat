@echo off
REM connect.bat — Open an interactive shell into the Lambda MicroVM (Windows)
REM
REM Delegates to connect.sh via Git Bash for proper terminal handling.
REM Requires: Git Bash, websocat, AWS CLI
REM
REM Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
REM SPDX-License-Identifier: MIT-0

setlocal

if "%~1"=="" (
    echo Usage: %~nx0 ^<microvm-id^>
    exit /b 1
)

REM Find Git Bash (not WSL)
set "GIT_BASH=%ProgramFiles%\Git\bin\bash.exe"
if not exist "%GIT_BASH%" set "GIT_BASH=%ProgramFiles(x86)%\Git\bin\bash.exe"
if not exist "%GIT_BASH%" (
    echo ERROR: Git Bash not found. Install Git for Windows:
    echo   https://git-scm.com/download/win
    exit /b 1
)

REM Delegate to connect.sh (handles websocat + raw terminal properly)
"%GIT_BASH%" "%~dp0connect.sh" %*
