n = int(input())
ns = list(map(int,input().split()))


ns.sort()
target = 1

for i in ns:
    if target < i:
        break
    target += i

print(target)