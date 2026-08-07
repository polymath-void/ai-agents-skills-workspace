import os
import json
from pathlib import Path

TOOLS_CATALOG = [
    {
        "name": "wc-scan",
        "category": "Inspection & Architecture",
        "description": "Recursively scans workspace directory tree, builds resilient JSON maps, and computes aggregate file/dir metrics.",
        "usage": "wc-scan <directory> [output_json]",
        "examples": [
            "wc-scan .",
            "wc-scan ~/repo/Piuu-Unified-Launcher-Android metadata.json"
        ]
    },
    {
        "name": "wc-search",
        "category": "Inspection & Search",
        "description": "Context-aware lightning-fast symbol, regex, and text finder that automatically ignores build/cache noise directories.",
        "usage": "wc-search <query> [path] [-e ext] [-C lines] [--json]",
        "examples": [
            "wc-search 'wallpaperTransparency' . -e kt,xml",
            "wc-search 'class .*ViewModel' . -r -e kt"
        ]
    },
    {
        "name": "wc-deps",
        "category": "Dependencies & Packages",
        "description": "Multi-ecosystem dependency manifest analyzer for Android Gradle, Node NPM, Python, and Rust Cargo.",
        "usage": "wc-deps [directory] [--json]",
        "examples": [
            "wc-deps .",
            "wc-deps ~/repo/Piuu-Unified-Launcher-Android --json"
        ]
    },
    {
        "name": "wc-analyze",
        "category": "Code Quality & Complexity",
        "description": "Calculates cyclomatic complexity, lines of code (LOC), functions, and structural metrics for codebase files.",
        "usage": "wc-analyze <complexity|metrics|summary> [directory]",
        "examples": [
            "wc-analyze summary .",
            "wc-analyze metrics ./lib"
        ]
    },
    {
        "name": "wc-manage",
        "category": "Workspace Maintenance",
        "description": "Safely sanitizes build artifacts, temporary logs, and orphan caches with protected root bounds and dry-run preview.",
        "usage": "wc-manage sanitize <directory> <pattern1> [pattern2...] [--dry-run]",
        "examples": [
            "wc-manage sanitize . '*.tmp' '*.bak' --dry-run",
            "wc-manage sanitize . '__pycache__'"
        ]
    },
    {
        "name": "wc-monitor",
        "category": "Health & Anomaly Detection",
        "description": "Continuously audits workspace health against complexity limits, large file bounds, and forbidden patterns.",
        "usage": "wc-monitor <root_path> [config_path]",
        "examples": [
            "wc-monitor .",
            "wc-monitor ~/repo/Piuu-Unified-Launcher-Android config/workspace-health.json"
        ]
    },
    {
        "name": "wc-git-sync",
        "category": "Git & CI/CD",
        "description": "Multi-branch synchronizer (e.g. main <-> master unified path) and fast working tree status inspector.",
        "usage": "wc-git-sync <status|sync> [dir] [src] [target]",
        "examples": [
            "wc-git-sync status .",
            "wc-git-sync sync . main master"
        ]
    },
    {
        "name": "wc-termux-env",
        "category": "Android & Termux System",
        "description": "Inspects Android/Termux hardware telemetry (RAM, CPU load), verified toolchains (clang, python, git), and fixes shebangs.",
        "usage": "wc-termux-env <status|toolchains|fix-shebangs> [dir]",
        "examples": [
            "wc-termux-env status",
            "wc-termux-env toolchains",
            "wc-termux-env fix-shebangs ./scripts"
        ]
    },
    {
        "name": "wc-tool-registry",
        "category": "Meta & Discovery",
        "description": "Interactive registry index providing instant capability discovery and zero-overhead invocation recipes.",
        "usage": "wc-tool-registry [category|tool_name] [--json]",
        "examples": [
            "wc-tool-registry",
            "wc-tool-registry --json"
        ]
    }
]

def get_registry_catalog(filter_query=None):
    """
    Returns filtered list of registered workspace context tools.
    """
    if not filter_query or filter_query == "--json":
        return TOOLS_CATALOG

    query = filter_query.lower()
    return [
        t for t in TOOLS_CATALOG
        if query in t["name"].lower() or query in t["category"].lower() or query in t["description"].lower()
    ]
