#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()


# TODO: Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)        # makes a sting value not a list of values    

pyperclip.copy(text)

