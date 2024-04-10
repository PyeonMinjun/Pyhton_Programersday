import sys
input = sys.stdin.readline

n = int(input())
ns = list(map(int,input().split()))
m = int(input())
ms = list(map(int,input().split()))


ns.sort()
def low_d(target):
    st = 0
    en = n  # en의 시작점이 ns의 길이값
    
    while(st < en):
        mid = (st + en ) // 2
        if ns[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st
        
def upper_d(target):
    st = 0
    en = n
    while (st < en):
        mid = ( st + en ) // 2
        if ns[mid] > target:
            en = mid
        else:
            st = mid + 1
    return st
        
    
    
arr = []
for i in ms:
    arr.append(upper_d(i)- low_d(i))

print(" ".join(map(str,arr)))
    

