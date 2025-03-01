"""Date Detection

Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date."""

# Regex for date detection
## \d\d \d\d \d\d\d\d
## (\d{2})/(\d{2})/(\d{4})

import re

def is_valid_date(day, month, year):
    """Check if the extracted date is valid."""
    thirty_day_months = {4, 6, 9, 11}  # April, June, September, November
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Ensure valid month range
    if month < 1 or month > 12:
        return False

    # Check valid days per month
    if month in thirty_day_months and day > 30:
        return False
    elif month == 2:  # February check
        if is_leap_year and day > 29:
            return False
        elif not is_leap_year and day > 28:
            return False
    elif day > 31:  # All other months
        return False

    return True  # If all conditions pass, the date is valid

# Define regex pattern for date detection
date_pattern = re.compile(r"(\d{2})/(\d{2})/(\d{4})")

# Sample text containing dates
text = "Today's date is 31/02/2020, another date is 29/02/2024 (leap year), and one more 15/08/2023."

# Find all date matches in the text
matches = date_pattern.findall(text)

# Process each extracted date
for match in matches:
    day, month, year = map(int, match)  # Convert string groups to integers
    
    if is_valid_date(day, month, year):
        print(f"✅ Valid date: {day:02d}/{month:02d}/{year}")
    else:
        print(f"❌ Invalid date: {day:02d}/{month:02d}/{year}")
