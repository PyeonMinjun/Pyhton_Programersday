n,m,v = map(int,input().split())
board = [[False] * (n+1) for _ in range(n+1)]
isused = [False] * (n+1)


for _ in range(m):
    x,y = map(int,input().split())
    board[x][y] = True
    board[y][x] = True


def dfs(v):
    print(v,end =" ")
    isused[v] = True
    for i in range(1,n+1):
        if not isused[i] and board[v][i]== True:
            dfs(i)

dfs(v)