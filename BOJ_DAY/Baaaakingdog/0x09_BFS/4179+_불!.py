from collections import deque
n,m = (map(int,input().split()))

board = [(input()) for _ in range(n)]

dist1 = [[-1]* m for _ in range(m)]
dist2 = [[-1]* m for _ in range(m)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

q1 = deque()
q2 = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == "F":
            q1.append((i,j))
            dist1[i][j] = 0
        
        elif board[i][j] == "J":
            q2.append((i,j))
            dist2[i][j] = 0
            

while q1:
    x,y = q1.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny <0 or ny >= m:
            continue
        if board[nx][ny] == "#" or dist1[nx][ny] >= 0:
            continue
        dist1[nx][ny] = dist1[x][y] + 1
        q1.append((nx,ny))

while q2:
    x,y = q2.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny <0 or ny >= m:
            print(dist2[x][y]+1)
            print(dist1)
            print(dist2)
    
            exit(0)
        
        if board[nx][ny] == "#" or dist2[nx][ny] >= 0 or board[nx][ny] == "F":
            continue
        
        if dist1[nx][ny] <= dist2[x][y]+1:
            continue
        # if dist1[nx][ny] > dist2[x][y]+1:
        dist2[nx][ny] = dist2[x][y] + 1
        q2.append((nx,ny))
else:
    print("IMPOSSIBLE")

    

print(dist1)
print(dist2)
    
    
            