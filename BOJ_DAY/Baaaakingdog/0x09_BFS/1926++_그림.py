from collections import deque

n,m = list(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(x,y):
    area = 1
    q = deque()
    vis[x][y] = True
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx,ny))
                area += 1
    return area

cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not vis[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i,j))
            
print(cnt)
print(max_area)

