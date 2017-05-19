"""listOfNumbers = []
while (True):
    number = int(input())
    if (number == 0):
        break
    else:
        listOfNumbers.append(number)

print(listOfNumbers)
"""

def toPercent(amount, total):
    return round(amount / total * 100, 2)

def main():
    listOfNumbers = [4, 4, 3, 3, 4, 2, 2, 4, 1, 2, 2, 4, 3, 1, 4, 4, 3, 1, 3, 1, 3, 3, 3, 3, 3, 3, 4, 4, 2, 4, 2, 4, 1, 2, 2, 4, 3, 4, 4, 4, 4, 3, 2, 4, 4, 1, 2, 3, 1, 4, 3, 2, 1, 3, 2, 4, 4, 2, 4, 2, 4, 1, 3, 2, 2, 3, 4, 4, 3, 3, 4, 1, 4, 3, 4, 1, 2, 3, 3, 2, 2, 4, 3, 4, 1, 1, 3, 2, 3, 4, 1, 4, 3, 3, 3, 3, 3, 2, 1, 2, 2, 4, 4, 3, 1, 2, 3, 1, 1, 3, 3, 3, 3, 2, 1, 3, 2, 3, 2, 3, 3, 2, 4, 1, 3, 1, 3, 3, 3, 3, 4, 2, 1, 2, 3, 4, 3, 4, 3, 2, 3, 2, 3, 2, 4, 3]
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    total = 0
    for i in listOfNumbers:
        if (i == 1):
            ones += 1
        elif (i == 2):
            twos += 1
        elif (i == 3):
            threes += 1
        elif (i == 4):
            fours += 1
        else:
            print("You fucked up")
        total += 1

    print("n = " + str(total))
    print("Elevator\tOne\tTwo\tThree\tFour")
    print("Count\t\t" + str(ones) + "\t" + str(twos) + "\t" + str(threes) + "\t" + str(fours))
    print("Percentages\t" + str(toPercent(ones, total))  + "\t" + str(toPercent(twos, total)) + "\t" + str(toPercent(threes, total)) + "\t" +str(toPercent(fours, total)))
