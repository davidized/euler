def factor(test):
    i = 1
    limit = test ** 0.5 # square root
    factors = []
    while i <= limit:
        if (test % i) == 0:
            inv = test / i
            factors.append(i)
            factors.append(inv)
        i = i + 1
    return factors
