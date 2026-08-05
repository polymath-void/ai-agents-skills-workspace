# Skill: Frida System Server & Framework Tracing

**Filename:** `skill_frida_tracing.md`
**Category:** Reverse Engineering

## Goal
To inspect internal runtime states and hook method invocations within Android system_server or app processes.

## Summary
Dynamically instrument Android framework services and system_server using Frida hooks.

## Inputs
- Target process name or PID, JavaScript hook script.

## Process
1. Push frida-server binary to device: adb push frida-server /data/local/tmp/.
2. Grant root execution permissions: adb shell chmod 755 /data/local/tmp/frida-server.
3. Launch frida-server in background.
4. Write Frida JavaScript hooking script intercepting targeted Java or Native functions.
5. Attach Frida to system_server or app process: frida -U -n system_server -l hook.js.
6. Analyze live parameters, return values, and call stacks.

## Outputs
- Real-time runtime state dump and execution trace.

## Prerequisites & Requirements
- **Tools Required:** Frida-server, Frida-tools CLI, JavaScript
- **Knowledge Required:** Android Runtime (ART) internals, JNI interface, Dynamic instrumentation

## Success Criteria
- Frida attaches without crash, intercepting targeted methods and logging parameters.

## Executable Code Snippets

### Frida Hook for ActivityManagerService
```javascript
Java.perform(function () {
    var AMS = Java.use("com.android.server.am.ActivityManagerService");
    AMS.startActivity.implementation = function () {
        console.log("[+] Intercepted startActivity invocation!");
        return this.startActivity.apply(this, arguments);
    };
});
```
