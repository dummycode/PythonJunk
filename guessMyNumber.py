import random

secretNumber = random.randint(1, 100) # random number in range [1, 100]
print('I am thinking of a number between 1 and 100...')

# get player's guess
for numOfGuesses in range(1, 11):
    print('Take a guess: ', end='')
    guess = int(input())
    if (guess > secretNumber):
        print('Lower...')
    elif(guess < secretNumber):
        print('Higher...')
    else:
        break

if (guess == secretNumber):
    print('Congrats, you successfully guessed in ' + str(numOfGuesses) + ' guesses')
else:
    print('You idiot, the number I was thinking of was ' + str(secretNumber))

