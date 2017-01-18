import shelve

shelfFile = shelve.open('shelveExample.config')
print(shelfFile['cats'])
print(shelfFile['size'])
