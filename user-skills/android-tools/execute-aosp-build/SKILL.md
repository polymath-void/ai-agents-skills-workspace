# Skill: Execute AOSP Build

**Filename:** `skill_execute_aosp_build.md`
**Category:** Core OS Knowledge

## Goal
To successfully compile the Android Open Source Project (AOSP) from source for a specified target device.

## Summary
Compile full Android Open Source Project (AOSP) system images for hardware targets or Cuttlefish emulator.

## Inputs
- Target device codename (e.g., 'oriole' for Pixel 6, 'aosp_cf_x86_64_phone' for Cuttlefish) and AOSP branch name.

## Process
1. Initialize repository tree: repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r1.
2. Sync source tree: repo sync -j$(nproc) --current-branch --no-tags.
3. Extract proprietary vendor drivers and binary blobs for targeted SoC/hardware.
4. Initialize build environment: source build/envsetup.sh.
5. Select lunch target: lunch aosp_<target>-userdebug.
6. Execute compilation: make -j$(nproc) or m -j$(nproc).
7. Monitor build logs for compiler errors, resolve missing dependencies, and verify artifact output.

## Outputs
- Complete set of flashable system images (boot.img, system.img, vendor.img, product.img, system_ext.img, super.img) in out/target/product/<target>/

## Prerequisites & Requirements
- **Tools Required:** Linux Build Host (Ubuntu 22.04+), Repo tool, Git, JDK 17, Python 3, 250GB+ SSD
- **Knowledge Required:** Git/Repo workflows, GNU Make & Soong/Android.bp, C++ & Java toolchains

## Success Criteria
- Build completes with zero error exit codes, generating flashable system images that boot successfully into Android framework.

## Executable Code Snippets

### AOSP Build Pipeline Sequence
```bash
# 1. Initialize & Sync Repo
repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r50
repo sync -j$(nproc) -c --no-clone-bundle

# 2. Setup environment and lunch target
source build/envsetup.sh
lunch aosp_oriole-userdebug

# 3. Compile full system image
m -j$(nproc)
```
