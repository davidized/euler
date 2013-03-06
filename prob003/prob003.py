def is_prime(test):
    factors = factor(test)
    if len(factors) == 0:
        return True
    else:
        return False


def factor(test):
    #print("Factoring ", test)
    i = 2
    limit = test ** 0.5 # square root
    factors = []
    while i <= (limit):
        if (test % i) == 0:
            #print("\tFactor: ", i)
            factors.append(i)
        #print("\tTried: ", i)
        if i == 2:                      # Now we will only test 2 and odds
            i = i + 1
        else:
            i = i + 2
    return factors

test = int(input())
factors = factor(test)
print(factors)

for f in factors:
    #print(f)
    if is_prime(f):
        #print(" is prime\n")
        print(f)
    #else:
        #print(" is not prime\n")
