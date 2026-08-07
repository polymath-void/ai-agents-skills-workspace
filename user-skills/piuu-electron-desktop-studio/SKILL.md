---
name: piuu-electron-desktop-studio
description: Electron desktop creator studio (piuu-studio-desktop), RSA signed .piuu zip bundle archive compiler, contextBridge IPC preload bridge, and live 60fps canvas phone simulator.
---

# 💻 Piuu Electron Desktop Extension Studio Skill (`piuu-electron-desktop-studio`)

This skill documents building cross-platform Electron desktop creator tools (`piuu-studio-desktop/`) for extension bundle creation, manifest validation, and live phone canvas previews.

---

## 🏗️ 1. Architecture Overview (`piuu-studio-desktop/`)

* **Main Process (`piuu-studio-desktop/main.js`)**: Node.js background process performing asynchronous zip archiving and SHA-256 integrity hashing.
* **Preload Bridge (`piuu-studio-desktop/src/preload.js`)**: Secure `contextBridge.exposeInMainWorld('piuuStudio', ...)` API exposing file system dialogs and export methods to Chromium.
* **Phone Canvas Simulator (`piuu-studio-desktop/src/index.html`)**: Real-time HTML5 60fps simulated phone canvas preview with dynamic theme sliders.

---

## 📦 2. Bundle Export Specification (`.piuu`)

The `.piuu` extension package is a compressed zip archive containing:
```text
my_custom_theme.piuu
├── plugin.json
├── preview.png
├── theme.json
└── icons/
```

---

## 🛠️ Required & Associated Agent Workspace Tools
When working on `.piuu` extension packaging, Electron desktop studios, or IPC bridges, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-bundle-packer`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-bundle-packer) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-bundle-packer.md)): Compiles and validates verified `.piuu` extension packages with auto-generated SHA-256 manifests.
- [`wc-json-validate`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-validate) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-json-validate.md)): Validates `plugin.json` and `theme.json` schemas.
- [`wc-contract-check`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-contract-check) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-contract-check.md)): Audits IPC bridge contracts and API payloads between preload and renderer.
- [`wc-deps`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-deps) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-deps.md)): Audits `package.json` dependencies for security vulnerabilities and version locks.
- *Upcoming Tool Note*: `wc-electron-runner` (Headless Electron IPC mock verifier) is in the roadmap.

