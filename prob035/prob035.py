# Did not solve with program, accidentally found answer while researching circular primes

import prob035func

maximum = 1000000

primes = prob035func.primesBelow(maximum)
print('Sieve completed')

notCircPrimes = []

print(primes)

for i in primes: #Go through each prime
    rotations = prob035func.rotatenums(i)
    print('Testing: ', i, ' rotations ', rotations)
    for j in rotations: #Go through rotations to check circular
        print('\trot: ', j)
        if primes.count(int(j)) == 0: #If not on prime list, not circular
            print('\t\t', j, ' Not Prime')
            notCircPrimes += [i]

for i in notCircPrimes:
    primes.remove(i)

#print(primes)
print(len(primes))
