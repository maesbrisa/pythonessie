
def getLastElementOfTuple(tup): return tup[-1]

def sortTuple(tup):
    return sorted(tup, key=getLastElementOfTuple)


if __name__ == '__main__':
    tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sortTuple(tuples))
