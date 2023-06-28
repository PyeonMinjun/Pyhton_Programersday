# 이분탐색으로 풀이
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

ns = sorted([input().rstrip() for i in range(n)])
ms = sorted([input().rstrip() for j in range(m)])


def d(target):
    st = 0
    en = n-1
    
    while(st <= en ):
        mid = (st + en ) // 2
        if ns[mid] == target:
            return 1
        if ns[mid] < target:
            st = mid + 1
        elif ns[mid] > target:
        # else:
            en = mid - 1
    return 0

res = []
for i in ms:
    if d(i):
       res.append(i)

print(len(res))
for i in res:
    print(i)     

        

for i in ms:
    d(i)
        
            

