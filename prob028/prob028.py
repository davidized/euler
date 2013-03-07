
sumDiags = 0

spiralsize = 1001

for i in range(spiralsize, 0, -1):

    if i % 2 == 0: continue #Skip evens, matrix reduces by 2 each time

    cornerTR = i * i              # TL    TR
    cornerTL = cornerTR - (i - 1) #
    cornerBL = cornerTL - (i - 1) #
    cornerBR = cornerBL - (i - 1) # BL    BR

    print(cornerTR, cornerTL, cornerBL, cornerBR)

    if i == 1: #Special case for middle number, otherwise we add 4
        sumDiags += 1
    else:
        sumDiags += (cornerTR + cornerTL + cornerBL + cornerBR)

print(sumDiags)
