n = input()
ns = list(map(int,input().split()))
cnt = 0
res = 0 
ns.sort()


for i in ns:
    cnt += 1
    if i <= cnt:
        res += 1
        cnt = 0

print(res)