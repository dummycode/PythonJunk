import locale

locale.setlocale(locale.LC_ALL, 'en_US')

print('Find the Nth term in the fibonacci sequence\nEnter N (#): ', end='')
n = int(input())
if(n == 1):
    print('0')
else:
    firstFib = 0
    secondFib = 1
    for i in range(1, n):
        temp = firstFib + secondFib
        firstFib = secondFib
        secondFib = temp
    answer = secondFib
    suffix = ''
    if (n % 10 == 1):
        suffix = 'st'
    elif (n % 10 == 2):
        suffix = 'nd'
    elif (n % 10 == 3):
        suffix = 'rd'
    else:
        suffix = 'th'

    print('The ' + str(n) + suffix + ' term is ' + str(locale.format('%d', answer, grouping=True)))

