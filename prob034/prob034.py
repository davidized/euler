from math import factorial

i = 3
sum = 0
while i < 100000:

    i_str = str(i)
    sub_sum = 0
    for j in i_str:
        j = int(j)
        sub_sum += factorial(j)

    if sub_sum == i:
        sum += i
        print(i)

    i += 1

print("Sum: ", sum)
