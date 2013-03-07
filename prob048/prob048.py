
count = 1
sum = 0
while count <= 1000:
    sum += count ** count
    count += 1

sum_str = str(sum)
sub_str = sum_str[-10:]

print(sub_str)
