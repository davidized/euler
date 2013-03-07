from prob004func import is_palindrome

def revNum(num):
    numstr = str(num)
    length = len(numstr)
    pos = length - 1 #Position in the number, start at end
    
    newstr = ''

    while pos >= 0:
        newstr += numstr[pos]

        pos -= 1

    newnum = int(newstr)
    return newnum

def isLychrel(num, maxitr):

    count = 1
    while count <= maxitr:

        total = num + revNum(num)

        if is_palindrome(total):
            return False
        
        count += 1
        num = total
    return True
