#! python3
# commandLineEmailer.py - Logs into Gmail using Selenium, 
# and sends an email with a message read from command line arguments.

"""
Usage:
  1. Install Selenium and a matching web driver (e.g., ChromeDriver for Google Chrome).
  2. Place your Gmail username and password in the code or in environment variables.
  3. Run from command line:
     python commandLineEmailer.py recipient@example.com "Your message text here"
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1) Ensure you have ChromeDriver or another driver installed.
#    e.g., place chromedriver.exe in your PATH if using Windows with Chrome.

# Replace these with your own credentials (NOT recommended for production).
GMAIL_USERNAME = "your.email@gmail.com"
GMAIL_PASSWORD = "your_password"

def main():
    if len(sys.argv) < 3:
        print("Usage: python commandLineEmailer.py <recipient_email> <message_text>")
        sys.exit(1)

    recipient = sys.argv[1]
    message_text = ' '.join(sys.argv[2:])  # Combine all subsequent args into one message string

    # 2) Initialize Selenium WebDriver (here we use Chrome as an example)
    print("Launching browser...")
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.

    try:
        # 3) Navigate to Gmail login page
        print("Navigating to Gmail login page...")
        driver.get("https://mail.google.com/")

        time.sleep(2)  # Wait for page to load

        # 4) Enter username
        print("Entering email...")
        email_elem = driver.find_element_by_id("identifierId")
        email_elem.send_keys(GMAIL_USERNAME)
        email_elem.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for transition to password page

        # 5) Enter password
        print("Entering password...")
        password_elem = driver.find_element_by_name("password")
        password_elem.send_keys(GMAIL_PASSWORD)
        password_elem.send_keys(Keys.RETURN)

        time.sleep(5)  # Give some time to ensure login is complete

        # 6) Click the "Compose" button
        print("Composing new email...")
        compose_btn = driver.find_element_by_css_selector(".T-I.T-I-KE.L3")
        compose_btn.click()

        time.sleep(3)  # Wait for compose window to appear

        # 7) Fill out recipient
        print("Filling out recipient address...")
        to_elem = driver.find_element_by_name("to")
        to_elem.send_keys(recipient)

        # 8) Fill out subject (optional, we'll do a simple subject)
        subject_elem = driver.find_element_by_name("subjectbox")
        subject_elem.send_keys("Automated Email (Selenium)")

        # 9) Fill out message body
        print("Writing message text...")
        body_elem = driver.find_element_by_css_selector("div[aria-label='Message Body']")
        body_elem.send_keys(message_text)

        time.sleep(1)

        # 10) Click "Send"
        print("Sending email...")
        send_btn = driver.find_element_by_css_selector("div[data-tooltip='Send ‪(Ctrl-Enter)‬']")
        send_btn.click()

        time.sleep(3)  # Wait a moment to ensure the email is sent
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 11) Close the browser
        print("Closing browser.")
        driver.quit()

if __name__ == "__main__":
    main()
