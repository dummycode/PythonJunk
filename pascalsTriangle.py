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
        numbers = ""
        for number in range(len(triangle[i])):
            numbers = numbers + str(triangle[i][number]) + " "
        print(numbers.center(length * 6))

triangle = []
initializeTriangle(triangle, 25)
printTriangle(triangle)

