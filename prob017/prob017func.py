def to_word(num):
    if num > 9999: exit("Error! Too big to convert")

    thousands = int(num / 1000)
    hundreds = int((num % 1000) / 100)
    tens = int((num % 100) / 10)
    ones = int(num % 10)

    word = ""

    if thousands > 0:
        word += word_ones(thousands) + " thousand "

    if hundreds > 0:
        word += word_ones(hundreds) + " hundred "

    if  tens > 0:
        if thousands > 0 or hundreds > 0:
            word += "and "

        if tens == 1:
            word += word_teens(ones)
        else:
            word += word_tens(tens) + " "
    
    if ones > 0 and tens > 1:
        word += word_ones(ones)

    if ones > 0 and tens == 0:
        if thousands > 0 or hundreds > 0:
            word += "and "

        word += word_ones(ones)

    #print(word)
    return word

def word_ones(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    else:
        return "zero"

def word_tens(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "twenty"
    elif num == 3:
        return "thirty"
    elif num == 4:
        return "forty"
    elif num == 5:
        return "fifty"
    elif num == 6:
        return "sixty"
    elif num == 7:
        return "seventy"
    elif num == 8:
        return "eighty"
    elif num == 9:
        return "ninety"
    else:
        return "zero"

def word_teens(num):
    if num == 1:
        return "eleven"
    elif num == 2:
        return "twelve"
    elif num == 3:
        return "thirteen"
    elif num == 4:
        return "fourteen"
    elif num == 5:
        return "fifteen"
    elif num == 6:
        return "sixteen"
    elif num == 7:
        return "seventeen"
    elif num == 8:
        return "eighteen"
    elif num == 9:
        return "nineteen"
    else:
        return "ten"

def to_word_num(num):
    if num > 9999: exit("Error! Too big to convert")

    thousands = int(num / 1000)
    hundreds = int((num % 1000) / 100)
    tens = int((num % 100) / 10)
    ones = int(num % 10)

    word = 0

    if thousands > 0:
        word += word_ones_num(thousands) + 8 #thousand

    if hundreds > 0:
        word += word_ones_num(hundreds) + 7 #" hundred "

    if  tens > 0:
        if thousands > 0 or hundreds > 0:
            word += 3 #"and "

        if tens == 1:
            word += word_teens_num(ones)
        else:
            word += word_tens_num(tens) # + " "
    
    if ones > 0 and tens > 1:
        word += word_ones_num(ones)

    if ones > 0 and tens == 0:
        if thousands > 0 or hundreds > 0:
            word += 3 #"and "

        word += word_ones_num(ones)

    #print(word)
    return word

def word_ones_num(num):
    if num == 1:
        return 3 #"one"
    elif num == 2:
        return 3 #"two"
    elif num == 3:
        return 5 #"three"
    elif num == 4:
        return 4 #"four"
    elif num == 5:
        return 4 #"five"
    elif num == 6:
        return 3 #"six"
    elif num == 7:
        return 5 #"seven"
    elif num == 8:
        return 5 #"eight"
    elif num == 9:
        return 4  #"nine"
    else:
        return 4 #"zero"

def word_tens_num(num):
    if num == 1:
        return 3 #"one"
    elif num == 2:
        return 6 #"twenty"
    elif num == 3:
        return 6 #"thirty"
    elif num == 4:
        return 5 #"forty"
    elif num == 5:
        return 5 #"fifty"
    elif num == 6:
        return 5 #"sixty"
    elif num == 7:
        return 7 #"seventy"
    elif num == 8:
        return 6 #"eighty"
    elif num == 9:
        return 6 #"ninety"
    else:
        return 4 #"zero"

def word_teens_num(num):
    if num == 1:
        return 6 #"eleven"
    elif num == 2:
        return 6 #"twelve"
    elif num == 3:
        return 8 #"thirteen"
    elif num == 4:
        return 8 #"fourteen"
    elif num == 5:
        return 7 #"fifteen"
    elif num == 6:
        return 7 #"sixteen"
    elif num == 7:
        return 9 #"seventeen"
    elif num == 8:
        return 8 #"eighteen"
    elif num == 9:
        return 8 #"nineteen"
    else:
        return 3 #"ten"
