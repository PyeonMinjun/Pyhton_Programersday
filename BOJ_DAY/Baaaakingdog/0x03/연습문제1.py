n = int(input())
ns = list(map(int, input().split()))
cnt = 0

x= 1

for i in ns:
    xs = ns[x:]
    for j in xs:
        if i + j == 100:
            cnt += 1
    x += 1 
print(cnt)


