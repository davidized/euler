import prob004func

a = 100
b = 100
largest = 0
largest_a = 0
largest_b = 0

while a <= 998:
    if b >= 1000:
        b = 100
        a += 1
    result = a * b
    if problem4func.is_palindrome(result):
        if result > largest:
            largest_a = a
            largest_b = b
            largest = result
            print(a, " * ", b, " = ", result, " LARGEST")
        else: 
            print(a, " * ", b, " = ", result)
    b += 1
print("Largest: ", a, " * ", b, " = ", largest)
