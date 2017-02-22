#! python3
# mapIt.py - Launches map in browser using address from the command line arguments or the clipboard

import webbrowser, sys, pyperclip

if (len(sys.argv) > 1):
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
