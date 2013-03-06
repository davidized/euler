upto = int(input("Test up to: "))
i = 1
maximum = 1
while i <= upto:
    maximum = maximum * i
    i += 1
print("Maximum: ", maximum)

i = 1
success = False
incr = 2 #Start at 2, only test even numbers
factor = 2

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
            status += " FAILED "
            if t > factor:
                factor = t
                incr = i
                status += repr(incr)
            break

    print(status)

    if success == True:
        exit()
    elif i == 1: # We don't need to check every number
        i += 1
    else:
        i += incr
    
