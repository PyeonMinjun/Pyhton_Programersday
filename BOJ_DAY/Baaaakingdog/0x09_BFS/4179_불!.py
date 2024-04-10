from collections import deque

n,m = map(int,input().split())


board =  [list(input()) for _ in range(n)]
dist  = [[-1] * m for _ in range(n)]
dist2 = [[-1] * m for _ in range(n)]

q = deque()
q2 = deque()

dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(n):
    for j in range(m):
        if board[i][j] == "F":
            q.append((i,j))
            dist[i][j] = 0
            
        if board[i][j] == "J":
            q2.append((i,j))
            dist2[i][j] = 0

# 불에 대한 BFS
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny <0 or ny >= m:
            continue
        if dist[nx][ny] >= 0 or board[nx][ny] == "#":
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))

print(dist)
while q2:
    x,y = q2.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            print(dist2[x][y]+1)
            exit(0)
            
        if dist2[nx][ny] >= 0 or board[nx][ny] == "#":
            continue
        
        if dist[nx][ny] != -1 and dist[nx][ny] <= dist2[x][y]+ 1:
            continue
        dist2[nx][ny] = dist2[x][y] + 1
        q2.append((nx,ny))

else:
    print("IMPOSSIBLE")
