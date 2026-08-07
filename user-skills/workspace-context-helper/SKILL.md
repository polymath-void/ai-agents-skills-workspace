---
name: workspace-context-helper
description: Provides workspace context, directory structure metadata, and advanced tools for analysis, management, and sanitization. Use for workspace inspection, cleanup, and architectural analysis.
---

# Workspace Context Helper

This skill provides quick access to the current workspace's directory structure, environment metadata, and advanced management tools.

## Workspace Structure

See [Workspace Structure](references/structure.md) for the complete directory tree.

## Tools Library

These tools are located in `tools/bin/` and `tools/lib/`.

### 1. `wc-scan` (Scanning & Metadata)
- **Purpose**: Generates a structured JSON map of your workspace.
- **When to use**: When you need a fast, programmatic overview of the directory structure.
- **Usage**: `tools/bin/wc-scan <directory> <output.json>`

### 2. `wc-manage` (Management & Sanitization)
- **Purpose**: Workspace maintenance, including file removal based on patterns.
- **When to use**: To clean up build artifacts, temporary files, or orphan dependencies.
- **Usage**: `tools/bin/wc-manage sanitize <directory> <pattern1> [pattern2 ...]`

### 3. `wc-analyze` (Analysis Framework)
- **Purpose**: Workspace analysis and quality metrics.
- **When to use**: To assess code complexity, identify bottlenecks, or perform dependency analysis.
- **Usage**: `tools/bin/wc-analyze complexity <directory>`

