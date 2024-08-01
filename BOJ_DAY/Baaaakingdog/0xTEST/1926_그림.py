from collections import deque
n,m  = list(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(n)]
dis = [ [False] * m for _ in range(n)]

q = deque()

dx =[0,-1,0,1]
dy =[-1,0,1,0]
res = []
flag = False
rnct = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            flag = True




for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and dis[i][j] == False:
            q.append((i,j))
            dis[i][j] = True
            cnt = 1
            
            while q:
                x,y = q.popleft()
                for o in range(4):
                    nx = x + dx[o]
                    ny = y + dy[o]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    
                    if board[nx][ny] == 1 and dis[nx][ny] == False:
                        cnt += 1 
                        q.append((nx,ny))
                        dis[nx][ny] = True
            res.append(cnt)
            rnct += 1
            
if not flag:
    print(0)
    print(0)
    exit(0)
else:
    print(rnct)
    print(max(res))
         







    

