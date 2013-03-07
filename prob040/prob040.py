number = ''
count = 1

while len(number) <= 1000001:
    number += str(count)
    count += 1

answer = int(number[0]) * int(number[9]) * int(number[99]) * int(number[999]) * int(number[9999]) * int(number[99999]) * int(number[999999])
print(int(number[0]), int(number[9]), int(number[99]), int(number[999]), int(number[9999]), int(number[99999]), int(number[999999]))
print(answer)
