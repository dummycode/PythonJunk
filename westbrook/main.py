from getStats import getStats
from isAveragingTripleDouble import isAveragingTripleDouble

# A simple "Is he?"
print(isAveragingTripleDouble())

# Show stats
stats = getStats()
print('Points: ' + stats[0])
print('Assists: ' + stats[1])
print('Rebounds: ' + stats[2])
