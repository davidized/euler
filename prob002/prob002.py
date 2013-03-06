i1 = 1
i2 = 1
i3 = 0
sum = 0
while (i3 < 4000000):
    i3 = i1 + i2
    if (i3 % 2) == 0:
        sum = sum + i3
    i1 = i2
    i2 = i3
print(sum)
