import sys
input=  sys.stdin.readline
n,m = map(int,input().split())


ns = set()
ms = set()
for _ in range(n):
    ns.add(input().rstrip())

for _ in range(m):
    ms.add(input().rstrip())

cnt = 0

result = sorted(list(ns & ms))

print(len(result))

for i in result:
    print(i)