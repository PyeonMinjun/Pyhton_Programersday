from itertools import *


n = int(input())
coins = list(map(int,input().split()))

arr = [0]* 1001

for i in coins:
    arr[i] += 1
    
for i in range(2,n):
    for j in list(combinations(coins,i)):
        total = 0
        for k in j:
            total += k
        arr[total] += 1

print(arr)
print(arr.index(0,1)) 

    





