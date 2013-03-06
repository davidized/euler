sumsquares = 0
i = 1

while i <= 100:
    sumsquares = sumsquares + (i * i)

    i = i + 1

j = 1
sum = 0
while j <= 100:
    sum = sum + j

    j = j + 1

#print("Sum: ", sum)

squaresum = sum * sum
diff = squaresum - sumsquares

print("Sum of squares: ", sumsquares)
print("Square of sum: ", squaresum)
print("Difference: ", diff)
