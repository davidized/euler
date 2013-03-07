size = 0

i1 = 1
i2 = 1
i3 = 0
count = 2 # Start at 2 because we've already set i1 and i2
while size < 1000:
    i3 = i1 + i2
    size = len(str(i3))
    i1 = i2
    i2 = i3
    count += 1

print(count)
