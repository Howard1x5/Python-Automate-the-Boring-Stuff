import re  # Import regular expressions for word replacement
import os  # Import OS for file handling

# Step 1: Read the text file
input_filename = "madlibs_input.txt"  # Input file with placeholders
output_filename = "madlibs_output.txt"  # File to save modified text

if not os.path.exists(input_filename):  # Check if input file exists
    print(f"Error: '{input_filename}' not found! Please create the file first.")
    exit()

with open(input_filename, 'r') as file:
    text = file.read()  # Read the content of the file

# Step 2: Define placeholders to be replaced
placeholders = ["ADJECTIVE", "NOUN", "VERB", "ADVERB"]

# Step 3: Loop through placeholders and prompt user for replacements
for placeholder in placeholders:
    pattern = re.compile(rf'\b{placeholder}\b')  # Match whole word
    while pattern.search(text):  # While placeholder exists in text
        user_input = input(f"Enter a {placeholder.lower()}: ")  # Get user input
        text = pattern.sub(user_input, text, 1)  # Replace first occurrence

# Step 4: Display the modified text
print("\nModified Mad Libs Text:")
print(text)

# Step 5: Save modified text to a new file
with open(output_filename, 'w') as file:
    file.write(text)

print(f"\nMad Libs saved to '{output_filename}'")
