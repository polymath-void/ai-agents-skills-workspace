---
name: android-scp-transfer
description: Transfer files between Android devices (Termux/SSH) and PC using SCP over local Wi-Fi or ADB.
---

# Android SCP File Transfer

Use this skill when copying files (e.g., `magisk_patched.img`, ROMs, logs) between an Android phone and host PC over SCP.

## Workflow

1. **Verify SSH Port on Phone**:
   - Termux default SSH port is `8022`.
   - Scan or verify open SSH ports on local IP: `nc -zv -w 2 <phone_ip> 8022`

2. **Execute SCP Download**:
   ```bash
   scp -P 8022 -o StrictHostKeyChecking=no -o ConnectTimeout=5 <user>@<phone_ip>:/sdcard/Download/<file_name> ~/Downloads/
   ```

3. **Verify Integrity**:
   - Check file size and type (`file ~/Downloads/<file_name>`).
