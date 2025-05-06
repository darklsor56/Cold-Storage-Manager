"""Primarily stores the files locations and NOT there acessed/download times"""
import os
from cold_storage_manager.data_structures.file_node import FileNode
    
class FileBST:
    """This is where the file's will be stored for log(n) access times"""
    def __init__(self):
        """Defines the whole tree."""
        self.root = None
    
    def insert(self, file_path, last_accessed):
        """If the root is empty fill it, otherwise, call the recursive function."""
        new_node = FileNode(file_path, last_accessed)
        if root is None:
            root = new_node
        else:
            self._insert_recursive(self.root, new_node)
                
    def _insert_recursive(self, current, new_node):
        """Recursivley insert based on lexicographic file_path"""
        # Traverse the left side
        if new_node.file_path < current.file_path:
            if current.left is None: # Fill the left side!
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else: # Traverse the right side
            if current.right is None: # Fill the right side!
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)
    
    def find(self, file_path):
        """Call the recursive function unless root is the correct node"""
        if root is None:
            print("The tree is empty.")
            return None
        return self._find_recursive(self.root, file_path)
            
    def _find_recursive(self, current, file_path):
        """Binary search based on file_path"""
        # Check the node
        if current is None:
            return None
        if current.file_path == file_path:
            return current
        
        # Traverse the left side
        if file_path < current.file_path:
            return self._find_recursive(current.left, file_path)
        else: # Traverse the right side
            return self._find_recursive(current.right, file_path)

    def update(self, file_path, new_access_time):
        """Update the access time if the file has been accessed or downloaded."""
        node = self.find(file_path)
        # First, ensure the file path exists, then update
        if node:
            node.last_accessed = new_access_time