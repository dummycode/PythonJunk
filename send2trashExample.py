import send2trash

# create a bacon file
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable')
baconFile.close()
# send it to the trash
send2trash.send2trash('bacon.txt')

