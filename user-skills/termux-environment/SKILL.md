---
name: termux-environment
description: Operating system rules, path mapping, capabilities, package management, and Termux API integration for Android Termux environment. Use when running terminal commands, managing packages, or configuring workflows in Android Termux environments.
---

# 🤖 Termux Environment (`termux-environment`)

Operating system rules, path mapping, package management, and Termux API integration for Android Termux environments.

---

## 🎯 When to Use
Use this skill when:
- Executing bash commands, scripts, or package installations within Android Termux
- Configuring storage permissions (`termux-setup-storage`) or Termux API commands
- Troubleshooting environment paths, proot/chroot containers, or CLI dependencies in Termux
- Managing non-interactive Git credentials, whole-environment backups, and shebang repairs

---

## 📋 Workflow Steps

### Step 1: Environment & Storage Verification
- Check Termux environment variables (`$HOME`, `$PREFIX`, `/data/data/com.termux/files/usr`).
- Verify storage access permissions (`termux-setup-storage` mapped to `~/storage`).
- Verify shebang compliance with `termux-fix-shebang` for portable scripts.

### Step 2: Package & Dependency Management
- Use `pkg update` and `pkg install <package>` for package management.
- For Python, Node.js, or C/C++ builds, verify build toolchains (`clang`, `make`, `python`).
- Maintain zero-resource standard (pure Python stdlib + POSIX utilities without heavy pip packages).

### Step 3: API & Automation Execution
- Utilize Termux API commands (`termux-notification`, `termux-clipboard-get`, `termux-battery-status`) when requested.
- Manage background tasks, cron jobs, and persistent terminal sessions cleanly.
- Execute full-environment backups via `agy-backup` or `wc-cloud-backup`.

---

## 🛠️ Required & Associated Workspace Tools
When executing commands, managing Git, or repairing Termux scripts, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-termux-env`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-termux-env) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-termux-env.md)): Audits Termux hardware telemetry, RAM, and automatically fixes shebang paths across scripts.
- [`wc-error-healer`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-error-healer) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-error-healer.md)): Automatically diagnoses and fixes Git 403 authorization errors and non-interactive token issues.
- [`wc-git-sync`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-git-sync) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-git-sync.md)): Synchronizes multi-branch repositories into a unified path (`main`).
- [`wc-agent-probe`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-probe) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-agent-probe.md)): Audits toolchains (clang, python, gh) and environment limits.
- [`wc-cloud-backup`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-cloud-backup) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-cloud-backup.md)): Creates whole-environment disaster recovery backups.
