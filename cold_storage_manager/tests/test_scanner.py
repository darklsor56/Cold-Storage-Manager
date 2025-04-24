"""This tests the scanner.py file to ensure it is properly returning unused files."""
import unittest
import tempfile
import os
import time
from cold_storage_manager import scanner

class TestScanner(unittest.TestCase):
    """This runs the test case for scanner"""
    def test_get_unused_files(self):
        """Run the test while looking in this directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "test.txt")
            with open(file_path, "w", encoding = "utf-8") as f:
                f.write("hello")
            # Set access time to 2 days ago
            two_days_ago = time.time() - (2 * 86400)
            os.utime(file_path, (two_days_ago, two_days_ago))
            result = scanner.get_unused_files(temp_dir, days = 1)
            self.assertIn(file_path, result)
