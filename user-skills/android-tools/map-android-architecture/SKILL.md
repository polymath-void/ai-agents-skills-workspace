# Skill: Map Android Architecture

**Filename:** `skill_map_android_architecture.md`
**Category:** Core OS Knowledge

## Goal
To analyze and describe the function of any major component of the Android OS, detailing its role and interactions.

## Summary
Analyze and describe the function of any major Android OS component (Zygote, Binder, HAL, ART) detailing role and IPC interactions.

## Inputs
- Component name (e.g., 'Zygote', 'Binder', 'HAL', 'ART', 'SystemServer').

## Process
1. Query AOSP source code documentation for component definition and architecture role.
2. Search for README files and comments within source directories (/frameworks, /system, /hardware).
3. Trace component initialization process during the system boot sequence.
4. Identify key IPC interfaces (Binder/AIDL/HIDL) and function calls between system services.

## Outputs
- Structured architecture breakdown document detailing component role, primary source files, dependencies, and IPC boundaries.

## Prerequisites & Requirements
- **Tools Required:** Access to AOSP source code, Code search tools (OpenGrok, grep, cscope), cuttlefish emulator
- **Knowledge Required:** C/C++, Java/Kotlin, Linux boot process, Binder IPC architecture

## Success Criteria
- Generated architecture description accurately maps component boundaries and provides workable pointers for OS modifications.

## Executable Code Snippets

### Trace Zygote Init in AOSP
```bash
# Inspect Zygote init configuration in system/core
grep -rn "service zygote" system/core/rootdir/init.rc

# Inspect Zygote startup class
cat frameworks/base/core/java/com/android/internal/os/ZygoteInit.java | grep -A 20 "public static void main"
```

### Inspect Binder Driver IPC Stat
```bash
# Dump binder transaction state on device
adb shell cat /d/binder/state
adb shell cat /d/binder/transactions | head -n 30
```
