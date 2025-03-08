#! python3
# imgurDownloader.py - Demonstrates how to search Imgur for a category 
# and download displayed images using Selenium.

"""
Usage:
    1. pip install selenium requests
    2. Download an appropriate WebDriver (e.g., ChromeDriver if you use Chrome).
    3. python imgurDownloader.py "funny cats"
    4. This script will:
       - Open Imgur in a Selenium-driven browser.
       - Enter the search term.
       - Attempt to parse the first batch of image links.
       - Download them to an 'imgur_images' folder in the current directory.
Note:
    - Imgur's layout can change over time.
    - This script doesn't handle infinite scrolling or logging in.
    - Check Imgur's Terms of Service before large-scale scraping.
"""

import sys
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    if len(sys.argv) < 2:
        print("Usage: python imgurDownloader.py <search term>")
        sys.exit(1)

    search_term = ' '.join(sys.argv[1:])
    download_folder = "imgur_images"
    os.makedirs(download_folder, exist_ok=True)

    # 1) Initialize Selenium (Chrome example)
    print("Launching browser...")
    driver = webdriver.Chrome()

    try:
        # 2) Go to Imgur
        print("Navigating to Imgur...")
        driver.get("https://imgur.com/")

        time.sleep(2)

        # 3) Accept cookies if needed (site updates frequently)
        try:
            accept_btn = driver.find_element(By.XPATH, '//button[text()="ACCEPT ALL"]')
            accept_btn.click()
        except:
            pass  # If there's no accept button, skip

        time.sleep(2)

        # 4) Find the search box, type the term, and press Enter
        print(f"Searching for: {search_term}")
        search_box = driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="Images, #tags, @users oh my!"]')
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)  # Wait for results to load

        # 5) Try to locate all the image elements on the search results page
        #    This CSS selector or XPATH may need updating if Imgur changes layout
        print("Collecting image links...")
        image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
        # The site might have many images for site layout or placeholders

        # Filter out images that are actually part of search results
        # We'll take a naive approach and try to pick out images with specific domain references
        # or check their classes
        img_urls = []
        for img_el in image_elements:
            src = img_el.get_attribute("src")
            # Heuristics for actual images (some might be placeholders or logos)
            if src and "https://i.imgur.com/" in src:
                img_urls.append(src)
        
        # 6) Remove duplicates (some images might appear multiple times)
        img_urls = list(set(img_urls))

        print(f"Found {len(img_urls)} image URLs.")

        # 7) Download each image
        for i, url in enumerate(img_urls, start=1):
            print(f"Downloading image {i}/{len(img_urls)}: {url}")
            try:
                res = requests.get(url)
                res.raise_for_status()

                # Extract a filename from the URL
                filename = os.path.basename(url)
                # Some filenames can end with ?1 or other params
                if '?' in filename:
                    filename = filename.split('?')[0]

                with open(os.path.join(download_folder, filename), 'wb') as file:
                    for chunk in res.iter_content(100000):
                        file.write(chunk)

            except Exception as e:
                print(f"Skipping {url} due to error: {e}")

    except Exception as err:
        print(f"An error occurred: {err}")

    finally:
        print("Closing browser.")
        driver.quit()

    print("Done.")

if __name__ == "__main__":
    main()
