import re

def isPhoneNumber(text):
    phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    return (not phoneNumberRegex.search(text) == None)

print('720-256-7244 is a phone number')
print(isPhoneNumber('720-256-7244'))
print('800-2E4-7628 is not a phone number')
print(isPhoneNumber('800-2E4-7628'))
print('Yoshi is not a phone number')
print(isPhoneNumber('Yoshi'))

# Check this blob of text for any
blob = 'Call me at 415-001-6783 tomorrow. 678-903-3245 is my office phone.'
for i in range(len(blob)):
    chunk = blob[i:i+12]
    if (isPhoneNumber(chunk)):
        print('Phone number found: ' + chunk)

