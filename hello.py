# This progam says hello and asks for my name

print('Hello world!')

# Get name
print('What is your name?') 
myName = input()
print('It\'s good to meet you, ' + myName)
print('The length of your name is ' + str(len(myName)))

# Get age
print('What is your age?') 
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
