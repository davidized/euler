from prob012func import factor

def sum_factors(num):
    factors = factor(num)
    sum_factors = 0
    for i in factors:
        if i != num:
            sum_factors += i

    return sum_factors

def is_amicable(num):
    num2 = sum_factors(num)

    if sum_factors(num2) == num:
        return True
    else:
        return False
