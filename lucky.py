#! python3
# lucky.py - Use if you're feeling lucky with your google searches

import requests, sys, webbrowser, bs4, pyperclip

if (len(sys.argv) > 1):
    searchString = ' '.join(sys.argv[1:])
else:
    searchString = pyperclip.paste()

print("Googling...")
res = requests.get("http://google.com/search?q=" + searchString)

# Quit on failure
try:
    res.raise_for_status()
except Exception as err:
    print("Error searching: " + str(err))
    exit()

# Convert to bs4 object
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open 5 or all result links
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

print('Opened')
