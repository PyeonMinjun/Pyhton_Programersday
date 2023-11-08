from collections import deque

m,n,h = list(map(int,input().split())) # m 세로 / n이 가로/ h 높이


# board = []
# for i in range(h):
#     board.append([list(map(int,input().split())) for _ in range(n)])

# dist = []
# for _ in range(h):
#     dist.append([[-1]*m for _ in range(n)])

board = [[list(map(int,input().split())) for i in range(n)] for _ in range(h)]
dist = [[[-1]* m for _ in range(n)] for _ in range(h)]

q = deque() 
dx = [0,-1,0,1,0,0]
dy = [-1,0,1,0,0,0]
dz = [0,0,0,0,-1,1] ## ?

for k in range(h):
    for i in range(n): # 3
        for j in range(m): # 5
            if board[k][i][j] == 1:
                q.append((k,i,j))
                dist[k][i][j] = 0

while q:
    z,x,y = q.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if nx < 0  or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
            continue
        
        if board[nz][nx][ny] == 0 and dist[nz][nx][ny] == -1:
            board[nz][nx][ny] = board[z][x][y] + 1
            q.append((nz,nx,ny))

mx = 0
flag = 1
for k in range(h):
    for i in range(n): # 3
        for j in range(m): # 5
            if board[k][i][j] == 0:
                flag = 0
            else:
                mx = max(board[k][i][j],mx)

if not flag:
    print(-1)
else:
    print(mx-1)
