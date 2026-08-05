# Skill: Recover via EDL

**Filename:** `skill_recover_via_edl.md`
**Category:** Advanced Repair

## Goal
To unbrick a hard-bricked Qualcomm-based device using Emergency Download (EDL) mode.

## Summary
Unbrick hard-bricked Qualcomm device in Emergency Download mode using Firehose programmer and QFIL.

## Inputs
- Device in EDL mode (9008), OEM Firehose programmer (.mbn/.elf), rawprogram.xml, patch.xml, firmware binaries.

## Process
1. Force device into EDL mode via key combination, EDL deep flash cable, or shorting motherboard test points.
2. Verify port detection: Qualcomm HS-USB QDLoader 9008.
3. Launch QFIL (Qualcomm Flash Image Loader) or edl-cli tool.
4. Select Firehose ELF/MBN programmer matching target SoC.
5. Load rawprogram0.xml and patch0.xml partition layouts.
6. Execute low-level flash sequence to reprogram raw storage blocks (UFS/eMMC).
7. Reboot device to fastboot/system once partition tables and bootloader are restored.

## Outputs
- Fully restored bootloader and storage partition map; device rescued from hard brick.

## Prerequisites & Requirements
- **Tools Required:** QPST / QFIL / edl-cli python tool, Firehose programmer, EDL Cable / Tweezers
- **Knowledge Required:** Qualcomm Sahara & Firehose protocol, eMMC/UFS partition tables

## Success Criteria
- Low level flash finishes with status SUCCESS; device boots into Fastboot mode.

## Executable Code Snippets

### CLI EDL Flash Command (edl python tool)
```bash
# Test Sahara handshake
edl printgpt

# Write rawprogram partitions via firehose
edl rawxml rawprogram0.xml patch0.xml . --loader=prog_firehose_ddr.elf

# Reset device to bootloader
edl reset
```
