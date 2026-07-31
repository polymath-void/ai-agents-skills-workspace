import os
import shutil
from pathlib import Path

def organize_skills(base_path):
    base = Path(base_path).expanduser()
    system_skills = base / "system-skills"
    user_skills = base / "user-skills"
    
    # Ensure standard directories exist
    system_skills.mkdir(parents=True, exist_ok=True)
    user_skills.mkdir(parents=True, exist_ok=True)

    # Scan for directories containing SKILL.md directly under base
    for item in base.iterdir():
        if item.is_dir() and item.name not in ["system-skills", "user-skills", ".git"]:
            if (item / "SKILL.md").exists():
                print(f"Organizing: {item.name}")
                # Simple heuristic: if it has 'system' or 'builtin' in name, move to system-skills
                if "system" in item.name.lower() or "builtin" in item.name.lower():
                    dest = system_skills / item.name
                else:
                    dest = user_skills / item.name
                
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.move(str(item), str(dest))
                print(f"Moved to: {dest}")

if __name__ == "__main__":
    organize_skills("~/skills-workspace")
