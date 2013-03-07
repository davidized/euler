from prob022func import name_number

# Retrieve the list, make list - maximum word score: 192
input = open('words.txt')
filestring = input.read()
filestring = filestring[1:-1]
words = filestring.split('","')

# Generate triangle numbers
t = 0
n = 1
triangle = []
while t < 192:
    t = 0.5 * n * (n + 1)
    triangle.append(t)
    #print(t)
    n += 1

# Go through the list, calculate score, check triangle numbers
counter = 0
for word in words:
    num = name_number(word) # Calculate score

    if triangle.count(num) > 0: # Check if triangle
        counter += 1

print(counter)
