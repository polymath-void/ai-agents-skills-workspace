---
name: workspace-context-helper
description: Autonomous task execution, atomic code refactoring, self-healing build diagnosis, bundle packaging, benchmarking, and zero-resource workspace context tools for AI agents.
---

# Workspace Context Helper (`workspace-context-helper`)

> **Notice**: The tools segment has been migrated to its own dedicated library:  
> **[AI-Agents-Workspace-Tools-Library](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library)**

This skill references the full 18-tool ecosystem organized across 7 functional categories for autonomous agents.

---

## 🧭 Quick Access to Dedicated Tools

To invoke any tool from the dedicated repository:

```bash
# Add tools to PATH
export PATH="$HOME/AI-Agents-Workspace-Tools-Library/bin:$PATH"

# Run tool capability registry
wc-tool-registry

# Execute an end-to-end task verification
wc-task-exec "Verify Launcher Build" ~/repo/Piuu-Unified-Launcher-Android

# Check cross-language JNI/IPC contracts
wc-contract-check ~/repo/Piuu-Unified-Launcher-Android
```

For full architecture, categorization taxonomy, and cited use cases, refer to [`AGENTS.md`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/AGENTS.md) and [`README.md`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/README.md) in the library repository.
