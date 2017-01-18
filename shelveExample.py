import shelve

shelfFile = shelve.open('shelveExample')
print(shelfFile['cats'])
print(shelfFile['size'])
shelfFile.close()
