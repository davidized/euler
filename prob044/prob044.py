import time
import prob044func
import prob045func

start = time.time()

pentNums = prob045func.listNums(1, 10000, 'pent')

pentNums = list(pentNums.values())

for x in pentNums:
    for y in pentNums:
        if y > x: break
        diff = x - y
        sum = x + y

        if prob044func.isPentagonal(diff) and prob044func.isPentagonal(sum):
            print('x: ', x, ' y: ', y, ' sum: ', sum, ' diff: ', diff, time.time()-start)

print("Executed in: ", time.time()-start)