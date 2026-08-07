import os
import sys
import time
import subprocess
from pathlib import Path

# Local imports
try:
    from .env_checker import get_system_telemetry, get_installed_toolchains
    from .dep_inspector import inspect_dependencies
    from .monitor import WorkspaceMonitor
except (ImportError, ValueError):
    from env_checker import get_system_telemetry, get_installed_toolchains
    from dep_inspector import inspect_dependencies
    from monitor import WorkspaceMonitor

def execute_autonomous_task(task_title, target_dir=".", run_tests=True):
    """
    Executes a complete multi-phase task validation pipeline and produces a structured execution receipt.
    """
    start_time = time.perf_counter()
    receipt = {
        "task_title": task_title,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "target_dir": str(Path(target_dir).resolve()),
        "phases": {},
        "success": True,
        "elapsed_seconds": 0.0
    }

    # Phase 1: Environment Telemetry
    telemetry = get_system_telemetry()
    toolchains = get_installed_toolchains()
    receipt["phases"]["environment"] = {
        "status": "PASS",
        "is_termux": telemetry["is_termux"],
        "python_version": telemetry["python_version"],
        "available_ram_mb": telemetry["available_ram_mb"],
        "tools_ready": [k for k, v in toolchains.items() if v["installed"]]
    }

    # Phase 2: Workspace Dependencies
    deps = inspect_dependencies(target_dir)
    receipt["phases"]["dependencies"] = {
        "status": "PASS",
        "gradle_modules": len(deps.get("gradle", [])),
        "npm_packages": len(deps.get("npm", [])),
        "python_manifests": len(deps.get("python", []))
    }

    # Phase 3: Workspace Health Audit
    monitor = WorkspaceMonitor()
    anomalies = monitor.check_health(target_dir)
    receipt["phases"]["health_audit"] = {
        "status": "PASS" if not anomalies else "WARNING",
        "anomalies_count": len(anomalies),
        "anomalies": anomalies[:5]
    }

    # Phase 4: Unit Test Suite Validation (if requested)
    if run_tests:
        tools_dir = Path(__file__).resolve().parent.parent
        if (tools_dir / "tests" / "test_all.py").exists():
            test_res = subprocess.run(
                ["python3", "-m", "unittest", "tests/test_all.py"],
                cwd=str(tools_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            test_passed = (test_res.returncode == 0)
            receipt["phases"]["unit_tests"] = {
                "status": "PASS" if test_passed else "FAIL",
                "output": test_res.stderr.strip() or test_res.stdout.strip()
            }
            if not test_passed:
                receipt["success"] = False

    receipt["elapsed_seconds"] = round(time.perf_counter() - start_time, 3)
    return receipt
