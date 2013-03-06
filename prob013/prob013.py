sum = 0

for line in open('prob013data'):
    sum += int(line)

print(sum)
sum = str(sum)
print('First ten: ', sum[:10])
