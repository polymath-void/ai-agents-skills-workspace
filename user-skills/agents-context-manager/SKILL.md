---
name: agents-context-manager
description: Manages AGENTS.md documentation lifecycle, rule enforcement, and skill creation/sync workflow across projects. Use when managing repository rules, updating AGENTS.md context files, or syncing skill specifications across agent workspaces.
---

# 🤖 Agents Context Manager (`agents-context-manager`)

A specialized skill for managing `AGENTS.md` context files, workspace rules, and skill specification sync workflows across AI agent projects.

---

## 🎯 When to Use
Use this skill when:
- Creating or updating `AGENTS.md` rules and operational guidelines in a project repo
- Enforcing project-level context boundaries, system prompts, or tool constraints
- Syncing skill specifications and documentation across agent workspaces
- Managing multi-agent roles, subagent prompt templates, and tool permission boundaries

---

## 📋 Workflow Steps

### Step 1: Context & Rule Audit
- Inspect existing `AGENTS.md` or workspace configuration files.
- Verify role definitions, tool access policies, and project constraints.
- Check tool submission pipeline rules (7-point standard) and zero-resource principles.

### Step 2: Rule Enforcement & Documentation Update
- Update `AGENTS.md` with structured instructions, explicit guardrails, and role boundaries.
- Align prompt templates, subagent dispatch contracts, and citation metadata.
- Document categorized tool registries and dedicated CLI documentation specs (`docs/tools/<tool>.md`).

### Step 3: Skill Sync & Verification
- Ensure project skills are properly indexed and mapped in the repository structure.
- Validate frontmatter metadata and trigger descriptions for consistency using `wc-skill-pack`.
- Synchronize skill directories across active agent CLI paths (`~/.gemini/antigravity-cli/skills/`).

---

## 🛠️ Required & Associated Workspace Tools
When managing agent rules, context lifecycles, and skill syncing, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-skill-pack`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-skill-pack) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-skill-pack.md)): Validates YAML frontmatters, lints skill dependencies, and packages `.skill` archives.
- [`wc-workflow-context`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-workflow-context) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-workflow-context.md)): Isolates and compresses context payloads across agent turns.
- [`wc-tool-registry`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-tool-registry) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-tool-registry.md)): Queries the master tool catalog and use-case matrix.
- [`wc-agent-memory`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-memory) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-agent-memory.md)): Stores persistent rules and session facts in local SQLite memory.
