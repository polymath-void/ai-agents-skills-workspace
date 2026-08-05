# Skill: Decompile APK

**Filename:** `skill_decompile_apk.md`
**Category:** Reverse Engineering

## Goal
To decompile an Android Application Package (APK) to analyze its source code and resources.

## Summary
Decompile Android APK using Apktool and JADX to reconstruct AndroidManifest.xml, resources, Smali assembly, and Java code.

## Inputs
- Target .apk file.

## Process
1. Decode APK assets, resources, and manifest using Apktool: apktool d app.apk -o output_dir.
2. Extract classes.dex file(s) from APK container.
3. Convert DEX bytecode to Java bytecode JAR using dex2jar: d2j-dex2jar classes.dex -o classes.jar.
4. Open JAR file in JADX-GUI or JD-GUI to inspect reconstructed Java source code.
5. Analyze AndroidManifest.xml for exported activities, broadcast receivers, services, content providers, and permissions.
6. Inspect Smali code in output_dir/smali/ for reverse-engineering or instrumentation.

## Outputs
- Readable directory containing AndroidManifest.xml, res/ resources, Smali code, and reconstructed Java/Kotlin sources.

## Prerequisites & Requirements
- **Tools Required:** Apktool, JADX / JADX-GUI, dex2jar, JD-GUI
- **Knowledge Required:** DEX Bytecode format, Smali syntax, Android App security model

## Success Criteria
- Successfully views Java source code and XML resources without decompiler crash.

## Executable Code Snippets

### Apktool & JADX CLI Decompilation
```bash
# Decode resources and Smali
apktool d target_app.apk -o target_decompiled

# Decompile directly to Java source tree with JADX
jadx -d source_out target_app.apk
```
