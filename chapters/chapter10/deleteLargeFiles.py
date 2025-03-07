#! python3
# large_file_finder.py - Walks through a folder tree and searches for
# files larger than a specified size (e.g., 100MB). Prints their absolute paths.

"""
Usage:
    1. Update FOLDER_PATH to the folder you want to search.
    2. Update SIZE_LIMIT_BYTES to the size threshold in bytes (e.g. 100 * 1024 * 1024 for 100MB).
    3. Run: python large_file_finder.py
    4. It will print any files that exceed SIZE_LIMIT_BYTES.
"""

import os

# 1) Define the folder to walk through and the size limit in bytes
FOLDER_PATH = "/path/to/folder"            # e.g., "/home/user/Documents"
SIZE_LIMIT_BYTES = 100 * 1024 * 1024       # 100MB (100 * 1024 * 1024 = 104,857,600 bytes)

def find_large_files(folder, size_limit):
    """
    Walks through 'folder' and prints paths of all files bigger than 'size_limit' bytes.
    """
    folder = os.path.abspath(folder)  # Ensure absolute path

    for foldername, subfolders, filenames in os.walk(folder):
        # Print current directory for reference
        print(f"Checking in {foldername}...")

        for filename in filenames:
            filepath = os.path.join(foldername, filename)

            try:
                filesize = os.path.getsize(filepath)
            except OSError:
                # Skip files we can't access
                print(f"Warning: Could not access {filepath}")
                continue

            # Compare file size to limit
            if filesize > size_limit:
                print(f"LARGE FILE: {filepath} ({filesize} bytes)")

if __name__ == "__main__":
    find_large_files(FOLDER_PATH, SIZE_LIMIT_BYTES)
