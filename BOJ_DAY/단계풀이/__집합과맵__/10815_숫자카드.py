import sys


n = int(input())
ns = list(map(int,input().split()))

m = int(input())
ms = list(map(int,input().split()))

res = {}

for i in range(n):
   res[ns[i]] = 0
   
for j in range(m):
    if ms[j] in res:
        print(1 ,end = " ")
    else:
        print(0, end = " ")