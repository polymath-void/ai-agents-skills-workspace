# Skill: Debug SELinux Denials

**Filename:** `skill_debug_selinux_denials.md`
**Category:** System Development

## Goal
To analyze, understand, and write a correct policy to resolve an SELinux denial.

## Summary
Capture, analyze, and craft precise SEPolicy rules (.te files) for AVC denials without compromising Android security.

## Inputs
- Raw logcat output containing 'avc: denied' audit log entries.

## Process
1. Set SELinux into permissive mode temporarily to test functionality: adb shell setenforce 0.
2. Capture complete denial logcat logs: adb logcat -b all | grep 'avc: denied'.
3. Use audit2allow on host to inspect proposed policy rules: audit2allow -i denial_log.txt.
4. Analyze rule intent carefully: Verify if source domain (scontext) legitimately requires privilege on target object (tcontext).
5. Locate the correct SEPolicy file (.te) in device/vendor/sepolicy or system/sepolicy/vendor/.
6. Add minimal necessary allow rule or domain transition rule.
7. Recompile SEPolicy and flash boot/vendor image: m selinux_policy.
8. Re-enable SELinux enforcing mode (setenforce 1) and verify zero regressions.

## Outputs
- Updated .te policy file granting minimal necessary permission while passing CTS/VTS SELinux checks.

## Prerequisites & Requirements
- **Tools Required:** audit2allow tool, AOSP SEPolicy compiler (secilc), ADB logcat
- **Knowledge Required:** SELinux domain labeling, Type enforcement, Neverallow rules, Android Treble SEPolicy architecture

## Success Criteria
- Feature functions flawlessly in SELinux enforcing mode with no new AVC denials.

## Executable Code Snippets

### Analyze AVC Denial & Generate Rule
```bash
# Capture logcat denial
adb logcat -d | grep "avc: denied" > avc_log.txt

# Inspect suggested rule
audit2allow -i avc_log.txt

# Example rule addition in system_server.te or custom daemon file:
# allow hal_foo_default sysfs_leds:file { read open write };
```
