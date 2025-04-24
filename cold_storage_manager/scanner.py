"""Scans directories for files unused beyond a given age."""
import os
import time
from typing import List

def get_unused_files(path: str, days: int) -> List[str]:
    """Returns a list of files in `path` unused for at least `days`."""
    cutoff_time = time.time() - (days * 86400) # seconds in a day
    unused_files = []
    
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            if os.path.getatime(full_path) < cutoff_time:
                unused_files.append(full_path)
    
    return unused_files