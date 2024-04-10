T = int(input())

for tc in range(1,T+1):
    n,m = (map(int,input().split()))
    ns = []
    for i in range(n):
        ns.append(list(map(int,input().split())))
    ans = 0
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for ci in range(i, i+m):
                for cj in range(j,j+m):
                    cnt += ns[ci][cj]
            if ans < cnt:
                ans = cnt
    print("#{} {}" .format(tc,ans))