def dfs(depth,start, tas, cal,i):
    global overcalorie,res

    if depth == i:
        res = max(res,tas)
        return

    for j in range(start,cnt):
        if cal+ board[j][1] <= overcalorie:
            dfs(depth+1, j+1, tas + board[j][0] ,cal + board[j][1],i )


t = int(input())
for tc in range(t):
    cnt, overcalorie = list(map(int,input().split()))
    # arr = [0] *  (cnt +1)
    res  = 0
    board = [list(map(int,input().split())) for _ in range(cnt)]
    for i in range(1,cnt+1):
        dfs(0,0,0,0,i)
    print("#{} {}" .format(tc+1,res))

# 먼가 잘못된건 알겠는데 , 어디서 잘 못된지 모르겠다 .
# 조합에서 for문을 돌며 가능한 모든 경우의 수를 구해야하는게 아닌가 
# 