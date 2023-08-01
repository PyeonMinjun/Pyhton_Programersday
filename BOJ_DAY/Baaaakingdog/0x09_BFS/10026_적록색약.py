from collections import deque
n = int(input())

board = [list(input()) for _ in range(n)]

vis = [[0]* n for _ in range(n)]
vis2 = [[0]* n for _ in range(n)]

q1 = deque()

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(x,y):
    q1.append((x,y))
    vis[x][y] = 1
    while q1:
        x,y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if vis[nx][ny] == 1 or  board[x][y] != board[nx][ny]:
                continue
            vis[nx][ny] = 1
            q1.append((nx,ny))
    return

cnt = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            cnt += 1
            bfs(i,j)
            

for i in range(n):
    for j in range(n):
        if board[i][j] == "G":
            board[i][j] = "R"
        vis[i][j] = 0


for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            cnt2 += 1
            bfs(i,j)
               
            
print(cnt,cnt2)
