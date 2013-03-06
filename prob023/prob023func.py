from prob012func import factor

def sum_unique_factors(num):
    factors = factor(num)
    factors.sort()
    sum_factors = 0
    prev = 0
    for i in factors:
        if i != num and i != prev:
            sum_factors += i
        prev = i

    return sum_factors

def is_abundant(num):
    if sum_unique_factors(num) > num:
        return True
    else:
        return False

#Don't need these, but they are smiple enough and may come in handy later
def is_deficient(num):
    if sum_unique_factors(num) < num:
        return True
    else:
        return False

def is_perfect(num):
    if sum_unique_factors(num) == num:
        return True
    else:
        return False
