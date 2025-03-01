"""Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
"""

import re

def is_strong_password(password):
    """Check if the password meets strength requirements."""
    # At least 8 characters long
    length_regex = re.compile(r".{8,}")
    # At least one lowercase letter
    lowercase_regex = re.compile(r"[a-z]")
    # At least one uppercase letter
    uppercase_regex = re.compile(r"[A-Z]")
    # At least one digit
    digit_regex = re.compile(r"\d")

    # Validate each condition
    if not length_regex.search(password):
        return "Password too short! Must be at least 8 characters."
    if not lowercase_regex.search(password):
        return "Password must contain at least one lowercase letter."
    if not uppercase_regex.search(password):
        return "Password must contain at least one uppercase letter."
    if not digit_regex.search(password):
        return "Password must contain at least one digit."

    return "Strong password!"

# Sample passwords for testing
test_passwords = [
    "Short1",        # Too short
    "nocapital123",  # Missing uppercase
    "NOLOWER123",    # Missing lowercase
    "NoDigitsHere",  # Missing digits
    "Str0ngPass!",   # Strong password
]

# Test all passwords
for pwd in test_passwords:
    print(f"Testing: {pwd} → {is_strong_password(pwd)}")
