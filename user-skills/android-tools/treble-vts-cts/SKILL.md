# Skill: Treble & VTS/CTS Verification

**Filename:** `skill_treble_vts_cts.md`
**Category:** Security And Testing

## Goal
To execute and pass Android VTS and CTS compliance tests on custom OEM hardware or GSI system builds.

## Summary
Run Vendor Test Suite (VTS) and Compatibility Test Suite (CTS) to ensure GSI compatibility and Android compliance.

## Inputs
- Android test host with Tradefed installed and connected test device.

## Process
1. Install Generic System Image (GSI) on target hardware to test Treble vendor separation.
2. Launch Trade Federation harness: vts-tradefed or cts-tradefed.
3. Run specific test module: run vts -m VtsHalThermalV2_0TargetTest.
4. Inspect test logs in out/host/vts/vts/results/ for failures.
5. Analyze failed test cases against Android Compatibility Definition Document (CDD).
6. Fix vendor driver HAL compliance or kernel API mismatch.

## Outputs
- 100% passing CTS/VTS test report zip package.

## Prerequisites & Requirements
- **Tools Required:** Tradefed test harness, VTS / CTS packages, Android GSI images
- **Knowledge Required:** Android CDD specifications, Treble architecture, Tradefed test execution

## Success Criteria
- Device achieves 0 test failures on target CTS/VTS modules.

## Executable Code Snippets

### Execute VTS Tradefed Test Module
```bash
# Start Tradefed console
./vts-tradefed

# Run targeted HAL compliance test
vts-tf > run vts -m VtsHalSensorsV2_0TargetTest
```
