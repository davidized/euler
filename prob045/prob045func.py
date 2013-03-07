
def triNum(n):
    return n*(n+1)/2

def pentNum(n):
    return n*(3*n-1)/2

def hexNum(n):
    return n*(2*n-1)

def listNums(start, end, kind):
    numlist = {}
    for n in range(start, end + 1):
        if kind == 'tri':
            numlist[n] = triNum(n)
        elif kind == 'pent':
            numlist[n] = pentNum(n)
        elif kind == 'hex':
            numlist[n] = hexNum(n)
    return numlist
