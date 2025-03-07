#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY format.

"""
Usage:
    1. Place this script in the folder with files that have American-style dates in their filenames.
    2. Run the script:
       python renameDates.py
    3. By default, it only prints the intended renaming.
       Uncomment the shutil.move() call to actually rename the files.
"""

import shutil
import os
import re

# Create a regex that matches files with the American date format.
# Groups in the regex:
#   1: All text before the date
#   2: The month (MM)
#   4: The day (DD)
#   6: The year (YYYY)
#   8: All text after the date
datePattern = re.compile(r"""
    ^(.*?)          # 1: all text before the date
    ((0|1)?\d)-     # 2: month (MM)
                    #    (0|1)? means optional leading digit 0 or 1
    ((0|1|2|3)?\d)- # 4: day (DD)
                    #    (0|1|2|3)? means optional leading digit for day
    ((19|20)\d\d)   # 6: year (YYYY) (1900-2099 for simplicity)
    (.*?)$          # 8: all text after the date
    """, re.VERBOSE)

# Loop over files in the current working directory.
for amerFilename in os.listdir('.'):
    # Search for a date pattern in the filename.
    mo = datePattern.search(amerFilename)

    # Skip files that don't match the date pattern.
    if mo is None:
        continue

    # Extract the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename (DD-MM-YYYY).
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilenameFull = os.path.join(absWorkingDir, amerFilename)
    euroFilenameFull = os.path.join(absWorkingDir, euroFilename)

    # Print what the rename would be.
    print(f'Renaming "{amerFilenameFull}" to "{euroFilenameFull}"...')

    # Uncomment this line to actually rename the files.
    shutil.move(amerFilenameFull, euroFilenameFull)