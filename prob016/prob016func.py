def sum_digits(num):
    num_str = str(num)
    num_sum = 0
    for i in num_str:
        num_sum += int(i)
    return num_sum
