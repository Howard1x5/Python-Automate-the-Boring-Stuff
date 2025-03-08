#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or from the clipboard.

"""
Usage:
  1. If running from the command line:
     python mapIt.py 870 Valencia St, San Francisco, CA 94110
     The program will parse the arguments and open Google Maps to this address.
  2. If no arguments are provided, it uses the address from the clipboard:
     - Copy an address.
     - Run: python mapIt.py
     The script will open Google Maps for the clipboard's address.
"""

import webbrowser  # For opening web pages
import sys         # For reading command line arguments
import pyperclip   # For accessing clipboard content

# Check if any command line arguments were provided (beyond the script name).
if len(sys.argv) > 1:
    # e.g., mapIt.py 870 Valencia St, San Francisco, CA 94110
    # sys.argv = ['mapIt.py', '870', 'Valencia', 'St,', 'San', 'Francisco,', 'CA', '94110']
    # We want to join everything after index 0 into one string:
    address = ' '.join(sys.argv[1:])
else:
    # If no command line arguments, take the address from the clipboard.
    address = pyperclip.paste()

# Construct the Google Maps URL.
maps_url = 'https://www.google.com/maps/place/' + address

print(f"Opening Google Maps for: {address}")
webbrowser.open(maps_url)
