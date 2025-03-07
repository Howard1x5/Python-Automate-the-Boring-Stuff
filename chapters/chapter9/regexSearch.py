import os  # For file handling
import re  # For regular expressions

# Step 1: Get folder path and regex pattern from the user
folder_path = input("Enter the folder path to search: ").strip()
if not os.path.isdir(folder_path):
    print("Error: The folder path is invalid!")
    exit()

regex_pattern = input("Enter the regex pattern to search for: ")

try:
    compiled_pattern = re.compile(regex_pattern)  # Compile the user-provided regex
except re.error:
    print("Error: Invalid regex pattern!")
    exit()

# Step 2: Loop through all .txt files in the folder
print("\nSearching for matches...\n")
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Only process .txt files
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_num, line in enumerate(file, 1):  # Read file line by line
                if compiled_pattern.search(line):  # If match is found
                    print(f"[{filename}, Line {line_num}] {line.strip()}")  # Print result

print("\nSearch complete.")
