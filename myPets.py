pets = ['Fido', 'Scooby', 'Copper', 'Dixie']
print('Enter a pet name: ')
name = input()
if (name in pets):
    print(name + ' is my pet') 
else:
    print('I do not have a pet named ' + name)
