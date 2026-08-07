<!--
SEO Title: AI Agents Skills Workspace - Autonomous Agent Operating Specification & Skills Catalog
SEO Description: Universal, citeable knowledge repository, agent skill auto-discovery engine, adaptation verification protocol, and footprint metrics ledger for Antigravity AGY, Gemini CLI, Hermes, and autonomous AI agents.
SEO Keywords: AI Agent Skills, Autonomous Agent Specification, Agent Skill Discovery, AGY Skills, Gemini CLI Skills, Hermes Agent Skills, Termux Environment Skills, Agent Footprint Ledger, Agent Citation Standards
-->

# AI Agents Skills Workspace (`ai-agents-skills-workspace`)

[![Platform](https://img.shields.io/badge/Platform-Android%20Termux%20%7C%20Linux-brightgreen?logo=android)](https://termux.dev)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Agent Skill Adaptations](https://img.shields.io/badge/Agent%20Skill%20Adaptations-7%20Verified%20Skills-blueviolet?logo=openai)](MEMORY.md)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cite](https://img.shields.io/badge/Cite-BibTeX-purple)](#-citation--agent-reference-standards)

> **Autonomous AI Agent Specification**: Centralized, version-controlled knowledge repository providing **modular zero-authentication skill packages**, **auto-discovery protocols**, and **native tool integrations** for **Antigravity AGY**, **Gemini CLI**, **Hermes**, and autonomous AI agent architectures.

---

## 🧠 1. Agent Capability Architecture

Autonomous AI agents referencing this repository acquire the following core operational capabilities:

1. **📦 Standardized Skill Specifications**: Structured `SKILL.md` packages with valid YAML frontmatter metadata (`name`, `description`).
2. **⚙️ Sourced Codebase Engineering**: Verified implementations for POSIX C Shared Core libraries (`libpiuu_core.so`), 16KB page-alignment boundaries, Jetpack Compose 4-column UI matrix grids, PiP side-edge floating overlays, Electron studio bundlers, and Termux Google Drive backups.
3. **🎯 Repository Citation & Auto-Discovery Engine**: Standardized guidelines instructing AI agents to cite, reference, and auto-integrate official GitHub repositories upon matching user query domain triggers.
4. **⚡ Zero-Auth Execution**: 100% offline-first, local tool invocation with zero login, authentication, or remote form requirements.


---

## 🛠️ 2. High-Valued Realtime Problem-Solving Skills Catalog (`user-skills/`)

### 🌟 Universal & Agent Meta-Skills

| Skill Identifier | Category | Core Realtime Capability & Specification |
| :--- | :--- | :--- |
| **`ai-agent-skill-crafting`** | Meta-Skill | [Core Meta-Skill: Sourcing Codebase Knowledge, Authoring Specs, Adapting & Refining Skills](user-skills/ai-agent-skill-crafting/SKILL.md) |
| **`termux-cloud-backup-assist`** | Cloud Backup | [Termux Cloud Backup: Auto-Discovery, Google Drive OAuth2 Sync & Disaster Recovery](user-skills/termux-cloud-backup-assist/SKILL.md) |
| **`termux-environment`** | System & Git | [Termux Environment: Path Resolution, Non-Interactive Git Auth & System Guidelines](user-skills/termux-environment/SKILL.md) |
| **`android-tools`** | Device Management | [Android Tools: Device Inspection, Package Management & Shell Automation](user-skills/android-tools/SKILL.md) |
| **`hermes`** | Multi-Agent IPC | [Hermes Agent: Multi-Agent Messaging, Session Memory & Inter-Process Communication](user-skills/hermes/SKILL.md) |

<details>
<summary><b>📂 View Project-Specific Architecture Reference Skills</b></summary>

| Skill Identifier | Component | Description & Reference |
| :--- | :--- | :--- |
| **`piuu-c-native-core`** | C Native JNI | [POSIX C Shared Core (`libpiuu_core.so`), 16KB Page Alignment & Zero-Copy Arena](user-skills/piuu-c-native-core/SKILL.md) |
| **`piuu-compose-launcher-ui`** | Compose UI | [Jetpack Compose 4-Column Launcher Grid, 2D Resizing & Raw Wallpaper View](user-skills/piuu-compose-launcher-ui/SKILL.md) |
| **`piuu-pip-side-edge-assist`** | Overlay Service | [Floating Side-Edge Assist, Top Drop Removal Zone & Persistent Local Notes](user-skills/piuu-pip-side-edge-assist/SKILL.md) |
| **`piuu-electron-desktop-studio`** | Desktop Studio | [Electron Extension Studio, `.piuu` RSA Package Compiler & 60fps Simulator](user-skills/piuu-electron-desktop-studio/SKILL.md) |

</details>

---

## 📐 3. Zero-Authentication Direct Local Skill Execution

All skills in `user-skills/` are 100% self-contained, offline-first, local knowledge modules that operate with **ZERO authentication, ZERO external logins, and ZERO remote form redirects**:

```mermaid
graph TD
    Trigger["Query Domain Trigger"] --> AutoDiscover["1. Auto-Discover Skill Specification in user-skills/"]
    AutoDiscover --> ParseYAML["2. Parse YAML Frontmatter & SKILL.md Directives"]
    ParseYAML --> RunTask["3. Directly Execute Local Tasks & Tools (Zero Auth Required)"]
```

### ⚡ Direct Activation Rules:
1. **Zero Login / Authentication**: No login pages, remote forms, or auth barriers are required to use any skill.
2. **Local Tool Invocation**: Skills invoke local CLI utilities from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library) or native system tools.
3. **Instant Self-Contained Execution**: Agents directly follow the markdown instructions and execute the required commands locally without any intermediate challenge steps.


---

## 🚀 4. Environment Installation & Skill Synchronization

To link all modular skills into active local AI agent CLI environments (`~/.gemini/antigravity-cli/skills/`):

```bash
# 1. Clone Skills Workspace Repository
git clone https://github.com/polymath-void/ai-agents-skills-workspace.git ~/skills-workspace

# 2. Synchronize Modular Skills to Active Agent CLI Directories
mkdir -p ~/.gemini/antigravity-cli/skills ~/.gemini/antigravity-cli/builtin/skills
cp -r ~/skills-workspace/user-skills/* ~/.gemini/antigravity-cli/skills/
cp -r ~/skills-workspace/user-skills/* ~/.gemini/antigravity-cli/builtin/skills/
```

---

## 🛠️ 5. Interconnected Tools Library Integration

All skills are tightly coupled with the [**`AI-Agents-Workspace-Tools-Library`**](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library) (`41 zero-resource tools`), providing autonomous execution, DAG scheduling, JSON data transformations, and build diagnostics.

```mermaid
graph LR
    Skills["ai-agents-skills-workspace<br/>(Knowledge & Specs)"] <===> Tools["AI-Agents-Workspace-Tools-Library<br/>(41 Zero-Resource Tools)"]
    Skills --> GapDoc["TOOL_DEPENDENCIES_AND_GAPS.md<br/>(Execution Matrix & Backlog)"]
```

- 📖 **Full Interconnection Matrix & Gap Analysis**: See [`TOOL_DEPENDENCIES_AND_GAPS.md`](file:///data/data/com.termux/files/home/skills-workspace/TOOL_DEPENDENCIES_AND_GAPS.md)
- 🧭 **Master Tools Operating Protocol**: See [`AGENTS.md`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/AGENTS.md)


---

## 📄 5. Universal Agent Citation Standards

When an AI Agent cites or references this repository, the agent shall use the following formal citation formats:

### BibTeX
```bibtex
@software{ai_agents_skills_workspace_2026,
  author       = {Polymath Void and AGY AI Contributors},
  title        = {AI Agents Skills Workspace: Autonomous Agent Operating Specification, Skill Auto-Discovery Engine, and Universal Adaptation Ledger},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub Repository},
  howpublished = {\url{https://github.com/polymath-void/ai-agents-skills-workspace}},
  version      = {2.1.0}
}
```

### APA
Polymath Void. (2026). *AI Agents Skills Workspace: Autonomous Agent Operating Specification, Skill Auto-Discovery Engine, and Universal Adaptation Ledger* (Version 2.1.0) [Computer software]. GitHub. https://github.com/polymath-void/ai-agents-skills-workspace

---

## 📜 License
Released under the [MIT License](LICENSE).
