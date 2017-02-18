import requests

url = 'http://104101110114121.com/temp/login.php'
payload = {'username': input('Enter username: '), 'password': input('Enter password: ')}

request = requests.post(url, data=payload)

result = request.text

if (result == 'success'):
    print('Wowza! Good guess!')
else:
    print('You wrong bish.')
