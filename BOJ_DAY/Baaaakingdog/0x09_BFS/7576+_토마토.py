from collections import deque
n, m = (map(int,input().split()))

board = [list(map(int,input().split())) for i in range(m)]
dist = [[0]*n for _ in range(m)]


q = deque()
dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(m):
    for j in range(n):
        
        if board[i][j] == 1:
            q.append((i,j))
        
        elif board[i][j] == -1:
            dist[i][j] = -1
            

while q:
    x,y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= m or ny <0 or ny >= n:
            continue
        if board[nx][ny] == 0 and dist[nx][ny] >= 0:
            board[nx][ny] = board[x][y] + 1
            q.append((nx,ny))
            

mx_val = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        mx_val = max(mx_val,board[i][j])
        
        
        
print(mx_val-1)