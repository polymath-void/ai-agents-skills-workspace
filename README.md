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
   Run the automated registration script to link all skills:
   ```bash
   python3 -c "
   import os
   from pathlib import Path
   workspace = Path.home() / 'skills-workspace' / 'user-skills' / 'hermes'
   skills_dir = Path.home() / '.gemini' / 'skills'
   for skill_md in workspace.rglob('SKILL.md'):
       skill_name = skill_md.parent.name
       target_dir = skills_dir / skill_name
       target_dir.mkdir(parents=True, exist_ok=True)
       symlink_path = target_dir / 'SKILL.md'
       if symlink_path.exists(): os.remove(symlink_path)
       os.symlink(skill_md, symlink_path)
   "
   ```

3. **Verify:**
   Verify the agent recognizes the skill by listing available skills (e.g., `ls ~/.gemini/skills/`).

## Tactics & Compatibility

To ensure full functionality, particularly for ported skills (like Hermes Agent skills):

- **Environment Setup:** Ensure `HERMES_HOME` is configured to point to your Gemini CLI home:
  ```bash
  export HERMES_HOME=$HOME/.gemini
  # Add to .bashrc or .zshrc
  ```
- **Dependencies:** Install required system tools (e.g., `pkg install gh` for GitHub PR integration).
- **Automation:**
  - **Auto-Organization:** `~/skills-workspace/organize_skills.py` handles folder placement.
  - **Git Automation:** The `pre-commit` hook triggers organization before committing, and the `post-commit` hook pushes changes automatically to GitHub.

## Workflow

1. **Creation/Update:** Place or edit skill files (e.g., `SKILL.md`) in `~/skills-workspace/system-skills/` or `~/skills-workspace/user-skills/`.
2. **Version Control:**
   ```bash
   cd ~/skills-workspace
   git add .
   git commit -m "feat: added/updated skill <skill-name>"
   ```
3. **Backup:** The `post-commit` hook automatically pushes changes to `origin main`.
