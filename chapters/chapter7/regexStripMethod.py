import re

def regex_strip(text, chars_to_remove=None):
    """Removes leading & trailing whitespace or specific characters using regex."""
    
    # If no second argument is given, strip whitespace
    if chars_to_remove is None:
        return re.sub(r"^\s+|\s+$", "", text)  # Removes leading & trailing whitespace
    
    # Create a regex pattern that removes specified characters from both ends
    pattern = f"^[{re.escape(chars_to_remove)}]+|[{re.escape(chars_to_remove)}]+$"
    return re.sub(pattern, "", text)

# Test Cases
print(regex_strip("   Hello World   "))         # Expected: "Hello World" (removes whitespace)
print(regex_strip("...Hello World...", "."))   # Expected: "Hello World" (removes dots)
print(regex_strip("xxHello Worldxx", "x"))     # Expected: "Hello World" (removes 'x' from ends)
print(regex_strip("123Hello World123", "123")) # Expected: "Hello World" (removes '1', '2', '3' from ends)
