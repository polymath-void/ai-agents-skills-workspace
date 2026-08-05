# Skill: Flash Factory Images

**Filename:** `skill_flash_factory_images.md`
**Category:** Device Manipulation

## Goal
To restore a device to its original software state by flashing official firmware.

## Summary
Restore an Android device to stock factory software by flashing official partition binaries.

## Inputs
- Target device model and OEM factory image zip archive.

## Process
1. Download official stock factory image archive from manufacturer portal.
2. Extract archive contents containing bootloader, radio, image zips, and flash-all scripts.
3. Reboot device into fastboot mode.
4. Execute flash-all.sh (or flash-all.bat).
5. If script fails, manually flash partitions sequentially: fastboot flash bootloader, fastboot reboot-bootloader, fastboot flash radio, fastboot flash boot, fastboot flash super (or system/vendor).
6. Perform factory reset if wiping userdata: fastboot -w reboot.

## Outputs
- Device running clean, stock factory firmware and verified boot state.

## Prerequisites & Requirements
- **Tools Required:** Fastboot tools, OEM Partition Maps
- **Knowledge Required:** Android dynamic partition layout, AVB metadata, Bootloader modes

## Success Criteria
- Device successfully completes initial boot and reaches Android setup wizard.

## Executable Code Snippets

### Manual Partition Flashing Sequence
```bash
# Reboot to bootloader
adb reboot bootloader

# Flash bootloader & radio
fastboot flash bootloader bootloader-<target>.img
fastboot reboot-bootloader
fastboot flash radio radio-<target>.img
fastboot reboot-bootloader

# Flash primary images
fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash super super.img
fastboot -w reboot
```
