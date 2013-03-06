from math import sqrt
import prob009func

a = 1
b = 2
c = 0
sum = 0
answer = 0

while a < 1000:
    b = a
    while b < 1000:
        cSq = a * a + b * b

        if prob009func.is_square(cSq):
            c = sqrt(cSq)
            sum = a + b + c
            print("a: ", a, " b: ", b, " c: ", c, " Sum: ", sum)

            if sum == 1000:
                answer = a * b * c

        b += 1
    a += 1

print(answer)
