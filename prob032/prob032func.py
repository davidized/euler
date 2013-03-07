def isPandigital(num, max):
    if len(str(num)) != max:
        return False
    
    for i in range(1, max + 1):

        if str(num).count(str(i)) != 1:
            return False

    return True
