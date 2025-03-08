#! python3
# downloadXkcd.py - Downloads every single XKCD comic by following
# the "Prev" button until it reaches the start.

"""
Usage:
  1. Make sure you have `requests` and `bs4` installed (e.g., `pip install requests beautifulsoup4`).
  2. Run: python downloadXkcd.py
  3. Comics will be saved in the "xkcd" folder within the current working directory.
"""

import requests, os, bs4

# Step 1: Set the starting URL and create a folder named 'xkcd' to store comics
url = 'https://xkcd.com'                # starting URL
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd (create if needed)

# Loop until we hit the first XKCD comic (indicated by a '#' link)
while not url.endswith('#'):
    # Step 2: Download the page
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Step 3: Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Could not find comic image.")
    else:
        # The <img> src attribute sometimes lacks the 'https:' prefix, so we prepend it if needed
        comicUrl = comicElem[0].get('src', '')
        if comicUrl.startswith('//'):
            comicUrl = 'https:' + comicUrl
        elif comicUrl.startswith('/'):
            comicUrl = 'https://xkcd.com' + comicUrl

        print(f"Downloading image {comicUrl}...")
        imgRes = requests.get(comicUrl)
        imgRes.raise_for_status()

        # Step 4: Save the image to the ./xkcd folder
        imageFileName = os.path.basename(comicUrl)
        with open(os.path.join('xkcd', imageFileName), 'wb') as imageFile:
            for chunk in imgRes.iter_content(100000):
                imageFile.write(chunk)

    # Step 5: Get the Prev button's url to go to the previous comic
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print("Done.")
