# 🔗 Skills-to-Tools Interconnection & Gap Analysis Matrix

This document maps every skill in **`ai-agents-skills-workspace`** to the corresponding specialized tools in **`AI-Agents-Workspace-Tools-Library`**, records the execution chain, and tracks missing tools required for upcoming implementations.

---

## 🗺️ 1. Interconnected Skills $\leftrightarrow$ Tools Mapping Matrix

| Skill Identifier | Category | Active Library Tools Utilized | Missing Tools (Roadmap Backlog) |
| :--- | :--- | :--- | :--- |
| **`workspace-context-helper`** | Agent Workflow | [`wc-task-dag`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-task-dag), [`wc-swarm-dispatch`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-swarm-dispatch), [`wc-workflow-context`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-workflow-context), [`wc-agent-mesh`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-mesh), [`wc-resource-lock`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-resource-lock), [`wc-agent-channel`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-channel), [`wc-context-pack`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-context-pack), [`wc-tool-registry`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-tool-registry) | *None (Fully Supported)* |
| **`piuu-c-native-core`** | POSIX C / JNI | [`wc-contract-check`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-contract-check), [`wc-build-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-build-doctor), [`wc-benchmark`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-benchmark), [`wc-crash-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-crash-doctor) | `wc-elf-align` (16KB page-alignment binary validator) |
| **`piuu-compose-launcher-ui`**| Compose UI | [`wc-scaffold`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-scaffold), [`wc-code-mod`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-code-mod), [`wc-analyze`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-analyze), [`wc-json-query`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-query) | `wc-compose-preview` (CLI AST preview validator) |
| **`piuu-electron-desktop-studio`**| Electron Studio | [`wc-bundle-packer`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-bundle-packer), [`wc-contract-check`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-contract-check), [`wc-json-validate`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-validate), [`wc-deps`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-deps) | `wc-electron-runner` (Headless IPC test harness) |
| **`piuu-pip-side-edge-assist`**| Overlay Assist | [`wc-scaffold`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-scaffold), [`wc-code-mod`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-code-mod), [`wc-crash-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-crash-doctor) | `wc-pip-overlay` (Android overlay permission validator) |
| **`termux-environment`** | System & Termux | [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env), [`wc-error-healer`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-error-healer), [`wc-git-sync`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-git-sync), [`wc-agent-probe`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-probe) | *None (Fully Supported)* |
| **`termux-cloud-backup-assist`**| Cloud Backup | [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env), [`wc-manage`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-manage), [`wc-agent-memory`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-memory) | `wc-rclone-gdrive` (Google Drive OAuth2 sync automation) |
| **`agy-gdrive-backup`** | AGY Cloud Sync | [`wc-agent-memory`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-memory), [`wc-context-pack`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-context-pack), [`wc-manage`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-manage) | `wc-cloud-backup` (Multi-target incremental tarball exporter) |
| **`ai-agent-skill-crafting`** | Meta-Skill | [`wc-json-prompt`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-prompt), [`wc-json-schema`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-schema), [`wc-tool-registry`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-tool-registry), [`wc-search`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-search) | `wc-skill-pack` (Skill bundle linter & YAML validator) |
| **`android-kernel-build`** | System Kernel | [`wc-build-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-build-doctor), [`wc-benchmark`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-benchmark), [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env) | `wc-kernel-builder` (AnyKernel3 compiler & defconfig auditor) |
| **`android-tools`** | Device Management | [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env), [`wc-crash-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-crash-doctor) | `wc-adb-bridge` (Wireless ADB pair, connect & screencap) |
| **`hermes`** | Multi-Agent IPC | [`wc-agent-channel`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-channel), [`wc-json-ndjson`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-ndjson), [`wc-json-filter`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-filter) | `wc-hermes-adapter` (Hermes JSON session translator) |
| **`phone-ssh-connect`** | Remote Access | [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env), [`wc-error-healer`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-error-healer) | `wc-ssh-keygen-helper` (Auto SSH authorized_keys deployer) |
| **`antigravity-support`** | IDE & AGY Engine | [`wc-tool-registry`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-tool-registry), [`wc-agent-probe`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-probe), [`wc-context-pack`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-context-pack) | `wc-agy-session` (AGY transcript JSONL analyzer) |

---

## 📝 2. Missing Tools Registry (Implementation Backlog)

The following **8 missing tools** have been identified through skill chain gap analysis and are scheduled for implementation into `AI-Agents-Workspace-Tools-Library`:

### 1. `wc-rclone-gdrive` / `wc-cloud-backup`
- **Target Category**: System & Cloud Backup (`categories/04_system_runtime/`)
- **Required By**: `agy-gdrive-backup`, `termux-cloud-backup-assist`
- **Purpose**: Zero-loss tarball compression, Google Drive OAuth2 token refresh, remote upload/sync with bandwidth throttling and backup verification receipts.

### 2. `wc-skill-pack`
- **Target Category**: Meta & Discovery (`categories/04_system_runtime/`)
- **Required By**: `ai-agent-skill-crafting`, `skill-creator`
- **Purpose**: Automated linter for `SKILL.md` frontmatter, schema validator for skill YAML tags, broken markdown link detector, and `.skill` zip bundle exporter.

### 3. `wc-kernel-builder`
- **Target Category**: Build & Self-Healing (`categories/04_system_runtime/`)
- **Required By**: `android-kernel-build`
- **Purpose**: AnyKernel3 zip flasher compiler, boot.img unpack/repack tool, and `.config` / `defconfig` verification.

### 4. `wc-adb-bridge`
- **Target Category**: Android & Termux System (`categories/04_system_runtime/`)
- **Required By**: `android-tools`, `phone-ssh-connect`
- **Purpose**: Termux wireless ADB pair/connect, intent dispatcher, package inspector, and headless framebuffer screencap grabber.

### 5. `wc-elf-align`
- **Target Category**: Cross-Language Contracts (`categories/03_code_refactoring/`)
- **Required By**: `piuu-c-native-core`
- **Purpose**: Inspects ELF binary headers of `.so` shared libraries to ensure strict 16KB memory page-alignment compliance on Android 15+.

### 6. `wc-hermes-adapter`
- **Target Category**: Multi-Tasking & Workflows (`categories/02_workflow_swarm/`)
- **Required By**: `hermes`
- **Purpose**: Translates between Hermes agent session formats, MCP JSON schema tool definitions, and Antigravity event buses.

### 7. `wc-electron-runner`
- **Target Category**: Packaging & Release (`categories/04_system_runtime/`)
- **Required By**: `piuu-electron-desktop-studio`
- **Purpose**: Headless Electron IPC contextBridge mock verifier and bundle tester.

### 8. `wc-agy-session`
- **Target Category**: Diagnostics & Workspace (`categories/04_system_runtime/`)
- **Required By**: `antigravity-support`
- **Purpose**: Fast parser for Antigravity conversation JSONL transcripts, extracting tool call frequency and token consumption metrics.

---

## 🔄 3. Next Steps & Implementation Pipeline
1. Interconnect all `SKILL.md` documentation in `skills-workspace/` to cite and execute the 41 active tools.
2. Mirror this gap analysis into `AI-Agents-Workspace-Tools-Library/docs/TOOL_GAP_ANALYSIS.md`.
3. Implement missing tools sequentially starting with `wc-cloud-backup` and `wc-skill-pack`.
