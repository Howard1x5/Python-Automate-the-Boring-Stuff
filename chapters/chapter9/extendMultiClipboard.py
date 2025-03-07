#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard using the shelve module.

"""
Usage:
    python mcb.pyw save <keyword> - Saves clipboard content under the given keyword.
    python mcb.pyw <keyword> - Loads the saved text for the keyword onto the clipboard.
    python mcb.pyw list - Loads all saved keywords onto the clipboard.
    python mcb.pyw delete <keyword> - Deletes a specific keyword.
    python mcb.pyw delete all - Deletes all saved keywords.
"""

import shelve  # Used for persistent key-value storage
import pyperclip  # Used for clipboard interaction
import sys  # Used to read command-line arguments

# Open the shelf file to store clipboard content persistently
mcbShelf = shelve.open('mcb')

# If user wants to save clipboard content with a keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    keyword = sys.argv[2]  # Second argument is the keyword
    mcbShelf[keyword] = pyperclip.paste()  # Save clipboard content under the keyword
    print(f"Saved clipboard content under keyword: '{keyword}'")

# If user wants to list all saved keywords
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    keywords = list(mcbShelf.keys())  # Get all saved keywords
    if keywords:
        pyperclip.copy(str(keywords))  # Copy the list of keywords to the clipboard
        print("Keywords copied to clipboard:", keywords)
    else:
        print("No saved keywords found.")

# If user wants to delete a specific keyword or all saved keywords
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    keyword = sys.argv[2]
    if keyword.lower() == 'all':
        mcbShelf.clear()  # Deletes all saved data
        print("All saved keywords deleted.")
    elif keyword in mcbShelf:
        del mcbShelf[keyword]  # Delete a specific keyword
        print(f"Deleted keyword: '{keyword}'")
    else:
        print(f"Keyword '{keyword}' not found.")

# If user wants to load content for a saved keyword
elif len(sys.argv) == 2:
    keyword = sys.argv[1]
    if keyword in mcbShelf:
        pyperclip.copy(mcbShelf[keyword])  # Copy the saved text to the clipboard
        print(f"Copied content for keyword '{keyword}' to clipboard.")
    else:
        print(f"Keyword '{keyword}' not found.")

# Close the shelf file
mcbShelf.close()
