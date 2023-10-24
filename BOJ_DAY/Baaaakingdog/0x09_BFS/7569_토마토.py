from collections import deque
n,m,h= map(int, input().split())
dx = [-1,0,0,1,0,0]
dy = [0,-1,0,0,1,0]
dz = [0,0,-1,0,0,1]
q = deque()

board =  [[list(map(int,input().split())) for _ in range(m)] for _ in range(h)]
dist =  [[[0] * n for _ in range(m)] for _ in range(h)]
# board =[]

# for i in range(h):
#     board.append(  [list(map(int,input().slit())) for _ in range(m)])

for i in range(h): # 1
    for j in range(m): # 3
        for k in range(n): # 5
            if board[i][j][k]== 1:
                q.append((k,j,i))
                
            if board[i][j][k] == 0:
                dist[i][j][k] = -1

while q:
    x,y,z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
            continue
        if dist[nz][ny][nx] >= 0:
            continue
        
        dist[nz][ny][nx] = dist[z][y][x] + 1
        q.append((nx,ny,nz))
        
max_borad = 0
print(dist)

for i in range(h):
    for j in range(m):
        for k in range(n):
            if dist[i][j][k] == -1:
                print(-1)
                exit(0)
                
            max_borad = max(max_borad,dist[i][j][k])


print(max_borad)