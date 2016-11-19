""" 
pw.py
an insecure password manager
"""

import sys #, paperclip

PASSWORDS = {
        'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
        'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
        'luggage': '12345'
}

if (len(sys.argv) != 2):
    print('Usage: python3 pw.py [account]')
    exit()

account = sys.argv[1]
if (account in PASSWORDS):
    print("The password is, " + PASSWORDS[account])
else:
    print("There is no account named " + account)
