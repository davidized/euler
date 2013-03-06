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

upto = int(input("Find prime: "))
count = 0
incr = 1

while count <= upto:
    if is_prime(incr):
        status = "Prime " + repr(count) + " is " + repr(incr)
        print(status)
        count += 1
    incr += 1
