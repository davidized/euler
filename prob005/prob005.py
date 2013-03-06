upto = 20
i = 1
maximum = 1
while i <= upto:
    maximum = maximum * i
    i += 1

print("Maximum: ", maximum)
i = 1
success = False
while i < maximum:
    status = "Testing: " + repr(i) + ": "
    t = 1
    while t <= upto:
        if i % t == 0:
            status += repr(t) + " "
            if t == upto:
                status += " PASSED"
                success = True
            t += 1
        else:
            status += " FAILED"
            break

    print(status)

    if success == True:
        exit()
    elif i == 1: # We don't need to check every number
        i += 720719
    else:
        i += 720720
    
