t = int(input())
ns = [list(map(int,input().split())) for _ in range(t)]
ans = []

for i in range(t):
    cnt = 0
    for j in range(t):
        if ns[i][0] < ns[j][0] and ns[i][1] < ns[j][1]: 
            cnt += 1
    ans.append(cnt+1)

for i in ans:
    print(i, end=" ")