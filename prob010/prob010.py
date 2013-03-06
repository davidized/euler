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

maximum = int(input("Maximum: "))
count = 2
sum = 0

while count <= maximum:
    print("Test: ", count)
    if is_prime(count):
       sum = sum + count
       print("Prime: ", count, "; Sum: ", sum)

    if count == 2:
        count += 1
    else:
        count += 2
