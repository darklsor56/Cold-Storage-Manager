"""This will test the file node class itself."""
import unittest
from cold_storage_manager.data_structures.file_node import FileNode

class TestFileNode(unittest.TestCase):
    """Test the file node class"""
    
    def test_initialization(self):
        """Ensure a single node can be made properly"""
        node = FileNode("/test/path.txt", 1714700000.0)
        self.assertEqual(node.file_path, "/test/path.txt")
        self.assertEqual(node.last_accessed, 1714700000.0)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        
    def test_equality(self):
        """Check for equality between two nodes"""
        node1 = FileNode("/test/file.txt", 1000.0)
        node2 = FileNode("/test/file.txt", 1000.0)
        node3 = FileNode("/test/file.txt", 2000.0)
        node4 = FileNode("/test/other.txt", 1000.0)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)
    
    def test_less_than(self):
        """Test the less than override"""
        older = FileNode("/file1", 1000.0)
        newer = FileNode("/file2", 2000.0)
        self.assertTrue(older < newer)
        self.assertFalse(newer < older)
        
    def test_repr(self):
        """Test the string representation"""
        node = FileNode("/example/file.txt", 1234567890.0)
        expected = "<FileNode /example/file.txt @ 1234567890.0>"
        self.assertEqual(repr(node), expected)
        
if __name__ == "__main__":
    unittest.main()