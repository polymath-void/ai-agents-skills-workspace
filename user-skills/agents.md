# Antigravity (AGY) Agent Ecosystem & Workflow Guidelines

## 1. Overview & Agent Architecture
Google Antigravity (AGY) operates as a multi-agent AI coding assistant designed for pair programming, codebase analysis, autonomous task completion, and background system orchestration inside Android Termux (`aarch64`).

### Supported Agent Profiles & Subagents
- **Primary Agent (Antigravity)**: Main pair-programmer equipped with code search, file editing, bash execution, terminal tasks, and slash commands.
- **Research Subagent**: Read-only exploration agent for codebase surveying and documentation retrieval.
- **Self Subagent**: Full-capability subagent for isolated subtasks.
- **Hermes Agent CLI**: External autonomous CLI agent integrated via `$HOME/.hermes`.

---

## 2. Universal Data Protection & Backup Integration
All agent session states, tool transcripts, scratch scripts, subagent logs, and persistent rules are continuously protected via `agy-backup`:

- **Active User Data Target**: `~/.gemini/antigravity-cli`
- **Subagent Transcripts**: `~/.gemini/antigravity-cli/brain/<conversation-id>/`
- **Knowledge Rules**: `~/.gemini/antigravity-cli/knowledge/`
- **Skills Directory**: `~/.gemini/antigravity-cli/skills/` and `~/skills-workspace/`

---

## 3. Conclusion & Automation Standard

> [!IMPORTANT]
> **Conclusion**:
> All AI agents, subagents, and CLI workflows within this Termux environment operate under a unified, automated cloud backup protocol powered by `agy-backup`. On every AGY CLI startup (`agy`), an asynchronous background process automatically triggers `agy-backup backup --target all`, computing SHA-256 manifest deltas and updating the latest Google Drive backup instances (`/AGY_Backups`) without causing launch delays. Furthermore, all skill and agent modifications are authoritatively tracked and pushed via Git to `~/skills-workspace`. This ensures total disaster recovery, zero data loss across device migrations, and 100% state persistence across all AI agents.
