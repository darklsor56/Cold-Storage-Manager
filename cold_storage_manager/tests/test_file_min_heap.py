import unittest
from cold_storage_manager.data_structures.file_node import FileNode
from cold_storage_manager.data_structures.file_min_heap import FileMinHeap

class TestFileMinHeap(unittest.TestCase):

    def test_insert_and_peek(self):
        """Tests to see if we peek the oldest file."""
        heap = FileMinHeap()
        node1 = FileNode("/file/a.txt", 100)
        node2 = FileNode("/file/b.txt", 50)
        node3 = FileNode("/file/c.txt", 75)

        heap.insert(node1)
        heap.insert(node2)
        heap.insert(node3)

        self.assertEqual(heap.peek_coldest().file_path, "/file/b.txt")

    def test_pop_coldest(self):
        """Ensure a file can be popped"""
        heap = FileMinHeap()
        heap.insert(FileNode("/file/x.txt", 300))
        heap.insert(FileNode("/file/y.txt", 100))

        coldest = heap.pop_coldest()
        self.assertEqual(coldest.file_path, "/file/y.txt")
        self.assertEqual(len(heap), 1)

    def test_update_access_time(self):
        """Test if we can update the access time from the FileMinHeap class."""
        heap = FileMinHeap()
        heap.insert(FileNode("/file/a.txt", 500))
        heap.insert(FileNode("/file/b.txt", 100))

        heap.update("/file/a.txt", 50)

        self.assertEqual(heap.peek_coldest().file_path, "/file/a.txt")

    def test_peek_empty(self):
        """Ensure we can run peek on an empty heap."""
        heap = FileMinHeap()
        self.assertIsNone(heap.peek_coldest())

    def test_pop_empty(self):
        """Ensure we can run pop on an empty heap."""
        heap = FileMinHeap()
        self.assertIsNone(heap.pop_coldest())