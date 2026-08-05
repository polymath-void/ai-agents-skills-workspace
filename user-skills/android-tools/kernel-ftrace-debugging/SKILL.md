# Skill: Kernel & Driver Debugging with ftrace

**Filename:** `skill_kernel_ftrace_debugging.md`
**Category:** Kernel And Drivers

## Goal
To debug Linux kernel driver panics, stalls, and memory leaks on Android devices.

## Summary
Diagnose Android kernel crashes, driver latency spikes, and I/O bottlenecks using ftrace, pstore, and kasan.

## Inputs
- Kernel panic log, pstore ramoops dump, or performance latency trace request.

## Process
1. Mount tracefs filesystem in adb shell: mount -t tracefs nodev /sys/kernel/tracing.
2. Enable specific kernel function graph tracer or subsystem events (e.g. sched, binder, storage).
3. Reproduce latency or driver issue and extract /sys/kernel/tracing/trace dump.
4. For kernel panics, extract /sys/fs/pstore/console-ramoops dump after reboot.
5. Recompile kernel with KASAN (Kernel Address Sanitizer) enabled to detect out-of-bounds memory accesses.
6. Fix race condition, null dereference, or deadlock in custom device driver C code.

## Outputs
- Detailed trace analysis identifying root cause function and driver patch.

## Prerequisites & Requirements
- **Tools Required:** ftrace / Perfetto, pstore ramoops, KASAN, GDB with vmlinux
- **Knowledge Required:** Linux Kernel Driver model, Concurrency & locking primitives, Memory management

## Success Criteria
- Kernel panic is isolated to exact line in C driver code and verified clean after fix.

## Executable Code Snippets

### Ftrace Kernel Debug Commands
```bash
# Enable function graph tracing for kernel driver
adb shell "echo function_graph > /sys/kernel/tracing/current_tracer"
adb shell "echo 1 > /sys/kernel/tracing/tracing_on"

# Capture trace output
adb shell "cat /sys/kernel/tracing/trace" > kernel_trace.txt
```
