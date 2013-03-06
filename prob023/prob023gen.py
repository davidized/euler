from prob023func import is_abundant

#List abundant numbers
count = 1
while count <= 28123:
    if is_abundant(count):
        print(count)

    count += 1
