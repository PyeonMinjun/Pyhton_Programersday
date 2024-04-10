from collections import deque

t = int(input())

board = [list(map(int,input())) for _ in range(t)]
dist = [[-1]* t for _ in range(t)]



q = deque()

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(t):
    for j in range(t):
        if board[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))

while q:
    area = 0
    x,y= q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= t or ny < 0 or ny >= t:
            continue
        
        if dist[nx][ny] >= 0:
            continue
        
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))
        
print(dist)