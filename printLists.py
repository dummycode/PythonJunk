def printList(myList):
    length = len(myList)
    i = 0
    while (i < length):
        print(myList[i], end='')
        if (length == 2 and i != length - 1):
            print(' and ', end='')
        elif (i == length - 2):
            print(', and ', end='')
        elif (i != length - 1):
            print(', ', end='')
        else:
            print()
        i += 1
spam = ['eggs', 'shrimp', 'steak', 'shrimp', 'milk']
printList(spam)

