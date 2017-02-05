import os

if (not os.path.isfile('madLibs.txt')):
    print('File not found. Please create a madLibs.txt file.')
else:
    storyFile = open('madLibs.txt', 'r')
    story = storyFile.read()

    print(story)
