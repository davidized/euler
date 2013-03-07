
# Retrieve the triangle file and create lists
input = open('triangle.txt')
filelines = input.readlines()
triangle = []

for line in filelines:
    line = line.rstrip()
    triangle.append(line.rsplit())

rows = len(triangle)-1 #We need the number of rows so we can start one row up
on_row = rows - 1

working_row = triangle[rows] #Row below the one we're working on (sums)

while on_row >= 0: #Step through rows

    item_pos = 0
    new_row = []
    for item in triangle[on_row]:

        adj1 = int(working_row[item_pos]) + int(item)
        adj2 = int(working_row[item_pos+1]) + int(item)

        new_row.append(max(adj1, adj2))
        item_pos += 1

    #print(on_row, ':\t', new_row)
    working_row = new_row
    on_row -= 1

print(working_row)
