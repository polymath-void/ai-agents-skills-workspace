# Skill Management System

This directory acts as the central workspace for custom agent skills.

## Workflow

1.  **Creation/Update:** When a new skill is created or an existing one is updated, ensure the skill files (e.g., `SKILL.md` and any associated scripts/resources) are placed in a dedicated subdirectory within `~/skills-workspace/`.
2.  **Version Control:** The system is managed by git. After adding or modifying skills, stage and commit the changes:
    ```bash
    git add .
    git commit -m "feat: updated/added skill <skill-name>"
    ```
3.  **Backup:** To sync with the cloud, push the changes to your configured remote repository:
    ```bash
    git push origin main
    ```

*Note: Automated backup/push functionality can be integrated into this flow via git hooks or alias shortcuts.*
