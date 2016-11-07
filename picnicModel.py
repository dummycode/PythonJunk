allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought...')
print('Apples: ' + str(totalBrought(allGuests, 'apples')))
print('Pretzels: ' + str(totalBrought(allGuests, 'pretzels')))
print('Ham Sandwiches: ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('Cups: ' + str(totalBrought(allGuests, 'cups')))
print('Apple pies: ' + str(totalBrought(allGuests, 'apple pies')))

