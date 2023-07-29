from collections import deque
t = int(input())
def bfs(x,y):
    area = 1
    q =  deque()
    vis[x][y] = True
    q.append((x,y)) 
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx,ny))
                area += 1
    return area
        
        
        
for i in range(t):
    m,n,k = map(int,input().split())

    board = [[0] * n for _ in range(m)]
    vis = [[False] * n for _ in range(m)]

    for _ in range(k):
        a,b = map(int,input().split())
        board[a][b] = 1
        

    dx = [0,-1,0,1]
    dy = [-1,0,1,0]


    cnt_board = 0
    max_area = 0

    for o in range(m):
        for p in range(n):
            if board[o][p] == 1 and not vis[o][p]:
                bfs(o,p)
                cnt_board += 1
            
    print(cnt_board)
