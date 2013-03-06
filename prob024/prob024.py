from itertools import permutations

result = permutations('0123456789')

count = 1

for i in result:
    print(count, ':\t', i)
    if count == 1000000: break
    count += 1
