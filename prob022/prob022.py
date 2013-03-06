import prob022func

# Retrieve the list, make list, sort alphabetically
input = open('names.txt')
filestring = input.read()
filestring = filestring[1:-1]
names = filestring.split("\",\"")
names.sort()

name_pos = 1
total = 0

for name in names:
    
    name_score = prob022func.name_score(name, name_pos)
    print(name, ": ", name_pos, ", ", name_score)

    total += name_score

    name_pos += 1

print(total)
