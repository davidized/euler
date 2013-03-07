
masterlist = []

for a in range(2, 101):

    for b in range(2, 101):

        masterlist += [a ** b]
        #print(a, ' ** ', b, ' = ', a**b)

masterlist.sort()
#print(masterlist)

uniquelist = []

for item in masterlist:
    if uniquelist.count(item) == 0:
        uniquelist += [item]

#print(uniquelist)
print(len(uniquelist))
