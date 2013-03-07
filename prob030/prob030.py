power = 5
count = 0
sumall = 0

for i in range(2, 354294): #Skip 1 per problem description
    istr = str(i)
    isum = 0
    for j in istr:
        isum += int(j) ** power

    if isum == i:
        count += 1
        sumall += i
        print(i)

print('Count: ', count, '\nSum: ', sumall)
