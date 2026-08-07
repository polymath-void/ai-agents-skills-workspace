---
name: workspace-context-helper
description: Multi-tasking DAG workflows, agent swarm orchestration, token compression, autonomous task execution, atomic code refactoring, self-healing build diagnosis, and zero-resource workspace context tools for AI agents.
---

# Workspace Context Helper (`workspace-context-helper`)

> **Notice**: The tools segment is maintained in its own dedicated library:  
> **[AI-Agents-Workspace-Tools-Library](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library)**

This skill references the full 26-tool ecosystem organized across 9 functional categories for autonomous agents, multi-agent swarms, and background workflows.

---

## 🧭 Multi-Tasking & Agentive Workflow Tools

```bash
# Add tools to PATH
export PATH="$HOME/AI-Agents-Workspace-Tools-Library/bin:$PATH"

# Run DAG Multi-Task Scheduler across worker pools
wc-task-dag workflow.json -w 4

# Multi-Agent Swarm Coordinator
wc-agent-mesh plan "Build Native JNI Buffer"

# Inter-Agent Pub/Sub IPC Message Bus
wc-agent-channel pub "build:done" "SUCCESS" -s "BuilderAgent"
wc-agent-channel sub "build:done" --mark-read

# Token Density & Context Window Optimizer
wc-context-pack build.log crash.log -m 30

# Distributed Mutex Lock (Anti-Race Condition)
wc-resource-lock acquire "gradle_build" -t 60

# Full Tool Registry Index
wc-tool-registry
```

For full architecture, categorization taxonomy, and cited use cases, refer to [`AGENTS.md`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/AGENTS.md) and [`README.md`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/README.md) in the library repository.
