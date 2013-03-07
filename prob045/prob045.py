import time
import prob045func

start = time.time()

maxn = 100000

#triNums = prob045func.listNums(1, maxn*100, 'tri')
pentNums = prob045func.listNums(1, maxn, 'pent')
hexNums = prob045func.listNums(1, maxn, 'hex')

#triNums = list(triNums.values())
pentNums = set(list(pentNums.values()))
hexNums = set(list(hexNums.values()))

#Ended up solving with interactive prompt using set(pentNums) & set(hexNums)
#Answer: 1533776805

#for hn in hexNums:
#    if pentNums.count(hn) > 0: # and triNums.count(hn) > 0:
#        print(hn)

#print(triNums, pentNums, hexNums)

print(pentNums & hexNums)
print("Executed In: ", time.time()-start)