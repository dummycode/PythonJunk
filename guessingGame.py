import random
guess = 'heads'
while guess in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    toss = 'tails' if toss == 1 else 'heads'
    if (toss == guess):
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if (toss == guess):
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

