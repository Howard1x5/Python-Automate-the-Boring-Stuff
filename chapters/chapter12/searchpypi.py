#! python3
# searchpypi.py - Opens several PyPI search result links in your default web browser.

"""
Usage:
    1. From the command line, type:
       python searchpypi.py <search terms>
       For example:
       python searchpypi.py requests library
    2. This script will:
       - Form a search URL for https://pypi.org/search/?q=<search terms>.
       - Download the search results page.
       - Scrape links for the top package listings (using BeautifulSoup).
       - Open the top 5 results (or fewer, if less than 5 results) in new browser tabs.
"""

import requests, sys, webbrowser, bs4

print("Searching on PyPI...")  # Display a message while downloading the search result page

# 1) Build the search URL from command line arguments
#    e.g. python searchpypi.py requests library
#    sys.argv = ['searchpypi.py', 'requests', 'library']
#    The query would be 'requests library'
search_terms = ' '.join(sys.argv[1:])
search_url = 'https://pypi.org/search/?q=' + search_terms

# 2) Download the search result page with requests
res = requests.get(search_url)
res.raise_for_status()  # if there's an error (e.g. 404), this will raise an exception

# 3) Parse the HTML with BeautifulSoup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# 4) Find all search result links on PyPI
#    Inspecting the PyPI search results HTML shows that class="package-snippet" is used for each result
linkElems = soup.select('.package-snippet')

# 5) Open a browser tab for each result
#    We'll open up to the first 5 results (or fewer, if there's less than 5)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # Each link's href is missing 'https://pypi.org', so we need to prepend it
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href', '')
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)
