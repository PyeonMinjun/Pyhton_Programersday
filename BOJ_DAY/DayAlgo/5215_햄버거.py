def dfs(t, tas, cal):
    global l,n,res,ans
    
    if t == n:
        ans = max(ans,tas)
        return

    # res[t][1]
    if cal + res[t][1] <= l:
        dfs(t+1,tas + res[t][0], cal + res[t][1])

    dfs(t+1, tas, cal) # 
    
    
tc = int(input())

for _ in range(tc):

    n,l = map(int,input().split())

    res = []
    for _ in range(n):
        res.append(list(map(int,input().split())))
    ans = 0 

    dfs(0, 0, 0);
    print(ans)

    
    




