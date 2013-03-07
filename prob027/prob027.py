from time import time
from prob035func import primesBelow

start = time()

primes = primesBelow(1000)
answer = { 'a': 0, 'b': 0, 'product': 0, 'count': 0}

for a in range(-1000, 1000):
    #print('a: ', a)
    for b in range(-1000, 1000):
        #print('b: ', b)
        n = 0
        while True:
            sol = n * n + a * n + b
            if primes.count(sol) == 0:
                break;
                            
            n += 1

        if n > answer['count']:
            answer = { 'a': a, 'b': b, 'product': a * b, 'count': n}
            print(answer)

print(answer)

print("Excecuted in: ", time()-start)
