#! python3
# linkVerifier.py - Given a URL, downloads the page, finds all linked pages,
# and checks if they return a 404 Not Found status code.

"""
Usage:
    1. pip install requests beautifulsoup4
    2. python linkVerifier.py <URL>
       e.g. python linkVerifier.py https://example.com
    3. The script will:
       - Download the page at the given URL
       - Parse out all links in <a> tags
       - Check each link with requests.get()
       - Print links that return a 404 status code
"""

import sys
import requests
import bs4
from urllib.parse import urljoin

def main():
    if len(sys.argv) < 2:
        print("Usage: python linkVerifier.py <URL>")
        sys.exit(1)

    start_url = sys.argv[1]
    print(f"Downloading main page: {start_url}")

    try:
        res = requests.get(start_url)
        res.raise_for_status()
    except Exception as e:
        print(f"Error downloading {start_url}: {e}")
        sys.exit(1)

    # Parse the main page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Gather all <a> links
    link_elems = soup.select('a[href]')
    print(f"Found {len(link_elems)} links on the page.")

    broken_links = []
    checked_links = set()  # To avoid checking the same link multiple times

    # Check each link
    for link_elem in link_elems:
        href = link_elem.get('href')
        # Convert relative links to absolute using urljoin
        absolute_url = urljoin(start_url, href)

        # Skip if we've seen this link before
        if absolute_url in checked_links:
            continue
        checked_links.add(absolute_url)

        print(f"Checking link: {absolute_url}")
        try:
            r = requests.get(absolute_url, timeout=10)  # set a timeout if site is slow
            if r.status_code == 404:
                print(f"  -> Broken link (404): {absolute_url}")
                broken_links.append(absolute_url)
            else:
                print(f"  -> OK ({r.status_code})")
        except requests.exceptions.RequestException as e:
            # If there's a network error or other request issue
            print(f"  -> Could not check link: {absolute_url} ({e})")

    # Summarize broken links
    if broken_links:
        print("\nBroken links found:")
        for link in broken_links:
            print(f" - {link}")
    else:
        print("\nNo broken links found.")

if __name__ == "__main__":
    main()
