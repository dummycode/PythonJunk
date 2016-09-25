def devideBy(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        return 'Error: Invalid argument'
print(devideBy(2))
print(devideBy(12))
print(devideBy(0))
