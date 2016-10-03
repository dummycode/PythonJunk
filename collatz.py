def collatz(number):
    if (number % 2 == 0):
        return int(number / 2)
    else:
        return int(3 * number + 1)

print('Enter number: ', end='')

try:
    number = int(input())
    print(str(collatz(number)))
except ValueError:
    print('You must enter an integer')    
