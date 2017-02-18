def boxPrint(symbol, width, height):
    if (len(symbol) != 1):
        raise Exception('Symbol must be a single character string.')
    if (width <= 2):
        raise Exception('Width must be greater than 2')
    if (height <= 2):
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2) + symbol))
    print(symbol * width)

print('A program to print boxes!')
for i in range(10):
    sym = input('Enter one character: ')
    w = input('Enter width: ')
    h = input('Enter height: ')
    try:
        boxPrint(sym, int(w), int(h))
    except Exception as err:
        print('An exception occurred: ' + str(err))
