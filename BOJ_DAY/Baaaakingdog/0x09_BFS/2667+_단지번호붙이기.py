from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dist = [[False] * n for _ in range(n)]
res = []



q = deque()

dx = [-1,0,1,0]
dy = [0,-1,0,1]

rcnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and dist[i][j]== False:
            q.append((i,j))
            dist[i][j] = True
            rcnt += 1
    
        cnt = 1

        if q:
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n :
                        continue

                    if board[nx][ny] == 0 or dist[nx][ny] == True:
                        continue

                    dist[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1

            res.append(cnt)


print(rcnt)

res.sort()
for i in res:
    print(i)    
    
        