from prob004func import is_palindrome

# Generate base 10 palindromes
i = 1
base10 = []
while i < 1000000:
    if is_palindrome(i):
        base10.append(i)

    i += 1

#print(base10)

# Check base 10 palindromes for plaindromes in base 2
base2 = []
for num in base10:
    test = bin(num)
    if is_palindrome(test[2:]):
        base2.append(num)

print(base2)
print(sum(base2))
    
