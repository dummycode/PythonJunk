import random, math

print('I am thinking of a four digit number, try and guess it!')

secret = random.randint(1000, 9999)

correct = False

while not correct:
    tempSecret = secret
    print('Guess (#): ', end='')
    guess = int(input())
    
    numCorrect = 0
    sumCorrect = 0

    for i in range(0, 4):
        guessDigit = guess % 10
        secretDigit = tempSecret % 10
        if (guessDigit == secretDigit):
            numCorrect += 1
            sumCorrect += secretDigit
        guess = math.floor(guess / 10)
        tempSecret = math.floor(tempSecret / 10)

    if (numCorrect != 4):
        print('num correct: ' + str(numCorrect))
        print('sum: ' + str(sumCorrect))
    else:
        print('Wow, you\'re a mind reader')
        correct = True
