#! python3
# selective_copy.py - Walks through a folder tree, finds files with
# a specified extension, and copies them to a new folder.

"""
Usage:
    1. Update the SOURCE_FOLDER to the folder you want to search.
    2. Update the DEST_FOLDER to the folder where found files should be copied.
    3. Update the FILE_EXTENSION to the extension you want to search (e.g., '.pdf' or '.jpg').
    4. Run: python selective_copy.py
"""

import os
import shutil

# 1) Define the folder to walk through (source), the destination folder, and the file extension
SOURCE_FOLDER = "/path/to/source/folder"      # e.g., "/home/user/Documents"
DEST_FOLDER   = "/path/to/destination/folder" # e.g., "/home/user/FoundFiles"
FILE_EXTENSION = ".pdf"                       # e.g., ".pdf" or ".jpg"

def selective_copy(src_folder, dest_folder, file_ext):
    """
    Walks through src_folder and copies all files ending with file_ext
    into dest_folder (keeping their filenames).
    """

    # Ensure the destination folder exists (create it if needed)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Walk the folder tree
    for foldername, subfolders, filenames in os.walk(src_folder):
        print(f"Searching in: {foldername} ...")

        # Loop through each file in the current folder
        for filename in filenames:
            # Check if file ends with the desired extension
            if filename.lower().endswith(file_ext.lower()):
                # Construct full path of the source file
                src_file_path = os.path.join(foldername, filename)
                # Construct the full path of the destination file
                dest_file_path = os.path.join(dest_folder, filename)

                print(f"Copying: {src_file_path} -> {dest_file_path}")
                # Copy the file to the destination folder
                shutil.copy2(src_file_path, dest_file_path)

    print("Search and copy complete.")

if __name__ == "__main__":
    selective_copy(SOURCE_FOLDER, DEST_FOLDER, FILE_EXTENSION)
