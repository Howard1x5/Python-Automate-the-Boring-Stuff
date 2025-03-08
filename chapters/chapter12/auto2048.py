#! python3
# auto2048.py - Automatically plays the 2048 game in the browser
# by cycling Up, Right, Down, Left arrow keys.

"""
Usage:
    1. pip install selenium
    2. Download the correct web driver (e.g., ChromeDriver) and ensure it's in your PATH or in the same folder.
    3. python auto2048.py
    4. Observe the game making automatic moves (Up, Right, Down, Left).
Note:
    - This script is a simple demonstration of sending arrow keys repeatedly.
    - The site or game logic may change over time, so updates may be needed.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    print("Launching browser...")
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.

    try:
        print("Navigating to 2048 game site...")
        driver.get("https://gabrielecirulli.github.io/2048/")
        time.sleep(2)  # wait for the page to load

        # The 2048 game listens for key events on the page's body
        body_elem = driver.find_element_by_tag_name("body")

        move_sequence = [Keys.ARROW_UP, Keys.ARROW_RIGHT, 
                         Keys.ARROW_DOWN, Keys.ARROW_LEFT]

        # We'll do ~1000 cycles (or you can do a while True loop)
        print("Starting automation loop (Up, Right, Down, Left)...")
        for i in range(1000):
            for move in move_sequence:
                body_elem.send_keys(move)
                # short pause so the game can render the move
                time.sleep(0.1)

        print("Automation complete. Check your score!")
    finally:
        print("Closing browser.")
        # driver.quit()  # uncomment if you want the browser to close automatically

if __name__ == "__main__":
    main()
