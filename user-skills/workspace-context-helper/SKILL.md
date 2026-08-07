---
name: workspace-context-helper
description: Provides workspace context, directory structure metadata, fast code search, multi-ecosystem dependency inspection, Git branch synchronization, Termux system telemetry, and maintenance tools for zero-resource capability discovery.
---

# Workspace Context Helper (`workspace-context-helper`)

A zero-overhead, modular suite of workspace inspection, code navigation, dependency auditing, Git synchronization, Termux runtime telemetry, and cleanup tools designed for autonomous AI agents and developers.

---

## 🛠️ Complete Tools Library (`tools/bin/` & `tools/lib/`)

### 1. `wc-tool-registry` (Meta & Capability Discovery)
- **Purpose**: Zero-resource lookup of all available workspace context tools, flags, and recipes.
- **Usage**: `tools/bin/wc-tool-registry [category|tool_name] [--json]`
- **Example**: `tools/bin/wc-tool-registry`

### 2. `wc-scan` (Directory Scanning & Metadata)
- **Purpose**: Generates a resilient, structured JSON directory tree with aggregate file/dir/size metrics.
- **Usage**: `tools/bin/wc-scan <directory> [output.json]`
- **Example**: `tools/bin/wc-scan .`

### 3. `wc-search` (Context-Aware Fast Code Finder)
- **Purpose**: High-speed symbol and text search automatically skipping build, cache, and noise directories.
- **Usage**: `tools/bin/wc-search <query> [path] [-e ext] [-C lines] [--json]`
- **Example**: `tools/bin/wc-search 'wallpaperTransparency' . -e kt,xml`

### 4. `wc-deps` (Multi-Ecosystem Dependency Inspector)
- **Purpose**: Scans and summarizes dependency manifests across Android (Gradle), Web (NPM), Python, and Rust (Cargo).
- **Usage**: `tools/bin/wc-deps [directory] [--json]`
- **Example**: `tools/bin/wc-deps .`

### 5. `wc-git-sync` (Branch Sync & Working Tree Status)
- **Purpose**: Synchronizes unified branch flows (e.g. `main` <-> `master`) and audits uncommitted working tree changes.
- **Usage**: `tools/bin/wc-git-sync <status|sync> [dir] [src] [target]`
- **Example**: `tools/bin/wc-git-sync sync . main master`

### 6. `wc-termux-env` (Android & Termux Telemetry & Shebangs)
- **Purpose**: Checks `/proc/meminfo` RAM, CPU load, installed compilers (Clang, Python, Java, Git), and auto-fixes shebangs.
- **Usage**: `tools/bin/wc-termux-env <status|toolchains|fix-shebangs> [dir]`
- **Example**: `tools/bin/wc-termux-env status`

### 7. `wc-analyze` (Complexity & Code Quality Framework)
- **Purpose**: Calculates cyclomatic complexity, lines of code (LOC), functions, and classes.
- **Usage**: `tools/bin/wc-analyze <complexity|metrics|summary> [directory]`
- **Example**: `tools/bin/wc-analyze summary .`

### 8. `wc-manage` (Workspace Sanitization & Maintenance)
- **Purpose**: Safely removes build artifacts, temporary logs, or orphan caches with `--dry-run` safety guards.
- **Usage**: `tools/bin/wc-manage sanitize <directory> <pattern1> [pattern2...] [--dry-run]`
- **Example**: `tools/bin/wc-manage sanitize . '*.tmp' '*.bak' --dry-run`

### 9. `wc-monitor` (Workspace Health & Anomaly Auditor)
- **Purpose**: Audits workspace health against complexity limits, large file bounds, and forbidden patterns.
- **Usage**: `tools/bin/wc-monitor <root_path> [config_path]`
- **Example**: `tools/bin/wc-monitor .`
