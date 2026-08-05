# Skill: Implement AIDL HAL Interface

**Filename:** `skill_implement_aidl_hal.md`
**Category:** Kernel And Drivers

## Goal
To design, write, and integrate a custom AIDL HAL service connecting vendor native drivers to Android system services.

## Summary
Create AIDL-defined Hardware Abstraction Layer (HAL) service for Android Treble architecture.

## Inputs
- HAL interface requirement specification (e.g., custom sensor, thermal controller, GPIO interface).

## Process
1. Define interface specification in .aidl file (e.g. IFooHardware.aidl).
2. Configure Android.bp for AIDL generation using aidl_interface module.
3. Implement C++ or Rust binder server class inheriting from BnFooHardware.
4. Write main init service entry point establishing binder service registry with ServiceManager.
5. Add VINTF manifest entry in vendor/etc/vintf/manifest/manifest.xml.
6. Add init.rc file to launch HAL daemon as vendor service.
7. Configure SELinux context for vendor HAL executable and service name.

## Outputs
- Functional AIDL HAL service registered on binder and accessible by Android framework.

## Prerequisites & Requirements
- **Tools Required:** AOSP C++ Toolchain, AIDL compiler, VINTF tools
- **Knowledge Required:** Android Treble architecture, Binder C++ / Rust bindings, VINTF manifest declarations

## Success Criteria
- HAL service registers on ServiceManager, responds to AIDL calls, and passes VTS test suite.

## Executable Code Snippets

### AIDL Interface Definition (IFoo.aidl)
```java
package hardware.custom.foo;

@VintfStability
interface IFoo {
    int getHardwareStatus();
    void setOutputLevel(in int level);
}
```
