class FileNode:
    """This stores the data for a file and the location for the next files."""
    def __init__(self, file_path: str, last_accessed: float):
        """Initiates the FileNode class"""
        self.file_path = file_path
        self.last_accessed = last_accessed
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        """Overides the < symbol ensuring the tree files work properly"""
        return (self.last_accessed < other.last_accessed)
    
    def __repr__(self):
        """The string representation of the FileNode class."""
        return f"<FileNode {self.file_path} @ {self.last_accessed}>"