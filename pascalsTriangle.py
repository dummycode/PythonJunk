# initialize pascals triangle with given rows
def initializeTriangle(triangle, rows):
    for y in range(rows):
        triangle.append([])
        for x in range(y + 1):
            if (x == 0 or x == y):
                triangle[y].append(1)
            else:
                triangle[y].append(triangle[y - 1][x] + triangle[y - 1][x - 1])
        
# make the triangle look pretty
def printTriangle(triangle):
    length = len(triangle)
    for i in range(length):
        numOfTabs = (length - i)
        for tab in range(numOfTabs):
            print(" ", end='')
        for number in range(len(triangle[i])):
                print(" " + str(triangle[i][number]) + " ", end='')
        for tab in range(numOfTabs):
            print(" ", end='')
        print()

triangle = []
initializeTriangle(triangle, 10)
printTriangle(triangle)

