---
name: android-flashing-tools
description: Instructions and reference workflows for Android bootloader unlocking, firmware flashing (fastboot/boot.img/vbmeta), ADB shell scripting, and device diagnostics.
---

# Android Bootloader & Firmware Flashing Specialist

This skill provides step-by-step procedures, safety checks, and reference workflows for Android bootloader operations, image flashing, ADB shell scripting, and device diagnostics.

---

## 1. Prerequisites & Tooling
- **ADB**: `adb` (v37.0.1 installed at `~/.local/bin/adb`)
- **Fastboot**: `fastboot` (v37.0.1 installed at `~/.local/bin/fastboot`)
- **Patched Boot Image**: `~/Downloads/magisk_patched-30700_8faB1.img`

---

## 2. Bootloader & Fastboot Workflows

### A. Rebooting to Bootloader/Fastboot
- From ADB: `adb reboot bootloader` or `adb reboot fastboot`
- Verify Fastboot connection: `fastboot devices`

### B. Bootloader Unlocking (Standard AOSP / Pixel / Motorola / OnePlus / Xiaomi)
- Check status: `fastboot getvar unlocked`
- Unlock command: `fastboot flashing unlock` (or `fastboot oem unlock`)

### C. Flashing Magisk Patched Boot Image
1. **Direct Boot Test (Non-Permanent Safe Test)**:
   ```bash
   fastboot boot ~/Downloads/magisk_patched-30700_8faB1.img
   ```
2. **Permanent Flash (A/B Partition Scheme)**:
   ```bash
   fastboot flash boot ~/Downloads/magisk_patched-30700_8faB1.img
   ```
   *(For slot-specific devices: `fastboot flash boot_a ...` or `fastboot flash boot_b ...`)*
3. **Devices with Separate `init_boot` or `vendor_boot`**:
   ```bash
   fastboot flash init_boot ~/Downloads/magisk_patched-30700_8faB1.img
   ```

### D. Disabling AVB / Verity (If Required)
```bash
fastboot flash vbmeta --disable-verity --disable-verification vbmeta.img
```

---

## 3. ADB Shell & Post-Flash Diagnostics

### A. Verify Magisk Root Access
```bash
adb shell "su -c 'id; getenforce; magisk -v'"
```

### B. Capture Logs
- **Logcat**: `adb logcat -d > ~/Downloads/logcat.log`
- **Kernel Dmesg**: `adb shell "su -c dmesg" > ~/Downloads/dmesg.log`

---

## 4. Safety Guardrails
- **Never reboot before verifying partition target** (`boot`, `init_boot`, `vendor_boot`).
- **Keep stock boot image backup** available for recovery.
- **Check active slot**: `fastboot getvar current-slot`.
