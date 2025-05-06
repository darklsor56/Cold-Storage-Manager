class FileNode:
    """Stores metadata for a file, and links to left/right children in a BST."""

    def __init__(self, file_path: str, last_accessed: float):
        """Initialize a file node with its path and last accessed time."""
        self.file_path: str = file_path
        self.last_accessed: float = last_accessed
        self.left: "FileNode | None" = None
        self.right: "FileNode | None" = None

    def __lt__(self, other: "FileNode") -> bool:
        """Define < operator for use in min-heaps (by last_accessed time)."""
        return self.last_accessed < other.last_accessed

    def __eq__(self, other: object) -> bool:
        """Define equality for easier testing/debugging."""
        if not isinstance(other, FileNode):
            return NotImplemented
        return (self.file_path == other.file_path and
                self.last_accessed == other.last_accessed)

    def __repr__(self) -> str:
        """Return a readable string representation for debugging."""
        return f"<FileNode {self.file_path} @ {self.last_accessed}>"
