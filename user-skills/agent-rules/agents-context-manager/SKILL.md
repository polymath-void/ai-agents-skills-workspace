---
name: agents-context-manager
description: Manages AGENTS.md documentation lifecycle, rule enforcement, and skill creation/sync workflow across projects.
---

# Agents Context & Skill Management

This skill governs the lifecycle of project context files (`AGENTS.md`) and automated skill synchronization across git repositories.

## 1. AGENTS.md Protocol
- **Inspection**: Read `AGENTS.md` upon entering any project directory. If absent, scan core codebase files and generate a new `AGENTS.md`.
- **Updates**: Append notes, architectural changes, milestone completions, and plans to `AGENTS.md` after every non-trivial task.

## 2. Skill Creation & Git Sync
- **Creation**: Whenever learning a new workflow or building a reusable procedure, create a `SKILL.md` file.
- **Sync**: Copy the skill to `~/skills-workspace/skills/<skill-name>/SKILL.md`.
- **Git Push**: Commit and push changes to the `skills-workspace` repository.
