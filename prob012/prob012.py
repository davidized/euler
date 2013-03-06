from prob012func import factor

count = 1

while count < 1000000:
    i = 1
    sum = 0
    while i <= count:
        sum += i
        i += 1

    length = len(factor(sum))
    print(count, ", ", sum, ", ", length)
    
    if (length >= 500): 
        print(factor(sum))
        exit()

    count += 1

#1+2
#1+2+3
