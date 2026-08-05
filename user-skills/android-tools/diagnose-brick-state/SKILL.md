# Skill: Diagnose Brick State

**Filename:** `skill_diagnose_brick_state.md`
**Category:** Advanced Repair

## Goal
To accurately determine if a non-booting device is soft-bricked or hard-bricked.

## Summary
Differentiate between soft brick (bootloop, fastboot accessible) and hard brick (EDL QDLoader 9008, MTK Preloader).

## Inputs
- Non-booting hardware symptoms, USB device IDs, key combo reactions.

## Process
1. Attempt hardware fastboot combination (Power + Vol Down). If fastboot loads -> Soft Brick.
2. Attempt recovery combination (Power + Vol Up). If recovery loads -> Soft Brick.
3. Connect device to PC via USB and observe host hardware enumeration.
4. Check device manager / lsusb: If detected as 'Qualcomm HS-USB QDLoader 9008' -> Hard Brick (Qualcomm EDL).
5. If detected as 'MediaTek Preloader' / 'MTK USB Port' -> Hard Brick (MTK Preloader).
6. If 0mA current drawn and zero USB enumeration -> Hardware Power/Battery Failure.

## Outputs
- Accurate diagnosis: Soft Brick, Hard Brick (EDL), Hard Brick (MTK), or Hardware Failure.

## Prerequisites & Requirements
- **Tools Required:** lsusb / Windows Device Manager, USB Ammeter, Platform Tools
- **Knowledge Required:** Emergency Bootloader modes (EDL, BROM, Download Mode), USB Vendor/Product IDs

## Success Criteria
- Correctly identifies device fault state to select safe recovery path.

## Executable Code Snippets

### Check USB Connection State on Linux
```bash
# Inspect USB device enumeration for emergency drivers
lsusb | grep -E "05c6|0e8d|18d1"

# Output examples:
# Bus 001 Device 012: ID 05c6:9008 Qualcomm, Inc. Qualcomm HS-USB QDLoader 9008
# Bus 001 Device 014: ID 0e8d:2000 MediaTek Inc. MT65xx Preloader
```
