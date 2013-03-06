from prob023func import is_abundant

# List of abundant numbers
count = 1
abundant = []
while count <= 28123:
    if is_abundant(count):
        abundant.append(count)
    
    count += 1

#print(abundant)
print('Abundants generated')
abundant = tuple(abundant)

# Test positive integers
count = 1
total = 0
while count <= 28123:
    print('Testing: ', count)

    for i in abundant:
        print('\twith: ', i)
        check = count - i
        if abundant.count(check) != 0:
            break

        if i > count * 0.5:
            total += count
            break

    count += 1

print(total)
