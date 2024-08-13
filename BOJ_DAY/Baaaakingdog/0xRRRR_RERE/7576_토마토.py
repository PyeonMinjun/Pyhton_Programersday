from collections import deque
n,m = list(map(int,input().split()))
board=  [list((map(int,input().split()))) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]


q= deque()
# 1인 토마토를 큐에 넣는다. 
# dist배열에도 넣는다.

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            dist[i][j] = 1
            q.append((i,j))


        if board[i][j] == -1:
            dist[i][j] = 0


while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]

        if nx < 0 or nx >= m or  ny < 0  or ny >= n:
            continue

        if dist[nx][ny] >= 0 or board[nx][ny] == -1:
            continue  

        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))

mx = -1
flag = True

for i in range(m):
    for j in range(n):
        if dist[i][j] == -1:
            flag = False
        mx = max(mx,dist[i][j])

if flag:
    print(mx-1)
else:
    print(-1)    






        