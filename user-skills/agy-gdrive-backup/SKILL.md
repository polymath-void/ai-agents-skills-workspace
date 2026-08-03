---
name: agy-gdrive-backup
description: Comprehensive workflow and procedures for backing up, restoring, authenticating, and verifying AGY CLI user data with Google Drive.
---

# AGY User Data Google Drive Backup & Restore Skill

## Overview
This skill defines standard operating procedures and workflows for managing, backing up, authenticating, and restoring AGY CLI (`agy`) user data to and from Google Drive.

## Data Scope & Target Directories
- **Source Directory**: `~/.gemini/antigravity-cli` (`/data/data/com.termux/files/home/.gemini/antigravity-cli`)
- **Remote Cloud Path**: Google Drive `/AGY_Backups/`

### 1. Inclusions (Essential User Data)
- `settings.json` (CLI configuration & permissions)
- `knowledge/` (Saved user rules & domain knowledge)
- `skills/` (Custom user skills & workflows)
- `memory/` (Persistent session memory)
- `history.jsonl` (Prompt & execution history)
- `conversations/` & `conversation_summaries.db` (Session databases)
- `brain/` (Artifacts, scratch scripts, subagent transcripts)
- `mcp_config.json` & `mcp/` (Model Context Protocol configs)

### 2. Exclusions (Ephemeral & Cache Files)
- `cache/` (Downloaded models or temp asset caches)
- `cli.log` (Current session runtime logs)
- `crashes/` & `updater/` (Crash dumps and update state)
- Temporary `.lock` files or socket listeners

---

## Workflows & Standard Procedures

### Workflow 1: Google Drive Authentication (OAuth2)
1. **Credentials Setup**:
   - Obtain Google OAuth Client ID & Client Secret (Google Cloud Console with Drive API enabled).
   - Store OAuth credentials securely in `~/.gemini/antigravity-cli/gdrive_credentials.json`.
2. **Interactive Authorization**:
   - Run `agy-backup auth`.
   - Complete browser/device-code authorization flow to issue refresh & access tokens.
   - Tokens stored securely at `~/.gemini/antigravity-cli/gdrive_token.json`.

---

### Workflow 2: Automated Cloud Backup
1. **Archive Generation**:
   - Compress included directories into a timestamped `.tar.gz` bundle:
     `agy_backup_YYYY-MM-DD_HHMMSS.tar.gz`
   - Calculate SHA256 checksum: `agy_backup_YYYY-MM-DD_HHMMSS.tar.gz.sha256`.
2. **Upload to Google Drive**:
   - Connect via Google Drive API v3.
   - Upload both archive and checksum file into the `/AGY_Backups` folder.
3. **Retention & Pruning**:
   - Keep the most recent 10 backups on Google Drive. Auto-prune older snapshots.

---

### Workflow 3: Complete Restoration (Safety First)
When restoring user data to a new device or recovering state:

1. **Pre-Restore Safety Snapshot**:
   - ALWAYS create a local pre-restore safety copy of existing `~/.gemini/antigravity-cli` before proceeding:
     `cp -r ~/.gemini/antigravity-cli ~/.gemini/antigravity-cli.pre-restore.bak`
2. **Select & Fetch Remote Backup**:
   - Query Google Drive `/AGY_Backups` for available backup archives.
   - Download the target backup `.tar.gz` and corresponding `.sha256` checksum file.
3. **Checksum Verification**:
   - Verify local file hash matches `.sha256`. Stop and fail if checksum fails.
4. **Controlled Extraction**:
   - Extract archive contents over `~/.gemini/antigravity-cli`.
5. **Post-Restore Termux Verification & Cleanup**:
   - Run `termux-fix-shebang` on executable scripts if restored on Android.
   - Verify `settings.json` is valid JSON.
   - Clean up temporary restore files.

---

### Workflow 4: Emergency Rollback Procedure
If a restoration attempt causes errors or invalid configuration:
1. Stop any running AGY CLI instances.
2. Remove corrupted directory: `rm -rf ~/.gemini/antigravity-cli`
3. Restore pre-restore safety snapshot: `mv ~/.gemini/antigravity-cli.pre-restore.bak ~/.gemini/antigravity-cli`
4. Confirm CLI functionality: `agy --help` or check `settings.json`.

---

## Utility Tool Command Reference
The `agy-backup` Python CLI utility implements these workflows:

| Command | Action |
|---|---|
| `python3 -m agy_backup.cli auth` | Authenticate with Google Drive OAuth2 |
| `python3 -m agy_backup.cli backup` | Create & upload backup archive to Google Drive |
| `python3 -m agy_backup.cli list` | List available backups on Google Drive |
| `python3 -m agy_backup.cli restore [file_id]` | Safely restore AGY user data from Google Drive |
| `python3 -m agy_backup.cli status` | Show auth & backup status |
