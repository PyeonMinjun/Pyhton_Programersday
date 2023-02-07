n = int(input())
ns = list(map(int,input().split()))
sumn = int(input()) 

arr = [0] * (2000001)
cnt = 0

for i in ns:
    if arr[sumn - i]:
        cnt += 1
    else:
        arr[i] += 1

print(cnt)        