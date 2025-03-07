#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

"""
Usage:
    1. Specify the folder path you want to back up.
    2. Run this script: python backupToZip.py
    3. It will create a ZIP file named <folderName>_1.zip, then <folderName>_2.zip, etc.
"""

import zipfile
import os

def backupToZip(folder):
    """
    Backs up the entire contents of 'folder' into a ZIP file.
    The ZIP file's name increments based on existing backups.
    """
    # Step 1: Ensure 'folder' is an absolute path
    folder = os.path.abspath(folder)

    # Step 2: Figure out the filename this code should use based on existing backups
    number = 1
    while True:
        # Construct ZIP filename: <folderName>_<number>.zip
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            # Found a filename that doesn't exist yet, break out of loop
            break
        number += 1

    # Step 3: Create the ZIP file in write mode
    print(f"Creating {zipFilename}...")
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Step 4: Walk the entire folder tree and add files to the ZIP
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")

        # Add the current folder to the ZIP file
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            # Construct absolute path for each file
            absFilePath = os.path.join(foldername, filename)

            # Skip any existing backup ZIP files to avoid recursion
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files

            # Write the file to the ZIP
            backupZip.write(absFilePath)

    # Close the ZIP file
    backupZip.close()
    print("Done.")

# Example usage:
# You can replace 'C:\\delicious' with the folder path you want to backup
if __name__ == "__main__":
    backupToZip('~/home/lordfarquad/Documents/Projects/Python-Automate-the-Boring-Stuff/chapters/chapter10/testbackupZip')
