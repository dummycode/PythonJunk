import shelve

def getStats():
    shelf = shelve.open('stats')
    return [shelf['points'], shelf['assists'], shelf['rebounds']];

