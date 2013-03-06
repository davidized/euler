def n_even(n):
    return n / 2

def n_odd(n):
    return 3 * n + 1

def chain_len(start):
    n = start
    i = 1
    while n != 1:
        if n % 2 == 0:
            n = n_even(n)
        else:
            n = n_odd(n)
        i += 1

    return i
