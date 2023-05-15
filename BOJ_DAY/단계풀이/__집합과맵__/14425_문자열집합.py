n,m = map(int,input().split())

ns = []
ms = []

cnt = 0
for _ in range(n):
    ns.append( input())
    
for _ in range(m):
    ms.append( input())

for k in ms:
    if k in ns:
        cnt += 1

print(cnt)