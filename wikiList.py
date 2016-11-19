import pyperclip

print("Enter list\n")

myList = pyperclip.paste()
myListLines = myList.split('\n')
for i in range(myListLines):
    myListLines[i] = "* " + lines[i]
myList = myList.join('\n')

print(myList)
pyperclip.copy(myList)
print("Copied to clipboard!")
