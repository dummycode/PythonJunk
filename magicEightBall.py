import random

def getAnswer(answerNumber):
    if (answerNumber == 1):
        return 'It is certain'
    elif (answerNumber == 2):
        return 'It is decidedly so'
    elif (answerNumber == 3):
        return 'Yes'
    elif (answerNumber == 4):
        return 'Hell nah'
    elif(answerNumber == 5):
        return 'Ask again later'
    elif(answerNumber == 6):
        return 'Outlook not so good'
    elif(answerNumber == 7):
        return 'Ask again later'

print(getAnswer(random.randint(1,7)))
