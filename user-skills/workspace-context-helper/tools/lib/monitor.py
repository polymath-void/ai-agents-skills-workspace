import json
import os
from pathlib import Path
try:
    from .analyzer import analyze_workspace
except (ImportError, ValueError):
    from analyzer import analyze_workspace

DEFAULT_HEALTH_CONFIG = {
    "max_cyclomatic_complexity": 15,
    "max_build_artifact_size_bytes": 52428800,
    "forbidden_patterns": ["*.tmp", "*.log", "*.bak"]
}

IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.gradle', '.cache'}

class WorkspaceMonitor:
    def __init__(self, config_path=None):
        self.config = dict(DEFAULT_HEALTH_CONFIG)
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    user_cfg = json.load(f)
                    self.config.update(user_cfg)
            except Exception:
                pass

    def check_health(self, root_path):
        anomalies = []
        root = Path(root_path).resolve()
        if not root.exists():
            return [f"Root path not found: {root_path}"]

        # 1. Complexity Check
        max_c = self.config.get('max_cyclomatic_complexity', 15)
        complexity_results = analyze_workspace(root_path, mode="complexity")
        for file_path, complexity in complexity_results.items():
            if isinstance(complexity, int) and complexity > max_c:
                anomalies.append(f"High Complexity ({complexity} > {max_c}): {file_path}")

        # 2. Forbidden Patterns Check
        for pattern in self.config.get('forbidden_patterns', []):
            try:
                for item in root.rglob(pattern):
                    if any(ignored in item.parts for ignored in IGNORE_DIRS):
                        continue
                    anomalies.append(f"Forbidden Pattern Found: {item}")
            except (OSError, PermissionError):
                continue

        # 3. File size check (safeguarded against broken links)
        max_size = self.config.get('max_build_artifact_size_bytes', 52428800)
        try:
            for item in root.rglob('*'):
                if any(ignored in item.parts for ignored in IGNORE_DIRS):
                    continue
                try:
                    if item.is_file(follow_symlinks=False):
                        size = item.stat().st_size
                        if size > max_size:
                            anomalies.append(f"Large File ({size} bytes > {max_size}): {item}")
                except (OSError, PermissionError):
                    continue
        except (OSError, PermissionError):
            pass

        return anomalies
