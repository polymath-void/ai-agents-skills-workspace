---
name: android-kernel-build
description: Cross-compilation protocol for custom Android GKI Linux Kernels (arm64/AArch64) using Clang-18 and LLVM on Linux hosts.
category: android-tools
---

# Android Kernel Cross-Compilation Skill (`android-kernel-build`)

This skill details the setup, dependencies, configuration, and compilation commands for cross-compiling an `arm64` custom Android Linux GKI kernel (like Mediatek MT6886 for Nothing Phone (2a)) using host Clang/LLVM toolchains.

---

## 📦 1. Host Build Environment & Dependencies

To cross-compile the kernel on an x86_64 Linux machine (Ubuntu/Debian/Linux Mint), install the compilation utilities and `aarch64` toolchain:

```bash
# Add official LLVM apt repository for LLVM-18
wget -qO- https://apt.llvm.org/llvm-snapshot.gpg.key | sudo tee /etc/apt/trusted.gpg.d/apt.llvm.org.asc > /dev/null
echo "deb http://apt.llvm.org/jammy/ llvm-toolchain-jammy-18 main" | sudo tee /etc/apt/sources.list.d/llvm18.list

# Install packages
sudo apt-get update -y
sudo apt-get install -y \
  bc bison flex libssl-dev libelf-dev build-essential \
  python3 cpio rsync kmod libncurses-dev libdw-dev pahole \
  binutils-aarch64-linux-gnu gcc-aarch64-linux-gnu \
  clang-18 lld-18 llvm-18
```

### Compiler Symlinks Setup
Ensure the Makefile finds the matching compiler bin names:
```bash
for tool in clang clang++ lld ld.lld llvm-ar llvm-nm llvm-objcopy llvm-objdump llvm-strip llvm-readelf llvm-ranlib; do
  BIN=$(which ${tool}-18 2>/dev/null)
  [ -n "$BIN" ] && sudo ln -sf "$BIN" /usr/local/bin/${tool} || true
done
```

---

## 🛠️ 2. Generating Kernel Configuration (`defconfig`)

Generate the default GKI kernel configuration before compilation. Always compile with LLVM environment variables:

```bash
make \
  ARCH=arm64 \
  LLVM=1 \
  LLVM_IAS=1 \
  CC=clang \
  LD=ld.lld \
  AR=llvm-ar \
  NM=llvm-nm \
  OBJCOPY=llvm-objcopy \
  OBJDUMP=llvm-objdump \
  STRIP=llvm-strip \
  CROSS_COMPILE=aarch64-linux-gnu- \
  gki_defconfig
```

---

## ⚙️ 3. Kernel Compilation Commands

Execute compilation using all available CPU threads (`-j$(nproc)`):

```bash
make -j$(nproc) \
  ARCH=arm64 \
  LLVM=1 \
  LLVM_IAS=1 \
  CC=clang \
  LD=ld.lld \
  AR=llvm-ar \
  NM=llvm-nm \
  OBJCOPY=llvm-objcopy \
  OBJDUMP=llvm-objdump \
  STRIP=llvm-strip \
  CROSS_COMPILE=aarch64-linux-gnu- \
  Image Image.gz Image.lz4
```

---

## 🔍 4. Verification and Output Checking

Once the build is complete, verify that the compiled kernel images exist and are valid `aarch64` binaries:

```bash
# Check boots files sizes
ls -lh arch/arm64/boot/Image*

# Verify binary format
file arch/arm64/boot/Image
```
*(Successful output should indicate: `Linux kernel arm64 boot executable Image, ...`)*

---

## 🛠️ Required & Associated Agent Workspace Tools
When building kernels or auditing toolchains, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-build-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-build-doctor) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-build-doctor.md)): Verifies compiler flags and LLVM toolchain configurations.
- [`wc-benchmark`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-benchmark) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-benchmark.md)): Measures compilation duration, CPU load, and thread efficiency.
- [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-termux-env.md)): Audits hardware memory bounds before launching multithreaded builds.
- *Upcoming Tool Note*: `wc-kernel-builder` (AnyKernel3 compiler and boot.img repackager) is scheduled for implementation.

