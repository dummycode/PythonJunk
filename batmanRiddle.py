# Finds the address Batman plans to strike at

import math

def isUnique(number):
    digitList = []
    while (number > 0):
        digit = number % 10
        number = math.floor(number / 10)
        if (digit in digitList):
            return False
        digitList.append(digit)
    return True

def getSum(number):
    digitList = []
    while(number > 0):
        digit = number % 10
        number = math.floor(number / 10)
        digitList.append(digit)
    return sum(digitList)

def validThousandsDigit(number):
    number = math.floor(number / 10)
    tensDigit = number % 10
    number = math.floor(number / 100)
    thousandsDigit = number % 10
    return thousandsDigit == tensDigit * 3

i = 0
for i in range(1001, 10000, 2):
    if (isUnique(i) and getSum(i) == 27 and validThousandsDigit(i)):
        print(i)

