# Contributing to AI Agents Skills Workspace ⚡

We warmly welcome contributions from **both human developers and autonomous AI agent swarms**!

---

## 🏛️ Core Skill Contribution Principles

1. **Zero-Authentication & Self-Contained**:
   - Every skill must operate without requiring manual human logins, interactive browser forms, or secret tokens.
   - Skill instructions must be self-contained and clear enough for newly spawned subagents to execute.
2. **Standardized Directory Anatomy**:
   ```
   user-skills/<skill-name>/
   ├── SKILL.md                 # Required: YAML frontmatter + operational directives
   ├── scripts/                 # Optional: Helper scripts & CLI utilities
   ├── examples/                # Optional: Example outputs and command logs
   ├── references/              # Optional: Specs & architecture references
   └── resources/               # Optional: Assets and templates
   ```
3. **Valid YAML Frontmatter in `SKILL.md`**:
   ```yaml
   ---
   name: skill-identifier
   description: Clear, actionable description of WHEN and HOW agents should activate this skill.
   ---
   ```
4. **Integration with `AI-Agents-Workspace-Tools-Library`**:
   - Whenever procedural actions require CLI utilities, leverage existing tools from `~/AI-Agents-Workspace-Tools-Library/bin/wc-*`.

---

## 🛠️ Step-by-Step Skill Submission Lifecycle

1. **Author Skill**: Create `user-skills/<skill-name>/SKILL.md`.
2. **Lint & Validate**:
   ```bash
   wc-skill-pack --lint user-skills/<skill-name>/
   ```
3. **Register in Catalogs**:
   - Add an entry to the skills table in [`README.md`](README.md).
   - Document in [`MEMORY.md`](MEMORY.md).
4. **Sync Locally**:
   ```bash
   cp -r user-skills/<skill-name> ~/.gemini/antigravity-cli/skills/
   ```
5. **Commit & Push**:
   - Use Conventional Commits: `feat(skill): add <skill-name> specification`.

---

## 📄 License
By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
