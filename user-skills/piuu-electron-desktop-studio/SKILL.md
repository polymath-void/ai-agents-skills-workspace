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
