import sys

input = sys.stdin.readline
n = int(input())
ns = list(map(int,input().split()))
m = int(input())
ms = list(map(int,input().split()))


ns.sort() # 1 2 3 4 5
def d(target):
    st = 0
    en = len(ns)-1
    mid = (st + en) // 2
    
    while(st <= en):
        mid = (st+en) //2
        if ns[mid] < target:
            st = mid + 1
        elif ns[mid] > target:
            en = mid - 1
        else:
            return 1
    else:
        return 0
    

for i in ms:
    print(d(i))
        
        
    
    