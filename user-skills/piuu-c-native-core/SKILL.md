---
name: piuu-c-native-core
description: POSIX C native shared library integration (libpiuu_core.so), 16KB page-alignment, zero-copy JNI memory arena buffers, and SELinux fallback system telemetry parsing for Android launchers.
---

# ⚙️ Piuu C Native Shared Core Skill (`piuu-c-native-core`)

This skill documents high-performance C native core engineering, JNI memory management, and Android 16 (API Level 36) 16KB memory alignment for Android launchers.

---

## 🏛️ 1. CMake 16KB Page-Alignment Linker Flags

Android 16 requires 64-bit native shared libraries (`.so`) to be compiled with a 16KB max page size boundary to prevent runtime `SIGSEGV` or `dlopen` failures on newer hardware.

In `CMakeLists.txt`:
```cmake
cmake_minimum_required(VERSION 3.22.1)
project("piuu_core" C)

# Enforce 16 KB max page size linker flag
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,-z,max-page-size=16384")

add_library(piuu_core SHARED piuu_core.c)
find_library(log-lib log)
target_link_libraries(piuu_core ${log-lib})
```

In `app/build.gradle`:
```groovy
externalNativeBuild {
    cmake {
        cFlags "-O3 -Wall -DANDROID_SUPPORT_FLEXIBLE_PAGE_SIZES=ON"
        abiFilters 'arm64-v8a', 'x86_64', 'armeabi-v7a'
    }
}
```

---

## 🧠 2. Zero-Copy JNI Direct Buffer Allocation

To share large extension datasets, icon bitmaps, or custom card render streams between C native memory and Kotlin Jetpack Compose without Java Garbage Collection (GC) latency spikes:

### C Native Implementation (`piuu_core.c`):
```c
JNIEXPORT jobject JNICALL
Java_com_piuu_launcher_repository_LibC_allocateArena(JNIEnv *env, jobject thiz, jint size) {
    void* buffer = malloc((size_t)size);
    if (!buffer) return NULL;
    memset(buffer, 0, (size_t)size);
    return (*env)->NewDirectByteBuffer(env, buffer, size);
}
```

### Kotlin JNI Bridge (`LibC.kt`):
```kotlin
object LibC {
    init {
        System.loadLibrary("piuu_core")
    }

    @JvmStatic private external fun allocateArena(size: Int): java.nio.ByteBuffer?
}
```

---

## 📊 3. POSIX `/proc` System Telemetry Engine

High-frequency telemetry polling (CPU load %, memory usage, thread count, PID signal delivery) using native C sys calls:

```c
JNIEXPORT jdouble JNICALL
Java_com_piuu_launcher_repository_LibC_nativeGetCpuUsage(JNIEnv* env, jobject thiz) {
    FILE* file = fopen("/proc/stat", "r");
    if (!file) return -1.0;
    // Parse CPU ticks and return CPU load percentage
}
```

---

## 🛠️ Required & Associated Agent Workspace Tools
When executing POSIX C native core modifications, activate these specialized tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-contract-check`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-contract-check) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-contract-check.md)): Audits and verifies JNI `external fun` signatures in Kotlin against exported C functions in `piuu_core.c`.
- [`wc-build-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-build-doctor) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-build-doctor.md)): Verifies 16KB max-page-size linker flags in `CMakeLists.txt` and `build.gradle`.
- [`wc-benchmark`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-benchmark) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-benchmark.md)): Measures execution latency of zero-copy buffer allocations and CPU telemetry parsing.
- [`wc-crash-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-crash-doctor) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-crash-doctor.md)): Analyzes native `SIGSEGV` or `dlopen` stacktraces.
- *Upcoming Tool Note*: `wc-elf-align` (ELF binary 16KB memory page-alignment validator) is currently in the implementation roadmap.

