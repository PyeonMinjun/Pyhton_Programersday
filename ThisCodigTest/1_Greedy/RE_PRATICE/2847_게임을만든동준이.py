n= int(input())
ns = [int(input()) for _ in range(n)]

ns = list(reversed(ns))
prev = ns[0]
cnt = 0

for i in range(1,n):
    if prev <= ns[i]:
        cnt += ns[i] - prev + 1
        ns[i] = prev - 1
    prev = ns[i] 
print(cnt)
        
        
        
    