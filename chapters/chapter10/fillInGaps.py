#! python3
# fill_gaps.py - Finds all files matching a given prefix + zero-padded number + extension
# in a single folder, and renames them to close any gaps in numbering.

"""
Usage:
    1. Update FOLDER_PATH to the folder containing numbered files (e.g., spam001.txt, spam003.txt).
    2. Update PREFIX and EXTENSION to match the pattern you expect (e.g., "spam" and ".txt").
    3. Run: python fill_gaps.py
    4. It will rename files to fill any missing numbers in the sequence.
"""

import os
import re
import shutil

# 1) Configuration
FOLDER_PATH = r"/path/to/folder"   # e.g. r"C:\temp\spamFiles"
PREFIX = "spam"                   # e.g. "spam"
EXTENSION = ".txt"                # e.g. ".txt"

def fill_in_gaps(folder, prefix, extension):
    """
    Finds all files with names matching 'prefix' + zero-padded number + extension,
    e.g. spam001.txt, spam002.txt, etc., in 'folder'.
    Then renames them to remove any numeric gaps in sequence.
    """
    folder = os.path.abspath(folder)

    # Step 2: Create a regex to match files of the form: prefix + digits + extension
    # Example: spam001.txt
    # Groups:
    #  - 1) entire numeric portion
    #  - 2) for capturing leading zeros if needed
    file_pattern = re.compile(rf"^({prefix})(\d+){extension}$", re.IGNORECASE)

    # Collect all matching files
    matching_files = []
    for filename in os.listdir(folder):
        match_obj = file_pattern.match(filename)
        if match_obj:
            numeric_part = match_obj.group(2)  # the digits (e.g. '001')
            # Convert string digits to an integer
            file_number = int(numeric_part)
            matching_files.append((filename, file_number, numeric_part))

    # If no matching files, nothing to do
    if not matching_files:
        print("No matching files found.")
        return

    # Sort files by their numeric part
    matching_files.sort(key=lambda x: x[1])  # Sort by integer value

    print("Files found (in numeric order):")
    for (orig_name, num_val, num_str) in matching_files:
        print(f"  {orig_name} -> number={num_val}")

    # Step 3: Rename files to close any gaps
    # The first file should have number 1, second file 2, etc.
    # We'll keep zero-padding consistent with the WIDEST numeric string found,
    # or you could keep original file's digit-length if you want.
    max_digits = max(len(x[2]) for x in matching_files)  # e.g. '003' => 3
    current_expected_num = 1

    for (orig_name, num_val, num_str) in matching_files:
        # Check if the file's numeric part matches the expected number
        if num_val != current_expected_num:
            # We'll rename it to prefix + zero-padded current_expected_num + extension
            new_num_str = str(current_expected_num).zfill(max_digits)
            new_name = prefix + new_num_str + extension

            # Build absolute paths
            orig_abs = os.path.join(folder, orig_name)
            new_abs = os.path.join(folder, new_name)

            print(f"Renaming {orig_abs} to {new_abs}")
            # Actually rename the file
            shutil.move(orig_abs, new_abs)
        else:
            # It's already in correct position; no rename needed
            pass

        current_expected_num += 1

    print("Done filling in gaps.")

if __name__ == "__main__":
    fill_in_gaps(FOLDER_PATH, PREFIX, EXTENSION)
