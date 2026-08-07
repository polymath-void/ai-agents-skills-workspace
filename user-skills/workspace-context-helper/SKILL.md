---
name: workspace-context-helper
description: Autonomous task execution, atomic code refactoring, self-healing build diagnosis, bundle packaging, benchmarking, and zero-resource workspace context tools for AI agents.
---

# Workspace Context Helper & Task Automation Suite (`workspace-context-helper`)

A comprehensive, zero-overhead ecosystem of **14 purpose-built tools** for complete task execution, atomic code refactoring, self-healing builds, bundle packaging, benchmarking, and instant workspace context discovery.

---

## ⚡ Task Completion & Automation Suite

### 1. `wc-task-exec` (Autonomous Multi-Phase Pipeline Runner)
- **Purpose**: Executes full end-to-end task validation (environment check, dependency inspection, health audits, unit test suite) and outputs a formatted receipt.
- **Usage**: `tools/bin/wc-task-exec [task_title] [path] [--json]`
- **Example**: `tools/bin/wc-task-exec "Verify Launcher Build Pipeline" .`

### 2. `wc-code-mod` (Atomic Code Modifier & Refactorer)
- **Purpose**: Batch AST/regex code modifier and import injector across projects with automatic rollback safety backups.
- **Usage**: `tools/bin/wc-code-mod <replace|import> [args...] [-e ext] [-d]`
- **Examples**:
  - `tools/bin/wc-code-mod replace 'oldMethod()' 'newMethod()' . -e kt --dry-run`
  - `tools/bin/wc-code-mod import 'import com.piuu.launcher.utils.*' . -e kt`

### 3. `wc-build-doctor` (Self-Healing Build & Config Doctor)
- **Purpose**: Diagnoses Android/Gradle & script configurations (targetSdk, Compose compiler, 16KB page alignment, shebangs) and applies repairs with `--fix`.
- **Usage**: `tools/bin/wc-build-doctor [path] [--fix]`
- **Example**: `tools/bin/wc-build-doctor ~/repo/Piuu-Unified-Launcher-Android --fix`

### 4. `wc-bundle-packer` (Extension & Release Packager)
- **Purpose**: Compiles `.piuu` extension bundles, validates `manifest.json`, calculates SHA-256 hashes, and verifies bundle integrity.
- **Usage**: `tools/bin/wc-bundle-packer <pack|verify> [args...]`
- **Examples**:
  - `tools/bin/wc-bundle-packer pack ./my-extension dist/my-extension.piuu --name 'Clock Widget'`
  - `tools/bin/wc-bundle-packer verify dist/my-extension.piuu`

### 5. `wc-benchmark` (Performance & Latency Benchmark Auditor)
- **Purpose**: Measures execution duration, peak RAM, and latency thresholds with pass/fail scorecards.
- **Usage**: `tools/bin/wc-benchmark <command...> [-n runs] [-t max_seconds]`
- **Example**: `tools/bin/wc-benchmark ./bin/wc-scan . -n 3 -t 0.5`

---

## 🔍 Workspace Context & Discovery Suite

| Tool | Category | Purpose | Quick Command |
| :--- | :--- | :--- | :--- |
| **`wc-tool-registry`** | Discovery | Instant lookup of all 14 tools and usage recipes. | `wc-tool-registry` |
| **`wc-search`** | Search | Fast symbol/regex finder skipping build/cache noise. | `wc-search 'query' . -e kt` |
| **`wc-deps`** | Manifests | Unified manifest inspector (Gradle, NPM, Python, Rust). | `wc-deps .` |
| **`wc-git-sync`** | Git | Multi-branch synchronizer (`main` ↔ `master`). | `wc-git-sync sync . main master` |
| **`wc-termux-env`** | Telemetry | Memory/CPU stats, verified toolchains, shebang repairs. | `wc-termux-env status` |
| **`wc-scan`** | Architecture| Recursive directory tree mapper with byte statistics. | `wc-scan .` |
| **`wc-analyze`** | Metrics | Cyclomatic complexity and lines-of-code breakdown. | `wc-analyze summary .` |
| **`wc-manage`** | Sanitization| Safe artifact & log cleanup with dry-run protection. | `wc-manage sanitize . '*.tmp' -d` |
| **`wc-monitor`** | Health | Continuous health anomaly & oversized file detector. | `wc-monitor .` |
