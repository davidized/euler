import math

def isPentagonal(x):
    n = (math.sqrt(24*x+1)+1)/6
    #Equation from wikipedia

    if n == int(n):
        return True
    else:
        return False
