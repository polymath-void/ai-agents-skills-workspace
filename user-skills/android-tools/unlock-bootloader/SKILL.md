# Skill: Unlock Bootloader

**Filename:** `skill_unlock_bootloader.md`
**Category:** Device Manipulation

## Goal
To unlock the bootloader of a supported Android device to allow flashing of custom images.

## Summary
Enable OEM unlock and issue fastboot protocols to unlock bootloader for custom system flashing.

## Inputs
- Connected Android device with USB debugging enabled.

## Process
1. Enable 'OEM unlocking' in Android Developer Options.
2. Reboot device into bootloader mode via adb reboot bootloader.
3. Verify fastboot communication: fastboot devices.
4. Execute standard unlock command: fastboot flashing unlock (or fastboot oem unlock).
5. For OEM specific locked devices, query manufacturer key portal for device unlock token.
6. Confirm bootloader unlock prompt using physical volume keys on hardware device.

## Outputs
- Device with bootloader state reported as UNLOCKED (fastboot getvar unlocked = yes).

## Prerequisites & Requirements
- **Tools Required:** ADB & Fastboot platform-tools, OEM USB Drivers
- **Knowledge Required:** Fastboot protocol, Android security model & Verified Boot (AVB)

## Success Criteria
- Command fastboot getvar unlocked returns 'yes'.

## Executable Code Snippets

### Fastboot Unlock Sequence
```bash
# Boot into bootloader
adb reboot bootloader

# Check connection
fastboot devices

# Unlock bootloader
fastboot flashing unlock

# Verify unlock variable
fastboot getvar unlocked
```
