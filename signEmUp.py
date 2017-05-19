import requests
import random
import string

url = 'http://localhost:8878/accounts'

for _ in range(5):
    email = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(10))
    name = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(10))
    params = {"email": email + "@gmail.com", "password": "d0nt4get", "passwordc": "d0nt4get", "name": name}

    requests.post(url, params=params, json='')
