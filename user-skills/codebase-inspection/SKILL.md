---
name: codebase-inspection
description: Perform structured inspection, architectural mapping, and status analysis of codebases and GitHub repositories. Use when asked to inspect, analyze, or audit a repository structure, dependencies, CI workflows, or codebase architecture.
---

# 🔍 Codebase Inspection (`codebase-inspection`)

A structured skill for auditing, inspecting, and mapping codebase architecture, repository configurations, and build/CI workflow statuses.

---

## 🎯 When to Use
Use this skill when the user asks to:
- Inspect or audit a codebase or repository structure
- Identify key entry points, dependencies, and architectural components
- Review build configurations, scripts, or GitHub Actions CI workflows
- Analyze codebase health, error traces, or structural patterns
- Perform zero-loss dependency mapping and architectural telemetry

---

## 📋 Workflow Steps

### Step 1: Structural & Directory Survey
- Examine the root directory for core configuration files (`package.json`, `pyproject.toml`, `Cargo.toml`, `requirements.txt`, `Dockerfile`, `.github/workflows/`, `settings.gradle.kts`, `CMakeLists.txt`, etc.).
- Identify project type, primary programming languages, build tools, and key dependencies.
- Map top-level directory layout (e.g., `src/`, `lib/`, `tests/`, `docs/`, `scripts/`, `bin/`).

### Step 2: Architecture & Entry Point Analysis
- Locate main application entry points (`index.ts`, `main.py`, `app.py`, `server.js`, `MainActivity.kt`, `libpiuu_core.c`).
- Trace core control flow, API routing layer, data models, and database/storage schemas.
- Review configuration management, environment variables, and authentication boundaries.

### Step 3: CI/CD & Build Inspection
- Inspect GitHub Actions workflows or build scripts under `.github/workflows/`.
- Review build commands, test runners, linter rules, and deployment pipelines.
- Verify status notification patterns, build triggers, and release automation.

### Step 4: Synthesis & Reporting
Generate a clear, structured summary containing:
1. **Overview & Tech Stack**: Core frameworks, runtime versions, and primary dependencies.
2. **Directory Architecture**: Concise map of major components.
3. **Entry Points & Data Flow**: Key operational paths and control lifecycles.
4. **Build & CI Status**: Summary of CI workflows, build configurations, and test suites.
5. **Observations & Key Findings**: Potential gaps, risks, or recommended improvements.

---

## 🛠️ Required & Associated Workspace Tools
When performing codebase inspections, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-scan`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-scan) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-scan.md)): Generates structured JSON directory trees and metadata maps.
- [`wc-analyze`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-analyze) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-analyze.md)): Computes codebase cyclomatic complexity, line counts, and maintainability metrics.
- [`wc-deps`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-deps) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-deps.md)): Maps dependency trees and detects security vulnerabilities or orphan packages.
- [`wc-contract-check`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-contract-check) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-contract-check.md)): Audits JNI Kotlin $\leftrightarrow$ C signatures and interface parity.
- [`wc-context-pack`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-context-pack) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-context-pack.md)): Compacts codebase inspection summaries into dense agent context payloads.
