import copy

def eggs(someParameter):
    someParameter.append('Hello')
spam = [1, 2, 3]
eggs(copy.copy(spam))
print(spam)
