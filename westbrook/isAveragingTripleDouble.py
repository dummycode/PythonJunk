from getStats import getStats

def isAveragingTripleDouble():
    stats = getStats()
    for stat in stats:
        if (int(float(stat)) <  10):
            return not True
    return True

