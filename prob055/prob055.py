import prob055func

i = 10
count = 0

while i <= 10000:

    if prob055func.isLychrel(i, 50):
        print(i)
        count += 1

    i += 1

print(count)
