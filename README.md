# Skill Management System

This directory acts as the central workspace for custom agent skills, version-controlled with Git and automatically backed up to GitHub.

## Use Cases

- **Agent Portability:** Easily deploy your custom skills across different terminal environments, machines, or new agent instances by cloning this repository.
- **Unified Skill Management:** Centralize system-level skills (managed by Gemini CLI) and your own custom-built skills in one searchable, structured hierarchy.
- **Collaborative Development:** Use Git's branching and pull-request features to refine skill definitions, test improvements, and collaborate with others.
- **Automated Backup:** Never lose your custom skill definitions; every commit automatically pushes your changes to the cloud.

## Installation Guidelines (How to use these skills)

To integrate a skill from this workspace into an agent environment:

1. **Clone the Workspace:**
   ```bash
   git clone git@github.com:polymath-void/gemini-skills-workspace.git ~/skills-workspace
   ```

2. **Register the Skill:**
   Depending on the agent framework, register the skill by pointing it to the directory containing the `SKILL.md` file. For Gemini CLI:
   ```bash
   # Example: Linking a system skill
   mkdir -p ~/.gemini/skills/antigravity-support
   ln -s ~/skills-workspace/system-skills/antigravity-support/SKILL.md ~/.gemini/skills/antigravity-support/SKILL.md
   ```

3. **Verify:**
   Verify the agent recognizes the skill by listing available skills in the agent's interactive interface (e.g., using `ls ~/.gemini/skills/`).

## Workflow

1. **Creation/Update:** Place or edit skill files (e.g., `SKILL.md` and associated scripts) in `~/skills-workspace/system-skills/` or `~/skills-workspace/user-skills/`.
2. **Version Control:**
   ```bash
   cd ~/skills-workspace
   git add .
   git commit -m "feat: added/updated skill <skill-name>"
   ```
3. **Backup:** The `post-commit` hook automatically pushes changes to `origin main`.
