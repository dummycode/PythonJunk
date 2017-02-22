#! python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    file = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()
except Exception as err:
    print("There was a problem: " + str(err))
