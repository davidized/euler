import prob011func

mx = prob011func.matrix()
i = 0 #row position
j = 0 #col position
curpos = {0: 0}

greatest = 0
position = {0: 0}

prod_f = prod_d = prod_df = prod_db = 0

rows = len(mx)

for row in mx:
    cols = len(row)
    for col in row: #looping through every position in the matrix
        curpos = {i: j}
        prod_f = prod_d = prod_df = prod_db = -1
        #horizontal forward [i][j+]
        if j + 3 < cols:
            prod_f = mx[i][j] * mx[i][j+1] * mx[i][j+2] * mx[i][j+3]

            if prod_f > greatest:
                greatest = prod_f
                position = curpos

        #vertical down [i+][j]
        if i + 3 < rows:
            prod_d = mx[i][j] * mx[i+1][j] * mx[i+2][j] * mx[i+3][j]
 
            if prod_d > greatest:
                greatest = prod_d
                position = curpos

        #diagonal down-forward [i+][j+]
        if i + 3 < rows and j + 3 < cols:
            prod_df = mx[i][j] * mx[i+1][j+1] * mx[i+2][j+2] * mx[i+3][j+3]

            if prod_df > greatest:
                greatest = prod_df
                position = curpos

        #diagonal down-backward [i+][j-]
        if i + 3 < rows and j - 3 >= 0:
            prod_db = mx[i][j] * mx[i+1][j-1] * mx[i+2][j-2] * mx[i+3][j-3]
        
            if prod_db > greatest:
                greatest = prod_db
                position = curpos

        print(curpos, ":\t", prod_f, ",\t", prod_d, ",\t", prod_df, ",\t", prod_db)

        j += 1 #increment column position
        
    #print("G: ", greatest, "P: ", position, "D: ", direction)
    input()
    i += 1 #increment row position
    j = 0 #reset column position

print("Greatest: ", greatest)
print("Position: ", position)
