import unittest
import os
import json
import shutil
from pathlib import Path
from lib.scanner import scan_directory
from lib.manager import sanitize_workspace
from lib.analyzer import ComplexityAnalyzer, analyze_workspace, workspace_summary
from lib.monitor import WorkspaceMonitor
from wie.storage.memory import WIEMemory

class TestWorkspaceTools(unittest.TestCase):
    def setUp(self):
        self.sandbox = Path(os.environ.get('HOME', '/tmp')) / 'workspace_test_sandbox'
        if self.sandbox.exists():
            shutil.rmtree(self.sandbox)
        self.sandbox.mkdir(parents=True, exist_ok=True)
        (self.sandbox / 'test_file.py').write_text('def test():\n    if True:\n        return 1\n')
        (self.sandbox / 'build').mkdir(exist_ok=True)
        (self.sandbox / 'build' / 'temp.o').write_text('dummy')

    def tearDown(self):
        if self.sandbox.exists():
            shutil.rmtree(self.sandbox)

    def test_scanner(self):
        tree = scan_directory(self.sandbox)
        self.assertIsNotNone(tree)
        self.assertEqual(tree['name'], 'workspace_test_sandbox')
        self.assertGreaterEqual(tree['total_files'], 2)
        self.assertGreaterEqual(tree['total_dirs'], 1)

    def test_manager_dry_run(self):
        would_remove = sanitize_workspace(self.sandbox, ['*.o'], dry_run=True)
        self.assertTrue(any('temp.o' in item for item in would_remove))
        self.assertTrue((self.sandbox / 'build' / 'temp.o').exists())

    def test_manager_sanitize(self):
        removed = sanitize_workspace(self.sandbox, ['*.o'])
        self.assertTrue(any('temp.o' in item for item in removed))
        self.assertFalse((self.sandbox / 'build' / 'temp.o').exists())

    def test_analyzer(self):
        analyzer = ComplexityAnalyzer(self.sandbox / 'test_file.py')
        complexity = analyzer.calculate_complexity()
        self.assertEqual(complexity, 2)
        
        metrics = analyzer.calculate_metrics()
        self.assertEqual(metrics['functions'], 1)
        self.assertEqual(metrics['complexity'], 2)

        summary = workspace_summary(self.sandbox)
        self.assertEqual(summary['total_files'], 1)
        self.assertEqual(summary['total_functions'], 1)

    def test_monitor(self):
        monitor = WorkspaceMonitor()
        anomalies = monitor.check_health(self.sandbox)
        self.assertIsInstance(anomalies, list)

    def test_memory_db(self):
        db_file = self.sandbox / 'storage' / 'wie_test.db'
        memory = WIEMemory(db_file)
        memory.log_event("CREATED", str(self.sandbox / 'test_file.py'))
        self.assertTrue(db_file.exists())

if __name__ == '__main__':
    unittest.main()
