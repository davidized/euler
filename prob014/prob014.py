from time import time
import prob014func

starttime = time()

start = 1
max_len = 0
max_start = 0

#while start <= 1000000:
for i in range(1, 1000000):    
    #chain_len = prob014func.chain_len(start)
    chain_len = prob014func.chain_len(i)
    if chain_len > max_len:
        max_len = chain_len
        #max_start = start
        max_start = i
    #print(start, " produces ", chain_len, " terms")

    start += 1

print("Max length produced from: ", max_start)
print("Executed in: ", time() - starttime)
