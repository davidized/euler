
def is_palindrome(test):
    teststr = str(test)
    length = len(teststr)
    count = 0
    ending = length - 1
    first = int(teststr[count])
    last = int(teststr[ending])

    if length == 1:
        return True

    while count <= ending:
        if first != last:
            return False
        count += 1
        ending -= 1
        first = int(teststr[count])
        last = int(teststr[ending])

    return True
