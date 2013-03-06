import prob017func

count = 1
sum = 0

while count <= 1000:
    
    sum += prob017func.to_word_num(count)
    
    count += 1

print(sum)
