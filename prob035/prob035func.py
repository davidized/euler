from math import sqrt

#Sieve of Eratosthenes
def primesBelow(n):
    primes = [2]
    #Setup list 3 to max, odds only
    for i in range(3, n):
        if i % 2 != 0:
            primes += [i]
    maxtest = int(sqrt(n)) + 1
    for j in range(3, maxtest):
        for k in primes:
            if k % j == 0 and k != j:
                primes.remove(k)

    return primes

def rotatenums(num):
    rotations = []
    numstr = str(num)
    for i in range(0, len(numstr)):
        newstr = numstr[i:] + numstr[0:i]
        rotations += [newstr]
    return rotations
