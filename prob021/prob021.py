import prob021func

count = 0
sum_amicables = 0

while count < 10000:
    if prob021func.is_amicable(count) and prob021func.sum_factors(count) !=count:
        sum_amicables += count
        print(count)
    count += 1

print("Sum: ", sum_amicables)
