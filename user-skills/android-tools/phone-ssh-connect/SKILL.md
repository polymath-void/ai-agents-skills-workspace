---
name: phone-ssh-connect
description: Setup and connect a mobile phone (Android/iOS) to the host machine over local Wi-Fi SSH.
category: android-tools
---

# Phone SSH Connection Skill (`phone-ssh-connect`)

This skill provides step-by-step instructions and configuration protocols for setting up a mobile phone (Android/iOS) to access the host machine's terminal and Antigravity CLI session securely over local Wi-Fi SSH.

---

## 📋 Prerequisites

1. **Same Wi-Fi Network**: Both the host machine and your phone must be connected to the same local Wi-Fi network.
2. **Find Host IP**: Find the host's local IP address on the Wi-Fi interface (e.g. `wlxa047d780dded` or similar):
   ```bash
   ip a | grep -E "inet .*wl"
   ```
   *(Note down the IP, e.g. `192.168.1.100`)*

---

## 🛠️ Step 1: Host SSH Server Setup

1. **Install OpenSSH Server**:
   ```bash
   sudo apt update && sudo apt install -y openssh-server
   ```
2. **Start and Enable Service**:
   ```bash
   sudo systemctl enable --now ssh
   ```
3. **Configure Firewall** (If UFW is enabled):
   ```bash
   sudo ufw allow 22/tcp
   ```
4. **Verify SSH Status**:
   ```bash
   sudo systemctl status ssh
   ```

---

## 📱 Step 2: Phone Client Configuration

### Method A: Android via Termux (Recommended)

1. **Install Termux** (from F-Droid or Github).
2. **Install OpenSSH Client** inside Termux:
   ```bash
   pkg update && pkg install openssh -y
   ```
3. **Generate SSH Key Pair** on phone:
   ```bash
   ssh-keygen -t ed25519 -C "phone-termux"
   ```
   *(Press enter to accept defaults)*
4. **Copy Public Key to Host**:
   ```bash
   ssh-copy-id username@<HOST_IP_ADDRESS>
   ```
   *(Enter your host password once)*
5. **Connect Securely**:
   ```bash
   ssh username@<HOST_IP_ADDRESS>
   ```

---

### Method B: Android via Graphic Apps (JuiceSSH / Termius)

1. Install **JuiceSSH** or **Termius** from the Google Play Store.
2. Create a new Connection:
   - **Type**: SSH
   - **Address / Host**: `<HOST_IP_ADDRESS>`
   - **Port**: `22`
   - **Username**: `<YOUR_HOST_USERNAME>`
3. Save and tap to connect. Enter your password when prompted.

---

### Method C: iOS (Termius / Blink / Prompt)

1. Install **Termius** or **Blink Shell** from the App Store.
2. Add a new Host:
   - **IP / Host**: `<HOST_IP_ADDRESS>`
   - **Username**: `<YOUR_HOST_USERNAME>`
   - **Password**: *(Enter your host login password)*
3. Save and connect.

---

## 🤖 Step 3: Accessing Antigravity CLI over SSH

Once connected from your phone terminal, type `agy` to start the AI session:
```bash
agy
```

### 💡 Troubleshooting DBus/Login Prompts:
If `agy` asks for a login screen on your phone terminal:
Ensure that your remote session binds to the active desktop session keyring:
```bash
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
export DISPLAY=":0"
```
*(This can be appended to your `~/.bashrc` to ensure clean passwordless key access).*
