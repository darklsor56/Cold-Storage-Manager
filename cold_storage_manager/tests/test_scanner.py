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
    def test_recently_accessed_files_not_returned(self):
        """Ensure that if files are recently accessed, they will not be returned."""
        with tempfile.TemporaryDirectory() as temp_dir:
            new_file_1 = os.path.join(temp_dir, "new_one.txt")
            new_file_2 = os.path.join(temp_dir, "new_two.txt")
            with open(new_file_1, "w", encoding = "utf-8") as f:
                f.write("I'm a child.")
            with open(new_file_2, "w", encoding = "utf-8") as f:
                f.write("I'm a young file.")
            one_day_ago = time.time() - 86400
            os.utime(new_file_2, (one_day_ago, one_day_ago))
            result = scanner.get_unused_files(temp_dir, days = 2)
            self.assertNotIn(new_file_1, result)
            self.assertNotIn(new_file_2, result)
    def test_get_unused_files_from_mixed(self):
        """Check if we only get the unused files from a set of files both used and unused."""
        with tempfile.TemporaryDirectory() as temp_dir:
            old_file_1 = os.path.join(temp_dir, "old_one.txt")
            new_file_1 = os.path.join(temp_dir, "new_one.txt")
            old_file_2 = os.path.join(temp_dir, "old_two.txt")
            new_file_2 = os.path.join(temp_dir, "new_two.txt")
            new_file_3 = os.path.join(temp_dir, "new_three.txt")
            new_file_4 = os.path.join(temp_dir, "new_four.txt")
            old_file_3 = os.path.join(temp_dir, "old_three.txt")
            with open(old_file_1, "w", encoding = "utf-8") as f:
                f.write("I'm old")
            with open(old_file_2, "w", encoding = "utf-8") as f:
                f.write("I'm older")
            with open(old_file_3, "w", encoding = "utf-8") as f:
                f.write("I'm oldest")
            with open(new_file_1, "w", encoding = "utf-8") as f:
                f.write("I'm a baby file")
            with open(new_file_2, "w", encoding = "utf-8") as f:
                f.write("I'm a child file")
            with open(new_file_3, "w", encoding = "utf-8") as f:
                f.write("I'm a young file")
            with open(new_file_4, "w", encoding = "utf-8") as f:
                f.write("I'm a teen file")
            # Set access time to 3 days ago
            three_days_ago = time.time() - (3 * 86400)
            two_days_ago = time.time() - (2 * 86400)
            os.utime(old_file_1, (two_days_ago, two_days_ago))
            os.utime(old_file_2, (three_days_ago, three_days_ago))
            os.utime(old_file_3, (three_days_ago, three_days_ago))
            result = scanner.get_unused_files(temp_dir, days = 1)
            self.assertIn(old_file_1, result)
            self.assertIn(old_file_2, result)
            self.assertIn(old_file_3, result)
            self.assertNotIn(new_file_1, result)
            self.assertNotIn(new_file_2, result)
            self.assertNotIn(new_file_3, result)
            self.assertNotIn(new_file_4, result)
    def test_nested_directories(self):
        """Ensure the scanner can go into nested directories."""
        with tempfile.TemporaryDirectory() as temp_dir:
            nested_dir = os.path.join(temp_dir, "subdir")
            os.makedirs(nested_dir)
            file_path = os.path.join(nested_dir, "nested.txt")
            with open(file_path, "w", encoding = "utf-8") as f:
                f.write("nested")
            # Set access time to 5 days ago
            five_days_ago = time.time() - (5 * 86400)
            os.utime(file_path, (five_days_ago, five_days_ago))
            result = scanner.get_unused_files(temp_dir, days=2)
            self.assertIn(file_path, result)
    def test_empty_directory(self):
        """Ensure the program can run properly if the directory is empty."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = scanner.get_unused_files(temp_dir, days = 1)
            self.assertEqual(result, [])
