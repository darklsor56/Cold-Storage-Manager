"""This will track the accessed time and NOT the file location."""
import heapq
from cold_storage_manager.data_structures.file_node import FileNode

class FileMinHeap:
    """MinHeap that stores FileNodes, sorted by last_accessed time."""
    
    def __init__(self):
        self.heap = []          # Internal heap of (last_accessed, file_path, FileNode)
        self._entry_finder = {} # Maps file_path -> (last_accessed, file_path, FileNode)
    
    def insert(self, node: FileNode):
        """Insert a FileNode into the heap"""
        entry = (node.last_accessed, node.file_path, node)
        heapq.heappush(self.heap, entry)
        self._entry_finder[node.file_path] = entry
        
    def peek_coldest(self) -> FileNode | None:
        """Return the coldest file (oldest last_accessed), or None if empty"""
        while self.heap:
            _, file_path, node = self.heap[0]
            if file_path in self._entry_finder:
                return node
            heapq.heappop(self.heap) # Remove stale reference
        return None
    
    def pop_coldest(self) -> FileNode | None:
        """Remove and return the coldest file."""
        while self.heap:
            _, file_path, node = heapq.heappop(self.heap)
            if file_path in self._entry_finder:
                del self._entry_finder[file_path]
                return node
        return None
    
    def update(self, file_path: str, new_last_accessed: float):
        """Update a FileNode's access time and reinsert"""
        if file_path in self._entry_finder:
            # Remove the old entry (lazy deletion)
            del self._entry_finder[file_path]
            # Insert updated node
            new_node = FileNode(file_path, new_last_accessed)
            self.insert(new_node)
            
    def __len__(self):
        return len(self._entry_finder)