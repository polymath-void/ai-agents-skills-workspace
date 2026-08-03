---
name: agy-gdrive-backup
description: Comprehensive workflow and procedures for incremental backups, manual local folder exports, multi-target sync (AGY, Gemini CLI, Termux), and restoration with Google Drive.
---

# AGY User Data & System Cloud Backup & Restore Skill

## Overview
This skill defines standard operating procedures and workflows for managing, backing up, authenticating, and restoring AGY CLI, Gemini CLI, and Termux user data to and from Google Drive or local storage directories.

## Data Targets & Inclusions
- **AGY CLI Data** (`-t agy`): `~/.gemini/antigravity-cli` (settings, rules, knowledge, skills, memory, history, conversations, brain, mcp)
- **Gemini CLI Data** (`-t gemini`): `~/.gemini` (credentials, project settings, history, policies, state)
- **Termux Environment Data** (`-t termux`): `~` (dotfiles `.termux`, `.bashrc`, `.zshrc`, `.profile`, `.gitconfig`, `.ssh`, `AGY` workspace, `skills-workspace`)

---

## Key Features & Workflows

### 1. Incremental Sync (Update-Only Mode)
- Computes SHA256 file matrix manifests (`backup_manifest.json`).
- Compares current files against last backup state.
- **If no files changed**: Skips backup upload and prints `✓ No changes detected. Backup instance is up to date.`
- **If files changed**: Overwrites/updates the existing latest backup instance on Google Drive instead of creating duplicate files on every run.

### 2. Manual Local Backup Directory Option
- Specify a custom destination path on local storage (e.g. SD card or shared folder):
  ```bash
  agy-backup backup -l ~/storage/downloads/Backups
  ```
- Or run local-only backups without cloud connection:
  ```bash
  agy-backup backup --local-only -l ~/manual_backups
  ```

---

## Utility Tool Command Reference

| Command | Description |
|---|---|
| `agy-backup auth` | Authenticate with Google Drive OAuth2 |
| `agy-backup backup [-t agy\|gemini\|termux\|all]` | Perform incremental cloud backup sync for selected target |
| `agy-backup backup -l <dir_path>` | Backup and save a copy to a manual local directory |
| `agy-backup backup --force` | Force re-backup regardless of file modification status |
| `agy-backup list` | List remote backup instances on Google Drive |
| `agy-backup restore [-t target]` | Restore target user data from Google Drive |
| `agy-backup restore --local-file <path>` | Restore target user data directly from a local archive file |
| `agy-backup rollback` | Emergency rollback to pre-restore local safety snapshot |
| `agy-backup status` | Show target paths, credentials, and local snapshot state |
