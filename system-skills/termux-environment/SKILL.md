---
name: termux-environment
description: Operating system rules, path mapping, capabilities, package management, and Termux API integration for Android Termux environment.
---

# Termux Environment Integration Skill

## Overview
This skill provides authoritative system knowledge and execution rules for operating inside **Termux on Android 16 (aarch64)**. Termux is a Linux terminal emulator environment for Android built on **Android Bionic libc**, not a standard desktop/server GNU/Linux distribution.

## Device & System Profile (Grounded Capabilities)
- **OS Kernel**: Linux 5.15 (aarch64 / ARM64) on Android 16
- **Device Hardware**: Nothing A142
- **Environment Type**: Android Termux (Application sandbox)
- **User ID**: `u0_a337` (Non-root application user)
- **Prefix Path (`$PREFIX`)**: `/data/data/com.termux/files/usr`
- **Home Directory (`$HOME`)**: `/data/data/com.termux/files/home`
- **Default Working Directory**: `/data/data/com.termux/files/home/AGY`
- **Installed Hardware/API Plugins**: `com.termux.api` (v1002), `com.termux.styling` (v1000)

## Critical Execution Rules for Termux

### 1. Shebang & Path Resolution
- **Rule**: Standard Linux shebangs (`#!/usr/bin/env` or `#!/bin/bash`) **do not exist** on Android natively.
- **Requirement**: Always run `termux-fix-shebang <file>` on executable scripts or Node.js packages.
- **Paths**: Binaries reside in `$PREFIX/bin` (`/data/data/com.termux/files/usr/bin`), NOT `/usr/bin` or `/bin`.

### 2. Package Management & Binary Compatibility
- Use `pkg` or `apt` for package installation (`pkg install <package>`).
- Package format is Debian `.deb` compiled against ARM64 Bionic libc.
- **Avoid `termux-glibc`**: Do NOT install `termux-glibc` as it introduces `ld-linux-aarch64.so.1` loader conflicts with native Termux binaries.

### 3. Termux API & Android Integration
The `com.termux.api` plugin is installed on this device (`versionCode: 1002`). You can interact with Android hardware and system services via `termux-api` CLI tools:
- **Clipboard**: `termux-clipboard-get`, `termux-clipboard-set`
- **Notifications**: `termux-notification --title "Title" --content "Message"`
- **Battery**: `termux-battery-status`
- **Toast Messages**: `termux-toast "Message"`
- **Vibration**: `termux-vibrate -d 500`
- **Storage Access**: `termux-setup-storage` (Shared storage mounted at `~/storage`)

### 4. Background Execution & Working Directory
- Android process lifecycle enforces memory management and background killing.
- Working directory MUST remain inside `/data/data/com.termux/files/home/AGY`.
